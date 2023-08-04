Subscribing to events
=====================

Especially when using an agent, there can be a lot of back-and-forth going on behind the scenes as a Chat Model processes a prompt. For agents, the response object contains an intermediateSteps object that you can print to see an overview of the steps it took to get there. If that's not enough and you want to see every exchange with the Chat Model, you can pass callbacks to the Chat Model for custom logging (or anything else you want to do) as the model goes through the steps:

For more info on the events available see the [Callbacks](/docs/modules/callbacks) section of the docs.

    import { HumanMessage, LLMResult } from "langchain/schema";import { ChatOpenAI } from "langchain/chat_models/openai";import { Serialized } from "langchain/load/serializable";// We can pass in a list of CallbackHandlers to the LLM constructor to get callbacks for various events.const model = new ChatOpenAI({  callbacks: [    {      handleLLMStart: async (llm: Serialized, prompts: string[]) => {        console.log(JSON.stringify(llm, null, 2));        console.log(JSON.stringify(prompts, null, 2));      },      handleLLMEnd: async (output: LLMResult) => {        console.log(JSON.stringify(output, null, 2));      },      handleLLMError: async (err: Error) => {        console.error(err);      },    },  ],});await model.call([  new HumanMessage(    "What is a good name for a company that makes colorful socks?"  ),]);/*{  "name": "openai"}[  "Human: What is a good name for a company that makes colorful socks?"]{  "generations": [    [      {        "text": "Rainbow Soles",        "message": {          "text": "Rainbow Soles"        }      }    ]  ],  "llmOutput": {    "tokenUsage": {      "completionTokens": 4,      "promptTokens": 21,      "totalTokens": 25    }  }}*/

#### API Reference:

*   [HumanMessage](/docs/api/schema/classes/HumanMessage) from `langchain/schema`
*   [LLMResult](/docs/api/schema/types/LLMResult) from `langchain/schema`
*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [Serialized](/docs/api/load_serializable/types/Serialized) from `langchain/load/serializable`