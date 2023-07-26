Cohere
======

> [Cohere](https://cohere.ai/about) is a Canadian startup that provides natural language processing models that help companies improve human-machine interactions.

Installation and Setup[](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

*   Install the Python SDK :

    pip install cohere

Get a [Cohere api key](https://dashboard.cohere.ai/) and set it as an environment variable (`COHERE_API_KEY`)

LLM[](#llm "Direct link to LLM")
---------------------------------

There exists an Cohere LLM wrapper, which you can access with See a [usage example](/docs/integrations/llms/cohere).

    from langchain.llms import Cohere

Text Embedding Model[](#text-embedding-model "Direct link to Text Embedding Model")
------------------------------------------------------------------------------------

There exists an Cohere Embedding model, which you can access with

    from langchain.embeddings import CohereEmbeddings

For a more detailed walkthrough of this, see [this notebook](/docs/integrations/text_embedding/cohere.html)

Retriever[](#retriever "Direct link to Retriever")
---------------------------------------------------

See a [usage example](/docs/integrations/retrievers/cohere-reranker).

    from langchain.retrievers.document_compressors import CohereRerank