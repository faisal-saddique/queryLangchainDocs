Firestore Chat Memory
=====================

For longer-term persistence across chat sessions, you can swap out the default in-memory `chatHistory` that backs chat memory classes like `BufferMemory` for a firestore.

Setup[](#setup "Direct link to Setup")
---------------------------------------

First, install the Firebase admin package in your project:

*   npm
*   Yarn
*   pnpm

    yarn add firebase-admin

    yarn add firebase-admin

    yarn add firebase-admin

Go to your the Settings icon Project settings in the Firebase console. In the Your apps card, select the nickname of the app for which you need a config object. Select Config from the Firebase SDK snippet pane. Copy the config object snippet, then add it to your firebase functions FirestoreChatMessageHistory.

Usage[](#usage "Direct link to Usage")
---------------------------------------

    import { BufferMemory } from "langchain/memory";import { FirestoreChatMessageHistory } from "langchain/stores/message/firestore";import { ChatOpenAI } from "langchain/chat_models/openai";import { ConversationChain } from "langchain/chains";const memory = new BufferMemory({  chatHistory: new FirestoreChatMessageHistory({    collectionName: "langchain",    sessionId: "lc-example",    userId: "a@example.com",    config: { projectId: "your-project-id" },  }),});const model = new ChatOpenAI();const chain = new ConversationChain({ llm: model, memory });const res1 = await chain.call({ input: "Hi! I'm Jim." });console.log({ res1 });/*{  res1: {    text: "Hello Jim! It's nice to meet you. My name is AI. How may I assist you today?"  }}*/const res2 = await chain.call({ input: "What did I just say my name was?" });console.log({ res2 });/*{  res1: {    text: "You said your name was Jim."  }}*/

#### API Reference:

*   [BufferMemory](/docs/api/memory/classes/BufferMemory) from `langchain/memory`
*   [FirestoreChatMessageHistory](/docs/api/stores_message_firestore/classes/FirestoreChatMessageHistory) from `langchain/stores/message/firestore`
*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [ConversationChain](/docs/api/chains/classes/ConversationChain) from `langchain/chains`

Firestore Rules[](#firestore-rules "Direct link to Firestore Rules")
---------------------------------------------------------------------

If your collection name is "chathistory," you can configure Firestore rules as follows.

          match /chathistory/{sessionId} {       allow read: if request.auth.uid == resource.data.createdBy;       allow write: if request.auth.uid == request.resource.data.createdBy;             }             match /chathistory/{sessionId}/messages/{messageId} {       allow read: if request.auth.uid == resource.data.createdBy;       allow write: if request.auth.uid == request.resource.data.createdBy;            }