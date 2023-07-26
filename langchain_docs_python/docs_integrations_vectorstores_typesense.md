Typesense
=========

> [Typesense](https://typesense.org) is an open source, in-memory search engine, that you can either [self-host](https://typesense.org/docs/guide/install-typesense.html#option-2-local-machine-self-hosting) or run on [Typesense Cloud](https://cloud.typesense.org/).
> 
> Typesense focuses on performance by storing the entire index in RAM (with a backup on disk) and also focuses on providing an out-of-the-box developer experience by simplifying available options and setting good defaults.
> 
> It also lets you combine attribute-based filtering together with vector queries, to fetch the most relevant documents.

This notebook shows you how to use Typesense as your VectorStore.

Let's first install our dependencies:

    pip install typesense openapi-schema-pydantic openai tiktoken

We want to use `OpenAIEmbeddings` so we have to get the OpenAI API Key.

    import osimport getpassos.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")

    from langchain.embeddings.openai import OpenAIEmbeddingsfrom langchain.text_splitter import CharacterTextSplitterfrom langchain.vectorstores import Typesensefrom langchain.document_loaders import TextLoader

Let's import our test dataset:

    loader = TextLoader("../../../state_of_the_union.txt")documents = loader.load()text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)docs = text_splitter.split_documents(documents)embeddings = OpenAIEmbeddings()

    docsearch = Typesense.from_documents(    docs,    embeddings,    typesense_client_params={        "host": "localhost",  # Use xxx.a1.typesense.net for Typesense Cloud        "port": "8108",  # Use 443 for Typesense Cloud        "protocol": "http",  # Use https for Typesense Cloud        "typesense_api_key": "xyz",        "typesense_collection_name": "lang-chain",    },)

Similarity Search[](#similarity-search "Direct link to Similarity Search")
---------------------------------------------------------------------------

    query = "What did the president say about Ketanji Brown Jackson"found_docs = docsearch.similarity_search(query)

    print(found_docs[0].page_content)

Typesense as a Retriever[](#typesense-as-a-retriever "Direct link to Typesense as a Retriever")
------------------------------------------------------------------------------------------------

Typesense, as all the other vector stores, is a LangChain Retriever, by using cosine similarity.

    retriever = docsearch.as_retriever()retriever

    query = "What did the president say about Ketanji Brown Jackson"retriever.get_relevant_documents(query)[0]