Cancelling requests
===================

You can cancel a request by passing a `signal` option when you call the model. For example, for OpenAI:

    import { ChatOpenAI } from "langchain/chat_models/openai";import { HumanMessage } from "langchain/schema";const model = new ChatOpenAI({ temperature: 1 });const controller = new AbortController();// Call `controller.abort()` somewhere to cancel the request.const res = await model.call(  [    new HumanMessage(      "What is a good name for a company that makes colorful socks?"    ),  ],  { signal: controller.signal });console.log(res);/*'\n\nSocktastic Colors'*/

#### API Reference:

*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [HumanMessage](/docs/api/schema/classes/HumanMessage) from `langchain/schema`

Note, this will only cancel the outgoing request if the underlying provider exposes that option. LangChain will cancel the underlying request if possible, otherwise it will cancel the processing of the response.