#!/usr/bin/env python3
"""
Directed Single-Source Shortest Paths benchmark

Compares:
- Classic Dijkstra with a binary heap (heapq)
- Integer-weight optimized Dijkstra using a Radix Heap (monotone PQ)

Notes on the paper "Breaking the Sorting Barrier for Directed Single-Source Shortest Paths" (https://arxiv.org/abs/2504.17033):
- The paper shows how to bypass comparison-based sorting bottlenecks for directed SSSP.
- In practice, bucketed or radix-like priority queues for non-negative integer weights
  can significantly outperform binary heaps by avoiding O(log n) comparisons per op.
- Here we implement a practical Radix Heap variant suitable for Dijkstra where keys
  (extracted distances) are non-decreasing. This aligns with the paper's sort-free
  spirit and is commonly faster on integer-weight graphs.

This script generates random directed graphs with non-negative integer weights and
benchmarks both algorithms end-to-end as true SSSP (distances from a single source
to all vertices), validates correctness, and reports timing and speedups.
"""

from __future__ import annotations

import argparse
import math
import random
import sys
import time
from dataclasses import dataclass
from typing import List, Tuple, Iterable, Optional

import heapq


# -----------------------------
# Graph utilities
# -----------------------------

Adj = List[List[Tuple[int, int]]]  # adjacency list: u -> list of (v, w), w >= 0 integer


def generate_random_digraph(n: int, m: int, max_w: int, seed: Optional[int] = None) -> Adj:
    """
    Generate a random directed graph with n nodes and m edges.
    Weights are integers in [0, max_w] (0 allowed). No multiple-edge suppression.
    """
    if n <= 0:
        raise ValueError("n must be > 0")
    if m < 0:
        raise ValueError("m must be >= 0")
    if max_w < 0:
        raise ValueError("max_w must be >= 0")

    rnd = random.Random(seed)
    adj: Adj = [[] for _ in range(n)]
    for _ in range(m):
        u = rnd.randrange(n)
        v = rnd.randrange(n)
        # allow self-loops; Dijkstra handles non-negative weights fine
        w = rnd.randrange(max_w + 1)
        adj[u].append((v, w))
    return adj


# -----------------------------
# Classic Dijkstra (binary heap)
# -----------------------------

def dijkstra_binary_heap(adj: Adj, src: int) -> List[float]:
    """
    Single-source shortest paths for non-negative weights using heapq.
    Returns distances array of length n (float('inf') for unreachable).
    """
    n = len(adj)
    dist = [math.inf] * n
    dist[src] = 0.0
    visited = [False] * n
    pq: List[Tuple[float, int]] = [(0.0, src)]

    while pq:
        d, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        # Early exit if all remaining are inf (optional micro-optimization)
        # if d == math.inf: break
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist


# -----------------------------
# Radix Heap for monotone integer keys
# -----------------------------

@dataclass
class _Item:
    key: int
    val: int


class RadixHeap:
    """
    Radix Heap priority queue for non-decreasing extract-min keys (monotone queue).
    Based on the classic implementation using buckets indexed by msb(key ^ last).

    - push(key:int, val)
    - pop() -> (key, val)
    - not monotone keys will break invariants (use only where extract-min keys are non-decreasing)

    Bucket count: 1 + max_bits, where max_bits=64 by default (supports 64-bit distances).
    """

    __slots__ = ("_buckets", "_last", "_size", "_max_bits")

    def __init__(self, max_bits: int = 64) -> None:
        self._max_bits = max_bits
        self._buckets: List[List[_Item]] = [[] for _ in range(max_bits + 1)]
        self._last = 0
        self._size = 0

    def __len__(self) -> int:
        return self._size

    @staticmethod
    def _idx(x: int) -> int:
        # index is bit_length; bit_length(0) == 0 maps to bucket 0
        return x.bit_length()

    def push(self, key: int, val: int) -> None:
        if key < self._last:
            raise ValueError("RadixHeap requires monotone non-decreasing keys")
        idx = self._idx(key ^ self._last)
        self._buckets[idx].append(_Item(key, val))
        self._size += 1

    def _pullup(self) -> None:
        # Find smallest non-empty bucket with index > 0
        i = 1
        while i <= self._max_bits and not self._buckets[i]:
            i += 1
        if i > self._max_bits:
            return  # nothing to do
        # New last is the minimum key in bucket i
        new_last = min(it.key for it in self._buckets[i])
        # Redistribute bucket i into lower buckets using new_last
        for it in self._buckets[i]:
            idx = self._idx(it.key ^ new_last)
            self._buckets[idx].append(it)
        self._buckets[i].clear()
        self._last = new_last

    def pop(self) -> Tuple[int, int]:
        if self._size == 0:
            raise IndexError("pop from empty RadixHeap")
        if not self._buckets[0]:
            self._pullup()
        # Now bucket 0 must be non-empty
        b0 = self._buckets[0]
        # Find min in bucket 0 (keys there are equal to self._last, but keep safe)
        min_idx = 0
        min_key = b0[0].key
        for i in range(1, len(b0)):
            if b0[i].key < min_key:
                min_key = b0[i].key
                min_idx = i
        it = b0.pop(min_idx)
        self._size -= 1
        # Maintain last as the key we just popped (monotone non-decreasing)
        if it.key < self._last:
            # Should not happen; safety check
            self._last = it.key
        else:
            self._last = it.key
        return it.key, it.val


def dijkstra_radix_heap(adj: Adj, src: int) -> List[int]:
    """
    Single-source shortest paths using a Radix Heap.
    Assumes non-negative integer weights and integer distances.
    Returns distances array of length n (math.inf represented as a large int).
    """
    n = len(adj)
    INF = (1 << 62) - 1  # large sentinel
    dist = [INF] * n
    dist[src] = 0
    visited = [False] * n
    pq = RadixHeap(max_bits=64)
    pq.push(0, src)

    while pq:
        d, u = pq.pop()
        if visited[u]:
            continue
        visited[u] = True
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                pq.push(nd, v)
    return dist


# -----------------------------
# Benchmark harness
# -----------------------------

def check_equal(d1: Iterable[float], d2: Iterable[float]) -> bool:
    INF_INT = 1 << 61
    for a, b in zip(d1, d2):
        a_inf = math.isinf(a)
        b_inf = (isinstance(b, int) and b >= INF_INT) or (isinstance(b, float) and math.isinf(b))
        if a_inf and b_inf:
            continue
        if a != b:
            return False
    return True


def bench_once(adj: Adj, src: int, repeat: int = 1) -> Tuple[float, float, List[float], List[int]]:
    """
    Run both algorithms on the same graph and return:
    (time_binary_heap_sec, time_radix_heap_sec, dist_binary, dist_radix)
    """
    # Warmup (tiny) and initialize outputs to satisfy linters even if repeat==0
    dist_b = dijkstra_binary_heap(adj, src)
    dist_r = dijkstra_radix_heap(adj, src)

    t1 = math.inf
    for _ in range(repeat):
        t0 = time.perf_counter()
        dist_b = dijkstra_binary_heap(adj, src)
        t1 = min(t1, time.perf_counter() - t0)

    t2 = math.inf
    for _ in range(repeat):
        t0 = time.perf_counter()
        dist_r = dijkstra_radix_heap(adj, src)
        t2 = min(t2, time.perf_counter() - t0)

    return t1, t2, dist_b, dist_r


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Benchmark classic vs radix-heap Dijkstra on directed graphs")
    p.add_argument("--n", type=int, default=5000, help="number of nodes")
    p.add_argument("--m", type=int, default=20000, help="number of directed edges")
    p.add_argument(
        "--m-list",
        nargs="+",
        help=(
            "optional list of edge-counts to sweep; items can be integers or of the form 'kN' (e.g. 4n, 10n). "
            "When provided, --m is ignored and each m in the list is benchmarked."
        ),
    )
    p.add_argument("--max-w", type=int, default=100, help="max integer edge weight (inclusive)")
    p.add_argument("--src", type=int, default=0, help="source vertex index [0..n-1]")
    p.add_argument("--trials", type=int, default=3, help="number of trials to average (min-time) per config")
    p.add_argument("--seed", type=int, default=42, help="RNG seed for graph generation")
    p.add_argument("--no-check", action="store_true", help="skip correctness check")
    args = p.parse_args(argv)

    n = args.n
    m = args.m
    max_w = args.max_w
    src = max(0, min(args.src, n - 1))

    def parse_m_tokens(tokens: Optional[List[str]], nval: int) -> Optional[List[int]]:
        if not tokens:
            return None
        out: List[int] = []
        for t in tokens:
            ts = t.strip().lower()
            if ts.endswith("n"):
                # forms like '4n' or '10n'
                coef_txt = ts[:-1]
                if coef_txt in ("", "+", "-"):
                    k = 1
                else:
                    try:
                        k = float(coef_txt)
                    except ValueError:
                        raise ValueError(f"Invalid m token '{t}'. Use integers or forms like '4n'.")
                out.append(int(k * nval))
            else:
                try:
                    out.append(int(ts))
                except ValueError:
                    raise ValueError(f"Invalid m token '{t}'. Use integers or forms like '4n'.")
        return out

    m_list = parse_m_tokens(args.m_list, n)

    if m_list:
        print(f"Sweep: n={n}, max_w={max_w}, src={src}, seed={args.seed}")
        print("m, time_binary_s, time_radix_s, speedup_b_over_r")
        for mi in m_list:
            mi = max(0, int(mi))
            print(f"# running m={mi}")
            adj = generate_random_digraph(n, mi, max_w, seed=args.seed)
            tb, tr, db, dr = bench_once(adj, src, repeat=max(1, args.trials))
            if not args.no_check:
                ok = check_equal(db, dr)
                status = "PASS" if ok else "FAIL"
                print(f"Correctness: {status}")
                if not ok:
                    INF_INT = 1 << 61
                    mism = [
                        (i, db[i], dr[i])
                        for i in range(n)
                        if not ((math.isinf(db[i]) and (isinstance(dr[i], int) and dr[i] >= INF_INT)) or db[i] == dr[i])
                    ]
                    print("First mismatches (up to 5):", mism[:5])
            speedup = tb / tr if tr > 0 else float('inf')
            print(f"{mi}, {tb:.6f}, {tr:.6f}, {speedup:.3f}")
        return 0

    print(f"Graph: n={n}, m={m}, max_w={max_w}, src={src}, seed={args.seed}")
    adj = generate_random_digraph(n, m, max_w, seed=args.seed)

    tb, tr, db, dr = bench_once(adj, src, repeat=max(1, args.trials))

    if not args.no_check:
        ok = check_equal(db, dr)
        print(f"Correctness: {'PASS' if ok else 'FAIL'}")
        if not ok:
            # Print a small diff sample
            INF_INT = 1 << 61
            mism = [
                (i, db[i], dr[i])
                for i in range(n)
                if not ((math.isinf(db[i]) and (isinstance(dr[i], int) and dr[i] >= INF_INT)) or db[i] == dr[i])
            ]
            print("First mismatches (up to 5):", mism[:5])

    speedup = tb / tr if tr > 0 else float('inf')
    print("Results (sec):")
    print(f"- Classic Dijkstra (binary heap): {tb:.6f}s")
    print(f"- Radix-heap Dijkstra        : {tr:.6f}s")
    print(f"Speedup (classic/radix)      : {speedup:.2f}x")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
