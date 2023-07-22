Quickstart
==========

Installation[​](#installation "Direct link to Installation")
------------------------------------------------------------

To install LangChain run:

*   npm
*   Yarn
*   pnpm

    npm install -S langchain

    yarn add langchain

    pnpm add langchain

For more details, see our [Installation guide](/docs/get_started/installation).

Environment setup[​](#environment-setup "Direct link to Environment setup")
---------------------------------------------------------------------------

Using LangChain will usually require integrations with one or more model providers, data stores, APIs, etc. For this example, we'll use OpenAI's model APIs.

Accessing their API requires an API key, which you can get by creating an account and heading [here](https://platform.openai.com/account/api-keys). Once we have a key we'll want to set it as an environment variable by running:

    export OPENAI_API_KEY="..."

If you'd prefer not to set an environment variable you can pass the key in directly via the `openAIApiKey` parameter when initializing the OpenAI LLM class:

    import { OpenAI } from "langchain/llms/openai";const llm = new OpenAI({  openAIApiKey: "YOUR_KEY_HERE",});

Building an application[​](#building-an-application "Direct link to Building an application")
---------------------------------------------------------------------------------------------

Now we can start building our language model application. LangChain provides many modules that can be used to build language model applications. Modules can be used as stand-alones in simple applications and they can be combined for more complex use cases.

LLMs[​](#llms "Direct link to LLMs")
------------------------------------

#### Get predictions from a language model[​](#get-predictions-from-a-language-model "Direct link to Get predictions from a language model")

The basic building block of LangChain is the LLM, which takes in text and generates more text.

As an example, suppose we're building an application that generates a company name based on a company description. In order to do this, we need to initialize an OpenAI model wrapper. In this case, since we want the outputs to be MORE random, we'll initialize our model with a HIGH temperature.

    import { OpenAI } from "langchain/llms/openai";const llm = new OpenAI({  temperature: 0.9,});

And now we can pass in text and get predictions!

    const result = await llm.predict("What would be a good company name for a company that makes colorful socks?");// "Feetful of Fun"

Chat models[​](#chat-models "Direct link to Chat models")
---------------------------------------------------------

Chat models are a variation on language models. While chat models use language models under the hood, the interface they expose is a bit different: rather than expose a "text in, text out" API, they expose an interface where "chat messages" are the inputs and outputs.

You can get chat completions by passing one or more messages to the chat model. The response will be a message. The types of messages currently supported in LangChain are `AIMessage`, `HumanMessage`, `SystemMessage`, `FunctionMessage`, and `ChatMessage` -- `ChatMessage` takes in an arbitrary role parameter. Most of the time, you'll just be dealing with `HumanMessage`, `AIMessage`, and `SystemMessage`.

    import { ChatOpenAI } from "langchain/chat_models/openai";import { HumanMessage, ChatMessage, SystemMessage } from "langchain/schema";const chat = new ChatOpenAI({  temperature: 0});const result = await chat.predictMessages([  new HumanMessage("Translate this sentence from English to French. I love programming.")]);/*  AIMessage {    content: "J'adore la programmation."  }*/

It is useful to understand how chat models are different from a normal LLM, but it can often be handy to just be able to treat them the same. LangChain makes that easy by also exposing an interface through which you can interact with a chat model as you would a normal LLM. You can access this through the `predict` interface.

    const result = await chat.predict("Translate this sentence from English to French. I love programming.")// "J'adore la programmation."

Prompt templates[​](#prompt-templates "Direct link to Prompt templates")
------------------------------------------------------------------------

Most LLM applications do not pass user input directly into an LLM. Usually they will add the user input to a larger piece of text, called a prompt template, that provides additional context on the specific task at hand.

In the previous example, the text we passed to the model contained instructions to generate a company name. For our application, it'd be great if the user only had to provide the description of a company/product, without having to worry about giving the model instructions.

*   LLMs
*   Chat models

With PromptTemplates this is easy! In this case our template would be very simple:

    import { PromptTemplate } from "langchain/prompts";const prompt = PromptTemplate.fromTemplate("What is a good name for a company that makes {product}?");const formattedPrompt = await prompt.format({  product: "colorful socks"});

    "What is a good name for a company that makes colorful socks?"

Similar to LLMs, you can make use of templating by using a `MessagePromptTemplate`. You can build a `ChatPromptTemplate` from one or more `MessagePromptTemplate`s. You can use `ChatPromptTemplate`'s `format_messages` method to generate the formatted messages.

Because this is generating a list of messages, it is slightly more complex than the normal prompt template which is generating only a string. Please see the detailed guides on prompts to understand more options available to you here.

    import {  ChatPromptTemplate,  SystemMessagePromptTemplate,  HumanMessagePromptTemplate} from "langchain/prompts";const template = "You are a helpful assistant that translates {input_language} to {output_language}.";const systemMessagePrompt = SystemMessagePromptTemplate.fromTemplate(template);const humanTemplate = "{text}";const humanMessagePrompt = HumanMessagePromptTemplate.fromTemplate(humanTemplate);const chatPrompt = ChatPromptTemplate.fromPromptMessages([systemMessagePrompt, humanMessagePrompt]);const formattedPrompt = await chatPrompt.formatMessages({  input_language: "English",  output_language: "French",  text: "I love programming."});

    /*  [    SystemMessage {      content: 'You are a helpful assistant that translates English to French.'    },    HumanMessage {      content: 'I love programming.'    }  ]*/

Chains[​](#chains "Direct link to Chains")
------------------------------------------

Now that we've got a model and a prompt template, we'll want to combine the two. Chains give us a way to link (or chain) together multiple primitives, like models, prompts, and other chains.

*   LLMs
*   Chat models

The simplest and most common type of chain is an LLMChain, which passes an input first to a PromptTemplate and then to an LLM. We can construct an LLM chain from our existing model and prompt template.

Using this we can replace

    const result = await llm.predict("What would be a good company name for a company that makes colorful socks?");

with

    import { OpenAI } from "langchain/llms/openai";import { LLMChain } from "langchain/chains";import { PromptTemplate } from "langchain/prompts";const llm = new OpenAI({});const prompt = PromptTemplate.fromTemplate("What is a good name for a company that makes {product}?");const chain = new LLMChain({  llm,  prompt});// Run is a convenience method for chains with prompts that require one input and one output.const result = await chain.run("colorful socks");

    "Feetful of Fun"

There we go, our first chain! Understanding how this simple chain works will set you up well for working with more complex chains.

The `LLMChain` can be used with chat models as well:

    import { ChatOpenAI } from "langchain/chat_models/openai";import { LLMChain } from "langchain/chains";import {  ChatPromptTemplate,  SystemMessagePromptTemplate,  HumanMessagePromptTemplate} from "langchain/prompts";const template = "You are a helpful assistant that translates {input_language} to {output_language}.";const systemMessagePrompt = SystemMessagePromptTemplate.fromTemplate(template);const humanTemplate = "{text}";const humanMessagePrompt = HumanMessagePromptTemplate.fromTemplate(humanTemplate);const chatPrompt = ChatPromptTemplate.fromPromptMessages([systemMessagePrompt, humanMessagePrompt]);const chat = new ChatOpenAI({  temperature: 0,});const chain = new LLMChain({  llm: chat,  prompt: chatPrompt,});const result = await chain.call({  input_language: "English",  output_language: "French",  text: "I love programming",});

    // { text: "J'adore programmer" }

Agents[​](#agents "Direct link to Agents")
------------------------------------------

Our first chain ran a pre-determined sequence of steps. To handle complex workflows, we need to be able to dynamically choose actions based on inputs.

Agents do just this: they use a language model to determine which actions to take and in what order. Agents are given access to tools, and they repeatedly choose a tool, run the tool, and observe the output until they come up with a final answer.

To load an agent, you need to choose a(n):

*   LLM/Chat model: The language model powering the agent.
*   Tool(s): A function that performs a specific duty. This can be things like: Google Search, Database lookup, Python REPL, other chains. For a list of predefined tools and their specifications, see the [Tools documentation](/docs/modules/agents/tools/).
*   Agent name: A string that references a supported agent class. An agent class is largely parameterized by the prompt the language model uses to determine which action to take. Because this notebook focuses on the simplest, highest level API, this only covers using the standard supported agents. If you want to implement a custom agent, see [here](/docs/modules/agents). For a list of supported agents and their specifications, see [here](/docs/modules/agents/agent_types/).

For this example, we'll be using SerpAPI to query a search engine.

You'll need to set the `SERPAPI_API_KEY` environment variable.

*   LLMs
*   Chat models

    import { initializeAgentExecutorWithOptions } from "langchain/agents";import { OpenAI } from "langchain/llms/openai";import { SerpAPI } from "langchain/tools";import { Calculator } from "langchain/tools/calculator";const model = new OpenAI({ temperature: 0 });const tools = [  new SerpAPI(process.env.SERPAPI_API_KEY, {    location: "Austin,Texas,United States",    hl: "en",    gl: "us",  }),  new Calculator(),];const executor = await initializeAgentExecutorWithOptions(tools, model, {  agentType: "zero-shot-react-description",  verbose: true,});const input = "What was the high temperature in SF yesterday in Fahrenheit? What is that number raised to the .023 power?";const result = await executor.call({  input,});

    > Entering new AgentExecutor chain...Thought: I need to find the temperature first, then use the calculator to raise it to the .023 power.Action: SearchAction Input: "High temperature in SF yesterday"Observation: San Francisco Temperature Yesterday. Maximum temperature yesterday: 57 °F (at 1:56 pm) Minimum temperature yesterday: 49 °F (at 1:56 am) Average temperature ...Thought: I now have the temperature, so I can use the calculator to raise it to the .023 power.Action: CalculatorAction Input: 57^.023Observation: Answer: 1.0974509573251117Thought: I now know the final answerFinal Answer: 1.0974509573251117.> Finished chain.

    // { output: "1.0974509573251117" }

Agents can also be used with chat models. There are a few varieties, but if using OpenAI and a functions-capable model, you can use `openai-functions` as the agent type.

    import { initializeAgentExecutorWithOptions } from "langchain/agents";import { ChatOpenAI } from "langchain/chat_models/openai";import { SerpAPI } from "langchain/tools";import { Calculator } from "langchain/tools/calculator";const executor = await initializeAgentExecutorWithOptions(  [new Calculator(), new SerpAPI()],  new ChatOpenAI({ modelName: "gpt-4-0613", temperature: 0 }),  {    agentType: "openai-functions",    verbose: true,  });const result = await executor.run("What is the temperature in New York?");

    /*  {    "output": "The current temperature in New York is 89°F, but it feels like 92°F. Please be cautious as the heat can lead to dehydration or heat stroke."  }*/

Memory[​](#memory "Direct link to Memory")
------------------------------------------

The chains and agents we've looked at so far have been stateless, but for many applications it's necessary to reference past interactions. This is clearly the case with a chatbot for example, where you want it to understand new messages in the context of past messages.

The Memory module gives you a way to maintain application state. The base Memory interface is simple: it lets you update state given the latest run inputs and outputs and it lets you modify (or contextualize) the next input using the stored state.

There are a number of built-in memory systems. The simplest of these is a buffer memory which just prepends the last few inputs/outputs to the current input - we will use this in the example below.

*   LLMs
*   Chat models

    import { OpenAI } from "langchain/llms/openai";import { BufferMemory } from "langchain/memory";import { ConversationChain } from "langchain/chains";const model = new OpenAI({});const memory = new BufferMemory();const chain = new ConversationChain({  llm: model,  memory,  verbose: true,});const res1 = await chain.call({ input: "Hi! I'm Jim." });

here's what's going on under the hood

    > Entering new chain...Prompt after formatting:The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.Current conversation:Human: Hi there!AI:> Finished chain.>> 'Hello! How are you today?'

Now if we run the chain again

    const res2 = await chain.call({ input: "What's my name?" });

we'll see that the full prompt that's passed to the model contains the input and output of our first interaction, along with our latest input

    > Entering new chain...Prompt after formatting:The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.Current conversation:Human: Hi there!AI:  Hello! How are you today?Human: I'm doing well! Just having a conversation with an AI.AI:> Finished chain.>> "Your name is Jim."

You can use Memory with chains and agents initialized with chat models. The main difference between this and Memory for LLMs is that rather than trying to condense all previous messages into a string, we can keep them as their own unique memory object.

    import { ConversationChain } from "langchain/chains";import { ChatOpenAI } from "langchain/chat_models/openai";import {  ChatPromptTemplate,  HumanMessagePromptTemplate,  SystemMessagePromptTemplate,  MessagesPlaceholder,} from "langchain/prompts";import { BufferMemory } from "langchain/memory";const chat = new ChatOpenAI({ temperature: 0 });const chatPrompt = ChatPromptTemplate.fromPromptMessages([  SystemMessagePromptTemplate.fromTemplate(    "The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know."  ),  new MessagesPlaceholder("history"),  HumanMessagePromptTemplate.fromTemplate("{input}"),]);// Return the current conversation directly as messages and insert them into the MessagesPlaceholder in the above prompt.const memory = new BufferMemory({  returnMessages: true,  memoryKey: "history"});const chain = new ConversationChain({  memory,  prompt: chatPrompt,  llm: chat,  verbose: true,});const res = await chain.call({  input: "My name is Jim.",});

    Hello Jim! It's nice to meet you. How can I assist you today?

    const res2 = await chain.call({  input: "What is my name?",});

    Your name is Jim. You mentioned it at the beginning of our conversation. Is there anything specific you would like to know or discuss, Jim?