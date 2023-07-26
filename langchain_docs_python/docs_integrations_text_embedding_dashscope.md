DashScope
=========

Let's load the DashScope Embedding class.

    from langchain.embeddings import DashScopeEmbeddings

    embeddings = DashScopeEmbeddings(    model="text-embedding-v1", dashscope_api_key="your-dashscope-api-key")

    text = "This is a test document."

    query_result = embeddings.embed_query(text)print(query_result)

    doc_results = embeddings.embed_documents(["foo"])print(doc_results)