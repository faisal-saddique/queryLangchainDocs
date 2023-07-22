Cohere
======

LangChain.js supports Cohere LLMs. Here's an example:

*   npm
*   Yarn
*   pnpm

    npm install cohere-ai

    yarn add cohere-ai

    pnpm add cohere-ai

    import { Cohere } from "langchain/llms/cohere";const model = new Cohere({  maxTokens: 20,  apiKey: "YOUR-API-KEY", // In Node.js defaults to process.env.COHERE_API_KEY});const res = await model.call(  "What would be a good company name a company that makes colorful socks?");console.log({ res });