Ensemble Retriever
==================

The `EnsembleRetriever` takes a list of retrievers as input and ensemble the results of their get\_relevant\_documents() methods and rerank the results based on the [Reciprocal Rank Fusion](https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf) algorithm.

By leveraging the strengths of different algorithms, the `EnsembleRetriever` can achieve better performance than any single algorithm.

The most common pattern is to combine a sparse retriever(like BM25) with a dense retriever(like Embedding similarity), because their strengths are complementary. It is also known as "hybrid search".The sparse retriever is good at finding relevant documents based on keywords, while the dense retriever is good at finding relevant documents based on semantic similarity.

    from langchain.retrievers import BM25Retriever, EnsembleRetrieverfrom langchain.vectorstores import FAISS

    doc_list = [    "I like apples",    "I like oranges",    "Apples and oranges are fruits",]# initialize the bm25 retriever and faiss retrieverbm25_retriever = BM25Retriever.from_texts(doc_list)bm25_retriever.k = 2embedding = OpenAIEmbeddings()faiss_vectorstore = FAISS.from_texts(doc_list, embedding)faiss_retriever = faiss_vectorstore.as_retriever(search_kwargs={"k": 2})# initialize the ensemble retrieverensemble_retriever = EnsembleRetriever(retrievers=[bm25_retriever, faiss_retriever], weights=[0.5, 0.5])

    docs = ensemble_retriever.get_relevant_documents("apples")docs

        [Document(page_content='I like apples', metadata={}),     Document(page_content='Apples and oranges are fruits', metadata={})]