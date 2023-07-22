Entity memory
=============

Entity Memory remembers given facts about specific entities in a conversation. It extracts information on entities (using an LLM) and builds up its knowledge about that entity over time (also using an LLM).

Let's first walk through using this functionality.

    import { OpenAI } from "langchain/llms/openai";import {  EntityMemory,  ENTITY_MEMORY_CONVERSATION_TEMPLATE,} from "langchain/memory";import { LLMChain } from "langchain/chains";export const run = async () => {  const memory = new EntityMemory({    llm: new OpenAI({ temperature: 0 }),    chatHistoryKey: "history", // Default value    entitiesKey: "entities", // Default value  });  const model = new OpenAI({ temperature: 0.9 });  const chain = new LLMChain({    llm: model,    prompt: ENTITY_MEMORY_CONVERSATION_TEMPLATE, // Default prompt - must include the set chatHistoryKey and entitiesKey as input variables.    memory,  });  const res1 = await chain.call({ input: "Hi! I'm Jim." });  console.log({    res1,    memory: await memory.loadMemoryVariables({ input: "Who is Jim?" }),  });  const res2 = await chain.call({    input: "I work in construction. What about you?",  });  console.log({    res2,    memory: await memory.loadMemoryVariables({ input: "Who is Jim?" }),  });};

#### API Reference:

*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [EntityMemory](/docs/api/memory/classes/EntityMemory) from `langchain/memory`
*   [ENTITY\_MEMORY\_CONVERSATION\_TEMPLATE](/docs/api/memory/variables/ENTITY_MEMORY_CONVERSATION_TEMPLATE) from `langchain/memory`
*   [LLMChain](/docs/api/chains/classes/LLMChain) from `langchain/chains`

### Inspecting the Memory Store[​](#inspecting-the-memory-store "Direct link to Inspecting the Memory Store")

You can also inspect the memory store directly to see the current summary of each entity:

    import { OpenAI } from "langchain/llms/openai";import {  EntityMemory,  ENTITY_MEMORY_CONVERSATION_TEMPLATE,} from "langchain/memory";import { LLMChain } from "langchain/chains";const memory = new EntityMemory({  llm: new OpenAI({ temperature: 0 }),});const model = new OpenAI({ temperature: 0.9 });const chain = new LLMChain({  llm: model,  prompt: ENTITY_MEMORY_CONVERSATION_TEMPLATE,  memory,});await chain.call({ input: "Hi! I'm Jim." });await chain.call({  input: "I work in sales. What about you?",});const res = await chain.call({  input: "My office is the Utica branch of Dunder Mifflin. What about you?",});console.log({  res,  memory: await memory.loadMemoryVariables({ input: "Who is Jim?" }),});/*  {    res: "As an AI language model, I don't have an office in the traditional sense. I exist entirely in digital space and am here to assist you with any questions or tasks you may have. Is there anything specific you need help with regarding your work at the Utica branch of Dunder Mifflin?",    memory: {      entities: {        Jim: 'Jim is a human named Jim who works in sales.',        Utica: 'Utica is the location of the branch of Dunder Mifflin where Jim works.',        'Dunder Mifflin': 'Dunder Mifflin has a branch in Utica.'      }    }  }*/

#### API Reference:

*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [EntityMemory](/docs/api/memory/classes/EntityMemory) from `langchain/memory`
*   [ENTITY\_MEMORY\_CONVERSATION\_TEMPLATE](/docs/api/memory/variables/ENTITY_MEMORY_CONVERSATION_TEMPLATE) from `langchain/memory`
*   [LLMChain](/docs/api/chains/classes/LLMChain) from `langchain/chains`