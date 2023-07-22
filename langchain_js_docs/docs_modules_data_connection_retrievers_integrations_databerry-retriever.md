Databerry Retriever
===================

This example shows how to use the Databerry Retriever in a `RetrievalQAChain` to retrieve documents from a Databerry.ai datastore.

Usage[​](#usage "Direct link to Usage")
---------------------------------------

    import { DataberryRetriever } from "langchain/retrievers/databerry";export const run = async () => {  const retriever = new DataberryRetriever({    datastoreUrl: "https://api.databerry.ai/query/clg1xg2h80000l708dymr0fxc",    apiKey: "DATABERRY_API_KEY", // optional: needed for private datastores    topK: 8, // optional: default value is 3  });  const docs = await retriever.getRelevantDocuments("hello");  console.log(docs);};

#### API Reference:

*   [DataberryRetriever](/docs/api/retrievers_databerry/classes/DataberryRetriever) from `langchain/retrievers/databerry`