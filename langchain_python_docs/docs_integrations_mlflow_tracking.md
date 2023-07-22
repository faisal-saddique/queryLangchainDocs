MLflow
======

This notebook goes over how to track your LangChain experiments into your MLflow Server

    pip install azureml-mlflowpip install pandaspip install textstatpip install spacypip install openaipip install google-search-resultspython -m spacy download en_core_web_sm

    import osos.environ["MLFLOW_TRACKING_URI"] = ""os.environ["OPENAI_API_KEY"] = ""os.environ["SERPAPI_API_KEY"] = ""

    from langchain.callbacks import MlflowCallbackHandlerfrom langchain.llms import OpenAI

    """Main function.This function is used to try the callback handler.Scenarios:1. OpenAI LLM2. Chain with multiple SubChains on multiple generations3. Agent with Tools"""mlflow_callback = MlflowCallbackHandler()llm = OpenAI(    model_name="gpt-3.5-turbo", temperature=0, callbacks=[mlflow_callback], verbose=True)

    # SCENARIO 1 - LLMllm_result = llm.generate(["Tell me a joke"])mlflow_callback.flush_tracker(llm)

    from langchain.prompts import PromptTemplatefrom langchain.chains import LLMChain

    # SCENARIO 2 - Chaintemplate = """You are a playwright. Given the title of play, it is your job to write a synopsis for that title.Title: {title}Playwright: This is a synopsis for the above play:"""prompt_template = PromptTemplate(input_variables=["title"], template=template)synopsis_chain = LLMChain(llm=llm, prompt=prompt_template, callbacks=[mlflow_callback])test_prompts = [    {        "title": "documentary about good video games that push the boundary of game design"    },]synopsis_chain.apply(test_prompts)mlflow_callback.flush_tracker(synopsis_chain)

    from langchain.agents import initialize_agent, load_toolsfrom langchain.agents import AgentType

    # SCENARIO 3 - Agent with Toolstools = load_tools(["serpapi", "llm-math"], llm=llm, callbacks=[mlflow_callback])agent = initialize_agent(    tools,    llm,    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,    callbacks=[mlflow_callback],    verbose=True,)agent.run(    "Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?")mlflow_callback.flush_tracker(agent, finish=True)