ReAct
=====

This walkthrough showcases using an agent to implement the [ReAct](https://react-lm.github.io/) logic.

    from langchain.agents import load_toolsfrom langchain.agents import initialize_agentfrom langchain.agents import AgentTypefrom langchain.llms import OpenAI

First, let's load the language model we're going to use to control the agent.

    llm = OpenAI(temperature=0)

Next, let's load some tools to use. Note that the `llm-math` tool uses an LLM, so we need to pass that in.

    tools = load_tools(["serpapi", "llm-math"], llm=llm)

Finally, let's initialize an agent with the tools, the language model, and the type of agent we want to use.

    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

Now let's test it out!

    agent.run("Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?")

        > Entering new AgentExecutor chain...     I need to find out who Leo DiCaprio's girlfriend is and then calculate her age raised to the 0.43 power.    Action: Search    Action Input: "Leo DiCaprio girlfriend"    Observation: Camila Morrone    Thought: I need to find out Camila Morrone's age    Action: Search    Action Input: "Camila Morrone age"    Observation: 25 years    Thought: I need to calculate 25 raised to the 0.43 power    Action: Calculator    Action Input: 25^0.43    Observation: Answer: 3.991298452658078        Thought: I now know the final answer    Final Answer: Camila Morrone is Leo DiCaprio's girlfriend and her current age raised to the 0.43 power is 3.991298452658078.        > Finished chain.    "Camila Morrone is Leo DiCaprio's girlfriend and her current age raised to the 0.43 power is 3.991298452658078."

Using chat models[​](#using-chat-models "Direct link to Using chat models")
---------------------------------------------------------------------------

You can also create ReAct agents that use chat models instead of LLMs as the agent driver.

    from langchain.chat_models import ChatOpenAIchat_model = ChatOpenAI(temperature=0)agent = initialize_agent(tools, chat_model, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)agent.run("Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?")