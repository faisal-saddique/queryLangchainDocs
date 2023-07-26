How to
======

[

📄️ Async API
-------------

LangChain provides async support for Chains by leveraging the asyncio library.

](/docs/modules/chains/how_to/async_chain)

[

📄️ Different call methods
--------------------------

All classes inherited from Chain offer a few ways of running chain logic. The most direct one is by using call:

](/docs/modules/chains/how_to/call_methods)

[

📄️ Custom chain
----------------

To implement your own custom chain you can subclass Chain and implement the following methods:

](/docs/modules/chains/how_to/custom_chain)

[

📄️ Debugging chains
--------------------

It can be hard to debug a Chain object solely from its output as most Chain objects involve a fair amount of input prompt preprocessing and LLM output post-processing.

](/docs/modules/chains/how_to/debugging)

[

📄️ Loading from LangChainHub
-----------------------------

This notebook covers how to load chains from LangChainHub.

](/docs/modules/chains/how_to/from_hub)

[

📄️ Adding memory (state)
-------------------------

Chains can be initialized with a Memory object, which will persist data across calls to the chain. This makes a Chain stateful.

](/docs/modules/chains/how_to/memory)

[

📄️ Serialization
-----------------

This notebook covers how to serialize chains to and from disk. The serialization format we use is json or yaml. Currently, only some chains support this type of serialization. We will grow the number of supported chains over time.

](/docs/modules/chains/how_to/serialization)