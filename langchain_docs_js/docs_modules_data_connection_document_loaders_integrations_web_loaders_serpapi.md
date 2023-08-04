SerpAPI Loader
==============

This guide shows how to use SerpAPI with LangChain to load web search results.

Overview[](#overview "Direct link to Overview")
------------------------------------------------

[SerpAPI](https://serpapi.com/) is a real-time API that provides access to search results from various search engines. It is commonly used for tasks like competitor analysis and rank tracking. It empowers businesses to scrape, extract, and make sense of data from all search engines' result pages.

This guide shows how to load web search results using the `SerpAPILoader` in LangChain. The `SerpAPILoader` simplifies the process of loading and processing web search results from SerpAPI.

Setup[](#setup "Direct link to Setup")
---------------------------------------

You'll need to sign up and retrieve your [SerpAPI API key](https://serpapi.com/dashboard).

Usage[](#usage "Direct link to Usage")
---------------------------------------

Here's an example of how to use the `SerpAPILoader`:

    import { OpenAI } from "langchain/llms/openai";import { RetrievalQAChain } from "langchain/chains";import { MemoryVectorStore } from "langchain/vectorstores/memory";import { OpenAIEmbeddings } from "langchain/embeddings/openai";import { SerpAPILoader } from "langchain/document_loaders/web/serpapi";// Initialize the necessary componentsconst llm = new OpenAI();const embeddings = new OpenAIEmbeddings();const apiKey = "Your SerpAPI API key";// Define your question and queryconst question = "Your question here";const query = "Your query here";// Use SerpAPILoader to load web search resultsconst loader = new SerpAPILoader({ q: query, apiKey });const docs = await loader.load();// Use MemoryVectorStore to store the loaded documents in memoryconst vectorStore = await MemoryVectorStore.fromDocuments(docs, embeddings);// Use RetrievalQAChain to retrieve documents and answer the questionconst chain = RetrievalQAChain.fromLLM(llm, vectorStore.asRetriever());const answer = await chain.call({ query: question });console.log(answer.text);

#### API Reference:

*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [RetrievalQAChain](/docs/api/chains/classes/RetrievalQAChain) from `langchain/chains`
*   [MemoryVectorStore](/docs/api/vectorstores_memory/classes/MemoryVectorStore) from `langchain/vectorstores/memory`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`
*   [SerpAPILoader](/docs/api/document_loaders_web_serpapi/classes/SerpAPILoader) from `langchain/document_loaders/web/serpapi`

In this example, the `SerpAPILoader` is used to load web search results, which are then stored in memory using `MemoryVectorStore`. The `RetrievalQAChain` is then used to retrieve the most relevant documents from the memory and answer the question based on these documents. This demonstrates how the `SerpAPILoader` can streamline the process of loading and processing web search results.