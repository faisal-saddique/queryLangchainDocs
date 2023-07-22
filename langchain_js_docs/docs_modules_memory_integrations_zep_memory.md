Zep Memory
==========

[Zep](https://github.com/getzep/zep) is a memory server that stores, summarizes, embeds, indexes, and enriches conversational AI chat histories, autonomous agent histories, document Q&A histories and exposes them via simple, low-latency APIs.

Key Features:

*   Long-term memory persistence, with access to historical messages irrespective of your summarization strategy.
*   Auto-summarization of memory messages based on a configurable message window. A series of summaries are stored, providing flexibility for future summarization strategies.
*   Vector search over memories, with messages automatically embedded on creation.
*   Auto-token counting of memories and summaries, allowing finer-grained control over prompt assembly.
*   [Python](https://github.com/getzep/zep-python) and [JavaScript](https://github.com/getzep/zep-js) SDKs.

Setup[​](#setup "Direct link to Setup")
---------------------------------------

See the instructions from [Zep](https://github.com/getzep/zep) for running the server locally or through an automated hosting provider.

Usage[​](#usage "Direct link to Usage")
---------------------------------------

    import { ChatOpenAI } from "langchain/chat_models/openai";import { ConversationChain } from "langchain/chains";import { ZepMemory } from "langchain/memory/zep";const sessionId = "TestSession";const zepURL = "http://localhost:8000";const memory = new ZepMemory({  sessionId,  baseURL: zepURL,  // This is optional. If you've enabled JWT authentication on your Zep server, you can  // pass it in here. See https://docs.getzep.com/deployment/auth  apiKey: "change_this_key",});const model = new ChatOpenAI({  modelName: "gpt-3.5-turbo",  temperature: 0,});const chain = new ConversationChain({ llm: model, memory });console.log("Memory Keys:", memory.memoryKeys);const res1 = await chain.call({ input: "Hi! I'm Jim." });console.log({ res1 });/*{  res1: {    text: "Hello Jim! It's nice to meet you. My name is AI. How may I assist you today?"  }}*/const res2 = await chain.call({ input: "What did I just say my name was?" });console.log({ res2 });/*{  res1: {    text: "You said your name was Jim."  }}*/console.log("Session ID: ", sessionId);console.log("Memory: ", await memory.loadMemoryVariables({}));

#### API Reference:

*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [ConversationChain](/docs/api/chains/classes/ConversationChain) from `langchain/chains`
*   [ZepMemory](/docs/api/memory_zep/classes/ZepMemory) from `langchain/memory/zep`