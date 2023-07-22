Google PaLM
===========

The [Google PaLM API](https://developers.generativeai.google/products/palm) can be integrated by first installing the required packages:

*   npm
*   Yarn
*   pnpm

    npm install google-auth-library @google-ai/generativelanguage

    yarn add google-auth-library @google-ai/generativelanguage

    pnpm add google-auth-library @google-ai/generativelanguage

Create an **API key** from [Google MakerSuite](https://makersuite.google.com/app/apikey). You can then set the key as `GOOGLE_PALM_API_KEY` environment variable or pass it as `apiKey` parameter while instantiating the model.

    import { GooglePaLM } from "langchain/llms/googlepalm";export const run = async () => {  const model = new GooglePaLM({    apiKey: "<YOUR API KEY>", // or set it in environment variable as `GOOGLE_PALM_API_KEY`    // other params    temperature: 1, // OPTIONAL    modelName: "models/text-bison-001", // OPTIONAL    maxOutputTokens: 1024, // OPTIONAL    topK: 40, // OPTIONAL    topP: 3, // OPTIONAL    safetySettings: [      // OPTIONAL      {        category: "HARM_CATEGORY_DANGEROUS",        threshold: "BLOCK_MEDIUM_AND_ABOVE",      },    ],    stopSequences: ["stop"], // OPTIONAL  });  const res = await model.call(    "What would be a good company name for a company that makes colorful socks?"  );  console.log({ res });};

#### API Reference:

*   [GooglePaLM](/docs/api/llms_googlepalm/classes/GooglePaLM) from `langchain/llms/googlepalm`