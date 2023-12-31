StochasticAI
============

> [Stochastic Acceleration Platform](https://docs.stochastic.ai/docs/introduction/) aims to simplify the life cycle of a Deep Learning model. From uploading and versioning the model, through training, compression and acceleration to putting it into production.

This example goes over how to use LangChain to interact with `StochasticAI` models.

You have to get the API\_KEY and the API\_URL [here](https://app.stochastic.ai/workspace/profile/settings?tab=profile).

    from getpass import getpassSTOCHASTICAI_API_KEY = getpass()

         ········

    import osos.environ["STOCHASTICAI_API_KEY"] = STOCHASTICAI_API_KEY

    YOUR_API_URL = getpass()

         ········

    from langchain.llms import StochasticAIfrom langchain import PromptTemplate, LLMChain

    template = """Question: {question}Answer: Let's think step by step."""prompt = PromptTemplate(template=template, input_variables=["question"])

    llm = StochasticAI(api_url=YOUR_API_URL)

    llm_chain = LLMChain(prompt=prompt, llm=llm)

    question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"llm_chain.run(question)

        "\n\nStep 1: In 1999, the St. Louis Rams won the Super Bowl.\n\nStep 2: In 1999, Beiber was born.\n\nStep 3: The Rams were in Los Angeles at the time.\n\nStep 4: So they didn't play in the Super Bowl that year.\n"