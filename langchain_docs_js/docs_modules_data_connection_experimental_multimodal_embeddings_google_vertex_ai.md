Google Vertex AI
================

Experimental

This API is new and may change in future LangChainJS versions.

The `GoogleVertexAIMultimodalEmbeddings` class provides additional methods that are parallels to the `embedDocuments()` and `embedQuery()` methods:

*   `embedImage()` and `embedImageQuery()` take node `Buffer` objects that are expected to contain an image.
*   `embedMedia()` and `embedMediaQuery()` take an object that contain a `text` string field, an `image` Buffer field, or both and returns a similarly constructed object containing the respective vectors.

**Note:** The Google Vertex AI embeddings models have different vector sizes than OpenAI's standard model, so some vector stores may not handle them correctly.

*   The `textembedding-gecko` model in `GoogleVertexAIEmbeddings` provides 768 dimensions.
*   The `multimodalembedding@001` model in `GoogleVertexAIMultimodalEmbeddings` provides 1408 dimensions.

Setup[](#setup "Direct link to Setup")
---------------------------------------

The Vertex AI implementation is meant to be used in Node.js and not directly in a browser, since it requires a service account to use.

Before running this code, you should make sure the Vertex AI API is enabled for the relevant project in your Google Cloud dashboard and that you've authenticated to Google Cloud using one of these methods:

*   You are logged into an account (using `gcloud auth application-default login`) permitted to that project.
*   You are running on a machine using a service account that is permitted to the project.
*   You have downloaded the credentials for a service account that is permitted to the project and set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of this file.

*   npm
*   Yarn
*   pnpm

    npm install google-auth-library

    yarn add google-auth-library

    pnpm add google-auth-library

Usage[](#usage "Direct link to Usage")
---------------------------------------

Here's a basic example that shows how to embed image queries:

    import fs from "fs";import { GoogleVertexAIMultimodalEmbeddings } from "langchain/experimental/multimodal_embeddings/googlevertexai";const model = new GoogleVertexAIMultimodalEmbeddings();// Load the image into a buffer to get the embedding of itconst img = fs.readFileSync("/path/to/file.jpg");const imgEmbedding = await model.embedImageQuery(img);console.log({ imgEmbedding });// You can also get text embeddingsconst textEmbedding = await model.embedQuery(  "What would be a good company name for a company that makes colorful socks?");console.log({ textEmbedding });

#### API Reference:

*   [GoogleVertexAIMultimodalEmbeddings](/docs/api/experimental_multimodal_embeddings_googlevertexai/classes/GoogleVertexAIMultimodalEmbeddings) from `langchain/experimental/multimodal_embeddings/googlevertexai`

Advanced usage[](#advanced-usage "Direct link to Advanced usage")
------------------------------------------------------------------

Here's a more advanced example that shows how to integrate these new embeddings with a LangChain vector store.

    import fs from "fs";import { GoogleVertexAIMultimodalEmbeddings } from "langchain/experimental/multimodal_embeddings/googlevertexai";import { FaissStore } from "langchain/vectorstores/faiss";import { Document } from "langchain/document";const embeddings = new GoogleVertexAIMultimodalEmbeddings();const vectorStore = await FaissStore.fromTexts(  ["dog", "cat", "horse", "seagull"],  [{ id: 2 }, { id: 1 }, { id: 3 }, { id: 4 }],  embeddings);const img = fs.readFileSync("parrot.jpeg");const vectors: number[] = await embeddings.embedImageQuery(img);const document = new Document({  pageContent: img.toString("base64"),  // Metadata is optional but helps track what kind of document is being retrieved  metadata: {    id: 5,    mediaType: "image",  },});// Add the image embedding vectors to the vector store directlyawait vectorStore.addVectors([vectors], [document]);// Use a similar image to the one just addedconst img2 = fs.readFileSync("parrot-icon.png");const vectors2: number[] = await embeddings.embedImageQuery(img2);// Use the lower level, direct APIconst resultTwo = await vectorStore.similaritySearchVectorWithScore(  vectors2,  2);console.log(JSON.stringify(resultTwo, null, 2));/*  [    [      Document {        pageContent: '<BASE64 ENCODED IMAGE DATA>'        metadata: {          id: 5,          mediaType: "image"        }      },      0.8931522965431213    ],    [      Document {        pageContent: 'seagull',        metadata: {          id: 4        }      },      1.9188631772994995    ]  ]*/

#### API Reference:

*   [GoogleVertexAIMultimodalEmbeddings](/docs/api/experimental_multimodal_embeddings_googlevertexai/classes/GoogleVertexAIMultimodalEmbeddings) from `langchain/experimental/multimodal_embeddings/googlevertexai`
*   [FaissStore](/docs/api/vectorstores_faiss/classes/FaissStore) from `langchain/vectorstores/faiss`
*   [Document](/docs/api/document/classes/Document) from `langchain/document`