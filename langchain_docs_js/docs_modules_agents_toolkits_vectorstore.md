VectorStore Agent Toolkit
=========================

This example shows how to load and use an agent with a vectorstore toolkit.

    import { OpenAI } from "langchain/llms/openai";import { HNSWLib } from "langchain/vectorstores/hnswlib";import { OpenAIEmbeddings } from "langchain/embeddings/openai";import { RecursiveCharacterTextSplitter } from "langchain/text_splitter";import * as fs from "fs";import {  VectorStoreToolkit,  createVectorStoreAgent,  VectorStoreInfo,} from "langchain/agents";const model = new OpenAI({ temperature: 0 });/* Load in the file we want to do question answering over */const text = fs.readFileSync("state_of_the_union.txt", "utf8");/* Split the text into chunks using character, not token, size */const textSplitter = new RecursiveCharacterTextSplitter({ chunkSize: 1000 });const docs = await textSplitter.createDocuments([text]);/* Create the vectorstore */const vectorStore = await HNSWLib.fromDocuments(docs, new OpenAIEmbeddings());/* Create the agent */const vectorStoreInfo: VectorStoreInfo = {  name: "state_of_union_address",  description: "the most recent state of the Union address",  vectorStore,};const toolkit = new VectorStoreToolkit(vectorStoreInfo, model);const agent = createVectorStoreAgent(model, toolkit);const input =  "What did biden say about Ketanji Brown Jackson is the state of the union address?";console.log(`Executing: ${input}`);const result = await agent.call({ input });console.log(`Got output ${result.output}`);console.log(  `Got intermediate steps ${JSON.stringify(result.intermediateSteps, null, 2)}`);

#### API Reference:

*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [HNSWLib](/docs/api/vectorstores_hnswlib/classes/HNSWLib) from `langchain/vectorstores/hnswlib`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`
*   [RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter) from `langchain/text_splitter`
*   [VectorStoreToolkit](/docs/api/agents/classes/VectorStoreToolkit) from `langchain/agents`
*   [createVectorStoreAgent](/docs/api/agents/functions/createVectorStoreAgent) from `langchain/agents`
*   [VectorStoreInfo](/docs/api/agents/interfaces/VectorStoreInfo) from `langchain/agents`