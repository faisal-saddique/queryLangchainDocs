VectorStoreRetrieverInput<V\>
=============================

Base Index class. All indexes should extend this class.

Type parameters[​](#type-parameters "Direct link to Type parameters")
---------------------------------------------------------------------

*   `V` _extends_ [`VectorStore`](/docs/api/vectorstores_base/classes/VectorStore)

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseRetrieverInput`](/docs/api/schema_retriever/interfaces/BaseRetrieverInput).**VectorStoreRetrieverInput**

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### vectorStore[​](#vectorstore "Direct link to vectorStore")

> **vectorStore**: `V`

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:15](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/base.ts#L15)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BaseRetrieverInput](/docs/api/schema_retriever/interfaces/BaseRetrieverInput).[callbacks](/docs/api/schema_retriever/interfaces/BaseRetrieverInput#callbacks)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:16](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L16)

### filter?[​](#filter "Direct link to filter?")

> **filter**: `V`\["FilterType"\]

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:17](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/base.ts#L17)

### k?[​](#k "Direct link to k?")

> **k**: `number`

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:16](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/base.ts#L16)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[BaseRetrieverInput](/docs/api/schema_retriever/interfaces/BaseRetrieverInput).[metadata](/docs/api/schema_retriever/interfaces/BaseRetrieverInput#metadata)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:18](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L18)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[BaseRetrieverInput](/docs/api/schema_retriever/interfaces/BaseRetrieverInput).[tags](/docs/api/schema_retriever/interfaces/BaseRetrieverInput#tags)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:17](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L17)

### verbose?[​](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[BaseRetrieverInput](/docs/api/schema_retriever/interfaces/BaseRetrieverInput).[verbose](/docs/api/schema_retriever/interfaces/BaseRetrieverInput#verbose)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:19](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L19)