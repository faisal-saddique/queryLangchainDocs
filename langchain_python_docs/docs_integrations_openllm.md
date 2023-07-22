OpenLLM
=======

This page demonstrates how to use [OpenLLM](https://github.com/bentoml/OpenLLM) with LangChain.

`OpenLLM` is an open platform for operating large language models (LLMs) in production. It enables developers to easily run inference with any open-source LLMs, deploy to the cloud or on-premises, and build powerful AI apps.

Installation and Setup[​](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

Install the OpenLLM package via PyPI:

    pip install openllm

LLM[​](#llm "Direct link to LLM")
---------------------------------

OpenLLM supports a wide range of open-source LLMs as well as serving users' own fine-tuned LLMs. Use `openllm model` command to see all available models that are pre-optimized for OpenLLM.

Wrappers[​](#wrappers "Direct link to Wrappers")
------------------------------------------------

There is a OpenLLM Wrapper which supports loading LLM in-process or accessing a remote OpenLLM server:

    from langchain.llms import OpenLLM

### Wrapper for OpenLLM server[​](#wrapper-for-openllm-server "Direct link to Wrapper for OpenLLM server")

This wrapper supports connecting to an OpenLLM server via HTTP or gRPC. The OpenLLM server can run either locally or on the cloud.

To try it out locally, start an OpenLLM server:

    openllm start flan-t5

Wrapper usage:

    from langchain.llms import OpenLLMllm = OpenLLM(server_url='http://localhost:3000')llm("What is the difference between a duck and a goose? And why there are so many Goose in Canada?")

### Wrapper for Local Inference[​](#wrapper-for-local-inference "Direct link to Wrapper for Local Inference")

You can also use the OpenLLM wrapper to load LLM in current Python process for running inference.

    from langchain.llms import OpenLLMllm = OpenLLM(model_name="dolly-v2", model_id='databricks/dolly-v2-7b')llm("What is the difference between a duck and a goose? And why there are so many Goose in Canada?")

### Usage[​](#usage "Direct link to Usage")

For a more detailed walkthrough of the OpenLLM Wrapper, see the [example notebook](/docs/modules/model_io/models/llms/integrations/openllm.html)