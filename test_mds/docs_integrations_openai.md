Chroma
======

> [Chroma](https://docs.trychroma.com/getting-started) is a database for building AI applications with embeddings.

Installation and Setup[](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

    pip install chromadb

VectorStore[](#vectorstore "Direct link to VectorStore")
---------------------------------------------------------

There exists a wrapper around Chroma vector databases, allowing you to use it as a vectorstore, whether for semantic search or example selection.

    from langchain.vectorstores import Chroma

For a more detailed walkthrough of the Chroma wrapper, see [this notebook](/docs/integrations/vectorstores/chroma.html)

Retriever[](#retriever "Direct link to Retriever")
---------------------------------------------------

See a [usage example](/docs/modules/data_connection/retrievers/how_to/self_query/chroma_self_query).

    from langchain.retrievers import SelfQueryRetriever