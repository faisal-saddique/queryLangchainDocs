SQL
===

This example demonstrates the use of the `SQLDatabaseChain` for answering questions over a SQL database.

This example uses Chinook database, which is a sample database available for SQL Server, Oracle, MySQL, etc.

Set up[](#set-up "Direct link to Set up")
------------------------------------------

First install `typeorm`:

    npm install typeorm

Then install the dependencies needed for your database. For example, for SQLite:

    npm install sqlite3

For other databases see [https://typeorm.io/#installation](https://typeorm.io/#installation)

Finally follow the instructions on [https://database.guide/2-sample-databases-sqlite/](https://database.guide/2-sample-databases-sqlite/) to get the sample database for this example.

    import { DataSource } from "typeorm";import { OpenAI } from "langchain/llms/openai";import { SqlDatabase } from "langchain/sql_db";import { SqlDatabaseChain } from "langchain/chains/sql_db";/** * This example uses Chinook database, which is a sample database available for SQL Server, Oracle, MySQL, etc. * To set it up follow the instructions on https://database.guide/2-sample-databases-sqlite/, placing the .db file * in the examples folder. */const datasource = new DataSource({  type: "sqlite",  database: "Chinook.db",});const db = await SqlDatabase.fromDataSourceParams({  appDataSource: datasource,});const chain = new SqlDatabaseChain({  llm: new OpenAI({ temperature: 0 }),  database: db,});const res = await chain.run("How many tracks are there?");console.log(res);// There are 3503 tracks.

#### API Reference:

*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [SqlDatabase](/docs/api/sql_db/classes/SqlDatabase) from `langchain/sql_db`
*   [SqlDatabaseChain](/docs/api/chains_sql_db/classes/SqlDatabaseChain) from `langchain/chains/sql_db`

You can include or exclude tables when creating the `SqlDatabase` object to help the chain focus on the tables you want. It can also reduce the number of tokens used in the chain.

    const db = await SqlDatabase.fromDataSourceParams({  appDataSource: datasource,  includesTables: ["Track"],});

If desired, you can return the used SQL command when calling the chain.

    import { DataSource } from "typeorm";import { OpenAI } from "langchain/llms/openai";import { SqlDatabase } from "langchain/sql_db";import { SqlDatabaseChain } from "langchain/chains/sql_db";/** * This example uses Chinook database, which is a sample database available for SQL Server, Oracle, MySQL, etc. * To set it up follow the instructions on https://database.guide/2-sample-databases-sqlite/, placing the .db file * in the examples folder. */const datasource = new DataSource({  type: "sqlite",  database: "Chinook.db",});const db = await SqlDatabase.fromDataSourceParams({  appDataSource: datasource,});const chain = new SqlDatabaseChain({  llm: new OpenAI({ temperature: 0 }),  database: db,  sqlOutputKey: "sql",});const res = await chain.call({ query: "How many tracks are there?" });/* Expected result: * { *   result: ' There are 3503 tracks.', *   sql: ' SELECT COUNT(*) FROM "Track";' * } */console.log(res);

#### API Reference:

*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [SqlDatabase](/docs/api/sql_db/classes/SqlDatabase) from `langchain/sql_db`
*   [SqlDatabaseChain](/docs/api/chains_sql_db/classes/SqlDatabaseChain) from `langchain/chains/sql_db`

Custom prompt[](#custom-prompt "Direct link to Custom prompt")
---------------------------------------------------------------

You can also customize the prompt that is used. Here is an example prompting the model to understand that "foobar" is the same as the Employee table:

    import { DataSource } from "typeorm";import { OpenAI } from "langchain/llms/openai";import { SqlDatabase } from "langchain/sql_db";import { SqlDatabaseChain } from "langchain/chains/sql_db";import { PromptTemplate } from "langchain/prompts";const template = `Given an input question, first create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.Use the following format:Question: "Question here"SQLQuery: "SQL Query to run"SQLResult: "Result of the SQLQuery"Answer: "Final answer here"Only use the following tables:{table_info}If someone asks for the table foobar, they really mean the employee table.Question: {input}`;const prompt = PromptTemplate.fromTemplate(template);/** * This example uses Chinook database, which is a sample database available for SQL Server, Oracle, MySQL, etc. * To set it up follow the instructions on https://database.guide/2-sample-databases-sqlite/, placing the .db file * in the examples folder. */const datasource = new DataSource({  type: "sqlite",  database: "data/Chinook.db",});const db = await SqlDatabase.fromDataSourceParams({  appDataSource: datasource,});const chain = new SqlDatabaseChain({  llm: new OpenAI({ temperature: 0 }),  database: db,  sqlOutputKey: "sql",  prompt,});const res = await chain.call({  query: "How many employees are there in the foobar table?",});console.log(res);/*  {    result: ' There are 8 employees in the foobar table.',    sql: ' SELECT COUNT(*) FROM Employee;'  }*/

#### API Reference:

*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [SqlDatabase](/docs/api/sql_db/classes/SqlDatabase) from `langchain/sql_db`
*   [SqlDatabaseChain](/docs/api/chains_sql_db/classes/SqlDatabaseChain) from `langchain/chains/sql_db`
*   [PromptTemplate](/docs/api/prompts/classes/PromptTemplate) from `langchain/prompts`