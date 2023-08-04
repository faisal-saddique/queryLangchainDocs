Weaviate
========

Weaviate is an open source vector database that stores both objects and vectors, allowing for combining vector search with structured filtering. LangChain connects to Weaviate via the `weaviate-ts-client` package, the official Typescript client for Weaviate.

LangChain inserts vectors directly to Weaviate, and queries Weaviate for the nearest neighbors of a given vector, so that you can use all the LangChain Embeddings integrations with Weaviate.

Setup[](#setup "Direct link to Setup")
---------------------------------------

*   npm
*   Yarn
*   pnpm

    npm install weaviate-ts-client graphql

    yarn add weaviate-ts-client graphql

    pnpm add weaviate-ts-client graphql

You'll need to run Weaviate either locally or on a server, see [the Weaviate documentation](https://weaviate.io/developers/weaviate/installation) for more information.

Usage, insert documents[](#usage-insert-documents "Direct link to Usage, insert documents")
--------------------------------------------------------------------------------------------

    /* eslint-disable @typescript-eslint/no-explicit-any */import weaviate from "weaviate-ts-client";import { WeaviateStore } from "langchain/vectorstores/weaviate";import { OpenAIEmbeddings } from "langchain/embeddings/openai";export async function run() {  // Something wrong with the weaviate-ts-client types, so we need to disable  const client = (weaviate as any).client({    scheme: process.env.WEAVIATE_SCHEME || "https",    host: process.env.WEAVIATE_HOST || "localhost",    apiKey: new (weaviate as any).ApiKey(      process.env.WEAVIATE_API_KEY || "default"    ),  });  // Create a store and fill it with some texts + metadata  await WeaviateStore.fromTexts(    ["hello world", "hi there", "how are you", "bye now"],    [{ foo: "bar" }, { foo: "baz" }, { foo: "qux" }, { foo: "bar" }],    new OpenAIEmbeddings(),    {      client,      indexName: "Test",      textKey: "text",      metadataKeys: ["foo"],    }  );}

#### API Reference:

*   [WeaviateStore](/docs/api/vectorstores_weaviate/classes/WeaviateStore) from `langchain/vectorstores/weaviate`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`

Usage, query documents[](#usage-query-documents "Direct link to Usage, query documents")
-----------------------------------------------------------------------------------------

    /* eslint-disable @typescript-eslint/no-explicit-any */import weaviate from "weaviate-ts-client";import { WeaviateStore } from "langchain/vectorstores/weaviate";import { OpenAIEmbeddings } from "langchain/embeddings/openai";export async function run() {  // Something wrong with the weaviate-ts-client types, so we need to disable  const client = (weaviate as any).client({    scheme: process.env.WEAVIATE_SCHEME || "https",    host: process.env.WEAVIATE_HOST || "localhost",    apiKey: new (weaviate as any).ApiKey(      process.env.WEAVIATE_API_KEY || "default"    ),  });  // Create a store for an existing index  const store = await WeaviateStore.fromExistingIndex(new OpenAIEmbeddings(), {    client,    indexName: "Test",    metadataKeys: ["foo"],  });  // Search the index without any filters  const results = await store.similaritySearch("hello world", 1);  console.log(results);  /*  [ Document { pageContent: 'hello world', metadata: { foo: 'bar' } } ]  */  // Search the index with a filter, in this case, only return results where  // the "foo" metadata key is equal to "baz", see the Weaviate docs for more  // https://weaviate.io/developers/weaviate/api/graphql/filters  const results2 = await store.similaritySearch("hello world", 1, {    where: {      operator: "Equal",      path: ["foo"],      valueText: "baz",    },  });  console.log(results2);  /*  [ Document { pageContent: 'hi there', metadata: { foo: 'baz' } } ]  */}

#### API Reference:

*   [WeaviateStore](/docs/api/vectorstores_weaviate/classes/WeaviateStore) from `langchain/vectorstores/weaviate`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`

Usage delete documents[](#usage-delete-documents "Direct link to Usage delete documents")
------------------------------------------------------------------------------------------

    /* eslint-disable @typescript-eslint/no-explicit-any */import weaviate from "weaviate-ts-client";import { WeaviateStore } from "langchain/vectorstores/weaviate";import { OpenAIEmbeddings } from "langchain/embeddings/openai";export async function run() {  // Something wrong with the weaviate-ts-client types, so we need to disable  const client = (weaviate as any).client({    scheme: process.env.WEAVIATE_SCHEME || "https",    host: process.env.WEAVIATE_HOST || "localhost",    apiKey: new (weaviate as any).ApiKey(      process.env.WEAVIATE_API_KEY || "default"    ),  });  // Create a store for an existing index  const store = await WeaviateStore.fromExistingIndex(new OpenAIEmbeddings(), {    client,    indexName: "Test",    metadataKeys: ["foo"],  });  const docs = [{ pageContent: "see ya!", metadata: { foo: "bar" } }];  // Also supports an additional {ids: []} parameter for upsertion  const ids = await store.addDocuments(docs);  // Search the index without any filters  const results = await store.similaritySearch("see ya!", 1);  console.log(results);  /*  [ Document { pageContent: 'see ya!', metadata: { foo: 'bar' } } ]  */  // Delete documents with ids  await store.delete({ ids });  const results2 = await store.similaritySearch("see ya!", 1);  console.log(results2);  /*  []  */  const docs2 = [    { pageContent: "hello world", metadata: { foo: "bar" } },    { pageContent: "hi there", metadata: { foo: "baz" } },    { pageContent: "how are you", metadata: { foo: "qux" } },    { pageContent: "hello world", metadata: { foo: "bar" } },    { pageContent: "bye now", metadata: { foo: "bar" } },  ];  await store.addDocuments(docs2);  const results3 = await store.similaritySearch("hello world", 1);  console.log(results3);  /*  [ Document { pageContent: 'hello world', metadata: { foo: 'bar' } } ]  */  // delete documents with filter  await store.delete({    filter: {      where: {        operator: "Equal",        path: ["foo"],        valueText: "bar",      },    },  });  const results4 = await store.similaritySearch("hello world", 1, {    where: {      operator: "Equal",      path: ["foo"],      valueText: "bar",    },  });  console.log(results4);  /*  []  */}

#### API Reference:

*   [WeaviateStore](/docs/api/vectorstores_weaviate/classes/WeaviateStore) from `langchain/vectorstores/weaviate`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`