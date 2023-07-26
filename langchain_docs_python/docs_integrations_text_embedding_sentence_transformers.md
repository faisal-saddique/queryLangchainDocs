Sentence Transformers Embeddings
================================

[SentenceTransformers](https://www.sbert.net/) embeddings are called using the `HuggingFaceEmbeddings` integration. We have also added an alias for `SentenceTransformerEmbeddings` for users who are more familiar with directly using that package.

SentenceTransformers is a python package that can generate text and image embeddings, originating from [Sentence-BERT](https://arxiv.org/abs/1908.10084)

    pip install sentence_transformers > /dev/null

            [notice] A new release of pip is available: 23.0.1 -> 23.1.1    [notice] To update, run: pip install --upgrade pip

    from langchain.embeddings import HuggingFaceEmbeddings, SentenceTransformerEmbeddings

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")# Equivalent to SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    text = "This is a test document."

    query_result = embeddings.embed_query(text)

    doc_result = embeddings.embed_documents([text, "This is not a test document."])