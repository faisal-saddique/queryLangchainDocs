Aleph Alpha
===========

[The Luminous series](https://docs.aleph-alpha.com/docs/introduction/luminous/) is a family of large language models.

This example goes over how to use LangChain to interact with Aleph Alpha models

    # Install the packagepip install aleph-alpha-client

    # create a new token: https://docs.aleph-alpha.com/docs/account/#create-a-new-tokenfrom getpass import getpassALEPH_ALPHA_API_KEY = getpass()

         ········

    from langchain.llms import AlephAlphafrom langchain import PromptTemplate, LLMChain

    template = """Q: {question}A:"""prompt = PromptTemplate(template=template, input_variables=["question"])

    llm = AlephAlpha(    model="luminous-extended",    maximum_tokens=20,    stop_sequences=["Q:"],    aleph_alpha_api_key=ALEPH_ALPHA_API_KEY,)

    llm_chain = LLMChain(prompt=prompt, llm=llm)

    question = "What is AI?"llm_chain.run(question)

        ' Artificial Intelligence (AI) is the simulation of human intelligence processes by machines, especially computer systems.\n'