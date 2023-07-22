Conversation Summary Memory
===========================

The Conversation Summary Memory summarizes the conversation as it happens and stores the current summary in memory. This memory can then be used to inject the summary of the conversation so far into a prompt/chain. This memory is most useful for longer conversations, where keeping the past message history in the prompt verbatim would take up too many tokens.

Usage, with an LLM[​](#usage-with-an-llm "Direct link to Usage, with an LLM")
-----------------------------------------------------------------------------

    import { OpenAI } from "langchain/llms/openai";import { ConversationSummaryMemory } from "langchain/memory";import { LLMChain } from "langchain/chains";import { PromptTemplate } from "langchain/prompts";export const run = async () => {  const memory = new ConversationSummaryMemory({    memoryKey: "chat_history",    llm: new OpenAI({ modelName: "gpt-3.5-turbo", temperature: 0 }),  });  const model = new OpenAI({ temperature: 0.9 });  const prompt =    PromptTemplate.fromTemplate(`The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.  Current conversation:  {chat_history}  Human: {input}  AI:`);  const chain = new LLMChain({ llm: model, prompt, memory });  const res1 = await chain.call({ input: "Hi! I'm Jim." });  console.log({ res1, memory: await memory.loadMemoryVariables({}) });  /*  {    res1: {      text: " Hi Jim, I'm AI! It's nice to meet you. I'm an AI programmed to provide information about the environment around me. Do you have any specific questions about the area that I can answer for you?"    },    memory: {      chat_history: 'Jim introduces himself to the AI and the AI responds, introducing itself as a program designed to provide information about the environment. The AI offers to answer any specific questions Jim may have about the area.'    }  }  */  const res2 = await chain.call({ input: "What's my name?" });  console.log({ res2, memory: await memory.loadMemoryVariables({}) });  /*  {    res2: { text: ' You told me your name is Jim.' },    memory: {      chat_history: 'Jim introduces himself to the AI and the AI responds, introducing itself as a program designed to provide information about the environment. The AI offers to answer any specific questions Jim may have about the area. Jim asks the AI what his name is, and the AI responds that Jim had previously told it his name.'    }  }  */};

#### API Reference:

*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [ConversationSummaryMemory](/docs/api/memory/classes/ConversationSummaryMemory) from `langchain/memory`
*   [LLMChain](/docs/api/chains/classes/LLMChain) from `langchain/chains`
*   [PromptTemplate](/docs/api/prompts/classes/PromptTemplate) from `langchain/prompts`

Usage, with a Chat Model[​](#usage-with-a-chat-model "Direct link to Usage, with a Chat Model")
-----------------------------------------------------------------------------------------------

    import { ChatOpenAI } from "langchain/chat_models/openai";import { ConversationSummaryMemory } from "langchain/memory";import { LLMChain } from "langchain/chains";import { PromptTemplate } from "langchain/prompts";export const run = async () => {  const memory = new ConversationSummaryMemory({    memoryKey: "chat_history",    llm: new ChatOpenAI({ modelName: "gpt-3.5-turbo", temperature: 0 }),  });  const model = new ChatOpenAI();  const prompt =    PromptTemplate.fromTemplate(`The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.  Current conversation:  {chat_history}  Human: {input}  AI:`);  const chain = new LLMChain({ llm: model, prompt, memory });  const res1 = await chain.call({ input: "Hi! I'm Jim." });  console.log({ res1, memory: await memory.loadMemoryVariables({}) });  /*  {    res1: {      text: "Hello Jim! It's nice to meet you. My name is AI. How may I assist you today?"    },    memory: {      chat_history: 'Jim introduces himself to the AI and the AI greets him and offers assistance.'    }  }  */  const res2 = await chain.call({ input: "What's my name?" });  console.log({ res2, memory: await memory.loadMemoryVariables({}) });  /*  {    res2: {      text: "Your name is Jim. It's nice to meet you, Jim. How can I assist you today?"    },    memory: {      chat_history: 'Jim introduces himself to the AI and the AI greets him and offers assistance. The AI addresses Jim by name and asks how it can assist him.'    }  }  */};

#### API Reference:

*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [ConversationSummaryMemory](/docs/api/memory/classes/ConversationSummaryMemory) from `langchain/memory`
*   [LLMChain](/docs/api/chains/classes/LLMChain) from `langchain/chains`
*   [PromptTemplate](/docs/api/prompts/classes/PromptTemplate) from `langchain/prompts`