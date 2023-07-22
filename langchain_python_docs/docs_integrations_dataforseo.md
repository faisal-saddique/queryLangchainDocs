DataForSEO
==========

This page provides instructions on how to use the DataForSEO search APIs within LangChain.

Installation and Setup[​](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

*   Get a DataForSEO API Access login and password, and set them as environment variables (`DATAFORSEO_LOGIN` and `DATAFORSEO_PASSWORD` respectively). You can find it in your dashboard.

Wrappers[​](#wrappers "Direct link to Wrappers")
------------------------------------------------

### Utility[​](#utility "Direct link to Utility")

The DataForSEO utility wraps the API. To import this utility, use:

    from langchain.utilities import DataForSeoAPIWrapper

For a detailed walkthrough of this wrapper, see [this notebook](/docs/modules/agents/tools/integrations/dataforseo.ipynb).

### Tool[​](#tool "Direct link to Tool")

You can also load this wrapper as a Tool to use with an Agent:

    from langchain.agents import load_toolstools = load_tools(["dataforseo-api-search"])

Example usage[​](#example-usage "Direct link to Example usage")
---------------------------------------------------------------

    dataforseo = DataForSeoAPIWrapper(api_login="your_login", api_password="your_password")result = dataforseo.run("Bill Gates")print(result)

Environment Variables[​](#environment-variables "Direct link to Environment Variables")
---------------------------------------------------------------------------------------

You can store your DataForSEO API Access login and password as environment variables. The wrapper will automatically check for these environment variables if no values are provided:

    import osos.environ["DATAFORSEO_LOGIN"] = "your_login"os.environ["DATAFORSEO_PASSWORD"] = "your_password"dataforseo = DataForSeoAPIWrapper()result = dataforseo.run("weather in Los Angeles")print(result)