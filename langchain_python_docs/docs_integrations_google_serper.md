Google Serper
=============

This page covers how to use the [Serper](https://serper.dev) Google Search API within LangChain. Serper is a low-cost Google Search API that can be used to add answer box, knowledge graph, and organic results data from Google Search. It is broken into two parts: setup, and then references to the specific Google Serper wrapper.

Setup[​](#setup "Direct link to Setup")
---------------------------------------

*   Go to [serper.dev](https://serper.dev) to sign up for a free account
*   Get the api key and set it as an environment variable (`SERPER_API_KEY`)

Wrappers[​](#wrappers "Direct link to Wrappers")
------------------------------------------------

### Utility[​](#utility "Direct link to Utility")

There exists a GoogleSerperAPIWrapper utility which wraps this API. To import this utility:

    from langchain.utilities import GoogleSerperAPIWrapper

You can use it as part of a Self Ask chain:

    from langchain.utilities import GoogleSerperAPIWrapperfrom langchain.llms.openai import OpenAIfrom langchain.agents import initialize_agent, Toolfrom langchain.agents import AgentTypeimport osos.environ["SERPER_API_KEY"] = ""os.environ['OPENAI_API_KEY'] = ""llm = OpenAI(temperature=0)search = GoogleSerperAPIWrapper()tools = [    Tool(        name="Intermediate Answer",        func=search.run,        description="useful for when you need to ask with search"    )]self_ask_with_search = initialize_agent(tools, llm, agent=AgentType.SELF_ASK_WITH_SEARCH, verbose=True)self_ask_with_search.run("What is the hometown of the reigning men's U.S. Open champion?")

#### Output[​](#output "Direct link to Output")

    Entering new AgentExecutor chain... Yes.Follow up: Who is the reigning men's U.S. Open champion?Intermediate answer: Current champions Carlos Alcaraz, 2022 men's singles champion.Follow up: Where is Carlos Alcaraz from?Intermediate answer: El Palmar, SpainSo the final answer is: El Palmar, Spain> Finished chain.'El Palmar, Spain'

For a more detailed walkthrough of this wrapper, see [this notebook](/docs/modules/agents/tools/integrations/google_serper.html).

### Tool[​](#tool "Direct link to Tool")

You can also easily load this wrapper as a Tool (to use with an Agent). You can do this with:

    from langchain.agents import load_toolstools = load_tools(["google-serper"])

For more information on tools, see [this page](/docs/modules/agents/tools/).