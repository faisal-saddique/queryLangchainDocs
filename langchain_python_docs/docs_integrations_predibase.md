Predibase
=========

Learn how to use LangChain with models on Predibase.

Setup[​](#setup "Direct link to Setup")
---------------------------------------

*   Create a [Predibase](hhttps://predibase.com/) account and [API key](https://docs.predibase.com/sdk-guide/intro).
*   Install the Predibase Python client with `pip install predibase`
*   Use your API key to authenticate

### LLM[​](#llm "Direct link to LLM")

Predibase integrates with LangChain by implementing LLM module. You can see a short example below or a full notebook under LLM > Integrations > Predibase.

    import osos.environ["PREDIBASE_API_TOKEN"] = "{PREDIBASE_API_TOKEN}"from langchain.llms import Predibasemodel =  Predibase(model = 'vicuna-13b', predibase_api_key=os.environ.get('PREDIBASE_API_TOKEN'))response = model("Can you recommend me a nice dry wine?")print(response)