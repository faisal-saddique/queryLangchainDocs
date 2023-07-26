OpenAI
======

Let's load the OpenAI Embedding class.

    from langchain.embeddings import OpenAIEmbeddings

    embeddings = OpenAIEmbeddings()

    text = "This is a test document."

    query_result = embeddings.embed_query(text)

    doc_result = embeddings.embed_documents([text])

Let's load the OpenAI Embedding class with first generation models (e.g. text-search-ada-doc-001/text-search-ada-query-001). Note: These are not recommended models - see [here](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings)

    from langchain.embeddings.openai import OpenAIEmbeddings

    embeddings = OpenAIEmbeddings()

    text = "This is a test document."

    query_result = embeddings.embed_query(text)

    doc_result = embeddings.embed_documents([text])

    # if you are behind an explicit proxy, you can use the OPENAI_PROXY environment variable to pass throughos.environ["OPENAI_PROXY"] = "http://proxy.yourcompany.com:8080"