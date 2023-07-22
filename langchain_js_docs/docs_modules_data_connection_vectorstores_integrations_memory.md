`MemoryVectorStore`
===================

MemoryVectorStore is an in-memory, ephemeral vectorstore that stores embeddings in-memory and does an exact, linear search for the most similar embeddings. The default similarity metric is cosine similarity, but can be changed to any of the similarity metrics supported by [ml-distance](https://mljs.github.io/distance/modules/similarity.html).

Usage[​](#usage "Direct link to Usage")
---------------------------------------

### Create a new index from texts[​](#create-a-new-index-from-texts "Direct link to Create a new index from texts")

    import { MemoryVectorStore } from "langchain/vectorstores/memory";import { OpenAIEmbeddings } from "langchain/embeddings/openai";const vectorStore = await MemoryVectorStore.fromTexts(  ["Hello world", "Bye bye", "hello nice world"],  [{ id: 2 }, { id: 1 }, { id: 3 }],  new OpenAIEmbeddings());const resultOne = await vectorStore.similaritySearch("hello world", 1);console.log(resultOne);/*  [    Document {      pageContent: "Hello world",      metadata: { id: 2 }    }  ]*/

#### API Reference:

*   [MemoryVectorStore](/docs/api/vectorstores_memory/classes/MemoryVectorStore) from `langchain/vectorstores/memory`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`

### Create a new index from a loader[​](#create-a-new-index-from-a-loader "Direct link to Create a new index from a loader")

    import { MemoryVectorStore } from "langchain/vectorstores/memory";import { OpenAIEmbeddings } from "langchain/embeddings/openai";import { TextLoader } from "langchain/document_loaders/fs/text";// Create docs with a loaderconst loader = new TextLoader("src/document_loaders/example_data/example.txt");const docs = await loader.load();// Load the docs into the vector storeconst vectorStore = await MemoryVectorStore.fromDocuments(  docs,  new OpenAIEmbeddings());// Search for the most similar documentconst resultOne = await vectorStore.similaritySearch("hello world", 1);console.log(resultOne);/*  [    Document {      pageContent: "Hello world",      metadata: { id: 2 }    }  ]*/

#### API Reference:

*   [MemoryVectorStore](/docs/api/vectorstores_memory/classes/MemoryVectorStore) from `langchain/vectorstores/memory`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`
*   [TextLoader](/docs/api/document_loaders_fs_text/classes/TextLoader) from `langchain/document_loaders/fs/text`

### Use a custom similarity metric[​](#use-a-custom-similarity-metric "Direct link to Use a custom similarity metric")

    import { MemoryVectorStore } from "langchain/vectorstores/memory";import { OpenAIEmbeddings } from "langchain/embeddings/openai";import { similarity } from "ml-distance";const vectorStore = await MemoryVectorStore.fromTexts(  ["Hello world", "Bye bye", "hello nice world"],  [{ id: 2 }, { id: 1 }, { id: 3 }],  new OpenAIEmbeddings(),  { similarity: similarity.pearson });const resultOne = await vectorStore.similaritySearch("hello world", 1);console.log(resultOne);

#### API Reference:

*   [MemoryVectorStore](/docs/api/vectorstores_memory/classes/MemoryVectorStore) from `langchain/vectorstores/memory`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`