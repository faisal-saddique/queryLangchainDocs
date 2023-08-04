Cohere
======

The `CohereEmbeddings` class uses the Cohere API to generate embeddings for a given text.

*   npm
*   Yarn
*   pnpm

    npm install cohere-ai

    yarn add cohere-ai

    pnpm add cohere-ai

    import { CohereEmbeddings } from "langchain/embeddings/cohere";const embeddings = new CohereEmbeddings({  apiKey: "YOUR-API-KEY", // In Node.js defaults to process.env.COHERE_API_KEY});