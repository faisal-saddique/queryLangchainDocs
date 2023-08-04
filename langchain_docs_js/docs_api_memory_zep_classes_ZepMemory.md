ZepMemory
=========

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseChatMemory`](/docs/api/memory/classes/BaseChatMemory).**ZepMemory**

Implements[](#implements "Direct link to Implements")
------------------------------------------------------

*   [`ZepMemoryInput`](/docs/api/memory_zep/interfaces/ZepMemoryInput)

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new ZepMemory**(`fields`: [`ZepMemoryInput`](/docs/api/memory_zep/interfaces/ZepMemoryInput)): [`ZepMemory`](/docs/api/memory_zep/classes/ZepMemory)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`fields`

[`ZepMemoryInput`](/docs/api/memory_zep/interfaces/ZepMemoryInput)

#### Returns[](#returns "Direct link to Returns")

[`ZepMemory`](/docs/api/memory_zep/classes/ZepMemory)

#### Overrides[](#overrides "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[constructor](/docs/api/memory/classes/BaseChatMemory#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/memory/zep.ts:47](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/zep.ts#L47)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### aiPrefix[](#aiprefix "Direct link to aiPrefix")

> **aiPrefix**: `string` = `"AI"`

#### Implementation of[](#implementation-of "Direct link to Implementation of")

[ZepMemoryInput](/docs/api/memory_zep/interfaces/ZepMemoryInput).[aiPrefix](/docs/api/memory_zep/interfaces/ZepMemoryInput#aiprefix)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/memory/zep.ts:37](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/zep.ts#L37)

### baseURL[](#baseurl "Direct link to baseURL")

> **baseURL**: `string`

#### Implementation of[](#implementation-of-1 "Direct link to Implementation of")

[ZepMemoryInput](/docs/api/memory_zep/interfaces/ZepMemoryInput).[baseURL](/docs/api/memory_zep/interfaces/ZepMemoryInput#baseurl)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/memory/zep.ts:41](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/zep.ts#L41)

### chatHistory[](#chathistory "Direct link to chatHistory")

> **chatHistory**: [`BaseChatMessageHistory`](/docs/api/schema/classes/BaseChatMessageHistory)

#### Implementation of[](#implementation-of-2 "Direct link to Implementation of")

[ZepMemoryInput](/docs/api/memory_zep/interfaces/ZepMemoryInput).[chatHistory](/docs/api/memory_zep/interfaces/ZepMemoryInput#chathistory)

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[chatHistory](/docs/api/memory/classes/BaseChatMemory#chathistory)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:19](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L19)

### humanPrefix[](#humanprefix "Direct link to humanPrefix")

> **humanPrefix**: `string` = `"Human"`

#### Implementation of[](#implementation-of-3 "Direct link to Implementation of")

[ZepMemoryInput](/docs/api/memory_zep/interfaces/ZepMemoryInput).[humanPrefix](/docs/api/memory_zep/interfaces/ZepMemoryInput#humanprefix)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/memory/zep.ts:35](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/zep.ts#L35)

### memoryKey[](#memorykey "Direct link to memoryKey")

> **memoryKey**: `string` = `"history"`

#### Implementation of[](#implementation-of-4 "Direct link to Implementation of")

[ZepMemoryInput](/docs/api/memory_zep/interfaces/ZepMemoryInput).[memoryKey](/docs/api/memory_zep/interfaces/ZepMemoryInput#memorykey)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/memory/zep.ts:39](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/zep.ts#L39)

### returnMessages[](#returnmessages "Direct link to returnMessages")

> **returnMessages**: `boolean` = `false`

#### Implementation of[](#implementation-of-5 "Direct link to Implementation of")

[ZepMemoryInput](/docs/api/memory_zep/interfaces/ZepMemoryInput).[returnMessages](/docs/api/memory_zep/interfaces/ZepMemoryInput#returnmessages)

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[returnMessages](/docs/api/memory/classes/BaseChatMemory#returnmessages)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:21](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L21)

### sessionId[](#sessionid "Direct link to sessionId")

> **sessionId**: `string`

#### Implementation of[](#implementation-of-6 "Direct link to Implementation of")

[ZepMemoryInput](/docs/api/memory_zep/interfaces/ZepMemoryInput).[sessionId](/docs/api/memory_zep/interfaces/ZepMemoryInput#sessionid)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/memory/zep.ts:43](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/zep.ts#L43)

### zepClient[](#zepclient "Direct link to zepClient")

> **zepClient**: `ZepClient`

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/memory/zep.ts:45](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/zep.ts#L45)

### inputKey?[](#inputkey "Direct link to inputKey?")

> **inputKey**: `string`

#### Implementation of[](#implementation-of-7 "Direct link to Implementation of")

[ZepMemoryInput](/docs/api/memory_zep/interfaces/ZepMemoryInput).[inputKey](/docs/api/memory_zep/interfaces/ZepMemoryInput#inputkey)

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[inputKey](/docs/api/memory/classes/BaseChatMemory#inputkey)

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:23](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L23)

### outputKey?[](#outputkey "Direct link to outputKey?")

> **outputKey**: `string`

#### Implementation of[](#implementation-of-8 "Direct link to Implementation of")

[ZepMemoryInput](/docs/api/memory_zep/interfaces/ZepMemoryInput).[outputKey](/docs/api/memory_zep/interfaces/ZepMemoryInput#outputkey)

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[outputKey](/docs/api/memory/classes/BaseChatMemory#outputkey)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:25](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L25)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### memoryKeys[](#memorykeys "Direct link to memoryKeys")

> **memoryKeys**(): `string`\[\]

#### Returns[](#returns-1 "Direct link to Returns")

`string`\[\]

#### Overrides[](#overrides-1 "Direct link to Overrides")

BaseChatMemory.memoryKeys

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/memory/zep.ts:62](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/zep.ts#L62)

#### Overrides[](#overrides-2 "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[memoryKeys](/docs/api/memory/classes/BaseChatMemory#memorykeys)

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/memory/zep.ts:62](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/zep.ts#L62)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### clear()[](#clear "Direct link to clear()")

> **clear**(): `Promise`<`void`\>

#### Returns[](#returns-2 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[](#overrides-3 "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[clear](/docs/api/memory/classes/BaseChatMemory#clear)

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/memory/zep.ts:155](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/zep.ts#L155)

### loadMemoryVariables()[](#loadmemoryvariables "Direct link to loadMemoryVariables()")

> **loadMemoryVariables**(`values`: `InputValues`): `Promise`<`MemoryVariables`\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`values`

`InputValues`

#### Returns[](#returns-3 "Direct link to Returns")

`Promise`<`MemoryVariables`\>

#### Overrides[](#overrides-4 "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[loadMemoryVariables](/docs/api/memory/classes/BaseChatMemory#loadmemoryvariables)

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/memory/zep.ts:66](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/zep.ts#L66)

### saveContext()[](#savecontext "Direct link to saveContext()")

> **saveContext**(`inputValues`: `InputValues`, `outputValues`: `OutputValues`): `Promise`<`void`\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`inputValues`

`InputValues`

`outputValues`

`OutputValues`

#### Returns[](#returns-4 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[](#overrides-5 "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[saveContext](/docs/api/memory/classes/BaseChatMemory#savecontext)

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/memory/zep.ts:121](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/zep.ts#L121)