Examples: Memory
================

[

📄️ Buffer Memory
-----------------

BufferMemory is the simplest type of memory - it just remembers previous conversational back and forths directly.

](/docs/modules/memory/integrations/buffer_memory)

[

📄️ Using Buffer Memory with Chat Models
----------------------------------------

This example covers how to use chat-specific memory classes with chat models.

](/docs/modules/memory/integrations/buffer_memory_chat)

[

📄️ Buffer Window Memory
------------------------

BufferWindowMemory keeps track of the back-and-forths in conversation, and then uses a window of size k to surface the last k back-and-forths to use as memory.

](/docs/modules/memory/integrations/buffer_window_memory)

[

📄️ Conversation Summary
------------------------

The Conversation Summary Memory summarizes the conversation as it happens and stores the current summary in memory. This memory can then be used to inject the summary of the conversation so far into a prompt/chain. This memory is most useful for longer conversations, where keeping the past message history in the prompt verbatim would take up too many tokens.

](/docs/modules/memory/integrations/conversation_summary)

[

📄️ DynamoDB-Backed Chat Memory
-------------------------------

For longer-term persistence across chat sessions, you can swap out the default in-memory chatHistory that backs chat memory classes like BufferMemory for a DynamoDB instance.

](/docs/modules/memory/integrations/dynamodb)

[

📄️ Entity Memory
-----------------

Entity Memory remembers given facts about specific entities in a conversation.

](/docs/modules/memory/integrations/entity_memory)

[

📄️ Firestore Chat Memory
-------------------------

For longer-term persistence across chat sessions, you can swap out the default in-memory chatHistory that backs chat memory classes like BufferMemory for a firestore.

](/docs/modules/memory/integrations/firestore)

[

📄️ Momento-Backed Chat Memory
------------------------------

For distributed, serverless persistence across chat sessions, you can swap in a Momento-backed chat message history.

](/docs/modules/memory/integrations/momento)

[

📄️ Motörhead Memory
--------------------

Motörhead is a memory server implemented in Rust. It automatically handles incremental summarization in the background and allows for stateless applications.

](/docs/modules/memory/integrations/motorhead_memory)

[

📄️ PlanetScale Chat Memory
---------------------------

Because PlanetScale works via a REST API, you can use this with Vercel Edge, Cloudflare Workers and other Serverless environments.

](/docs/modules/memory/integrations/planetscale)

[

📄️ Redis-Backed Chat Memory
----------------------------

For longer-term persistence across chat sessions, you can swap out the default in-memory chatHistory that backs chat memory classes like BufferMemory for a Redis instance.

](/docs/modules/memory/integrations/redis)

[

📄️ Upstash Redis-Backed Chat Memory
------------------------------------

Because Upstash Redis works via a REST API, you can use this with Vercel Edge, Cloudflare Workers and other Serverless environments.

](/docs/modules/memory/integrations/upstash_redis)

[

📄️ VectorStore-Backed Memory
-----------------------------

VectorStoreRetrieverMemory stores memories in a VectorDB and queries the top-K most "salient" docs every time it is called.

](/docs/modules/memory/integrations/vector_store_memory)

[

📄️ Zep Memory
--------------

Zep is a memory server that stores, summarizes, embeds, indexes, and enriches conversational AI chat histories, autonomous agent histories, document Q&A histories and exposes them via simple, low-latency APIs.

](/docs/modules/memory/integrations/zep_memory)