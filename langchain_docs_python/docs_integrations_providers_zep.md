Zep
===

> [Zep](https://docs.getzep.com/) - A long-term memory store for LLM applications.

> `Zep` stores, summarizes, embeds, indexes, and enriches conversational AI chat histories, and exposes them via simple, low-latency APIs.
> 
> *   Long-term memory persistence, with access to historical messages irrespective of your summarization strategy.
> *   Auto-summarization of memory messages based on a configurable message window. A series of summaries are stored, providing flexibility for future summarization strategies.
> *   Vector search over memories, with messages automatically embedded on creation.
> *   Auto-token counting of memories and summaries, allowing finer-grained control over prompt assembly.
> *   Python and JavaScript SDKs.

`Zep` [project](https://github.com/getzep/zep)

Installation and Setup[](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

    pip install zep_python

Retriever[](#retriever "Direct link to Retriever")
---------------------------------------------------

See a [usage example](/docs/integrations/retrievers/zep_memorystore).

    from langchain.retrievers import ZepRetriever