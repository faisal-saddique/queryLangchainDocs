Zilliz
======

> [Zilliz Cloud](https://zilliz.com/doc/quick_start) is a fully managed service on cloud for `LF AI Milvus®`,

Installation and Setup[](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

Install the Python SDK:

    pip install pymilvus

Vectorstore[](#vectorstore "Direct link to Vectorstore")
---------------------------------------------------------

A wrapper around Zilliz indexes allows you to use it as a vectorstore, whether for semantic search or example selection.

    from langchain.vectorstores import Milvus

For a more detailed walkthrough of the Miluvs wrapper, see [this notebook](/docs/integrations/vectorstores/zilliz.html)