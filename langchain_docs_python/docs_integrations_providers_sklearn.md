scikit-learn
============

> [scikit-learn](https://scikit-learn.org/stable/) is an open source collection of machine learning algorithms, including some implementations of the [k nearest neighbors](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html). `SKLearnVectorStore` wraps this implementation and adds the possibility to persist the vector store in json, bson (binary json) or Apache Parquet format.

Installation and Setup[](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

*   Install the Python package with `pip install scikit-learn`

Vector Store[](#vector-store "Direct link to Vector Store")
------------------------------------------------------------

`SKLearnVectorStore` provides a simple wrapper around the nearest neighbor implementation in the scikit-learn package, allowing you to use it as a vectorstore.

To import this vectorstore:

    from langchain.vectorstores import SKLearnVectorStore

For a more detailed walkthrough of the SKLearnVectorStore wrapper, see [this notebook](/docs/integrations/vectorstores/sklearn.html).