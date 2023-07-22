Tigris
======

Tigris makes it easy to build AI applications with vector embeddings. It is a fully managed cloud-native database that allows you store and index documents and vector embeddings for fast and scalable vector search.

Compatibility

Only available on Node.js.

Setup[​](#setup "Direct link to Setup")
---------------------------------------

### 1\. Install the Tigris SDK[​](#1-install-the-tigris-sdk "Direct link to 1. Install the Tigris SDK")

Install the SDK as follows

*   npm
*   Yarn
*   pnpm

    npm install -S @tigrisdata/vector

    yarn add @tigrisdata/vector

    pnpm add @tigrisdata/vector

### 2\. Fetch Tigris API credentials[​](#2-fetch-tigris-api-credentials "Direct link to 2. Fetch Tigris API credentials")

You can sign up for a free Tigris account [here](https://console.preview.tigrisdata.cloud/signup).

Once you have signed up for the Tigris account, create a new project called `vectordemo`. Next, make a note of the `clientId` and `clientSecret`, which you can get from the Application Keys section of the project.

Index docs[​](#index-docs "Direct link to Index docs")
------------------------------------------------------

    import { VectorDocumentStore } from "@tigrisdata/vector";import { Document } from "langchain/document";import { OpenAIEmbeddings } from "langchain/embeddings/openai";import { TigrisVectorStore } from "langchain/vectorstores/tigris";const index = new VectorDocumentStore({  connection: {    serverUrl: "api.preview.tigrisdata.cloud",    projectName: process.env.TIGRIS_PROJECT,    clientId: process.env.TIGRIS_CLIENT_ID,    clientSecret: process.env.TIGRIS_CLIENT_SECRET,  },  indexName: "examples_index",  numDimensions: 1536, // match the OpenAI embedding size});const docs = [  new Document({    metadata: { foo: "bar" },    pageContent: "tigris is a cloud-native vector db",  }),  new Document({    metadata: { foo: "bar" },    pageContent: "the quick brown fox jumped over the lazy dog",  }),  new Document({    metadata: { baz: "qux" },    pageContent: "lorem ipsum dolor sit amet",  }),  new Document({    metadata: { baz: "qux" },    pageContent: "tigris is a river",  }),];await TigrisVectorStore.fromDocuments(docs, new OpenAIEmbeddings(), { index });

#### API Reference:

*   [Document](/docs/api/document/classes/Document) from `langchain/document`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`
*   [TigrisVectorStore](/docs/api/vectorstores_tigris/classes/TigrisVectorStore) from `langchain/vectorstores/tigris`

Query docs[​](#query-docs "Direct link to Query docs")
------------------------------------------------------

    import { VectorDocumentStore } from "@tigrisdata/vector";import { OpenAIEmbeddings } from "langchain/embeddings/openai";import { TigrisVectorStore } from "langchain/vectorstores/tigris";const index = new VectorDocumentStore({  connection: {    serverUrl: "api.preview.tigrisdata.cloud",    projectName: process.env.TIGRIS_PROJECT,    clientId: process.env.TIGRIS_CLIENT_ID,    clientSecret: process.env.TIGRIS_CLIENT_SECRET,  },  indexName: "examples_index",  numDimensions: 1536, // match the OpenAI embedding size});const vectorStore = await TigrisVectorStore.fromExistingIndex(  new OpenAIEmbeddings(),  { index });/* Search the vector DB independently with metadata filters */const results = await vectorStore.similaritySearch("tigris", 1, {  "metadata.foo": "bar",});console.log(JSON.stringify(results, null, 2));/*[  Document {    pageContent: 'tigris is a cloud-native vector db',    metadata: { foo: 'bar' }  }]*/

#### API Reference:

*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`
*   [TigrisVectorStore](/docs/api/vectorstores_tigris/classes/TigrisVectorStore) from `langchain/vectorstores/tigris`