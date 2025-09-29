#!/usr/bin/env python3
import csv
import sys
import platform
import subprocess
from collections import defaultdict
from statistics import mean
from pathlib import Path


def load_rows(csv_path: Path):
    with csv_path.open() as f:
        reader = csv.DictReader(f)
        rows = [r for r in reader]
    # Cast elapsed_seconds to float, success to int
    for r in rows:
        try:
            r["elapsed_seconds"] = float(r.get("elapsed_seconds", "nan"))
        except Exception:
            r["elapsed_seconds"] = float("nan")
        try:
            r["success"] = int(r.get("success", 0))
        except Exception:
            r["success"] = 0
    return rows


def _nan():
    return float("nan")


def make_markdown(rows):
    lines = []
    lines.append("## Benchmark Summary: uv vs pip")
    lines.append("")

    # Aggregate per-python per-manager
    py_mgr_all = defaultdict(lambda: defaultdict(list))  # all elapsed values (may be NaN)
    py_mgr_success = defaultdict(lambda: defaultdict(list))  # successful elapsed values
    py_mgr_counts = defaultdict(lambda: defaultdict(lambda: {"succ": 0, "total": 0}))

    for r in rows:
        py = r.get("python", "unknown")
        mgr = r.get("manager", "unknown")
        el = r.get("elapsed_seconds", _nan())
        suc = 1 if r.get("success", 0) == 1 else 0
        py_mgr_all[py][mgr].append(el)
        if suc == 1 and el == el:
            py_mgr_success[py][mgr].append(el)
        py_mgr_counts[py][mgr]["total"] += 1
        py_mgr_counts[py][mgr]["succ"] += suc

    lines.append("### Per Python version")
    lines.append("")
    lines.append("| Python | pip | uv | winner |")
    lines.append("|---|---:|---:|:--:|")

    def fmt_mean(vals):
        if not vals:
            return "NaN"
        m = mean(vals)
        return f"{m:.3f}"

    def extract_py_version(py_path):
        """Extract python version from path like '/opt/homebrew/bin/python3.9' -> 'python3.9'"""
        if '/python' in py_path:
            return py_path.split('/')[-1]
        return py_path

    def sort_py_versions(py_list):
        """Sort Python versions in order: 3.9, 3.10, 3.11, 3.12, 3.13"""
        def version_key(py):
            if 'python3.' in py:
                try:
                    version = float(py.replace('python3.', ''))
                    return version
                except:
                    return 999  # put unknown versions at end
            return 999
        return sorted(py_list, key=version_key)

    # Sort Python versions in the desired order
    sorted_py_versions = sort_py_versions(py_mgr_counts.keys())
    
    for py in sorted_py_versions:
        pip_succ = py_mgr_success[py].get("pip", [])
        uv_succ = py_mgr_success[py].get("uv", [])
        pip_cell = fmt_mean(pip_succ)
        uv_cell = fmt_mean(uv_succ)
        py_display = extract_py_version(py)
        
        # Winner: only if both have at least 1 success
        if pip_succ and uv_succ:
            win = "uv" if mean(uv_succ) < mean(pip_succ) else ("pip" if mean(pip_succ) < mean(uv_succ) else "=")
        elif pip_succ:
            win = "pip"
        elif uv_succ:
            win = "uv"
        else:
            win = "-"
        lines.append(f"| {py_display} | {pip_cell} | {uv_cell} | {win} |")

    # Overall averages
    mgr_all_success = defaultdict(list)
    for r in rows:
        if r["success"] == 1 and r["elapsed_seconds"] == r["elapsed_seconds"]:
            mgr_all_success[r["manager"]].append(r["elapsed_seconds"])

    lines.append("")
    lines.append("### Overall mean (seconds over successful runs)")
    lines.append("")
    lines.append("| Manager | Mean seconds | Successful runs | Total runs |")
    lines.append("|---|---:|---:|---:|")
    for mgr in ("pip", "uv"):
        vals = mgr_all_success.get(mgr, [])
        succ = sum(1 for r in rows if r.get("manager") == mgr and r.get("success") == 1 and r.get("elapsed_seconds") == r.get("elapsed_seconds"))
        total = sum(1 for r in rows if r.get("manager") == mgr)
        mean_str = f"{mean(vals):.3f}" if vals else "NaN"
        lines.append(f"| {mgr} | {mean_str} | {succ} | {total} |")

    if not rows:
        lines.append("")
        lines.append("No benchmark rows found in CSV.")
    elif all(r.get("success") != 1 for r in rows):
        lines.append("")
        lines.append("Note: All recorded runs failed or have missing times; no successful timings to average.")

    # Add system information
    lines.append("")
    lines.append("## System Information")
    lines.append("")
    lines.append(f"- **OS**: {os} {version}".format(os=platform.system(), version=platform.release()))
    lines.append(f"- **Architecture**: {platform.machine()}")
    lines.append(f"- **Python**: {platform.python_version()}")
    
    # Try to get more detailed OS info
    try:
        if platform.system() == "Darwin":  # macOS
            result = subprocess.run(["sw_vers", "-productName", "-productVersion"], 
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                lines.append(f"- **macOS**: {result.stdout.strip().replace(chr(10), ' ')}")
    except:
        pass
    
    try:
        if platform.system() == "Linux":
            result = subprocess.run(["lsb_release", "-d"], 
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                lines.append(f"- **Linux**: {result.stdout.split(':')[1].strip()}")
    except:
        pass

    return "\n".join(lines) + "\n"


def main():
    if len(sys.argv) != 3:
        print("Usage: compare_results.py /path/to/benchmark_results.csv /path/to/output.md", file=sys.stderr)
        sys.exit(2)
    csv_path = Path(sys.argv[1])
    md_path = Path(sys.argv[2])
    rows = load_rows(csv_path)
    md = make_markdown(rows)
    md_path.write_text(md)
    print(f"Wrote {md_path}")


if __name__ == "__main__":
    main()
