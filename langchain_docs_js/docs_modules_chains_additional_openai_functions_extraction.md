`Extraction`
============

Compatibility

Must be used with an [OpenAI Functions](https://platform.openai.com/docs/guides/gpt/function-calling) model.

This chain is designed to extract lists of objects from an input text and schema of desired info.

    import { z } from "zod";import { ChatOpenAI } from "langchain/chat_models/openai";import { createExtractionChainFromZod } from "langchain/chains";const zodSchema = z.object({  "person-name": z.string().optional(),  "person-age": z.number().optional(),  "person-hair_color": z.string().optional(),  "dog-name": z.string().optional(),  "dog-breed": z.string().optional(),});const chatModel = new ChatOpenAI({  modelName: "gpt-3.5-turbo-0613",  temperature: 0,});const chain = createExtractionChainFromZod(zodSchema, chatModel);console.log(  await chain.run(`Alex is 5 feet tall. Claudia is 4 feet taller Alex and jumps higher than him. Claudia is a brunette and Alex is blonde.Alex's dog Frosty is a labrador and likes to play hide and seek.`));/*[  {    'person-name': 'Alex',    'person-age': 0,    'person-hair_color': 'blonde',    'dog-name': 'Frosty',    'dog-breed': 'labrador'  },  {    'person-name': 'Claudia',    'person-age': 0,    'person-hair_color': 'brunette',    'dog-name': '',    'dog-breed': ''  }]*/

#### API Reference:

*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [createExtractionChainFromZod](/docs/api/chains/functions/createExtractionChainFromZod) from `langchain/chains`