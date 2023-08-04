Contextual compression
======================

One challenge with retrieval is that usually you don't know the specific queries your document storage system will face when you ingest data into the system. This means that the information most relevant to a query may be buried in a document with a lot of irrelevant text. Passing that full document through your application can lead to more expensive LLM calls and poorer responses.

Contextual compression is meant to fix this. The idea is simple: instead of immediately returning retrieved documents as-is, you can compress them using the context of the given query, so that only the relevant information is returned. “Compressing” here refers to both compressing the contents of an individual document and filtering out documents wholesale.

To use the Contextual Compression Retriever, you'll need:

*   a base Retriever
*   a Document Compressor

The Contextual Compression Retriever passes queries to the base Retriever, takes the initial documents and passes them through the Document Compressor. The Document Compressor takes a list of Documents and shortens it by reducing the contents of Documents or dropping Documents altogether.

![](https://drive.google.com/uc?id=1CtNgWODXZudxAWSRiWgSGEoTNrUFT98v)

Get started[](#get-started "Direct link to Get started")
---------------------------------------------------------

Here's an example of how this works:

    import * as fs from "fs";import { OpenAI } from "langchain/llms/openai";import { RecursiveCharacterTextSplitter } from "langchain/text_splitter";import { RetrievalQAChain } from "langchain/chains";import { HNSWLib } from "langchain/vectorstores/hnswlib";import { OpenAIEmbeddings } from "langchain/embeddings/openai";import { ContextualCompressionRetriever } from "langchain/retrievers/contextual_compression";import { LLMChainExtractor } from "langchain/retrievers/document_compressors/chain_extract";const model = new OpenAI();const baseCompressor = LLMChainExtractor.fromLLM(model);const text = fs.readFileSync("state_of_the_union.txt", "utf8");const textSplitter = new RecursiveCharacterTextSplitter({ chunkSize: 1000 });const docs = await textSplitter.createDocuments([text]);// Create a vector store from the documents.const vectorStore = await HNSWLib.fromDocuments(docs, new OpenAIEmbeddings());const retriever = new ContextualCompressionRetriever({  baseCompressor,  baseRetriever: vectorStore.asRetriever(),});const chain = RetrievalQAChain.fromLLM(model, retriever);const res = await chain.call({  query: "What did the speaker say about Justice Breyer?",});console.log({ res });

#### API Reference:

*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter) from `langchain/text_splitter`
*   [RetrievalQAChain](/docs/api/chains/classes/RetrievalQAChain) from `langchain/chains`
*   [HNSWLib](/docs/api/vectorstores_hnswlib/classes/HNSWLib) from `langchain/vectorstores/hnswlib`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`
*   [ContextualCompressionRetriever](/docs/api/retrievers_contextual_compression/classes/ContextualCompressionRetriever) from `langchain/retrievers/contextual_compression`
*   [LLMChainExtractor](/docs/api/retrievers_document_compressors_chain_extract/classes/LLMChainExtractor) from `langchain/retrievers/document_compressors/chain_extract`