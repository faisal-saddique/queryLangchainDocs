GoogleVertexAIChatMessage
=========================

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new GoogleVertexAIChatMessage**(`fields`: [`GoogleVertexAIChatMessageFields`](/docs/api/chat_models_googlevertexai/types/GoogleVertexAIChatMessageFields)): [`GoogleVertexAIChatMessage`](/docs/api/chat_models_googlevertexai/classes/GoogleVertexAIChatMessage)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`fields`

[`GoogleVertexAIChatMessageFields`](/docs/api/chat_models_googlevertexai/types/GoogleVertexAIChatMessageFields)

#### Returns[](#returns "Direct link to Returns")

[`GoogleVertexAIChatMessage`](/docs/api/chat_models_googlevertexai/classes/GoogleVertexAIChatMessage)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/chat\_models/googlevertexai.ts:51](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/googlevertexai.ts#L51)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### content[](#content "Direct link to content")

> **content**: `string`

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/chat\_models/googlevertexai.ts:47](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/googlevertexai.ts#L47)

### author?[](#author "Direct link to author?")

> **author**: [`GoogleVertexAIChatAuthor`](/docs/api/chat_models_googlevertexai/types/GoogleVertexAIChatAuthor)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/chat\_models/googlevertexai.ts:45](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/googlevertexai.ts#L45)

### name?[](#name "Direct link to name?")

> **name**: `string`

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/chat\_models/googlevertexai.ts:49](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/googlevertexai.ts#L49)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### extractGenericMessageCustomRole()[](#extractgenericmessagecustomrole "Direct link to extractGenericMessageCustomRole()")

> `Static` **extractGenericMessageCustomRole**(`message`: [`ChatMessage`](/docs/api/schema/classes/ChatMessage)): [`GoogleVertexAIChatAuthor`](/docs/api/chat_models_googlevertexai/types/GoogleVertexAIChatAuthor)

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`message`

[`ChatMessage`](/docs/api/schema/classes/ChatMessage)

#### Returns[](#returns-1 "Direct link to Returns")

[`GoogleVertexAIChatAuthor`](/docs/api/chat_models_googlevertexai/types/GoogleVertexAIChatAuthor)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/chat\_models/googlevertexai.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/googlevertexai.ts#L57)

### fromChatMessage()[](#fromchatmessage "Direct link to fromChatMessage()")

> `Static` **fromChatMessage**(`message`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage), `model`: `string`): [`GoogleVertexAIChatMessage`](/docs/api/chat_models_googlevertexai/classes/GoogleVertexAIChatMessage)

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`message`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)

`model`

`string`

#### Returns[](#returns-2 "Direct link to Returns")

[`GoogleVertexAIChatMessage`](/docs/api/chat_models_googlevertexai/classes/GoogleVertexAIChatMessage)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/chat\_models/googlevertexai.ts:96](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/googlevertexai.ts#L96)

### mapMessageTypeToVertexChatAuthor()[](#mapmessagetypetovertexchatauthor "Direct link to mapMessageTypeToVertexChatAuthor()")

> `Static` **mapMessageTypeToVertexChatAuthor**(`message`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage), `model`: `string`): [`GoogleVertexAIChatAuthor`](/docs/api/chat_models_googlevertexai/types/GoogleVertexAIChatAuthor)

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

`message`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)

`model`

`string`

#### Returns[](#returns-3 "Direct link to Returns")

[`GoogleVertexAIChatAuthor`](/docs/api/chat_models_googlevertexai/types/GoogleVertexAIChatAuthor)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/chat\_models/googlevertexai.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/googlevertexai.ts#L70)