Cassandra
=========

> [Apache Cassandra®](https://cassandra.apache.org/) is a free and open-source, distributed, wide-column store, NoSQL database management system designed to handle large amounts of data across many commodity servers, providing high availability with no single point of failure. Cassandra offers support for clusters spanning multiple datacenters, with asynchronous masterless replication allowing low latency operations for all clients. Cassandra was designed to implement a combination of _Amazon's Dynamo_ distributed storage and replication techniques combined with _Google's Bigtable_ data and storage engine model.

Installation and Setup[​](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

    pip install cassandra-driverpip install cassio

Vector Store[​](#vector-store "Direct link to Vector Store")
------------------------------------------------------------

See a [usage example](/docs/modules/data_connection/vectorstores/integrations/cassandra.html).

    from langchain.memory import CassandraChatMessageHistory

Memory[​](#memory "Direct link to Memory")
------------------------------------------

See a [usage example](/docs/modules/memory/integrations/cassandra_chat_message_history.html).

    from langchain.memory import CassandraChatMessageHistory