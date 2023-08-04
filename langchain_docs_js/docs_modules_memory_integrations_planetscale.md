PlanetScale Chat Memory
=======================

Because PlanetScale works via a REST API, you can use this with [Vercel Edge](https://vercel.com/docs/concepts/functions/edge-functions/edge-runtime), [Cloudflare Workers](https://developers.cloudflare.com/workers/) and other Serverless environments.

For longer-term persistence across chat sessions, you can swap out the default in-memory `chatHistory` that backs chat memory classes like `BufferMemory` for an PlanetScale [Database](https://planetscale.com/) instance.

Setup[](#setup "Direct link to Setup")
---------------------------------------

You will need to install [@planetscale/database](https://github.com/planetscale/database-js) in your project:

*   npm
*   Yarn
*   pnpm

    npm install @planetscale/database

    yarn add @planetscale/database

    pnpm add @planetscale/database

You will also need an PlanetScale Account and a database to connect to. See instructions on [PlanetScale Docs](https://planetscale.com/docs) on how to create a HTTP client.

Usage[](#usage "Direct link to Usage")
---------------------------------------

Each chat history session stored in PlanetScale database must have a unique id. The `config` parameter is passed directly into the `new Client()` constructor of [@planetscale/database](https://planetscale.com/docs/tutorials/planetscale-serverless-driver), and takes all the same arguments.

    import { BufferMemory } from "langchain/memory";import { PlanetScaleChatMessageHistory } from "langchain/stores/message/planetscale";import { ChatOpenAI } from "langchain/chat_models/openai";import { ConversationChain } from "langchain/chains";const memory = new BufferMemory({  chatHistory: new PlanetScaleChatMessageHistory({    tableName: "stored_message",    sessionId: "lc-example",    config: {      url: "ADD_YOURS_HERE", // Override with your own database instance's URL    },  }),});const model = new ChatOpenAI();const chain = new ConversationChain({ llm: model, memory });const res1 = await chain.call({ input: "Hi! I'm Jim." });console.log({ res1 });/*{  res1: {    text: "Hello Jim! It's nice to meet you. My name is AI. How may I assist you today?"  }}*/const res2 = await chain.call({ input: "What did I just say my name was?" });console.log({ res2 });/*{  res1: {    text: "You said your name was Jim."  }}*/

#### API Reference:

*   [BufferMemory](/docs/api/memory/classes/BufferMemory) from `langchain/memory`
*   [PlanetScaleChatMessageHistory](/docs/api/stores_message_planetscale/classes/PlanetScaleChatMessageHistory) from `langchain/stores/message/planetscale`
*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [ConversationChain](/docs/api/chains/classes/ConversationChain) from `langchain/chains`

Advanced Usage[](#advanced-usage "Direct link to Advanced Usage")
------------------------------------------------------------------

You can also directly pass in a previously created [@planetscale/database](https://planetscale.com/docs/tutorials/planetscale-serverless-driver) client instance:

    import { BufferMemory } from "langchain/memory";import { PlanetScaleChatMessageHistory } from "langchain/stores/message/planetscale";import { ChatOpenAI } from "langchain/chat_models/openai";import { ConversationChain } from "langchain/chains";import { Client } from "@planetscale/database";// Create your own Planetscale database clientconst client = new Client({  url: "ADD_YOURS_HERE", // Override with your own database instance's URL});const memory = new BufferMemory({  chatHistory: new PlanetScaleChatMessageHistory({    tableName: "stored_message",    sessionId: "lc-example",    client, // You can reuse your existing database client  }),});const model = new ChatOpenAI();const chain = new ConversationChain({ llm: model, memory });const res1 = await chain.call({ input: "Hi! I'm Jim." });console.log({ res1 });/*{  res1: {    text: "Hello Jim! It's nice to meet you. My name is AI. How may I assist you today?"  }}*/const res2 = await chain.call({ input: "What did I just say my name was?" });console.log({ res2 });/*{  res1: {    text: "You said your name was Jim."  }}*/

#### API Reference:

*   [BufferMemory](/docs/api/memory/classes/BufferMemory) from `langchain/memory`
*   [PlanetScaleChatMessageHistory](/docs/api/stores_message_planetscale/classes/PlanetScaleChatMessageHistory) from `langchain/stores/message/planetscale`
*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [ConversationChain](/docs/api/chains/classes/ConversationChain) from `langchain/chains`