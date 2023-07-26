TextGen
=======

[GitHub:oobabooga/text-generation-webui](https://github.com/oobabooga/text-generation-webui) A gradio web UI for running Large Language Models like LLaMA, llama.cpp, GPT-J, Pythia, OPT, and GALACTICA.

This example goes over how to use LangChain to interact with LLM models via the `text-generation-webui` API integration.

Please ensure that you have `text-generation-webui` configured and an LLM installed. Recommended installation via the [one-click installer appropriate](https://github.com/oobabooga/text-generation-webui#one-click-installers) for your OS.

Once `text-generation-webui` is installed and confirmed working via the web interface, please enable the `api` option either through the web model configuration tab, or by adding the run-time arg `--api` to your start command.

Set model\_url and run the example[](#set-model_url-and-run-the-example "Direct link to Set model_url and run the example")
----------------------------------------------------------------------------------------------------------------------------

    model_url = "http://localhost:5000"

    import langchainfrom langchain import PromptTemplate, LLMChainfrom langchain.llms import TextGenlangchain.debug = Truetemplate = """Question: {question}Answer: Let's think step by step."""prompt = PromptTemplate(template=template, input_variables=["question"])llm = TextGen(model_url=model_url)llm_chain = LLMChain(prompt=prompt, llm=llm)question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"llm_chain.run(question)