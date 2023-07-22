ChatMessages
============

The primary interface through which end users interact with these is a chat interface. For this reason, some model providers even started providing access to the underlying API in a way that expects chat messages. These messages have a content field (which is usually text) and are associated with a user. Right now the supported users are System, Human, and AI.

### SystemChatMessage[​](#systemchatmessage "Direct link to SystemChatMessage")

A chat message representing information that should be instructions to the AI system.

### HumanChatMessage[​](#humanchatmessage "Direct link to HumanChatMessage")

A chat message representing information coming from a human interacting with the AI system.

### AIChatMessage[​](#aichatmessage "Direct link to AIChatMessage")

A chat message representing information coming from the AI system.