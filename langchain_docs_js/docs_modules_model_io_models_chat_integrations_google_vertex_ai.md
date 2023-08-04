ChatGoogleVertexAI
==================

The Vertex AI implementation is meant to be used in Node.js and not directly from a browser, since it requires a service account to use.

Before running this code, you should make sure the Vertex AI API is enabled for the relevant project and that you've authenticated to Google Cloud using one of these methods:

*   You are logged into an account (using `gcloud auth application-default login`) permitted to that project.
*   You are running on a machine using a service account that is permitted to the project.
*   You have downloaded the credentials for a service account that is permitted to the project and set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of this file.

*   npm
*   Yarn
*   pnpm

    npm install google-auth-library

    yarn add google-auth-library

    pnpm add google-auth-library

The ChatGoogleVertexAI class works just like other chat-based LLMs, with a few exceptions:

1.  The first `SystemMessage` passed in is mapped to the "context" parameter that the PaLM model expects. No other `SystemMessages` are allowed.
2.  After the first `SystemMessage`, there must be an odd number of messages, representing a conversation between a human and the model.
3.  Human messages must alternate with AI messages.

    import { ChatGoogleVertexAI } from "langchain/chat_models/googlevertexai";const model = new ChatGoogleVertexAI({  temperature: 0.7,});

#### API Reference:

*   [ChatGoogleVertexAI](/docs/api/chat_models_googlevertexai/classes/ChatGoogleVertexAI) from `langchain/chat_models/googlevertexai`

There is also an optional `examples` constructor parameter that can help the model understand what an appropriate response looks like.

    import { ChatGoogleVertexAI } from "langchain/chat_models/googlevertexai";import { AIMessage, HumanMessage, SystemMessage } from "langchain/schema";export const run = async () => {  const examples = [    {      input: new HumanMessage("What is your favorite sock color?"),      output: new AIMessage("My favorite sock color be arrrr-ange!"),    },  ];  const model = new ChatGoogleVertexAI({    temperature: 0.7,    examples,  });  const questions = [    new SystemMessage(      "You are a funny assistant that answers in pirate language."    ),    new HumanMessage("What is your favorite food?"),  ];  // You can also use the model as part of a chain  const res = await model.call(questions);  console.log({ res });};

#### API Reference:

*   [ChatGoogleVertexAI](/docs/api/chat_models_googlevertexai/classes/ChatGoogleVertexAI) from `langchain/chat_models/googlevertexai`
*   [AIMessage](/docs/api/schema/classes/AIMessage) from `langchain/schema`
*   [HumanMessage](/docs/api/schema/classes/HumanMessage) from `langchain/schema`
*   [SystemMessage](/docs/api/schema/classes/SystemMessage) from `langchain/schema`