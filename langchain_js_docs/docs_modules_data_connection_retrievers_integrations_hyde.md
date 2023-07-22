HyDE Retriever
==============

This example shows how to use the HyDE Retriever, which implements Hypothetical Document Embeddings (HyDE) as described in [this paper](https://arxiv.org/abs/2212.10496).

At a high level, HyDE is an embedding technique that takes queries, generates a hypothetical answer, and then embeds that generated document and uses that as the final example.

In order to use HyDE, we therefore need to provide a base embedding model, as well as an LLM that can be used to generate those documents. By default, the HyDE class comes with some default prompts to use (see the paper for more details on them), but we can also create our own, which should have a single input variable `{question}`.

Usage[​](#usage "Direct link to Usage")
---------------------------------------

    import { OpenAI } from "langchain/llms/openai";import { OpenAIEmbeddings } from "langchain/embeddings/openai";import { MemoryVectorStore } from "langchain/vectorstores/memory";import { HydeRetriever } from "langchain/retrievers/hyde";import { Document } from "langchain/document";const embeddings = new OpenAIEmbeddings();const vectorStore = new MemoryVectorStore(embeddings);const llm = new OpenAI();const retriever = new HydeRetriever({  vectorStore,  llm,  k: 1,});await vectorStore.addDocuments(  [    "My name is John.",    "My name is Bob.",    "My favourite food is pizza.",    "My favourite food is pasta.",  ].map((pageContent) => new Document({ pageContent })));const results = await retriever.getRelevantDocuments(  "What is my favourite food?");console.log(results);/*[  Document { pageContent: 'My favourite food is pasta.', metadata: {} }]*/

#### API Reference:

*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`
*   [MemoryVectorStore](/docs/api/vectorstores_memory/classes/MemoryVectorStore) from `langchain/vectorstores/memory`
*   [HydeRetriever](/docs/api/retrievers_hyde/classes/HydeRetriever) from `langchain/retrievers/hyde`
*   [Document](/docs/api/document/classes/Document) from `langchain/document`