CombinedMemory
==============

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseChatMemory`](/docs/api/memory/classes/BaseChatMemory).**CombinedMemory**

Implements[](#implements "Direct link to Implements")
------------------------------------------------------

*   [`CombinedMemoryInput`](/docs/api/memory/interfaces/CombinedMemoryInput)

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new CombinedMemory**(`fields`?: [`CombinedMemoryInput`](/docs/api/memory/interfaces/CombinedMemoryInput)): [`CombinedMemory`](/docs/api/memory/classes/CombinedMemory)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`fields?`

[`CombinedMemoryInput`](/docs/api/memory/interfaces/CombinedMemoryInput)

#### Returns[](#returns "Direct link to Returns")

[`CombinedMemory`](/docs/api/memory/classes/CombinedMemory)

#### Overrides[](#overrides "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[constructor](/docs/api/memory/classes/BaseChatMemory#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/memory/combined\_memory.ts:28](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/combined_memory.ts#L28)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### aiPrefix[](#aiprefix "Direct link to aiPrefix")

> **aiPrefix**: `string` = `"AI"`

#### Implementation of[](#implementation-of "Direct link to Implementation of")

[CombinedMemoryInput](/docs/api/memory/interfaces/CombinedMemoryInput).[aiPrefix](/docs/api/memory/interfaces/CombinedMemoryInput#aiprefix)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/memory/combined\_memory.ts:22](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/combined_memory.ts#L22)

### chatHistory[](#chathistory "Direct link to chatHistory")

> **chatHistory**: [`BaseChatMessageHistory`](/docs/api/schema/classes/BaseChatMessageHistory)

#### Implementation of[](#implementation-of-1 "Direct link to Implementation of")

[CombinedMemoryInput](/docs/api/memory/interfaces/CombinedMemoryInput).[chatHistory](/docs/api/memory/interfaces/CombinedMemoryInput#chathistory)

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[chatHistory](/docs/api/memory/classes/BaseChatMemory#chathistory)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:19](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L19)

### humanPrefix[](#humanprefix "Direct link to humanPrefix")

> **humanPrefix**: `string` = `"Human"`

#### Implementation of[](#implementation-of-2 "Direct link to Implementation of")

[CombinedMemoryInput](/docs/api/memory/interfaces/CombinedMemoryInput).[humanPrefix](/docs/api/memory/interfaces/CombinedMemoryInput#humanprefix)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/memory/combined\_memory.ts:20](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/combined_memory.ts#L20)

### memories[](#memories "Direct link to memories")

> **memories**: [`BaseMemory`](/docs/api/memory/classes/BaseMemory)\[\] = `[]`

#### Implementation of[](#implementation-of-3 "Direct link to Implementation of")

[CombinedMemoryInput](/docs/api/memory/interfaces/CombinedMemoryInput).[memories](/docs/api/memory/interfaces/CombinedMemoryInput#memories)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/memory/combined\_memory.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/combined_memory.ts#L26)

### memoryKey[](#memorykey "Direct link to memoryKey")

> **memoryKey**: `string` = `"history"`

#### Implementation of[](#implementation-of-4 "Direct link to Implementation of")

[CombinedMemoryInput](/docs/api/memory/interfaces/CombinedMemoryInput).[memoryKey](/docs/api/memory/interfaces/CombinedMemoryInput#memorykey)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/memory/combined\_memory.ts:24](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/combined_memory.ts#L24)

### returnMessages[](#returnmessages "Direct link to returnMessages")

> **returnMessages**: `boolean` = `false`

#### Implementation of[](#implementation-of-5 "Direct link to Implementation of")

[CombinedMemoryInput](/docs/api/memory/interfaces/CombinedMemoryInput).[returnMessages](/docs/api/memory/interfaces/CombinedMemoryInput#returnmessages)

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[returnMessages](/docs/api/memory/classes/BaseChatMemory#returnmessages)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:21](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L21)

### inputKey?[](#inputkey "Direct link to inputKey?")

> **inputKey**: `string`

#### Implementation of[](#implementation-of-6 "Direct link to Implementation of")

[CombinedMemoryInput](/docs/api/memory/interfaces/CombinedMemoryInput).[inputKey](/docs/api/memory/interfaces/CombinedMemoryInput#inputkey)

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[inputKey](/docs/api/memory/classes/BaseChatMemory#inputkey)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:23](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L23)

### outputKey?[](#outputkey "Direct link to outputKey?")

> **outputKey**: `string`

#### Implementation of[](#implementation-of-7 "Direct link to Implementation of")

[CombinedMemoryInput](/docs/api/memory/interfaces/CombinedMemoryInput).[outputKey](/docs/api/memory/interfaces/CombinedMemoryInput#outputkey)

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[outputKey](/docs/api/memory/classes/BaseChatMemory#outputkey)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:25](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L25)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### memoryKeys[](#memorykeys "Direct link to memoryKeys")

> **memoryKeys**(): `string`\[\]

#### Returns[](#returns-1 "Direct link to Returns")

`string`\[\]

#### Overrides[](#overrides-1 "Direct link to Overrides")

BaseChatMemory.memoryKeys

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/memory/combined\_memory.ts:101](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/combined_memory.ts#L101)

#### Overrides[](#overrides-2 "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[memoryKeys](/docs/api/memory/classes/BaseChatMemory#memorykeys)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/memory/combined\_memory.ts:101](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/combined_memory.ts#L101)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### checkInputKey()[](#checkinputkey "Direct link to checkInputKey()")

> **checkInputKey**(): `void`

#### Returns[](#returns-2 "Direct link to Returns")

`void`

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/memory/combined\_memory.ts:59](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/combined_memory.ts#L59)

### checkRepeatedMemoryVariable()[](#checkrepeatedmemoryvariable "Direct link to checkRepeatedMemoryVariable()")

> **checkRepeatedMemoryVariable**(): `void`

#### Returns[](#returns-3 "Direct link to Returns")

`void`

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/memory/combined\_memory.ts:44](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/combined_memory.ts#L44)

### clear()[](#clear "Direct link to clear()")

> **clear**(): `Promise`<`void`\>

#### Returns[](#returns-4 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[](#overrides-3 "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[clear](/docs/api/memory/classes/BaseChatMemory#clear)

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/memory/combined\_memory.ts:93](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/combined_memory.ts#L93)

### loadMemoryVariables()[](#loadmemoryvariables "Direct link to loadMemoryVariables()")

> **loadMemoryVariables**(`inputValues`: `InputValues`): `Promise`<`MemoryVariables`\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`inputValues`

`InputValues`

#### Returns[](#returns-5 "Direct link to Returns")

`Promise`<`MemoryVariables`\>

#### Overrides[](#overrides-4 "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[loadMemoryVariables](/docs/api/memory/classes/BaseChatMemory#loadmemoryvariables)

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/memory/combined\_memory.ts:72](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/combined_memory.ts#L72)

### saveContext()[](#savecontext "Direct link to saveContext()")

> **saveContext**(`inputValues`: `InputValues`, `outputValues`: `OutputValues`): `Promise`<`void`\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`inputValues`

`InputValues`

`outputValues`

`OutputValues`

#### Returns[](#returns-6 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[](#overrides-5 "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[saveContext](/docs/api/memory/classes/BaseChatMemory#savecontext)

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/memory/combined\_memory.ts:87](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/combined_memory.ts#L87)