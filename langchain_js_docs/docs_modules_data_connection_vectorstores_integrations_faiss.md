Faiss
=====

Compatibility

Only available on Node.js.

[Faiss](https://github.com/facebookresearch/faiss) is a library for efficient similarity search and clustering of dense vectors.

Langchainjs supports using Faiss as a vectorstore that can be saved to file. It also provides the ability to read the saved file from [Python's implementation](https://python.langchain.com/en/latest/modules/indexes/vectorstores/examples/faiss.html#saving-and-loading).

Setup[​](#setup "Direct link to Setup")
---------------------------------------

Install the [faiss-node](https://github.com/ewfian/faiss-node), which is a Node.js bindings for [Faiss](https://github.com/facebookresearch/faiss).

*   npm
*   Yarn
*   pnpm

    npm install -S faiss-node

    yarn add faiss-node

    pnpm add faiss-node

To enable the ability to read the saved file from [Python's implementation](https://python.langchain.com/en/latest/modules/indexes/vectorstores/examples/faiss.html#saving-and-loading), the [pickleparser](https://github.com/ewfian/pickleparser) also needs to install.

*   npm
*   Yarn
*   pnpm

    npm install -S pickleparser

    yarn add pickleparser

    pnpm add pickleparser

Usage[​](#usage "Direct link to Usage")
---------------------------------------

### Create a new index from texts[​](#create-a-new-index-from-texts "Direct link to Create a new index from texts")

    import { FaissStore } from "langchain/vectorstores/faiss";import { OpenAIEmbeddings } from "langchain/embeddings/openai";export const run = async () => {  const vectorStore = await FaissStore.fromTexts(    ["Hello world", "Bye bye", "hello nice world"],    [{ id: 2 }, { id: 1 }, { id: 3 }],    new OpenAIEmbeddings()  );  const resultOne = await vectorStore.similaritySearch("hello world", 1);  console.log(resultOne);};

#### API Reference:

*   [FaissStore](/docs/api/vectorstores_faiss/classes/FaissStore) from `langchain/vectorstores/faiss`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`

### Create a new index from a loader[​](#create-a-new-index-from-a-loader "Direct link to Create a new index from a loader")

    import { FaissStore } from "langchain/vectorstores/faiss";import { OpenAIEmbeddings } from "langchain/embeddings/openai";import { TextLoader } from "langchain/document_loaders/fs/text";// Create docs with a loaderconst loader = new TextLoader("src/document_loaders/example_data/example.txt");const docs = await loader.load();// Load the docs into the vector storeconst vectorStore = await FaissStore.fromDocuments(  docs,  new OpenAIEmbeddings());// Search for the most similar documentconst resultOne = await vectorStore.similaritySearch("hello world", 1);console.log(resultOne);

#### API Reference:

*   [FaissStore](/docs/api/vectorstores_faiss/classes/FaissStore) from `langchain/vectorstores/faiss`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`
*   [TextLoader](/docs/api/document_loaders_fs_text/classes/TextLoader) from `langchain/document_loaders/fs/text`

### Save an index to file and load it again[​](#save-an-index-to-file-and-load-it-again "Direct link to Save an index to file and load it again")

    import { FaissStore } from "langchain/vectorstores/faiss";import { OpenAIEmbeddings } from "langchain/embeddings/openai";// Create a vector store through any method, here from texts as an exampleconst vectorStore = await FaissStore.fromTexts(  ["Hello world", "Bye bye", "hello nice world"],  [{ id: 2 }, { id: 1 }, { id: 3 }],  new OpenAIEmbeddings());// Save the vector store to a directoryconst directory = "your/directory/here";await vectorStore.save(directory);// Load the vector store from the same directoryconst loadedVectorStore = await FaissStore.load(  directory,  new OpenAIEmbeddings());// vectorStore and loadedVectorStore are identicalconst result = await loadedVectorStore.similaritySearch("hello world", 1);console.log(result);

#### API Reference:

*   [FaissStore](/docs/api/vectorstores_faiss/classes/FaissStore) from `langchain/vectorstores/faiss`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`

### Load the saved file from [Python's implementation](https://python.langchain.com/en/latest/modules/indexes/vectorstores/examples/faiss.html#saving-and-loading)[​](#load-the-saved-file-from-pythons-implementation "Direct link to load-the-saved-file-from-pythons-implementation")

    import { FaissStore } from "langchain/vectorstores/faiss";import { OpenAIEmbeddings } from "langchain/embeddings/openai";// The directory of data saved from Pythonconst directory = "your/directory/here";// Load the vector store from the directoryconst loadedVectorStore = await FaissStore.loadFromPython(  directory,  new OpenAIEmbeddings());// Search for the most similar documentconst result = await loadedVectorStore.similaritySearch("test", 2);console.log("result", result);

#### API Reference:

*   [FaissStore](/docs/api/vectorstores_faiss/classes/FaissStore) from `langchain/vectorstores/faiss`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`