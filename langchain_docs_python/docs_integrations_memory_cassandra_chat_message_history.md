Cassandra Chat Message History
==============================

> [Apache Cassandra®](https://cassandra.apache.org) is a NoSQL, row-oriented, highly scalable and highly available database, well suited for storing large amounts of data.

Cassandra is a good choice for storing chat message history because it is easy to scale and can handle a large number of writes.

This notebook goes over how to use Cassandra to store chat message history.

To run this notebook you need either a running Cassandra cluster or a DataStax Astra DB instance running in the cloud (you can get one for free at [datastax.com](https://astra.datastax.com)). Check [cassio.org](https://cassio.org/start_here/) for more information.

    pip install "cassio>=0.0.7"

### Please provide database connection parameters and secrets:[](#please-provide-database-connection-parameters-and-secrets "Direct link to Please provide database connection parameters and secrets:")

    import osimport getpassdatabase_mode = (input("\n(C)assandra or (A)stra DB? ")).upper()keyspace_name = input("\nKeyspace name? ")if database_mode == "A":    ASTRA_DB_APPLICATION_TOKEN = getpass.getpass('\nAstra DB Token ("AstraCS:...") ')    #    ASTRA_DB_SECURE_BUNDLE_PATH = input("Full path to your Secure Connect Bundle? ")elif database_mode == "C":    CASSANDRA_CONTACT_POINTS = input(        "Contact points? (comma-separated, empty for localhost) "    ).strip()

#### depending on whether local or cloud-based Astra DB, create the corresponding database connection "Session" object[](#depending-on-whether-local-or-cloud-based-astra-db-create-the-corresponding-database-connection-session-object "Direct link to depending on whether local or cloud-based Astra DB, create the corresponding database connection "Session" object")

    from cassandra.cluster import Clusterfrom cassandra.auth import PlainTextAuthProviderif database_mode == "C":    if CASSANDRA_CONTACT_POINTS:        cluster = Cluster(            [cp.strip() for cp in CASSANDRA_CONTACT_POINTS.split(",") if cp.strip()]        )    else:        cluster = Cluster()    session = cluster.connect()elif database_mode == "A":    ASTRA_DB_CLIENT_ID = "token"    cluster = Cluster(        cloud={            "secure_connect_bundle": ASTRA_DB_SECURE_BUNDLE_PATH,        },        auth_provider=PlainTextAuthProvider(            ASTRA_DB_CLIENT_ID,            ASTRA_DB_APPLICATION_TOKEN,        ),    )    session = cluster.connect()else:    raise NotImplementedError

### Creation and usage of the Chat Message History[](#creation-and-usage-of-the-chat-message-history "Direct link to Creation and usage of the Chat Message History")

    from langchain.memory import CassandraChatMessageHistorymessage_history = CassandraChatMessageHistory(    session_id="test-session",    session=session,    keyspace=keyspace_name,)message_history.add_user_message("hi!")message_history.add_ai_message("whats up?")

    message_history.messages