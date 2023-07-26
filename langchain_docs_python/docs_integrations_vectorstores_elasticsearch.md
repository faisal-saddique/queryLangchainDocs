ElasticSearch
=============

> [Elasticsearch](https://www.elastic.co/elasticsearch/) is a distributed, RESTful search and analytics engine. It provides a distributed, multitenant-capable full-text search engine with an HTTP web interface and schema-free JSON documents.

This notebook shows how to use functionality related to the `Elasticsearch` database.

Installation[](#installation "Direct link to Installation")
------------------------------------------------------------

Check out [Elasticsearch installation instructions](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html).

To connect to an Elasticsearch instance that does not require login credentials, pass the Elasticsearch URL and index name along with the embedding object to the constructor.

Example:

            from langchain import ElasticVectorSearch        from langchain.embeddings import OpenAIEmbeddings        embedding = OpenAIEmbeddings()        elastic_vector_search = ElasticVectorSearch(            elasticsearch_url="http://localhost:9200",            index_name="test_index",            embedding=embedding        )

To connect to an Elasticsearch instance that requires login credentials, including Elastic Cloud, use the Elasticsearch URL format https://username:password@es\_host:9243. For example, to connect to Elastic Cloud, create the Elasticsearch URL with the required authentication details and pass it to the ElasticVectorSearch constructor as the named parameter elasticsearch\_url.

You can obtain your Elastic Cloud URL and login credentials by logging in to the Elastic Cloud console at [https://cloud.elastic.co](https://cloud.elastic.co), selecting your deployment, and navigating to the "Deployments" page.

To obtain your Elastic Cloud password for the default "elastic" user:

1.  Log in to the Elastic Cloud console at [https://cloud.elastic.co](https://cloud.elastic.co)
2.  Go to "Security" > "Users"
3.  Locate the "elastic" user and click "Edit"
4.  Click "Reset password"
5.  Follow the prompts to reset the password

Format for Elastic Cloud URLs is https://username:[password@cluster\_id.region\_id.gcp.cloud.es.io](mailto:password@cluster_id.region_id.gcp.cloud.es.io):9243.

Example:

            from langchain import ElasticVectorSearch        from langchain.embeddings import OpenAIEmbeddings        embedding = OpenAIEmbeddings()        elastic_host = "cluster_id.region_id.gcp.cloud.es.io"        elasticsearch_url = f"https://username:password@{elastic_host}:9243"        elastic_vector_search = ElasticVectorSearch(            elasticsearch_url=elasticsearch_url,            index_name="test_index",            embedding=embedding        )

    pip install elasticsearch

    import osimport getpassos.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")

        OpenAI API Key: ········

Example[](#example "Direct link to Example")
---------------------------------------------

    from langchain.embeddings.openai import OpenAIEmbeddingsfrom langchain.text_splitter import CharacterTextSplitterfrom langchain.vectorstores import ElasticVectorSearchfrom langchain.document_loaders import TextLoader

    from langchain.document_loaders import TextLoaderloader = TextLoader("../../../state_of_the_union.txt")documents = loader.load()text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)docs = text_splitter.split_documents(documents)embeddings = OpenAIEmbeddings()

    db = ElasticVectorSearch.from_documents(    docs, embeddings, elasticsearch_url="http://localhost:9200")query = "What did the president say about Ketanji Brown Jackson"docs = db.similarity_search(query)

    print(docs[0].page_content)

        In state after state, new laws have been passed, not only to suppress the vote, but to subvert entire elections.         We cannot let this happen.         Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections.         Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service.         One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court.         And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.

ElasticKnnSearch Class
======================

The `ElasticKnnSearch` implements features allowing storing vectors and documents in Elasticsearch for use with approximate [kNN search](https://www.elastic.co/guide/en/elasticsearch/reference/current/knn-search.html)

    pip install langchain elasticsearch

    from langchain.vectorstores.elastic_vector_search import ElasticKnnSearchfrom langchain.embeddings import ElasticsearchEmbeddingsimport elasticsearch

    # Initialize ElasticsearchEmbeddingsmodel_id = "<model_id_from_es>"dims = dim_countes_cloud_id = "ESS_CLOUD_ID"es_user = "es_user"es_password = "es_pass"test_index = "<index_name>"# input_field = "your_input_field" # if different from 'text_field'

    # Generate embedding objectembeddings = ElasticsearchEmbeddings.from_credentials(    model_id,    # input_field=input_field,    es_cloud_id=es_cloud_id,    es_user=es_user,    es_password=es_password,)

    # Initialize ElasticKnnSearchknn_search = ElasticKnnSearch(    es_cloud_id=es_cloud_id,    es_user=es_user,    es_password=es_password,    index_name=test_index,    embedding=embeddings,)

Test adding vectors[](#test-adding-vectors "Direct link to Test adding vectors")
---------------------------------------------------------------------------------

    # Test `add_texts` methodtexts = ["Hello, world!", "Machine learning is fun.", "I love Python."]knn_search.add_texts(texts)# Test `from_texts` methodnew_texts = [    "This is a new text.",    "Elasticsearch is powerful.",    "Python is great for data analysis.",]knn_search.from_texts(new_texts, dims=dims)

Test knn search using query vector builder[](#test-knn-search-using-query-vector-builder "Direct link to Test knn search using query vector builder")
------------------------------------------------------------------------------------------------------------------------------------------------------

    # Test `knn_search` method with model_id and query_textquery = "Hello"knn_result = knn_search.knn_search(query=query, model_id=model_id, k=2)print(f"kNN search results for query '{query}': {knn_result}")print(    f"The 'text' field value from the top hit is: '{knn_result['hits']['hits'][0]['_source']['text']}'")# Test `hybrid_search` methodquery = "Hello"hybrid_result = knn_search.knn_hybrid_search(query=query, model_id=model_id, k=2)print(f"Hybrid search results for query '{query}': {hybrid_result}")print(    f"The 'text' field value from the top hit is: '{hybrid_result['hits']['hits'][0]['_source']['text']}'")

Test knn search using pre generated vector[](#test-knn-search-using-pre-generated-vector "Direct link to Test knn search using pre generated vector")
------------------------------------------------------------------------------------------------------------------------------------------------------

    # Generate embedding for testsquery_text = "Hello"query_embedding = embeddings.embed_query(query_text)print(    f"Length of embedding: {len(query_embedding)}\nFirst two items in embedding: {query_embedding[:2]}")# Test knn Searchknn_result = knn_search.knn_search(query_vector=query_embedding, k=2)print(    f"The 'text' field value from the top hit is: '{knn_result['hits']['hits'][0]['_source']['text']}'")# Test hybrid search - Requires both query_text and query_vectorknn_result = knn_search.knn_hybrid_search(    query_vector=query_embedding, query=query_text, k=2)print(    f"The 'text' field value from the top hit is: '{knn_result['hits']['hits'][0]['_source']['text']}'")

Test source option[](#test-source-option "Direct link to Test source option")
------------------------------------------------------------------------------

    # Test `knn_search` method with model_id and query_textquery = "Hello"knn_result = knn_search.knn_search(query=query, model_id=model_id, k=2, source=False)assert not "_source" in knn_result["hits"]["hits"][0].keys()# Test `hybrid_search` methodquery = "Hello"hybrid_result = knn_search.knn_hybrid_search(    query=query, model_id=model_id, k=2, source=False)assert not "_source" in hybrid_result["hits"]["hits"][0].keys()

Test fields option[](#test-fields-option "Direct link to Test fields option")
------------------------------------------------------------------------------

    # Test `knn_search` method with model_id and query_textquery = "Hello"knn_result = knn_search.knn_search(query=query, model_id=model_id, k=2, fields=["text"])assert "text" in knn_result["hits"]["hits"][0]["fields"].keys()# Test `hybrid_search` methodquery = "Hello"hybrid_result = knn_search.knn_hybrid_search(    query=query, model_id=model_id, k=2, fields=["text"])assert "text" in hybrid_result["hits"]["hits"][0]["fields"].keys()

### Test with es client connection rather than cloud\_id[](#test-with-es-client-connection-rather-than-cloud_id "Direct link to Test with es client connection rather than cloud_id")

    # Create Elasticsearch connectiones_connection = Elasticsearch(    hosts=["https://es_cluster_url:port"], basic_auth=("user", "password"))

    # Instantiate ElasticsearchEmbeddings using es_connectionembeddings = ElasticsearchEmbeddings.from_es_connection(    model_id,    es_connection,)

    # Initialize ElasticKnnSearchknn_search = ElasticKnnSearch(    es_connection=es_connection, index_name=test_index, embedding=embeddings)

    # Test `knn_search` method with model_id and query_textquery = "Hello"knn_result = knn_search.knn_search(query=query, model_id=model_id, k=2)print(f"kNN search results for query '{query}': {knn_result}")print(    f"The 'text' field value from the top hit is: '{knn_result['hits']['hits'][0]['_source']['text']}'")