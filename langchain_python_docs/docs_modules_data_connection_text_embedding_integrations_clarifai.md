Clarifai
========

> [Clarifai](https://www.clarifai.com/) is an AI Platform that provides the full AI lifecycle ranging from data exploration, data labeling, model training, evaluation, and inference.

This example goes over how to use LangChain to interact with `Clarifai` [models](https://clarifai.com/explore/models). Text embedding models in particular can be found [here](https://clarifai.com/explore/models?page=1&perPage=24&filterData=%5B%7B%22field%22%3A%22model_type_id%22%2C%22value%22%3A%5B%22text-embedder%22%5D%7D%5D).

To use Clarifai, you must have an account and a Personal Access Token (PAT) key. [Check here](https://clarifai.com/settings/security) to get or create a PAT.

Dependencies
============

    # Install required dependenciespip install clarifai

Imports
=======

Here we will be setting the personal access token. You can find your PAT under [settings/security](https://clarifai.com/settings/security) in your Clarifai account.

    # Please login and get your API key from  https://clarifai.com/settings/securityfrom getpass import getpassCLARIFAI_PAT = getpass()

         ········

    # Import the required modulesfrom langchain.embeddings import ClarifaiEmbeddingsfrom langchain import PromptTemplate, LLMChain

Input
=====

Create a prompt template to be used with the LLM Chain:

    template = """Question: {question}Answer: Let's think step by step."""prompt = PromptTemplate(template=template, input_variables=["question"])

Setup
=====

Set the user id and app id to the application in which the model resides. You can find a list of public models on [https://clarifai.com/explore/models](https://clarifai.com/explore/models)

You will have to also initialize the model id and if needed, the model version id. Some models have many versions, you can choose the one appropriate for your task.

    USER_ID = "openai"APP_ID = "embed"MODEL_ID = "text-embedding-ada"# You can provide a specific model version as the model_version_id arg.# MODEL_VERSION_ID = "MODEL_VERSION_ID"

    # Initialize a Clarifai embedding modelembeddings = ClarifaiEmbeddings(    pat=CLARIFAI_PAT, user_id=USER_ID, app_id=APP_ID, model_id=MODEL_ID)

    text = "This is a test document."

    query_result = embeddings.embed_query(text)

    doc_result = embeddings.embed_documents([text])