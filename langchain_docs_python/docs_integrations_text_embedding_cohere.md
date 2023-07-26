Cohere
======

Let's load the Cohere Embedding class.

    from langchain.embeddings import CohereEmbeddings

    embeddings = CohereEmbeddings(cohere_api_key=cohere_api_key)

    text = "This is a test document."

    query_result = embeddings.embed_query(text)

    doc_result = embeddings.embed_documents([text])