ArangoDB QA chain
=================

[![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hwchase17/langchain/blob/master/docs/extras/modules/chains/additional/graph_arangodb_qa.ipynb)

This notebook shows how to use LLMs to provide a natural language interface to an [ArangoDB](https://github.com/arangodb/arangodb#readme) database.

You can get a local ArangoDB instance running via the [ArangoDB Docker image](https://hub.docker.com/_/arangodb):

    docker run -p 8529:8529 -e ARANGO_ROOT_PASSWORD= arangodb/arangodb

An alternative is to use the [ArangoDB Cloud Connector package](https://github.com/arangodb/adb-cloud-connector#readme) to get a temporary cloud instance running:

    pip install python-arango # The ArangoDB Python Driverpip install adb-cloud-connector # The ArangoDB Cloud Instance provisionerpip install openaipip install langchain

    # Instantiate ArangoDB Databaseimport jsonfrom arango import ArangoClientfrom adb_cloud_connector import get_temp_credentialscon = get_temp_credentials()db = ArangoClient(hosts=con["url"]).db(    con["dbName"], con["username"], con["password"], verify=True)print(json.dumps(con, indent=2))

        Log: requesting new credentials...    Succcess: new credentials acquired    {      "dbName": "TUT3sp29s3pjf1io0h4cfdsq",      "username": "TUTo6nkwgzkizej3kysgdyeo8",      "password": "TUT9vx0qjqt42i9bq8uik4v9",      "hostname": "tutorials.arangodb.cloud",      "port": 8529,      "url": "https://tutorials.arangodb.cloud:8529"    }

    # Instantiate the ArangoDB-LangChain Graphfrom langchain.graphs import ArangoGraphgraph = ArangoGraph(db)

Populating the Database[](#populating-the-database "Direct link to Populating the Database")
---------------------------------------------------------------------------------------------

We will rely on the Python Driver to import our [GameOfThrones](https://github.com/arangodb/example-datasets/tree/master/GameOfThrones) data into our database.

    if db.has_graph("GameOfThrones"):    db.delete_graph("GameOfThrones", drop_collections=True)db.create_graph(    "GameOfThrones",    edge_definitions=[        {            "edge_collection": "ChildOf",            "from_vertex_collections": ["Characters"],            "to_vertex_collections": ["Characters"],        },    ],)documents = [    {        "_key": "NedStark",        "name": "Ned",        "surname": "Stark",        "alive": True,        "age": 41,        "gender": "male",    },    {        "_key": "CatelynStark",        "name": "Catelyn",        "surname": "Stark",        "alive": False,        "age": 40,        "gender": "female",    },    {        "_key": "AryaStark",        "name": "Arya",        "surname": "Stark",        "alive": True,        "age": 11,        "gender": "female",    },    {        "_key": "BranStark",        "name": "Bran",        "surname": "Stark",        "alive": True,        "age": 10,        "gender": "male",    },]edges = [    {"_to": "Characters/NedStark", "_from": "Characters/AryaStark"},    {"_to": "Characters/NedStark", "_from": "Characters/BranStark"},    {"_to": "Characters/CatelynStark", "_from": "Characters/AryaStark"},    {"_to": "Characters/CatelynStark", "_from": "Characters/BranStark"},]db.collection("Characters").import_bulk(documents)db.collection("ChildOf").import_bulk(edges)

        {'error': False,     'created': 4,     'errors': 0,     'empty': 0,     'updated': 0,     'ignored': 0,     'details': []}

Getting & Setting the ArangoDB Schema[](#getting--setting-the-arangodb-schema "Direct link to Getting & Setting the ArangoDB Schema")
--------------------------------------------------------------------------------------------------------------------------------------

An initial ArangoDB Schema is generated upon instantiating the `ArangoDBGraph` object. Below are the schema's getter & setter methods should you be interested in viewing or modifying the schema:

    # The schema should be empty here,# since `graph` was initialized prior to ArangoDB Data ingestion (see above).import jsonprint(json.dumps(graph.schema, indent=4))

        {        "Graph Schema": [],        "Collection Schema": []    }

    graph.set_schema()

    # We can now view the generated schemaimport jsonprint(json.dumps(graph.schema, indent=4))

        {        "Graph Schema": [            {                "graph_name": "GameOfThrones",                "edge_definitions": [                    {                        "edge_collection": "ChildOf",                        "from_vertex_collections": [                            "Characters"                        ],                        "to_vertex_collections": [                            "Characters"                        ]                    }                ]            }        ],        "Collection Schema": [            {                "collection_name": "ChildOf",                "collection_type": "edge",                "edge_properties": [                    {                        "name": "_key",                        "type": "str"                    },                    {                        "name": "_id",                        "type": "str"                    },                    {                        "name": "_from",                        "type": "str"                    },                    {                        "name": "_to",                        "type": "str"                    },                    {                        "name": "_rev",                        "type": "str"                    }                ],                "example_edge": {                    "_key": "266218884025",                    "_id": "ChildOf/266218884025",                    "_from": "Characters/AryaStark",                    "_to": "Characters/NedStark",                    "_rev": "_gVPKGSq---"                }            },            {                "collection_name": "Characters",                "collection_type": "document",                "document_properties": [                    {                        "name": "_key",                        "type": "str"                    },                    {                        "name": "_id",                        "type": "str"                    },                    {                        "name": "_rev",                        "type": "str"                    },                    {                        "name": "name",                        "type": "str"                    },                    {                        "name": "surname",                        "type": "str"                    },                    {                        "name": "alive",                        "type": "bool"                    },                    {                        "name": "age",                        "type": "int"                    },                    {                        "name": "gender",                        "type": "str"                    }                ],                "example_document": {                    "_key": "NedStark",                    "_id": "Characters/NedStark",                    "_rev": "_gVPKGPi---",                    "name": "Ned",                    "surname": "Stark",                    "alive": true,                    "age": 41,                    "gender": "male"                }            }        ]    }

Querying the ArangoDB Database[](#querying-the-arangodb-database "Direct link to Querying the ArangoDB Database")
------------------------------------------------------------------------------------------------------------------

We can now use the ArangoDB Graph QA Chain to inquire about our data

    import osos.environ["OPENAI_API_KEY"] = "your-key-here"

    from langchain.chat_models import ChatOpenAIfrom langchain.chains import ArangoGraphQAChainchain = ArangoGraphQAChain.from_llm(    ChatOpenAI(temperature=0), graph=graph, verbose=True)

    chain.run("Is Ned Stark alive?")

                > Entering new ArangoGraphQAChain chain...    AQL Query (1):    WITH Characters    FOR character IN Characters    FILTER character.name == "Ned" AND character.surname == "Stark"    RETURN character.alive        AQL Result:    [True]        > Finished chain.    'Yes, Ned Stark is alive.'

    chain.run("How old is Arya Stark?")

                > Entering new ArangoGraphQAChain chain...    AQL Query (1):    WITH Characters    FOR character IN Characters    FILTER character.name == "Arya" && character.surname == "Stark"    RETURN character.age        AQL Result:    [11]        > Finished chain.    'Arya Stark is 11 years old.'

    chain.run("Are Arya Stark and Ned Stark related?")

                > Entering new ArangoGraphQAChain chain...    AQL Query (1):    WITH Characters, ChildOf    FOR v, e, p IN 1..1 OUTBOUND 'Characters/AryaStark' ChildOf        FILTER p.vertices[-1]._key == 'NedStark'        RETURN p        AQL Result:    [{'vertices': [{'_key': 'AryaStark', '_id': 'Characters/AryaStark', '_rev': '_gVPKGPi--B', 'name': 'Arya', 'surname': 'Stark', 'alive': True, 'age': 11, 'gender': 'female'}, {'_key': 'NedStark', '_id': 'Characters/NedStark', '_rev': '_gVPKGPi---', 'name': 'Ned', 'surname': 'Stark', 'alive': True, 'age': 41, 'gender': 'male'}], 'edges': [{'_key': '266218884025', '_id': 'ChildOf/266218884025', '_from': 'Characters/AryaStark', '_to': 'Characters/NedStark', '_rev': '_gVPKGSq---'}], 'weights': [0, 1]}]        > Finished chain.    'Yes, Arya Stark and Ned Stark are related. According to the information retrieved from the database, there is a relationship between them. Arya Stark is the child of Ned Stark.'

    chain.run("Does Arya Stark have a dead parent?")

                > Entering new ArangoGraphQAChain chain...    AQL Query (1):    WITH Characters, ChildOf    FOR v, e IN 1..1 OUTBOUND 'Characters/AryaStark' ChildOf    FILTER v.alive == false    RETURN e        AQL Result:    [{'_key': '266218884027', '_id': 'ChildOf/266218884027', '_from': 'Characters/AryaStark', '_to': 'Characters/CatelynStark', '_rev': '_gVPKGSu---'}]        > Finished chain.    'Yes, Arya Stark has a dead parent. The parent is Catelyn Stark.'

Chain Modifiers[](#chain-modifiers "Direct link to Chain Modifiers")
---------------------------------------------------------------------

You can alter the values of the following `ArangoDBGraphQAChain` class variables to modify the behaviour of your chain results

    # Specify the maximum number of AQL Query Results to returnchain.top_k = 10# Specify whether or not to return the AQL Query in the output dictionarychain.return_aql_query = True# Specify whether or not to return the AQL JSON Result in the output dictionarychain.return_aql_result = True# Specify the maximum amount of AQL Generation attempts that should be madechain.max_aql_generation_attempts = 5# Specify a set of AQL Query Examples, which are passed to# the AQL Generation Prompt Template to promote few-shot-learning.# Defaults to an empty string.chain.aql_examples = """# Is Ned Stark alive?RETURN DOCUMENT('Characters/NedStark').alive# Is Arya Stark the child of Ned Stark?FOR e IN ChildOf    FILTER e._from == "Characters/AryaStark" AND e._to == "Characters/NedStark"    RETURN e"""

    chain.run("Is Ned Stark alive?")# chain("Is Ned Stark alive?") # Returns a dictionary with the AQL Query & AQL Result

                > Entering new ArangoGraphQAChain chain...    AQL Query (1):    RETURN DOCUMENT('Characters/NedStark').alive        AQL Result:    [True]        > Finished chain.    'Yes, according to the information in the database, Ned Stark is alive.'

    chain.run("Is Bran Stark the child of Ned Stark?")

                > Entering new ArangoGraphQAChain chain...    AQL Query (1):    FOR e IN ChildOf        FILTER e._from == "Characters/BranStark" AND e._to == "Characters/NedStark"        RETURN e        AQL Result:    [{'_key': '266218884026', '_id': 'ChildOf/266218884026', '_from': 'Characters/BranStark', '_to': 'Characters/NedStark', '_rev': '_gVPKGSq--_'}]        > Finished chain.    'Yes, according to the information in the ArangoDB database, Bran Stark is indeed the child of Ned Stark.'