BufferMemory
============

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseChatMemory`](/docs/api/memory/classes/BaseChatMemory).**BufferMemory**

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   [`BufferMemoryInput`](/docs/api/memory/interfaces/BufferMemoryInput)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new BufferMemory**(`fields`?: [`BufferMemoryInput`](/docs/api/memory/interfaces/BufferMemoryInput)): [`BufferMemory`](/docs/api/memory/classes/BufferMemory)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields?`

[`BufferMemoryInput`](/docs/api/memory/interfaces/BufferMemoryInput)

#### Returns[​](#returns "Direct link to Returns")

[`BufferMemory`](/docs/api/memory/classes/BufferMemory)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[constructor](/docs/api/memory/classes/BaseChatMemory#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/memory/buffer\_memory.ts:17](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/buffer_memory.ts#L17)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### aiPrefix[​](#aiprefix "Direct link to aiPrefix")

> **aiPrefix**: `string` = `"AI"`

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

[BufferMemoryInput](/docs/api/memory/interfaces/BufferMemoryInput).[aiPrefix](/docs/api/memory/interfaces/BufferMemoryInput#aiprefix)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/memory/buffer\_memory.ts:13](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/buffer_memory.ts#L13)

### chatHistory[​](#chathistory "Direct link to chatHistory")

> **chatHistory**: [`BaseChatMessageHistory`](/docs/api/schema/classes/BaseChatMessageHistory)

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

[BufferMemoryInput](/docs/api/memory/interfaces/BufferMemoryInput).[chatHistory](/docs/api/memory/interfaces/BufferMemoryInput#chathistory)

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[chatHistory](/docs/api/memory/classes/BaseChatMemory#chathistory)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:19](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/chat_memory.ts#L19)

### humanPrefix[​](#humanprefix "Direct link to humanPrefix")

> **humanPrefix**: `string` = `"Human"`

#### Implementation of[​](#implementation-of-2 "Direct link to Implementation of")

[BufferMemoryInput](/docs/api/memory/interfaces/BufferMemoryInput).[humanPrefix](/docs/api/memory/interfaces/BufferMemoryInput#humanprefix)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/memory/buffer\_memory.ts:11](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/buffer_memory.ts#L11)

### memoryKey[​](#memorykey "Direct link to memoryKey")

> **memoryKey**: `string` = `"history"`

#### Implementation of[​](#implementation-of-3 "Direct link to Implementation of")

[BufferMemoryInput](/docs/api/memory/interfaces/BufferMemoryInput).[memoryKey](/docs/api/memory/interfaces/BufferMemoryInput#memorykey)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/memory/buffer\_memory.ts:15](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/buffer_memory.ts#L15)

### returnMessages[​](#returnmessages "Direct link to returnMessages")

> **returnMessages**: `boolean` = `false`

#### Implementation of[​](#implementation-of-4 "Direct link to Implementation of")

[BufferMemoryInput](/docs/api/memory/interfaces/BufferMemoryInput).[returnMessages](/docs/api/memory/interfaces/BufferMemoryInput#returnmessages)

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[returnMessages](/docs/api/memory/classes/BaseChatMemory#returnmessages)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:21](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/chat_memory.ts#L21)

### inputKey?[​](#inputkey "Direct link to inputKey?")

> **inputKey**: `string`

#### Implementation of[​](#implementation-of-5 "Direct link to Implementation of")

[BufferMemoryInput](/docs/api/memory/interfaces/BufferMemoryInput).[inputKey](/docs/api/memory/interfaces/BufferMemoryInput#inputkey)

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[inputKey](/docs/api/memory/classes/BaseChatMemory#inputkey)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/chat_memory.ts#L23)

### outputKey?[​](#outputkey "Direct link to outputKey?")

> **outputKey**: `string`

#### Implementation of[​](#implementation-of-6 "Direct link to Implementation of")

[BufferMemoryInput](/docs/api/memory/interfaces/BufferMemoryInput).[outputKey](/docs/api/memory/interfaces/BufferMemoryInput#outputkey)

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[outputKey](/docs/api/memory/classes/BaseChatMemory#outputkey)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:25](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/chat_memory.ts#L25)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### memoryKeys[​](#memorykeys "Direct link to memoryKeys")

> **memoryKeys**(): `string`\[\]

#### Returns[​](#returns-1 "Direct link to Returns")

`string`\[\]

#### Overrides[​](#overrides-1 "Direct link to Overrides")

BaseChatMemory.memoryKeys

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/memory/buffer\_memory.ts:29](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/buffer_memory.ts#L29)

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[memoryKeys](/docs/api/memory/classes/BaseChatMemory#memorykeys)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/memory/buffer\_memory.ts:29](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/buffer_memory.ts#L29)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### clear()[​](#clear "Direct link to clear()")

> **clear**(): `Promise`<`void`\>

#### Returns[​](#returns-2 "Direct link to Returns")

`Promise`<`void`\>

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[clear](/docs/api/memory/classes/BaseChatMemory#clear)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:48](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/chat_memory.ts#L48)

### loadMemoryVariables()[​](#loadmemoryvariables "Direct link to loadMemoryVariables()")

> **loadMemoryVariables**(`_values`: `InputValues`): `Promise`<`MemoryVariables`\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`_values`

`InputValues`

#### Returns[​](#returns-3 "Direct link to Returns")

`Promise`<`MemoryVariables`\>

#### Overrides[​](#overrides-3 "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[loadMemoryVariables](/docs/api/memory/classes/BaseChatMemory#loadmemoryvariables)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/memory/buffer\_memory.ts:33](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/buffer_memory.ts#L33)

### saveContext()[​](#savecontext "Direct link to saveContext()")

> **saveContext**(`inputValues`: `InputValues`, `outputValues`: `OutputValues`): `Promise`<`void`\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`inputValues`

`InputValues`

`outputValues`

`OutputValues`

#### Returns[​](#returns-4 "Direct link to Returns")

`Promise`<`void`\>

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[saveContext](/docs/api/memory/classes/BaseChatMemory#savecontext)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:35](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/chat_memory.ts#L35)