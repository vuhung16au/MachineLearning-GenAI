# Python Package Manager Comparison: uv vs pip

This project benchmarks `uv` against `pip` on macOS (Apple Silicon) using the same dependency set and scenarios. It measures install speed and basic environment handling across multiple Python versions.

## Scenarios
- Clean install: create a fresh virtual environment and install from `requirements.txt` with a cold cache.

## Iterations
By default, each Python version is tested **3 times** to provide statistical significance. You can customize this with the `ITERATIONS` parameter:
- More iterations = more reliable results but longer execution time
- Fewer iterations = faster execution but less statistical confidence
- Default: 3 iterations per Python version

## Python versions
Configured in `scripts/run_benchmarks.sh`. Defaults to:
- /opt/homebrew/bin/python3.9
- /opt/homebrew/bin/python3.10
- /opt/homebrew/bin/python3.11
- /opt/homebrew/bin/python3.12
- /opt/homebrew/bin/python3.13

## Prerequisites
- macOS (Apple Silicon)
- `uv` installed (see `https://astral.sh/uv`)
- Target Python versions installed (via Homebrew `brew install python@3.12` etc.)

## Quick start

### Basic usage (3 iterations per Python version)
```bash
# From repo root
make all
```

### Custom number of iterations
```bash
# Run 5 iterations per Python version
make all ITERATIONS=5

# Run only Python 3.11 with 10 iterations
make python311 ITERATIONS=10

# Run all Python versions with 1 iteration (quick test)
make all ITERATIONS=1
```

### Manual execution
```bash
# Run with default 3 iterations
chmod +x scripts/run_benchmarks.sh
./scripts/run_benchmarks.sh

# Run with custom iterations
ITERATIONS=5 ./scripts/run_benchmarks.sh

# Run specific Python version with custom iterations
ITERATIONS=10 PYTHONS_CSV="/opt/homebrew/bin/python3.11" ./scripts/run_benchmarks.sh
```

### Generate reports
```bash
# Generate Markdown report and PNG graphs
make gen

# Or manually
python3 scripts/compare_results.py results/benchmark_results.csv results/benchmark_results.md results/benchmark_results.png
```

## Outputs
- `results/benchmark_results.csv`: Append-only raw results
- `results/benchmark_results.md`: Summary table and notes
- `results/logs/`: Per-run logs and environment details

## Notes
- Cold cache runs clear pip/uv caches and remove any `.venv*` directories before installing.
- You can safely rerun; new rows are appended with timestamps.
- Each iteration creates a fresh virtual environment for accurate timing.
- Results include statistical analysis across multiple iterations for more reliable comparisons.
