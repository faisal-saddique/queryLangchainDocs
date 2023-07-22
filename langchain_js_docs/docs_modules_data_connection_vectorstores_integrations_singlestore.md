SingleStore
===========

[SingleStoreDB](https://singlestore.com/) is a high-performance distributed SQL database that supports deployment both in the [cloud](https://www.singlestore.com/cloud/) and on-premise. It provides vector storage, as well as vector functions like [dot\_product](https://docs.singlestore.com/managed-service/en/reference/sql-reference/vector-functions/dot_product.html) and [euclidean\_distance](https://docs.singlestore.com/managed-service/en/reference/sql-reference/vector-functions/euclidean_distance.html), thereby supporting AI applications that require text similarity matching.

Compatibility

Only available on Node.js.

LangChain.js requires the `mysql2` library to create a connection to a SingleStoreDB instance.

Setup[​](#setup "Direct link to Setup")
---------------------------------------

1.  Establish a SingleStoreDB environment. You have the flexibility to choose between [Cloud-based](https://docs.singlestore.com/managed-service/en/getting-started-with-singlestoredb-cloud.html) or [On-Premise](https://docs.singlestore.com/db/v8.1/en/developer-resources/get-started-using-singlestoredb-for-free.html) editions.
2.  Install the mysql2 JS client

*   npm
*   Yarn
*   pnpm

    npm install -S mysql2

    yarn add mysql2

    pnpm add mysql2

Usage[​](#usage "Direct link to Usage")
---------------------------------------

`SingleStoreVectorStore` manages a connection pool. It is recommended to call `await store.end();` before terminating your application to assure all connections are appropriately closed and prevent any possible resource leaks.

### Standard usage[​](#standard-usage "Direct link to Standard usage")

Below is a straightforward example showcasing how to import the relevant module and perform a base similarity search using the `SingleStoreVectorStore`:

    import { SingleStoreVectorStore } from "langchain/vectorstores/singlestore";import { OpenAIEmbeddings } from "langchain/embeddings/openai";export const run = async () => {  const vectorStore = await SingleStoreVectorStore.fromTexts(    ["Hello world", "Bye bye", "hello nice world"],    [{ id: 2 }, { id: 1 }, { id: 3 }],    new OpenAIEmbeddings(),    {      connectionOptions: {        host: process.env.SINGLESTORE_HOST,        port: Number(process.env.SINGLESTORE_PORT),        user: process.env.SINGLESTORE_USERNAME,        password: process.env.SINGLESTORE_PASSWORD,        database: process.env.SINGLESTORE_DATABASE,      },    }  );  const resultOne = await vectorStore.similaritySearch("hello world", 1);  console.log(resultOne);  await vectorStore.end();};

#### API Reference:

*   [SingleStoreVectorStore](/docs/api/vectorstores_singlestore/classes/SingleStoreVectorStore) from `langchain/vectorstores/singlestore`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`

### Metadata Filtering[​](#metadata-filtering "Direct link to Metadata Filtering")

If it is needed to filter results based on specific metadata fields, you can pass a filter parameter to narrow down your search to the documents that match all specified fields in the filter object:

    import { SingleStoreVectorStore } from "langchain/vectorstores/singlestore";import { OpenAIEmbeddings } from "langchain/embeddings/openai";export const run = async () => {  const vectorStore = await SingleStoreVectorStore.fromTexts(    ["Good afternoon", "Bye bye", "Boa tarde!", "Até logo!"],    [      { id: 1, language: "English" },      { id: 2, language: "English" },      { id: 3, language: "Portugese" },      { id: 4, language: "Portugese" },    ],    new OpenAIEmbeddings(),    {      connectionOptions: {        host: process.env.SINGLESTORE_HOST,        port: Number(process.env.SINGLESTORE_PORT),        user: process.env.SINGLESTORE_USERNAME,        password: process.env.SINGLESTORE_PASSWORD,        database: process.env.SINGLESTORE_DATABASE,      },      distanceMetric: "EUCLIDEAN_DISTANCE",    }  );  const resultOne = await vectorStore.similaritySearch("greetings", 1, {    language: "Portugese",  });  console.log(resultOne);  await vectorStore.end();};

#### API Reference:

*   [SingleStoreVectorStore](/docs/api/vectorstores_singlestore/classes/SingleStoreVectorStore) from `langchain/vectorstores/singlestore`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`