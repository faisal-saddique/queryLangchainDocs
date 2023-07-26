ArangoDB
========

> [ArangoDB](https://github.com/arangodb/arangodb) is a scalable graph database system to drive value from connected data, faster. Native graphs, an integrated search engine, and JSON support, via a single query language. ArangoDB runs on-prem, in the cloud – anywhere.

Dependencies[](#dependencies "Direct link to Dependencies")
------------------------------------------------------------

Install the [ArangoDB Python Driver](https://github.com/ArangoDB-Community/python-arango) package with

    pip install python-arango

Graph QA Chain[](#graph-qa-chain "Direct link to Graph QA Chain")
------------------------------------------------------------------

Connect your ArangoDB Database with a Chat Model to get insights on your data.

See the notebook example [here](/docs/modules/chains/additional/graph_arangodb_qa.html).

    from arango import ArangoClientfrom langchain.graphs import ArangoGraphfrom langchain.chains import ArangoGraphQAChain