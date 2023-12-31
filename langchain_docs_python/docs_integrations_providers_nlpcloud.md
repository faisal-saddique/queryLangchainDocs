NLPCloud
========

This page covers how to use the NLPCloud ecosystem within LangChain. It is broken into two parts: installation and setup, and then references to specific NLPCloud wrappers.

Installation and Setup[](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

*   Install the Python SDK with `pip install nlpcloud`
*   Get an NLPCloud api key and set it as an environment variable (`NLPCLOUD_API_KEY`)

Wrappers[](#wrappers "Direct link to Wrappers")
------------------------------------------------

### LLM[](#llm "Direct link to LLM")

There exists an NLPCloud LLM wrapper, which you can access with

    from langchain.llms import NLPCloud