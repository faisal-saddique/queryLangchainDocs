Predibase
=========

[Predibase](https://predibase.com/) allows you to train, finetune, and deploy any ML model—from linear regression to large language model.

This example demonstrates using Langchain with models deployed on Predibase

Setup
=====

To run this notebook, you'll need a [Predibase account](https://predibase.com/free-trial/?utm_source=langchain) and an [API key](https://docs.predibase.com/sdk-guide/intro).

You'll also need to install the Predibase Python package:

    pip install predibaseimport osos.environ["PREDIBASE_API_TOKEN"] = "{PREDIBASE_API_TOKEN}"

Initial Call[​](#initial-call "Direct link to Initial Call")
------------------------------------------------------------

    from langchain.llms import Predibasemodel = Predibase(    model="vicuna-13b", predibase_api_key=os.environ.get("PREDIBASE_API_TOKEN"))

    response = model("Can you recommend me a nice dry wine?")print(response)

Chain Call Setup[​](#chain-call-setup "Direct link to Chain Call Setup")
------------------------------------------------------------------------

    llm = Predibase(    model="vicuna-13b", predibase_api_key=os.environ.get("PREDIBASE_API_TOKEN"))

SequentialChain[​](#sequentialchain "Direct link to SequentialChain")
---------------------------------------------------------------------

    from langchain.chains import LLMChainfrom langchain.prompts import PromptTemplate

    # This is an LLMChain to write a synopsis given a title of a play.template = """You are a playwright. Given the title of play, it is your job to write a synopsis for that title.Title: {title}Playwright: This is a synopsis for the above play:"""prompt_template = PromptTemplate(input_variables=["title"], template=template)synopsis_chain = LLMChain(llm=llm, prompt=prompt_template)

    # This is an LLMChain to write a review of a play given a synopsis.template = """You are a play critic from the New York Times. Given the synopsis of play, it is your job to write a review for that play.Play Synopsis:{synopsis}Review from a New York Times play critic of the above play:"""prompt_template = PromptTemplate(input_variables=["synopsis"], template=template)review_chain = LLMChain(llm=llm, prompt=prompt_template)

    # This is the overall chain where we run these two chains in sequence.from langchain.chains import SimpleSequentialChainoverall_chain = SimpleSequentialChain(    chains=[synopsis_chain, review_chain], verbose=True)

    review = overall_chain.run("Tragedy at sunset on the beach")

Fine-tuned LLM (Use your own fine-tuned LLM from Predibase)[​](#fine-tuned-llm-use-your-own-fine-tuned-llm-from-predibase "Direct link to Fine-tuned LLM (Use your own fine-tuned LLM from Predibase)")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    from langchain.llms import Predibasemodel = Predibase(    model="my-finetuned-LLM", predibase_api_key=os.environ.get("PREDIBASE_API_TOKEN"))# replace my-finetuned-LLM with the name of your model in Predibase

    # response = model("Can you help categorize the following emails into positive, negative, and neutral?")