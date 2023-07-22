Metaphor Search
===============

Metaphor is a search engine fully designed to be used by LLMs. You can search and then get the contents for any page.

This notebook goes over how to use Metaphor search.

First, you need to set up the proper API keys and environment variables. Get 1000 free searches/month [here](https://platform.metaphor.systems/).

Then enter your API key as an environment variable.

    import osos.environ["METAPHOR_API_KEY"] = ""

    from langchain.utilities import MetaphorSearchAPIWrapper

    search = MetaphorSearchAPIWrapper()

Call the API
============

`results` takes in a Metaphor-optimized search query and a number of results (up to 500). It returns a list of results with title, url, author, and creation date.

    search.results("The best blog post about AI safety is definitely this: ", 10)

Adding filters
==============

We can also add filters to our search.

include\_domains: Optional\[List\[str\]\] - List of domains to include in the search. If specified, results will only come from these domains. Only one of include\_domains and exclude\_domains should be specified.

exclude\_domains: Optional\[List\[str\]\] - List of domains to exclude in the search. If specified, results will only come from these domains. Only one of include\_domains and exclude\_domains should be specified.

start\_crawl\_date: Optional\[str\] - "Crawl date" refers to the date that Metaphor discovered a link, which is more granular and can be more useful than published date. If start\_crawl\_date is specified, results will only include links that were crawled after start\_crawl\_date. Must be specified in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ)

end\_crawl\_date: Optional\[str\] - "Crawl date" refers to the date that Metaphor discovered a link, which is more granular and can be more useful than published date. If endCrawlDate is specified, results will only include links that were crawled before end\_crawl\_date. Must be specified in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ)

start\_published\_date: Optional\[str\] - If specified, only links with a published date after start\_published\_date will be returned. Must be specified in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ). Note that for some links, we have no published date, and these links will be excluded from the results if start\_published\_date is specified.

end\_published\_date: Optional\[str\] - If specified, only links with a published date before end\_published\_date will be returned. Must be specified in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ). Note that for some links, we have no published date, and these links will be excluded from the results if end\_published\_date is specified.

See full docs [here](https://metaphorapi.readme.io/).

    search.results(    "The best blog post about AI safety is definitely this: ",    10,    include_domains=["lesswrong.com"],    start_published_date="2019-01-01",)

Use Metaphor as a tool
======================

Metaphor can be used as a tool that gets URLs that other tools such as browsing tools.

    from langchain.agents.agent_toolkits import PlayWrightBrowserToolkitfrom langchain.tools.playwright.utils import (    create_async_playwright_browser,  # A synchronous browser is available, though it isn't compatible with jupyter.)async_browser = create_async_playwright_browser()toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=async_browser)tools = toolkit.get_tools()tools_by_name = {tool.name: tool for tool in tools}print(tools_by_name.keys())navigate_tool = tools_by_name["navigate_browser"]extract_text = tools_by_name["extract_text"]

    from langchain.agents import initialize_agent, AgentTypefrom langchain.chat_models import ChatOpenAIfrom langchain.tools import MetaphorSearchResultsllm = ChatOpenAI(model_name="gpt-4", temperature=0.7)metaphor_tool = MetaphorSearchResults(api_wrapper=search)agent_chain = initialize_agent(    [metaphor_tool, extract_text, navigate_tool],    llm,    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,    verbose=True,)agent_chain.run(    "find me an interesting tweet about AI safety using Metaphor, then tell me the first sentence in the post. Do not finish until able to retrieve the first sentence.")