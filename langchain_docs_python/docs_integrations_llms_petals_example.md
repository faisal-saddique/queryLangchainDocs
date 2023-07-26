Petals
======

`Petals` runs 100B+ language models at home, BitTorrent-style.

This notebook goes over how to use Langchain with [Petals](https://github.com/bigscience-workshop/petals).

Install petals[](#install-petals "Direct link to Install petals")
------------------------------------------------------------------

The `petals` package is required to use the Petals API. Install `petals` using `pip3 install petals`.

    pip3 install petals

Imports[](#imports "Direct link to Imports")
---------------------------------------------

    import osfrom langchain.llms import Petalsfrom langchain import PromptTemplate, LLMChain

Set the Environment API Key[](#set-the-environment-api-key "Direct link to Set the Environment API Key")
---------------------------------------------------------------------------------------------------------

Make sure to get [your API key](https://huggingface.co/docs/api-inference/quicktour#get-your-api-token) from Huggingface.

    from getpass import getpassHUGGINGFACE_API_KEY = getpass()

         ········

    os.environ["HUGGINGFACE_API_KEY"] = HUGGINGFACE_API_KEY

Create the Petals instance[](#create-the-petals-instance "Direct link to Create the Petals instance")
------------------------------------------------------------------------------------------------------

You can specify different parameters such as the model name, max new tokens, temperature, etc.

    # this can take several minutes to download big files!llm = Petals(model_name="bigscience/bloom-petals")

        Downloading:   1%|▏                        | 40.8M/7.19G [00:24<15:44, 7.57MB/s]

Create a Prompt Template[](#create-a-prompt-template "Direct link to Create a Prompt Template")
------------------------------------------------------------------------------------------------

We will create a prompt template for Question and Answer.

    template = """Question: {question}Answer: Let's think step by step."""prompt = PromptTemplate(template=template, input_variables=["question"])

Initiate the LLMChain[](#initiate-the-llmchain "Direct link to Initiate the LLMChain")
---------------------------------------------------------------------------------------

    llm_chain = LLMChain(prompt=prompt, llm=llm)

Run the LLMChain[](#run-the-llmchain "Direct link to Run the LLMChain")
------------------------------------------------------------------------

Provide a question and run the LLMChain.

    question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"llm_chain.run(question)