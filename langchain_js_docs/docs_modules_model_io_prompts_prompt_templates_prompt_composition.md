Composition
===========

This notebook goes over how to compose multiple prompts together. This can be useful when you want to reuse parts of prompts. This can be done with a PipelinePrompt. A PipelinePrompt consists of two main parts:

*   Final prompt: This is the final prompt that is returned
*   Pipeline prompts: This is a list of tuples, consisting of a string name and a prompt template. Each prompt template will be formatted and then passed to future prompt templates as a variable with the same name.

    import { PromptTemplate, PipelinePromptTemplate } from "langchain/prompts";const fullPrompt = PromptTemplate.fromTemplate(`{introduction}{example}{start}`);const introductionPrompt = PromptTemplate.fromTemplate(  `You are impersonating {person}.`);const examplePrompt =  PromptTemplate.fromTemplate(`Here's an example of an interaction:Q: {example_q}A: {example_a}`);const startPrompt = PromptTemplate.fromTemplate(`Now, do this for real!Q: {input}A:`);const composedPrompt = new PipelinePromptTemplate({  pipelinePrompts: [    {      name: "introduction",      prompt: introductionPrompt,    },    {      name: "example",      prompt: examplePrompt,    },    {      name: "start",      prompt: startPrompt,    },  ],  finalPrompt: fullPrompt,});const formattedPrompt = await composedPrompt.format({  person: "Elon Musk",  example_q: `What's your favorite car?`,  example_a: "Telsa",  input: `What's your favorite social media site?`,});console.log(formattedPrompt);/*  You are impersonating Elon Musk.  Here's an example of an interaction:  Q: What's your favorite car?  A: Telsa  Now, do this for real!  Q: What's your favorite social media site?  A:*/

#### API Reference:

*   [PromptTemplate](/docs/api/prompts/classes/PromptTemplate) from `langchain/prompts`
*   [PipelinePromptTemplate](/docs/api/prompts/classes/PipelinePromptTemplate) from `langchain/prompts`