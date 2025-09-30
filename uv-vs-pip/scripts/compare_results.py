#!/usr/bin/env python3
import csv
import sys
import platform
import subprocess
try:
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    GRAPH_AVAILABLE = True
except ImportError:
    GRAPH_AVAILABLE = False
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
    lines.append(f"- **OS**: {platform.system()} {platform.release()}")
    lines.append(f"- **Architecture**: {platform.machine()}")
    lines.append(f"- **Python**: {platform.python_version()}")
    
    # Try to get more detailed OS info
    try:
        if platform.system() == "Darwin":  # macOS
            result = subprocess.run(["sw_vers", "-productName", "-productVersion"], 
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                output = result.stdout.strip()
                lines.append(f"- **macOS**: {output}")
    except Exception:
        pass
    
    try:
        if platform.system() == "Linux":
            result = subprocess.run(["lsb_release", "-d"], 
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                lines.append(f"- **Linux**: {result.stdout.split(':')[1].strip()}")
    except Exception:
        pass

    return "\n".join(lines) + "\n"


def create_text_summary(csv_path: Path, output_path: Path):
    """Create a simple text-based performance summary when matplotlib is not available"""
    
    # Load data manually
    rows = load_rows(csv_path)
    successful_rows = [r for r in rows if r.get("success") == 1]
    
    if not successful_rows:
        print("No successful benchmark data found.")
        return
    
    # Group by manager and calculate stats
    manager_stats = defaultdict(list)
    for r in successful_rows:
        manager_stats[r["manager"]].append(r["elapsed_seconds"])
    
    # Create simple text visualization
    lines = []
    lines.append("=" * 60)
    lines.append("PERFORMANCE COMPARISON: pip vs uv")
    lines.append("=" * 60)
    lines.append("")
    
    # Calculate statistics
    pip_times = manager_stats.get("pip", [])
    uv_times = manager_stats.get("uv", [])
    
    if pip_times and uv_times:
        pip_avg = mean(pip_times)
        uv_avg = mean(uv_times)
        speedup = pip_avg / uv_avg
        
        lines.append(f"Average Installation Time:")
        lines.append(f"  pip: {pip_avg:.1f} seconds")
        lines.append(f"  uv:  {uv_avg:.1f} seconds")
        lines.append(f"  Speedup: {speedup:.1f}x faster with uv")
        lines.append("")
        
        # Create simple bar chart representation
        max_time = max(pip_avg, uv_avg)
        pip_bars = int((pip_avg / max_time) * 40)
        uv_bars = int((uv_avg / max_time) * 40)
        
        lines.append("Visual Comparison (bar chart):")
        lines.append(f"pip: {'█' * pip_bars} ({pip_avg:.1f}s)")
        lines.append(f"uv:  {'█' * uv_bars} ({uv_avg:.1f}s)")
        lines.append("")
        
        # Winner announcement
        lines.append("🏆 WINNER: uv is significantly faster!")
        lines.append(f"   uv is {speedup:.1f}x faster than pip on average")
        lines.append("")
        
        # Per Python version breakdown
        py_stats = defaultdict(lambda: defaultdict(list))
        for r in successful_rows:
            py = r.get("python", "unknown")
            mgr = r.get("manager", "unknown")
            py_stats[py][mgr].append(r["elapsed_seconds"])
        
        lines.append("Per Python Version:")
        lines.append("-" * 40)
        for py in sorted(py_stats.keys()):
            pip_py = mean(py_stats[py].get("pip", [0]))
            uv_py = mean(py_stats[py].get("uv", [0]))
            if pip_py > 0 and uv_py > 0:
                py_speedup = pip_py / uv_py
                lines.append(f"{py}: pip={pip_py:.1f}s, uv={uv_py:.1f}s ({py_speedup:.1f}x)")
    
    lines.append("=" * 60)
    
    # Write to file
    with open(output_path.with_suffix('.txt'), 'w') as f:
        f.write('\n'.join(lines))
    
    print(f"Created text summary: {output_path.with_suffix('.txt')}")


def create_performance_graphs(csv_path: Path, output_path: Path):
    """Create comprehensive performance comparison graphs"""
    
    if not GRAPH_AVAILABLE:
        print("Creating simple text-based performance summary...")
        create_text_summary(csv_path, output_path)
        return
    
    # Load and process data
    df = pd.read_csv(csv_path)
    df = df[df['success'] == 1]  # Only successful runs
    
    # Extract Python version from path
    df['python_version'] = df['python'].str.extract(r'python(\d+\.\d+)')
    df['python_version'] = 'Python ' + df['python_version']
    
    # Sort Python versions in chronological order: 3.9, 3.10, 3.11, 3.12, 3.13
    def sort_python_versions(version_str):
        """Extract version number for sorting"""
        try:
            return float(version_str.replace('Python ', ''))
        except:
            return 999  # Put unknown versions at the end
    
    df = df.sort_values('python_version', key=lambda x: x.map(sort_python_versions))
    
    # Set up the plotting style
    plt.style.use('default')
    plt.rcParams['figure.facecolor'] = 'white'
    plt.rcParams['axes.facecolor'] = 'white'
    
    # Create figure with subplots
    fig = plt.figure(figsize=(16, 12))
    fig.suptitle('Performance Comparison: pip vs uv', fontsize=20, fontweight='bold', y=0.98)
    
    # 1. Main Performance Comparison (Grouped Bar Chart)
    ax1 = plt.subplot(2, 2, 1)
    
    # Prepare data for grouped bar chart
    performance_data = df.groupby(['python_version', 'manager'])['elapsed_seconds'].mean().unstack()
    
    # Ensure the performance data is sorted by Python version in chronological order
    performance_data = performance_data.sort_index(key=lambda x: x.map(sort_python_versions))
    
    # Create grouped bar chart
    performance_data.plot(kind='bar', ax=ax1, color=['#e74c3c', '#3498db'], width=0.8)
    ax1.set_title('Installation Time by Python Version', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Python Version', fontsize=12)
    ax1.set_ylabel('Time (seconds)', fontsize=12)
    ax1.legend(['pip', 'uv'], title='Package Manager', loc='upper right')
    ax1.grid(True, alpha=0.3)
    
    # Add value labels on bars
    for i, idx in enumerate(performance_data.index):
        for j, col in enumerate(['pip', 'uv']):
            if col in performance_data.columns:
                value = performance_data.loc[idx, col]
                ax1.text(i + (j-0.5)*0.4, value + 1, f'{value:.1f}s', 
                        ha='center', va='bottom', fontweight='bold', fontsize=10)
    
    # 2. Speedup Analysis
    ax2 = plt.subplot(2, 2, 2)
    
    # Calculate speedup ratios
    speedup_data = []
    for version in performance_data.index:
        if 'pip' in performance_data.columns and 'uv' in performance_data.columns:
            pip_time = performance_data.loc[version, 'pip']
            uv_time = performance_data.loc[version, 'uv']
            speedup = pip_time / uv_time
            speedup_data.append({'Python Version': version, 'Speedup': speedup})
    
    speedup_df = pd.DataFrame(speedup_data)
    
    # Sort speedup data by Python version in chronological order
    speedup_df = speedup_df.sort_values('Python Version', key=lambda x: x.map(sort_python_versions))
    
    # Create speedup bar chart
    bars = ax2.bar(speedup_df['Python Version'], speedup_df['Speedup'], 
                   color=['#f39c12', '#e67e22', '#d35400', '#c0392b', '#a93226'])
    ax2.set_title('Speedup Ratio (pip time / uv time)', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Python Version', fontsize=12)
    ax2.set_ylabel('Speedup Factor', fontsize=12)
    ax2.grid(True, alpha=0.3)
    
    # Add speedup values on bars
    for bar, speedup in zip(bars, speedup_df['Speedup']):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
                f'{speedup:.1f}x', ha='center', va='bottom', fontweight='bold', fontsize=11)
    
    # Add horizontal line at 1x (no speedup)
    ax2.axhline(y=1, color='red', linestyle='--', alpha=0.7, label='No speedup')
    ax2.legend()
    
    # 3. Overall Performance Comparison
    ax3 = plt.subplot(2, 2, 3)
    
    # Calculate overall means
    overall_means = df.groupby('manager')['elapsed_seconds'].mean()
    
    # Create pie chart for overall performance
    colors = ['#e74c3c', '#3498db']
    wedges, texts, autotexts = ax3.pie(overall_means.values, labels=overall_means.index, 
                                       autopct='%1.1f%%', colors=colors, startangle=90)
    ax3.set_title('Overall Performance Distribution', fontsize=14, fontweight='bold')
    
    # Add time values to pie chart
    for i, (manager, time) in enumerate(overall_means.items()):
        ax3.text(0, 0, f'{manager}\n{time:.1f}s', ha='center', va='center', 
                fontsize=12, fontweight='bold', transform=ax3.transAxes)
    
    # 4. Performance Trend Analysis
    ax4 = plt.subplot(2, 2, 4)
    
    # Create line plot showing trend across Python versions
    for manager in ['pip', 'uv']:
        manager_data = df[df['manager'] == manager].groupby('python_version')['elapsed_seconds'].mean()
        # Sort the data by Python version in chronological order
        manager_data = manager_data.sort_index(key=lambda x: x.map(sort_python_versions))
        ax4.plot(manager_data.index, manager_data.values, marker='o', linewidth=3, 
                markersize=8, label=manager, alpha=0.8)
    
    ax4.set_title('Performance Trend Across Python Versions', fontsize=14, fontweight='bold')
    ax4.set_xlabel('Python Version', fontsize=12)
    ax4.set_ylabel('Time (seconds)', fontsize=12)
    ax4.legend(title='Package Manager', loc='upper right')
    ax4.grid(True, alpha=0.3)
    
    # Add annotations for best performance
    min_uv_time = df[df['manager'] == 'uv']['elapsed_seconds'].min()
    min_pip_time = df[df['manager'] == 'pip']['elapsed_seconds'].min()
    
    ax4.annotate(f'Best uv: {min_uv_time:.1f}s', 
                xy=(0.02, 0.98), xycoords='axes fraction',
                bbox=dict(boxstyle="round,pad=0.3", facecolor='lightblue', alpha=0.7),
                fontsize=10, fontweight='bold')
    
    ax4.annotate(f'Best pip: {min_pip_time:.1f}s', 
                xy=(0.02, 0.88), xycoords='axes fraction',
                bbox=dict(boxstyle="round,pad=0.3", facecolor='lightcoral', alpha=0.7),
                fontsize=10, fontweight='bold')
    
    # Add winner annotation
    overall_speedup = overall_means['pip'] / overall_means['uv']
    ax4.text(0.5, 0.95, f'uv is {overall_speedup:.1f}x faster overall!', 
            transform=ax4.transAxes, ha='center', va='top',
            bbox=dict(boxstyle="round,pad=0.5", facecolor='gold', alpha=0.8),
            fontsize=14, fontweight='bold')
    
    # Adjust layout and save
    plt.tight_layout()
    plt.subplots_adjust(top=0.93)
    
    # Save with high quality
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"Generated performance graphs: {output_path}")
    
    # Also create a summary statistics text
    summary_text = f"""
Performance Summary:
- uv is {overall_speedup:.1f}x faster than pip on average
- Best speedup: {speedup_df['Speedup'].max():.1f}x
- Average pip time: {overall_means['pip']:.1f}s
- Average uv time: {overall_means['uv']:.1f}s
- Total successful runs: {len(df)}
"""
    print(summary_text)


def main():
    if len(sys.argv) < 3:
        print("Usage: compare_results.py /path/to/benchmark_results.csv /path/to/output.md [graph_output.png]", file=sys.stderr)
        sys.exit(2)
    
    csv_path = Path(sys.argv[1])
    md_path = Path(sys.argv[2])
    
    # Load data and generate markdown
    rows = load_rows(csv_path)
    md = make_markdown(rows)
    md_path.write_text(md)
    print(f"Wrote {md_path}")
    
    # Generate graphs if output path provided
    if len(sys.argv) >= 4:
        graph_path = Path(sys.argv[3])
        try:
            create_performance_graphs(csv_path, graph_path)
        except ImportError as e:
            print(f"Warning: Could not generate graphs due to missing dependencies: {e}")
            print("Install required packages: pip install pandas seaborn matplotlib")
        except Exception as e:
            print(f"Error generating graphs: {e}")


if __name__ == "__main__":
    main()
