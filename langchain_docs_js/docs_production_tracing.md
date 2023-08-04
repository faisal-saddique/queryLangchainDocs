LangSmith
=========

Introduction[](#introduction "Direct link to Introduction")
------------------------------------------------------------

**LangSmith** is a platform for building production-grade LLM applications.

It lets you debug, test, evaluate, and monitor chains and intelligent agents built on **any LLM framework** and seamlessly integrates with **LangChain**, the go-to open source framework for building with LLMs.

LangSmith is developed by LangChain, the company behind the open source LangChain framework.

Active Development

LangSmith is an early product in beta. We may need to periodically gate new signups to ensure a smooth experience for our users. If you run into any urgent issues or bugs, please reach out to us at [](mailto:support@langchain.dev)[support@langchain.dev](mailto:support@langchain.dev).

We appreciate your patience.

Interactive Tutorial

If following along with code is more your thing, we've set up this [Jupyter notebook](https://github.com/langchain-ai/langchain/blob/master/docs/extras/guides/langsmith/walkthrough.ipynb) to help you get started with LangSmith.

Quick Start[](#quick-start "Direct link to Quick Start")
---------------------------------------------------------

*   LangChain
*   Without LangChain

If you already use LangChain, you can connect to LangSmith in a few steps:

1.  Create a [LangSmith account](https://smith.langchain.com/) using one of the supported login methods.
2.  Create an API Key by navigating to the [settings page](https://smith.langchain.com/settings).
3.  Install the latest version `LangChain` for your target environment and programming language.

*   pip
*   yarn
*   npm
*   pnpm

    pip install -U langchain

    yarn add langchain

    npm install -S langchain

    pnpm add langchain

5.  Configure runtime environment; replace `"<your-api-key>"` with the API key generated in step 1.

*   Shell

    export LANGCHAIN_TRACING_V2=trueexport LANGCHAIN_ENDPOINT=https://api.smith.langchain.comexport LANGCHAIN_API_KEY=<your-api-key>export LANGCHAIN_PROJECT=<your-project>  # if not specified, defaults to "default"

7.  Run the example code below.

*   Python
*   Typescript

    from langchain.chat_models import ChatOpenAIllm = ChatOpenAI()llm.predict("Hello, world!")

    import { ChatOpenAI } from "langchain/chat_models/openai";const llm = new ChatOpenAI()await llm.predict("Hello, world!");/** * For environments where process.env is not defined, * initialize by explicitly passing keys: */import { Client } from "langsmith";import { LangChainTracer } from "langchain/callbacks";const client = new Client({  apiUrl: "https://api.smith.langchain.com",  apiKey: "YOUR_API_KEY"});const tracer = new LangChainTracer({  projectName: "YOUR_PROJECT_NAME",  client});const model = new ChatOpenAI({  openAIApiKey: "YOUR_OPENAI_API_KEY",  callbacks: [tracer]});

If you don't want to use LangChain in your LLM application, you can get started with LangSmith in just a few steps:

1.  Create a [LangSmith account](https://smith.langchain.com/) using one of the supported login methods.
2.  Create an API Key by navigating to the [settings page](https://smith.langchain.com/settings).
3.  Install the LangSmith SDK for your target environment.

*   pip
*   yarn
*   npm
*   pnpm

    pip install -U langsmith

    yarn add langsmith

    npm install -S langsmith

    pnpm add langsmith

5.  Configure runtime environment; replace `"<your-api-key>"` with the API key generated in step 1.

*   Shell

    export LANGCHAIN_TRACING_V2=trueexport LANGCHAIN_ENDPOINT=https://api.smith.langchain.comexport LANGCHAIN_API_KEY=<your-api-key>export LANGCHAIN_PROJECT=<your-project>  # if not specified, defaults to "default"

7.  Run the example code below. So long as the environment is correctly configured, all your LangChain code will be traced.

*   Python
*   Python (experimental)
*   Typescript

    from langsmith.run_trees import RunTreeparent_run = RunTree(    name="My Chat Bot",    run_type="chain",    inputs={"text": "Summarize this morning's meetings."},    serialized={})child_llm_run = parent_run.create_child(    name="My Proprietary LLM",    run_type="llm",    inputs={        "prompts": [            "You are an AI Assistant. Summarize this morning's meetings."        ]    },)child_llm_run.end(outputs={"generations": ["Summary of the meeting..."]})parent_run.end(outputs={"output": ["The meeting notes are as follows:..."]})res = parent_run.post(exclude_child_runs=False)res.result()

    import datetimefrom typing import Anyimport openaifrom langsmith.run_helpers import traceable@traceable(run_type="llm")def my_llm(prompt: str, temperature: float = 0.0, **kwargs: Any) -> str:  messages = [      {          "role": "system",          "content": "You are an AI Assistant. The time is "          + str(datetime.datetime.now()),      },      {"role": "user", "content": prompt},  ]  return (      openai.ChatCompletion.create(          model="gpt-3.5-turbo", messages=messages, temperature=temperature, **kwargs      )      .choices[0]      .message.content  )@traceable(run_type="tool")def my_tool(tool_input: str) -> str:  return tool_input.upper()@traceable(run_type="chain")def my_chat_bot(text: str) -> str:  generated = my_llm(text, temperature=0.0)  if "meeting" in generated:    return my_tool(generated)  else:    return generatedmy_chat_bot("Summarize this morning's meetings.")# See an example run at: https://smith.langchain.com/public/b5e2666d-f570-4b83-a611-86a2503ed91b/r

    import { RunTree, RunTreeConfig } from "langsmith";const parentRunConfig: RunTreeConfig = {    name: "My Chat Bot",    run_type: "chain",    inputs: {        text: "Summarize this morning's meetings.",    },    serialized: {}};const parentRun = new RunTree(parentRunConfig);const childLlmRun = await parentRun.createChild({    name: "My Proprietary LLM",    run_type: "llm",    inputs: {        prompts: [        "You are an AI Assistant. Summarize this morning's meetings.",        ],    },});await childLlmRun.end({outputs: {    generations: [    "Summary of the meeting...",    ],},});await parentRun.end({outputs: {    output: ["The meeting notes are as follows:..."],},});// False means post all nested runs as a batch// (don't exclude child runs)await parentRun.postRun(false);  

Congratulations! Your first run is now visible in LangSmith! Navigate to the [projects page](https://smith.langchain.com/projects) to view your "Hello, world!" trace.

Next Steps[](#next-steps "Direct link to Next Steps")
------------------------------------------------------

Read the [LangSmith Overview](/overview) to learn more about what LangSmith has to offer.

To learn how to best take advantage of the visualization and replay capabilities within LangSmith, check out the [tracing documentation](/tracing).

To start testing and evaluating your LLMs, chains, and agents, check out the [testing & evaluation quickstart](/evaluation/quickstart) and related documentation.

Additional Resources[](#additional-resources "Direct link to Additional Resources")
------------------------------------------------------------------------------------

*   [LangChain Python](https://python.langchain.com/en/latest/) Docs for the Python LangChain library.
    
*   [LangChain Python API Reference](https://api.python.langchain.com/en/latest/) documentation to review the core APIs of LangChain.
    
*   [LangChain JS](https://js.langchain.com/docs/) Docs for the TypeScript LangChain library
    
*   [Discord](https://discord.gg/6adMQxSpJS): Join us on our Discord to discuss all things LangChain!
    

Production Support

If you are a company building with LangChain in production, we'd love to hear from you. Drop us a line at [](mailto:support@langchain.dev)[support@langchain.dev](mailto:support@langchain.dev) and we'll set up a dedicated support Slack channel.