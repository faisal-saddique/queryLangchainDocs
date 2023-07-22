Time-Weighted Retriever
=======================

A Time-Weighted Retriever is a retriever that takes into account recency in addition to similarity. The scoring algorithm is:

    let score = (1.0 - this.decayRate) ** hoursPassed + vectorRelevance;

Notably, `hoursPassed` above refers to the time since the object in the retriever was last accessed, not since it was created. This means that frequently accessed objects remain "fresh" and score higher.

`this.decayRate` is a configurable decimal number between 0 and 1. A lower number means that documents will be "remembered" for longer, while a higher number strongly weights more recently accessed documents.

Note that setting a decay rate of exactly 0 or 1 makes `hoursPassed` irrelevant and makes this retriever equivalent to a standard vector lookup.

Usage[​](#usage "Direct link to Usage")
---------------------------------------

This example shows how to intialize a `TimeWeightedVectorStoreRetriever` with a vector store. It is important to note that due to required metadata, all documents must be added to the backing vector store using the `addDocuments` method on the **retriever**, not the vector store itself.

    import { TimeWeightedVectorStoreRetriever } from "langchain/retrievers/time_weighted";import { MemoryVectorStore } from "langchain/vectorstores/memory";import { OpenAIEmbeddings } from "langchain/embeddings/openai";const vectorStore = new MemoryVectorStore(new OpenAIEmbeddings());const retriever = new TimeWeightedVectorStoreRetriever({  vectorStore,  memoryStream: [],  searchKwargs: 2,});const documents = [  "My name is John.",  "My name is Bob.",  "My favourite food is pizza.",  "My favourite food is pasta.",  "My favourite food is sushi.",].map((pageContent) => ({ pageContent, metadata: {} }));// All documents must be added using this method on the retriever (not the vector store!)// so that the correct access history metadata is populatedawait retriever.addDocuments(documents);const results1 = await retriever.getRelevantDocuments(  "What is my favourite food?");console.log(results1);/*[  Document { pageContent: 'My favourite food is pasta.', metadata: {} }] */const results2 = await retriever.getRelevantDocuments(  "What is my favourite food?");console.log(results2);/*[  Document { pageContent: 'My favourite food is pasta.', metadata: {} }] */

#### API Reference:

*   [TimeWeightedVectorStoreRetriever](/docs/api/retrievers_time_weighted/classes/TimeWeightedVectorStoreRetriever) from `langchain/retrievers/time_weighted`
*   [MemoryVectorStore](/docs/api/vectorstores_memory/classes/MemoryVectorStore) from `langchain/vectorstores/memory`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`