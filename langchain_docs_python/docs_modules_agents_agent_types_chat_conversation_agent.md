Conversational
==============

This walkthrough demonstrates how to use an agent optimized for conversation. Other agents are often optimized for using tools to figure out the best response, which is not ideal in a conversational setting where you may want the agent to be able to chat with the user as well.

This is accomplished with a specific type of agent (`conversational-react-description`) which expects to be used with a memory component.

    from langchain.agents import Toolfrom langchain.agents import AgentTypefrom langchain.memory import ConversationBufferMemoryfrom langchain import OpenAIfrom langchain.utilities import SerpAPIWrapperfrom langchain.agents import initialize_agent

    search = SerpAPIWrapper()tools = [    Tool(        name = "Current Search",        func=search.run,        description="useful for when you need to answer questions about current events or the current state of the world"    ),]

    memory = ConversationBufferMemory(memory_key="chat_history")

    llm=OpenAI(temperature=0)agent_chain = initialize_agent(tools, llm, agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION, verbose=True, memory=memory)

    agent_chain.run(input="hi, i am bob")

        > Entering new AgentExecutor chain...        Thought: Do I need to use a tool? No    AI: Hi Bob, nice to meet you! How can I help you today?        > Finished chain.    'Hi Bob, nice to meet you! How can I help you today?'

    agent_chain.run(input="what's my name?")

        > Entering new AgentExecutor chain...        Thought: Do I need to use a tool? No    AI: Your name is Bob!        > Finished chain.    'Your name is Bob!'

    agent_chain.run("what are some good dinners to make this week, if i like thai food?")

        > Entering new AgentExecutor chain...        Thought: Do I need to use a tool? Yes    Action: Current Search    Action Input: Thai food dinner recipes    Observation: 59 easy Thai recipes for any night of the week · Marion Grasby's Thai spicy chilli and basil fried rice · Thai curry noodle soup · Marion Grasby's Thai Spicy ...    Thought: Do I need to use a tool? No    AI: Here are some great Thai dinner recipes you can try this week: Marion Grasby's Thai Spicy Chilli and Basil Fried Rice, Thai Curry Noodle Soup, Thai Green Curry with Coconut Rice, Thai Red Curry with Vegetables, and Thai Coconut Soup. I hope you enjoy them!        > Finished chain.    "Here are some great Thai dinner recipes you can try this week: Marion Grasby's Thai Spicy Chilli and Basil Fried Rice, Thai Curry Noodle Soup, Thai Green Curry with Coconut Rice, Thai Red Curry with Vegetables, and Thai Coconut Soup. I hope you enjoy them!"

    agent_chain.run(input="tell me the last letter in my name, and also tell me who won the world cup in 1978?")

        > Entering new AgentExecutor chain...        Thought: Do I need to use a tool? Yes    Action: Current Search    Action Input: Who won the World Cup in 1978    Observation: Argentina national football team    Thought: Do I need to use a tool? No    AI: The last letter in your name is "b" and the winner of the 1978 World Cup was the Argentina national football team.        > Finished chain.    'The last letter in your name is "b" and the winner of the 1978 World Cup was the Argentina national football team.'

    agent_chain.run(input="whats the current temperature in pomfret?")

        > Entering new AgentExecutor chain...        Thought: Do I need to use a tool? Yes    Action: Current Search    Action Input: Current temperature in Pomfret    Observation: Partly cloudy skies. High around 70F. Winds W at 5 to 10 mph. Humidity41%.    Thought: Do I need to use a tool? No    AI: The current temperature in Pomfret is around 70F with partly cloudy skies and winds W at 5 to 10 mph. The humidity is 41%.        > Finished chain.    'The current temperature in Pomfret is around 70F with partly cloudy skies and winds W at 5 to 10 mph. The humidity is 41%.'

Using a chat model[](#using-a-chat-model "Direct link to Using a chat model")
------------------------------------------------------------------------------

The `chat-conversational-react-description` agent type lets us create a conversational agent using a chat model instead of an LLM.

    from langchain.memory import ConversationBufferMemoryfrom langchain.chat_models import ChatOpenAImemory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0)agent_chain = initialize_agent(tools, llm, agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION, verbose=True, memory=memory)

    agent_chain.run(input="hi, i am bob")

        > Entering new AgentExecutor chain...    {        "action": "Final Answer",        "action_input": "Hello Bob! How can I assist you today?"    }        > Finished chain.    'Hello Bob! How can I assist you today?'

    agent_chain.run(input="what's my name?")

        > Entering new AgentExecutor chain...    {        "action": "Final Answer",        "action_input": "Your name is Bob."    }        > Finished chain.    'Your name is Bob.'

    agent_chain.run("what are some good dinners to make this week, if i like thai food?")

        > Entering new AgentExecutor chain...    {        "action": "Current Search",        "action_input": "Thai food dinner recipes"    }    Observation: 64 easy Thai recipes for any night of the week · Thai curry noodle soup · Thai yellow cauliflower, snake bean and tofu curry · Thai-spiced chicken hand pies · Thai ...    Thought:{        "action": "Final Answer",        "action_input": "Here are some Thai food dinner recipes you can try this week: Thai curry noodle soup, Thai yellow cauliflower, snake bean and tofu curry, Thai-spiced chicken hand pies, and many more. You can find the full list of recipes at the source I found earlier."    }        > Finished chain.    'Here are some Thai food dinner recipes you can try this week: Thai curry noodle soup, Thai yellow cauliflower, snake bean and tofu curry, Thai-spiced chicken hand pies, and many more. You can find the full list of recipes at the source I found earlier.'

    agent_chain.run(input="tell me the last letter in my name, and also tell me who won the world cup in 1978?")

        > Entering new AgentExecutor chain...    {        "action": "Final Answer",        "action_input": "The last letter in your name is 'b'. Argentina won the World Cup in 1978."    }        > Finished chain.    "The last letter in your name is 'b'. Argentina won the World Cup in 1978."

    agent_chain.run(input="whats the weather like in pomfret?")

        > Entering new AgentExecutor chain...    {        "action": "Current Search",        "action_input": "weather in pomfret"    }    Observation: Cloudy with showers. Low around 55F. Winds S at 5 to 10 mph. Chance of rain 60%. Humidity76%.    Thought:{        "action": "Final Answer",        "action_input": "Cloudy with showers. Low around 55F. Winds S at 5 to 10 mph. Chance of rain 60%. Humidity76%."    }        > Finished chain.    'Cloudy with showers. Low around 55F. Winds S at 5 to 10 mph. Chance of rain 60%. Humidity76%.'