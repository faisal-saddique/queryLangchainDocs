Xata
====

[Xata](https://xata.io) is a serverless data platform, based on PostgreSQL. It provides a type-safe TypeScript/JavaScript SDK for interacting with your database, and a UI for managing your data.

Xata has a native vector type, which can be added to any table, and supports similarity search. LangChain inserts vectors directly to Xata, and queries it for the nearest neighbors of a given vector, so that you can use all the LangChain Embeddings integrations with Xata.

Setup[](#setup "Direct link to Setup")
---------------------------------------

### Install the Xata CLI[](#install-the-xata-cli "Direct link to Install the Xata CLI")

    npm install @xata.io/cli -g

### Create a database to be used as a vector store[](#create-a-database-to-be-used-as-a-vector-store "Direct link to Create a database to be used as a vector store")

In the [Xata UI](https://app.xata.io) create a new database. You can name it whatever you want, but for this example we'll use `langchain`. Create a table, again you can name it anything, but we will use `vectors`. Add the following columns via the UI:

*   `content` of type "Long text". This is used to store the `Document.pageContent` values.
*   `embedding` of type "Vector". Use the dimension used by the model you plan to use (1536 for OpenAI).
*   any other columns you want to use as metadata. They are populated from the `Document.metadata` object. For example, if in the `Document.metadata` object you have a `title` property, you can create a `title` column in the table and it will be populated.

### Initialize the project[](#initialize-the-project "Direct link to Initialize the project")

In your project, run:

    xata init

and then choose the database you created above. This will also generate a `xata.ts` or `xata.js` file that defines the client you can use to interact with the database. See the [Xata getting started docs](https://xata.io/docs/getting-started/installation) for more details on using the Xata JavaScript/TypeScript SDK.

Usage[](#usage "Direct link to Usage")
---------------------------------------

### Example: Q&A chatbot using OpenAI and Xata as vector store[](#example-qa-chatbot-using-openai-and-xata-as-vector-store "Direct link to Example: Q&A chatbot using OpenAI and Xata as vector store")

This example uses the `VectorDBQAChain` to search the documents stored in Xata and then pass them as context to the OpenAI model, in order to answer the question asked by the user.

    import { XataVectorSearch } from "langchain/vectorstores/xata";import { OpenAIEmbeddings } from "langchain/embeddings/openai";import { BaseClient } from "@xata.io/client";import { Document } from "langchain/document";import { VectorDBQAChain } from "langchain/chains";import { OpenAI } from "langchain/llms/openai";// First, follow set-up instructions at// https://js.langchain.com/docs/modules/data_connection/vectorstores/integrations/xata// if you use the generated client, you don't need this function.// Just import getXataClient from the generated xata.ts instead.const getXataClient = () => {  if (!process.env.XATA_API_KEY) {    throw new Error("XATA_API_KEY not set");  }  if (!process.env.XATA_DB_URL) {    throw new Error("XATA_DB_URL not set");  }  const xata = new BaseClient({    databaseURL: process.env.XATA_DB_URL,    apiKey: process.env.XATA_API_KEY,    branch: process.env.XATA_BRANCH || "main",  });  return xata;};export async function run() {  const client = getXataClient();  const table = "vectors";  const embeddings = new OpenAIEmbeddings();  const store = new XataVectorSearch(embeddings, { client, table });  // Add documents  const docs = [    new Document({      pageContent: "Xata is a Serverless Data platform based on PostgreSQL",    }),    new Document({      pageContent:        "Xata offers a built-in vector type that can be used to store and query vectors",    }),    new Document({      pageContent: "Xata includes similarity search",    }),  ];  const ids = await store.addDocuments(docs);  // eslint-disable-next-line no-promise-executor-return  await new Promise((r) => setTimeout(r, 2000));  const model = new OpenAI();  const chain = VectorDBQAChain.fromLLM(model, store, {    k: 1,    returnSourceDocuments: true,  });  const response = await chain.call({ query: "What is Xata?" });  console.log(JSON.stringify(response, null, 2));  await store.delete({ ids });}

#### API Reference:

*   [XataVectorSearch](/docs/api/vectorstores_xata/classes/XataVectorSearch) from `langchain/vectorstores/xata`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`
*   [Document](/docs/api/document/classes/Document) from `langchain/document`
*   [VectorDBQAChain](/docs/api/chains/classes/VectorDBQAChain) from `langchain/chains`
*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`

### Example: Similarity search with a metadata filter[](#example-similarity-search-with-a-metadata-filter "Direct link to Example: Similarity search with a metadata filter")

This example shows how to implement semantic search using LangChain.js and Xata. Before running it, make sure to add an `author` column of type String to the `vectors` table in Xata.

    import { XataVectorSearch } from "langchain/vectorstores/xata";import { OpenAIEmbeddings } from "langchain/embeddings/openai";import { BaseClient } from "@xata.io/client";import { Document } from "langchain/document";// First, follow set-up instructions at// https://js.langchain.com/docs/modules/data_connection/vectorstores/integrations/xata// Also, add a column named "author" to the "vectors" table.// if you use the generated client, you don't need this function.// Just import getXataClient from the generated xata.ts instead.const getXataClient = () => {  if (!process.env.XATA_API_KEY) {    throw new Error("XATA_API_KEY not set");  }  if (!process.env.XATA_DB_URL) {    throw new Error("XATA_DB_URL not set");  }  const xata = new BaseClient({    databaseURL: process.env.XATA_DB_URL,    apiKey: process.env.XATA_API_KEY,    branch: process.env.XATA_BRANCH || "main",  });  return xata;};export async function run() {  const client = getXataClient();  const table = "vectors";  const embeddings = new OpenAIEmbeddings();  const store = new XataVectorSearch(embeddings, { client, table });  // Add documents  const docs = [    new Document({      pageContent: "Xata works great with Langchain.js",      metadata: { author: "Xata" },    }),    new Document({      pageContent: "Xata works great with Langchain",      metadata: { author: "Langchain" },    }),    new Document({      pageContent: "Xata includes similarity search",      metadata: { author: "Xata" },    }),  ];  const ids = await store.addDocuments(docs);  // eslint-disable-next-line no-promise-executor-return  await new Promise((r) => setTimeout(r, 2000));  // author is applied as pre-filter to the similarity search  const results = await store.similaritySearchWithScore("xata works great", 6, {    author: "Langchain",  });  console.log(JSON.stringify(results, null, 2));  await store.delete({ ids });}

#### API Reference:

*   [XataVectorSearch](/docs/api/vectorstores_xata/classes/XataVectorSearch) from `langchain/vectorstores/xata`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`
*   [Document](/docs/api/document/classes/Document) from `langchain/document`