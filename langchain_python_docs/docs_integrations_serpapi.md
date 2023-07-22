SerpAPI
=======

This page covers how to use the SerpAPI search APIs within LangChain. It is broken into two parts: installation and setup, and then references to the specific SerpAPI wrapper.

Installation and Setup[​](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

*   Install requirements with `pip install google-search-results`
*   Get a SerpAPI api key and either set it as an environment variable (`SERPAPI_API_KEY`)

Wrappers[​](#wrappers "Direct link to Wrappers")
------------------------------------------------

### Utility[​](#utility "Direct link to Utility")

There exists a SerpAPI utility which wraps this API. To import this utility:

    from langchain.utilities import SerpAPIWrapper

For a more detailed walkthrough of this wrapper, see [this notebook](/docs/modules/agents/tools/integrations/serpapi.html).

### Tool[​](#tool "Direct link to Tool")

You can also easily load this wrapper as a Tool (to use with an Agent). You can do this with:

    from langchain.agents import load_toolstools = load_tools(["serpapi"])

For more information on this, see [this page](/docs/modules/agents/tools)