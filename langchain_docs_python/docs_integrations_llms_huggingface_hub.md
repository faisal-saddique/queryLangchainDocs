Hugging Face Hub
================

> The [Hugging Face Hub](https://huggingface.co/docs/hub/index) is a platform with over 120k models, 20k datasets, and 50k demo apps (Spaces), all open source and publicly available, in an online platform where people can easily collaborate and build ML together.

This example showcases how to connect to the `Hugging Face Hub` and use different models.

Installation and Setup[](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

To use, you should have the `huggingface_hub` python [package installed](https://huggingface.co/docs/huggingface_hub/installation).

    pip install huggingface_hub

    # get a token: https://huggingface.co/docs/api-inference/quicktour#get-your-api-tokenfrom getpass import getpassHUGGINGFACEHUB_API_TOKEN = getpass()

         ········

    import osos.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN

Prepare Examples[](#prepare-examples "Direct link to Prepare Examples")
------------------------------------------------------------------------

    from langchain import HuggingFaceHub

    from langchain import PromptTemplate, LLMChain

    question = "Who won the FIFA World Cup in the year 1994? "template = """Question: {question}Answer: Let's think step by step."""prompt = PromptTemplate(template=template, input_variables=["question"])

Examples[](#examples "Direct link to Examples")
------------------------------------------------

Below are some examples of models you can access through the `Hugging Face Hub` integration.

### Flan, by Google[](#flan-by-google "Direct link to Flan, by Google")

    repo_id = "google/flan-t5-xxl"  # See https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads for some other options

    llm = HuggingFaceHub(    repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 64})llm_chain = LLMChain(prompt=prompt, llm=llm)print(llm_chain.run(question))

        The FIFA World Cup was held in the year 1994. West Germany won the FIFA World Cup in 1994

### Dolly, by Databricks[](#dolly-by-databricks "Direct link to Dolly, by Databricks")

See [Databricks](https://huggingface.co/databricks) organization page for a list of available models.

    repo_id = "databricks/dolly-v2-3b"

    llm = HuggingFaceHub(    repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 64})llm_chain = LLMChain(prompt=prompt, llm=llm)print(llm_chain.run(question))

         First of all, the world cup was won by the Germany. Then the Argentina won the world cup in 2022. So, the Argentina won the world cup in 1994.            Question: Who

### Camel, by Writer[](#camel-by-writer "Direct link to Camel, by Writer")

See [Writer's](https://huggingface.co/Writer) organization page for a list of available models.

    repo_id = "Writer/camel-5b-hf"  # See https://huggingface.co/Writer for other options

    llm = HuggingFaceHub(    repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 64})llm_chain = LLMChain(prompt=prompt, llm=llm)print(llm_chain.run(question))

### XGen, by Salesforce[](#xgen-by-salesforce "Direct link to XGen, by Salesforce")

See [more information](https://github.com/salesforce/xgen).

    repo_id = "Salesforce/xgen-7b-8k-base"

    llm = HuggingFaceHub(    repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 64})llm_chain = LLMChain(prompt=prompt, llm=llm)print(llm_chain.run(question))

### Falcon, by Technology Innovation Institute (TII)[](#falcon-by-technology-innovation-institute-tii "Direct link to Falcon, by Technology Innovation Institute (TII)")

See [more information](https://huggingface.co/tiiuae/falcon-40b).

    repo_id = "tiiuae/falcon-40b"

    llm = HuggingFaceHub(    repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 64})llm_chain = LLMChain(prompt=prompt, llm=llm)print(llm_chain.run(question))