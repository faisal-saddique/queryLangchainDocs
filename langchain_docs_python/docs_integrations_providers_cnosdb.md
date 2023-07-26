CnosDB
======

> [CnosDB](https://github.com/cnosdb/cnosdb) is an open source distributed time series database with high performance, high compression rate and high ease of use.

Installation and Setup[](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

    pip install cnos-connector

Connecting to CnosDB[](#connecting-to-cnosdb "Direct link to Connecting to CnosDB")
------------------------------------------------------------------------------------

You can connect to CnosDB using the `SQLDatabase.from_cnosdb()` method.

### Syntax[](#syntax "Direct link to Syntax")

    def SQLDatabase.from_cnosdb(url: str = "127.0.0.1:8902",                              user: str = "root",                              password: str = "",                              tenant: str = "cnosdb",                              database: str = "public")

Args:

1.  url (str): The HTTP connection host name and port number of the CnosDB service, excluding "http://" or "https://", with a default value of "127.0.0.1:8902".
2.  user (str): The username used to connect to the CnosDB service, with a default value of "root".
3.  password (str): The password of the user connecting to the CnosDB service, with a default value of "".
4.  tenant (str): The name of the tenant used to connect to the CnosDB service, with a default value of "cnosdb".
5.  database (str): The name of the database in the CnosDB tenant.

Examples[](#examples "Direct link to Examples")
------------------------------------------------

    # Connecting to CnosDB with SQLDatabase Wrapperfrom langchain import SQLDatabasedb = SQLDatabase.from_cnosdb()

    # Creating a OpenAI Chat LLM Wrapperfrom langchain.chat_models import ChatOpenAIllm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

### SQL Database Chain[](#sql-database-chain "Direct link to SQL Database Chain")

This example demonstrates the use of the SQL Chain for answering a question over a CnosDB.

    from langchain import SQLDatabaseChaindb_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)db_chain.run(    "What is the average temperature of air at station XiaoMaiDao between October 19, 2022 and Occtober 20, 2022?")

    > Entering new  chain...What is the average temperature of air at station XiaoMaiDao between October 19, 2022 and Occtober 20, 2022?SQLQuery:SELECT AVG(temperature) FROM air WHERE station = 'XiaoMaiDao' AND time >= '2022-10-19' AND time < '2022-10-20'SQLResult: [(68.0,)]Answer:The average temperature of air at station XiaoMaiDao between October 19, 2022 and October 20, 2022 is 68.0.> Finished chain.

### SQL Database Agent[](#sql-database-agent "Direct link to SQL Database Agent")

This example demonstrates the use of the SQL Database Agent for answering questions over a CnosDB.

    from langchain.agents import create_sql_agentfrom langchain.agents.agent_toolkits import SQLDatabaseToolkittoolkit = SQLDatabaseToolkit(db=db, llm=llm)agent = create_sql_agent(llm=llm, toolkit=toolkit, verbose=True)

    agent.run(    "What is the average temperature of air at station XiaoMaiDao between October 19, 2022 and Occtober 20, 2022?")

    > Entering new  chain...Action: sql_db_list_tablesAction Input: ""Observation: airThought:The "air" table seems relevant to the question. I should query the schema of the "air" table to see what columns are available.Action: sql_db_schemaAction Input: "air"Observation:CREATE TABLE air (    pressure FLOAT,    station STRING,    temperature FLOAT,    time TIMESTAMP,    visibility FLOAT)/*3 rows from air table:pressure    station temperature time    visibility75.0    XiaoMaiDao  67.0    2022-10-19T03:40:00 54.077.0    XiaoMaiDao  69.0    2022-10-19T04:40:00 56.076.0    XiaoMaiDao  68.0    2022-10-19T05:40:00 55.0*/Thought:The "temperature" column in the "air" table is relevant to the question. I can query the average temperature between the specified dates.Action: sql_db_queryAction Input: "SELECT AVG(temperature) FROM air WHERE station = 'XiaoMaiDao' AND time >= '2022-10-19' AND time <= '2022-10-20'"Observation: [(68.0,)]Thought:The average temperature of air at station XiaoMaiDao between October 19, 2022 and October 20, 2022 is 68.0.Final Answer: 68.0> Finished chain.