MongoDB Atlas
=============

Compatibility

Only available on Node.js.

Langchain supports MongoDB Atlas as a vector store.

Setup[​](#setup "Direct link to Setup")
---------------------------------------

### Installation[​](#installation "Direct link to Installation")

First, add the Node MongoDB SDK to your project:

*   npm
*   Yarn
*   pnpm

    npm install -S mongodb

    yarn add mongodb

    pnpm add mongodb

### Initial Cluster Configuration[​](#initial-cluster-configuration "Direct link to Initial Cluster Configuration")

Next, you'll need create a MongoDB Atlas cluster. Navigate to the [MongoDB Atlas website](https://www.mongodb.com/atlas/database) and create an account if you don't already have one.

Create and name a cluster when prompted, then find it under `Database`. Select `Collections` and create either a blank collection or one from the provided sample data.

### Creating an Index[​](#creating-an-index "Direct link to Creating an Index")

After configuring your cluster, you'll need to create an index on the collection field you want to search over.

Go to the `Search` tab within your cluster, then select `Create Search Index`. Using the JSON editor option, add an index to the collection you wish to use.

    {  "mappings": {    "fields": {      // Default value, should match the name of the field within your collection that contains embeddings      "embedding": [        {          "dimensions": 1024,          "similarity": "euclidean",          "type": "knnVector"        }      ]    }  }}

The `dimensions` property should match the dimensionality of the embeddings you are using. For example, Cohere embeddings have 1024 dimensions, and OpenAI embeddings have 1536.

**Note:** By default the vector store expects an index name of `default`, an indexed collection field name of `embedding`, and a raw text field name of `text`. You should initialize the vector store with field names matching your collection schema as shown below.

Finally, proceed to build the index.

Usage[​](#usage "Direct link to Usage")
---------------------------------------

### Ingestion[​](#ingestion "Direct link to Ingestion")

    import { MongoDBAtlasVectorSearch } from "langchain/vectorstores/mongodb_atlas";import { CohereEmbeddings } from "langchain/embeddings/cohere";import { MongoClient } from "mongodb";export const run = async () => {  const client = new MongoClient(process.env.MONGODB_ATLAS_URI || "");  const namespace = "langchain.test";  const [dbName, collectionName] = namespace.split(".");  const collection = client.db(dbName).collection(collectionName);  await MongoDBAtlasVectorSearch.fromTexts(    ["Hello world", "Bye bye", "What's this?"],    [{ id: 2 }, { id: 1 }, { id: 3 }],    new CohereEmbeddings(),    {      collection,      indexName: "default", // The name of the Atlas search index. Defaults to "default"      textKey: "text", // The name of the collection field containing the raw content. Defaults to "text"      embeddingKey: "embedding", // The name of the collection field containing the embedded text. Defaults to "embedding"    }  );  await client.close();};

#### API Reference:

*   [MongoDBAtlasVectorSearch](/docs/api/vectorstores_mongodb_atlas/classes/MongoDBAtlasVectorSearch) from `langchain/vectorstores/mongodb_atlas`
*   [CohereEmbeddings](/docs/api/embeddings_cohere/classes/CohereEmbeddings) from `langchain/embeddings/cohere`

### Search[​](#search "Direct link to Search")

    import { MongoDBAtlasVectorSearch } from "langchain/vectorstores/mongodb_atlas";import { CohereEmbeddings } from "langchain/embeddings/cohere";import { MongoClient } from "mongodb";export const run = async () => {  const client = new MongoClient(process.env.MONGODB_ATLAS_URI || "");  const namespace = "langchain.test";  const [dbName, collectionName] = namespace.split(".");  const collection = client.db(dbName).collection(collectionName);  const vectorStore = new MongoDBAtlasVectorSearch(new CohereEmbeddings(), {    collection,    indexName: "default", // The name of the Atlas search index. Defaults to "default"    textKey: "text", // The name of the collection field containing the raw content. Defaults to "text"    embeddingKey: "embedding", // The name of the collection field containing the embedded text. Defaults to "embedding"  });  const resultOne = await vectorStore.similaritySearch("Hello world", 1);  console.log(resultOne);  await client.close();};

#### API Reference:

*   [MongoDBAtlasVectorSearch](/docs/api/vectorstores_mongodb_atlas/classes/MongoDBAtlasVectorSearch) from `langchain/vectorstores/mongodb_atlas`
*   [CohereEmbeddings](/docs/api/embeddings_cohere/classes/CohereEmbeddings) from `langchain/embeddings/cohere`