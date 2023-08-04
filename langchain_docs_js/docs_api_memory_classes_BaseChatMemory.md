BaseChatMemory
==============

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseMemory`](/docs/api/memory/classes/BaseMemory).**BaseChatMemory**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new BaseChatMemory**(`fields`?: [`BaseChatMemoryInput`](/docs/api/memory/interfaces/BaseChatMemoryInput)): [`BaseChatMemory`](/docs/api/memory/classes/BaseChatMemory)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`fields?`

[`BaseChatMemoryInput`](/docs/api/memory/interfaces/BaseChatMemoryInput)

#### Returns[](#returns "Direct link to Returns")

[`BaseChatMemory`](/docs/api/memory/classes/BaseChatMemory)

#### Overrides[](#overrides "Direct link to Overrides")

[BaseMemory](/docs/api/memory/classes/BaseMemory).[constructor](/docs/api/memory/classes/BaseMemory#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:27](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L27)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### chatHistory[](#chathistory "Direct link to chatHistory")

> **chatHistory**: [`BaseChatMessageHistory`](/docs/api/schema/classes/BaseChatMessageHistory)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:19](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L19)

### returnMessages[](#returnmessages "Direct link to returnMessages")

> **returnMessages**: `boolean` = `false`

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:21](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L21)

### inputKey?[](#inputkey "Direct link to inputKey?")

> **inputKey**: `string`

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:23](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L23)

### outputKey?[](#outputkey "Direct link to outputKey?")

> **outputKey**: `string`

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:25](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L25)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### memoryKeys[](#memorykeys "Direct link to memoryKeys")

> `Abstract` **memoryKeys**(): `string`\[\]

#### Returns[](#returns-1 "Direct link to Returns")

`string`\[\]

#### Inherited from[](#inherited-from "Direct link to Inherited from")

BaseMemory.memoryKeys

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/memory/base.ts:10](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/base.ts#L10)

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[BaseMemory](/docs/api/memory/classes/BaseMemory).[memoryKeys](/docs/api/memory/classes/BaseMemory#memorykeys)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/memory/base.ts:10](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/base.ts#L10)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### clear()[](#clear "Direct link to clear()")

> **clear**(): `Promise`<`void`\>

#### Returns[](#returns-2 "Direct link to Returns")

`Promise`<`void`\>

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L48)

### loadMemoryVariables()[](#loadmemoryvariables "Direct link to loadMemoryVariables()")

> `Abstract` **loadMemoryVariables**(`values`: `InputValues`): `Promise`<`MemoryVariables`\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`values`

`InputValues`

#### Returns[](#returns-3 "Direct link to Returns")

`Promise`<`MemoryVariables`\>

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[BaseMemory](/docs/api/memory/classes/BaseMemory).[loadMemoryVariables](/docs/api/memory/classes/BaseMemory#loadmemoryvariables)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/memory/base.ts:12](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/base.ts#L12)

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

#### Overrides[](#overrides-1 "Direct link to Overrides")

[BaseMemory](/docs/api/memory/classes/BaseMemory).[saveContext](/docs/api/memory/classes/BaseMemory#savecontext)

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:35](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L35)