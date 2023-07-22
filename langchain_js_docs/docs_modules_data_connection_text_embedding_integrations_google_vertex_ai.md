Google Vertex AI
================

The `GoogleVertexAIEmbeddings` class uses Google's Vertex AI PaLM models to generate embeddings for a given text.

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

    import { GoogleVertexAIEmbeddings } from "langchain/embeddings/googlevertexai";export const run = async () => {  const model = new GoogleVertexAIEmbeddings();  const res = await model.embedQuery(    "What would be a good company name for a company that makes colorful socks?"  );  console.log({ res });};

#### API Reference:

*   [GoogleVertexAIEmbeddings](/docs/api/embeddings_googlevertexai/classes/GoogleVertexAIEmbeddings) from `langchain/embeddings/googlevertexai`

**Note:** The default Google Vertex AI embeddings model, `textembedding-gecko`, has a different number of dimensions than OpenAI's `text-embedding-ada-002` model and may not be supported by all vector store providers.