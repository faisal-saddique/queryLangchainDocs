Motörhead Memory
================

[Motörhead](https://github.com/getmetal/motorhead) is a memory server implemented in Rust. It automatically handles incremental summarization in the background and allows for stateless applications.

Setup[​](#setup "Direct link to Setup")
---------------------------------------

See instructions at [Motörhead](https://github.com/getmetal/motorhead) for running the server locally, or [https://getmetal.io](https://getmetal.io) to get API keys for the hosted version.

Usage[​](#usage "Direct link to Usage")
---------------------------------------

    import { MotorheadMemory } from "langchain/memory";import { ChatOpenAI } from "langchain/chat_models/openai";import { ConversationChain } from "langchain/chains";// Managed Example (visit https://getmetal.io to get your keys)// const managedMemory = new MotorheadMemory({//   memoryKey: "chat_history",//   sessionId: "test",//   apiKey: "MY_API_KEY",//   clientId: "MY_CLIENT_ID",// });// Self Hosted Exampleconst memory = new MotorheadMemory({  memoryKey: "chat_history",  sessionId: "test",  url: "localhost:8080", // Required for self hosted});const model = new ChatOpenAI({  modelName: "gpt-3.5-turbo",  temperature: 0,});const chain = new ConversationChain({ llm: model, memory });const res1 = await chain.call({ input: "Hi! I'm Jim." });console.log({ res1 });/*{  res1: {    text: "Hello Jim! It's nice to meet you. My name is AI. How may I assist you today?"  }}*/const res2 = await chain.call({ input: "What did I just say my name was?" });console.log({ res2 });/*{  res1: {    text: "You said your name was Jim."  }}*/

#### API Reference:

*   [MotorheadMemory](/docs/api/memory/classes/MotorheadMemory) from `langchain/memory`
*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [ConversationChain](/docs/api/chains/classes/ConversationChain) from `langchain/chains`