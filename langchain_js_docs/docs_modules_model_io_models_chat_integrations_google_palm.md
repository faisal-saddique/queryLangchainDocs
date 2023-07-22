ChatGooglePaLM
==============

The [Google PaLM API](https://developers.generativeai.google/products/palm) can be integrated by first installing the required packages:

*   npm
*   Yarn
*   pnpm

    npm install google-auth-library @google-ai/generativelanguage

    yarn add google-auth-library @google-ai/generativelanguage

    pnpm add google-auth-library @google-ai/generativelanguage

Create an **API key** from [Google MakerSuite](https://makersuite.google.com/app/apikey). You can then set the key as `GOOGLE_PALM_API_KEY` environment variable or pass it as `apiKey` parameter while instantiating the model.

    import { ChatGooglePaLM } from "langchain/chat_models/googlepalm";import { AIMessage, HumanMessage, SystemMessage } from "langchain/schema";export const run = async () => {  const model = new ChatGooglePaLM({    apiKey: "<YOUR API KEY>", // or set it in environment variable as `GOOGLE_PALM_API_KEY`    temperature: 0.7, // OPTIONAL    modelName: "models/chat-bison-001", // OPTIONAL    topK: 40, // OPTIONAL    topP: 3, // OPTIONAL    examples: [      // OPTIONAL      {        input: new HumanMessage("What is your favorite sock color?"),        output: new AIMessage("My favorite sock color be arrrr-ange!"),      },    ],  });  // ask questions  const questions = [    new SystemMessage(      "You are a funny assistant that answers in pirate language."    ),    new HumanMessage("What is your favorite food?"),  ];  // You can also use the model as part of a chain  const res = await model.call(questions);  console.log({ res });};

#### API Reference:

*   [ChatGooglePaLM](/docs/api/chat_models_googlepalm/classes/ChatGooglePaLM) from `langchain/chat_models/googlepalm`
*   [AIMessage](/docs/api/schema/classes/AIMessage) from `langchain/schema`
*   [HumanMessage](/docs/api/schema/classes/HumanMessage) from `langchain/schema`
*   [SystemMessage](/docs/api/schema/classes/SystemMessage) from `langchain/schema`