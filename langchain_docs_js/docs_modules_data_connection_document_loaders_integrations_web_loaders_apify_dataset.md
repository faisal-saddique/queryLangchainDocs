Apify Dataset
=============

This guide shows how to use [Apify](https://apify.com) with LangChain to load documents from an Apify Dataset.

Overview[](#overview "Direct link to Overview")
------------------------------------------------

[Apify](https://apify.com) is a cloud platform for web scraping and data extraction, which provides an [ecosystem](https://apify.com/store) of more than a thousand ready-made apps called _Actors_ for various web scraping, crawling, and data extraction use cases.

This guide shows how to load documents from an [Apify Dataset](https://docs.apify.com/platform/storage/dataset) — a scalable append-only storage built for storing structured web scraping results, such as a list of products or Google SERPs, and then export them to various formats like JSON, CSV, or Excel.

Datasets are typically used to save results of Actors. For example, [Website Content Crawler](https://apify.com/apify/website-content-crawler) Actor deeply crawls websites such as documentation, knowledge bases, help centers, or blogs, and then stores the text content of webpages into a dataset, from which you can feed the documents into a vector index and answer questions from it.

Setup[](#setup "Direct link to Setup")
---------------------------------------

You'll first need to install the official Apify client:

*   npm
*   Yarn
*   pnpm

    npm install apify-client

    yarn add apify-client

    pnpm add apify-client

You'll also need to sign up and retrieve your [Apify API token](https://console.apify.com/account/integrations).

Usage[](#usage "Direct link to Usage")
---------------------------------------

### From a New Dataset[](#from-a-new-dataset "Direct link to From a New Dataset")

If you don't already have an existing dataset on the Apify platform, you'll need to initialize the document loader by calling an Actor and waiting for the results.

**Note:** Calling an Actor can take a significant amount of time, on the order of hours, or even days for large sites!

Here's an example:

    import { ApifyDatasetLoader } from "langchain/document_loaders/web/apify_dataset";import { Document } from "langchain/document";import { HNSWLib } from "langchain/vectorstores/hnswlib";import { OpenAIEmbeddings } from "langchain/embeddings/openai";import { RetrievalQAChain } from "langchain/chains";import { OpenAI } from "langchain/llms/openai";/* * datasetMappingFunction is a function that maps your Apify dataset format to LangChain documents. * In the below example, the Apify dataset format looks like this: * { *   "url": "https://apify.com", *   "text": "Apify is the best web scraping and automation platform." * } */const loader = await ApifyDatasetLoader.fromActorCall(  "apify/website-content-crawler",  {    startUrls: [{ url: "https://js.langchain.com/docs/" }],  },  {    datasetMappingFunction: (item) =>      new Document({        pageContent: (item.text || "") as string,        metadata: { source: item.url },      }),    clientOptions: {      token: "your-apify-token", // Or set as process.env.APIFY_API_TOKEN    },  });const docs = await loader.load();const vectorStore = await HNSWLib.fromDocuments(docs, new OpenAIEmbeddings());const model = new OpenAI({  temperature: 0,});const chain = RetrievalQAChain.fromLLM(model, vectorStore.asRetriever(), {  returnSourceDocuments: true,});const res = await chain.call({ query: "What is LangChain?" });console.log(res.text);console.log(res.sourceDocuments.map((d: Document) => d.metadata.source));/*  LangChain is a framework for developing applications powered by language models.  [    'https://js.langchain.com/docs/',    'https://js.langchain.com/docs/modules/chains/',    'https://js.langchain.com/docs/modules/chains/llmchain/',    'https://js.langchain.com/docs/category/functions-4'  ]*/

#### API Reference:

*   [ApifyDatasetLoader](/docs/api/document_loaders_web_apify_dataset/classes/ApifyDatasetLoader) from `langchain/document_loaders/web/apify_dataset`
*   [Document](/docs/api/document/classes/Document) from `langchain/document`
*   [HNSWLib](/docs/api/vectorstores_hnswlib/classes/HNSWLib) from `langchain/vectorstores/hnswlib`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`
*   [RetrievalQAChain](/docs/api/chains/classes/RetrievalQAChain) from `langchain/chains`
*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`

From an Existing Dataset[](#from-an-existing-dataset "Direct link to From an Existing Dataset")
------------------------------------------------------------------------------------------------

If you already have an existing dataset on the Apify platform, you can initialize the document loader with the constructor directly:

    import { ApifyDatasetLoader } from "langchain/document_loaders/web/apify_dataset";import { Document } from "langchain/document";import { HNSWLib } from "langchain/vectorstores/hnswlib";import { OpenAIEmbeddings } from "langchain/embeddings/openai";import { RetrievalQAChain } from "langchain/chains";import { OpenAI } from "langchain/llms/openai";/* * datasetMappingFunction is a function that maps your Apify dataset format to LangChain documents. * In the below example, the Apify dataset format looks like this: * { *   "url": "https://apify.com", *   "text": "Apify is the best web scraping and automation platform." * } */const loader = new ApifyDatasetLoader("your-dataset-id", {  datasetMappingFunction: (item) =>    new Document({      pageContent: (item.text || "") as string,      metadata: { source: item.url },    }),  clientOptions: {    token: "your-apify-token", // Or set as process.env.APIFY_API_TOKEN  },});const docs = await loader.load();const vectorStore = await HNSWLib.fromDocuments(docs, new OpenAIEmbeddings());const model = new OpenAI({  temperature: 0,});const chain = RetrievalQAChain.fromLLM(model, vectorStore.asRetriever(), {  returnSourceDocuments: true,});const res = await chain.call({ query: "What is LangChain?" });console.log(res.text);console.log(res.sourceDocuments.map((d: Document) => d.metadata.source));/*  LangChain is a framework for developing applications powered by language models.  [    'https://js.langchain.com/docs/',    'https://js.langchain.com/docs/modules/chains/',    'https://js.langchain.com/docs/modules/chains/llmchain/',    'https://js.langchain.com/docs/category/functions-4'  ]*/

#### API Reference:

*   [ApifyDatasetLoader](/docs/api/document_loaders_web_apify_dataset/classes/ApifyDatasetLoader) from `langchain/document_loaders/web/apify_dataset`
*   [Document](/docs/api/document/classes/Document) from `langchain/document`
*   [HNSWLib](/docs/api/vectorstores_hnswlib/classes/HNSWLib) from `langchain/vectorstores/hnswlib`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`
*   [RetrievalQAChain](/docs/api/chains/classes/RetrievalQAChain) from `langchain/chains`
*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`