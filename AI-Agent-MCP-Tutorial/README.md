# What is This

This demonstrates Vibe practice and how an AI Agent can speed-up your development.

It probably won't work on the first run, especially without a good architectural understanding of the mentioned tech stack. So, grab a coffee, try it yourself, and good luck.

# How to Run This Repository/Tutorial 

- Install [Visual Studio Code](https://code.visualstudio.com/)
- Enable VS Code [Agent Mode](https://code.visualstudio.com/blogs/2025/04/07/agentMode)

- Install Postgres and create a table, create and/or import sample data. You can use [Docker Postgres](https://github.com/docker/awesome-compose/tree/master/postgresql-pgadmin) and a sample Docker Compose can be found under folder `postgresql-pgadmin`

In this tutorial, I used: 

```bash
$docker run --name macpostgres -e POSTGRES_PASSWORD=xY7pQ1mR2z -d postgres
```

You can use `create_insert_employees.sql` to create the table and populate sample data

Put the connection string to `.env` and added to the prompt contexts.

MCP Server Configuration
```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-postgres",
        "postgresql://admin:xY7pQ1mR2z@localhost:5432/postgres"
      ]
    }
  }
}
```

- (Refer to prompt.md) Setup environment with the help of Agent Mode. A sample reponse can be found at `Prompt1-Response-Sample-Grok.md`
- Feed the Agent with the list of features (or user stories) you want to implement, grab a coffee (this can take a while)
- Boom! It is done. Happy fixing with AI- Generated codes.

# Agent in Action
(implementing VS Agent Mode to generate JS code)

![implementing VS Agent Mode to generate JS code)](VS-CodeAgent-Mode.png)