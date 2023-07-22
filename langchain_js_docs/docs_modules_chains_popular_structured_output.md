Structured Output with OpenAI functions
=======================================

Compatibility

Must be used with an [OpenAI functions](https://platform.openai.com/docs/guides/gpt/function-calling) model.

This chain leverages OpenAI functions to output objects that match a given format for any given prompt. It converts input schema into an OpenAI function, then forces OpenAI to call that function to return a response in the correct format.

You can use it where you would use a chain with a [`StructuredOutputParser`](/docs/modules/model_io/output_parsers) without any special instructions stuffed into the prompt. It will also more reliably output structured results with higher `temperature` values, making it better suited for more creative applications.

**Note:** The outermost layer of the input schema must be an object.

Usage[​](#usage "Direct link to Usage")
---------------------------------------

### Format Text into Structured Data[​](#format-text-into-structured-data "Direct link to Format Text into Structured Data")

    import { z } from "zod";import { ChatOpenAI } from "langchain/chat_models/openai";import {  ChatPromptTemplate,  SystemMessagePromptTemplate,  HumanMessagePromptTemplate,} from "langchain/prompts";import { createStructuredOutputChainFromZod } from "langchain/chains/openai_functions";const zodSchema = z.object({  foods: z    .array(      z.object({        name: z.string().describe("The name of the food item"),        healthy: z.boolean().describe("Whether the food is good for you"),        color: z.string().optional().describe("The color of the food"),      })    )    .describe("An array of food items mentioned in the text"),});const prompt = new ChatPromptTemplate({  promptMessages: [    SystemMessagePromptTemplate.fromTemplate(      "List all food items mentioned in the following text."    ),    HumanMessagePromptTemplate.fromTemplate("{inputText}"),  ],  inputVariables: ["inputText"],});const llm = new ChatOpenAI({ modelName: "gpt-3.5-turbo-0613", temperature: 0 });const chain = createStructuredOutputChainFromZod(zodSchema, {  prompt,  llm,});const response = await chain.call({  inputText: "I like apples, bananas, oxygen, and french fries.",});console.log(JSON.stringify(response, null, 2));/*  {    "output": {      "foods": [        {          "name": "apples",          "healthy": true,          "color": "red"        },        {          "name": "bananas",          "healthy": true,          "color": "yellow"        },        {          "name": "french fries",          "healthy": false,          "color": "golden"        }      ]    }  }*/

#### API Reference:

*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [ChatPromptTemplate](/docs/api/prompts/classes/ChatPromptTemplate) from `langchain/prompts`
*   [SystemMessagePromptTemplate](/docs/api/prompts/classes/SystemMessagePromptTemplate) from `langchain/prompts`
*   [HumanMessagePromptTemplate](/docs/api/prompts/classes/HumanMessagePromptTemplate) from `langchain/prompts`
*   [createStructuredOutputChainFromZod](/docs/api/chains_openai_functions/functions/createStructuredOutputChainFromZod) from `langchain/chains/openai_functions`

### Generate a Database Record[​](#generate-a-database-record "Direct link to Generate a Database Record")

    import { z } from "zod";import { ChatOpenAI } from "langchain/chat_models/openai";import {  ChatPromptTemplate,  SystemMessagePromptTemplate,  HumanMessagePromptTemplate,} from "langchain/prompts";import { createStructuredOutputChainFromZod } from "langchain/chains/openai_functions";const zodSchema = z.object({  name: z.string().describe("Human name"),  surname: z.string().describe("Human surname"),  age: z.number().describe("Human age"),  birthplace: z.string().describe("Where the human was born"),  appearance: z.string().describe("Human appearance description"),  shortBio: z.string().describe("Short bio secription"),  university: z.string().optional().describe("University name if attended"),  gender: z.string().describe("Gender of the human"),  interests: z    .array(z.string())    .describe("json array of strings human interests"),});const prompt = new ChatPromptTemplate({  promptMessages: [    SystemMessagePromptTemplate.fromTemplate(      "Generate details of a hypothetical person."    ),    HumanMessagePromptTemplate.fromTemplate("Additional context: {inputText}"),  ],  inputVariables: ["inputText"],});const llm = new ChatOpenAI({ modelName: "gpt-3.5-turbo-0613", temperature: 1 });const chain = createStructuredOutputChainFromZod(zodSchema, {  prompt,  llm,  outputKey: "person",});const response = await chain.call({  inputText:    "Please generate a diverse group of people, but don't generate anyone who likes video games.",});console.log(JSON.stringify(response, null, 2));/*  {    "person": {      "name": "Sophia",      "surname": "Martinez",      "age": 32,      "birthplace": "Mexico City, Mexico",      "appearance": "Sophia has long curly brown hair and hazel eyes. She has a warm smile and a contagious laugh.",      "shortBio": "Sophia is a passionate environmentalist who is dedicated to promoting sustainable living. She believes in the power of individual actions to create a positive impact on the planet.",      "university": "Stanford University",      "gender": "Female",      "interests": [        "Hiking",        "Yoga",        "Cooking",        "Reading"      ]    }  }*/

#### API Reference:

*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [ChatPromptTemplate](/docs/api/prompts/classes/ChatPromptTemplate) from `langchain/prompts`
*   [SystemMessagePromptTemplate](/docs/api/prompts/classes/SystemMessagePromptTemplate) from `langchain/prompts`
*   [HumanMessagePromptTemplate](/docs/api/prompts/classes/HumanMessagePromptTemplate) from `langchain/prompts`
*   [createStructuredOutputChainFromZod](/docs/api/chains_openai_functions/functions/createStructuredOutputChainFromZod) from `langchain/chains/openai_functions`

### Customization[​](#customization "Direct link to Customization")

This chain takes all the same arguments as a standard [`LLMChain`](/docs/modules/chains/foundational/llm_chain) minus an `outputParser`. It will also be created with a default model set to `gpt-3.5-turbo-0613`, but you can pass an options parameter into the input parameters with a pre-created `ChatOpenAI` instance as `llm`.