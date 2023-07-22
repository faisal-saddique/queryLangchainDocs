Momento-Backed Chat Memory
==========================

For distributed, serverless persistence across chat sessions, you can swap in a [Momento](https://gomomento.com/)\-backed chat message history. Because a Momento cache is instantly available and requires zero infrastructure maintenance, it's a great way to get started with chat history whether building locally or in production.

Setup[​](#setup "Direct link to Setup")
---------------------------------------

You will need to install the [Momento Client Library](https://github.com/momentohq/client-sdk-javascript) in your project:

*   npm
*   Yarn
*   pnpm

    npm install @gomomento/sdk

    yarn add @gomomento/sdk

    pnpm add @gomomento/sdk

You will also need an API key from [Momento](https://gomomento.com/). You can sign up for a free account [here](https://console.gomomento.com/).

Usage[​](#usage "Direct link to Usage")
---------------------------------------

To distinguish one chat history session from another, we need a unique `sessionId`. You may also provide an optional `sessionTtl` to make sessions expire after a given number of seconds.

    import {  CacheClient,  Configurations,  CredentialProvider,} from "@gomomento/sdk";import { BufferMemory } from "langchain/memory";import { ChatOpenAI } from "langchain/chat_models/openai";import { ConversationChain } from "langchain/chains";import { MomentoChatMessageHistory } from "langchain/stores/message/momento";// See https://github.com/momentohq/client-sdk-javascript for connection optionsconst client = new CacheClient({  configuration: Configurations.Laptop.v1(),  credentialProvider: CredentialProvider.fromEnvironmentVariable({    environmentVariableName: "MOMENTO_AUTH_TOKEN",  }),  defaultTtlSeconds: 60 * 60 * 24,});// Create a unique session IDconst sessionId = new Date().toISOString();const cacheName = "langchain";const memory = new BufferMemory({  chatHistory: await MomentoChatMessageHistory.fromProps({    client,    cacheName,    sessionId,    sessionTtl: 300,  }),});console.log(  `cacheName=${cacheName} and sessionId=${sessionId} . This will be used to store the chat history. You can inspect the values at your Momento console at https://console.gomomento.com.`);const model = new ChatOpenAI({  modelName: "gpt-3.5-turbo",  temperature: 0,});const chain = new ConversationChain({ llm: model, memory });const res1 = await chain.call({ input: "Hi! I'm Jim." });console.log({ res1 });/*{  res1: {    text: "Hello Jim! It's nice to meet you. My name is AI. How may I assist you today?"  }}*/const res2 = await chain.call({ input: "What did I just say my name was?" });console.log({ res2 });/*{  res1: {    text: "You said your name was Jim."  }}*/// See the chat history in the Momentoconsole.log(await memory.chatHistory.getMessages());

#### API Reference:

*   [BufferMemory](/docs/api/memory/classes/BufferMemory) from `langchain/memory`
*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [ConversationChain](/docs/api/chains/classes/ConversationChain) from `langchain/chains`
*   [MomentoChatMessageHistory](/docs/api/stores_message_momento/classes/MomentoChatMessageHistory) from `langchain/stores/message/momento`