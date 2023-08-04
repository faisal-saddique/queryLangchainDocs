BaseConversationSummaryMemory
=============================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseChatMemory`](/docs/api/memory/classes/BaseChatMemory).**BaseConversationSummaryMemory**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new BaseConversationSummaryMemory**(`fields`: [`BaseConversationSummaryMemoryInput`](/docs/api/memory/interfaces/BaseConversationSummaryMemoryInput)): [`BaseConversationSummaryMemory`](/docs/api/memory/classes/BaseConversationSummaryMemory)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`fields`

[`BaseConversationSummaryMemoryInput`](/docs/api/memory/interfaces/BaseConversationSummaryMemoryInput)

#### Returns[](#returns "Direct link to Returns")

[`BaseConversationSummaryMemory`](/docs/api/memory/classes/BaseConversationSummaryMemory)

#### Overrides[](#overrides "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[constructor](/docs/api/memory/classes/BaseChatMemory#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/memory/summary.ts:40](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/summary.ts#L40)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### aiPrefix[](#aiprefix "Direct link to aiPrefix")

> **aiPrefix**: `string` = `"AI"`

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/memory/summary.ts:32](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/summary.ts#L32)

### chatHistory[](#chathistory "Direct link to chatHistory")

> **chatHistory**: [`BaseChatMessageHistory`](/docs/api/schema/classes/BaseChatMessageHistory)

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[chatHistory](/docs/api/memory/classes/BaseChatMemory#chathistory)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:19](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L19)

### humanPrefix[](#humanprefix "Direct link to humanPrefix")

> **humanPrefix**: `string` = `"Human"`

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/memory/summary.ts:30](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/summary.ts#L30)

### llm[](#llm "Direct link to llm")

> **llm**: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/memory/summary.ts:34](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/summary.ts#L34)

### memoryKey[](#memorykey "Direct link to memoryKey")

> **memoryKey**: `string` = `"history"`

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/memory/summary.ts:28](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/summary.ts#L28)

### prompt[](#prompt "Direct link to prompt")

> **prompt**: [`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)<[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\> = `SUMMARY_PROMPT`

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/memory/summary.ts:36](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/summary.ts#L36)

### returnMessages[](#returnmessages "Direct link to returnMessages")

> **returnMessages**: `boolean` = `false`

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[returnMessages](/docs/api/memory/classes/BaseChatMemory#returnmessages)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

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

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/memory/summary.ts:38](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/summary.ts#L38)

### inputKey?[](#inputkey "Direct link to inputKey?")

> **inputKey**: `string`

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[inputKey](/docs/api/memory/classes/BaseChatMemory#inputkey)

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:23](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L23)

### outputKey?[](#outputkey "Direct link to outputKey?")

> **outputKey**: `string`

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[outputKey](/docs/api/memory/classes/BaseChatMemory#outputkey)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:25](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L25)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### memoryKeys[](#memorykeys "Direct link to memoryKeys")

> `Abstract` **memoryKeys**(): `string`\[\]

#### Returns[](#returns-2 "Direct link to Returns")

`string`\[\]

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

BaseChatMemory.memoryKeys

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/memory/base.ts:10](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/base.ts#L10)

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[memoryKeys](/docs/api/memory/classes/BaseChatMemory#memorykeys)

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/memory/base.ts:10](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/base.ts#L10)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### clear()[](#clear "Direct link to clear()")

> **clear**(): `Promise`<`void`\>

#### Returns[](#returns-3 "Direct link to Returns")

`Promise`<`void`\>

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[clear](/docs/api/memory/classes/BaseChatMemory#clear)

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L48)

### loadMemoryVariables()[](#loadmemoryvariables "Direct link to loadMemoryVariables()")

> `Abstract` **loadMemoryVariables**(`values`: `InputValues`): `Promise`<`MemoryVariables`\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`values`

`InputValues`

#### Returns[](#returns-4 "Direct link to Returns")

`Promise`<`MemoryVariables`\>

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[loadMemoryVariables](/docs/api/memory/classes/BaseChatMemory#loadmemoryvariables)

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/memory/base.ts:12](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/base.ts#L12)

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

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/memory/summary.ts:64](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/summary.ts#L64)

### saveContext()[](#savecontext "Direct link to saveContext()")

> **saveContext**(`inputValues`: `InputValues`, `outputValues`: `OutputValues`): `Promise`<`void`\>

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

`inputValues`

`InputValues`

`outputValues`

`OutputValues`

#### Returns[](#returns-6 "Direct link to Returns")

`Promise`<`void`\>

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[saveContext](/docs/api/memory/classes/BaseChatMemory#savecontext)

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:35](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L35)