DataForSeo API Wrapper
======================

This notebook demonstrates how to use the DataForSeo API wrapper to obtain search engine results. The DataForSeo API allows users to retrieve SERP from most popular search engines like Google, Bing, Yahoo. It also allows to get SERPs from different search engine types like Maps, News, Events, etc.

    from langchain.utilities import DataForSeoAPIWrapper

Setting up the API wrapper with your credentials[](#setting-up-the-api-wrapper-with-your-credentials "Direct link to Setting up the API wrapper with your credentials")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can obtain your API credentials by registering on the DataForSeo website.

    import osos.environ["DATAFORSEO_LOGIN"] = "your_api_access_username"os.environ["DATAFORSEO_PASSWORD"] = "your_api_access_password"wrapper = DataForSeoAPIWrapper()

The run method will return the first result snippet from one of the following elements: answer\_box, knowledge\_graph, featured\_snippet, shopping, organic.

    wrapper.run("Weather in Los Angeles")

The Difference Between `run` and `results`[](#the-difference-between-run-and-results "Direct link to the-difference-between-run-and-results")
----------------------------------------------------------------------------------------------------------------------------------------------

`run` and `results` are two methods provided by the `DataForSeoAPIWrapper` class.

The `run` method executes the search and returns the first result snippet from the answer box, knowledge graph, featured snippet, shopping, or organic results. These elements are sorted by priority from highest to lowest.

The `results` method returns a JSON response configured according to the parameters set in the wrapper. This allows for more flexibility in terms of what data you want to return from the API.

Getting Results as JSON[](#getting-results-as-json "Direct link to Getting Results as JSON")
---------------------------------------------------------------------------------------------

You can customize the result types and fields you want to return in the JSON response. You can also set a maximum count for the number of top results to return.

    json_wrapper = DataForSeoAPIWrapper(    json_result_types=["organic", "knowledge_graph", "answer_box"],    json_result_fields=["type", "title", "description", "text"],    top_count=3,)

    json_wrapper.results("Bill Gates")

Customizing Location and Language[](#customizing-location-and-language "Direct link to Customizing Location and Language")
---------------------------------------------------------------------------------------------------------------------------

You can specify the location and language of your search results by passing additional parameters to the API wrapper.

    customized_wrapper = DataForSeoAPIWrapper(    top_count=10,    json_result_types=["organic", "local_pack"],    json_result_fields=["title", "description", "type"],    params={"location_name": "Germany", "language_code": "en"},)customized_wrapper.results("coffee near me")

Customizing the Search Engine[](#customizing-the-search-engine "Direct link to Customizing the Search Engine")
---------------------------------------------------------------------------------------------------------------

You can also specify the search engine you want to use.

    customized_wrapper = DataForSeoAPIWrapper(    top_count=10,    json_result_types=["organic", "local_pack"],    json_result_fields=["title", "description", "type"],    params={"location_name": "Germany", "language_code": "en", "se_name": "bing"},)customized_wrapper.results("coffee near me")

Customizing the Search Type[](#customizing-the-search-type "Direct link to Customizing the Search Type")
---------------------------------------------------------------------------------------------------------

The API wrapper also allows you to specify the type of search you want to perform. For example, you can perform a maps search.

    maps_search = DataForSeoAPIWrapper(    top_count=10,    json_result_fields=["title", "value", "address", "rating", "type"],    params={        "location_coordinate": "52.512,13.36,12z",        "language_code": "en",        "se_type": "maps",    },)maps_search.results("coffee near me")

Integration with Langchain Agents[](#integration-with-langchain-agents "Direct link to Integration with Langchain Agents")
---------------------------------------------------------------------------------------------------------------------------

You can use the `Tool` class from the `langchain.agents` module to integrate the `DataForSeoAPIWrapper` with a langchain agent. The `Tool` class encapsulates a function that the agent can call.

    from langchain.agents import Toolsearch = DataForSeoAPIWrapper(    top_count=3,    json_result_types=["organic"],    json_result_fields=["title", "description", "type"],)tool = Tool(    name="google-search-answer",    description="My new answer tool",    func=search.run,)json_tool = Tool(    name="google-search-json",    description="My new json tool",    func=search.results,)