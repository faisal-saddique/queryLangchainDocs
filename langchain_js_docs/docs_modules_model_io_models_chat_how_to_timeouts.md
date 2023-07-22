Adding a timeout
================

By default, LangChain will wait indefinitely for a response from the model provider. If you want to add a timeout, you can pass a `timeout` option, in milliseconds, when you call the model. For example, for OpenAI:

    import { ChatOpenAI } from "langchain/chat_models/openai";import { HumanMessage } from "langchain/schema";const chat = new ChatOpenAI({ temperature: 1 });const response = await chat.call(  [    new HumanMessage(      "What is a good name for a company that makes colorful socks?"    ),  ],  { timeout: 1000 } // 1s timeout);console.log(response);// AIMessage { text: '\n\nRainbow Sox Co.' }

#### API Reference:

*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [HumanMessage](/docs/api/schema/classes/HumanMessage) from `langchain/schema`