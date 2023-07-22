Streaming
=========

Some Chat models provide a streaming response. This means that instead of waiting for the entire response to be returned, you can start processing it as soon as it's available. This is useful if you want to display the response to the user as it's being generated, or if you want to process the response as it's being generated.

    import { ChatOpenAI } from "langchain/chat_models/openai";import { HumanMessage } from "langchain/schema";const chat = new ChatOpenAI({  maxTokens: 25,  streaming: true,});const response = await chat.call([new HumanMessage("Tell me a joke.")], {  callbacks: [    {      handleLLMNewToken(token: string) {        console.log({ token });      },    },  ],});console.log(response);// { token: '' }// { token: '\n\n' }// { token: 'Why' }// { token: ' don' }// { token: "'t" }// { token: ' scientists' }// { token: ' trust' }// { token: ' atoms' }// { token: '?\n\n' }// { token: 'Because' }// { token: ' they' }// { token: ' make' }// { token: ' up' }// { token: ' everything' }// { token: '.' }// { token: '' }// AIMessage {//   text: "\n\nWhy don't scientists trust atoms?\n\nBecause they make up everything."// }

#### API Reference:

*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [HumanMessage](/docs/api/schema/classes/HumanMessage) from `langchain/schema`