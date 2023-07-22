ConversationSummaryMemory
=========================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseChatMemory`](/docs/api/memory/classes/BaseChatMemory).**ConversationSummaryMemory**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new ConversationSummaryMemory**(`fields`: [`ConversationSummaryMemoryInput`](/docs/api/memory/interfaces/ConversationSummaryMemoryInput)): [`ConversationSummaryMemory`](/docs/api/memory/classes/ConversationSummaryMemory)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields`

[`ConversationSummaryMemoryInput`](/docs/api/memory/interfaces/ConversationSummaryMemoryInput)

#### Returns[​](#returns "Direct link to Returns")

[`ConversationSummaryMemory`](/docs/api/memory/classes/ConversationSummaryMemory)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[constructor](/docs/api/memory/classes/BaseChatMemory#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/memory/summary.ts:38](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/summary.ts#L38)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### aiPrefix[​](#aiprefix "Direct link to aiPrefix")

> **aiPrefix**: `string` = `"AI"`

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/memory/summary.ts:30](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/summary.ts#L30)

### buffer[​](#buffer "Direct link to buffer")

> **buffer**: `string` = `""`

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/memory/summary.ts:24](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/summary.ts#L24)

### chatHistory[​](#chathistory "Direct link to chatHistory")

> **chatHistory**: [`BaseChatMessageHistory`](/docs/api/schema/classes/BaseChatMessageHistory)

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[chatHistory](/docs/api/memory/classes/BaseChatMemory#chathistory)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:19](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/chat_memory.ts#L19)

### humanPrefix[​](#humanprefix "Direct link to humanPrefix")

> **humanPrefix**: `string` = `"Human"`

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/memory/summary.ts:28](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/summary.ts#L28)

### llm[​](#llm "Direct link to llm")

> **llm**: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/memory/summary.ts:32](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/summary.ts#L32)

### memoryKey[​](#memorykey "Direct link to memoryKey")

> **memoryKey**: `string` = `"history"`

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/memory/summary.ts:26](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/summary.ts#L26)

### prompt[​](#prompt "Direct link to prompt")

> **prompt**: [`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate) = `SUMMARY_PROMPT`

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/memory/summary.ts:34](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/summary.ts#L34)

### returnMessages[​](#returnmessages "Direct link to returnMessages")

> **returnMessages**: `boolean` = `false`

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[returnMessages](/docs/api/memory/classes/BaseChatMemory#returnmessages)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:21](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/chat_memory.ts#L21)

### summaryChatMessageClass[​](#summarychatmessageclass "Direct link to summaryChatMessageClass")

> **summaryChatMessageClass**: `Function` = `SystemMessage`

#### Type declaration[​](#type-declaration "Direct link to Type declaration")

> **new summaryChatMessageClass**(`content`: `string`): [`BaseMessage`](/docs/api/schema/classes/BaseMessage)

##### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`content`

`string`

##### Returns[​](#returns-1 "Direct link to Returns")

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/memory/summary.ts:36](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/summary.ts#L36)

### inputKey?[​](#inputkey "Direct link to inputKey?")

> **inputKey**: `string`

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[inputKey](/docs/api/memory/classes/BaseChatMemory#inputkey)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/chat_memory.ts#L23)

### outputKey?[​](#outputkey "Direct link to outputKey?")

> **outputKey**: `string`

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[outputKey](/docs/api/memory/classes/BaseChatMemory#outputkey)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:25](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/chat_memory.ts#L25)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### memoryKeys[​](#memorykeys "Direct link to memoryKeys")

> **memoryKeys**(): `string`\[\]

#### Returns[​](#returns-2 "Direct link to Returns")

`string`\[\]

#### Overrides[​](#overrides-1 "Direct link to Overrides")

BaseChatMemory.memoryKeys

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/memory/summary.ts:62](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/summary.ts#L62)

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[memoryKeys](/docs/api/memory/classes/BaseChatMemory#memorykeys)

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/memory/summary.ts:62](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/summary.ts#L62)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### clear()[​](#clear "Direct link to clear()")

> **clear**(): `Promise`<`void`\>

#### Returns[​](#returns-3 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[​](#overrides-3 "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[clear](/docs/api/memory/classes/BaseChatMemory#clear)

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/memory/summary.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/summary.ts#L98)

### loadMemoryVariables()[​](#loadmemoryvariables "Direct link to loadMemoryVariables()")

> **loadMemoryVariables**(`_`: `InputValues`): `Promise`<`MemoryVariables`\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`_`

`InputValues`

#### Returns[​](#returns-4 "Direct link to Returns")

`Promise`<`MemoryVariables`\>

#### Overrides[​](#overrides-4 "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[loadMemoryVariables](/docs/api/memory/classes/BaseChatMemory#loadmemoryvariables)

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/memory/summary.ts:78](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/summary.ts#L78)

### predictNewSummary()[​](#predictnewsummary "Direct link to predictNewSummary()")

> **predictNewSummary**(`messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\], `existingSummary`: `string`): `Promise`<`string`\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]

`existingSummary`

`string`

#### Returns[​](#returns-5 "Direct link to Returns")

`Promise`<`string`\>

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/memory/summary.ts:66](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/summary.ts#L66)

### saveContext()[​](#savecontext "Direct link to saveContext()")

> **saveContext**(`inputValues`: `InputValues`, `outputValues`: `OutputValues`): `Promise`<`void`\>

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`inputValues`

`InputValues`

`outputValues`

`OutputValues`

#### Returns[​](#returns-6 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[​](#overrides-5 "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[saveContext](/docs/api/memory/classes/BaseChatMemory#savecontext)

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/memory/summary.ts:89](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/summary.ts#L89)