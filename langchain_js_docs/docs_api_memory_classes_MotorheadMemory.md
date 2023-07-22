MotorheadMemory
===============

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseChatMemory`](/docs/api/memory/classes/BaseChatMemory).**MotorheadMemory**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new MotorheadMemory**(`fields`: [`MotorheadMemoryInput`](/docs/api/memory/interfaces/MotorheadMemoryInput)): [`MotorheadMemory`](/docs/api/memory/classes/MotorheadMemory)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields`

[`MotorheadMemoryInput`](/docs/api/memory/interfaces/MotorheadMemoryInput)

#### Returns[​](#returns "Direct link to Returns")

[`MotorheadMemory`](/docs/api/memory/classes/MotorheadMemory)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[constructor](/docs/api/memory/classes/BaseChatMemory#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/memory/motorhead\_memory.ts:50](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/motorhead_memory.ts#L50)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### caller[​](#caller "Direct link to caller")

> **caller**: `AsyncCaller`

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/memory/motorhead\_memory.ts:43](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/motorhead_memory.ts#L43)

### chatHistory[​](#chathistory "Direct link to chatHistory")

> **chatHistory**: [`BaseChatMessageHistory`](/docs/api/schema/classes/BaseChatMessageHistory)

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[chatHistory](/docs/api/memory/classes/BaseChatMemory#chathistory)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:19](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/chat_memory.ts#L19)

### memoryKey[​](#memorykey "Direct link to memoryKey")

> **memoryKey**: `string` = `"history"`

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/memory/motorhead\_memory.ts:37](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/motorhead_memory.ts#L37)

### returnMessages[​](#returnmessages "Direct link to returnMessages")

> **returnMessages**: `boolean` = `false`

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[returnMessages](/docs/api/memory/classes/BaseChatMemory#returnmessages)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:21](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/chat_memory.ts#L21)

### sessionId[​](#sessionid "Direct link to sessionId")

> **sessionId**: `string`

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/memory/motorhead\_memory.ts:39](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/motorhead_memory.ts#L39)

### timeout[​](#timeout "Direct link to timeout")

> **timeout**: `number` = `3000`

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/memory/motorhead\_memory.ts:35](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/motorhead_memory.ts#L35)

### url[​](#url "Direct link to url")

> **url**: `string` = `MANAGED_URL`

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/memory/motorhead\_memory.ts:33](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/motorhead_memory.ts#L33)

### apiKey?[​](#apikey "Direct link to apiKey?")

> **apiKey**: `string`

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/memory/motorhead\_memory.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/motorhead_memory.ts#L46)

### clientId?[​](#clientid "Direct link to clientId?")

> **clientId**: `string`

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/memory/motorhead\_memory.ts:48](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/motorhead_memory.ts#L48)

### context?[​](#context "Direct link to context?")

> **context**: `string`

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/memory/motorhead\_memory.ts:41](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/motorhead_memory.ts#L41)

### inputKey?[​](#inputkey "Direct link to inputKey?")

> **inputKey**: `string`

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[inputKey](/docs/api/memory/classes/BaseChatMemory#inputkey)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/chat_memory.ts#L23)

### outputKey?[​](#outputkey "Direct link to outputKey?")

> **outputKey**: `string`

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

[langchain/src/memory/motorhead\_memory.ts:75](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/motorhead_memory.ts#L75)

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[memoryKeys](/docs/api/memory/classes/BaseChatMemory#memorykeys)

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/memory/motorhead\_memory.ts:75](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/motorhead_memory.ts#L75)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### \_getHeaders()[​](#_getheaders "Direct link to _getheaders")

> **\_getHeaders**(): `HeadersInit`

#### Returns[​](#returns-2 "Direct link to Returns")

`HeadersInit`

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/memory/motorhead\_memory.ts:79](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/motorhead_memory.ts#L79)

### clear()[​](#clear "Direct link to clear()")

> **clear**(): `Promise`<`void`\>

#### Returns[​](#returns-3 "Direct link to Returns")

`Promise`<`void`\>

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[clear](/docs/api/memory/classes/BaseChatMemory#clear)

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:48](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/chat_memory.ts#L48)

### init()[​](#init "Direct link to init()")

> **init**(): `Promise`<`void`\>

#### Returns[​](#returns-4 "Direct link to Returns")

`Promise`<`void`\>

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/memory/motorhead\_memory.ts:99](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/motorhead_memory.ts#L99)

### loadMemoryVariables()[​](#loadmemoryvariables "Direct link to loadMemoryVariables()")

> **loadMemoryVariables**(`_values`: `InputValues`): `Promise`<`MemoryVariables`\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`_values`

`InputValues`

#### Returns[​](#returns-5 "Direct link to Returns")

`Promise`<`MemoryVariables`\>

#### Overrides[​](#overrides-3 "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[loadMemoryVariables](/docs/api/memory/classes/BaseChatMemory#loadmemoryvariables)

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/memory/motorhead\_memory.ts:128](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/motorhead_memory.ts#L128)

### saveContext()[​](#savecontext "Direct link to saveContext()")

> **saveContext**(`inputValues`: `InputValues`, `outputValues`: `OutputValues`): `Promise`<`void`\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`inputValues`

`InputValues`

`outputValues`

`OutputValues`

#### Returns[​](#returns-6 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[​](#overrides-4 "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[saveContext](/docs/api/memory/classes/BaseChatMemory#savecontext)

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/memory/motorhead\_memory.ts:142](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/motorhead_memory.ts#L142)