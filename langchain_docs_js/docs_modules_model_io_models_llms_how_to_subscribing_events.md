Subscribing to events
=====================

Especially when using an agent, there can be a lot of back-and-forth going on behind the scenes as a LLM processes a prompt. For agents, the response object contains an intermediateSteps object that you can print to see an overview of the steps it took to get there. If that's not enough and you want to see every exchange with the LLM, you can pass callbacks to the LLM for custom logging (or anything else you want to do) as the model goes through the steps:

For more info on the events available see the [Callbacks](/docs/modules/callbacks/) section of the docs.

    import { LLMResult } from "langchain/schema";import { OpenAI } from "langchain/llms/openai";import { Serialized } from "langchain/load/serializable";// We can pass in a list of CallbackHandlers to the LLM constructor to get callbacks for various events.const model = new OpenAI({  callbacks: [    {      handleLLMStart: async (llm: Serialized, prompts: string[]) => {        console.log(JSON.stringify(llm, null, 2));        console.log(JSON.stringify(prompts, null, 2));      },      handleLLMEnd: async (output: LLMResult) => {        console.log(JSON.stringify(output, null, 2));      },      handleLLMError: async (err: Error) => {        console.error(err);      },    },  ],});await model.call(  "What would be a good company name a company that makes colorful socks?");// {//     "name": "openai"// }// [//     "What would be a good company name a company that makes colorful socks?"// ]// {//   "generations": [//     [//         {//             "text": "\n\nSocktastic Splashes.",//             "generationInfo": {//                 "finishReason": "stop",//                 "logprobs": null//             }//         }//     ]//  ],//   "llmOutput": {//     "tokenUsage": {//         "completionTokens": 9,//          "promptTokens": 14,//          "totalTokens": 23//     }//   }// }

#### API Reference:

*   [LLMResult](/docs/api/schema/types/LLMResult) from `langchain/schema`
*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [Serialized](/docs/api/load_serializable/types/Serialized) from `langchain/load/serializable`