Amazon Kendra Retriever
=======================

Amazon Kendra is an intelligent search service provided by Amazon Web Services (AWS). It utilizes advanced natural language processing (NLP) and machine learning algorithms to enable powerful search capabilities across various data sources within an organization. Kendra is designed to help users find the information they need quickly and accurately, improving productivity and decision-making.

With Kendra, users can search across a wide range of content types, including documents, FAQs, knowledge bases, manuals, and websites. It supports multiple languages and can understand complex queries, synonyms, and contextual meanings to provide highly relevant search results.

Setup[](#setup "Direct link to Setup")
---------------------------------------

*   npm
*   Yarn
*   pnpm

    npm i @aws-sdk/client-kendra

    yarn add @aws-sdk/client-kendra

    pnpm add @aws-sdk/client-kendra

Usage[](#usage "Direct link to Usage")
---------------------------------------

    import { AmazonKendraRetriever } from "langchain/retrievers/amazon_kendra";const retriever = new AmazonKendraRetriever({  topK: 10,  indexId: "YOUR_INDEX_ID",  region: "us-east-2", // Your region  clientOptions: {    credentials: {      accessKeyId: "YOUR_ACCESS_KEY_ID",      secretAccessKey: "YOUR_SECRET_ACCESS_KEY",    },  },});const docs = await retriever.getRelevantDocuments("How are clouds formed?");console.log(docs);

#### API Reference:

*   [AmazonKendraRetriever](/docs/api/retrievers_amazon_kendra/classes/AmazonKendraRetriever) from `langchain/retrievers/amazon_kendra`