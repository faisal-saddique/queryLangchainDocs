OpenWeatherMap API
==================

This notebook goes over how to use the OpenWeatherMap component to fetch weather information.

First, you need to sign up for an OpenWeatherMap API key:

1.  Go to OpenWeatherMap and sign up for an API key [here](https://openweathermap.org/api/)
2.  pip install pyowm

Then we will need to set some environment variables:

1.  Save your API KEY into OPENWEATHERMAP\_API\_KEY env variable

Use the wrapper[](#use-the-wrapper "Direct link to Use the wrapper")
---------------------------------------------------------------------

    from langchain.utilities import OpenWeatherMapAPIWrapperimport osos.environ["OPENWEATHERMAP_API_KEY"] = ""weather = OpenWeatherMapAPIWrapper()

    weather_data = weather.run("London,GB")print(weather_data)

        In London,GB, the current weather is as follows:    Detailed status: broken clouds    Wind speed: 2.57 m/s, direction: 240°    Humidity: 55%    Temperature:       - Current: 20.12°C      - High: 21.75°C      - Low: 18.68°C      - Feels like: 19.62°C    Rain: {}    Heat index: None    Cloud cover: 75%

Use the tool[](#use-the-tool "Direct link to Use the tool")
------------------------------------------------------------

    from langchain.llms import OpenAIfrom langchain.agents import load_tools, initialize_agent, AgentTypeimport osos.environ["OPENAI_API_KEY"] = ""os.environ["OPENWEATHERMAP_API_KEY"] = ""llm = OpenAI(temperature=0)tools = load_tools(["openweathermap-api"], llm)agent_chain = initialize_agent(    tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    agent_chain.run("What's the weather like in London?")

                > Entering new AgentExecutor chain...     I need to find out the current weather in London.    Action: OpenWeatherMap    Action Input: London,GB    Observation: In London,GB, the current weather is as follows:    Detailed status: broken clouds    Wind speed: 2.57 m/s, direction: 240°    Humidity: 56%    Temperature:       - Current: 20.11°C      - High: 21.75°C      - Low: 18.68°C      - Feels like: 19.64°C    Rain: {}    Heat index: None    Cloud cover: 75%    Thought: I now know the current weather in London.    Final Answer: The current weather in London is broken clouds, with a wind speed of 2.57 m/s, direction 240°, humidity of 56%, temperature of 20.11°C, high of 21.75°C, low of 18.68°C, and a heat index of None.        > Finished chain.    'The current weather in London is broken clouds, with a wind speed of 2.57 m/s, direction 240°, humidity of 56%, temperature of 20.11°C, high of 21.75°C, low of 18.68°C, and a heat index of None.'