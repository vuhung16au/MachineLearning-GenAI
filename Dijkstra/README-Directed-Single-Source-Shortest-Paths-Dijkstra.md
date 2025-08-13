# Directed SSSP: Dijkstra variants benchmark (binary heap vs radix heap)

This folder contains a practical benchmark comparing two implementations of single-source shortest paths (SSSP) for directed graphs with non-negative integer weights:

- Classic Dijkstra with a binary heap (heapq)
- Dijkstra with a monotone Radix Heap (bucketed priority queue for non-decreasing keys)

The goal is to empirically illustrate the “sort-free” advantage on sparse graphs by removing O(log n) comparisons per PQ op, inspired by ideas discussed in the paper “Breaking the Sorting Barrier for Directed Single-Source Shortest Paths” (arXiv:2504.17033). Note: the paper’s algorithm is different (theoretical O(m log^(2/3) n) in the comparison-addition model). Here we benchmark two practical Dijkstra variants; this is a proxy experiment showing how avoiding comparisons can help in sparse regimes with integer weights.


## What’s implemented

- Random directed graph generator with m edges, integer weights in [0, max_w]
- Two SSSP solvers: binary-heap Dijkstra and radix-heap Dijkstra
- A sweep mode to test multiple m values in one run (tokens like `1n`, `4n`, `10n` expand to k·n edges)
- Correctness checks and CSV-like timing output

File of interest: `Directed-Single-Source-Shortest-Paths-Dijkstra.py`


## Usage

Basic single run:

```zsh
python3 Dijkstra/Directed-Single-Source-Shortest-Paths-Dijkstra.py \
  --n 5000 --m 20000 --max-w 100 --trials 3 --seed 1
```

Sweep several edge counts (CSV output line per m):

```zsh
python3 Dijkstra/Directed-Single-Source-Shortest-Paths-Dijkstra.py \
  --n 200000 --m-list 1n 2n 4n 8n --max-w 100 --trials 3 --seed 1
```

- `--m-list` accepts integers or tokens like `kn` meaning m = k·n (e.g., `4n`).
- Output columns: `m, time_binary_s, time_radix_s, speedup_b_over_r`.
  - `speedup_b_over_r > 1` means radix-heap is faster.


## Recommended experiments (sparse vs denser)

Sparse regime (m = O(n)):

```zsh
python3 Dijkstra/Directed-Single-Source-Shortest-Paths-Dijkstra.py \
  --n 200000 --m-list 1n 2n 3n 4n 6n --max-w 100 --trials 3 --seed 1
```

Denser regime (growing m):

```zsh
python3 Dijkstra/Directed-Single-Source-Shortest-Paths-Dijkstra.py \
  --n 100000 --m-list 8n 16n 32n 64n --max-w 100 --trials 3 --seed 1
```

Tips:

- Use larger `n` (≥ 2e5) so trends aren’t dominated by constant overheads.
- Keep `--max-w` moderate (e.g., 100–1000) to stay within fast integer distances.


## How to interpret

- In sparse graphs, binary-heap Dijkstra has a noticeable `n log n` component, while radix-heap reduces comparison overhead and often wins in practice as `n` grows.
- As graphs get denser (large `m`), the gap typically narrows; the advantage isn’t universal outside sparse regimes.
- This mirrors the paper’s high-level message that beating sorting can help, though the paper’s algorithm and models differ from this practical test.


## Sample result (small n sanity check)

Command run (on macOS, Python 3):

```zsh
python3 Dijkstra/Directed-Single-Source-Shortest-Paths-Dijkstra.py \
  --n 1000 --m-list 1n 2n 4n 8n --trials 2 --max-w 100 --seed 1
```

Output (truncated for the CSV lines):

```text
1000, 0.000005, 0.000011, 0.452
2000, 0.000366, 0.001170, 0.313
4000, 0.000742, 0.001790, 0.415
8000, 0.001203, 0.002556, 0.471
```

Observation: at such small `n`, overheads dominate and the radix-heap shows slower times (< 1 speedup). Increase `n` per the recommended experiments to observe the expected sparse-graph advantage.


## Notes and limitations

- This is not an implementation of the new O(m log^(2/3) n) algorithm; it’s a practical comparison of two Dijkstra PQ variants to illustrate sort-free benefits on integer-weight graphs.
- Radix heap requires non-decreasing extracted keys and non-negative integer weights; this holds for Dijkstra.
- Random graphs are uniform; different graph families may exhibit different behaviors.
- For rigorous reproduction, pin Python, CPU governor, and run multiple trials (`--trials`) taking min-time.


## Quick reference

- Binary heap Dijkstra: O(m + n log n) operations, comparison-based PQ
- Radix heap Dijkstra: integer bucketed PQ; fewer comparisons, often faster for sparse integer-weight graphs


## Reproducing CSV to a file

```zsh
python3 Dijkstra/Directed-Single-Source-Shortest-Paths-Dijkstra.py \
  --n 200000 --m-list 1n 2n 4n 8n --max-w 100 --trials 3 --seed 1 \
  | tee results_sparse.csv
```

Each line: `m, t_binary, t_radix, speedup_b_over_r`.
