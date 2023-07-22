Access intermediate steps
=========================

In order to get more visibility into what an agent is doing, we can also return intermediate steps. This comes in the form of an extra key in the return value, which is a list of (action, observation) tuples.

    from langchain.agents import load_toolsfrom langchain.agents import initialize_agentfrom langchain.agents import AgentTypefrom langchain.llms import OpenAI

Initialize the components needed for the agent.

    llm = OpenAI(temperature=0, model_name="text-davinci-002")tools = load_tools(["serpapi", "llm-math"], llm=llm)

Initialize the agent with `return_intermediate_steps=True`

    agent = initialize_agent(    tools,    llm,    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,    verbose=True,    return_intermediate_steps=True,)

    response = agent(    {        "input": "Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?"    })

                > Entering new AgentExecutor chain...     I should look up who Leo DiCaprio is dating    Action: Search    Action Input: "Leo DiCaprio girlfriend"    Observation: Camila Morrone    Thought: I should look up how old Camila Morrone is    Action: Search    Action Input: "Camila Morrone age"    Observation: 25 years    Thought: I should calculate what 25 years raised to the 0.43 power is    Action: Calculator    Action Input: 25^0.43    Observation: Answer: 3.991298452658078        Thought: I now know the final answer    Final Answer: Camila Morrone is Leo DiCaprio's girlfriend and she is 3.991298452658078 years old.        > Finished chain.

    # The actual return type is a NamedTuple for the agent action, and then an observationprint(response["intermediate_steps"])

        [(AgentAction(tool='Search', tool_input='Leo DiCaprio girlfriend', log=' I should look up who Leo DiCaprio is dating\nAction: Search\nAction Input: "Leo DiCaprio girlfriend"'), 'Camila Morrone'), (AgentAction(tool='Search', tool_input='Camila Morrone age', log=' I should look up how old Camila Morrone is\nAction: Search\nAction Input: "Camila Morrone age"'), '25 years'), (AgentAction(tool='Calculator', tool_input='25^0.43', log=' I should calculate what 25 years raised to the 0.43 power is\nAction: Calculator\nAction Input: 25^0.43'), 'Answer: 3.991298452658078\n')]

    import jsonprint(json.dumps(response["intermediate_steps"], indent=2))

        [      [        [          "Search",          "Leo DiCaprio girlfriend",          " I should look up who Leo DiCaprio is dating\nAction: Search\nAction Input: \"Leo DiCaprio girlfriend\""        ],        "Camila Morrone"      ],      [        [          "Search",          "Camila Morrone age",          " I should look up how old Camila Morrone is\nAction: Search\nAction Input: \"Camila Morrone age\""        ],        "25 years"      ],      [        [          "Calculator",          "25^0.43",          " I should calculate what 25 years raised to the 0.43 power is\nAction: Calculator\nAction Input: 25^0.43"        ],        "Answer: 3.991298452658078\n"      ]    ]