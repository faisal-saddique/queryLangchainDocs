AI21
====

You can get started with AI21Labs' Jurassic family of models, as well as see a full list of available foundational models, by signing up for an API key [on their website](https://www.ai21.com/).

Here's an example of initializing an instance in LangChain.js:

    import { AI21 } from "langchain/llms/ai21";const model = new AI21({  ai21ApiKey: "YOUR_AI21_API_KEY", // Or set as process.env.AI21_API_KEY});const res = await model.call(`Translate "I love programming" into German.`);console.log({ res });/*  {    res: "\nIch liebe das Programmieren."  } */

#### API Reference:

*   [AI21](/docs/api/llms_ai21/classes/AI21) from `langchain/llms/ai21`