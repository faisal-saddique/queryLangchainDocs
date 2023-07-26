Pinecone
========

> [Pinecone](https://docs.pinecone.io/docs/overview) is a vector database with broad functionality.

This notebook shows how to use functionality related to the `Pinecone` vector database.

To use Pinecone, you must have an API key. Here are the [installation instructions](https://docs.pinecone.io/docs/quickstart).

    pip install pinecone-client openai tiktoken

    import osimport getpassPINECONE_API_KEY = getpass.getpass("Pinecone API Key:")

    PINECONE_ENV = getpass.getpass("Pinecone Environment:")

We want to use `OpenAIEmbeddings` so we have to get the OpenAI API Key.

    os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")

    from langchain.embeddings.openai import OpenAIEmbeddingsfrom langchain.text_splitter import CharacterTextSplitterfrom langchain.vectorstores import Pineconefrom langchain.document_loaders import TextLoader

    from langchain.document_loaders import TextLoaderloader = TextLoader("../../../state_of_the_union.txt")documents = loader.load()text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)docs = text_splitter.split_documents(documents)embeddings = OpenAIEmbeddings()

    import pinecone# initialize pineconepinecone.init(    api_key=PINECONE_API_KEY,  # find at app.pinecone.io    environment=PINECONE_ENV,  # next to api key in console)index_name = "langchain-demo"docsearch = Pinecone.from_documents(docs, embeddings, index_name=index_name)# if you already have an index, you can load it like this# docsearch = Pinecone.from_existing_index(index_name, embeddings)query = "What did the president say about Ketanji Brown Jackson"docs = docsearch.similarity_search(query)

    print(docs[0].page_content)

### Adding More Text to an Existing Index[](#adding-more-text-to-an-existing-index "Direct link to Adding More Text to an Existing Index")

More text can embedded and upserted to an existing Pinecone index using the `add_texts` function

    index = pinecone.Index("langchain-demo")vectorstore = Pinecone(index, embeddings.embed_query, "text")vectorstore.add_texts("More text!")

### Maximal Marginal Relevance Searches[](#maximal-marginal-relevance-searches "Direct link to Maximal Marginal Relevance Searches")

In addition to using similarity search in the retriever object, you can also use `mmr` as retriever.

    retriever = docsearch.as_retriever(search_type="mmr")matched_docs = retriever.get_relevant_documents(query)for i, d in enumerate(matched_docs):    print(f"\n## Document {i}\n")    print(d.page_content)

Or use `max_marginal_relevance_search` directly:

    found_docs = docsearch.max_marginal_relevance_search(query, k=2, fetch_k=10)for i, doc in enumerate(found_docs):    print(f"{i + 1}.", doc.page_content, "\n")