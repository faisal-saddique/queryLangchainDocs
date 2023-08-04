Remote Retriever
================

This example shows how to use a Remote Retriever in a `RetrievalQAChain` to retrieve documents from a remote server.

Usage[](#usage "Direct link to Usage")
---------------------------------------

    import { OpenAI } from "langchain/llms/openai";import { RetrievalQAChain } from "langchain/chains";import { RemoteLangChainRetriever } from "langchain/retrievers/remote";export const run = async () => {  // Initialize the LLM to use to answer the question.  const model = new OpenAI({});  // Initialize the remote retriever.  const retriever = new RemoteLangChainRetriever({    url: "http://0.0.0.0:8080/retrieve", // Replace with your own URL.    auth: { bearer: "foo" }, // Replace with your own auth.    inputKey: "message",    responseKey: "response",  });  // Create a chain that uses the OpenAI LLM and remote retriever.  const chain = RetrievalQAChain.fromLLM(model, retriever);  // Call the chain with a query.  const res = await chain.call({    query: "What did the president say about Justice Breyer?",  });  console.log({ res });  /*  {    res: {      text: 'The president said that Justice Breyer was an Army veteran, Constitutional scholar,      and retiring Justice of the United States Supreme Court and thanked him for his service.'    }  }  */};

#### API Reference:

*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [RetrievalQAChain](/docs/api/chains/classes/RetrievalQAChain) from `langchain/chains`
*   [RemoteLangChainRetriever](/docs/api/retrievers_remote/classes/RemoteLangChainRetriever) from `langchain/retrievers/remote`