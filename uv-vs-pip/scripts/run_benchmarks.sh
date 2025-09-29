#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
RESULTS_CSV="$REPO_ROOT/results/benchmark_results.csv"
LOG_DIR="$REPO_ROOT/results/logs"

# Default Python versions (Homebrew paths)
PYTHONS=(
  "/opt/homebrew/bin/python3.9"
  "/opt/homebrew/bin/python3.10"
  "/opt/homebrew/bin/python3.11"
  "/opt/homebrew/bin/python3.12"
  "/opt/homebrew/bin/python3.13"
)

# Allow override via env var PYTHONS_CSV
if [ "${PYTHONS_CSV:-}" != "" ]; then
  IFS=',' read -r -a PYTHONS <<<"$PYTHONS_CSV"
fi

mkdir -p "$LOG_DIR"

TIMESTAMP() { date -u +"%Y-%m-%dT%H:%M:%SZ"; }

run_case() {
  local manager="$1"; shift
  local py="$1"; shift

  local py_id
  py_id="$($py -c 'import sys; v=sys.version_info; print(f"{v.major}.{v.minor}")' 2>/dev/null || echo "unknown")"
  local ts
  ts="$(date +%Y%m%d_%H%M%S)"
  local log_path="$LOG_DIR/${ts}_${manager}_py${py_id}.log"

  local elapsed=""
  local success="0"

  if [ "$manager" = "pip" ]; then
    if [ ! -x "$REPO_ROOT/pip-tests/install_and_time.sh" ]; then chmod +x "$REPO_ROOT/pip-tests/install_and_time.sh"; fi
    set +e
    elapsed="$($REPO_ROOT/pip-tests/install_and_time.sh "$py" "$log_path" 2>>"$log_path")"
    rc=$?
    set -e
  else
    if [ ! -x "$REPO_ROOT/uv-tests/install_and_time.sh" ]; then chmod +x "$REPO_ROOT/uv-tests/install_and_time.sh"; fi
    set +e
    elapsed="$($REPO_ROOT/uv-tests/install_and_time.sh "$py" "$log_path" 2>>"$log_path")"
    rc=$?
    set -e
  fi

  if [ "$rc" -eq 0 ]; then success="1"; fi

  # Append CSV: timestamp,manager,python,scenario,success,elapsed_seconds,log_path
  echo "$(TIMESTAMP),$manager,$py,clean_cold,$success,$elapsed,$log_path" | tee -a "$RESULTS_CSV" >/dev/null
}

# Header if file empty
if [ ! -s "$RESULTS_CSV" ]; then
  echo "timestamp,manager,python,scenario,success,elapsed_seconds,log_path" >"$RESULTS_CSV"
fi

for py in "${PYTHONS[@]}"; do
  if [ ! -x "$py" ]; then
    echo "Skipping missing python: $py" >&2
    continue
  fi
  for manager in pip uv; do
    echo "Running $manager on $py ..."
    run_case "$manager" "$py"
  done
done

echo "Done. Results appended to: $RESULTS_CSV"
