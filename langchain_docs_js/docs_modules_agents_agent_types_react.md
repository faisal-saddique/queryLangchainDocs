ReAct
=====

This walkthrough showcases using an agent to implement the [ReAct](https://react-lm.github.io/) logic.

    import { initializeAgentExecutorWithOptions } from "langchain/agents";import { OpenAI } from "langchain/llms/openai";import { SerpAPI } from "langchain/tools";import { Calculator } from "langchain/tools/calculator";const model = new OpenAI({ temperature: 0 });const tools = [  new SerpAPI(process.env.SERPAPI_API_KEY, {    location: "Austin,Texas,United States",    hl: "en",    gl: "us",  }),  new Calculator(),];const executor = await initializeAgentExecutorWithOptions(tools, model, {  agentType: "zero-shot-react-description",  verbose: true,});const input = `Who is Olivia Wilde's boyfriend? What is his current age raised to the 0.23 power?`;const result = await executor.call({ input });

#### API Reference:

*   [initializeAgentExecutorWithOptions](/docs/api/agents/functions/initializeAgentExecutorWithOptions) from `langchain/agents`
*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [SerpAPI](/docs/api/tools/classes/SerpAPI) from `langchain/tools`
*   [Calculator](/docs/api/tools_calculator/classes/Calculator) from `langchain/tools/calculator`

Using chat models[](#using-chat-models "Direct link to Using chat models")
---------------------------------------------------------------------------

You can also create ReAct agents that use chat models instead of LLMs as the agent driver.

    import { initializeAgentExecutorWithOptions } from "langchain/agents";import { ChatOpenAI } from "langchain/chat_models/openai";import { SerpAPI } from "langchain/tools";import { Calculator } from "langchain/tools/calculator";export const run = async () => {  const model = new ChatOpenAI({ temperature: 0 });  const tools = [    new SerpAPI(process.env.SERPAPI_API_KEY, {      location: "Austin,Texas,United States",      hl: "en",      gl: "us",    }),    new Calculator(),  ];  const executor = await initializeAgentExecutorWithOptions(tools, model, {    agentType: "chat-zero-shot-react-description",    returnIntermediateSteps: true,  });  console.log("Loaded agent.");  const input = `Who is Olivia Wilde's boyfriend? What is his current age raised to the 0.23 power?`;  console.log(`Executing with input "${input}"...`);  const result = await executor.call({ input });  console.log(`Got output ${result.output}`);  console.log(    `Got intermediate steps ${JSON.stringify(      result.intermediateSteps,      null,      2    )}`  );};

#### API Reference:

*   [initializeAgentExecutorWithOptions](/docs/api/agents/functions/initializeAgentExecutorWithOptions) from `langchain/agents`
*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [SerpAPI](/docs/api/tools/classes/SerpAPI) from `langchain/tools`
*   [Calculator](/docs/api/tools_calculator/classes/Calculator) from `langchain/tools/calculator`