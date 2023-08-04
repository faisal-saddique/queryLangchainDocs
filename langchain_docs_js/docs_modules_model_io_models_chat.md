Chat models
===========

Chat models are a variation on language models. While chat models use language models under the hood, the interface they expose is a bit different. Rather than expose a "text in, text out" API, they expose an interface where "chat messages" are the inputs and outputs.

Chat model APIs are fairly new, so we are still figuring out the correct abstractions.

The following sections of documentation are provided:

*   **How-to guides**: Walkthroughs of core functionality, like streaming, creating chat prompts, etc.
    
*   **Integrations**: How to use different chat model providers (OpenAI, Anthropic, etc).
    

Get started[](#get-started "Direct link to Get started")
---------------------------------------------------------

### Setup[](#setup "Direct link to Setup")

To start we'll need to install the official OpenAI package:

*   npm
*   Yarn
*   pnpm

    npm install -S openai

    yarn add openai

    pnpm add openai

Accessing the API requires an API key, which you can get by creating an account and heading [here](https://platform.openai.com/account/api-keys). Once we have a key we'll want to set it as an environment variable by running:

    export OPENAI_API_KEY="..."

If you'd prefer not to set an environment variable you can pass the key in directly via the `openAIApiKey` parameter when initializing the ChatOpenAI class:

    import { ChatOpenAI } from "langchain/chat_models/openai";const chat = new ChatOpenAI({  openAIApiKey: "YOUR_KEY_HERE"});

otherwise you can initialize it with an empty object:

    import { ChatOpenAI } from "langchain/chat_models/openai";const chat = new ChatOpenAI({});

### Messages[](#messages "Direct link to Messages")

The chat model interface is based around messages rather than raw text. The types of messages currently supported in LangChain are `AIMessage`, `HumanMessage`, `SystemMessage`, `FunctionMessage`, and `ChatMessage` -- `ChatMessage` takes in an arbitrary role parameter. Most of the time, you'll just be dealing with `HumanMessage`, `AIMessage`, and `SystemMessage`

### `call`[](#call "Direct link to call")

#### Messages in -> message out[](#messages-in---message-out "Direct link to Messages in -> message out")

You can get chat completions by passing one or more messages to the chat model. The response will be a message.

    import { ChatOpenAI } from "langchain/chat_models/openai";import { HumanMessage } from "langchain/schema";const chat = new ChatOpenAI();// Pass in a list of messages to `call` to start a conversation. In this simple example, we only pass in one message.const response = await chat.call([  new HumanMessage(    "What is a good name for a company that makes colorful socks?"  ),]);console.log(response);// AIMessage { text: '\n\nRainbow Sox Co.' }

#### API Reference:

*   [ChatOpenAI](/docs/api/chat_models_openai/classes/ChatOpenAI) from `langchain/chat_models/openai`
*   [HumanMessage](/docs/api/schema/classes/HumanMessage) from `langchain/schema`

OpenAI's chat model also supports multiple messages as input. See [here](https://platform.openai.com/docs/guides/chat/chat-vs-completions) for more information. Here is an example of sending a system and user message to the chat model:

    const response2 = await chat.call([  new SystemMessage(    "You are a helpful assistant that translates English to French."  ),  new HumanMessage("Translate: I love programming."),]);console.log(response2);// AIMessage { text: "J'aime programmer." }

### `generate`[](#generate "Direct link to generate")

#### Batch calls, richer outputs[](#batch-calls-richer-outputs "Direct link to Batch calls, richer outputs")

You can go one step further and generate completions for multiple sets of messages using `generate`. This returns an `LLMResult` with an additional `message` parameter.

    const response3 = await chat.generate([  [    new SystemMessage(      "You are a helpful assistant that translates English to French."    ),    new HumanMessage(      "Translate this sentence from English to French. I love programming."    ),  ],  [    new SystemMessage(      "You are a helpful assistant that translates English to French."    ),    new HumanMessage(      "Translate this sentence from English to French. I love artificial intelligence."    ),  ],]);console.log(response3);/*  {    generations: [      [        {          text: "J'aime programmer.",          message: AIMessage { text: "J'aime programmer." },        }      ],      [        {          text: "J'aime l'intelligence artificielle.",          message: AIMessage { text: "J'aime l'intelligence artificielle." }        }      ]    ]  }*/

You can recover things like token usage from this LLMResult:

    console.log(response3.llmOutput);/*  {    tokenUsage: { completionTokens: 20, promptTokens: 69, totalTokens: 89 }  }*/