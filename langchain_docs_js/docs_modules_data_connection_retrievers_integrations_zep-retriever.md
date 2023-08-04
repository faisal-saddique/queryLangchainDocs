Zep Retriever
=============

This example shows how to use the Zep Retriever in a `RetrievalQAChain` to retrieve documents from Zep memory store.

Setup[](#setup "Direct link to Setup")
---------------------------------------

*   npm
*   Yarn
*   pnpm

    npm i @getzep/zep-js

    yarn add @getzep/zep-js

    pnpm add @getzep/zep-js

Usage[](#usage "Direct link to Usage")
---------------------------------------

    import { ZepRetriever } from "langchain/retrievers/zep";export const run = async () => {  const url = process.env.ZEP_URL || "http://localhost:8000";  const sessionId = "TestSession1232";  console.log(`Session ID: ${sessionId}, URL: ${url}`);  const retriever = new ZepRetriever({ sessionId, url });  const query = "hello";  const docs = await retriever.getRelevantDocuments(query);  console.log(docs);};

#### API Reference:

*   [ZepRetriever](/docs/api/retrievers_zep/classes/ZepRetriever) from `langchain/retrievers/zep`