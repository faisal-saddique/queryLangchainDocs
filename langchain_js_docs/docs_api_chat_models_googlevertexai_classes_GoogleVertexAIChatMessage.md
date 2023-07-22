GoogleVertexAIChatMessage
=========================

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new GoogleVertexAIChatMessage**(`fields`: [`GoogleVertexAIChatMessageFields`](/docs/api/chat_models_googlevertexai/types/GoogleVertexAIChatMessageFields)): [`GoogleVertexAIChatMessage`](/docs/api/chat_models_googlevertexai/classes/GoogleVertexAIChatMessage)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields`

[`GoogleVertexAIChatMessageFields`](/docs/api/chat_models_googlevertexai/types/GoogleVertexAIChatMessageFields)

#### Returns[​](#returns "Direct link to Returns")

[`GoogleVertexAIChatMessage`](/docs/api/chat_models_googlevertexai/classes/GoogleVertexAIChatMessage)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/chat\_models/googlevertexai.ts:50](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/googlevertexai.ts#L50)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### content[​](#content "Direct link to content")

> **content**: `string`

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/chat\_models/googlevertexai.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/googlevertexai.ts#L46)

### author?[​](#author "Direct link to author?")

> **author**: [`GoogleVertexAIChatAuthor`](/docs/api/chat_models_googlevertexai/types/GoogleVertexAIChatAuthor)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/chat\_models/googlevertexai.ts:44](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/googlevertexai.ts#L44)

### name?[​](#name "Direct link to name?")

> **name**: `string`

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/chat\_models/googlevertexai.ts:48](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/googlevertexai.ts#L48)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### fromChatMessage()[​](#fromchatmessage "Direct link to fromChatMessage()")

> `Static` **fromChatMessage**(`message`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage), `model`: `string`): [`GoogleVertexAIChatMessage`](/docs/api/chat_models_googlevertexai/classes/GoogleVertexAIChatMessage)

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`message`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)

`model`

`string`

#### Returns[​](#returns-1 "Direct link to Returns")

[`GoogleVertexAIChatMessage`](/docs/api/chat_models_googlevertexai/classes/GoogleVertexAIChatMessage)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/chat\_models/googlevertexai.ts:76](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/googlevertexai.ts#L76)

### mapMessageTypeToVertexChatAuthor()[​](#mapmessagetypetovertexchatauthor "Direct link to mapMessageTypeToVertexChatAuthor()")

> `Static` **mapMessageTypeToVertexChatAuthor**(`baseMessageType`: [`MessageType`](/docs/api/schema/types/MessageType), `model`: `string`): [`GoogleVertexAIChatAuthor`](/docs/api/chat_models_googlevertexai/types/GoogleVertexAIChatAuthor)

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`baseMessageType`

[`MessageType`](/docs/api/schema/types/MessageType)

`model`

`string`

#### Returns[​](#returns-2 "Direct link to Returns")

[`GoogleVertexAIChatAuthor`](/docs/api/chat_models_googlevertexai/types/GoogleVertexAIChatAuthor)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/chat\_models/googlevertexai.ts:56](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/googlevertexai.ts#L56)