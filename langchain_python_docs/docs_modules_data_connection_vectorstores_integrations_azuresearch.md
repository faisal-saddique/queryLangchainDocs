Azure Cognitive Search
======================

> [Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search) (formerly known as `Azure Search`) is a cloud search service that gives developers infrastructure, APIs, and tools for building a rich search experience over private, heterogeneous content in web, mobile, and enterprise applications.

Install Azure Cognitive Search SDK[​](#install-azure-cognitive-search-sdk "Direct link to Install Azure Cognitive Search SDK")
------------------------------------------------------------------------------------------------------------------------------

    pip install --index-url=https://pkgs.dev.azure.com/azure-sdk/public/_packaging/azure-sdk-for-python/pypi/simple/ azure-search-documents==11.4.0a20230509004pip install azure-identity

Import required libraries[​](#import-required-libraries "Direct link to Import required libraries")
---------------------------------------------------------------------------------------------------

    import os, jsonimport openaifrom dotenv import load_dotenvfrom langchain.embeddings.openai import OpenAIEmbeddingsfrom langchain.vectorstores.azuresearch import AzureSearch

Configure OpenAI settings[​](#configure-openai-settings "Direct link to Configure OpenAI settings")
---------------------------------------------------------------------------------------------------

Configure the OpenAI settings to use Azure OpenAI or OpenAI

    # Load environment variables from a .env file using load_dotenv():load_dotenv()openai.api_type = "azure"openai.api_base = "YOUR_OPENAI_ENDPOINT"openai.api_version = "2023-05-15"openai.api_key = "YOUR_OPENAI_API_KEY"model: str = "text-embedding-ada-002"

Configure vector store settings[​](#configure-vector-store-settings "Direct link to Configure vector store settings")
---------------------------------------------------------------------------------------------------------------------

Set up the vector store settings using environment variables:

    vector_store_address: str = "YOUR_AZURE_SEARCH_ENDPOINT"vector_store_password: str = "YOUR_AZURE_SEARCH_ADMIN_KEY"index_name: str = "langchain-vector-demo"

Create embeddings and vector store instances[​](#create-embeddings-and-vector-store-instances "Direct link to Create embeddings and vector store instances")
------------------------------------------------------------------------------------------------------------------------------------------------------------

Create instances of the OpenAIEmbeddings and AzureSearch classes:

    embeddings: OpenAIEmbeddings = OpenAIEmbeddings(model=model, chunk_size=1)vector_store: AzureSearch = AzureSearch(    azure_search_endpoint=vector_store_address,    azure_search_key=vector_store_password,    index_name=index_name,    embedding_function=embeddings.embed_query,)

Insert text and embeddings into vector store[​](#insert-text-and-embeddings-into-vector-store "Direct link to Insert text and embeddings into vector store")
------------------------------------------------------------------------------------------------------------------------------------------------------------

Add texts and metadata from the JSON data to the vector store:

    from langchain.document_loaders import TextLoaderfrom langchain.text_splitter import CharacterTextSplitterloader = TextLoader("../../../state_of_the_union.txt", encoding="utf-8")documents = loader.load()text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)docs = text_splitter.split_documents(documents)vector_store.add_documents(documents=docs)

Perform a vector similarity search[​](#perform-a-vector-similarity-search "Direct link to Perform a vector similarity search")
------------------------------------------------------------------------------------------------------------------------------

Execute a pure vector similarity search using the similarity\_search() method:

    # Perform a similarity searchdocs = vector_store.similarity_search(    query="What did the president say about Ketanji Brown Jackson",    k=3,    search_type="similarity",)print(docs[0].page_content)

        Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections.         Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service.         One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court.         And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.

Perform a Hybrid Search[​](#perform-a-hybrid-search "Direct link to Perform a Hybrid Search")
---------------------------------------------------------------------------------------------

Execute hybrid search using the hybrid\_search() method:

    # Perform a hybrid searchdocs = vector_store.similarity_search(    query="What did the president say about Ketanji Brown Jackson", k=3)print(docs[0].page_content)

        Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections.         Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service.         One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court.         And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.