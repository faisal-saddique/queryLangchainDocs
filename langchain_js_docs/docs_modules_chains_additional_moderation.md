Moderation
==========

This notebook walks through examples of how to use a moderation chain, and several common ways for doing so. Moderation chains are useful for detecting text that could be hateful, violent, etc. This can be useful to apply on both user input, but also on the output of a Language Model. Some API providers, like OpenAI, [specifically prohibit](https://beta.openai.com/docs/usage-policies/use-case-policy) you, or your end users, from generating some types of harmful content. To comply with this (and to just generally prevent your application from being harmful) you may often want to append a moderation chain to any LLMChains, in order to make sure any output the LLM generates is not harmful.

If the content passed into the moderation chain is harmful, there is not one best way to handle it, it probably depends on your application. Sometimes you may want to throw an error in the Chain (and have your application handle that). Other times, you may want to return something to the user explaining that the text was harmful. There could even be other ways to handle it! We will cover all these ways in this walkthrough.

Usage[​](#usage "Direct link to Usage")
---------------------------------------

    import { OpenAIModerationChain, LLMChain } from "langchain/chains";import { PromptTemplate } from "langchain/prompts";import { OpenAI } from "langchain/llms/openai";// A string containing potentially offensive content from the userconst badString = "Bad naughty words from user";try {  // Create a new instance of the OpenAIModerationChain  const moderation = new OpenAIModerationChain({    throwError: true, // If set to true, the call will throw an error when the moderation chain detects violating content. If set to false, violating content will return "Text was found that violates OpenAI's content policy.".  });  // Send the user's input to the moderation chain and wait for the result  const { output: badResult } = await moderation.call({    input: badString,  });  // If the moderation chain does not detect violating content, it will return the original input and you can proceed to use the result in another chain.  const model = new OpenAI({ temperature: 0 });  const template = "Hello, how are you today {person}?";  const prompt = new PromptTemplate({ template, inputVariables: ["person"] });  const chainA = new LLMChain({ llm: model, prompt });  const resA = await chainA.call({ person: badResult });  console.log({ resA });} catch (error) {  // If an error is caught, it means the input contains content that violates OpenAI TOS  console.error("Naughty words detected!");}

#### API Reference:

*   [OpenAIModerationChain](/docs/api/chains/classes/OpenAIModerationChain) from `langchain/chains`
*   [LLMChain](/docs/api/chains/classes/LLMChain) from `langchain/chains`
*   [PromptTemplate](/docs/api/prompts/classes/PromptTemplate) from `langchain/prompts`
*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`