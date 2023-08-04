OpenAI functions
================

Certain OpenAI models (like gpt-3.5-turbo-0613 and gpt-4-0613) have been fine-tuned to detect when a function should to be called and respond with the inputs that should be passed to the function. In an API call, you can describe functions and have the model intelligently choose to output a JSON object containing arguments to call those functions. The goal of the OpenAI Function APIs is to more reliably return valid and useful function calls than a generic text completion or chat API.

The OpenAI Functions Agent is designed to work with these models.

Compatibility

Must be used with an [OpenAI Functions](https://platform.openai.com/docs/guides/gpt/function-calling) model.

This agent also supports `StructuredTool`s with more complex input schemas.

    import { initializeAgentExecutorWithOptions } from "langchain/agents";import { ChatOpenAI } from "langchain/chat_models/openai";import { SerpAPI } from "langchain/tools";import { Calculator } from "langchain/tools/calculator";const tools = [new Calculator(), new SerpAPI()];const chat = new ChatOpenAI({ modelName: "gpt-4", temperature: 0 });const executor = await initializeAgentExecutorWithOptions(tools, chat, {  agentType: "openai-functions",  verbose: true,});const result = await executor.run("What is the weather in New York?");console.log(result);/*  The current weather in New York is 72°F with a wind speed of 1 mph coming from the SSW. The humidity is at 89% and the UV index is 0 out of 11. The cloud cover is 79% and there has been no rain.*/

#### API Reference:

*   [initializeAgentExecutorWithOptions](/docs/api/agents/functions/initializeAgentExecutorWithOptions) from `langchain/agents`
*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [SerpAPI](/docs/api/tools/classes/SerpAPI) from `langchain/tools`
*   [Calculator](/docs/api/tools_calculator/classes/Calculator) from `langchain/tools/calculator`

Prompt customization[](#prompt-customization "Direct link to Prompt customization")
------------------------------------------------------------------------------------

You can pass in a custom string to be used as the system message of the prompt as follows:

    import { initializeAgentExecutorWithOptions } from "langchain/agents";import { ChatOpenAI } from "langchain/chat_models/openai";import { SerpAPI } from "langchain/tools";import { Calculator } from "langchain/tools/calculator";const tools = [new Calculator(), new SerpAPI()];const chat = new ChatOpenAI({ modelName: "gpt-4", temperature: 0 });const prefix =  "You are a helpful AI assistant. However, all final response to the user must be in pirate dialect.";const executor = await initializeAgentExecutorWithOptions(tools, chat, {  agentType: "openai-functions",  verbose: true,  agentArgs: {    prefix,  },});const result = await executor.run("What is the weather in New York?");console.log(result);// Arr matey, in New York, it be feelin' like 75 degrees, with a gentle breeze blowin' from the northwest at 3 knots. The air be 77% full o' water, and the clouds be coverin' 35% of the sky. There be no rain in sight, yarr!

#### API Reference:

*   [initializeAgentExecutorWithOptions](/docs/api/agents/functions/initializeAgentExecutorWithOptions) from `langchain/agents`
*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [SerpAPI](/docs/api/tools/classes/SerpAPI) from `langchain/tools`
*   [Calculator](/docs/api/tools_calculator/classes/Calculator) from `langchain/tools/calculator`