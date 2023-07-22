Spacy Embedding
===============

### Loading the Spacy embedding class to generate and query embeddings[​](#loading-the-spacy-embedding-class-to-generate-and-query-embeddings "Direct link to Loading the Spacy embedding class to generate and query embeddings")

#### Import the necessary classes[​](#import-the-necessary-classes "Direct link to Import the necessary classes")

    from langchain.embeddings.spacy_embeddings import SpacyEmbeddings

#### Initialize SpacyEmbeddings.This will load the Spacy model into memory.[​](#initialize-spacyembeddingsthis-will-load-the-spacy-model-into-memory "Direct link to Initialize SpacyEmbeddings.This will load the Spacy model into memory.")

    embedder = SpacyEmbeddings()

#### Define some example texts . These could be any documents that you want to analyze - for example, news articles, social media posts, or product reviews.[​](#define-some-example-texts--these-could-be-any-documents-that-you-want-to-analyze---for-example-news-articles-social-media-posts-or-product-reviews "Direct link to Define some example texts . These could be any documents that you want to analyze - for example, news articles, social media posts, or product reviews.")

    texts = [    "The quick brown fox jumps over the lazy dog.",    "Pack my box with five dozen liquor jugs.",    "How vexingly quick daft zebras jump!",    "Bright vixens jump; dozy fowl quack.",]

#### Generate and print embeddings for the texts . The SpacyEmbeddings class generates an embedding for each document, which is a numerical representation of the document's content. These embeddings can be used for various natural language processing tasks, such as document similarity comparison or text classification.[​](#generate-and-print-embeddings-for-the-texts--the-spacyembeddings-class-generates-an-embedding-for-each-document-which-is-a-numerical-representation-of-the-documents-content-these-embeddings-can-be-used-for-various-natural-language-processing-tasks-such-as-document-similarity-comparison-or-text-classification "Direct link to Generate and print embeddings for the texts . The SpacyEmbeddings class generates an embedding for each document, which is a numerical representation of the document's content. These embeddings can be used for various natural language processing tasks, such as document similarity comparison or text classification.")

    embeddings = embedder.embed_documents(texts)for i, embedding in enumerate(embeddings):    print(f"Embedding for document {i+1}: {embedding}")

#### Generate and print an embedding for a single piece of text. You can also generate an embedding for a single piece of text, such as a search query. This can be useful for tasks like information retrieval, where you want to find documents that are similar to a given query.[​](#generate-and-print-an-embedding-for-a-single-piece-of-text-you-can-also-generate-an-embedding-for-a-single-piece-of-text-such-as-a-search-query-this-can-be-useful-for-tasks-like-information-retrieval-where-you-want-to-find-documents-that-are-similar-to-a-given-query "Direct link to Generate and print an embedding for a single piece of text. You can also generate an embedding for a single piece of text, such as a search query. This can be useful for tasks like information retrieval, where you want to find documents that are similar to a given query.")

    query = "Quick foxes and lazy dogs."query_embedding = embedder.embed_query(query)print(f"Embedding for query: {query_embedding}")