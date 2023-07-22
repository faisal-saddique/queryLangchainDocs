Alibaba Cloud OpenSearch
========================

> [Alibaba Cloud Opensearch](https://www.alibabacloud.com/product/opensearch) is a one-stop platform to develop intelligent search services. `OpenSearch` was built on the large-scale distributed search engine developed by `Alibaba`. `OpenSearch` serves more than 500 business cases in Alibaba Group and thousands of Alibaba Cloud customers. `OpenSearch` helps develop search services in different search scenarios, including e-commerce, O2O, multimedia, the content industry, communities and forums, and big data query in enterprises.

> `OpenSearch` helps you develop high quality, maintenance-free, and high performance intelligent search services to provide your users with high search efficiency and accuracy.

> `OpenSearch` provides the vector search feature. In specific scenarios, especially test question search and image search scenarios, you can use the vector search feature together with the multimodal search feature to improve the accuracy of search results.

This notebook shows how to use functionality related to the `Alibaba Cloud OpenSearch Vector Search Edition`. To run, you should have an [OpenSearch Vector Search Edition](https://opensearch.console.aliyun.com) instance up and running:

Read the [help document](https://www.alibabacloud.com/help/en/opensearch/latest/vector-search) to quickly familiarize and configure OpenSearch Vector Search Edition instance.

After the instance is up and running, follow these steps to split documents, get embeddings, connect to the alibaba cloud opensearch instance, index documents, and perform vector retrieval.

We need to install the following Python packages first.

    #!pip install alibabacloud-ha3engine

We want to use `OpenAIEmbeddings` so we have to get the OpenAI API Key.

    import osimport getpassos.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")

    from langchain.embeddings.openai import OpenAIEmbeddingsfrom langchain.text_splitter import CharacterTextSplitterfrom langchain.vectorstores import (    AlibabaCloudOpenSearch,    AlibabaCloudOpenSearchSettings,)

Split documents and get embeddings.

    from langchain.document_loaders import TextLoaderloader = TextLoader("../../../state_of_the_union.txt")documents = loader.load()text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)docs = text_splitter.split_documents(documents)embeddings = OpenAIEmbeddings()

Create opensearch settings.

    settings = AlibabaCloudOpenSearchSettings(    endpoint="The endpoint of opensearch instance, You can find it from the console of Alibaba Cloud OpenSearch.",    instance_id="The identify of opensearch instance, You can find it from the console of Alibaba Cloud OpenSearch.",    datasource_name="The name of the data source specified when creating it.",    username="The username specified when purchasing the instance.",    password="The password specified when purchasing the instance.",    embedding_index_name="The name of the vector attribute specified when configuring the instance attributes.",    field_name_mapping={        "id": "id",  # The id field name mapping of index document.        "document": "document",  # The text field name mapping of index document.        "embedding": "embedding",  # The embedding field name mapping of index document.        "name_of_the_metadata_specified_during_search": "opensearch_metadata_field_name,=",  # The metadata field name mapping of index document, could specify multiple, The value field contains mapping name and operator, the operator would be used when executing metadata filter query.    },)# for example# settings = AlibabaCloudOpenSearchSettings(#     endpoint="ha-cn-5yd39d83c03.public.ha.aliyuncs.com",#     instance_id="ha-cn-5yd39d83c03",#     datasource_name="ha-cn-5yd39d83c03_test",#     username="this is a user name",#     password="this is a password",#     embedding_index_name="index_embedding",#     field_name_mapping={#         "id": "id",#         "document": "document",#         "embedding": "embedding",#         "metadata_a": "metadata_a,=" #The value field contains mapping name and operator, the operator would be used when executing metadata filter query#         "metadata_b": "metadata_b,>"#         "metadata_c": "metadata_c,<"#         "metadata_else": "metadata_else,="#     })

Create an opensearch access instance by settings.

    # Create an opensearch instance and index docs.opensearch = AlibabaCloudOpenSearch.from_texts(    texts=docs, embedding=embeddings, config=settings)

or

    # Create an opensearch instance.opensearch = AlibabaCloudOpenSearch(embedding=embeddings, config=settings)

Add texts and build index.

    metadatas = {"md_key_a": "md_val_a", "md_key_b": "md_val_b"}# the key of metadatas must match field_name_mapping in settings.opensearch.add_texts(texts=docs, ids=[], metadatas=metadatas)

Query and retrieve data.

    query = "What did the president say about Ketanji Brown Jackson"docs = opensearch.similarity_search(query)print(docs[0].page_content)

Query and retrieve data with metadata.

    query = "What did the president say about Ketanji Brown Jackson"metadatas = {"md_key_a": "md_val_a"}docs = opensearch.similarity_search(query, filter=metadatas)print(docs[0].page_content)

If you encounter any problems during use, please feel free to contact [xingshaomin.xsm@alibaba-inc.com](mailto:xingshaomin.xsm@alibaba-inc.com), and we will do our best to provide you with assistance and support.