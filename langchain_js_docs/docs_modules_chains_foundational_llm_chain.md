LLM
===

An LLMChain is a simple chain that adds some functionality around language models. It is used widely throughout LangChain, including in other chains and agents.

An LLMChain consists of a PromptTemplate and a language model (either an LLM or chat model). It formats the prompt template using the input key values provided (and also memory key values, if available), passes the formatted string to LLM and returns the LLM output.

Get started[​](#get-started "Direct link to Get started")
---------------------------------------------------------

We can construct an LLMChain which takes user input, formats it with a PromptTemplate, and then passes the formatted response to an LLM:

    import { OpenAI } from "langchain/llms/openai";import { PromptTemplate } from "langchain/prompts";import { LLMChain } from "langchain/chains";// We can construct an LLMChain from a PromptTemplate and an LLM.const model = new OpenAI({ temperature: 0 });const prompt = PromptTemplate.fromTemplate(  "What is a good name for a company that makes {product}?");const chainA = new LLMChain({ llm: model, prompt });// The result is an object with a `text` property.const resA = await chainA.call({ product: "colorful socks" });console.log({ resA });// { resA: { text: '\n\nSocktastic!' } }// Since this LLMChain is a single-input, single-output chain, we can also `run` it.// This convenience method takes in a string and returns the value// of the output key field in the chain response. For LLMChains, this defaults to "text".const resA2 = await chainA.run("colorful socks");console.log({ resA2 });// { resA2: '\n\nSocktastic!' }

#### API Reference:

*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [PromptTemplate](/docs/api/prompts/classes/PromptTemplate) from `langchain/prompts`
*   [LLMChain](/docs/api/chains/classes/LLMChain) from `langchain/chains`

Usage with Chat Models[​](#usage-with-chat-models "Direct link to Usage with Chat Models")
------------------------------------------------------------------------------------------

We can also construct an LLMChain which takes user input, formats it with a PromptTemplate, and then passes the formatted response to a ChatModel:

    import {  ChatPromptTemplate,  HumanMessagePromptTemplate,  SystemMessagePromptTemplate,} from "langchain/prompts";import { LLMChain } from "langchain/chains";import { ChatOpenAI } from "langchain/chat_models/openai";// We can also construct an LLMChain from a ChatPromptTemplate and a chat model.const chat = new ChatOpenAI({ temperature: 0 });const chatPrompt = ChatPromptTemplate.fromPromptMessages([  SystemMessagePromptTemplate.fromTemplate(    "You are a helpful assistant that translates {input_language} to {output_language}."  ),  HumanMessagePromptTemplate.fromTemplate("{text}"),]);const chainB = new LLMChain({  prompt: chatPrompt,  llm: chat,});const resB = await chainB.call({  input_language: "English",  output_language: "French",  text: "I love programming.",});console.log({ resB });// { resB: { text: "J'adore la programmation." } }

#### API Reference:

*   [ChatPromptTemplate](/docs/api/prompts/classes/ChatPromptTemplate) from `langchain/prompts`
*   [HumanMessagePromptTemplate](/docs/api/prompts/classes/HumanMessagePromptTemplate) from `langchain/prompts`
*   [SystemMessagePromptTemplate](/docs/api/prompts/classes/SystemMessagePromptTemplate) from `langchain/prompts`
*   [LLMChain](/docs/api/chains/classes/LLMChain) from `langchain/chains`
*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`

Usage in Streaming Mode[​](#usage-in-streaming-mode "Direct link to Usage in Streaming Mode")
---------------------------------------------------------------------------------------------

We can also construct an LLMChain which takes user input, formats it with a PromptTemplate, and then passes the formatted response to an LLM in streaming mode, which will stream back tokens as they are generated:

    import { OpenAI } from "langchain/llms/openai";import { PromptTemplate } from "langchain/prompts";import { LLMChain } from "langchain/chains";// Create a new LLMChain from a PromptTemplate and an LLM in streaming mode.const model = new OpenAI({ temperature: 0.9, streaming: true });const prompt = PromptTemplate.fromTemplate(  "What is a good name for a company that makes {product}?");const chain = new LLMChain({ llm: model, prompt });// Call the chain with the inputs and a callback for the streamed tokensconst res = await chain.call({ product: "colorful socks" }, [  {    handleLLMNewToken(token: string) {      process.stdout.write(token);    },  },]);console.log({ res });// { res: { text: '\n\nKaleidoscope Socks' } }

#### API Reference:

*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [PromptTemplate](/docs/api/prompts/classes/PromptTemplate) from `langchain/prompts`
*   [LLMChain](/docs/api/chains/classes/LLMChain) from `langchain/chains`

Cancelling a running LLMChain[​](#cancelling-a-running-llmchain "Direct link to Cancelling a running LLMChain")
---------------------------------------------------------------------------------------------------------------

We can also cancel a running LLMChain by passing an AbortSignal to the `call` method:

    import { OpenAI } from "langchain/llms/openai";import { PromptTemplate } from "langchain/prompts";import { LLMChain } from "langchain/chains";// Create a new LLMChain from a PromptTemplate and an LLM in streaming mode.const model = new OpenAI({ temperature: 0.9, streaming: true });const prompt = PromptTemplate.fromTemplate(  "Give me a long paragraph about {product}?");const chain = new LLMChain({ llm: model, prompt });const controller = new AbortController();// Call `controller.abort()` somewhere to cancel the request.setTimeout(() => {  controller.abort();}, 3000);try {  // Call the chain with the inputs and a callback for the streamed tokens  const res = await chain.call(    { product: "colorful socks", signal: controller.signal },    [      {        handleLLMNewToken(token: string) {          process.stdout.write(token);        },      },    ]  );} catch (e) {  console.log(e);  // Error: Cancel: canceled}

#### API Reference:

*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [PromptTemplate](/docs/api/prompts/classes/PromptTemplate) from `langchain/prompts`
*   [LLMChain](/docs/api/chains/classes/LLMChain) from `langchain/chains`

In this example we show cancellation in streaming mode, but it works the same way in non-streaming mode.