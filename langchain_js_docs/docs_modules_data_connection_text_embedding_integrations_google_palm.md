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

    import { GooglePaLMEmbeddings } from "langchain/embeddings/googlepalm";export const run = async () => {  const model = new GooglePaLMEmbeddings({    apiKey: "<YOUR API KEY>", // or set it in environment variable as `GOOGLE_PALM_API_KEY`    modelName: "models/embedding-gecko-001", // OPTIONAL  });  /* Embed queries */  const res = await model.embedQuery(    "What would be a good company name for a company that makes colorful socks?"  );  console.log({ res });  /* Embed documents */  const documentRes = await model.embedDocuments(["Hello world", "Bye bye"]);  console.log({ documentRes });};

#### API Reference:

*   [GooglePaLMEmbeddings](/docs/api/embeddings_googlepalm/classes/GooglePaLMEmbeddings) from `langchain/embeddings/googlepalm`