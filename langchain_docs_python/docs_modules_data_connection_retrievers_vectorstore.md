Vector store-backed retriever
=============================

A vector store retriever is a retriever that uses a vector store to retrieve documents. It is a lightweight wrapper around the Vector Store class to make it conform to the Retriever interface. It uses the search methods implemented by a vector store, like similarity search and MMR, to query the texts in the vector store.

Once you construct a Vector store, it's very easy to construct a retriever. Let's walk through an example.

    from langchain.document_loaders import TextLoaderloader = TextLoader('../../../state_of_the_union.txt')

    from langchain.text_splitter import CharacterTextSplitterfrom langchain.vectorstores import FAISSfrom langchain.embeddings import OpenAIEmbeddingsdocuments = loader.load()text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)texts = text_splitter.split_documents(documents)embeddings = OpenAIEmbeddings()db = FAISS.from_documents(texts, embeddings)

        Exiting: Cleaning up .chroma directory

    retriever = db.as_retriever()

    docs = retriever.get_relevant_documents("what did he say about ketanji brown jackson")

Maximum Marginal Relevance Retrieval[](#maximum-marginal-relevance-retrieval "Direct link to Maximum Marginal Relevance Retrieval")
------------------------------------------------------------------------------------------------------------------------------------

By default, the vectorstore retriever uses similarity search. If the underlying vectorstore support maximum marginal relevance search, you can specify that as the search type.

    retriever = db.as_retriever(search_type="mmr")

    docs = retriever.get_relevant_documents("what did he say about ketanji brown jackson")

Similarity Score Threshold Retrieval[](#similarity-score-threshold-retrieval "Direct link to Similarity Score Threshold Retrieval")
------------------------------------------------------------------------------------------------------------------------------------

You can also a retrieval method that sets a similarity score threshold and only returns documents with a score above that threshold

    retriever = db.as_retriever(search_type="similarity_score_threshold", search_kwargs={"score_threshold": .5})

    docs = retriever.get_relevant_documents("what did he say about ketanji brown jackson")

Specifying top k[](#specifying-top-k "Direct link to Specifying top k")
------------------------------------------------------------------------

You can also specify search kwargs like `k` to use when doing retrieval.

    retriever = db.as_retriever(search_kwargs={"k": 1})

    docs = retriever.get_relevant_documents("what did he say about ketanji brown jackson")

    len(docs)

        1