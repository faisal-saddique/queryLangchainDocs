OpenAI
======

[OpenAI](https://platform.openai.com/docs/introduction) offers a spectrum of models with different levels of power suitable for different tasks.

This example goes over how to use LangChain to interact with `OpenAI` [models](https://platform.openai.com/docs/models)

    # get a token: https://platform.openai.com/account/api-keysfrom getpass import getpassOPENAI_API_KEY = getpass()

    import osos.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

Should you need to specify your organization ID, you can use the following cell. However, it is not required if you are only part of a single organization or intend to use your default organization. You can check your default organization [here](https://platform.openai.com/account/api-keys).

To specify your organization, you can use this:

    OPENAI_ORGANIZATION = getpass()os.environ["OPENAI_ORGANIZATION"] = OPENAI_ORGANIZATION

    from langchain.llms import OpenAIfrom langchain import PromptTemplate, LLMChain

    template = """Question: {question}Answer: Let's think step by step."""prompt = PromptTemplate(template=template, input_variables=["question"])

    llm = OpenAI()

If you manually want to specify your OpenAI API key and/or organization ID, you can use the following:

    llm = OpenAI(openai_api_key="YOUR_API_KEY", openai_organization="YOUR_ORGANIZATION_ID")

Remove the openai\_organization parameter should it not apply to you.

    llm_chain = LLMChain(prompt=prompt, llm=llm)

    question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"llm_chain.run(question)

        ' Justin Bieber was born in 1994, so the NFL team that won the Super Bowl in 1994 was the Dallas Cowboys.'

If you are behind an explicit proxy, you can use the OPENAI\_PROXY environment variable to pass through

    os.environ["OPENAI_PROXY"] = "http://proxy.yourcompany.com:8080"