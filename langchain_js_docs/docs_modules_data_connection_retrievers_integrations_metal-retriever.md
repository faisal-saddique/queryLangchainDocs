Metal Retriever
===============

This example shows how to use the Metal Retriever in a `RetrievalQAChain` to retrieve documents from a Metal index.

Setup[​](#setup "Direct link to Setup")
---------------------------------------

*   npm
*   Yarn
*   pnpm

    npm i @getmetal/metal-sdk

    yarn add @getmetal/metal-sdk

    pnpm add @getmetal/metal-sdk

Usage[​](#usage "Direct link to Usage")
---------------------------------------

    /* eslint-disable @typescript-eslint/no-non-null-assertion */import Metal from "@getmetal/metal-sdk";import { MetalRetriever } from "langchain/retrievers/metal";export const run = async () => {  const MetalSDK = Metal;  const client = new MetalSDK(    process.env.METAL_API_KEY!,    process.env.METAL_CLIENT_ID!,    process.env.METAL_INDEX_ID  );  const retriever = new MetalRetriever({ client });  const docs = await retriever.getRelevantDocuments("hello");  console.log(docs);};

#### API Reference:

*   [MetalRetriever](/docs/api/retrievers_metal/classes/MetalRetriever) from `langchain/retrievers/metal`