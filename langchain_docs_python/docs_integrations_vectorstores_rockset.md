Rockset
=======

> [Rockset](https://rockset.com/product/) is a real-time analytics database service for serving low latency, high concurrency analytical queries at scale. It builds a Converged Index™ on structured and semi-structured data with an efficient store for vector embeddings. Its support for running SQL on schemaless data makes it a perfect choice for running vector search with metadata filters.

This notebook demonstrates how to use `Rockset` as a vectorstore in langchain. To get started, make sure you have a `Rockset` account and an API key available.

Setting up environment[](#setting-up-environment "Direct link to Setting up environment")
------------------------------------------------------------------------------------------

1.  Make sure you have Rockset account and go to the web console to get the API key. Details can be found on [the website](https://rockset.com/docs/rest-api/). For the purpose of this notebook, we will assume you're using Rockset from `Oregon(us-west-2)`.
    
2.  Now you will need to create a Rockset collection to write to, use the Rockset web console to do this. For the purpose of this exercise, we will create a collection called `langchain_demo`. Since Rockset supports schemaless ingest, you don't need to inform us of the shape of metadata for your texts. However, you do need to decide on two columns upfront:
    

*   Where to store the text. We will use the column `description` for this.
*   Where to store the vector-embedding for the text. We will use the column `description_embedding` for this.

Also you will need to inform Rockset that `description_embedding` is a vector-embedding, so that we can optimize its format. You can do this using a **Rockset ingest transformation** while creating your collection:

SELECT \_input.\* EXCEPT(\_meta), VECTOR\_ENFORCE(\_input.description\_embedding, #length\_of\_vector\_embedding, 'float') as description\_embedding FROM \_input

// We used OpenAI `text-embedding-ada-002` for this examples, where #length\_of\_vector\_embedding = 1536

3.  Now let's install the [rockset-python-client](https://github.com/rockset/rockset-python-client). This is used by langchain to talk to the Rockset database.

    pip install rockset

This is it! Now you're ready to start writing some python code to store vector embeddings in Rockset, and querying the database to find texts similar to your query! We support 3 distance functions: `COSINE_SIM`, `EUCLIDEAN_DIST` and `DOT_PRODUCT`.

Example[](#example "Direct link to Example")
---------------------------------------------

    import osimport rockset# Make sure env variable ROCKSET_API_KEY is setROCKSET_API_KEY = os.environ.get("ROCKSET_API_KEY")ROCKSET_API_SERVER = (    rockset.Regions.usw2a1)  # Make sure this points to the correct Rockset regionrockset_client = rockset.RocksetClient(ROCKSET_API_SERVER, ROCKSET_API_KEY)COLLECTION_NAME = "langchain_demo"TEXT_KEY = "description"EMBEDDING_KEY = "description_embedding"

Now let's use this client to create a Rockset Langchain Vectorstore!

### 1\. Inserting texts[](#1-inserting-texts "Direct link to 1. Inserting texts")

    from langchain.embeddings.openai import OpenAIEmbeddingsfrom langchain.text_splitter import CharacterTextSplitterfrom langchain.document_loaders import TextLoaderfrom langchain.vectorstores.rocksetdb import RocksetDBloader = TextLoader("../../../state_of_the_union.txt")documents = loader.load()text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)docs = text_splitter.split_documents(documents)

Now we have the documents we want to insert. Let's create a Rockset vectorstore and insert these docs into the Rockset collection. We will use `OpenAIEmbeddings` to create embeddings for the texts, but you're free to use whatever you want.

    # Make sure the environment variable OPENAI_API_KEY is set upembeddings = OpenAIEmbeddings()docsearch = RocksetDB(    client=rockset_client,    embeddings=embeddings,    collection_name=COLLECTION_NAME,    text_key=TEXT_KEY,    embedding_key=EMBEDDING_KEY,)ids = docsearch.add_texts(    texts=[d.page_content for d in docs],    metadatas=[d.metadata for d in docs],)## If you go to the Rockset console now, you should be able to see this docs along with the metadata `source`

### 2\. Searching similar texts[](#2-searching-similar-texts "Direct link to 2. Searching similar texts")

Now let's try to search Rockset to find strings similar to our query string!

    query = "What did the president say about Ketanji Brown Jackson"output = docsearch.similarity_search_with_relevance_scores(    query, 4, RocksetDB.DistanceFunction.COSINE_SIM)print("output length:", len(output))for d, dist in output:    print(dist, d.metadata, d.page_content[:20] + "...")### output length: 4# 0.764990692109871 {'source': '../../../state_of_the_union.txt'} Madam Speaker, Madam...# 0.7485416901622112 {'source': '../../../state_of_the_union.txt'} And I’m taking robus...# 0.7468678973398306 {'source': '../../../state_of_the_union.txt'} And so many families...# 0.7436231261419488 {'source': '../../../state_of_the_union.txt'} Groups of citizens b...

You can also use a where filter to prune your search space. You can add filters on text key, or any of the metadata fields.

> **Note**: Since Rockset stores each metadata field as a separate column internally, these filters are much faster than other vector databases which store all metadata as a single JSON.

For eg, to find all texts NOT containing the substring "and", you can use the following code:

    output = docsearch.similarity_search_with_relevance_scores(    query,    4,    RocksetDB.DistanceFunction.COSINE_SIM,    where_str="{} NOT LIKE '%citizens%'".format(TEXT_KEY),)print("output length:", len(output))for d, dist in output:    print(dist, d.metadata, d.page_content[:20] + "...")### output length: 4# 0.7651359650263554 {'source': '../../../state_of_the_union.txt'} Madam Speaker, Madam...# 0.7486265516824893 {'source': '../../../state_of_the_union.txt'} And I’m taking robus...# 0.7469625542348115 {'source': '../../../state_of_the_union.txt'} And so many families...# 0.7344177777547739 {'source': '../../../state_of_the_union.txt'} We see the unity amo...

### 3\. \[Optional\] Drop all inserted documents[](#3-optional-drop-all-inserted-documents "Direct link to 3-optional-drop-all-inserted-documents")

In order to delete texts from the Rockset collection, you need to know the unique ID associated with each document inside Rockset. These ids can either be supplied directly by the user while inserting the texts (in the `RocksetDB.add_texts()` function), else Rockset will generate a unique ID or each document. Either way, `Rockset.add_texts()` returns the ids for the inserted documents.

To delete these docs, simply use the `RocksetDB.delete_texts()` function.

    docsearch.delete_texts(ids)

Congratulations![](#congratulations "Direct link to Congratulations!")
-----------------------------------------------------------------------

Voila! In this example you successfuly created a Rockset collection, inserted documents along with their OpenAI vector embeddings, and searched for similar docs both with and without any metadata filters.

Keep an eye on [https://rockset.com/blog/introducing-vector-search-on-rockset/](https://rockset.com/blog/introducing-vector-search-on-rockset/) for future updates in this space!