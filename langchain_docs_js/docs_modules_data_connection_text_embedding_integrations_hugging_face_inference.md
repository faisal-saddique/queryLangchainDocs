HuggingFace Inference
=====================

This Embeddings integration uses the HuggingFace Inference API to generate embeddings for a given text using by default the `sentence-transformers/distilbert-base-nli-mean-tokens` model. You can pass a different model name to the constructor to use a different model.

*   npm
*   Yarn
*   pnpm

    npm install @huggingface/inference@1

    yarn add @huggingface/inference@1

    pnpm add @huggingface/inference@1

    import { HuggingFaceInferenceEmbeddings } from "langchain/embeddings/hf";const embeddings = new HuggingFaceInferenceEmbeddings({  apiKey: "YOUR-API-KEY", // In Node.js defaults to process.env.HUGGINGFACEHUB_API_KEY});