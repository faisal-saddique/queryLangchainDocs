PipelineAI
==========

PipelineAI allows you to run your ML models at scale in the cloud. It also provides API access to [several LLM models](https://pipeline.ai).

This notebook goes over how to use Langchain with [PipelineAI](https://docs.pipeline.ai/docs).

Install pipeline-ai[​](#install-pipeline-ai "Direct link to Install pipeline-ai")
---------------------------------------------------------------------------------

The `pipeline-ai` library is required to use the `PipelineAI` API, AKA `Pipeline Cloud`. Install `pipeline-ai` using `pip install pipeline-ai`.

    # Install the packagepip install pipeline-ai

Imports[​](#imports "Direct link to Imports")
---------------------------------------------

    import osfrom langchain.llms import PipelineAIfrom langchain import PromptTemplate, LLMChain

Set the Environment API Key[​](#set-the-environment-api-key "Direct link to Set the Environment API Key")
---------------------------------------------------------------------------------------------------------

Make sure to get your API key from PipelineAI. Check out the [cloud quickstart guide](https://docs.pipeline.ai/docs/cloud-quickstart). You'll be given a 30 day free trial with 10 hours of serverless GPU compute to test different models.

    os.environ["PIPELINE_API_KEY"] = "YOUR_API_KEY_HERE"

Create the PipelineAI instance[​](#create-the-pipelineai-instance "Direct link to Create the PipelineAI instance")
------------------------------------------------------------------------------------------------------------------

When instantiating PipelineAI, you need to specify the id or tag of the pipeline you want to use, e.g. `pipeline_key = "public/gpt-j:base"`. You then have the option of passing additional pipeline-specific keyword arguments:

    llm = PipelineAI(pipeline_key="YOUR_PIPELINE_KEY", pipeline_kwargs={...})

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