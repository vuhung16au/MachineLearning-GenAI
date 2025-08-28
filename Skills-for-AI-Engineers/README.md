# Job Description Skills Extractor

A Python tool that automatically downloads job descriptions from URLs and extracts skills from them. The tool analyzes skill frequency and demand levels across multiple job postings, generating comprehensive reports in markdown format.

## Features

- **Automatic Job Description Download**: Uses `wget` with a browser User-Agent
- **Polite crawling**: Waits 2 seconds between downloads
- **Duplicate handling**: Skips duplicate URLs by job ID
- **Skill Extraction**: Pattern matching + context heuristics
- **Comprehensive Analysis**: Categorizes skills by demand level (High, Medium, Lower)
- **Correct percentages**: Percentages are based on number of jobs containing each skill (never > 100%)
- **Markdown Reports**: Summary and detailed analysis reports
- **Clean Project Structure**

## Project Structure

```text
Skills-for-AI-Engineers/
├── 00.inputs/
│   └── job_description.txt          # URLs of job descriptions to analyze
├── 01.processing/                   # Downloaded job description HTML files
├── 02.outputs/
│   ├── skills_analysis_summary.md   # Summary report with tables
│   └── skills_analysis_detail.md    # Detailed analysis report
├── extract_skills.py                # Main script
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
└── LICENSE.md                       # MIT License
```

## Prerequisites

- Python 3.11+ installed (macOS, Linux, or Windows)
  - macOS/Linux: `python3 --version`
  - Windows: `py --version` or `python --version`
- `wget` installed and available on PATH (required by the script)
  - macOS: `brew install wget`
  - Ubuntu/Debian: `sudo apt-get install wget`
  - Fedora/CentOS: `sudo dnf install wget` (or `sudo yum install wget`)
  - Windows: `winget install GnuWin32.Wget` or `choco install wget`
- `pip` available to install dependencies (bundled with Python)
- Internet connection

## Installation

1. Navigate to project directory:

```bash
cd /path/to/Skills-for-AI-Engineers
```

1. Create a virtual environment:

```bash
python3 -m venv .venv
```

1. Activate the virtual environment:

```bash
source .venv/bin/activate
```

1. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### 1) Prepare Job Description URLs

Create or edit `00.inputs/job_description.txt` with one URL per line:

```text
https://www.seek.com.au/job/86772095
https://www.seek.com.au/job/86762902
https://www.seek.com.au/job/86770962
```

Notes:

- Duplicate lines or different variants of the same job URL are automatically deduplicated by job ID
- Non-HTTP lines are ignored

### 2) Run the Analysis

```bash
# Ensure virtual environment is activated
source .venv/bin/activate

python extract_skills.py
```

### 3) View Results

- Downloads (HTML): `01.processing/job_<JOB_ID>.html`
- Summary report: `02.outputs/skills_analysis_summary.md`
- Detailed report: `02.outputs/skills_analysis_detail.md`

## How It Works

### Downloading

- Reads URLs from `00.inputs/job_description.txt`
- Deduplicates by job ID (extracted from the URL path)
- Downloads with `wget` using a browser-like User-Agent
- Waits 2 seconds between downloads to be polite
- Saves to `01.processing/job_<JOB_ID>.html`

### Text Extraction

- Parses HTML using BeautifulSoup (`html.parser`)
- Removes scripts and styles
- Normalizes whitespace

### Skill Extraction

- Regex patterns for common technologies, cloud, databases, AI/ML, DevOps, etc.
- Keyword-window heuristic around requirement phrases
- Cleans noise and normalizes skills case-insensitively (e.g., "Communication" == "communication")

### Analysis

- Counts in how many jobs each skill appears (job-level presence, not total occurrences)
- Computes percentages as: `(jobs_with_skill / total_jobs) * 100`
- Categorizes:
  - High Demand: > 50% of jobs
  - Medium Demand: 15–50% of jobs
  - Lower Demand: < 15% of jobs
- Produces tables for Top 10, High/Medium/Lower demand, and detailed listings

## Supported Skills (examples)

- Programming: Python, Java, JavaScript, TypeScript, Go, Rust, etc.
- Frameworks: React, Angular, Django, Flask, Spring, etc.
- Cloud & DevOps: AWS, Azure, GCP, Kubernetes, Terraform, CI/CD, etc.
- Data & AI/ML: SQL/NoSQL, TensorFlow, PyTorch, LangChain, MLOps, etc.
- Soft skills: Communication, Leadership, Problem Solving, etc.

## Customization

### Add new skill patterns
 
Edit `skill_patterns` in `extract_skills.py`:

```python
skill_patterns = [
    r'\b(Your New Skill|Another Skill)\b',
    # ... existing patterns
]
```

### Adjust demand thresholds
 
In `generate_analysis()`:

```python
high_demand = {s: c for s, c in skill_counts.items() if skill_percentages[s] > 50}
medium_demand = {s: c for s, c in skill_counts.items() if 15 <= skill_percentages[s] <= 50}
lower_demand = {s: c for s, c in skill_counts.items() if skill_percentages[s] < 15}
```

## Troubleshooting

1. Download failures

- Ensure `wget` is installed and available on PATH
- Some sites may block automated requests; the script uses a browser UA and waits between requests

1. No skills found

- Add/adjust patterns to match domain-specific terms

1. Permissions

- Ensure the script can write to `01.processing/` and `02.outputs/`

## License

This project is licensed under the MIT License — see `LICENSE.md`.
