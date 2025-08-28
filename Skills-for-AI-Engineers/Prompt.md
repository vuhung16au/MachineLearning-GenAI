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


