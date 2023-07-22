SQL Agent Toolkit
=================

This example shows how to load and use an agent with a SQL toolkit.

Setup[​](#setup "Direct link to Setup")
---------------------------------------

You'll need to first install `typeorm`:

*   npm
*   Yarn
*   pnpm

    npm install typeorm

    yarn add typeorm

    pnpm add typeorm

Usage[​](#usage "Direct link to Usage")
---------------------------------------

    import { OpenAI } from "langchain/llms/openai";import { SqlDatabase } from "langchain/sql_db";import { createSqlAgent, SqlToolkit } from "langchain/agents/toolkits/sql";import { DataSource } from "typeorm";/** This example uses Chinook database, which is a sample database available for SQL Server, Oracle, MySQL, etc. * To set it up follow the instructions on https://database.guide/2-sample-databases-sqlite/, placing the .db file * in the examples folder. */export const run = async () => {  const datasource = new DataSource({    type: "sqlite",    database: "Chinook.db",  });  const db = await SqlDatabase.fromDataSourceParams({    appDataSource: datasource,  });  const model = new OpenAI({ temperature: 0 });  const toolkit = new SqlToolkit(db, model);  const executor = createSqlAgent(model, toolkit);  const input = `List the total sales per country. Which country's customers spent the most?`;  console.log(`Executing with input "${input}"...`);  const result = await executor.call({ input });  console.log(`Got output ${result.output}`);  console.log(    `Got intermediate steps ${JSON.stringify(      result.intermediateSteps,      null,      2    )}`  );  await datasource.destroy();};

#### API Reference:

*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [SqlDatabase](/docs/api/sql_db/classes/SqlDatabase) from `langchain/sql_db`
*   [createSqlAgent](/docs/api/agents_toolkits_sql/functions/createSqlAgent) from `langchain/agents/toolkits/sql`
*   [SqlToolkit](/docs/api/agents_toolkits_sql/classes/SqlToolkit) from `langchain/agents/toolkits/sql`