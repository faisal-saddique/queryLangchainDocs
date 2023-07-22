Fake Embeddings
===============

LangChain also provides a fake embedding class. You can use this to test your pipelines.

    from langchain.embeddings import FakeEmbeddings

    embeddings = FakeEmbeddings(size=1352)

    query_result = embeddings.embed_query("foo")

    doc_results = embeddings.embed_documents(["foo"])