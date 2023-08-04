Contextual Compression Retriever
================================

A Contextual Compression Retriever is designed to improve the answers returned from vector store document similarity searches by better taking into account the context from the query.

It wraps another retriever, and uses a Document Compressor as an intermediate step after the initial similarity search that removes information irrelevant to the initial query from the retrieved documents. This reduces the amount of distraction a subsequent chain has to deal with when parsing the retrieved documents and making its final judgements.

Usage[](#usage "Direct link to Usage")
---------------------------------------

This example shows how to intialize a `ContextualCompressionRetriever` with a vector store and a document compressor:

    import * as fs from "fs";import { OpenAI } from "langchain/llms/openai";import { RecursiveCharacterTextSplitter } from "langchain/text_splitter";import { RetrievalQAChain } from "langchain/chains";import { HNSWLib } from "langchain/vectorstores/hnswlib";import { OpenAIEmbeddings } from "langchain/embeddings/openai";import { ContextualCompressionRetriever } from "langchain/retrievers/contextual_compression";import { LLMChainExtractor } from "langchain/retrievers/document_compressors/chain_extract";const model = new OpenAI();const baseCompressor = LLMChainExtractor.fromLLM(model);const text = fs.readFileSync("state_of_the_union.txt", "utf8");const textSplitter = new RecursiveCharacterTextSplitter({ chunkSize: 1000 });const docs = await textSplitter.createDocuments([text]);// Create a vector store from the documents.const vectorStore = await HNSWLib.fromDocuments(docs, new OpenAIEmbeddings());const retriever = new ContextualCompressionRetriever({  baseCompressor,  baseRetriever: vectorStore.asRetriever(),});const chain = RetrievalQAChain.fromLLM(model, retriever);const res = await chain.call({  query: "What did the speaker say about Justice Breyer?",});console.log({ res });

#### API Reference:

*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter) from `langchain/text_splitter`
*   [RetrievalQAChain](/docs/api/chains/classes/RetrievalQAChain) from `langchain/chains`
*   [HNSWLib](/docs/api/vectorstores_hnswlib/classes/HNSWLib) from `langchain/vectorstores/hnswlib`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`
*   [ContextualCompressionRetriever](/docs/api/retrievers_contextual_compression/classes/ContextualCompressionRetriever) from `langchain/retrievers/contextual_compression`
*   [LLMChainExtractor](/docs/api/retrievers_document_compressors_chain_extract/classes/LLMChainExtractor) from `langchain/retrievers/document_compressors/chain_extract`