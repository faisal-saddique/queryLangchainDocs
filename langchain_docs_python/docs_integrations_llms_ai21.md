AI21
====

[AI21 Studio](https://docs.ai21.com/) provides API access to `Jurassic-2` large language models.

This example goes over how to use LangChain to interact with [AI21 models](https://docs.ai21.com/docs/jurassic-2-models).

    # install the package:pip install ai21

    # get AI21_API_KEY. Use https://studio.ai21.com/account/accountfrom getpass import getpassAI21_API_KEY = getpass()

         ········

    from langchain.llms import AI21from langchain import PromptTemplate, LLMChain

    template = """Question: {question}Answer: Let's think step by step."""prompt = PromptTemplate(template=template, input_variables=["question"])

    llm = AI21(ai21_api_key=AI21_API_KEY)

    llm_chain = LLMChain(prompt=prompt, llm=llm)

    question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"llm_chain.run(question)

        '\n1. What year was Justin Bieber born?\nJustin Bieber was born in 1994.\n2. What team won the Super Bowl in 1994?\nThe Dallas Cowboys won the Super Bowl in 1994.'