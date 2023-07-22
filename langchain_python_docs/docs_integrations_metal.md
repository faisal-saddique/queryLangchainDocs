Metal
=====

This page covers how to use [Metal](https://getmetal.io) within LangChain.

What is Metal?[​](#what-is-metal "Direct link to What is Metal?")
-----------------------------------------------------------------

Metal is a managed retrieval & memory platform built for production. Easily index your data into `Metal` and run semantic search and retrieval on it.

![Metal](/assets/images/MetalDash-f7ba8afe5c172a7967af0e2aa84f1f74.png)

Quick start[​](#quick-start "Direct link to Quick start")
---------------------------------------------------------

Get started by [creating a Metal account](https://app.getmetal.io/signup).

Then, you can easily take advantage of the `MetalRetriever` class to start retrieving your data for semantic search, prompting context, etc. This class takes a `Metal` instance and a dictionary of parameters to pass to the Metal API.

    from langchain.retrievers import MetalRetrieverfrom metal_sdk.metal import Metalmetal = Metal("API_KEY", "CLIENT_ID", "INDEX_ID");retriever = MetalRetriever(metal, params={"limit": 2})docs = retriever.get_relevant_documents("search term")