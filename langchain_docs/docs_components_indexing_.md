Indexes
=======

info

[Python Guide](https://python.langchain.com/en/latest/modules/indexes.html)

[JS Guide](https://js.langchain.com/docs/modules/indexes/)

Indexes refer to ways to structure documents so that LLMs can best interact with them. This module contains utility functions for working with documents, different types of indexes, and then examples for using those indexes in chains.

The most common way that indexes are used in chains is in a "retrieval" step. This step refers to taking a user's query and returning the most relevant documents. We draw this distinction because (1) an index can be used for other things besides retrieval, and (2) retrieval can use other logic besides an index to find relevant documents. We therefor have a concept of a "Retriever" interface - this is the interface that most chains work with.

Most of the time when we talk about indexes and retrieval we are talking about indexing and retrieving unstructured data (like text documents). For interacting with structured data (SQL tables, etc) or APIs, please see the corresponding use case sections for links to relevant functionality. The primary index and retrieval types supported by LangChain are currently centered around vector databases, and therefore a lot of the functionality we dive deep on those topics.

**Document Loaders**

Classes responsible for loading documents from various sources.

**Text Splitters**

Classes responsible for splitting text into smaller chunks.

**VectorStores**

The most common type of index. One that relies on embeddings.

**Retrievers**

Interface for fetching relevant documents to combine with language models.

Go deeper[​](#go-deeper "Direct link to Go deeper")
---------------------------------------------------

[

📄️ Document Loaders
--------------------

Python Guide

](/docs/components/indexing/document-loaders)

[

📄️ Text Splitters
------------------

Python Guide

](/docs/components/indexing/text-splitters)

[

📄️ Retriever
-------------

Python Guide

](/docs/components/indexing/retriever)

[

📄️ Vectorstore
---------------

Python Guide

](/docs/components/indexing/vectorstore)