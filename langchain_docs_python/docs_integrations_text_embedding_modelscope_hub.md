ModelScope
==========

Let's load the ModelScope Embedding class.

    from langchain.embeddings import ModelScopeEmbeddings

    model_id = "damo/nlp_corom_sentence-embedding_english-base"

    embeddings = ModelScopeEmbeddings(model_id=model_id)

    text = "This is a test document."

    query_result = embeddings.embed_query(text)

    doc_results = embeddings.embed_documents(["foo"])