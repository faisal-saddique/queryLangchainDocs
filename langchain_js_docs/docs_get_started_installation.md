Installation
============

info

Updating from <0.0.52? See [this section](#updating-from-0052) for instructions.

Supported Environments[​](#supported-environments "Direct link to Supported Environments")
------------------------------------------------------------------------------------------

LangChain is written in TypeScript and can be used in:

*   Node.js (ESM and CommonJS) - 18.x, 19.x, 20.x
*   Cloudflare Workers
*   Vercel / Next.js (Browser, Serverless and Edge functions)
*   Supabase Edge Functions
*   Browser
*   Deno

Installation[​](#installation "Direct link to Installation")
------------------------------------------------------------

To get started, install LangChain with the following command:

*   npm
*   Yarn
*   pnpm

    npm install -S langchain

    yarn add langchain

    pnpm add langchain

### TypeScript[​](#typescript "Direct link to TypeScript")

LangChain is written in TypeScript and provides type definitions for all of its public APIs.

Loading the library[​](#loading-the-library "Direct link to Loading the library")
---------------------------------------------------------------------------------

### ESM[​](#esm "Direct link to ESM")

LangChain provides an ESM build targeting Node.js environments. You can import it using the following syntax:

    import { OpenAI } from "langchain/llms/openai";

If you are using TypeScript in an ESM project we suggest updating your `tsconfig.json` to include the following:

tsconfig.json

    {  "compilerOptions": {    ...    "target": "ES2020", // or higher    "module": "nodenext",  }}

### CommonJS[​](#commonjs "Direct link to CommonJS")

LangChain provides a CommonJS build targeting Node.js environments. You can import it using the following syntax:

    const { OpenAI } = require("langchain/llms/openai");

### Cloudflare Workers[​](#cloudflare-workers "Direct link to Cloudflare Workers")

LangChain can be used in Cloudflare Workers. You can import it using the following syntax:

    import { OpenAI } from "langchain/llms/openai";

### Vercel / Next.js[​](#vercel--nextjs "Direct link to Vercel / Next.js")

LangChain can be used in Vercel / Next.js. We support using LangChain in frontend components, in Serverless functions and in Edge functions. You can import it using the following syntax:

    import { OpenAI } from "langchain/llms/openai";

### Deno / Supabase Edge Functions[​](#deno--supabase-edge-functions "Direct link to Deno / Supabase Edge Functions")

LangChain can be used in Deno / Supabase Edge Functions. You can import it using the following syntax:

    import { OpenAI } from "https://esm.sh/langchain/llms/openai";

We recommend looking at our [Supabase Template](https://github.com/langchain-ai/langchain-template-supabase) for an example of how to use LangChain in Supabase Edge Functions.

### Browser[​](#browser "Direct link to Browser")

LangChain can be used in the browser. In our CI we test bundling LangChain with Webpack and Vite, but other bundlers should work too. You can import it using the following syntax:

    import { OpenAI } from "langchain/llms/openai";

Updating from <0.0.52[​](#updating-from-0052 "Direct link to Updating from <0.0.52")
------------------------------------------------------------------------------------

If you are updating from a version of LangChain prior to 0.0.52, you will need to update your imports to use the new path structure.

For example, if you were previously doing

    import { OpenAI } from "langchain/llms";

you will now need to do

    import { OpenAI } from "langchain/llms/openai";

This applies to all imports from the following 6 modules, which have been split into submodules for each integration. The combined modules are deprecated, do not work outside of Node.js, and will be removed in a future version.

*   If you were using `langchain/llms`, see [LLMs](/docs/modules/model_io/models/llms) for updated import paths.
*   If you were using `langchain/chat_models`, see [Chat Models](/docs/modules/model_io/models/chat) for updated import paths.
*   If you were using `langchain/embeddings`, see [Embeddings](/docs/modules/data_connection/text_embedding) for updated import paths.
*   If you were using `langchain/vectorstores`, see [Vector Stores](/docs/modules/data_connection/vectorstores) for updated import paths.
*   If you were using `langchain/document_loaders`, see [Document Loaders](/docs/modules/data_connection/document_loaders) for updated import paths.
*   If you were using `langchain/retrievers`, see [Retrievers](/docs/modules/data_connection/retrievers) for updated import paths.

Other modules are not affected by this change, and you can continue to import them from the same path.

Additionally, there are some breaking changes that were needed to support new environments:

*   `import { Calculator } from "langchain/tools";` now moved to
    *   `import { Calculator } from "langchain/tools/calculator";`
*   `import { loadLLM } from "langchain/llms";` now moved to
    *   `import { loadLLM } from "langchain/llms/load";`
*   `import { loadAgent } from "langchain/agents";` now moved to
    *   `import { loadAgent } from "langchain/agents/load";`
*   `import { loadPrompt } from "langchain/prompts";` now moved to
    *   `import { loadPrompt } from "langchain/prompts/load";`
*   `import { loadChain } from "langchain/chains";` now moved to
    *   `import { loadChain } from "langchain/chains/load";`

Unsupported: Node.js 16[​](#unsupported-nodejs-16 "Direct link to Unsupported: Node.js 16")
-------------------------------------------------------------------------------------------

We do not support Node.js 16, but if you still want to run LangChain on Node.js 16, you will need to follow the instructions in this section. We do not guarantee that these instructions will continue to work in the future.

You will have to make `fetch` available globally, either:

*   run your application with `NODE_OPTIONS='--experimental-fetch' node ...`, or
*   install `node-fetch` and follow the instructions [here](https://github.com/node-fetch/node-fetch#providing-global-access)

Additionally you'll have to polyfill `structuredClone`, eg. by installing `core-js` and following the instructions [here](https://github.com/zloirock/core-js).

If you are running this on Node.js 18+, you do not need to do anything.