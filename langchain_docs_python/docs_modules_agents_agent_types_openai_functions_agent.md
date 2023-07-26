OpenAI functions
================

Certain OpenAI models (like gpt-3.5-turbo-0613 and gpt-4-0613) have been fine-tuned to detect when a function should to be called and respond with the inputs that should be passed to the function. In an API call, you can describe functions and have the model intelligently choose to output a JSON object containing arguments to call those functions. The goal of the OpenAI Function APIs is to more reliably return valid and useful function calls than a generic text completion or chat API.

The OpenAI Functions Agent is designed to work with these models.

Install openai,google-search-results packages which are required as the langchain packages call them internally

> pip install openai google-search-results

    from langchain import LLMMathChain, OpenAI, SerpAPIWrapper, SQLDatabase, SQLDatabaseChainfrom langchain.agents import initialize_agent, Toolfrom langchain.agents import AgentTypefrom langchain.chat_models import ChatOpenAI

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")search = SerpAPIWrapper()llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)db = SQLDatabase.from_uri("sqlite:///../../../../../notebooks/Chinook.db")db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)tools = [    Tool(        name = "Search",        func=search.run,        description="useful for when you need to answer questions about current events. You should ask targeted questions"    ),    Tool(        name="Calculator",        func=llm_math_chain.run,        description="useful for when you need to answer questions about math"    ),    Tool(        name="FooBar-DB",        func=db_chain.run,        description="useful for when you need to answer questions about FooBar. Input should be in the form of a question containing full context"    )]

    agent = initialize_agent(tools, llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=True)

    agent.run("Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?")

        > Entering new  chain...        Invoking: `Search` with `{'query': 'Leo DiCaprio girlfriend'}`            Amidst his casual romance with Gigi, Leo allegedly entered a relationship with 19-year old model, Eden Polani, in February 2023.    Invoking: `Calculator` with `{'expression': '19^0.43'}`        > Entering new  chain...    19^0.43```
text    19**0.43    
```    ...numexpr.evaluate("19**0.43")...        Answer: 3.547023357958959    > Finished chain.    Answer: 3.547023357958959Leo DiCaprio's girlfriend is reportedly Eden Polani. Her current age raised to the power of 0.43 is approximately 3.55.        > Finished chain.    "Leo DiCaprio's girlfriend is reportedly Eden Polani. Her current age raised to the power of 0.43 is approximately 3.55."