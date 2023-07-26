GooseAI
=======

This page covers how to use the GooseAI ecosystem within LangChain. It is broken into two parts: installation and setup, and then references to specific GooseAI wrappers.

Installation and Setup[](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

*   Install the Python SDK with `pip install openai`
*   Get your GooseAI api key from this link [here](https://goose.ai/).
*   Set the environment variable (`GOOSEAI_API_KEY`).

    import osos.environ["GOOSEAI_API_KEY"] = "YOUR_API_KEY"

Wrappers[](#wrappers "Direct link to Wrappers")
------------------------------------------------

### LLM[](#llm "Direct link to LLM")

There exists an GooseAI LLM wrapper, which you can access with:

    from langchain.llms import GooseAI