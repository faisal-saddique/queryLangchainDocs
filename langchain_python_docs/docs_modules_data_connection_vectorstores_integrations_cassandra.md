Cassandra
=========

> [Apache Cassandra®](https://cassandra.apache.org) is a NoSQL, row-oriented, highly scalable and highly available database.

Newest Cassandra releases natively [support](https://cwiki.apache.org/confluence/display/CASSANDRA/CEP-30%3A+Approximate+Nearest+Neighbor(ANN)+Vector+Search+via+Storage-Attached+Indexes) Vector Similarity Search.

To run this notebook you need either a running Cassandra cluster equipped with Vector Search capabilities (in pre-release at the time of writing) or a DataStax Astra DB instance running in the cloud (you can get one for free at [datastax.com](https://astra.datastax.com)). Check [cassio.org](https://cassio.org/start_here/) for more information.

    pip install "cassio>=0.0.7"

### Please provide database connection parameters and secrets:[​](#please-provide-database-connection-parameters-and-secrets "Direct link to Please provide database connection parameters and secrets:")

    import osimport getpassdatabase_mode = (input("\n(C)assandra or (A)stra DB? ")).upper()keyspace_name = input("\nKeyspace name? ")if database_mode == "A":    ASTRA_DB_APPLICATION_TOKEN = getpass.getpass('\nAstra DB Token ("AstraCS:...") ')    #    ASTRA_DB_SECURE_BUNDLE_PATH = input("Full path to your Secure Connect Bundle? ")elif database_mode == "C":    CASSANDRA_CONTACT_POINTS = input(        "Contact points? (comma-separated, empty for localhost) "    ).strip()

#### depending on whether local or cloud-based Astra DB, create the corresponding database connection "Session" object[​](#depending-on-whether-local-or-cloud-based-astra-db-create-the-corresponding-database-connection-session-object "Direct link to depending on whether local or cloud-based Astra DB, create the corresponding database connection "Session" object")

    from cassandra.cluster import Clusterfrom cassandra.auth import PlainTextAuthProviderif database_mode == "C":    if CASSANDRA_CONTACT_POINTS:        cluster = Cluster(            [cp.strip() for cp in CASSANDRA_CONTACT_POINTS.split(",") if cp.strip()]        )    else:        cluster = Cluster()    session = cluster.connect()elif database_mode == "A":    ASTRA_DB_CLIENT_ID = "token"    cluster = Cluster(        cloud={            "secure_connect_bundle": ASTRA_DB_SECURE_BUNDLE_PATH,        },        auth_provider=PlainTextAuthProvider(            ASTRA_DB_CLIENT_ID,            ASTRA_DB_APPLICATION_TOKEN,        ),    )    session = cluster.connect()else:    raise NotImplementedError

### Please provide OpenAI access key[​](#please-provide-openai-access-key "Direct link to Please provide OpenAI access key")

We want to use `OpenAIEmbeddings` so we have to get the OpenAI API Key.

    os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")

### Creation and usage of the Vector Store[​](#creation-and-usage-of-the-vector-store "Direct link to Creation and usage of the Vector Store")

    from langchain.embeddings.openai import OpenAIEmbeddingsfrom langchain.text_splitter import CharacterTextSplitterfrom langchain.vectorstores import Cassandrafrom langchain.document_loaders import TextLoader

    from langchain.document_loaders import TextLoaderloader = TextLoader("../../../state_of_the_union.txt")documents = loader.load()text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)docs = text_splitter.split_documents(documents)embedding_function = OpenAIEmbeddings()

    table_name = "my_vector_db_table"docsearch = Cassandra.from_documents(    documents=docs,    embedding=embedding_function,    session=session,    keyspace=keyspace_name,    table_name=table_name,)query = "What did the president say about Ketanji Brown Jackson"docs = docsearch.similarity_search(query)

    ## if you already have an index, you can load it and use it like this:# docsearch_preexisting = Cassandra(#     embedding=embedding_function,#     session=session,#     keyspace=keyspace_name,#     table_name=table_name,# )# docsearch_preexisting.similarity_search(query, k=2)

    print(docs[0].page_content)

### Maximal Marginal Relevance Searches[​](#maximal-marginal-relevance-searches "Direct link to Maximal Marginal Relevance Searches")

In addition to using similarity search in the retriever object, you can also use `mmr` as retriever.

    retriever = docsearch.as_retriever(search_type="mmr")matched_docs = retriever.get_relevant_documents(query)for i, d in enumerate(matched_docs):    print(f"\n## Document {i}\n")    print(d.page_content)

Or use `max_marginal_relevance_search` directly:

    found_docs = docsearch.max_marginal_relevance_search(query, k=2, fetch_k=10)for i, doc in enumerate(found_docs):    print(f"{i + 1}.", doc.page_content, "\n")