ChatGPT Plugin Retriever
========================

This example shows how to use the ChatGPT Retriever Plugin within LangChain.

To set up the ChatGPT Retriever Plugin, please follow instructions [here](https://github.com/openai/chatgpt-retrieval-plugin).

Usage[​](#usage "Direct link to Usage")
---------------------------------------

    import { ChatGPTPluginRetriever } from "langchain/retrievers/remote";export const run = async () => {  const retriever = new ChatGPTPluginRetriever({    url: "http://0.0.0.0:8000",    auth: {      bearer: "super-secret-jwt-token-with-at-least-32-characters-long",    },  });  const docs = await retriever.getRelevantDocuments("hello world");  console.log(docs);};

#### API Reference:

*   [ChatGPTPluginRetriever](/docs/api/retrievers_remote/classes/ChatGPTPluginRetriever) from `langchain/retrievers/remote`