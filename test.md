# Databricks

This notebook covers how to connect to the [Databricks
runtimes](https://docs.databricks.com/runtime/index.html) and [Databricks
SQL](https://www.databricks.com/product/databricks-sql) using the SQLDatabase
wrapper of LangChain. It is broken into 3 parts: installation and setup,
connecting to Databricks, and examples.

## Installation and Setup

pip install databricks-sql-connector


## Connecting to Databricks

You can connect to [Databricks
runtimes](https://docs.databricks.com/runtime/index.html) and [Databricks
SQL](https://www.databricks.com/product/databricks-sql) using the
`SQLDatabase.from_databricks()` method.

### Syntax



SQLDatabase.from_databricks(    catalog: str,    schema: str,    host: Optional[str] = None,    api_token: Optional[str] = None,    warehouse_id: Optional[str] = None,    cluster_id: Optional[str] = None,    engine_args: Optional[dict] = None,    **kwargs: Any)


### Required Parameters

  * `catalog`: The catalog name in the Databricks database.
  * `schema`: The schema name in the catalog.

### Optional Parameters

There following parameters are optional. When executing the method in a
Databricks notebook, you don't need to provide them in most of the cases.

  * `host`: The Databricks workspace hostname, excluding 'https://' part. Defaults to 'DATABRICKS_HOST' environment variable or current workspace if in a Databricks notebook.
  * `api_token`: The Databricks personal access token for accessing the Databricks SQL warehouse or the cluster. Defaults to 'DATABRICKS_TOKEN' environment variable or a temporary one is generated if in a Databricks notebook.
  * `warehouse_id`: The warehouse ID in the Databricks SQL.
  * `cluster_id`: The cluster ID in the Databricks Runtime. If running in a Databricks notebook and both 'warehouse_id' and 'cluster_id' are None, it uses the ID of the cluster the notebook is attached to.
  * `engine_args`: The arguments to be used when connecting Databricks.
  * `**kwargs`: Additional keyword arguments for the `SQLDatabase.from_uri` method.

## Examples



# Connecting to Databricks with SQLDatabase wrapperfrom langchain import SQLDatabasedb = SQLDatabase.from_databricks(catalog="samples", schema="nyctaxi")

# Creating a OpenAI Chat LLM wrapperfrom langchain.chat_models import ChatOpenAIllm = ChatOpenAI(temperature=0, model_name="gpt-4")


### SQL Chain example

This example demonstrates the use of the [SQL
Chain](https://python.langchain.com/en/latest/modules/chains/examples/sqlite.html)
for answering a question over a Databricks database.



from langchain import SQLDatabaseChaindb_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

db_chain.run(    "What is the average duration of taxi rides that start between midnight and 6am?")

> Entering new SQLDatabaseChain chain...    What is the average duration of taxi rides that start between midnight and 6am?    SQLQuery:SELECT AVG(UNIX_TIMESTAMP(tpep_dropoff_datetime) - UNIX_TIMESTAMP(tpep_pickup_datetime)) as avg_duration    FROM trips    WHERE HOUR(tpep_pickup_datetime) >= 0 AND HOUR(tpep_pickup_datetime) < 6    SQLResult: [(987.8122786304605,)]    Answer:The average duration of taxi rides that start between midnight and 6am is 987.81 seconds.    > Finished chain.    'The average duration of taxi rides that start between midnight and 6am is 987.81 seconds.'


### SQL Database Agent example

This example demonstrates the use of the [SQL Database
Agent](/docs/modules/agents/toolkits/sql_database.html) for answering
questions over a Databricks database.



from langchain.agents import create_sql_agentfrom langchain.agents.agent_toolkits import SQLDatabaseToolkittoolkit = SQLDatabaseToolkit(db=db, llm=llm)agent = create_sql_agent(llm=llm, toolkit=toolkit, verbose=True)

agent.run("What is the longest trip distance and how long did it take?")

> Entering new AgentExecutor chain...    Action: list_tables_sql_db    Action Input:     Observation: trips    Thought:I should check the schema of the trips table to see if it has the necessary columns for trip distance and duration.    Action: schema_sql_db    Action Input: trips    Observation:     CREATE TABLE trips (        tpep_pickup_datetime TIMESTAMP,         tpep_dropoff_datetime TIMESTAMP,         trip_distance FLOAT,         fare_amount FLOAT,         pickup_zip INT,         dropoff_zip INT    ) USING DELTA        /*    3 rows from trips table:    tpep_pickup_datetime    tpep_dropoff_datetime   trip_distance   fare_amount pickup_zip  dropoff_zip    2016-02-14 16:52:13+00:00   2016-02-14 17:16:04+00:00   4.94    19.0    10282   10171    2016-02-04 18:44:19+00:00   2016-02-04 18:46:00+00:00   0.28    3.5 10110   10110    2016-02-17 17:13:57+00:00   2016-02-17 17:17:55+00:00   0.7 5.0 10103   10023    */    Thought:The trips table has the necessary columns for trip distance and duration. I will write a query to find the longest trip distance and its duration.    Action: query_checker_sql_db    Action Input: SELECT trip_distance, tpep_dropoff_datetime - tpep_pickup_datetime as duration FROM trips ORDER BY trip_distance DESC LIMIT 1    Observation: SELECT trip_distance, tpep_dropoff_datetime - tpep_pickup_datetime as duration FROM trips ORDER BY trip_distance DESC LIMIT 1    Thought:The query is correct. I will now execute it to find the longest trip distance and its duration.    Action: query_sql_db    Action Input: SELECT trip_distance, tpep_dropoff_datetime - tpep_pickup_datetime as duration FROM trips ORDER BY trip_distance DESC LIMIT 1    Observation: [(30.6, '0 00:43:31.000000000')]    Thought:I now know the final answer.    Final Answer: The longest trip distance is 30.6 miles and it took 43 minutes and 31 seconds.        > Finished chain.    'The longest trip distance is 30.6 miles and it took 43 minutes and 31 seconds.'


