EntityMemory
============

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseChatMemory`](/docs/api/memory/classes/BaseChatMemory).**EntityMemory**

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   `EntityMemoryInput`

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new EntityMemory**(`fields`: `EntityMemoryInput`): [`EntityMemory`](/docs/api/memory/classes/EntityMemory)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields`

`EntityMemoryInput`

#### Returns[​](#returns "Direct link to Returns")

[`EntityMemory`](/docs/api/memory/classes/EntityMemory)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[constructor](/docs/api/memory/classes/BaseChatMemory#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/memory/entity\_memory.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/entity_memory.ts#L55)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### chatHistory[​](#chathistory "Direct link to chatHistory")

> **chatHistory**: [`BaseChatMessageHistory`](/docs/api/schema/classes/BaseChatMessageHistory)

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

EntityMemoryInput.chatHistory

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[chatHistory](/docs/api/memory/classes/BaseChatMemory#chathistory)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:19](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/chat_memory.ts#L19)

### chatHistoryKey[​](#chathistorykey "Direct link to chatHistoryKey")

> **chatHistoryKey**: `string` = `"history"`

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

EntityMemoryInput.chatHistoryKey

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/memory/entity\_memory.ts:45](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/entity_memory.ts#L45)

### entitiesKey[​](#entitieskey "Direct link to entitiesKey")

> **entitiesKey**: `string` = `"entities"`

#### Implementation of[​](#implementation-of-2 "Direct link to Implementation of")

EntityMemoryInput.entitiesKey

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/memory/entity\_memory.ts:49](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/entity_memory.ts#L49)

### entityCache[​](#entitycache "Direct link to entityCache")

> **entityCache**: `string`\[\] = `[]`

#### Implementation of[​](#implementation-of-3 "Direct link to Implementation of")

EntityMemoryInput.entityCache

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/memory/entity\_memory.ts:41](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/entity_memory.ts#L41)

### entityStore[​](#entitystore "Direct link to entityStore")

> **entityStore**: [`BaseEntityStore`](/docs/api/schema/classes/BaseEntityStore)

#### Implementation of[​](#implementation-of-4 "Direct link to Implementation of")

EntityMemoryInput.entityStore

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/memory/entity\_memory.ts:39](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/entity_memory.ts#L39)

### k[​](#k "Direct link to k")

> **k**: `number` = `3`

#### Implementation of[​](#implementation-of-5 "Direct link to Implementation of")

EntityMemoryInput.k

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/memory/entity\_memory.ts:43](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/entity_memory.ts#L43)

### llm[​](#llm "Direct link to llm")

> **llm**: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)

#### Implementation of[​](#implementation-of-6 "Direct link to Implementation of")

EntityMemoryInput.llm

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/memory/entity\_memory.ts:47](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/entity_memory.ts#L47)

### returnMessages[​](#returnmessages "Direct link to returnMessages")

> **returnMessages**: `boolean` = `false`

#### Implementation of[​](#implementation-of-7 "Direct link to Implementation of")

EntityMemoryInput.returnMessages

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[returnMessages](/docs/api/memory/classes/BaseChatMemory#returnmessages)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:21](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/chat_memory.ts#L21)

### aiPrefix?[​](#aiprefix "Direct link to aiPrefix?")

> **aiPrefix**: `string`

#### Implementation of[​](#implementation-of-8 "Direct link to Implementation of")

EntityMemoryInput.aiPrefix

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/memory/entity\_memory.ts:53](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/entity_memory.ts#L53)

### humanPrefix?[​](#humanprefix "Direct link to humanPrefix?")

> **humanPrefix**: `string`

#### Implementation of[​](#implementation-of-9 "Direct link to Implementation of")

EntityMemoryInput.humanPrefix

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/memory/entity\_memory.ts:51](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/entity_memory.ts#L51)

### inputKey?[​](#inputkey "Direct link to inputKey?")

> **inputKey**: `string`

#### Implementation of[​](#implementation-of-10 "Direct link to Implementation of")

EntityMemoryInput.inputKey

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[inputKey](/docs/api/memory/classes/BaseChatMemory#inputkey)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/chat_memory.ts#L23)

### outputKey?[​](#outputkey "Direct link to outputKey?")

> **outputKey**: `string`

#### Implementation of[​](#implementation-of-11 "Direct link to Implementation of")

EntityMemoryInput.outputKey

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[outputKey](/docs/api/memory/classes/BaseChatMemory#outputkey)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:25](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/chat_memory.ts#L25)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### memoryKeys[​](#memorykeys "Direct link to memoryKeys")

> **memoryKeys**(): `string`\[\]

#### Returns[​](#returns-1 "Direct link to Returns")

`string`\[\]

#### Overrides[​](#overrides-1 "Direct link to Overrides")

BaseChatMemory.memoryKeys

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/memory/entity\_memory.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/entity_memory.ts#L80)

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[memoryKeys](/docs/api/memory/classes/BaseChatMemory#memorykeys)

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/memory/entity\_memory.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/entity_memory.ts#L80)

### memoryVariables[​](#memoryvariables "Direct link to memoryVariables")

> **memoryVariables**(): `string`\[\]

#### Returns[​](#returns-2 "Direct link to Returns")

`string`\[\]

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/memory/entity\_memory.ts:85](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/entity_memory.ts#L85)

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/memory/entity\_memory.ts:85](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/entity_memory.ts#L85)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### clear()[​](#clear "Direct link to clear()")

> **clear**(): `Promise`<`void`\>

#### Returns[​](#returns-3 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[​](#overrides-3 "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[clear](/docs/api/memory/classes/BaseChatMemory#clear)

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/memory/entity\_memory.ts:156](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/entity_memory.ts#L156)

### loadMemoryVariables()[​](#loadmemoryvariables "Direct link to loadMemoryVariables()")

> **loadMemoryVariables**(`inputs`: `InputValues`): `Promise`<`MemoryVariables`\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`inputs`

`InputValues`

#### Returns[​](#returns-4 "Direct link to Returns")

`Promise`<`MemoryVariables`\>

#### Overrides[​](#overrides-4 "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[loadMemoryVariables](/docs/api/memory/classes/BaseChatMemory#loadmemoryvariables)

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/memory/entity\_memory.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/entity_memory.ts#L90)

### saveContext()[​](#savecontext "Direct link to saveContext()")

> **saveContext**(`inputs`: `InputValues`, `outputs`: `OutputValues`): `Promise`<`void`\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`inputs`

`InputValues`

`outputs`

`OutputValues`

#### Returns[​](#returns-5 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[​](#overrides-5 "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[saveContext](/docs/api/memory/classes/BaseChatMemory#savecontext)

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/memory/entity\_memory.ts:125](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/entity_memory.ts#L125)