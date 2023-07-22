HNSWLib
=======

Compatibility

Only available on Node.js.

HNSWLib is an in-memory vectorstore that can be saved to a file. It uses [HNSWLib](https://github.com/nmslib/hnswlib).

Setup[​](#setup "Direct link to Setup")
---------------------------------------

caution

**On Windows**, you might need to install [Visual Studio](https://visualstudio.microsoft.com/downloads/) first in order to properly build the `hnswlib-node` package.

You can install it with

*   npm
*   Yarn
*   pnpm

    npm install hnswlib-node

    yarn add hnswlib-node

    pnpm add hnswlib-node

Usage[​](#usage "Direct link to Usage")
---------------------------------------

### Create a new index from texts[​](#create-a-new-index-from-texts "Direct link to Create a new index from texts")

    import { HNSWLib } from "langchain/vectorstores/hnswlib";import { OpenAIEmbeddings } from "langchain/embeddings/openai";const vectorStore = await HNSWLib.fromTexts(  ["Hello world", "Bye bye", "hello nice world"],  [{ id: 2 }, { id: 1 }, { id: 3 }],  new OpenAIEmbeddings());const resultOne = await vectorStore.similaritySearch("hello world", 1);console.log(resultOne);

#### API Reference:

*   [HNSWLib](/docs/api/vectorstores_hnswlib/classes/HNSWLib) from `langchain/vectorstores/hnswlib`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`

### Create a new index from a loader[​](#create-a-new-index-from-a-loader "Direct link to Create a new index from a loader")

    import { HNSWLib } from "langchain/vectorstores/hnswlib";import { OpenAIEmbeddings } from "langchain/embeddings/openai";import { TextLoader } from "langchain/document_loaders/fs/text";// Create docs with a loaderconst loader = new TextLoader("src/document_loaders/example_data/example.txt");const docs = await loader.load();// Load the docs into the vector storeconst vectorStore = await HNSWLib.fromDocuments(docs, new OpenAIEmbeddings());// Search for the most similar documentconst result = await vectorStore.similaritySearch("hello world", 1);console.log(result);

#### API Reference:

*   [HNSWLib](/docs/api/vectorstores_hnswlib/classes/HNSWLib) from `langchain/vectorstores/hnswlib`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`
*   [TextLoader](/docs/api/document_loaders_fs_text/classes/TextLoader) from `langchain/document_loaders/fs/text`

### Save an index to a file and load it again[​](#save-an-index-to-a-file-and-load-it-again "Direct link to Save an index to a file and load it again")

    import { HNSWLib } from "langchain/vectorstores/hnswlib";import { OpenAIEmbeddings } from "langchain/embeddings/openai";// Create a vector store through any method, here from texts as an exampleconst vectorStore = await HNSWLib.fromTexts(  ["Hello world", "Bye bye", "hello nice world"],  [{ id: 2 }, { id: 1 }, { id: 3 }],  new OpenAIEmbeddings());// Save the vector store to a directoryconst directory = "your/directory/here";await vectorStore.save(directory);// Load the vector store from the same directoryconst loadedVectorStore = await HNSWLib.load(directory, new OpenAIEmbeddings());// vectorStore and loadedVectorStore are identicalconst result = await loadedVectorStore.similaritySearch("hello world", 1);console.log(result);

#### API Reference:

*   [HNSWLib](/docs/api/vectorstores_hnswlib/classes/HNSWLib) from `langchain/vectorstores/hnswlib`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`

### Filter documents[​](#filter-documents "Direct link to Filter documents")

    import { HNSWLib } from "langchain/vectorstores/hnswlib";import { OpenAIEmbeddings } from "langchain/embeddings/openai";const vectorStore = await HNSWLib.fromTexts(  ["Hello world", "Bye bye", "hello nice world"],  [{ id: 2 }, { id: 1 }, { id: 3 }],  new OpenAIEmbeddings());const result = await vectorStore.similaritySearch(  "hello world",  10,  (document) => document.metadata.id === 3);// only "hello nice world" will be returnedconsole.log(result);

#### API Reference:

*   [HNSWLib](/docs/api/vectorstores_hnswlib/classes/HNSWLib) from `langchain/vectorstores/hnswlib`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`