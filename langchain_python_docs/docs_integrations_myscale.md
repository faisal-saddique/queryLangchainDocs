MyScale
=======

This page covers how to use MyScale vector database within LangChain. It is broken into two parts: installation and setup, and then references to specific MyScale wrappers.

With MyScale, you can manage both structured and unstructured (vectorized) data, and perform joint queries and analytics on both types of data using SQL. Plus, MyScale's cloud-native OLAP architecture, built on top of ClickHouse, enables lightning-fast data processing even on massive datasets.

Introduction[​](#introduction "Direct link to Introduction")
------------------------------------------------------------

[Overview to MyScale and High performance vector search](https://docs.myscale.com/en/overview/)

You can now register on our SaaS and [start a cluster now!](https://docs.myscale.com/en/quickstart/)

If you are also interested in how we managed to integrate SQL and vector, please refer to [this document](https://docs.myscale.com/en/vector-reference/) for further syntax reference.

We also deliver with live demo on huggingface! Please checkout our [huggingface space](https://huggingface.co/myscale)! They search millions of vector within a blink!

Installation and Setup[​](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

*   Install the Python SDK with `pip install clickhouse-connect`

### Setting up environments[​](#setting-up-environments "Direct link to Setting up environments")

There are two ways to set up parameters for myscale index.

1.  Environment Variables
    
    Before you run the app, please set the environment variable with `export`: `export MYSCALE_HOST='<your-endpoints-url>' MYSCALE_PORT=<your-endpoints-port> MYSCALE_USERNAME=<your-username> MYSCALE_PASSWORD=<your-password> ...`
    
    You can easily find your account, password and other info on our SaaS. For details please refer to [this document](https://docs.myscale.com/en/cluster-management/) Every attributes under `MyScaleSettings` can be set with prefix `MYSCALE_` and is case insensitive.
    
2.  Create `MyScaleSettings` object with parameters
    

    ```pythonfrom langchain.vectorstores import MyScale, MyScaleSettingsconfig = MyScaleSetting(host="<your-backend-url>", port=8443, ...)index = MyScale(embedding_function, config)index.add_documents(...)```

Wrappers[​](#wrappers "Direct link to Wrappers")
------------------------------------------------

supported functions:

*   `add_texts`
*   `add_documents`
*   `from_texts`
*   `from_documents`
*   `similarity_search`
*   `asimilarity_search`
*   `similarity_search_by_vector`
*   `asimilarity_search_by_vector`
*   `similarity_search_with_relevance_scores`

### VectorStore[​](#vectorstore "Direct link to VectorStore")

There exists a wrapper around MyScale database, allowing you to use it as a vectorstore, whether for semantic search or similar example retrieval.

To import this vectorstore:

    from langchain.vectorstores import MyScale

For a more detailed walkthrough of the MyScale wrapper, see [this notebook](/docs/modules/data_connection/vectorstores/integrations/myscale.html)