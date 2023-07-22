Elasticsearch
=============

Compatibility

Only available on Node.js.

[Elasticsearch](https://github.com/elastic/elasticsearch) is a distributed, RESTful search engine optimized for speed and relevance on production-scale workloads. It supports also vector search using the [k-nearest neighbor](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) (kNN) algorithm and also [custom models for Natural Language Processing](https://www.elastic.co/blog/how-to-deploy-nlp-text-embeddings-and-vector-search) (NLP). You can read more about the support of vector search in Elasticsearch [here](https://www.elastic.co/guide/en/elasticsearch/reference/current/knn-search.html).

LangChain.js accepts [@elastic/elasticsearch](https://github.com/elastic/elasticsearch-js) as the client for Elasticsearch vectorstore.

Setup[​](#setup "Direct link to Setup")
---------------------------------------

*   npm
*   Yarn
*   pnpm

    npm install -S @elastic/elasticsearch

    yarn add @elastic/elasticsearch

    pnpm add @elastic/elasticsearch

You'll also need to have an Elasticsearch instance running. You can use the [official Docker image](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html) to get started, or you can use [Elastic Cloud](https://www.elastic.co/cloud/) the official cloud service provided by Elastic.

For connecting to Elastic Cloud you can read the documentation reported [here](https://www.elastic.co/guide/en/kibana/current/api-keys.html) for obtaining an API key.

Example: index docs, vector search and LLM integration[​](#example-index-docs-vector-search-and-llm-integration "Direct link to Example: index docs, vector search and LLM integration")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Below is an example that indexes 4 documents in Elasticsearch, runs a vector search query, and finally uses an LLM to answer a question in natural language based on the retrieved documents.

    import { Client, ClientOptions } from "@elastic/elasticsearch";import { Document } from "langchain/document";import { OpenAI } from "langchain/llms/openai";import { OpenAIEmbeddings } from "langchain/embeddings/openai";import {  ElasticClientArgs,  ElasticVectorSearch,} from "langchain/vectorstores/elasticsearch";import { VectorDBQAChain } from "langchain/chains";// to run this first run Elastic's docker-container with `docker-compose up -d --build`export async function run() {  const config: ClientOptions = {    node: process.env.ELASTIC_URL ?? "http://127.0.0.1:9200",  };  if (process.env.ELASTIC_API_KEY) {    config.auth = {      apiKey: process.env.ELASTIC_API_KEY,    };  } else if (process.env.ELASTIC_USERNAME && process.env.ELASTIC_PASSWORD) {    config.auth = {      username: process.env.ELASTIC_USERNAME,      password: process.env.ELASTIC_PASSWORD,    };  }  const clientArgs: ElasticClientArgs = {    client: new Client(config),    indexName: process.env.ELASTIC_INDEX ?? "test_vectorstore",  };  // Index documents  const docs = [    new Document({      metadata: { foo: "bar" },      pageContent: "Elasticsearch is a powerful vector db",    }),    new Document({      metadata: { foo: "bar" },      pageContent: "the quick brown fox jumped over the lazy dog",    }),    new Document({      metadata: { baz: "qux" },      pageContent: "lorem ipsum dolor sit amet",    }),    new Document({      metadata: { baz: "qux" },      pageContent:        "Elasticsearch a distributed, RESTful search engine optimized for speed and relevance on production-scale workloads.",    }),  ];  const embeddings = new OpenAIEmbeddings(undefined, {    baseOptions: { temperature: 0 },  });  // await ElasticVectorSearch.fromDocuments(docs, embeddings, clientArgs);  const vectorStore = new ElasticVectorSearch(embeddings, clientArgs);  // Also supports an additional {ids: []} parameter for upsertion  const ids = await vectorStore.addDocuments(docs);  /* Search the vector DB independently with meta filters */  const results = await vectorStore.similaritySearch("fox jump", 1);  console.log(JSON.stringify(results, null, 2));  /* [        {          "pageContent": "the quick brown fox jumped over the lazy dog",          "metadata": {            "foo": "bar"          }        }    ]  */  /* Use as part of a chain (currently no metadata filters) for LLM query */  const model = new OpenAI();  const chain = VectorDBQAChain.fromLLM(model, vectorStore, {    k: 1,    returnSourceDocuments: true,  });  const response = await chain.call({ query: "What is Elasticsearch?" });  console.log(JSON.stringify(response, null, 2));  /*    {      "text": " Elasticsearch is a distributed, RESTful search engine optimized for speed and relevance on production-scale workloads.",      "sourceDocuments": [        {          "pageContent": "Elasticsearch a distributed, RESTful search engine optimized for speed and relevance on production-scale workloads.",          "metadata": {            "baz": "qux"          }        }      ]    }    */  await vectorStore.delete({ ids });  const response2 = await chain.call({ query: "What is Elasticsearch?" });  console.log(JSON.stringify(response2, null, 2));  /*    []  */}

#### API Reference:

*   [Document](/docs/api/document/classes/Document) from `langchain/document`
*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`
*   [ElasticClientArgs](/docs/api/vectorstores_elasticsearch/interfaces/ElasticClientArgs) from `langchain/vectorstores/elasticsearch`
*   [ElasticVectorSearch](/docs/api/vectorstores_elasticsearch/classes/ElasticVectorSearch) from `langchain/vectorstores/elasticsearch`
*   [VectorDBQAChain](/docs/api/chains/classes/VectorDBQAChain) from `langchain/chains`