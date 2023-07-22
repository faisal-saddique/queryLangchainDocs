VectorStoreRetrieverMemory
==========================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseMemory`](/docs/api/memory/classes/BaseMemory).**VectorStoreRetrieverMemory**

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   [`VectorStoreRetrieverMemoryParams`](/docs/api/memory/interfaces/VectorStoreRetrieverMemoryParams)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new VectorStoreRetrieverMemory**(`fields`: [`VectorStoreRetrieverMemoryParams`](/docs/api/memory/interfaces/VectorStoreRetrieverMemoryParams)): [`VectorStoreRetrieverMemory`](/docs/api/memory/classes/VectorStoreRetrieverMemory)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields`

[`VectorStoreRetrieverMemoryParams`](/docs/api/memory/interfaces/VectorStoreRetrieverMemoryParams)

#### Returns[​](#returns "Direct link to Returns")

[`VectorStoreRetrieverMemory`](/docs/api/memory/classes/VectorStoreRetrieverMemory)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseMemory](/docs/api/memory/classes/BaseMemory).[constructor](/docs/api/memory/classes/BaseMemory#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/memory/vector\_store.ts:31](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/vector_store.ts#L31)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### memoryKey[​](#memorykey "Direct link to memoryKey")

> **memoryKey**: `string`

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

[VectorStoreRetrieverMemoryParams](/docs/api/memory/interfaces/VectorStoreRetrieverMemoryParams).[memoryKey](/docs/api/memory/interfaces/VectorStoreRetrieverMemoryParams#memorykey)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/memory/vector\_store.ts:27](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/vector_store.ts#L27)

### returnDocs[​](#returndocs "Direct link to returnDocs")

> **returnDocs**: `boolean`

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

[VectorStoreRetrieverMemoryParams](/docs/api/memory/interfaces/VectorStoreRetrieverMemoryParams).[returnDocs](/docs/api/memory/interfaces/VectorStoreRetrieverMemoryParams#returndocs)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/memory/vector\_store.ts:29](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/vector_store.ts#L29)

### vectorStoreRetriever[​](#vectorstoreretriever "Direct link to vectorStoreRetriever")

> **vectorStoreRetriever**: [`VectorStoreRetriever`](/docs/api/vectorstores_base/classes/VectorStoreRetriever)<[`VectorStore`](/docs/api/vectorstores_base/classes/VectorStore)\>

#### Implementation of[​](#implementation-of-2 "Direct link to Implementation of")

[VectorStoreRetrieverMemoryParams](/docs/api/memory/interfaces/VectorStoreRetrieverMemoryParams).[vectorStoreRetriever](/docs/api/memory/interfaces/VectorStoreRetrieverMemoryParams#vectorstoreretriever)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/memory/vector\_store.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/vector_store.ts#L23)

### inputKey?[​](#inputkey "Direct link to inputKey?")

> **inputKey**: `string`

#### Implementation of[​](#implementation-of-3 "Direct link to Implementation of")

[VectorStoreRetrieverMemoryParams](/docs/api/memory/interfaces/VectorStoreRetrieverMemoryParams).[inputKey](/docs/api/memory/interfaces/VectorStoreRetrieverMemoryParams#inputkey)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/memory/vector\_store.ts:25](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/vector_store.ts#L25)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### memoryKeys[​](#memorykeys "Direct link to memoryKeys")

> **memoryKeys**(): `string`\[\]

#### Returns[​](#returns-1 "Direct link to Returns")

`string`\[\]

#### Overrides[​](#overrides-1 "Direct link to Overrides")

BaseMemory.memoryKeys

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/memory/vector\_store.ts:39](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/vector_store.ts#L39)

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[BaseMemory](/docs/api/memory/classes/BaseMemory).[memoryKeys](/docs/api/memory/classes/BaseMemory#memorykeys)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/memory/vector\_store.ts:39](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/vector_store.ts#L39)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### loadMemoryVariables()[​](#loadmemoryvariables "Direct link to loadMemoryVariables()")

> **loadMemoryVariables**(`values`: `InputValues`): `Promise`<`MemoryVariables`\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`values`

`InputValues`

#### Returns[​](#returns-2 "Direct link to Returns")

`Promise`<`MemoryVariables`\>

#### Overrides[​](#overrides-3 "Direct link to Overrides")

[BaseMemory](/docs/api/memory/classes/BaseMemory).[loadMemoryVariables](/docs/api/memory/classes/BaseMemory#loadmemoryvariables)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/memory/vector\_store.ts:43](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/vector_store.ts#L43)

### saveContext()[​](#savecontext "Direct link to saveContext()")

> **saveContext**(`inputValues`: `InputValues`, `outputValues`: `OutputValues`): `Promise`<`void`\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`inputValues`

`InputValues`

`outputValues`

`OutputValues`

#### Returns[​](#returns-3 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[​](#overrides-4 "Direct link to Overrides")

[BaseMemory](/docs/api/memory/classes/BaseMemory).[saveContext](/docs/api/memory/classes/BaseMemory#savecontext)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/memory/vector\_store.ts:53](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/vector_store.ts#L53)