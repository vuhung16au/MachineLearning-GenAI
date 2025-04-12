# Prompt 1: Greet the LLM

This is the first prompt. You will use this prompt with your fav LLM.

You can use the following prompt with your favorite LLM, such as Gemini, ChatGPT, Grok to prepare for the project. Please ignore all the typos, grammar mistakes as the LLMs are smart enough to understand.

--- 

I have a database with table named "employees".

The connection string is: 
`DB_CONNECTION=postgresql://admin:xY7pQ1mR2z@localhost:5432/postgres`

The employees table on Posrgres in the public schema of the postgres database has the following structure:

Columns:

| Column     | Data Type        | Nullable | Primary Key | Default Value                       | Index        | Rows |
|------------|------------------|----------|-------------|-------------------------------------|--------------|------|
| id         | INTEGER (int4)   | No       | Yes         | nextval('employees_id_seq'::regclass) | UNIQUE (PK)  | 102  |
| first_name | VARCHAR(50)      | Yes      | No          |                                     |              |      |
| last_name  | VARCHAR(50)      | Yes      | No          |                                     |              |      |
| email      | VARCHAR(100)     | Yes      | No          |                                     |              |      |
| hire_date  | DATE             | Yes      | No          |                                     |              |      |

My objective is to build an app that can list/modify/add/delete employees information.

The tech stack I want to use 

Backend: Python/Flask (use latest stable fixed version) for implementing Restful API
Frontend: AngularJS (use latest stable fixed version) (and add more if you want)

The IDE is VS Code

I will use VS Code with Agent mode as my coding assisstant.

For the first step, I only need to build and test it on my localhost. 

Please help me how to prepare the development environemnt. this app.

List all the commands I need to run.
List the folder structure on backend and frontend.

Help me create a list of features for this program, using Markdown table format.

Response each question one by one, ask me before you move to the next question. Don't response until I say "Next"

# Prompt 2: Setup Development Environment

Follow the environment setup guide you got in previous response, with the help of the Agent, setup your development environment.

# Prompt 3: Implement the Features

(Ask VS Code Agent - in *Agent* mode)
Please implement all the features listed in the file `FeatureList.md`
