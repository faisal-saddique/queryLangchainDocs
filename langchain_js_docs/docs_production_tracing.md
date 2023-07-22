LangSmith
=========

Introduction[​](#introduction "Direct link to Introduction")
------------------------------------------------------------

**LangSmith** is a platform for building production-grade LLM applications.

It lets you debug, test, evaluate, and monitor chains and intelligent agents built on **any LLM framework** and seamlessly integrates with **LangChain**, the go-to open source framework for building with LLMs.

LangSmith is developed by LangChain, the company behind the open source LangChain framework.

Active Development

LangSmith is an early product in beta. We may need to periodically gate new signups to ensure a smooth experience for our users. If you run into any urgent issues or bugs, please reach out to us at [](mailto:support@langchain.dev)[support@langchain.dev](mailto:support@langchain.dev).

We appreciate your patience.

Interactive Tutorial

If following along with code is more your thing, we've set up this [Jupyter notebook](https://github.com/hwchase17/langchain/blob/master/docs/extras/guides/langsmith/walkthrough.ipynb) to help you get started with LangSmith.

Quick Start[​](#quick-start "Direct link to Quick Start")
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

    import { ChatOpenAI } from "langchain/chat_models/openai";const llm = new ChatOpenAI()await llm.call("Hello, world!");

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

5.  Configure runtime environment.

*   Shell

    export LANGCHAIN_TRACING_V2=trueexport LANGCHAIN_ENDPOINT=https://api.smith.langchain.comexport LANGCHAIN_API_KEY=<your-api-key>export LANGCHAIN_PROJECT=<your-project>  # if not specified, defaults to "default"

7.  Run the example code below, making sure to replace `"<your-api-key>"` with the API key generated in step 1. So long as the environment is correctly configured, all your LangChain code will be traced.

*   Python
*   Typescript

    from langsmith.run_trees import RunTreeparent_run = RunTree(    name="My Chat Bot",    run_type="chain",    inputs={"text": "Summarize this morning's meetings."},    serialized={})child_llm_run = parent_run.create_child(    name="My Proprietary LLM",    run_type="llm",    inputs={        "prompts": [            "You are an AI Assistant. Summarize this morning's meetings."        ]    },)child_llm_run.end(outputs={"generations": ["Summary of the meeting..."]})parent_run.end(outputs={"output": ["The meeting notes are as follows:..."]})res = parent_run.post(exclude_child_runs=False)res.result()

    import { RunTree, RunTreeConfig } from "langsmith";const parentRunConfig: RunTreeConfig = {    name: "My Chat Bot",    run_type: "chain",    inputs: {        text: "Summarize this morning's meetings.",    },    serialized: {}};const parentRun = new RunTree(parentRunConfig);const childLlmRun = await parentRun.createChild({    name: "My Proprietary LLM",    run_type: "llm",    inputs: {        prompts: [        "You are an AI Assistant. Summarize this morning's meetings.",        ],    },});await childLlmRun.end({outputs: {    generations: [    "Summary of the meeting...",    ],},});await parentRun.end({outputs: {    output: ["The meeting notes are as follows:..."],},});await parentRun.postRun({ exclude_child_runs: false });          

Congratulations! Your first run is now visible in LangSmith! Navigate to the [projects page](https://smith.langchain.com/projects) to view your "Hello, world!" trace.

Next Steps[​](#next-steps "Direct link to Next Steps")
------------------------------------------------------

Read the [LangSmith Overview](/overview) to learn more about what LangSmith has to offer.

To learn how to best take advantage of the visualization and replay capabilities within LangSmith, check out the [tracing documentation](/tracing).

To start testing and evaluating your LLMs, chains, and agents, check out the [testing & evaluation quickstart](/evaluation/quickstart) and related documentation.

Additional Resources[​](#additional-resources "Direct link to Additional Resources")
------------------------------------------------------------------------------------

*   [LangChain Python](https://python.langchain.com/en/latest/) Docs for the Python LangChain library.
    
*   [LangChain Python API Reference](https://api.python.langchain.com/en/latest/) documentation to review the core APIs of LangChain.
    
*   [LangChain JS](https://js.langchain.com/docs/) Docs for the TypeScript LangChain library
    
*   [Discord](https://discord.gg/6adMQxSpJS): Join us on our Discord to discuss all things LangChain!
    

Production Support

If you are a company building with LangChain in production, we'd love to hear from you. Drop us a line at [](mailto:support@langchain.dev)[support@langchain.dev](mailto:support@langchain.dev) and we'll set up a dedicated support Slack channel.