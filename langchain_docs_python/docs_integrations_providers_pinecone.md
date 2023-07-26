Pinecone
========

This page covers how to use the Pinecone ecosystem within LangChain. It is broken into two parts: installation and setup, and then references to specific Pinecone wrappers.

Installation and Setup[](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

Install the Python SDK:

    pip install pinecone-client

Vectorstore[](#vectorstore "Direct link to Vectorstore")
---------------------------------------------------------

There exists a wrapper around Pinecone indexes, allowing you to use it as a vectorstore, whether for semantic search or example selection.

    from langchain.vectorstores import Pinecone

For a more detailed walkthrough of the Pinecone vectorstore, see [this notebook](/docs/integrations/vectorstores/pinecone.html)