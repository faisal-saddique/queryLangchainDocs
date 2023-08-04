ConversationSummaryMemoryInput
==============================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseConversationSummaryMemoryInput`](/docs/api/memory/interfaces/BaseConversationSummaryMemoryInput).**ConversationSummaryMemoryInput**

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### llm[](#llm "Direct link to llm")

> **llm**: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BaseConversationSummaryMemoryInput](/docs/api/memory/interfaces/BaseConversationSummaryMemoryInput).[llm](/docs/api/memory/interfaces/BaseConversationSummaryMemoryInput#llm)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/memory/summary.ts:19](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/summary.ts#L19)

### aiPrefix?[](#aiprefix "Direct link to aiPrefix?")

> **aiPrefix**: `string`

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[BaseConversationSummaryMemoryInput](/docs/api/memory/interfaces/BaseConversationSummaryMemoryInput).[aiPrefix](/docs/api/memory/interfaces/BaseConversationSummaryMemoryInput#aiprefix)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/memory/summary.ts:22](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/summary.ts#L22)

### chatHistory?[](#chathistory "Direct link to chatHistory?")

> **chatHistory**: [`BaseChatMessageHistory`](/docs/api/schema/classes/BaseChatMessageHistory)

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[BaseConversationSummaryMemoryInput](/docs/api/memory/interfaces/BaseConversationSummaryMemoryInput).[chatHistory](/docs/api/memory/interfaces/BaseConversationSummaryMemoryInput#chathistory)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:12](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L12)

### humanPrefix?[](#humanprefix "Direct link to humanPrefix?")

> **humanPrefix**: `string`

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[BaseConversationSummaryMemoryInput](/docs/api/memory/interfaces/BaseConversationSummaryMemoryInput).[humanPrefix](/docs/api/memory/interfaces/BaseConversationSummaryMemoryInput#humanprefix)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/memory/summary.ts:21](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/summary.ts#L21)

### inputKey?[](#inputkey "Direct link to inputKey?")

> **inputKey**: `string`

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[BaseConversationSummaryMemoryInput](/docs/api/memory/interfaces/BaseConversationSummaryMemoryInput).[inputKey](/docs/api/memory/interfaces/BaseConversationSummaryMemoryInput#inputkey)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:14](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L14)

### memoryKey?[](#memorykey "Direct link to memoryKey?")

> **memoryKey**: `string`

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[BaseConversationSummaryMemoryInput](/docs/api/memory/interfaces/BaseConversationSummaryMemoryInput).[memoryKey](/docs/api/memory/interfaces/BaseConversationSummaryMemoryInput#memorykey)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/memory/summary.ts:20](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/summary.ts#L20)

### outputKey?[](#outputkey "Direct link to outputKey?")

> **outputKey**: `string`

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[BaseConversationSummaryMemoryInput](/docs/api/memory/interfaces/BaseConversationSummaryMemoryInput).[outputKey](/docs/api/memory/interfaces/BaseConversationSummaryMemoryInput#outputkey)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:15](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L15)

### prompt?[](#prompt "Direct link to prompt?")

> **prompt**: [`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)<[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\>

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

[BaseConversationSummaryMemoryInput](/docs/api/memory/interfaces/BaseConversationSummaryMemoryInput).[prompt](/docs/api/memory/interfaces/BaseConversationSummaryMemoryInput#prompt)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/memory/summary.ts:23](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/summary.ts#L23)

### returnMessages?[](#returnmessages "Direct link to returnMessages?")

> **returnMessages**: `boolean`

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

[BaseConversationSummaryMemoryInput](/docs/api/memory/interfaces/BaseConversationSummaryMemoryInput).[returnMessages](/docs/api/memory/interfaces/BaseConversationSummaryMemoryInput#returnmessages)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:13](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L13)

### summaryChatMessageClass?[](#summarychatmessageclass "Direct link to summaryChatMessageClass?")

> **summaryChatMessageClass**: `Function`

#### Type declaration[](#type-declaration "Direct link to Type declaration")

> **new summaryChatMessageClass**(`content`: `string`): [`BaseMessage`](/docs/api/schema/classes/BaseMessage)

##### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`content`

`string`

##### Returns[](#returns "Direct link to Returns")

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)

#### Inherited from[](#inherited-from-9 "Direct link to Inherited from")

[BaseConversationSummaryMemoryInput](/docs/api/memory/interfaces/BaseConversationSummaryMemoryInput).[summaryChatMessageClass](/docs/api/memory/interfaces/BaseConversationSummaryMemoryInput#summarychatmessageclass)

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/memory/summary.ts:24](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/summary.ts#L24)