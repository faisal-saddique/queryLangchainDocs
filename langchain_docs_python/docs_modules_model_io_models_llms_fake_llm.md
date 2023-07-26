Fake LLM
========

We expose a fake LLM class that can be used for testing. This allows you to mock out calls to the LLM and simulate what would happen if the LLM responded in a certain way.

In this notebook we go over how to use this.

We start this with using the FakeLLM in an agent.

    from langchain.llms.fake import FakeListLLM

    from langchain.agents import load_toolsfrom langchain.agents import initialize_agentfrom langchain.agents import AgentType

    tools = load_tools(["python_repl"])

    responses = ["Action: Python REPL\nAction Input: print(2 + 2)", "Final Answer: 4"]llm = FakeListLLM(responses=responses)

    agent = initialize_agent(    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    agent.run("whats 2 + 2")

                > Entering new AgentExecutor chain...    Action: Python REPL    Action Input: print(2 + 2)    Observation: 4        Thought:Final Answer: 4        > Finished chain.    '4'