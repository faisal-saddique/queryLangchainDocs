Weaviate
========

This page covers how to use the Weaviate ecosystem within LangChain.

What is Weaviate?

**Weaviate in a nutshell:**

*   Weaviate is an open-source database of the type vector search engine.
*   Weaviate allows you to store JSON documents in a class property-like fashion while attaching machine learning vectors to these documents to represent them in vector space.
*   Weaviate can be used stand-alone (aka bring your vectors) or with a variety of modules that can do the vectorization for you and extend the core capabilities.
*   Weaviate has a GraphQL-API to access your data easily.
*   We aim to bring your vector search set up to production to query in mere milliseconds (check our [open source benchmarks](https://weaviate.io/developers/weaviate/current/benchmarks/) to see if Weaviate fits your use case).
*   Get to know Weaviate in the [basics getting started guide](https://weaviate.io/developers/weaviate/current/core-knowledge/basics.html) in under five minutes.

**Weaviate in detail:**

Weaviate is a low-latency vector search engine with out-of-the-box support for different media types (text, images, etc.). It offers Semantic Search, Question-Answer Extraction, Classification, Customizable Models (PyTorch/TensorFlow/Keras), etc. Built from scratch in Go, Weaviate stores both objects and vectors, allowing for combining vector search with structured filtering and the fault tolerance of a cloud-native database. It is all accessible through GraphQL, REST, and various client-side programming languages.

Installation and Setup[](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

*   Install the Python SDK with `pip install weaviate-client`

Wrappers[](#wrappers "Direct link to Wrappers")
------------------------------------------------

### VectorStore[](#vectorstore "Direct link to VectorStore")

There exists a wrapper around Weaviate indexes, allowing you to use it as a vectorstore, whether for semantic search or example selection.

To import this vectorstore:

    from langchain.vectorstores import Weaviate

For a more detailed walkthrough of the Weaviate wrapper, see [this notebook](/docs/integrations/vectorstores/weaviate.html)