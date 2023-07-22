CerebriumAI
===========

`Cerebrium` is an AWS Sagemaker alternative. It also provides API access to [several LLM models](https://docs.cerebrium.ai/cerebrium/prebuilt-models/deployment).

This notebook goes over how to use Langchain with [CerebriumAI](https://docs.cerebrium.ai/introduction).

Install cerebrium[​](#install-cerebrium "Direct link to Install cerebrium")
---------------------------------------------------------------------------

The `cerebrium` package is required to use the `CerebriumAI` API. Install `cerebrium` using `pip3 install cerebrium`.

    # Install the packagepip3 install cerebrium

Imports[​](#imports "Direct link to Imports")
---------------------------------------------

    import osfrom langchain.llms import CerebriumAIfrom langchain import PromptTemplate, LLMChain

Set the Environment API Key[​](#set-the-environment-api-key "Direct link to Set the Environment API Key")
---------------------------------------------------------------------------------------------------------

Make sure to get your API key from CerebriumAI. See [here](https://dashboard.cerebrium.ai/login). You are given a 1 hour free of serverless GPU compute to test different models.

    os.environ["CEREBRIUMAI_API_KEY"] = "YOUR_KEY_HERE"

Create the CerebriumAI instance[​](#create-the-cerebriumai-instance "Direct link to Create the CerebriumAI instance")
---------------------------------------------------------------------------------------------------------------------

You can specify different parameters such as the model endpoint url, max length, temperature, etc. You must provide an endpoint url.

    llm = CerebriumAI(endpoint_url="YOUR ENDPOINT URL HERE")

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