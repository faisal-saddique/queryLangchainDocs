TimeWeightedVectorStoreRetrieverFields
======================================

Base Index class. All indexes should extend this class.

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseRetrieverInput`](/docs/api/schema_retriever/interfaces/BaseRetrieverInput).**TimeWeightedVectorStoreRetrieverFields**

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### vectorStore[](#vectorstore "Direct link to vectorStore")

> **vectorStore**: [`VectorStore`](/docs/api/vectorstores_base/classes/VectorStore)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/retrievers/time\_weighted.ts:8](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/time_weighted.ts#L8)

### callbacks?[](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BaseRetrieverInput](/docs/api/schema_retriever/interfaces/BaseRetrieverInput).[callbacks](/docs/api/schema_retriever/interfaces/BaseRetrieverInput#callbacks)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:16](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/retriever.ts#L16)

### decayRate?[](#decayrate "Direct link to decayRate?")

> **decayRate**: `number`

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/retrievers/time\_weighted.ts:11](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/time_weighted.ts#L11)

### defaultSalience?[](#defaultsalience "Direct link to defaultSalience?")

> **defaultSalience**: `number`

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/retrievers/time\_weighted.ts:14](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/time_weighted.ts#L14)

### k?[](#k "Direct link to k?")

> **k**: `number`

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/retrievers/time\_weighted.ts:12](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/time_weighted.ts#L12)

### memoryStream?[](#memorystream "Direct link to memoryStream?")

> **memoryStream**: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/retrievers/time\_weighted.ts:10](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/time_weighted.ts#L10)

### metadata?[](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[BaseRetrieverInput](/docs/api/schema_retriever/interfaces/BaseRetrieverInput).[metadata](/docs/api/schema_retriever/interfaces/BaseRetrieverInput#metadata)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:18](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/retriever.ts#L18)

### otherScoreKeys?[](#otherscorekeys "Direct link to otherScoreKeys?")

> **otherScoreKeys**: `string`\[\]

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/retrievers/time\_weighted.ts:13](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/time_weighted.ts#L13)

### searchKwargs?[](#searchkwargs "Direct link to searchKwargs?")

> **searchKwargs**: `number`

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/retrievers/time\_weighted.ts:9](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/time_weighted.ts#L9)

### tags?[](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[BaseRetrieverInput](/docs/api/schema_retriever/interfaces/BaseRetrieverInput).[tags](/docs/api/schema_retriever/interfaces/BaseRetrieverInput#tags)

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:17](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/retriever.ts#L17)

### verbose?[](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[BaseRetrieverInput](/docs/api/schema_retriever/interfaces/BaseRetrieverInput).[verbose](/docs/api/schema_retriever/interfaces/BaseRetrieverInput#verbose)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:19](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/retriever.ts#L19)