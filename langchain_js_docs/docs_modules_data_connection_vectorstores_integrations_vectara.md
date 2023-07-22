Vectara
=======

Vectara is a developer-first API platform for easily building conversational search experiences.

You can use Vectara as a vector store with LangChain.js.

👉 Embeddings Included[​](#-embeddings-included "Direct link to 👉 Embeddings Included")
----------------------------------------------------------------------------------------

Vectara uses its own embeddings under the hood, so you don't have to provide any yourself or call another service to obtain embeddings.

This also means that if you provide your own embeddings, they'll be a no-op.

    const store = await VectaraStore.fromTexts(  ["hello world", "hi there"],  [{ foo: "bar" }, { foo: "baz" }],  // This won't have an effect. Provide a FakeEmbeddings instance instead for clarity.  new OpenAIEmbeddings(),  args);

Setup[​](#setup "Direct link to Setup")
---------------------------------------

You'll need to:

*   Create a [free Vectara account](https://console.vectara.com/signup).
*   Create a [corpus](https://docs.vectara.com/docs/console-ui/creating-a-corpus) to store your data
*   Create an [API key](https://docs.vectara.com/docs/common-use-cases/app-authn-authz/api-keys) with QueryService and IndexService access so you can access this corpus

Configure your `.env` file or provide args to connect LangChain to your Vectara corpus:

    VECTARA_CUSTOMER_ID=your_customer_idVECTARA_CORPUS_ID=your_corpus_idVECTARA_API_KEY=your-vectara-api-key

Usage[​](#usage "Direct link to Usage")
---------------------------------------

    import { VectaraStore } from "langchain/vectorstores/vectara";import { Document } from "langchain/document";// Create the store.const store = new VectaraStore({  customerId: Number(process.env.VECTARA_CUSTOMER_ID),  corpusId: Number(process.env.VECTARA_CORPUS_ID),  apiKey: String(process.env.VECTARA_API_KEY),  verbose: true,});// Store your data.await store.addDocuments([  new Document({    pageContent: "Do I dare to eat a peach?",    metadata: {      foo: "baz",    },  }),  new Document({    pageContent: "In the room the women come and go talking of Michelangelo",    metadata: {      foo: "bar",    },  }),]);// "Added 2 documents to Vectara"const resultsWithScore = await store.similaritySearchWithScore(  "What were the women talking about?",  1,  {    lambda: 0.025,  });console.log(JSON.stringify(resultsWithScore, null, 2));// [//   [//     {//       "pageContent": "In the room the women come and go talking of Michelangelo",//       "metadata": [//         {//           "name": "lang",//           "value": "eng"//         },//         {//           "name": "offset",//           "value": "0"//         },//         {//           "name": "len",//           "value": "57"//         }//       ]//     },//     0.38169062//   ]// ]

#### API Reference:

*   [VectaraStore](/docs/api/vectorstores_vectara/classes/VectaraStore) from `langchain/vectorstores/vectara`
*   [Document](/docs/api/document/classes/Document) from `langchain/document`

Note that `lambda` is a parameter related to Vectara's hybrid search capbility, providing a tradeoff between neural search and boolean/exact match as described [here](https://docs.vectara.com/docs/api-reference/search-apis/lexical-matching). We recommend the value of 0.025 as a default, while providing a way for advanced users to customize this value if needed.

APIs[​](#apis "Direct link to APIs")
------------------------------------

Vectara's LangChain vector store consumes Vectara's core APIs:

*   [Indexing API](https://docs.vectara.com/docs/indexing-apis/indexing) for storing documents in a Vectara corpus.
*   [Search API](https://docs.vectara.com/docs/search-apis/search) for querying this data. This API supports hybrid search.