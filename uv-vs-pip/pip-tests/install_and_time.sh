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
REQS_FILE="$REPO_ROOT/pip-tests/requirements.txt"

# Derive python version identifier
PYVER="$("$PYTHON_PATH" -c 'import sys; v=sys.version_info; print(f"{v.major}.{v.minor}")')"
VENV_DIR="$REPO_ROOT/.venv-pip-$PYVER"

# Prepare logs directory
mkdir -p "$(dirname "$LOG_PATH")"

# Clean previous venv and caches for cold run
rm -rf "$VENV_DIR"
"$PYTHON_PATH" -m pip --version >/dev/null 2>&1 || "$PYTHON_PATH" -m ensurepip --upgrade >/dev/null 2>&1 || true
"$PYTHON_PATH" -m pip install --upgrade pip >/dev/null 2>&1 || true
"$PYTHON_PATH" -m pip cache purge >/dev/null 2>&1 || true

# Start timer using the provided Python
START_SEC="$($PYTHON_PATH -c 'import time; print(time.time())')"
{
  echo "[pip] Python: $PYTHON_PATH (v$PYVER)"
  echo "[pip] Creating venv: $VENV_DIR"
} >>"$LOG_PATH" 2>&1

"$PYTHON_PATH" -m venv "$VENV_DIR" >>"$LOG_PATH" 2>&1
# shellcheck source=/dev/null
source "$VENV_DIR/bin/activate"

{
  echo "[pip] Upgrading pip and installing requirements from $REQS_FILE"
  python -V
  pip -V
} >>"$LOG_PATH" 2>&1

pip install --upgrade pip wheel setuptools >>"$LOG_PATH" 2>&1
pip install -r "$REQS_FILE" >>"$LOG_PATH" 2>&1

deactivate || true
# End timer using the same Python interpreter
END_SEC="$($PYTHON_PATH -c 'import time; print(time.time())')"

ELAPSED_SEC=$(awk -v s="$START_SEC" -v e="$END_SEC" 'BEGIN { printf "%.3f", (e - s) }')

echo "$ELAPSED_SEC"
exit 0
