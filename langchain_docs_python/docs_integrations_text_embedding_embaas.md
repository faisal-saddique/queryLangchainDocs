Embaas
======

[embaas](https://embaas.io) is a fully managed NLP API service that offers features like embedding generation, document text extraction, document to embeddings and more. You can choose a [variety of pre-trained models](https://embaas.io/docs/models/embeddings).

In this tutorial, we will show you how to use the embaas Embeddings API to generate embeddings for a given text.

### Prerequisites[](#prerequisites "Direct link to Prerequisites")

Create your free embaas account at [https://embaas.io/register](https://embaas.io/register) and generate an [API key](https://embaas.io/dashboard/api-keys).

    # Set API keyembaas_api_key = "YOUR_API_KEY"# or set environment variableos.environ["EMBAAS_API_KEY"] = "YOUR_API_KEY"

    from langchain.embeddings import EmbaasEmbeddings

    embeddings = EmbaasEmbeddings()

    # Create embeddings for a single documentdoc_text = "This is a test document."doc_text_embedding = embeddings.embed_query(doc_text)

    # Print created embeddingprint(doc_text_embedding)

    # Create embeddings for multiple documentsdoc_texts = ["This is a test document.", "This is another test document."]doc_texts_embeddings = embeddings.embed_documents(doc_texts)

    # Print created embeddingsfor i, doc_text_embedding in enumerate(doc_texts_embeddings):    print(f"Embedding for document {i + 1}: {doc_text_embedding}")

    # Using a different model and/or custom instructionembeddings = EmbaasEmbeddings(    model="instructor-large",    instruction="Represent the Wikipedia document for retrieval",)

For more detailed information about the embaas Embeddings API, please refer to [the official embaas API documentation](https://embaas.io/api-reference).