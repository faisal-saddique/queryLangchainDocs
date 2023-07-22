Google Search
=============

This page covers how to use the Google Search API within LangChain. It is broken into two parts: installation and setup, and then references to the specific Google Search wrapper.

Installation and Setup[​](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

*   Install requirements with `pip install google-api-python-client`
*   Set up a Custom Search Engine, following [these instructions](https://stackoverflow.com/questions/37083058/programmatically-searching-google-in-python-using-custom-search)
*   Get an API Key and Custom Search Engine ID from the previous step, and set them as environment variables `GOOGLE_API_KEY` and `GOOGLE_CSE_ID` respectively

Wrappers[​](#wrappers "Direct link to Wrappers")
------------------------------------------------

### Utility[​](#utility "Direct link to Utility")

There exists a GoogleSearchAPIWrapper utility which wraps this API. To import this utility:

    from langchain.utilities import GoogleSearchAPIWrapper

For a more detailed walkthrough of this wrapper, see [this notebook](/docs/modules/agents/tools/integrations/google_search.html).

### Tool[​](#tool "Direct link to Tool")

You can also easily load this wrapper as a Tool (to use with an Agent). You can do this with:

    from langchain.agents import load_toolstools = load_tools(["google-search"])

For more information on tools, see [this page](/docs/modules/agents/tools/).