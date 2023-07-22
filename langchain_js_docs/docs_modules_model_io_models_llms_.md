LLMs
====

Large Language Models (LLMs) are a core component of LangChain. LangChain does not serve it's own LLMs, but rather provides a standard interface for interacting with many different LLMs.

For more detailed documentation check out our:

*   **How-to guides**: Walkthroughs of core functionality, like streaming, async, etc.
    
*   **Integrations**: How to use different LLM providers (OpenAI, Anthropic, etc.)
    

Get started[​](#get-started "Direct link to Get started")
---------------------------------------------------------

There are lots of LLM providers (OpenAI, Cohere, Hugging Face, etc) - the `LLM` class is designed to provide a standard interface for all of them.

In this walkthrough we'll work with an OpenAI LLM wrapper, although the functionalities highlighted are generic for all LLM types.

### Setup[​](#setup "Direct link to Setup")

To start we'll need to install the official OpenAI package:

*   npm
*   Yarn
*   pnpm

    npm install -S openai

    yarn add openai

    pnpm add openai

Accessing the API requires an API key, which you can get by creating an account and heading [here](https://platform.openai.com/account/api-keys). Once we have a key we'll want to set it as an environment variable by running:

    export OPENAI_API_KEY="..."

If you'd prefer not to set an environment variable you can pass the key in directly via the `openAIApiKey` parameter when initializing the OpenAI LLM class:

    import { OpenAI } from "langchain/llms/openai";const llm = new OpenAI({  openAIApiKey: "YOUR_KEY_HERE",});

otherwise you can initialize with an empty object:

    import { OpenAI } from "langchain/llms/openai";const llm = new OpenAI({});

### `call`: string in -> string out[​](#call-string-in---string-out "Direct link to call-string-in---string-out")

The simplest way to use an LLM is the `.call` method: pass in a string, get a string completion.

    const res = await llm.call("Tell me a joke");console.log(res);// "Why did the chicken cross the road?\n\nTo get to the other side."

### `generate`: batch calls, richer outputs[​](#generate-batch-calls-richer-outputs "Direct link to generate-batch-calls-richer-outputs")

`generate` lets you can call the model with a list of strings, getting back a more complete response than just the text. This complete response can includes things like multiple top responses and other LLM provider-specific information:

    const llmResult = await llm.generate(["Tell me a joke", "Tell me a poem"], ["Tell me a joke", "Tell me a poem"]);console.log(llmResult.generations.length)// 30console.log(llmResult.generations[0]);/*  [    {      text: "\n\nQ: What did the fish say when it hit the wall?\nA: Dam!",      generationInfo: { finishReason: "stop", logprobs: null }    }  ]*/console.log(llmResult.generations[1]);/*  [    {      text: "\n\nRoses are red,\nViolets are blue,\nSugar is sweet,\nAnd so are you.",      generationInfo: { finishReason: "stop", logprobs: null }    }  ]*/

You can also access provider specific information that is returned. This information is NOT standardized across providers.

    console.log(llmResult.llmOutput);/*  {    tokenUsage: { completionTokens: 46, promptTokens: 8, totalTokens: 54 }  }*/

Here's an example with additional parameters, which sets `-1` for `max_tokens` to turn on token size calculations:

    import { OpenAI } from "langchain/llms/openai";export const run = async () => {  const model = new OpenAI({    // customize openai model that's used, `text-davinci-003` is the default    modelName: "text-ada-001",    // `max_tokens` supports a magic -1 param where the max token length for the specified modelName    //  is calculated and included in the request to OpenAI as the `max_tokens` param    maxTokens: -1,    // use `modelKwargs` to pass params directly to the openai call    // note that they use snake_case instead of camelCase    modelKwargs: {      user: "me",    },    // for additional logging for debugging purposes    verbose: true,  });  const resA = await model.call(    "What would be a good company name a company that makes colorful socks?"  );  console.log({ resA });  // { resA: '\n\nSocktastic Colors' }};

#### API Reference:

*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`

Advanced[​](#advanced "Direct link to Advanced")
------------------------------------------------

_This section is for users who want a deeper technical understanding of how LangChain works. If you are just getting started, you can skip this section._

Both LLMs and Chat Models are built on top of the `BaseLanguageModel` class. This class provides a common interface for all models, and allows us to easily swap out models in chains without changing the rest of the code.

The `BaseLanguageModel` class has two abstract methods: `generatePrompt` and `getNumTokens`, which are implemented by `BaseChatModel` and `BaseLLM` respectively.

`BaseLLM` is a subclass of `BaseLanguageModel` that provides a common interface for LLMs while `BaseChatModel` is a subclass of `BaseLanguageModel` that provides a common interface for chat models.