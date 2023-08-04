Using Buffer Memory with Chat Models
====================================

This example covers how to use chat-specific memory classes with chat models. The key thing to notice is that setting `returnMessages: true` makes the memory return a list of chat messages instead of a string.

    import { ConversationChain } from "langchain/chains";import { ChatOpenAI } from "langchain/chat_models/openai";import {  ChatPromptTemplate,  HumanMessagePromptTemplate,  SystemMessagePromptTemplate,  MessagesPlaceholder,} from "langchain/prompts";import { BufferMemory } from "langchain/memory";export const run = async () => {  const chat = new ChatOpenAI({ temperature: 0 });  const chatPrompt = ChatPromptTemplate.fromPromptMessages([    SystemMessagePromptTemplate.fromTemplate(      "The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know."    ),    new MessagesPlaceholder("history"),    HumanMessagePromptTemplate.fromTemplate("{input}"),  ]);  const chain = new ConversationChain({    memory: new BufferMemory({ returnMessages: true, memoryKey: "history" }),    prompt: chatPrompt,    llm: chat,  });  const response = await chain.call({    input: "hi! whats up?",  });  console.log(response);};

#### API Reference:

*   [ConversationChain](/docs/api/chains/classes/ConversationChain) from `langchain/chains`
*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [ChatPromptTemplate](/docs/api/prompts/classes/ChatPromptTemplate) from `langchain/prompts`
*   [HumanMessagePromptTemplate](/docs/api/prompts/classes/HumanMessagePromptTemplate) from `langchain/prompts`
*   [SystemMessagePromptTemplate](/docs/api/prompts/classes/SystemMessagePromptTemplate) from `langchain/prompts`
*   [MessagesPlaceholder](/docs/api/prompts/classes/MessagesPlaceholder) from `langchain/prompts`
*   [BufferMemory](/docs/api/memory/classes/BufferMemory) from `langchain/memory`