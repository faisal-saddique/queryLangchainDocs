ConversationSummaryBufferMemory
===============================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseConversationSummaryMemory`](/docs/api/memory/classes/BaseConversationSummaryMemory).**ConversationSummaryBufferMemory**

Implements[](#implements "Direct link to Implements")
------------------------------------------------------

*   [`ConversationSummaryBufferMemoryInput`](/docs/api/memory/interfaces/ConversationSummaryBufferMemoryInput)

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new ConversationSummaryBufferMemory**(`fields`: [`ConversationSummaryBufferMemoryInput`](/docs/api/memory/interfaces/ConversationSummaryBufferMemoryInput)): [`ConversationSummaryBufferMemory`](/docs/api/memory/classes/ConversationSummaryBufferMemory)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`fields`

[`ConversationSummaryBufferMemoryInput`](/docs/api/memory/interfaces/ConversationSummaryBufferMemoryInput)

#### Returns[](#returns "Direct link to Returns")

[`ConversationSummaryBufferMemory`](/docs/api/memory/classes/ConversationSummaryBufferMemory)

#### Overrides[](#overrides "Direct link to Overrides")

[BaseConversationSummaryMemory](/docs/api/memory/classes/BaseConversationSummaryMemory).[constructor](/docs/api/memory/classes/BaseConversationSummaryMemory#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/memory/summary\_buffer.ts:25](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/summary_buffer.ts#L25)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### aiPrefix[](#aiprefix "Direct link to aiPrefix")

> **aiPrefix**: `string` = `"AI"`

#### Implementation of[](#implementation-of "Direct link to Implementation of")

[ConversationSummaryBufferMemoryInput](/docs/api/memory/interfaces/ConversationSummaryBufferMemoryInput).[aiPrefix](/docs/api/memory/interfaces/ConversationSummaryBufferMemoryInput#aiprefix)

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BaseConversationSummaryMemory](/docs/api/memory/classes/BaseConversationSummaryMemory).[aiPrefix](/docs/api/memory/classes/BaseConversationSummaryMemory#aiprefix)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/memory/summary.ts:32](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/summary.ts#L32)

### chatHistory[](#chathistory "Direct link to chatHistory")

> **chatHistory**: [`BaseChatMessageHistory`](/docs/api/schema/classes/BaseChatMessageHistory)

#### Implementation of[](#implementation-of-1 "Direct link to Implementation of")

[ConversationSummaryBufferMemoryInput](/docs/api/memory/interfaces/ConversationSummaryBufferMemoryInput).[chatHistory](/docs/api/memory/interfaces/ConversationSummaryBufferMemoryInput#chathistory)

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[BaseConversationSummaryMemory](/docs/api/memory/classes/BaseConversationSummaryMemory).[chatHistory](/docs/api/memory/classes/BaseConversationSummaryMemory#chathistory)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:19](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L19)

### humanPrefix[](#humanprefix "Direct link to humanPrefix")

> **humanPrefix**: `string` = `"Human"`

#### Implementation of[](#implementation-of-2 "Direct link to Implementation of")

[ConversationSummaryBufferMemoryInput](/docs/api/memory/interfaces/ConversationSummaryBufferMemoryInput).[humanPrefix](/docs/api/memory/interfaces/ConversationSummaryBufferMemoryInput#humanprefix)

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[BaseConversationSummaryMemory](/docs/api/memory/classes/BaseConversationSummaryMemory).[humanPrefix](/docs/api/memory/classes/BaseConversationSummaryMemory#humanprefix)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/memory/summary.ts:30](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/summary.ts#L30)

### llm[](#llm "Direct link to llm")

> **llm**: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>

#### Implementation of[](#implementation-of-3 "Direct link to Implementation of")

[ConversationSummaryBufferMemoryInput](/docs/api/memory/interfaces/ConversationSummaryBufferMemoryInput).[llm](/docs/api/memory/interfaces/ConversationSummaryBufferMemoryInput#llm)

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[BaseConversationSummaryMemory](/docs/api/memory/classes/BaseConversationSummaryMemory).[llm](/docs/api/memory/classes/BaseConversationSummaryMemory#llm)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/memory/summary.ts:34](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/summary.ts#L34)

### maxTokenLimit[](#maxtokenlimit "Direct link to maxTokenLimit")

> **maxTokenLimit**: `number` = `2000`

#### Implementation of[](#implementation-of-4 "Direct link to Implementation of")

[ConversationSummaryBufferMemoryInput](/docs/api/memory/interfaces/ConversationSummaryBufferMemoryInput).[maxTokenLimit](/docs/api/memory/interfaces/ConversationSummaryBufferMemoryInput#maxtokenlimit)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/memory/summary\_buffer.ts:23](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/summary_buffer.ts#L23)

### memoryKey[](#memorykey "Direct link to memoryKey")

> **memoryKey**: `string` = `"history"`

#### Implementation of[](#implementation-of-5 "Direct link to Implementation of")

[ConversationSummaryBufferMemoryInput](/docs/api/memory/interfaces/ConversationSummaryBufferMemoryInput).[memoryKey](/docs/api/memory/interfaces/ConversationSummaryBufferMemoryInput#memorykey)

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[BaseConversationSummaryMemory](/docs/api/memory/classes/BaseConversationSummaryMemory).[memoryKey](/docs/api/memory/classes/BaseConversationSummaryMemory#memorykey)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/memory/summary.ts:28](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/summary.ts#L28)

### movingSummaryBuffer[](#movingsummarybuffer "Direct link to movingSummaryBuffer")

> **movingSummaryBuffer**: `string` = `""`

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/memory/summary\_buffer.ts:21](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/summary_buffer.ts#L21)

### prompt[](#prompt "Direct link to prompt")

> **prompt**: [`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)<[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\> = `SUMMARY_PROMPT`

#### Implementation of[](#implementation-of-6 "Direct link to Implementation of")

[ConversationSummaryBufferMemoryInput](/docs/api/memory/interfaces/ConversationSummaryBufferMemoryInput).[prompt](/docs/api/memory/interfaces/ConversationSummaryBufferMemoryInput#prompt)

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[BaseConversationSummaryMemory](/docs/api/memory/classes/BaseConversationSummaryMemory).[prompt](/docs/api/memory/classes/BaseConversationSummaryMemory#prompt)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/memory/summary.ts:36](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/summary.ts#L36)

### returnMessages[](#returnmessages "Direct link to returnMessages")

> **returnMessages**: `boolean` = `false`

#### Implementation of[](#implementation-of-7 "Direct link to Implementation of")

[ConversationSummaryBufferMemoryInput](/docs/api/memory/interfaces/ConversationSummaryBufferMemoryInput).[returnMessages](/docs/api/memory/interfaces/ConversationSummaryBufferMemoryInput#returnmessages)

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[BaseConversationSummaryMemory](/docs/api/memory/classes/BaseConversationSummaryMemory).[returnMessages](/docs/api/memory/classes/BaseConversationSummaryMemory#returnmessages)

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:21](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L21)

### summaryChatMessageClass[](#summarychatmessageclass "Direct link to summaryChatMessageClass")

> **summaryChatMessageClass**: `Function` = `SystemMessage`

#### Type declaration[](#type-declaration "Direct link to Type declaration")

> **new summaryChatMessageClass**(`content`: `string`): [`BaseMessage`](/docs/api/schema/classes/BaseMessage)

##### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`content`

`string`

##### Returns[](#returns-1 "Direct link to Returns")

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)

#### Implementation of[](#implementation-of-8 "Direct link to Implementation of")

[ConversationSummaryBufferMemoryInput](/docs/api/memory/interfaces/ConversationSummaryBufferMemoryInput).[summaryChatMessageClass](/docs/api/memory/interfaces/ConversationSummaryBufferMemoryInput#summarychatmessageclass)

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

[BaseConversationSummaryMemory](/docs/api/memory/classes/BaseConversationSummaryMemory).[summaryChatMessageClass](/docs/api/memory/classes/BaseConversationSummaryMemory#summarychatmessageclass)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/memory/summary.ts:38](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/summary.ts#L38)

### inputKey?[](#inputkey "Direct link to inputKey?")

> **inputKey**: `string`

#### Implementation of[](#implementation-of-9 "Direct link to Implementation of")

[ConversationSummaryBufferMemoryInput](/docs/api/memory/interfaces/ConversationSummaryBufferMemoryInput).[inputKey](/docs/api/memory/interfaces/ConversationSummaryBufferMemoryInput#inputkey)

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

[BaseConversationSummaryMemory](/docs/api/memory/classes/BaseConversationSummaryMemory).[inputKey](/docs/api/memory/classes/BaseConversationSummaryMemory#inputkey)

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:23](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L23)

### outputKey?[](#outputkey "Direct link to outputKey?")

> **outputKey**: `string`

#### Implementation of[](#implementation-of-10 "Direct link to Implementation of")

[ConversationSummaryBufferMemoryInput](/docs/api/memory/interfaces/ConversationSummaryBufferMemoryInput).[outputKey](/docs/api/memory/interfaces/ConversationSummaryBufferMemoryInput#outputkey)

#### Inherited from[](#inherited-from-9 "Direct link to Inherited from")

[BaseConversationSummaryMemory](/docs/api/memory/classes/BaseConversationSummaryMemory).[outputKey](/docs/api/memory/classes/BaseConversationSummaryMemory#outputkey)

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:25](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L25)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### memoryKeys[](#memorykeys "Direct link to memoryKeys")

> **memoryKeys**(): `string`\[\]

#### Returns[](#returns-2 "Direct link to Returns")

`string`\[\]

#### Overrides[](#overrides-1 "Direct link to Overrides")

BaseConversationSummaryMemory.memoryKeys

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/memory/summary\_buffer.ts:31](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/summary_buffer.ts#L31)

#### Overrides[](#overrides-2 "Direct link to Overrides")

[BaseConversationSummaryMemory](/docs/api/memory/classes/BaseConversationSummaryMemory).[memoryKeys](/docs/api/memory/classes/BaseConversationSummaryMemory#memorykeys)

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/memory/summary\_buffer.ts:31](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/summary_buffer.ts#L31)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### clear()[](#clear "Direct link to clear()")

> **clear**(): `Promise`<`void`\>

#### Returns[](#returns-3 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[](#overrides-3 "Direct link to Overrides")

[BaseConversationSummaryMemory](/docs/api/memory/classes/BaseConversationSummaryMemory).[clear](/docs/api/memory/classes/BaseConversationSummaryMemory#clear)

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/memory/summary\_buffer.ts:94](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/summary_buffer.ts#L94)

### loadMemoryVariables()[](#loadmemoryvariables "Direct link to loadMemoryVariables()")

> **loadMemoryVariables**(`_`: `InputValues`): `Promise`<`MemoryVariables`\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`_`

`InputValues`

#### Returns[](#returns-4 "Direct link to Returns")

`Promise`<`MemoryVariables`\>

#### Overrides[](#overrides-4 "Direct link to Overrides")

[BaseConversationSummaryMemory](/docs/api/memory/classes/BaseConversationSummaryMemory).[loadMemoryVariables](/docs/api/memory/classes/BaseConversationSummaryMemory#loadmemoryvariables)

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/memory/summary\_buffer.ts:35](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/summary_buffer.ts#L35)

### predictNewSummary()[](#predictnewsummary "Direct link to predictNewSummary()")

> **predictNewSummary**(`messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\], `existingSummary`: `string`): `Promise`<`string`\>

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

`messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]

`existingSummary`

`string`

#### Returns[](#returns-5 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[](#inherited-from-10 "Direct link to Inherited from")

[BaseConversationSummaryMemory](/docs/api/memory/classes/BaseConversationSummaryMemory).[predictNewSummary](/docs/api/memory/classes/BaseConversationSummaryMemory#predictnewsummary)

#### Defined in[](#defined-in-17 "Direct link to Defined in")

[langchain/src/memory/summary.ts:64](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/summary.ts#L64)

### prune()[](#prune "Direct link to prune()")

> **prune**(): `Promise`<`void`\>

#### Returns[](#returns-6 "Direct link to Returns")

`Promise`<`void`\>

#### Defined in[](#defined-in-18 "Direct link to Defined in")

[langchain/src/memory/summary\_buffer.ts:62](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/summary_buffer.ts#L62)

### saveContext()[](#savecontext "Direct link to saveContext()")

> **saveContext**(`inputValues`: `InputValues`, `outputValues`: `OutputValues`): `Promise`<`void`\>

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

`inputValues`

`InputValues`

`outputValues`

`OutputValues`

#### Returns[](#returns-7 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[](#overrides-5 "Direct link to Overrides")

[BaseConversationSummaryMemory](/docs/api/memory/classes/BaseConversationSummaryMemory).[saveContext](/docs/api/memory/classes/BaseConversationSummaryMemory#savecontext)

#### Defined in[](#defined-in-19 "Direct link to Defined in")

[langchain/src/memory/summary\_buffer.ts:54](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/summary_buffer.ts#L54)