Adding memory (state)
=====================

Chains can be initialized with a Memory object, which will persist data across calls to the chain. This makes a Chain stateful.

Get started[](#get-started "Direct link to Get started")
---------------------------------------------------------

    from langchain.chains import ConversationChainfrom langchain.memory import ConversationBufferMemoryconversation = ConversationChain(    llm=chat,    memory=ConversationBufferMemory())conversation.run("Answer briefly. What are the first 3 colors of a rainbow?")# -> The first three colors of a rainbow are red, orange, and yellow.conversation.run("And the next 4?")# -> The next four colors of a rainbow are green, blue, indigo, and violet.

        'The next four colors of a rainbow are green, blue, indigo, and violet.'

Essentially, `BaseMemory` defines an interface of how `langchain` stores memory. It allows reading of stored data through `load_memory_variables` method and storing new data through `save_context` method. You can learn more about it in the [Memory](/docs/modules/memory/) section.