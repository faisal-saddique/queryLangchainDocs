Self ask with search
====================

This walkthrough showcases the Self Ask With Search chain.

    from langchain import OpenAI, SerpAPIWrapperfrom langchain.agents import initialize_agent, Toolfrom langchain.agents import AgentTypellm = OpenAI(temperature=0)search = SerpAPIWrapper()tools = [    Tool(        name="Intermediate Answer",        func=search.run,        description="useful for when you need to ask with search",    )]self_ask_with_search = initialize_agent(    tools, llm, agent=AgentType.SELF_ASK_WITH_SEARCH, verbose=True)self_ask_with_search.run(    "What is the hometown of the reigning men's U.S. Open champion?")

                > Entering new AgentExecutor chain...     Yes.    Follow up: Who is the reigning men's U.S. Open champion?    Intermediate answer: Carlos Alcaraz Garfia    Follow up: Where is Carlos Alcaraz Garfia from?    Intermediate answer: El Palmar, Spain    So the final answer is: El Palmar, Spain        > Finished chain.    'El Palmar, Spain'