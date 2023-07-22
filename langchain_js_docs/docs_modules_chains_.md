Chains
======

Using an LLM in isolation is fine for simple applications, but more complex applications require chaining LLMs - either with each other or with other components.

LangChain provides the **Chain** interface for such "chained" applications. We define a Chain very generically as a sequence of calls to components, which can include other chains. The base interface is simple:

    import { CallbackManagerForChainRun } from "langchain/callbacks";import { BaseChain as _ } from "langchain/chains";import { BaseMemory } from "langchain/memory";import { ChainValues } from "langchain/schema";abstract class BaseChain {  memory?: BaseMemory;  /**   * Run the core logic of this chain and return the output   */  abstract _call(    values: ChainValues,    runManager?: CallbackManagerForChainRun  ): Promise<ChainValues>;  /**   * Return the string type key uniquely identifying this class of chain.   */  abstract _chainType(): string;  /**   * Return the list of input keys this chain expects to receive when called.   */  abstract get inputKeys(): string[];  /**   * Return the list of output keys this chain will produce when called.   */  abstract get outputKeys(): string[];}

#### API Reference:

*   [CallbackManagerForChainRun](/docs/api/callbacks/classes/CallbackManagerForChainRun) from `langchain/callbacks`
*   [BaseChain](/docs/api/chains/classes/BaseChain) from `langchain/chains`
*   [BaseMemory](/docs/api/memory/classes/BaseMemory) from `langchain/memory`
*   [ChainValues](/docs/api/schema/types/ChainValues) from `langchain/schema`

This idea of composing components together in a chain is simple but powerful. It drastically simplifies and makes more modular the implementation of complex applications, which in turn makes it much easier to debug, maintain, and improve your applications.

For more specifics check out:

*   [How-to](/docs/modules/chains/how_to/) for walkthroughs of different chain features
*   [Foundational](/docs/modules/chains/foundational/) to get acquainted with core building block chains
*   [Document](/docs/modules/chains/document/) to learn how to incorporate documents into chains
*   [Popular](/docs/modules/chains/popular/) chains for the most common use cases
*   [Additional](/docs/modules/chains/additional/) to see some of the more advanced chains and integrations that you can use out of the box

Why do we need chains?[​](#why-do-we-need-chains "Direct link to Why do we need chains?")
-----------------------------------------------------------------------------------------

Chains allow us to combine multiple components together to create a single, coherent application. For example, we can create a chain that takes user input, formats it with a PromptTemplate, and then passes the formatted response to an LLM. We can build more complex chains by combining multiple chains together, or by combining chains with other components.

Get started[​](#get-started "Direct link to Get started")
---------------------------------------------------------

### Using `LLMChain`[​](#using-llmchain "Direct link to using-llmchain")

The `LLMChain` is most basic building block chain. It takes in a prompt template, formats it with the user input and returns the response from an LLM.

To use the `LLMChain`, first create a prompt template.

    import { OpenAI } from "langchain/llms/openai";import { PromptTemplate } from "langchain/prompts";import { LLMChain } from "langchain/chains";// We can construct an LLMChain from a PromptTemplate and an LLM.const model = new OpenAI({ temperature: 0 });const prompt = PromptTemplate.fromTemplate(  "What is a good name for a company that makes {product}?");

We can now create a very simple chain that will take user input, format the prompt with it, and then send it to the LLM.

    const chain = new LLMChain({ llm: model, prompt });// Since this LLMChain is a single-input, single-output chain, we can also `run` it.// This convenience method takes in a string and returns the value// of the output key field in the chain response. For LLMChains, this defaults to "text".const res = await chain.run("colorful socks");console.log({ res });// { res: "\n\nSocktastic!" }

If there are multiple variables, you can input them all at once using a dictionary. This will return the complete chain response.

    const prompt = PromptTemplate.fromTemplate(  "What is a good name for {company} that makes {product}?");const chain = new LLMChain({ llm: model, prompt });const res = await chain.call({  company: "a startup",  product: "colorful socks"});console.log({ res });// { res: { text: '\n\Socktopia Colourful Creations.' } }

You can use a chat model in an `LLMChain` as well:

    import {  ChatPromptTemplate,  HumanMessagePromptTemplate,  SystemMessagePromptTemplate,} from "langchain/prompts";import { LLMChain } from "langchain/chains";import { ChatOpenAI } from "langchain/chat_models/openai";// We can also construct an LLMChain from a ChatPromptTemplate and a chat model.const chat = new ChatOpenAI({ temperature: 0 });const chatPrompt = ChatPromptTemplate.fromPromptMessages([  SystemMessagePromptTemplate.fromTemplate(    "You are a helpful assistant that translates {input_language} to {output_language}."  ),  HumanMessagePromptTemplate.fromTemplate("{text}"),]);const chainB = new LLMChain({  prompt: chatPrompt,  llm: chat,});const resB = await chainB.call({  input_language: "English",  output_language: "French",  text: "I love programming.",});console.log({ resB });// { resB: { text: "J'adore la programmation." } }

#### API Reference:

*   [ChatPromptTemplate](/docs/api/prompts/classes/ChatPromptTemplate) from `langchain/prompts`
*   [HumanMessagePromptTemplate](/docs/api/prompts/classes/HumanMessagePromptTemplate) from `langchain/prompts`
*   [SystemMessagePromptTemplate](/docs/api/prompts/classes/SystemMessagePromptTemplate) from `langchain/prompts`
*   [LLMChain](/docs/api/chains/classes/LLMChain) from `langchain/chains`
*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`