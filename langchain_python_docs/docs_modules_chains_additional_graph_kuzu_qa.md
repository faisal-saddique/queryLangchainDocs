KuzuQAChain
===========

This notebook shows how to use LLMs to provide a natural language interface to [Kùzu](https://kuzudb.com) database.

[Kùzu](https://kuzudb.com) is an in-process property graph database management system. You can simply install it with `pip`:

    pip install kuzu

Once installed, you can simply import it and start creating a database on the local machine and connect to it:

    import kuzudb = kuzu.Database("test_db")conn = kuzu.Connection(db)

First, we create the schema for a simple movie database:

    conn.execute("CREATE NODE TABLE Movie (name STRING, PRIMARY KEY(name))")conn.execute(    "CREATE NODE TABLE Person (name STRING, birthDate STRING, PRIMARY KEY(name))")conn.execute("CREATE REL TABLE ActedIn (FROM Person TO Movie)")

        <kuzu.query_result.QueryResult at 0x1066ff410>

Then we can insert some data.

    conn.execute("CREATE (:Person {name: 'Al Pacino', birthDate: '1940-04-25'})")conn.execute("CREATE (:Person {name: 'Robert De Niro', birthDate: '1943-08-17'})")conn.execute("CREATE (:Movie {name: 'The Godfather'})")conn.execute("CREATE (:Movie {name: 'The Godfather: Part II'})")conn.execute(    "CREATE (:Movie {name: 'The Godfather Coda: The Death of Michael Corleone'})")conn.execute(    "MATCH (p:Person), (m:Movie) WHERE p.name = 'Al Pacino' AND m.name = 'The Godfather' CREATE (p)-[:ActedIn]->(m)")conn.execute(    "MATCH (p:Person), (m:Movie) WHERE p.name = 'Al Pacino' AND m.name = 'The Godfather: Part II' CREATE (p)-[:ActedIn]->(m)")conn.execute(    "MATCH (p:Person), (m:Movie) WHERE p.name = 'Al Pacino' AND m.name = 'The Godfather Coda: The Death of Michael Corleone' CREATE (p)-[:ActedIn]->(m)")conn.execute(    "MATCH (p:Person), (m:Movie) WHERE p.name = 'Robert De Niro' AND m.name = 'The Godfather: Part II' CREATE (p)-[:ActedIn]->(m)")

        <kuzu.query_result.QueryResult at 0x107016210>

Creating `KuzuQAChain`[​](#creating-kuzuqachain "Direct link to creating-kuzuqachain")
--------------------------------------------------------------------------------------

We can now create the `KuzuGraph` and `KuzuQAChain`. To create the `KuzuGraph` we simply need to pass the database object to the `KuzuGraph` constructor.

    from langchain.chat_models import ChatOpenAIfrom langchain.graphs import KuzuGraphfrom langchain.chains import KuzuQAChain

    graph = KuzuGraph(db)

    chain = KuzuQAChain.from_llm(ChatOpenAI(temperature=0), graph=graph, verbose=True)

Refresh graph schema information[​](#refresh-graph-schema-information "Direct link to Refresh graph schema information")
------------------------------------------------------------------------------------------------------------------------

If the schema of database changes, you can refresh the schema information needed to generate Cypher statements.

    # graph.refresh_schema()

    print(graph.get_schema)

        Node properties: [{'properties': [('name', 'STRING')], 'label': 'Movie'}, {'properties': [('name', 'STRING'), ('birthDate', 'STRING')], 'label': 'Person'}]    Relationships properties: [{'properties': [], 'label': 'ActedIn'}]    Relationships: ['(:Person)-[:ActedIn]->(:Movie)']    

Querying the graph[​](#querying-the-graph "Direct link to Querying the graph")
------------------------------------------------------------------------------

We can now use the `KuzuQAChain` to ask question of the graph

    chain.run("Who played in The Godfather: Part II?")

                > Entering new  chain...    Generated Cypher:    MATCH (p:Person)-[:ActedIn]->(m:Movie {name: 'The Godfather: Part II'}) RETURN p.name    Full Context:    [{'p.name': 'Al Pacino'}, {'p.name': 'Robert De Niro'}]        > Finished chain.    'Al Pacino and Robert De Niro both played in The Godfather: Part II.'

    chain.run("Robert De Niro played in which movies?")

                > Entering new  chain...    Generated Cypher:    MATCH (p:Person {name: 'Robert De Niro'})-[:ActedIn]->(m:Movie)    RETURN m.name    Full Context:    [{'m.name': 'The Godfather: Part II'}]        > Finished chain.    'Robert De Niro played in The Godfather: Part II.'

    chain.run("Robert De Niro is born in which year?")

                > Entering new  chain...    Generated Cypher:    MATCH (p:Person {name: 'Robert De Niro'})-[:ActedIn]->(m:Movie)    RETURN p.birthDate    Full Context:    [{'p.birthDate': '1943-08-17'}]        > Finished chain.    'Robert De Niro was born on August 17, 1943.'

    chain.run("Who is the oldest actor who played in The Godfather: Part II?")

                > Entering new  chain...    Generated Cypher:    MATCH (p:Person)-[:ActedIn]->(m:Movie{name:'The Godfather: Part II'})    WITH p, m, p.birthDate AS birthDate    ORDER BY birthDate ASC    LIMIT 1    RETURN p.name    Full Context:    [{'p.name': 'Al Pacino'}]        > Finished chain.    'The oldest actor who played in The Godfather: Part II is Al Pacino.'