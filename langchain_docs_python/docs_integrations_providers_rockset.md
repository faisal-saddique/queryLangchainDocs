Rockset
=======

> [Rockset](https://rockset.com/product/) is a real-time analytics database service for serving low latency, high concurrency analytical queries at scale. It builds a Converged Index™ on structured and semi-structured data with an efficient store for vector embeddings. Its support for running SQL on schemaless data makes it a perfect choice for running vector search with metadata filters.

Installation and Setup[](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

Make sure you have Rockset account and go to the web console to get the API key. Details can be found on [the website](https://rockset.com/docs/rest-api/).

    pip install rockset

Vector Store[](#vector-store "Direct link to Vector Store")
------------------------------------------------------------

See a [usage example](/docs/integrations/vectorstores/rockset).

    from langchain.vectorstores import RocksetDB

Document Loader[](#document-loader "Direct link to Document Loader")
---------------------------------------------------------------------

See a [usage example](/docs/integrations/providers/docs/modules/data_connection/document_loaders/integrations/rockset).

    from langchain.document_loaders import RocksetLoader