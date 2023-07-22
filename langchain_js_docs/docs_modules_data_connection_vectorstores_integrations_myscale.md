MyScale
=======

Compatibility

Only available on Node.js.

[MyScale](https://myscale.com/) is an emerging AI database that harmonizes the power of vector search and SQL analytics, providing a managed, efficient, and responsive experience.

Setup[​](#setup "Direct link to Setup")
---------------------------------------

1.  Launch a cluster through [MyScale's Web Console](https://console.myscale.com/). See [MyScale's official documentation](https://docs.myscale.com/en/quickstart/) for more information.
2.  After launching a cluster, view your `Connection Details` from your cluster's `Actions` menu. You will need the host, port, username, and password.
3.  Install the required Node.js peer dependency in your workspace.

*   npm
*   Yarn
*   pnpm

    npm install -S @clickhouse/client

    yarn add @clickhouse/client

    pnpm add @clickhouse/client

Index and Query Docs[​](#index-and-query-docs "Direct link to Index and Query Docs")
------------------------------------------------------------------------------------

    import { MyScaleStore } from "langchain/vectorstores/myscale";import { OpenAIEmbeddings } from "langchain/embeddings/openai";const vectorStore = await MyScaleStore.fromTexts(  ["Hello world", "Bye bye", "hello nice world"],  [    { id: 2, name: "2" },    { id: 1, name: "1" },    { id: 3, name: "3" },  ],  new OpenAIEmbeddings(),  {    host: process.env.MYSCALE_HOST || "localhost",    port: process.env.MYSCALE_PORT || "8443",    username: process.env.MYSCALE_USERNAME || "username",    password: process.env.MYSCALE_PASSWORD || "password",  });const results = await vectorStore.similaritySearch("hello world", 1);console.log(results);const filteredResults = await vectorStore.similaritySearch("hello world", 1, {  whereStr: "metadata.name = '1'",});console.log(filteredResults);

#### API Reference:

*   [MyScaleStore](/docs/api/vectorstores_myscale/classes/MyScaleStore) from `langchain/vectorstores/myscale`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`

Query Docs From an Existing Collection[​](#query-docs-from-an-existing-collection "Direct link to Query Docs From an Existing Collection")
------------------------------------------------------------------------------------------------------------------------------------------

    import { MyScaleStore } from "langchain/vectorstores/myscale";import { OpenAIEmbeddings } from "langchain/embeddings/openai";const vectorStore = await MyScaleStore.fromExistingIndex(  new OpenAIEmbeddings(),  {    host: process.env.MYSCALE_HOST || "localhost",    port: process.env.MYSCALE_PORT || "8443",    username: process.env.MYSCALE_USERNAME || "username",    password: process.env.MYSCALE_PASSWORD || "password",    database: "your_database", // defaults to "default"    table: "your_table", // defaults to "vector_table"  });const results = await vectorStore.similaritySearch("hello world", 1);console.log(results);const filteredResults = await vectorStore.similaritySearch("hello world", 1, {  whereStr: "metadata.name = '1'",});console.log(filteredResults);

#### API Reference:

*   [MyScaleStore](/docs/api/vectorstores_myscale/classes/MyScaleStore) from `langchain/vectorstores/myscale`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`