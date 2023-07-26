AzureOpenAI
===========

Let's load the OpenAI Embedding class with environment variables set to indicate to use Azure endpoints.

    # set the environment variables needed for openai package to know to reach out to azureimport osos.environ["OPENAI_API_TYPE"] = "azure"os.environ["OPENAI_API_BASE"] = "https://<your-endpoint.openai.azure.com/"os.environ["OPENAI_API_KEY"] = "your AzureOpenAI key"os.environ["OPENAI_API_VERSION"] = "2023-05-15"

    from langchain.embeddings import OpenAIEmbeddingsembeddings = OpenAIEmbeddings(deployment="your-embeddings-deployment-name")

    text = "This is a test document."

    query_result = embeddings.embed_query(text)

    doc_result = embeddings.embed_documents([text])