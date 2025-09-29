# Python Package Manager Comparison: uv vs pip

This project benchmarks `uv` against `pip` on macOS (Apple Silicon) using the same dependency set and scenarios. It measures install speed and basic environment handling across multiple Python versions.

## Scenarios
- Clean install: create a fresh virtual environment and install from `requirements.txt` with a cold cache.

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
```bash
# From repo root
chmod +x scripts/run_benchmarks.sh
./scripts/run_benchmarks.sh

# Generate summary Markdown from CSV
/opt/homebrew/bin/python3 scripts/compare_results.py results/benchmark_results.csv results/benchmark_results.md
```

## Outputs
- `results/benchmark_results.csv`: Append-only raw results
- `results/benchmark_results.md`: Summary table and notes
- `results/logs/`: Per-run logs and environment details

## Notes
- Cold cache runs clear pip/uv caches and remove any `.venv*` directories before installing.
- You can safely rerun; new rows are appended with timestamps.
