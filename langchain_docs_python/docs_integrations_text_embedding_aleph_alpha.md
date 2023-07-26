Aleph Alpha
===========

There are two possible ways to use Aleph Alpha's semantic embeddings. If you have texts with a dissimilar structure (e.g. a Document and a Query) you would want to use asymmetric embeddings. Conversely, for texts with comparable structures, symmetric embeddings are the suggested approach.

Asymmetric[](#asymmetric "Direct link to Asymmetric")
------------------------------------------------------

    from langchain.embeddings import AlephAlphaAsymmetricSemanticEmbedding

    document = "This is a content of the document"query = "What is the contnt of the document?"

    embeddings = AlephAlphaAsymmetricSemanticEmbedding()

    doc_result = embeddings.embed_documents([document])

    query_result = embeddings.embed_query(query)

Symmetric[](#symmetric "Direct link to Symmetric")
---------------------------------------------------

    from langchain.embeddings import AlephAlphaSymmetricSemanticEmbedding

    text = "This is a test text"

    embeddings = AlephAlphaSymmetricSemanticEmbedding()

    doc_result = embeddings.embed_documents([text])

    query_result = embeddings.embed_query(text)