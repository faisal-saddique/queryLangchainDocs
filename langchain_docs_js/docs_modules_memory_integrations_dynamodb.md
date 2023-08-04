DynamoDB-Backed Chat Memory
===========================

For longer-term persistence across chat sessions, you can swap out the default in-memory `chatHistory` that backs chat memory classes like `BufferMemory` for a DynamoDB instance.

Setup[](#setup "Direct link to Setup")
---------------------------------------

First, install the AWS DynamoDB client in your project:

*   npm
*   Yarn
*   pnpm

    npm install @aws-sdk/client-dynamodb

    yarn add @aws-sdk/client-dynamodb

    pnpm add @aws-sdk/client-dynamodb

Next, sign into your AWS account and create a DynamoDB table. Name the table `langchain`, and name your partition key `id`. Make sure your partition key is a string. You can leave sort key and the other settings alone.

You'll also need to retrieve an AWS access key and secret key for a role or user that has access to the table and add them to your environment variables.

Usage[](#usage "Direct link to Usage")
---------------------------------------

    import { BufferMemory } from "langchain/memory";import { DynamoDBChatMessageHistory } from "langchain/stores/message/dynamodb";import { ChatOpenAI } from "langchain/chat_models/openai";import { ConversationChain } from "langchain/chains";const memory = new BufferMemory({  chatHistory: new DynamoDBChatMessageHistory({    tableName: "langchain",    partitionKey: "id",    sessionId: new Date().toISOString(), // Or some other unique identifier for the conversation    config: {      region: "us-east-2",      credentials: {        accessKeyId: "<your AWS access key id>",        secretAccessKey: "<your AWS secret access key>",      },    },  }),});const model = new ChatOpenAI();const chain = new ConversationChain({ llm: model, memory });const res1 = await chain.call({ input: "Hi! I'm Jim." });console.log({ res1 });/*{  res1: {    text: "Hello Jim! It's nice to meet you. My name is AI. How may I assist you today?"  }}*/const res2 = await chain.call({ input: "What did I just say my name was?" });console.log({ res2 });/*{  res1: {    text: "You said your name was Jim."  }}*/

#### API Reference:

*   [BufferMemory](/docs/api/memory/classes/BufferMemory) from `langchain/memory`
*   [DynamoDBChatMessageHistory](/docs/api/stores_message_dynamodb/classes/DynamoDBChatMessageHistory) from `langchain/stores/message/dynamodb`
*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [ConversationChain](/docs/api/chains/classes/ConversationChain) from `langchain/chains`