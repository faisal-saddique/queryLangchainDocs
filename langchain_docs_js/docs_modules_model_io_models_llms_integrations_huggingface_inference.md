HuggingFaceInference
====================

Here's an example of calling a HugggingFaceInference model as an LLM:

*   npm
*   Yarn
*   pnpm

    npm install @huggingface/inference@1

    yarn add @huggingface/inference@1

    pnpm add @huggingface/inference@1

    import { HuggingFaceInference } from "langchain/llms/hf";const model = new HuggingFaceInference({  model: "gpt2",  apiKey: "YOUR-API-KEY", // In Node.js defaults to process.env.HUGGINGFACEHUB_API_KEY});const res = await model.call("1 + 1 =");console.log({ res });