Schema
======

This section covers the basic data types and schemas that are used throughout the codebase.

[

📄️ Text
--------

When working with language models, the primary interface through which you can interact with them is through text. As an over simplification, a lot of models are "text in, text out". Therefor, a lot of the interfaces in LangChain are centered around text.

](/docs/components/schema/text)

[

📄️ ChatMessages
----------------

The primary interface through which end users interact with these is a chat interface. For this reason, some model providers even started providing access to the underlying API in a way that expects chat messages. These messages have a content field (which is usually text) and are associated with a user. Right now the supported users are System, Human, and AI.

](/docs/components/schema/chat-messages)

[

📄️ Examples
------------

Examples are input/output pairs that represent inputs to a function and then expected output. They can be used in both training and evaluation of models.

](/docs/components/schema/examples)

[

📄️ Document
------------

A piece of unstructured data. Consists of page\_content (the content of the data) and metadata (auxiliary pieces of information describing attributes of the data).

](/docs/components/schema/document)