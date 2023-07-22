OpenAI
======

> [OpenAI](https://en.wikipedia.org/wiki/OpenAI) is American artificial intelligence (AI) research laboratory consisting of the non-profit `OpenAI Incorporated` and its for-profit subsidiary corporation `OpenAI Limited Partnership`. `OpenAI` conducts AI research with the declared intention of promoting and developing a friendly AI. `OpenAI` systems run on an `Azure`\-based supercomputing platform from `Microsoft`.

> The [OpenAI API](https://platform.openai.com/docs/models) is powered by a diverse set of models with different capabilities and price points.
> 
> [ChatGPT](https://chat.openai.com) is the Artificial Intelligence (AI) chatbot developed by `OpenAI`.

Installation and Setup[​](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

*   Install the Python SDK with

    pip install openai

*   Get an OpenAI api key and set it as an environment variable (`OPENAI_API_KEY`)
*   If you want to use OpenAI's tokenizer (only available for Python 3.9+), install it

    pip install tiktoken

LLM[​](#llm "Direct link to LLM")
---------------------------------

    from langchain.llms import OpenAI

If you are using a model hosted on `Azure`, you should use different wrapper for that:

    from langchain.llms import AzureOpenAI

For a more detailed walkthrough of the `Azure` wrapper, see [this notebook](/docs/modules/model_io/models/llms/integrations/azure_openai_example.html)

Text Embedding Model[​](#text-embedding-model "Direct link to Text Embedding Model")
------------------------------------------------------------------------------------

    from langchain.embeddings import OpenAIEmbeddings

For a more detailed walkthrough of this, see [this notebook](/docs/modules/data_connection/text_embedding/integrations/openai.html)

Tokenizer[​](#tokenizer "Direct link to Tokenizer")
---------------------------------------------------

There are several places you can use the `tiktoken` tokenizer. By default, it is used to count tokens for OpenAI LLMs.

You can also use it to count tokens when splitting documents with

    from langchain.text_splitter import CharacterTextSplitterCharacterTextSplitter.from_tiktoken_encoder(...)

For a more detailed walkthrough of this, see [this notebook](/docs/modules/data_connection/document_transformers/text_splitters/tiktoken.html)

Chain[​](#chain "Direct link to Chain")
---------------------------------------

See a [usage example](/docs/modules/chains/additional/moderation.html).

    from langchain.chains import OpenAIModerationChain

Document Loader[​](#document-loader "Direct link to Document Loader")
---------------------------------------------------------------------

See a [usage example](/docs/modules/data_connection/document_loaders/integrations/chatgpt_loader.html).

    from langchain.document_loaders.chatgpt import ChatGPTLoader

Retriever[​](#retriever "Direct link to Retriever")
---------------------------------------------------

See a [usage example](/docs/modules/data_connection/retrievers/integrations/chatgpt-plugin.html).

    from langchain.retrievers import ChatGPTPluginRetriever