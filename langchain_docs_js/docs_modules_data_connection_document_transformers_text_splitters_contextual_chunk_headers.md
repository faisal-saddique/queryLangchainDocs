Contextual chunk headers
========================

Consider a scenario where you want to store a large, arbitrary collection of documents in a vector store and perform Q&A tasks on them. Simply splitting documents with overlapping text may not provide sufficient context for LLMs to determine if multiple chunks are referencing the same information, or how to resolve information from contradictory sources.

Tagging each document with metadata is a solution if you know what to filter against, but you may not know ahead of time exactly what kind of queries your vector store will be expected to handle. Including additional contextual information directly in each chunk in the form of headers can help deal with arbitrary queries.

Here's an example:

    import { OpenAI } from "langchain/llms/openai";import { RetrievalQAChain, loadQAStuffChain } from "langchain/chains";import { CharacterTextSplitter } from "langchain/text_splitter";import { OpenAIEmbeddings } from "langchain/embeddings/openai";import { HNSWLib } from "langchain/vectorstores/hnswlib";const splitter = new CharacterTextSplitter({  chunkSize: 1536,  chunkOverlap: 200,});const jimDocs = await splitter.createDocuments(  [`My favorite color is blue.`],  [],  {    chunkHeader: `DOCUMENT NAME: Jim Interview\n\n---\n\n`,    appendChunkOverlapHeader: true,  });const pamDocs = await splitter.createDocuments(  [`My favorite color is red.`],  [],  {    chunkHeader: `DOCUMENT NAME: Pam Interview\n\n---\n\n`,    appendChunkOverlapHeader: true,  });const vectorStore = await HNSWLib.fromDocuments(  jimDocs.concat(pamDocs),  new OpenAIEmbeddings());const model = new OpenAI({ temperature: 0 });const chain = new RetrievalQAChain({  combineDocumentsChain: loadQAStuffChain(model),  retriever: vectorStore.asRetriever(),  returnSourceDocuments: true,});const res = await chain.call({  query: "What is Pam's favorite color?",});console.log(JSON.stringify(res, null, 2));/*  {    "text": " Red.",    "sourceDocuments": [      {        "pageContent": "DOCUMENT NAME: Pam Interview\n\n---\n\nMy favorite color is red.",        "metadata": {          "loc": {            "lines": {              "from": 1,              "to": 1            }          }        }      },      {        "pageContent": "DOCUMENT NAME: Jim Interview\n\n---\n\nMy favorite color is blue.",        "metadata": {          "loc": {            "lines": {              "from": 1,              "to": 1            }          }        }      }    ]  }*/

#### API Reference:

*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [RetrievalQAChain](/docs/api/chains/classes/RetrievalQAChain) from `langchain/chains`
*   [loadQAStuffChain](/docs/api/chains/functions/loadQAStuffChain) from `langchain/chains`
*   [CharacterTextSplitter](/docs/api/text_splitter/classes/CharacterTextSplitter) from `langchain/text_splitter`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`
*   [HNSWLib](/docs/api/vectorstores_hnswlib/classes/HNSWLib) from `langchain/vectorstores/hnswlib`

;