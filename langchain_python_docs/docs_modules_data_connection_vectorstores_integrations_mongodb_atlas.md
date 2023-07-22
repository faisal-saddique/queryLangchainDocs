MongoDB Atlas
=============

> [MongoDB Atlas](https://www.mongodb.com/docs/atlas/) is a fully-managed cloud database available in AWS , Azure, and GCP. It now has support for native Vector Search on your MongoDB document data.

This notebook shows how to use `MongoDB Atlas Vector Search` to store your embeddings in MongoDB documents, create a vector search index, and perform KNN search with an approximate nearest neighbor algorithm.

It uses the [knnBeta Operator](https://www.mongodb.com/docs/atlas/atlas-search/knn-beta) available in MongoDB Atlas Search. This feature is in Public Preview and available for evaluation purposes, to validate functionality, and to gather feedback from public preview users. It is not recommended for production deployments as we may introduce breaking changes.

To use MongoDB Atlas, you must first deploy a cluster. We have a Forever-Free tier of clusters available. To get started head over to Atlas here: [quick start](https://www.mongodb.com/docs/atlas/getting-started/).

    pip install pymongo

    import osimport getpassMONGODB_ATLAS_CLUSTER_URI = getpass.getpass("MongoDB Atlas Cluster URI:")

We want to use `OpenAIEmbeddings` so we need to set up our OpenAI API Key.

    os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")

Now, let's create a vector search index on your cluster. In the below example, `embedding` is the name of the field that contains the embedding vector. Please refer to the [documentation](https://www.mongodb.com/docs/atlas/atlas-search/define-field-mappings-for-vector-search) to get more details on how to define an Atlas Vector Search index. You can name the index `langchain_demo` and create the index on the namespace `lanchain_db.langchain_col`. Finally, write the following definition in the JSON editor on MongoDB Atlas:

    {  "mappings": {    "dynamic": true,    "fields": {      "embedding": {        "dimensions": 1536,        "similarity": "cosine",        "type": "knnVector"      }    }  }}

    from langchain.embeddings.openai import OpenAIEmbeddingsfrom langchain.text_splitter import CharacterTextSplitterfrom langchain.vectorstores import MongoDBAtlasVectorSearchfrom langchain.document_loaders import TextLoaderloader = TextLoader("../../../state_of_the_union.txt")documents = loader.load()text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)docs = text_splitter.split_documents(documents)embeddings = OpenAIEmbeddings()

    from pymongo import MongoClient# initialize MongoDB python clientclient = MongoClient(MONGODB_ATLAS_CLUSTER_URI)db_name = "langchain_db"collection_name = "langchain_col"collection = client[db_name][collection_name]index_name = "langchain_demo"# insert the documents in MongoDB Atlas with their embeddingdocsearch = MongoDBAtlasVectorSearch.from_documents(    docs, embeddings, collection=collection, index_name=index_name)# perform a similarity search between the embedding of the query and the embeddings of the documentsquery = "What did the president say about Ketanji Brown Jackson"docs = docsearch.similarity_search(query)

    print(docs[0].page_content)

You can also instantiate the vector store directly and execute a query as follows:

    # initialize vector storevectorstore = MongoDBAtlasVectorSearch(    collection, OpenAIEmbeddings(), index_name=index_name)# perform a similarity search between a query and the ingested documentsquery = "What did the president say about Ketanji Brown Jackson"docs = vectorstore.similarity_search(query)print(docs[0].page_content)