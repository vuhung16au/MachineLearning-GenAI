# Use Case

See `README.md`

# Requirements and Commandline Arguments

Here’s the improved PDF Split script prompt converted into a Markdown table format, summarizing each feature and its details:

| **Feature**                | **Description**                                                                 |
|----------------------------|---------------------------------------------------------------------------------|
| **Input files**            | Process all `.pdf` files (case insensitive) in `./input` (default). Customizable with `--input-folder` or `-i`. <br> **Errors**: Exit with "Error: <path> is not a valid directory" if invalid; exit with "Warning: No PDF files found in '<path>'" if empty (unless `--dry-run`). |
| **Output folder**          | Save split PDFs to `./output/` (default). Customizable with `--output-folder` or `-o`. <br> **Errors**: Create folder if missing; exit with "Error: Cannot create/write to '<path>': <reason>" if issues arise. |
| **Number of pages per split** | Default: 1 page per file. Customizable with `--number-of-pages` or `-n`. <br> **Errors**: Exit with "Error: Number of pages must be positive" if invalid; warn "Requested pages (<n>) exceed total (<total>); creating one file" if exceeded. |
| **File naming**            | Default: `Input-001.pdf`, etc. (zero-padded). Custom `--prefix` and `--start-index` (default: 1). <br> **Errors**: Exit with "Error: Prefix contains invalid characters" or "Error: Start index must be positive" if invalid; skip with "Error: Filename too long" if limits exceeded. |
| **Overwrite protection**   | Skip if output files exist unless `--force` or `-f` used; warn "Output file '<filename>' exists". Optional `--clean` (with `--force`) deletes output folder contents. <br> **Errors**: Skip with "Error: Cannot overwrite '<filename>': <reason>" if fails. |
| **Progress reporting**     | Show progress bar or percentage; use text updates (e.g., "Processed page X/Y") in non-interactive environments. <br> **Errors**: Log failures silently if display fails. |
| **Error handling**         | - Invalid PDFs: Skip with "Error: Cannot read '<filename>': Invalid PDF". <br> - Encrypted PDFs: Skip with "Error: '<filename>' is encrypted; not supported". <br> - Memory issues: Skip with "Error: Insufficient memory; try smaller --number-of-pages". <br> - Permissions: Skip with "Error: No permission for '<filename>'". <br> - Write errors: Skip with "Error: Cannot write '<filename>': <reason>" (e.g., disk full). <br> - Argument validation: Exit with specific errors (e.g., "Error: Invalid path"). <br> - Dependencies: Exit with "Error: Install pypdf: pip install pypdf" if missing. |
| **Help flag**              | Print usage, flags, defaults, examples, and log file note with `--help` or `-h`. <br> **Errors**: Show help even if other arguments are invalid. |
| **Dry run**                | Simulate with `--dry-run`, validating inputs, permissions, disk space. Show planned actions. <br> **Errors**: Report issues (e.g., "Dry run: Cannot write to <path>"). |
| **Logging**                | Save `logs/split_log.txt` (configurable via `--log-file`). Create `logs` folder if needed. Log actions, errors, warnings, timestamps. <br> **Errors**: Warn "Cannot write log; using console" if fails. |
| **Dependencies**           | Use `pypdf` library, Python 3.8+. <br> **Errors**: Exit with "Error: Install pypdf: pip install pypdf" if missing. |

# **Example Runs**:

1. **Basic run**:
   - Input: `./input/Before.pdf` (10 pages)
   - Command: `python SplitPDF.py`
   - Output: 10 files in `./output/`:
     - `./output/Before-001.pdf`, `./output/Before-002.pdf`, ..., `./output/Before-010.pdf`
     - Each file contains 1 page.

2. **Custom pages and prefix**:
   - Input: `./input/Before.pdf` (10 pages)
   - Command: `python SplitPDF.py -n 2 --prefix Payslip`
   - Output: 5 files in `./output/`:
     - `./output/Payslip-001.pdf` (pages 1-2), `./output/Payslip-002.pdf` (pages 3-4), ..., `./output/Payslip-005.pdf` (pages 9-10).

3. **Custom folders and dry run**:
   - Command: `python SplitPDF.py -i ./my_pdfs -o ./split_files --dry-run`
   - Output: Prints planned actions (e.g., files to be created) without modifying or creating files.

4. **Help**:
   - Command: `python SplitPDF.py --help`
   - Output: Displays usage instructions, all flags, defaults, and examples.

**Implementation notes**:
- Ensure the program is efficient for large PDFs (e.g., 60+ pages).
- Use `argparse` for command-line argument parsing.
- Include input validation (e.g., positive integers for `-n` and `--start-index`).
- Provide user-friendly error messages (e.g., "Input folder not found" or "Invalid PDF detected").

**Error handling (general)**:
  - **Invalid PDFs**: If a PDF is corrupted or unreadable, display "Error: Cannot read '<filename>': Invalid PDF" and skip to the next file.
  - **Memory issues**: Handle large PDFs (e.g., 60+ pages) gracefully; if memory errors occur, display "Error: Insufficient memory for '<filename>'; try reducing --number-of-pages" and skip the file.
  - **Permission errors**: If a PDF file is not readable (e.g., no permissions), display "Error: No read permission for '<filename>'" and skip.
  - **Output write errors**: If writing an output file fails (e.g., disk full), display "Error: Cannot write '<filename>': <reason>" and skip.
  - **Unexpected errors**: Catch unhandled exceptions, display "Unexpected error: <details>", log the error, and continue with the next file if possible.
  - **Validation**: Before processing, validate all command-line arguments; if any are invalid (e.g., negative numbers, malformed paths), display a specific error and exit.

# Unit Test 

- PyUnit
- Test all the arguments 

# Prompt (Simple Version)

```
Write a program to split PDF files

- Input files: All files with extensions .pdf (case insensitive) under folder "./input" (default). This can be used with "--input-folder" or "-i"
- Output folder: Splitted pdf files will be saved to "./output/" (default). This can be used with "--output-folder" or "-o"
- Number of pages to split: a) default is 1, b) and the number of pages in splitted pdf files can be set with "--number-of-pages" or "-n"
- include "--help" or "-h" to print instruction

Example run: 

Says under folder './input/', there is only one file 'Before.pdf' with 10 pages

When run `python SplitPDF.py`
the file 'Before.pdf' will be splitted into 10 files and saved to 
'./output/Before-01.pdf'
'./output/Before-02.pdf'
...
'./output/Before-10.pdf'

```