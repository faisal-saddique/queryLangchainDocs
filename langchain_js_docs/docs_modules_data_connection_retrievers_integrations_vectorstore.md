Vector Store
============

Once you've created a [Vector Store](/docs/modules/data_connection/vectorstores), the way to use it as a Retriever is very simple:

    vectorStore = ...retriever = vectorStore.asRetriever()