Qdrant
======

[Qdrant](https://qdrant.tech/) is a vector similarity search engine. It provides a production-ready service with a convenient API to store, search, and manage points - vectors with an additional payload.

Compatibility

Only available on Node.js.

Setup[​](#setup "Direct link to Setup")
---------------------------------------

1.  Run a Qdrant instance with Docker on your computer by following the [Qdrant setup instructions](https://qdrant.tech/documentation/install/).
    
2.  Install the Qdrant Node.js SDK.
    
    *   npm
    *   Yarn
    *   pnpm
    
        npm install -S @qdrant/js-client-rest
    
        yarn add @qdrant/js-client-rest
    
        pnpm add @qdrant/js-client-rest
    
3.  Setup Env variables for Qdrant before running the code
    
    3.1 OpenAI
    
        export OPENAI_API_KEY=YOUR_OPENAI_API_KEY_HEREexport QDRANT_URL=YOUR_QDRANT_URL_HERE # for example http://localhost:6333
    
    3.2 Azure OpenAI
    
        export AZURE_OPENAI_API_KEY=YOUR_AZURE_OPENAI_API_KEY_HEREexport AZURE_OPENAI_API_INSTANCE_NAME=YOUR_AZURE_OPENAI_INSTANCE_NAME_HEREexport AZURE_OPENAI_API_DEPLOYMENT_NAME=YOUR_AZURE_OPENAI_DEPLOYMENT_NAME_HEREexport AZURE_OPENAI_API_COMPLETIONS_DEPLOYMENT_NAME=YOUR_AZURE_OPENAI_COMPLETIONS_DEPLOYMENT_NAME_HEREexport AZURE_OPENAI_API_EMBEDDINGS_DEPLOYMENT_NAME=YOUR_AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT_NAME_HEREexport AZURE_OPENAI_API_VERSION=YOUR_AZURE_OPENAI_API_VERSION_HEREexport AZURE_OPENAI_BASE_PATH=YOUR_AZURE_OPENAI_BASE_PATH_HEREexport QDRANT_URL=YOUR_QDRANT_URL_HERE # for example http://localhost:6333
    

Usage[​](#usage "Direct link to Usage")
---------------------------------------

### Create a new index from texts[​](#create-a-new-index-from-texts "Direct link to Create a new index from texts")

    import { QdrantVectorStore } from "langchain/vectorstores/qdrant";import { OpenAIEmbeddings } from "langchain/embeddings/openai";// text sample from Godel, Escher, Bachconst vectorStore = await QdrantVectorStore.fromTexts(  [    `Tortoise: Labyrinth? Labyrinth? Could it Are we in the notorious LittleHarmonic Labyrinth of the dreaded Majotaur?`,    `Achilles: Yiikes! What is that?`,    `Tortoise: They say-although I person never believed it myself-that an I            Majotaur has created a tiny labyrinth sits in a pit in the middle of            it, waiting innocent victims to get lost in its fears complexity.            Then, when they wander and dazed into the center, he laughs and            laughs at them-so hard, that he laughs them to death!`,    `Achilles: Oh, no!`,    `Tortoise: But it's only a myth. Courage, Achilles.`,  ],  [{ id: 2 }, { id: 1 }, { id: 3 }, { id: 4 }, { id: 5 }],  new OpenAIEmbeddings(),  {    url: process.env.QDRANT_URL,    collectionName: "goldel_escher_bach",  });const response = await vectorStore.similaritySearch("scared", 2);console.log(response);/*[  Document { pageContent: 'Achilles: Oh, no!', metadata: {} },  Document {    pageContent: 'Achilles: Yiikes! What is that?',    metadata: { id: 1 }  }]*/

#### API Reference:

*   [QdrantVectorStore](/docs/api/vectorstores_qdrant/classes/QdrantVectorStore) from `langchain/vectorstores/qdrant`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`

### Create a new index from docs[​](#create-a-new-index-from-docs "Direct link to Create a new index from docs")

    import { QdrantVectorStore } from "langchain/vectorstores/qdrant";import { OpenAIEmbeddings } from "langchain/embeddings/openai";import { TextLoader } from "langchain/document_loaders/fs/text";// Create docs with a loaderconst loader = new TextLoader("src/document_loaders/example_data/example.txt");const docs = await loader.load();const vectorStore = await QdrantVectorStore.fromDocuments(  docs,  new OpenAIEmbeddings(),  {    url: process.env.QDRANT_URL,    collectionName: "a_test_collection",  });// Search for the most similar documentconst response = await vectorStore.similaritySearch("hello", 1);console.log(response);/*[  Document {    pageContent: 'Foo\nBar\nBaz\n\n',    metadata: { source: 'src/document_loaders/example_data/example.txt' }  }]*/

#### API Reference:

*   [QdrantVectorStore](/docs/api/vectorstores_qdrant/classes/QdrantVectorStore) from `langchain/vectorstores/qdrant`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`
*   [TextLoader](/docs/api/document_loaders_fs_text/classes/TextLoader) from `langchain/document_loaders/fs/text`

### Query docs from existing collection[​](#query-docs-from-existing-collection "Direct link to Query docs from existing collection")

    import { QdrantVectorStore } from "langchain/vectorstores/qdrant";import { OpenAIEmbeddings } from "langchain/embeddings/openai";const vectorStore = await QdrantVectorStore.fromExistingCollection(  new OpenAIEmbeddings(),  {    url: process.env.QDRANT_URL,    collectionName: "goldel_escher_bach",  });const response = await vectorStore.similaritySearch("scared", 2);console.log(response);/*[  Document { pageContent: 'Achilles: Oh, no!', metadata: {} },  Document {    pageContent: 'Achilles: Yiikes! What is that?',    metadata: { id: 1 }  }]*/

#### API Reference:

*   [QdrantVectorStore](/docs/api/vectorstores_qdrant/classes/QdrantVectorStore) from `langchain/vectorstores/qdrant`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`