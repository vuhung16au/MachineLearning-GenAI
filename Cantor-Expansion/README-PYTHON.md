# Cantor Expansion Verification - Python Setup

This directory contains a Python program to verify the solution to the Cantor expansion problem for `1/2025^1000`.

## Problem Description

Find the smallest positive integer `n` such that:

```
1/2025^1000 = a_1 + a_2/2! + a_3/3! + ... + a_n/n!
```

Where:
- `n` is a positive integer
- `a_1, a_2, ..., a_n` are nonnegative integers
- `a_k < k` for `k = 2, ..., n`
- `a_n > 0`

The solution claims `n = 8013`.

## Prerequisites

- Python 3.9 or higher
- `uv` package manager (for virtual environment management)

### Installing uv

If you don't have `uv` installed, install it using:

```bash
# On macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or using pip
pip install uv
```

## Setup Instructions

### 1. Navigate to the Project Directory

```bash
cd /path/to/Cantor-Expansion
```

### 2. Create Virtual Environment

```bash
# Create virtual environment with Python 3.9
uv venv .venv --python 3.9
```

### 3. Activate Virtual Environment

```bash
# On macOS/Linux
source .venv/bin/activate

# On Windows
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
# Install dependencies (this project only uses standard library)
uv pip install -r requirements.txt
```

## Running the Program

### Basic Execution

```bash
# Make sure virtual environment is activated
source .venv/bin/activate

# Run the verification program
python cantor-2025-1000.py
```

### Alternative Execution

```bash
# Run directly with uv
uv run cantor-2025-1000.py
```

## Program Output

The program will output detailed verification steps:

1. **Prime Factorization**: Shows that `2025^1000 = 3^4000 * 5^2000`
2. **Factor Analysis**: Finds minimum `n` for `5^2000` constraint
3. **Constraint Checking**: Verifies `3^4000` constraint
4. **Coefficient Verification**: Ensures `a_n > 0`
5. **Minimality Check**: Confirms `n` is the smallest valid value

## Expected Results

The program should verify that:
- `n = 8013` is the correct answer
- `v_3(8013!) = 4000` (exactly 4000 factors of 3)
- `v_5(8013!) = 2000` (exactly 2000 factors of 5)
- `a_8013 > 0` (the last coefficient is positive)
- `n = 8013` is minimal (8012 doesn't work)

## File Structure

```
Cantor-Expansion/
├── cantor-2025-1000.py    # Main verification program
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore file
├── .venv/                # Virtual environment (created by uv)
└── README-PYTHON.md      # This file
```

## Troubleshooting

### Virtual Environment Issues

If you have issues with the virtual environment:

```bash
# Remove existing virtual environment
rm -rf .venv

# Recreate with uv
uv venv .venv --python 3.9

# Activate and try again
source .venv/bin/activate
```

### Python Version Issues

If Python 3.9 is not available:

```bash
# Check available Python versions
uv python list

# Use a different Python version
uv venv .venv --python 3.10  # or 3.11, 3.12, etc.
```

### Permission Issues

If you get permission errors:

```bash
# Make the script executable
chmod +x cantor-2025-1000.py

# Run with explicit Python
python3 cantor-2025-1000.py
```

## Mathematical Background

The program uses:

- **Legendre's Formula**: For calculating prime exponents in factorials
- **Binary Search**: For finding minimum `n` efficiently
- **Modular Arithmetic**: For verifying coefficient constraints
- **Prime Factorization**: For understanding divisibility requirements

## Performance Notes

- The program uses efficient algorithms to handle large numbers
- No external libraries are required (uses only Python standard library)
- Calculations are done using integer arithmetic to avoid floating-point errors
- The verification completes in seconds even for large factorials

## Development

To modify or extend the program:

1. Activate the virtual environment
2. Edit `cantor-2025-1000.py`
3. Run the program to test changes
4. The program includes comprehensive error handling and detailed output

## License

This verification program is part of the Cantor Expansion mathematical problem solution.
