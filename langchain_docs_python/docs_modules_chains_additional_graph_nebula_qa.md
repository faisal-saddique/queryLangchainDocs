NebulaGraphQAChain
==================

This notebook shows how to use LLMs to provide a natural language interface to NebulaGraph database.

You will need to have a running NebulaGraph cluster, for which you can run a containerized cluster by running the following script:

    curl -fsSL nebula-up.siwei.io/install.sh | bash

Other options are:

*   Install as a [Docker Desktop Extension](https://www.docker.com/blog/distributed-cloud-native-graph-database-nebulagraph-docker-extension/). See [here](https://docs.nebula-graph.io/3.5.0/2.quick-start/1.quick-start-workflow/)
*   NebulaGraph Cloud Service. See [here](https://www.nebula-graph.io/cloud)
*   Deploy from package, source code, or via Kubernetes. See [here](https://docs.nebula-graph.io/)

Once the cluster is running, we could create the SPACE and SCHEMA for the database.

    # connect ngql jupyter extension to nebulagraph# create a new space%ngql CREATE SPACE IF NOT EXISTS langchain(partition_num=1, replica_factor=1, vid_type=fixed_string(128));

    # Wait for a few seconds for the space to be created.%ngql USE langchain;

Create the schema, for full dataset, refer [here](https://www.siwei.io/en/nebulagraph-etl-dbt/).

    CREATE TAG IF NOT EXISTS movie(name string);CREATE TAG IF NOT EXISTS person(name string, birthdate string);CREATE EDGE IF NOT EXISTS acted_in();CREATE TAG INDEX IF NOT EXISTS person_index ON person(name(128));CREATE TAG INDEX IF NOT EXISTS movie_index ON movie(name(128));

Wait for schema creation to complete, then we can insert some data.

    INSERT VERTEX person(name, birthdate) VALUES "Al Pacino":("Al Pacino", "1940-04-25");INSERT VERTEX movie(name) VALUES "The Godfather II":("The Godfather II");INSERT VERTEX movie(name) VALUES "The Godfather Coda: The Death of Michael Corleone":("The Godfather Coda: The Death of Michael Corleone");INSERT EDGE acted_in() VALUES "Al Pacino"->"The Godfather II":();INSERT EDGE acted_in() VALUES "Al Pacino"->"The Godfather Coda: The Death of Michael Corleone":();

        UsageError: Cell magic `%%ngql` not found.

    from langchain.chat_models import ChatOpenAIfrom langchain.chains import NebulaGraphQAChainfrom langchain.graphs import NebulaGraph

    graph = NebulaGraph(    space="langchain",    username="root",    password="nebula",    address="127.0.0.1",    port=9669,    session_pool_size=30,)

Refresh graph schema information[](#refresh-graph-schema-information "Direct link to Refresh graph schema information")
------------------------------------------------------------------------------------------------------------------------

If the schema of database changes, you can refresh the schema information needed to generate nGQL statements.

    # graph.refresh_schema()

    print(graph.get_schema)

        Node properties: [{'tag': 'movie', 'properties': [('name', 'string')]}, {'tag': 'person', 'properties': [('name', 'string'), ('birthdate', 'string')]}]    Edge properties: [{'edge': 'acted_in', 'properties': []}]    Relationships: ['(:person)-[:acted_in]->(:movie)']    

Querying the graph[](#querying-the-graph "Direct link to Querying the graph")
------------------------------------------------------------------------------

We can now use the graph cypher QA chain to ask question of the graph

    chain = NebulaGraphQAChain.from_llm(    ChatOpenAI(temperature=0), graph=graph, verbose=True)

    chain.run("Who played in The Godfather II?")

                > Entering new NebulaGraphQAChain chain...    Generated nGQL:    MATCH (p:`person`)-[:acted_in]->(m:`movie`) WHERE m.`movie`.`name` == 'The Godfather II'    RETURN p.`person`.`name`    Full Context:    {'p.person.name': ['Al Pacino']}        > Finished chain.    'Al Pacino played in The Godfather II.'