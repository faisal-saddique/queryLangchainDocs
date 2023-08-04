Adding a timeout
================

By default, LangChain will wait indefinitely for a response from the model provider. If you want to add a timeout, you can pass a `timeout` option, in milliseconds, when you call the model. For example, for OpenAI:

    import { OpenAI } from "langchain/llms/openai";const model = new OpenAI({ temperature: 1 });const resA = await model.call(  "What would be a good company name a company that makes colorful socks?",  { timeout: 1000 } // 1s timeout);console.log({ resA });// '\n\nSocktastic Colors' }

#### API Reference:

*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`