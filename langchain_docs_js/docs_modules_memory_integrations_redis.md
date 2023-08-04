Redis-Backed Chat Memory
========================

For longer-term persistence across chat sessions, you can swap out the default in-memory `chatHistory` that backs chat memory classes like `BufferMemory` for a [Redis](https://redis.io/) instance.

Setup[](#setup "Direct link to Setup")
---------------------------------------

You will need to install [node-redis](https://github.com/redis/node-redis) in your project:

*   npm
*   Yarn
*   pnpm

    npm install redis

    yarn add redis

    pnpm add redis

You will also need a Redis instance to connect to. See instructions on [the official Redis website](https://redis.io/docs/getting-started/) for running the server locally.

Usage[](#usage "Direct link to Usage")
---------------------------------------

Each chat history session stored in Redis must have a unique id. You can provide an optional `sessionTTL` to make sessions expire after a give number of seconds. The `config` parameter is passed directly into the `createClient` method of [node-redis](https://github.com/redis/node-redis), and takes all the same arguments.

    import { BufferMemory } from "langchain/memory";import { RedisChatMessageHistory } from "langchain/stores/message/ioredis";import { ChatOpenAI } from "langchain/chat_models/openai";import { ConversationChain } from "langchain/chains";const memory = new BufferMemory({  chatHistory: new RedisChatMessageHistory({    sessionId: new Date().toISOString(), // Or some other unique identifier for the conversation    sessionTTL: 300, // 5 minutes, omit this parameter to make sessions never expire    url: "redis://localhost:6379", // Default value, override with your own instance's URL  }),});const model = new ChatOpenAI({  modelName: "gpt-3.5-turbo",  temperature: 0,});const chain = new ConversationChain({ llm: model, memory });const res1 = await chain.call({ input: "Hi! I'm Jim." });console.log({ res1 });/*{  res1: {    text: "Hello Jim! It's nice to meet you. My name is AI. How may I assist you today?"  }}*/const res2 = await chain.call({ input: "What did I just say my name was?" });console.log({ res2 });/*{  res1: {    text: "You said your name was Jim."  }}*/

#### API Reference:

*   [BufferMemory](/docs/api/memory/classes/BufferMemory) from `langchain/memory`
*   [RedisChatMessageHistory](/docs/api/stores_message_ioredis/classes/RedisChatMessageHistory) from `langchain/stores/message/ioredis`
*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [ConversationChain](/docs/api/chains/classes/ConversationChain) from `langchain/chains`

Advanced Usage[](#advanced-usage "Direct link to Advanced Usage")
------------------------------------------------------------------

You can also directly pass in a previously created [node-redis](https://github.com/redis/node-redis) client instance:

    import { Redis } from "ioredis";import { BufferMemory } from "langchain/memory";import { RedisChatMessageHistory } from "langchain/stores/message/ioredis";import { ChatOpenAI } from "langchain/chat_models/openai";import { ConversationChain } from "langchain/chains";const client = new Redis("redis://localhost:6379");const memory = new BufferMemory({  chatHistory: new RedisChatMessageHistory({    sessionId: new Date().toISOString(),    sessionTTL: 300,    client,  }),});const model = new ChatOpenAI({  modelName: "gpt-3.5-turbo",  temperature: 0,});const chain = new ConversationChain({ llm: model, memory });const res1 = await chain.call({ input: "Hi! I'm Jim." });console.log({ res1 });/*{  res1: {    text: "Hello Jim! It's nice to meet you. My name is AI. How may I assist you today?"  }}*/const res2 = await chain.call({ input: "What did I just say my name was?" });console.log({ res2 });/*{  res1: {    text: "You said your name was Jim."  }}*/

#### API Reference:

*   [BufferMemory](/docs/api/memory/classes/BufferMemory) from `langchain/memory`
*   [RedisChatMessageHistory](/docs/api/stores_message_ioredis/classes/RedisChatMessageHistory) from `langchain/stores/message/ioredis`
*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [ConversationChain](/docs/api/chains/classes/ConversationChain) from `langchain/chains`

### Redis Sentinel Support[](#redis-sentinel-support "Direct link to Redis Sentinel Support")

You can enable a Redis Sentinel backed cache using [ioredis](https://github.com/redis/ioredis)

This will require the installation of [ioredis](https://github.com/redis/ioredis) in your project.

*   npm
*   Yarn
*   pnpm

    npm install ioredis

    yarn add ioredis

    pnpm add ioredis

    import { Redis } from "ioredis";import { BufferMemory } from "langchain/memory";import { RedisChatMessageHistory } from "langchain/stores/message/ioredis";import { ChatOpenAI } from "langchain/chat_models/openai";import { ConversationChain } from "langchain/chains";// Uses ioredis to facilitate Sentinel Connections see their docs for details on setting up more complex Sentinels: https://github.com/redis/ioredis#sentinelconst client = new Redis({  sentinels: [    { host: "localhost", port: 26379 },    { host: "localhost", port: 26380 },  ],  name: "mymaster",});const memory = new BufferMemory({  chatHistory: new RedisChatMessageHistory({    sessionId: new Date().toISOString(),    sessionTTL: 300,    client,  }),});const model = new ChatOpenAI({ temperature: 0.5 });const chain = new ConversationChain({ llm: model, memory });const res1 = await chain.call({ input: "Hi! I'm Jim." });console.log({ res1 });/*{  res1: {    text: "Hello Jim! It's nice to meet you. My name is AI. How may I assist you today?"  }}*/const res2 = await chain.call({ input: "What did I just say my name was?" });console.log({ res2 });/*{  res1: {    text: "You said your name was Jim."  }}*/

#### API Reference:

*   [BufferMemory](/docs/api/memory/classes/BufferMemory) from `langchain/memory`
*   [RedisChatMessageHistory](/docs/api/stores_message_ioredis/classes/RedisChatMessageHistory) from `langchain/stores/message/ioredis`
*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [ConversationChain](/docs/api/chains/classes/ConversationChain) from `langchain/chains`