Memory
======

info

[Python Guide](https://python.langchain.com/en/latest/modules/memory.html)

[JS Guide](https://js.langchain.com/docs/modules/memory/)

Memory is the concept of storing and retrieving data in the process of a conversation. There are two main methods:

1.  Based on input, fetch any relevant pieces of data
2.  Based on the input and output, update state accordingly

There are two main types of memory: short term and long term.

Short term memory generally refers to how to pass data in the context of a singular conversation (generally is previous ChatMessages or summaries of them).

Long term memory deals with how to fetch and update information between conversations.

Go deeper[​](#go-deeper "Direct link to Go deeper")
---------------------------------------------------

[

📄️ Chat Message History
------------------------

The primary interface with language models at the moment in through a chat interface. The ChatMessageHistory class is responsible for remembering all previous chat interactions. These can then be passed directly back into the model, summarized in some way, or some combination.

](/docs/components/memory/chat_message_history)