Cancelling requests
===================

You can cancel a request by passing a `signal` option when you call the model. For example, for OpenAI:

    import { OpenAI } from "langchain/llms/openai";const model = new OpenAI({ temperature: 1 });const controller = new AbortController();// Call `controller.abort()` somewhere to cancel the request.const res = await model.call(  "What would be a good company name a company that makes colorful socks?",  { signal: controller.signal });console.log(res);/*'\n\nSocktastic Colors'*/

#### API Reference:

*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`

Note, this will only cancel the outgoing request if the underlying provider exposes that option. LangChain will cancel the underlying request if possible, otherwise it will cancel the processing of the response.