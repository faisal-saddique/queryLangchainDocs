`Tagging`
=========

Compatibility

Must be used with an [OpenAI Functions](https://platform.openai.com/docs/guides/gpt/function-calling) model.

This chain is designed to tag an input text according to properties defined in a schema.

    import { createTaggingChain } from "langchain/chains";import { ChatOpenAI } from "langchain/chat_models/openai";import type { FunctionParameters } from "langchain/output_parsers";const schema: FunctionParameters = {  type: "object",  properties: {    sentiment: { type: "string" },    tone: { type: "string" },    language: { type: "string" },  },  required: ["tone"],};const chatModel = new ChatOpenAI({ modelName: "gpt-4-0613", temperature: 0 });const chain = createTaggingChain(schema, chatModel);console.log(  await chain.run(    `Estoy increiblemente contento de haberte conocido! Creo que seremos muy buenos amigos!`  ));/*{ tone: 'positive', language: 'Spanish' }*/

#### API Reference:

*   [createTaggingChain](/docs/api/chains/functions/createTaggingChain) from `langchain/chains`
*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [FunctionParameters](/docs/api/output_parsers/types/FunctionParameters) from `langchain/output_parsers`