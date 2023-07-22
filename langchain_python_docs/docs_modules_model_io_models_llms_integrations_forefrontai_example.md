ForefrontAI
===========

The `Forefront` platform gives you the ability to fine-tune and use [open source large language models](https://docs.forefront.ai/forefront/master/models).

This notebook goes over how to use Langchain with [ForefrontAI](https://www.forefront.ai/).

Imports[​](#imports "Direct link to Imports")
---------------------------------------------

    import osfrom langchain.llms import ForefrontAIfrom langchain import PromptTemplate, LLMChain

Set the Environment API Key[​](#set-the-environment-api-key "Direct link to Set the Environment API Key")
---------------------------------------------------------------------------------------------------------

Make sure to get your API key from ForefrontAI. You are given a 5 day free trial to test different models.

    # get a new token: https://docs.forefront.ai/forefront/api-reference/authenticationfrom getpass import getpassFOREFRONTAI_API_KEY = getpass()

    os.environ["FOREFRONTAI_API_KEY"] = FOREFRONTAI_API_KEY

Create the ForefrontAI instance[​](#create-the-forefrontai-instance "Direct link to Create the ForefrontAI instance")
---------------------------------------------------------------------------------------------------------------------

You can specify different parameters such as the model endpoint url, length, temperature, etc. You must provide an endpoint url.

    llm = ForefrontAI(endpoint_url="YOUR ENDPOINT URL HERE")

Create a Prompt Template[​](#create-a-prompt-template "Direct link to Create a Prompt Template")
------------------------------------------------------------------------------------------------

We will create a prompt template for Question and Answer.

    template = """Question: {question}Answer: Let's think step by step."""prompt = PromptTemplate(template=template, input_variables=["question"])

Initiate the LLMChain[​](#initiate-the-llmchain "Direct link to Initiate the LLMChain")
---------------------------------------------------------------------------------------

    llm_chain = LLMChain(prompt=prompt, llm=llm)

Run the LLMChain[​](#run-the-llmchain "Direct link to Run the LLMChain")
------------------------------------------------------------------------

Provide a question and run the LLMChain.

    question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"llm_chain.run(question)