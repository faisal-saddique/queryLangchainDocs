Vector stores
=============

One of the most common ways to store and search over unstructured data is to embed it and store the resulting embedding vectors, and then at query time to embed the unstructured query and retrieve the embedding vectors that are 'most similar' to the embedded query. A vector store takes care of storing embedded data and performing vector search for you.

Get started[​](#get-started "Direct link to Get started")
---------------------------------------------------------

This walkthrough showcases basic functionality related to VectorStores. A key part of working with vector stores is creating the vector to put in them, which is usually created via embeddings. Therefore, it is recommended that you familiarize yourself with the [text embedding model](/docs/modules/data_connection/text_embedding/) interfaces before diving into this.

This walkthrough uses a basic, unoptimized implementation called MemoryVectorStore that stores embeddings in-memory and does an exact, linear search for the most similar embeddings.

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

Here is the current base interface all vector stores share:

    interface VectorStore {  /**   * Add more documents to an existing VectorStore.   * Some providers support additional parameters, e.g. to associate custom ids   * with added documents or to change the batch size of bulk inserts.   * Returns an array of ids for the documents or nothing.   */  addDocuments(    documents: Document[],    options?: Record<string, any>  ): Promise<string[] | void>;  /**   * Search for the most similar documents to a query   */  similaritySearch(    query: string,    k?: number,    filter?: object | undefined  ): Promise<Document[]>;  /**   * Search for the most similar documents to a query,   * and return their similarity score   */  similaritySearchWithScore(    query: string,    k = 4,    filter: object | undefined = undefined  ): Promise<[object, number][]>;  /**   * Turn a VectorStore into a Retriever   */  asRetriever(k?: number): BaseRetriever;  /**   * Delete embedded documents from the vector store matching the passed in parameter.   * Not supported by every provider.   */  delete(params?: Record<string, any>): Promise<void>;  /**   * Advanced: Add more documents to an existing VectorStore,   * when you already have their embeddings   */  addVectors(    vectors: number[][],    documents: Document[],    options?: Record<string, any>  ): Promise<string[] | void>;  /**   * Advanced: Search for the most similar documents to a query,   * when you already have the embedding of the query   */  similaritySearchVectorWithScore(    query: number[],    k: number,    filter?: object  ): Promise<[Document, number][]>;}

You can create a vector store from a list of [Documents](/docs/api/document/classes/Document), or from a list of texts and their corresponding metadata. You can also create a vector store from an existing index, the signature of this method depends on the vector store you're using, check the documentation of the vector store you're interested in.

    abstract class BaseVectorStore implements VectorStore {  static fromTexts(    texts: string[],    metadatas: object[] | object,    embeddings: Embeddings,    dbConfig: Record<string, any>  ): Promise<VectorStore>;  static fromDocuments(    docs: Document[],    embeddings: Embeddings,    dbConfig: Record<string, any>  ): Promise<VectorStore>;}

Which one to pick?[​](#which-one-to-pick "Direct link to Which one to pick?")
-----------------------------------------------------------------------------

Here's a quick guide to help you pick the right vector store for your use case:

*   If you're after something that can just run inside your Node.js application, in-memory, without any other servers to stand up, then go for [HNSWLib](/docs/modules/data_connection/vectorstores/integrations/hnswlib), [Faiss](/docs/modules/data_connection/vectorstores/integrations/faiss), or [LanceDB](/docs/modules/data_connection/vectorstores/integrations/lancedb)
*   If you're looking for something that can run in-memory in browser-like environments, then go for [MemoryVectorStore](/docs/modules/data_connection/vectorstores/integrations/memory)
*   If you come from Python and you were looking for something similar to FAISS, try [HNSWLib](/docs/modules/data_connection/vectorstores/integrations/hnswlib) or [Faiss](/docs/modules/data_connection/vectorstores/integrations/faiss)
*   If you're looking for an open-source full-featured vector database that you can run locally in a docker container, then go for [Chroma](/docs/modules/data_connection/vectorstores/integrations/chroma)
*   If you're looking for an open-source production-ready vector database that you can run locally (in a docker container) or hosted in the cloud, then go for [Weaviate](/docs/modules/data_connection/vectorstores/integrations/weaviate).
*   If you're using Supabase already then look at the [Supabase](/docs/modules/data_connection/vectorstores/integrations/supabase) vector store to use the same Postgres database for your embeddings too
*   If you're looking for a production-ready vector store you don't have to worry about hosting yourself, then go for [Pinecone](/docs/modules/data_connection/vectorstores/integrations/pinecone)
*   If you are already utilizing SingleStore, or if you find yourself in need of a distributed, high-performance database, you might want to consider the [SingleStore](/docs/modules/data_connection/vectorstores/integrations/singlestore) vector store.
*   If you are looking for an online MPP (Massively Parallel Processing) data warehousing service, you might want to consider the [AnalyticDB](/docs/modules/data_connection/vectorstores/integrations/analyticdb) vector store.