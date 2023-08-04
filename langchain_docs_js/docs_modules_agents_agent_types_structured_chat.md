Structured tool chat
====================

The structured tool chat agent is capable of using multi-input tools.

Older agents are configured to specify an action input as a single string, but this agent can use the provided tools' `args_schema` to populate the action input.

This makes it easier to create and use tools that require multiple input values - rather than prompting for a stringified object or comma separated list, you can specify an object with multiple keys. Here's an example with a `DynamicStructuredTool`:

    import { z } from "zod";import { ChatOpenAI } from "langchain/chat_models/openai";import { initializeAgentExecutorWithOptions } from "langchain/agents";import { Calculator } from "langchain/tools/calculator";import { DynamicStructuredTool } from "langchain/tools";export const run = async () => {  const model = new ChatOpenAI({ temperature: 0 });  const tools = [    new Calculator(), // Older existing single input tools will still work    new DynamicStructuredTool({      name: "random-number-generator",      description: "generates a random number between two input numbers",      schema: z.object({        low: z.number().describe("The lower bound of the generated number"),        high: z.number().describe("The upper bound of the generated number"),      }),      func: async ({ low, high }) =>        (Math.random() * (high - low) + low).toString(), // Outputs still must be strings      returnDirect: false, // This is an option that allows the tool to return the output directly    }),  ];  const executor = await initializeAgentExecutorWithOptions(tools, model, {    agentType: "structured-chat-zero-shot-react-description",    verbose: true,  });  console.log("Loaded agent.");  const input = `What is a random number between 5 and 10 raised to the second power?`;  console.log(`Executing with input "${input}"...`);  const result = await executor.call({ input });  console.log({ result });  /*    {      "output": "67.95299776074"    }  */};

#### API Reference:

*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [initializeAgentExecutorWithOptions](/docs/api/agents/functions/initializeAgentExecutorWithOptions) from `langchain/agents`
*   [Calculator](/docs/api/tools_calculator/classes/Calculator) from `langchain/tools/calculator`
*   [DynamicStructuredTool](/docs/api/tools/classes/DynamicStructuredTool) from `langchain/tools`

Adding Memory[](#adding-memory "Direct link to Adding Memory")
---------------------------------------------------------------

You can add memory to this agent like this:

    import { ChatOpenAI } from "langchain/chat_models/openai";import { initializeAgentExecutorWithOptions } from "langchain/agents";import { Calculator } from "langchain/tools/calculator";import { MessagesPlaceholder } from "langchain/prompts";import { BufferMemory } from "langchain/memory";export const run = async () => {  const model = new ChatOpenAI({ temperature: 0 });  const tools = [new Calculator()];  const executor = await initializeAgentExecutorWithOptions(tools, model, {    agentType: "structured-chat-zero-shot-react-description",    verbose: true,    memory: new BufferMemory({      memoryKey: "chat_history",      returnMessages: true,    }),    agentArgs: {      inputVariables: ["input", "agent_scratchpad", "chat_history"],      memoryPrompts: [new MessagesPlaceholder("chat_history")],    },  });  const result = await executor.call({ input: `what is 9 to the 2nd power?` });  console.log(result);  /*    {      "output": "81"    }  */  const result2 = await executor.call({    input: `what is that number squared?`,  });  console.log(result2);  /*    {      "output": "6561"    }  */};

#### API Reference:

*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [initializeAgentExecutorWithOptions](/docs/api/agents/functions/initializeAgentExecutorWithOptions) from `langchain/agents`
*   [Calculator](/docs/api/tools_calculator/classes/Calculator) from `langchain/tools/calculator`
*   [MessagesPlaceholder](/docs/api/prompts/classes/MessagesPlaceholder) from `langchain/prompts`
*   [BufferMemory](/docs/api/memory/classes/BufferMemory) from `langchain/memory`