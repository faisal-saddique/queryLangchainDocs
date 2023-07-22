Banana
======

[Banana](https://www.banana.dev/about-us) is focused on building the machine learning infrastructure.

This example goes over how to use LangChain to interact with Banana models

    # Install the package  https://docs.banana.dev/banana-docs/core-concepts/sdks/pythonpip install banana-dev

    # get new tokens: https://app.banana.dev/# We need two tokens, not just an `api_key`: `BANANA_API_KEY` and `YOUR_MODEL_KEY`import osfrom getpass import getpassos.environ["BANANA_API_KEY"] = "YOUR_API_KEY"# OR# BANANA_API_KEY = getpass()

    from langchain.llms import Bananafrom langchain import PromptTemplate, LLMChain

    template = """Question: {question}Answer: Let's think step by step."""prompt = PromptTemplate(template=template, input_variables=["question"])

    llm = Banana(model_key="YOUR_MODEL_KEY")

    llm_chain = LLMChain(prompt=prompt, llm=llm)

    question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"llm_chain.run(question)