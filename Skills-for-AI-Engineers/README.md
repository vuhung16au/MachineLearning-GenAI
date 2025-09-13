# AI Engineer Skills Analysis Pipeline

A comprehensive Python pipeline that scrapes AI Engineer job listings from Seek.com.au in Sydney, extracts skills from job descriptions, and generates beautiful visualizations and reports. The tool analyzes skill frequency and demand levels across multiple job postings, creating interactive dashboards and comprehensive reports.

## Features

- **Complete Web Scraping**: Automatically scrapes all 25 pages of Sydney AI Engineer jobs from Seek.com.au
- **Intelligent Job Link Extraction**: Extracts and deduplicates job description links
- **Polite Crawling**: Implements 1-second delays between requests to respect server resources
- **Advanced Skill Extraction**: Pattern matching + context heuristics for comprehensive skill detection
- **Visual Analytics**: Generates word clouds and interactive pie charts
- **Beautiful Dashboard**: Full HD (1920x1300) HTML dashboard with Tailwind CSS styling
- **Comprehensive Analysis**: Categorizes skills by demand level (High, Medium, Lower)
- **Multiple Output Formats**: Markdown reports, HTML dashboard, and PNG visualizations
- **Clean Project Structure**: Organized directory structure for easy navigation

## Project Structure

```text
Skills-for-AI-Engineers/
├── 00.inputs/                       # Input files (legacy)
├── 01.processing/                   # Scraped data and processing files
│   ├── page_1.html to page_25.html  # Scraped job listing pages
│   ├── jd-list.txt                  # Extracted job description links
│   └── <job_id>.html                # Individual job descriptions
├── 02.outputs/                      # Generated reports and visualizations
│   ├── skills_analysis_summary.md   # Summary report with tables
│   ├── skills_analysis_detail.md    # Detailed analysis report
│   ├── skills_wordcloud.png         # Skills word cloud visualization
│   ├── skills_analysis_dashboard.html # Interactive HTML dashboard
│   ├── skills_analysis_html.png     # Dashboard as PNG image
│   └── report.md                    # Final comprehensive report
├── scrape_sydney_jobs.py            # Web scraper for Seek.com.au
├── extract_skills.py                # Skills extraction and analysis
├── generate_report.py               # Report and dashboard generation
├── run_pipeline.py                  # Complete pipeline orchestrator
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
└── LICENSE.md                       # MIT License
```

## Prerequisites

- Python 3.11+ installed (macOS, Linux, or Windows)
  - macOS/Linux: `python3 --version`
  - Windows: `py --version` or `python --version`
- `pip` available to install dependencies (bundled with Python)
- Internet connection
- Chrome browser (for PNG generation - optional)

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

### Quick Start - Run Complete Pipeline

```bash
# Ensure virtual environment is activated
source .venv/bin/activate

# Run the complete pipeline
python run_pipeline.py
```

This will automatically:
1. Scrape all 25 pages of Sydney AI Engineer jobs from Seek.com.au
2. Extract job description links and save to `01.processing/jd-list.txt`
3. Fetch individual job descriptions
4. Extract skills and generate wordcloud
5. Generate comprehensive reports and dashboard

### Individual Scripts

You can also run individual components:

```bash
# Step 1-4: Scrape jobs and extract links
python scrape_sydney_jobs.py

# Step 5: Extract skills and generate wordcloud
python extract_skills.py

# Step 6-7: Generate reports and dashboard
python generate_report.py
```

### View Results

- **Interactive Dashboard**: `02.outputs/skills_analysis_dashboard.html`
- **Word Cloud**: `02.outputs/skills_wordcloud.png`
- **Summary Report**: `02.outputs/skills_analysis_summary.md`
- **Detailed Report**: `02.outputs/skills_analysis_detail.md`
- **Final Report**: `02.outputs/report.md`
- **Job Links**: `01.processing/jd-list.txt`
- **Job Descriptions**: `01.processing/<job_id>.html`

## How It Works

### Web Scraping

- Scrapes all 25 pages of Sydney AI Engineer jobs from Seek.com.au
- Uses polite crawling with 1-second delays between requests
- Saves each page as `01.processing/page_<number>.html`
- Extracts job description links and saves to `01.processing/jd-list.txt`
- Fetches individual job descriptions and saves as `01.processing/<job_id>.html`

### Text Extraction

- Parses HTML using BeautifulSoup (`html.parser`)
- Removes scripts and styles
- Normalizes whitespace

### Skill Extraction

- Regex patterns for common technologies, cloud, databases, AI/ML, DevOps, etc.
- Keyword-window heuristic around requirement phrases
- Cleans noise and normalizes skills case-insensitively (e.g., "Communication" == "communication")

### Analysis & Visualization

- Counts in how many jobs each skill appears (job-level presence, not total occurrences)
- Computes percentages as: `(jobs_with_skill / total_jobs) * 100`
- Categorizes:
  - High Demand: > 50% of jobs
  - Medium Demand: 15–50% of jobs
  - Lower Demand: < 15% of jobs
- Generates word cloud visualization of all skills
- Creates interactive pie charts for top skills
- Produces comprehensive HTML dashboard with Tailwind CSS styling
- Saves dashboard as PNG image (1920x1300 resolution)

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
