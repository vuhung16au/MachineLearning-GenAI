# Refactor `extract_skills.py` so that users can run from a specific step.

Currently, `extract_skills.py` has several steps. We want to refactor it so that users can run from a specific step.

I want to skip the steps that have already been completed.
I want to skip the data scraping steps and proceed with the skills extraction step.

You can implement the refactoring by adding a new argument to the `extract_skills.py` script.

E.g 

python extract_skills.py --step 2
python extract_skills.py --step 3
python extract_skills.py --step 4
python extract_skills.py --step 5
python extract_skills.py --step 6
python extract_skills.py --step 7

Implement: `python extract_skills.py --help` to show the help message.

---
# Delete markdown format

Delete markdown format in "Key Findings" when you export to png file (skills_analysis_html.png)

E.g
If text is "**Communication**" then delete the "**"
If text is "*Communication*" then delete the "*"
If text is "_Communication_" then delete the "_"
If text is "Communication" then keep the text as is
...

---



# Print the progress of the program

- Print when you start or finish each step
- Print when you start or finish `01.processing/page_<page_number>.html`
- Print when you start or finish `01.processing/<job-id>.html`. Print "X of Y jobs processed" to show the progress
- ...

---

# Implement a new version 

Step 1. Search and browse all Sydney jobs 
@Web https://www.seek.com.au/ai-engineer-jobs/in-All-Sydney-NSW

Step 2. Loop all the pages

Page number: from 1 to 25
@Web https://www.seek.com.au/ai-engineer-jobs/in-All-Sydney-NSW?page=1
@Web https://www.seek.com.au/ai-engineer-jobs/in-All-Sydney-NSW?page=2
@Web https://www.seek.com.au/ai-engineer-jobs/in-All-Sydney-NSW?page=3
… 
@Web https://www.seek.com.au/ai-engineer-jobs/in-All-Sydney-NSW?page=25
(Last page is 25) 

sleep 1 second between each page fetch

Fetch the pages and save them to `01.processing/page_<page_number>.html`

Step 3. Get all job description details 

The job description links on the left.

Format of links to JD 
- `https://www.seek.com.au/job/87042835`
Where `87042835` is the job ID 

Sleep 1 second


Save all JD links to a file 

`01.processing/jd-list.txt`

The format of the file is as follows:
```
https://www.seek.com.au/job/87042835
https://www.seek.com.au/job/xxxxxxxxxx
….
```

The URL, e.g `https://www.seek.com.au/job/87042835` may be already exists in the file.
- If it exists, skip it.
- If it does not exist, add it to the file.

Make sure 
- the file is sorted by the URL.
- no duplicated URLs in the file.

Step 4. Fetch job description details

Loop through `jd-list.txt` and fetch the job description details

- Fetch (wget, curl, etc.) the content of links listed in `jd-list.txt`
- Save it to `01.processing/<job-id>.html`
 - if the file already exists, skip it.
- Sleep 1 second between each fetch

Step 5. Extract the skills from the job descriptions

- Use `extract_skills.py` to extract the skills from the job descriptions
- Save the skills to `02.outputs/skills_analysis_summary.md`
- Save the skills to `02.outputs/skills_analysis_detail.md`

Step 6. Generate the report

- Use `generate_report.py` to generate the report
- Save the report to `02.outputs/report.md`

Step 7. Save the report 

Save the report to 
- `02.outputs/skills_analysis_summary.md` 
- `02.outputs/skills_analysis_detail.md`

Step 8. Generate wordcloud for the skills

Implement the wordcloud in the `extract_skills.py`
- Use `extract_skills.py` to generate the wordcloud for the skills
- Save the wordcloud to `02.outputs/skills_wordcloud.png`

Step 9. Generate a comprehensive report as a dashboard

- Save the HTML report to `02.outputs/skills_analysis_html.png`
- Use tailwindcss to style the HTML report
- Use styles similar to @Web https://www.wealthfront.com/
- Size of the dashboard: Full HD - 1920 pixels in width by 1300 pixels in height

The design of the dashboard report should looks like:

Has 2 rows:

Top row:
- The word cloud of the skills
- A pie chart of top 5 skills
- 3 key findings (text)

2nd row: 
- TOP 10 MOST DEMANDED SKILLS
- 5 HIGH DEMAND SKILLS (>50% of jobs)
- 5 MEDIUM DEMAND SKILLS (15-50% of jobs)

--------------------------------

(Below: Old prompt for Phase 1)
# The objective 

The objective of this project is to create a tool that can be used to extract skills from job descriptions and generate a list of skills that are required for the job. 

- Language: Python 
- Use `/opt/homebrew/bin/python3.13` to create the virtual environment

- Use `.venv` to create the virtual environment
- Use `requirements.txt` to install the dependencies
- Libray: You decide 

# The output should have the following content:

## `02.outputs/skill_analysis_summary.md`: 

- ALL SKILLS REQUIRED FOR ALL JOBS (by frequency)
- High Demand (more than 50% of jobs require)
- Medium Demand (15 - 49% of jobs require)
- Lower Demand (1-14 jobs require)
- TOP 10 MOST DEMANDED SKILLS
- Key Insights

Turn the skill analysis summary into a markdown table.

# The output

The output should have the following content:

## `02.outputs/skill_analysis_summary.md`: 

- ALL SKILLS REQUIRED FOR ALL JOBS (by frequency)
- High Demand (more than 50% of jobs require)
- Medium Demand (15 - 49% of jobs require)
- Lower Demand (1-14 jobs require)
- TOP 10 MOST DEMANDED SKILLS
- Key Insights

Sample output: `o02.utputs/skill_analysis_summary.md`

## `skills_analysis_detail.md`

- TOP 10 MOST DEMANDED SKILLS
- SKILLS ANALYSIS
- ALL SKILLS BY FREQUENCY
- SKILLS BY JOB (Details)

Sample output: `skills_analysis_detail.md`

# The input 

Jobs descriptions are in the form of a text file: job_description.txt

Format of `job_description.txt` is as follows:
```
URL1
URL2
...
``` 

Sample `job_description.txt` is as follows:
```
https://www.seek.com.au/job/86772095
https://www.seek.com.au/job/86762902
...
```

## Input files processing 

- use `wget` command line to download the job descriptions from the URLs in `job_description.txt`
- use `beautifulsoup4` library to parse the job descriptions

Save all the downloaded job descriptions in the `00.inputs/job_descriptions` directory.

Save all the in-between files in the `01.processing` directory.

# Sample code: 
`extract_skills.py`

# Other requirements

- Create `README.md` to describe the project; how to set up and run the project
- Create `LICENSE.md` and claim the project is under the MIT license
- Create `requirements.txt` to describe the dependencies
- Create `.gitignore` for this Python project and ignore the `01.processing` directory

- Keep the code clean and readable
- Keep the project as simple as possible


