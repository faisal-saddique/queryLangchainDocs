Upstash Redis-Backed Chat Memory
================================

Because Upstash Redis works via a REST API, you can use this with [Vercel Edge](https://vercel.com/docs/concepts/functions/edge-functions/edge-runtime), [Cloudflare Workers](https://developers.cloudflare.com/workers/) and other Serverless environments. Based on Redis-Backed Chat Memory.

For longer-term persistence across chat sessions, you can swap out the default in-memory `chatHistory` that backs chat memory classes like `BufferMemory` for an Upstash [Redis](https://redis.io/) instance.

Setup[](#setup "Direct link to Setup")
---------------------------------------

You will need to install [@upstash/redis](https://github.com/upstash/upstash-redis) in your project:

*   npm
*   Yarn
*   pnpm

    npm install @upstash/redis

    yarn add @upstash/redis

    pnpm add @upstash/redis

You will also need an Upstash Account and a Redis database to connect to. See instructions on [Upstash Docs](https://docs.upstash.com/redis) on how to create a HTTP client.

Usage[](#usage "Direct link to Usage")
---------------------------------------

Each chat history session stored in Redis must have a unique id. You can provide an optional `sessionTTL` to make sessions expire after a give number of seconds. The `config` parameter is passed directly into the `new Redis()` constructor of [@upstash/redis](https://docs.upstash.com/redis/sdks/javascriptsdk/overview), and takes all the same arguments.

    import { BufferMemory } from "langchain/memory";import { UpstashRedisChatMessageHistory } from "langchain/stores/message/upstash_redis";import { ChatOpenAI } from "langchain/chat_models/openai";import { ConversationChain } from "langchain/chains";const memory = new BufferMemory({  chatHistory: new UpstashRedisChatMessageHistory({    sessionId: new Date().toISOString(), // Or some other unique identifier for the conversation    sessionTTL: 300, // 5 minutes, omit this parameter to make sessions never expire    config: {      url: "https://ADD_YOURS_HERE.upstash.io", // Override with your own instance's URL      token: "********", // Override with your own instance's token    },  }),});const model = new ChatOpenAI({  modelName: "gpt-3.5-turbo",  temperature: 0,});const chain = new ConversationChain({ llm: model, memory });const res1 = await chain.call({ input: "Hi! I'm Jim." });console.log({ res1 });/*{  res1: {    text: "Hello Jim! It's nice to meet you. My name is AI. How may I assist you today?"  }}*/const res2 = await chain.call({ input: "What did I just say my name was?" });console.log({ res2 });/*{  res1: {    text: "You said your name was Jim."  }}*/

#### API Reference:

*   [BufferMemory](/docs/api/memory/classes/BufferMemory) from `langchain/memory`
*   [UpstashRedisChatMessageHistory](/docs/api/stores_message_upstash_redis/classes/UpstashRedisChatMessageHistory) from `langchain/stores/message/upstash_redis`
*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [ConversationChain](/docs/api/chains/classes/ConversationChain) from `langchain/chains`

Advanced Usage[](#advanced-usage "Direct link to Advanced Usage")
------------------------------------------------------------------

You can also directly pass in a previously created [@upstash/redis](https://docs.upstash.com/redis/sdks/javascriptsdk/overview) client instance:

    import { Redis } from "@upstash/redis";import { BufferMemory } from "langchain/memory";import { UpstashRedisChatMessageHistory } from "langchain/stores/message/upstash_redis";import { ChatOpenAI } from "langchain/chat_models/openai";import { ConversationChain } from "langchain/chains";// Create your own Redis clientconst client = new Redis({  url: "https://ADD_YOURS_HERE.upstash.io",  token: "********",});const memory = new BufferMemory({  chatHistory: new UpstashRedisChatMessageHistory({    sessionId: new Date().toISOString(),    sessionTTL: 300,    client, // You can reuse your existing Redis client  }),});const model = new ChatOpenAI({  modelName: "gpt-3.5-turbo",  temperature: 0,});const chain = new ConversationChain({ llm: model, memory });const res1 = await chain.call({ input: "Hi! I'm Jim." });console.log({ res1 });/*{  res1: {    text: "Hello Jim! It's nice to meet you. My name is AI. How may I assist you today?"  }}*/const res2 = await chain.call({ input: "What did I just say my name was?" });console.log({ res2 });/*{  res1: {    text: "You said your name was Jim."  }}*/

#### API Reference:

*   [BufferMemory](/docs/api/memory/classes/BufferMemory) from `langchain/memory`
*   [UpstashRedisChatMessageHistory](/docs/api/stores_message_upstash_redis/classes/UpstashRedisChatMessageHistory) from `langchain/stores/message/upstash_redis`
*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [ConversationChain](/docs/api/chains/classes/ConversationChain) from `langchain/chains`