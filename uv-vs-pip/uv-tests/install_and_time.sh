#!/usr/bin/env bash
set -euo pipefail

if [ "${1:-}" = "" ] || [ "${2:-}" = "" ]; then
  echo "Usage: $0 /path/to/python /path/to/logfile" >&2
  exit 2
fi

PYTHON_PATH="$1"
LOG_PATH="$2"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
REQS_FILE="$REPO_ROOT/uv-tests/requirements.txt"

# Derive python version identifier
PYVER="$("$PYTHON_PATH" -c 'import sys; v=sys.version_info; print(f"{v.major}.{v.minor}")')"
VENV_DIR="$REPO_ROOT/.venv-uv-$PYVER"

mkdir -p "$(dirname "$LOG_PATH")"

# Clean previous venv and uv cache for cold run
rm -rf "$VENV_DIR"
uv --version >>"$LOG_PATH" 2>&1 || { echo "uv not installed" >&2; exit 3; }
uv cache clean -y >>"$LOG_PATH" 2>&1 || true

# Start timer using the provided Python
START_SEC="$($PYTHON_PATH -c 'import time; print(time.time())')"
{
  echo "[uv] Python: $PYTHON_PATH (v$PYVER)"
  echo "[uv] Creating venv: $VENV_DIR"
} >>"$LOG_PATH" 2>&1

uv venv --python "$PYTHON_PATH" "$VENV_DIR" >>"$LOG_PATH" 2>&1
# shellcheck source=/dev/null
source "$VENV_DIR/bin/activate"

{
  echo "[uv] Installing requirements via uv pip from $REQS_FILE"
  python -V
  uv --version
} >>"$LOG_PATH" 2>&1

uv pip install -r "$REQS_FILE" >>"$LOG_PATH" 2>&1

deactivate || true
# End timer using the same Python interpreter
END_SEC="$($PYTHON_PATH -c 'import time; print(time.time())')"

ELAPSED_SEC=$(awk -v s="$START_SEC" -v e="$END_SEC" 'BEGIN { printf "%.3f", (e - s) }')

echo "$ELAPSED_SEC"
exit 0
