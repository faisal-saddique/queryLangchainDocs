Chroma
======

> [Chroma](https://docs.trychroma.com/getting-started) is a AI-native open-source vector database focused on developer productivity and happiness. Chroma is licensed under Apache 2.0.

[![Discord](https://img.shields.io/discord/1073293645303795742)](https://discord.gg/MMeYNTmh3x)  [![License](https://img.shields.io/static/v1?label=license&message=Apache 2.0&color=white)](https://github.com/chroma-core/chroma/blob/master/LICENSE)  ![Integration Tests](https://github.com/chroma-core/chroma/actions/workflows/chroma-integration-test.yml/badge.svg?branch=main)

*   [Website](https://www.trychroma.com/)
*   [Documentation](https://docs.trychroma.com/)
*   [Twitter](https://twitter.com/trychroma)
*   [Discord](https://discord.gg/MMeYNTmh3x)

Setup[](#setup "Direct link to Setup")
---------------------------------------

1.  Run Chroma with Docker on your computer

    git clone git@github.com:chroma-core/chroma.gitdocker-compose up -d --build

2.  Install the Chroma JS SDK.

*   npm
*   Yarn
*   pnpm

    npm install -S chromadb

    yarn add chromadb

    pnpm add chromadb

Chroma is fully-typed, fully-tested and fully-documented.

Like any other database, you can:

*   `.add`
*   `.get`
*   `.update`
*   `.upsert`
*   `.delete`
*   `.peek`
*   and `.query` runs the similarity search.

View full docs at [docs](https://docs.trychroma.com/js_reference/Collection).

Usage, Index and query Documents[](#usage-index-and-query-documents "Direct link to Usage, Index and query Documents")
-----------------------------------------------------------------------------------------------------------------------

    import { Chroma } from "langchain/vectorstores/chroma";import { OpenAIEmbeddings } from "langchain/embeddings/openai";import { TextLoader } from "langchain/document_loaders/fs/text";// Create docs with a loaderconst loader = new TextLoader("src/document_loaders/example_data/example.txt");const docs = await loader.load();// Create vector store and index the docsconst vectorStore = await Chroma.fromDocuments(docs, new OpenAIEmbeddings(), {  collectionName: "a-test-collection",});// Search for the most similar documentconst response = await vectorStore.similaritySearch("hello", 1);console.log(response);/*[  Document {    pageContent: 'Foo\nBar\nBaz\n\n',    metadata: { source: 'src/document_loaders/example_data/example.txt' }  }]*/

#### API Reference:

*   [Chroma](/docs/api/vectorstores_chroma/classes/Chroma) from `langchain/vectorstores/chroma`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`
*   [TextLoader](/docs/api/document_loaders_fs_text/classes/TextLoader) from `langchain/document_loaders/fs/text`

Usage, Index and query texts[](#usage-index-and-query-texts "Direct link to Usage, Index and query texts")
-----------------------------------------------------------------------------------------------------------

    import { Chroma } from "langchain/vectorstores/chroma";import { OpenAIEmbeddings } from "langchain/embeddings/openai";// text sample from Godel, Escher, Bachconst vectorStore = await Chroma.fromTexts(  [    `Tortoise: Labyrinth? Labyrinth? Could it Are we in the notorious Little        Harmonic Labyrinth of the dreaded Majotaur?`,    "Achilles: Yiikes! What is that?",    `Tortoise: They say-although I person never believed it myself-that an I        Majotaur has created a tiny labyrinth sits in a pit in the middle of        it, waiting innocent victims to get lost in its fears complexity.        Then, when they wander and dazed into the center, he laughs and        laughs at them-so hard, that he laughs them to death!`,    "Achilles: Oh, no!",    "Tortoise: But it's only a myth. Courage, Achilles.",  ],  [{ id: 2 }, { id: 1 }, { id: 3 }],  new OpenAIEmbeddings(),  {    collectionName: "godel-escher-bach",  });const response = await vectorStore.similaritySearch("scared", 2);console.log(response);/*[  Document { pageContent: 'Achilles: Oh, no!', metadata: {} },  Document {    pageContent: 'Achilles: Yiikes! What is that?',    metadata: { id: 1 }  }]*/// You can also filter by metadataconst filteredResponse = await vectorStore.similaritySearch("scared", 2, {  id: 1,});console.log(filteredResponse);/*[  Document {    pageContent: 'Achilles: Yiikes! What is that?',    metadata: { id: 1 }  }]*/

#### API Reference:

*   [Chroma](/docs/api/vectorstores_chroma/classes/Chroma) from `langchain/vectorstores/chroma`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`

Usage, Query docs from existing collection[](#usage-query-docs-from-existing-collection "Direct link to Usage, Query docs from existing collection")
-----------------------------------------------------------------------------------------------------------------------------------------------------

    import { Chroma } from "langchain/vectorstores/chroma";import { OpenAIEmbeddings } from "langchain/embeddings/openai";const vectorStore = await Chroma.fromExistingCollection(  new OpenAIEmbeddings(),  { collectionName: "godel-escher-bach" });const response = await vectorStore.similaritySearch("scared", 2);console.log(response);/*[  Document { pageContent: 'Achilles: Oh, no!', metadata: {} },  Document {    pageContent: 'Achilles: Yiikes! What is that?',    metadata: { id: 1 }  }]*/

#### API Reference:

*   [Chroma](/docs/api/vectorstores_chroma/classes/Chroma) from `langchain/vectorstores/chroma`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`

Usage, delete docs[](#usage-delete-docs "Direct link to Usage, delete docs")
-----------------------------------------------------------------------------

    import { Chroma } from "langchain/vectorstores/chroma";import { OpenAIEmbeddings } from "langchain/embeddings/openai";const embeddings = new OpenAIEmbeddings();const vectorStore = new Chroma(embeddings, {  collectionName: "test-deletion",});const documents = [  {    pageContent: `Tortoise: Labyrinth? Labyrinth? Could it Are we in the notorious Little    Harmonic Labyrinth of the dreaded Majotaur?`,    metadata: {      speaker: "Tortoise",    },  },  {    pageContent: "Achilles: Yiikes! What is that?",    metadata: {      speaker: "Achilles",    },  },  {    pageContent: `Tortoise: They say-although I person never believed it myself-that an I    Majotaur has created a tiny labyrinth sits in a pit in the middle of    it, waiting innocent victims to get lost in its fears complexity.    Then, when they wander and dazed into the center, he laughs and    laughs at them-so hard, that he laughs them to death!`,    metadata: {      speaker: "Tortoise",    },  },  {    pageContent: "Achilles: Oh, no!",    metadata: {      speaker: "Achilles",    },  },  {    pageContent: "Tortoise: But it's only a myth. Courage, Achilles.",    metadata: {      speaker: "Tortoise",    },  },];// Also supports an additional {ids: []} parameter for upsertionconst ids = await vectorStore.addDocuments(documents);const response = await vectorStore.similaritySearch("scared", 2);console.log(response);/*[  Document { pageContent: 'Achilles: Oh, no!', metadata: {} },  Document {    pageContent: 'Achilles: Yiikes! What is that?',    metadata: { id: 1 }  }]*/// You can also pass a "filter" parameter insteadawait vectorStore.delete({ ids });const response2 = await vectorStore.similaritySearch("scared", 2);console.log(response2);/*  []*/

#### API Reference:

*   [Chroma](/docs/api/vectorstores_chroma/classes/Chroma) from `langchain/vectorstores/chroma`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`