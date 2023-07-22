Retrievers
==========

A retriever is an interface that returns documents given an unstructured query. It is more general than a vector store. A retriever does not need to be able to store documents, only to return (or retrieve) it. Vector stores can be used as the backbone of a retriever, but there are other types of retrievers as well.

Get started[​](#get-started "Direct link to Get started")
---------------------------------------------------------

The public API of the `BaseRetriever` class in LangChain.js is as follows:

    export abstract class BaseRetriever {  abstract getRelevantDocuments(query: string): Promise<Document[]>;}

It's that simple! You can call `getRelevantDocuments` to retrieve documents relevant to a query, where "relevance" is defined by the specific retriever object you are calling.

Of course, we also help construct what we think useful Retrievers are. The main type of Retriever in LangChain is a vector store retriever. We will focus on that here.

**Note:** Before reading, it's important to understand [what a vector store is](/docs/modules/data_connection/vectorstores).

This example showcases question answering over documents. We have chosen this as the example for getting started because it nicely combines a lot of different elements (Text splitters, embeddings, vectorstores) and then also shows how to use them in a chain.

Question answering over documents consists of four steps:

1.  Create an index
2.  Create a Retriever from that index
3.  Create a question answering chain
4.  Ask questions!

Each of the steps has multiple sub steps and potential configurations, but we'll go through one common flow using HNSWLib, a local vector store. This assumes you're using Node, but you can swap in another integration if necessary.

First, install the required dependency:

*   npm
*   Yarn
*   pnpm

    npm install -S hnswlib-node

    yarn add hnswlib-node

    pnpm add hnswlib-node

You can download the `state_of_the_union.txt` file [here](https://github.com/hwchase17/langchain/blob/master/docs/extras/modules/state_of_the_union.txt).

    import { OpenAI } from "langchain/llms/openai";import { RetrievalQAChain } from "langchain/chains";import { HNSWLib } from "langchain/vectorstores/hnswlib";import { OpenAIEmbeddings } from "langchain/embeddings/openai";import { RecursiveCharacterTextSplitter } from "langchain/text_splitter";import * as fs from "fs";// Initialize the LLM to use to answer the question.const model = new OpenAI({});const text = fs.readFileSync("state_of_the_union.txt", "utf8");const textSplitter = new RecursiveCharacterTextSplitter({ chunkSize: 1000 });const docs = await textSplitter.createDocuments([text]);// Create a vector store from the documents.const vectorStore = await HNSWLib.fromDocuments(docs, new OpenAIEmbeddings());// Initialize a retriever wrapper around the vector storeconst vectorStoreRetriever = vectorStore.asRetriever();// Create a chain that uses the OpenAI LLM and HNSWLib vector store.const chain = RetrievalQAChain.fromLLM(model, vectorStoreRetriever);const res = await chain.call({  query: "What did the president say about Justice Breyer?",});console.log({ res });/*{  res: {    text: 'The president said that Justice Breyer was an Army veteran, Constitutional scholar,    and retiring Justice of the United States Supreme Court and thanked him for his service.'  }}*/

#### API Reference:

*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [RetrievalQAChain](/docs/api/chains/classes/RetrievalQAChain) from `langchain/chains`
*   [HNSWLib](/docs/api/vectorstores_hnswlib/classes/HNSWLib) from `langchain/vectorstores/hnswlib`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`
*   [RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter) from `langchain/text_splitter`

Let's walk through what's happening here.

1.  We first load a long text and split it into smaller documents using a text splitter. We then load those documents (which also embeds the documents using the passed `OpenAIEmbeddings` instance) into HNSWLib, our vector store, creating our index.
    
2.  Though we can query the vector store directly, we convert the vector store into a retriever to return retrieved documents in the right format for the question answering chain.
    
3.  We initialize a `RetrievalQAChain` with the `.fromLLM` method, which we'll call later in step 4.
    
4.  We ask questions!
    

See the individual sections for deeper dives on specific retrievers.