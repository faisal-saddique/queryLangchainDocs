BaseMemory
==========

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseChatMemory`](/docs/api/memory/classes/BaseChatMemory)
*   [`VectorStoreRetrieverMemory`](/docs/api/memory/classes/VectorStoreRetrieverMemory)
*   [`GenerativeAgentMemory`](/docs/api/experimental_generative_agents/classes/GenerativeAgentMemory)

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new BaseMemory**(): [`BaseMemory`](/docs/api/memory/classes/BaseMemory)

#### Returns[](#returns "Direct link to Returns")

[`BaseMemory`](/docs/api/memory/classes/BaseMemory)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### memoryKeys[](#memorykeys "Direct link to memoryKeys")

> `Abstract` **memoryKeys**(): `string`\[\]

#### Returns[](#returns-1 "Direct link to Returns")

`string`\[\]

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/memory/base.ts:10](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/base.ts#L10)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/memory/base.ts:10](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/base.ts#L10)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### loadMemoryVariables()[](#loadmemoryvariables "Direct link to loadMemoryVariables()")

> `Abstract` **loadMemoryVariables**(`values`: `InputValues`): `Promise`<`MemoryVariables`\>

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`values`

`InputValues`

#### Returns[](#returns-2 "Direct link to Returns")

`Promise`<`MemoryVariables`\>

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/memory/base.ts:12](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/base.ts#L12)

### saveContext()[](#savecontext "Direct link to saveContext()")

> `Abstract` **saveContext**(`inputValues`: `InputValues`, `outputValues`: `OutputValues`): `Promise`<`void`\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`inputValues`

`InputValues`

`outputValues`

`OutputValues`

#### Returns[](#returns-3 "Direct link to Returns")

`Promise`<`void`\>

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/memory/base.ts:14](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/base.ts#L14)