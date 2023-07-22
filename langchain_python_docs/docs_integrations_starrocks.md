StarRocks
=========

> [StarRocks](https://www.starrocks.io/) is a High-Performance Analytical Database. `StarRocks` is a next-gen sub-second MPP database for full analytics scenarios, including multi-dimensional analytics, real-time analytics and ad-hoc query.

> Usually `StarRocks` is categorized into OLAP, and it has showed excellent performance in [ClickBench — a Benchmark For Analytical DBMS](https://benchmark.clickhouse.com/). Since it has a super-fast vectorized execution engine, it could also be used as a fast vectordb.

Installation and Setup[​](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

    pip install pymysql

Vector Store[​](#vector-store "Direct link to Vector Store")
------------------------------------------------------------

See a [usage example](/docs/modules/data_connection/vectorstores/integrations/starrocks.html).

    from langchain.vectorstores import StarRocks