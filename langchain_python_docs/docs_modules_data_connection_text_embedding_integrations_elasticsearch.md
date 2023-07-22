Elasticsearch
=============

Walkthrough of how to generate embeddings using a hosted embedding model in Elasticsearch

The easiest way to instantiate the `ElasticsearchEmbeddings` class it either

*   using the `from_credentials` constructor if you are using Elastic Cloud
*   or using the `from_es_connection` constructor with any Elasticsearch cluster

    pip -q install elasticsearch langchain

    import elasticsearchfrom langchain.embeddings.elasticsearch import ElasticsearchEmbeddings

    # Define the model IDmodel_id = "your_model_id"

Testing with `from_credentials`[​](#testing-with-from_credentials "Direct link to testing-with-from_credentials")
-----------------------------------------------------------------------------------------------------------------

This required an Elastic Cloud `cloud_id`

    # Instantiate ElasticsearchEmbeddings using credentialsembeddings = ElasticsearchEmbeddings.from_credentials(    model_id,    es_cloud_id="your_cloud_id",    es_user="your_user",    es_password="your_password",)

    # Create embeddings for multiple documentsdocuments = [    "This is an example document.",    "Another example document to generate embeddings for.",]document_embeddings = embeddings.embed_documents(documents)

    # Print document embeddingsfor i, embedding in enumerate(document_embeddings):    print(f"Embedding for document {i+1}: {embedding}")

    # Create an embedding for a single queryquery = "This is a single query."query_embedding = embeddings.embed_query(query)

    # Print query embeddingprint(f"Embedding for query: {query_embedding}")

Testing with Existing Elasticsearch client connection[​](#testing-with-existing-elasticsearch-client-connection "Direct link to Testing with Existing Elasticsearch client connection")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This can be used with any Elasticsearch deployment

    # Create Elasticsearch connectiones_connection = Elasticsearch(    hosts=["https://es_cluster_url:port"], basic_auth=("user", "password"))

    # Instantiate ElasticsearchEmbeddings using es_connectionembeddings = ElasticsearchEmbeddings.from_es_connection(    model_id,    es_connection,)

    # Create embeddings for multiple documentsdocuments = [    "This is an example document.",    "Another example document to generate embeddings for.",]document_embeddings = embeddings.embed_documents(documents)

    # Print document embeddingsfor i, embedding in enumerate(document_embeddings):    print(f"Embedding for document {i+1}: {embedding}")

    # Create an embedding for a single queryquery = "This is a single query."query_embedding = embeddings.embed_query(query)

    # Print query embeddingprint(f"Embedding for query: {query_embedding}")