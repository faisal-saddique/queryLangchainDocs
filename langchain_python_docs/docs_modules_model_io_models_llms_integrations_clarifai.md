Clarifai
========

> [Clarifai](https://www.clarifai.com/) is an AI Platform that provides the full AI lifecycle ranging from data exploration, data labeling, model training, evaluation, and inference.

This example goes over how to use LangChain to interact with `Clarifai` [models](https://clarifai.com/explore/models).

To use Clarifai, you must have an account and a Personal Access Token (PAT) key. [Check here](https://clarifai.com/settings/security) to get or create a PAT.

Dependencies
============

    # Install required dependenciespip install clarifai

Imports
=======

Here we will be setting the personal access token. You can find your PAT under [settings/security](https://clarifai.com/settings/security) in your Clarifai account.

    # Please login and get your API key from  https://clarifai.com/settings/securityfrom getpass import getpassCLARIFAI_PAT = getpass()

         ········

    # Import the required modulesfrom langchain.llms import Clarifaifrom langchain import PromptTemplate, LLMChain

Input
=====

Create a prompt template to be used with the LLM Chain:

    template = """Question: {question}Answer: Let's think step by step."""prompt = PromptTemplate(template=template, input_variables=["question"])

Setup
=====

Setup the user id and app id where the model resides. You can find a list of public models on [https://clarifai.com/explore/models](https://clarifai.com/explore/models)

You will have to also initialize the model id and if needed, the model version id. Some models have many versions, you can choose the one appropriate for your task.

    USER_ID = "openai"APP_ID = "chat-completion"MODEL_ID = "GPT-3_5-turbo"# You can provide a specific model version as the model_version_id arg.# MODEL_VERSION_ID = "MODEL_VERSION_ID"

    # Initialize a Clarifai LLMclarifai_llm = Clarifai(    pat=CLARIFAI_PAT, user_id=USER_ID, app_id=APP_ID, model_id=MODEL_ID)

    # Create LLM chainllm_chain = LLMChain(prompt=prompt, llm=clarifai_llm)

Run Chain
=========

    question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"llm_chain.run(question)

        'Justin Bieber was born on March 1, 1994. So, we need to figure out the Super Bowl winner for the 1994 season. The NFL season spans two calendar years, so the Super Bowl for the 1994 season would have taken place in early 1995. \n\nThe Super Bowl in question is Super Bowl XXIX, which was played on January 29, 1995. The game was won by the San Francisco 49ers, who defeated the San Diego Chargers by a score of 49-26. Therefore, the San Francisco 49ers won the Super Bowl in the year Justin Bieber was born.'