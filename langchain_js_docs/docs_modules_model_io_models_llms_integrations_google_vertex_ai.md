Google Vertex AI
================

The Vertex AI implementation is meant to be used in Node.js and not directly in a browser, since it requires a service account to use.

Before running this code, you should make sure the Vertex AI API is enabled for the relevant project in your Google Cloud dashboard and that you've authenticated to Google Cloud using one of these methods:

*   You are logged into an account (using `gcloud auth application-default login`) permitted to that project.
*   You are running on a machine using a service account that is permitted to the project.
*   You have downloaded the credentials for a service account that is permitted to the project and set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of this file.

*   npm
*   Yarn
*   pnpm

    npm install google-auth-library

    yarn add google-auth-library

    pnpm add google-auth-library

    import { GoogleVertexAI } from "langchain/llms/googlevertexai";/* * Before running this, you should make sure you have created a * Google Cloud Project that is permitted to the Vertex AI API. * * You will also need permission to access this project / API. * Typically, this is done in one of three ways: * - You are logged into an account permitted to that project. * - You are running this on a machine using a service account permitted to *   the project. * - The `GOOGLE_APPLICATION_CREDENTIALS` environment variable is set to the *   path of a credentials file for a service account permitted to the project. */export const run = async () => {  const model = new GoogleVertexAI({    temperature: 0.7,  });  const res = await model.call(    "What would be a good company name a company that makes colorful socks?"  );  console.log({ res });};

#### API Reference:

*   [GoogleVertexAI](/docs/api/llms_googlevertexai/classes/GoogleVertexAI) from `langchain/llms/googlevertexai`

Google also has separate models for their "Codey" code generation models.

The "code-gecko" model is useful for code completion:

    import { GoogleVertexAI } from "langchain/llms/googlevertexai";/* * Before running this, you should make sure you have created a * Google Cloud Project that is permitted to the Vertex AI API. * * You will also need permission to access this project / API. * Typically, this is done in one of three ways: * - You are logged into an account permitted to that project. * - You are running this on a machine using a service account permitted to *   the project. * - The `GOOGLE_APPLICATION_CREDENTIALS` environment variable is set to the *   path of a credentials file for a service account permitted to the project. */const model = new GoogleVertexAI({  model: "code-gecko",});const res = await model.call("for (let co=0;");console.log({ res });

#### API Reference:

*   [GoogleVertexAI](/docs/api/llms_googlevertexai/classes/GoogleVertexAI) from `langchain/llms/googlevertexai`

While the "code-bison" model is better at larger code generation based on a text prompt:

    import { GoogleVertexAI } from "langchain/llms/googlevertexai";/* * Before running this, you should make sure you have created a * Google Cloud Project that is permitted to the Vertex AI API. * * You will also need permission to access this project / API. * Typically, this is done in one of three ways: * - You are logged into an account permitted to that project. * - You are running this on a machine using a service account permitted to *   the project. * - The `GOOGLE_APPLICATION_CREDENTIALS` environment variable is set to the *   path of a credentials file for a service account permitted to the project. */const model = new GoogleVertexAI({  model: "code-bison",  maxOutputTokens: 2048,});const res = await model.call("A Javascript function that counts from 1 to 10.");console.log({ res });

#### API Reference:

*   [GoogleVertexAI](/docs/api/llms_googlevertexai/classes/GoogleVertexAI) from `langchain/llms/googlevertexai`