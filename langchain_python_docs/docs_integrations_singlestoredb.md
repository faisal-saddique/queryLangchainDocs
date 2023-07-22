SingleStoreDB
=============

> [SingleStoreDB](https://singlestore.com/) is a high-performance distributed SQL database that supports deployment both in the [cloud](https://www.singlestore.com/cloud/) and on-premises. It provides vector storage, and vector functions including [dot\_product](https://docs.singlestore.com/managed-service/en/reference/sql-reference/vector-functions/dot_product.html) and [euclidean\_distance](https://docs.singlestore.com/managed-service/en/reference/sql-reference/vector-functions/euclidean_distance.html), thereby supporting AI applications that require text similarity matching.

Installation and Setup[​](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

There are several ways to establish a [connection](https://singlestoredb-python.labs.singlestore.com/generated/singlestoredb.connect.html) to the database. You can either set up environment variables or pass named parameters to the `SingleStoreDB constructor`. Alternatively, you may provide these parameters to the `from_documents` and `from_texts` methods.

    pip install singlestoredb

Vector Store[​](#vector-store "Direct link to Vector Store")
------------------------------------------------------------

See a [usage example](/docs/modules/data_connection/vectorstores/integrations/singlestoredb.html).

    from langchain.vectorstores import SingleStoreDB