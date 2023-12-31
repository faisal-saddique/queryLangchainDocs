Prompts
=======

Prompts for Chat models are built around messages, instead of just plain text.

You can make use of templating by using a `ChatPromptTemplate` from one or more `MessagePromptTemplates`, then using `ChatPromptTemplate`'s `formatPrompt` method.

For convenience, there is also a `fromTemplate` method exposed on the template. If you were to use this template, this is what it would look like:

    import { ChatOpenAI } from "langchain/chat_models/openai";import { LLMChain } from "langchain/chains";import {  ChatPromptTemplate,  SystemMessagePromptTemplate,  HumanMessagePromptTemplate} from "langchain/prompts";const template = "You are a helpful assistant that translates {input_language} to {output_language}.";const systemMessagePrompt = SystemMessagePromptTemplate.fromTemplate(template);const humanTemplate = "{text}";const humanMessagePrompt = HumanMessagePromptTemplate.fromTemplate(humanTemplate);const chatPrompt = ChatPromptTemplate.fromPromptMessages([systemMessagePrompt, humanMessagePrompt]);const chat = new ChatOpenAI({  temperature: 0,});const chain = new LLMChain({  llm: chat,  prompt: chatPrompt,});const result = await chain.call({  input_language: "English",  output_language: "French",  text: "I love programming",});

    // { text: "J'adore programmer" }