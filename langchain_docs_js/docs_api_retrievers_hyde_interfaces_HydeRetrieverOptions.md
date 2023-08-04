HydeRetrieverOptions<V\>
========================

Base Index class. All indexes should extend this class.

Type parameters[](#type-parameters "Direct link to Type parameters")
---------------------------------------------------------------------

*   `V` _extends_ [`VectorStore`](/docs/api/vectorstores_base/classes/VectorStore)

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`VectorStoreRetrieverInput`](/docs/api/vectorstores_base/interfaces/VectorStoreRetrieverInput)<`V`\>.**HydeRetrieverOptions**

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### llm[](#llm "Direct link to llm")

> **llm**: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/retrievers/hyde.ts:25](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/hyde.ts#L25)

### vectorStore[](#vectorstore "Direct link to vectorStore")

> **vectorStore**: `V`

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[VectorStoreRetrieverInput](/docs/api/vectorstores_base/interfaces/VectorStoreRetrieverInput).[vectorStore](/docs/api/vectorstores_base/interfaces/VectorStoreRetrieverInput#vectorstore)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:15](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/base.ts#L15)

### callbacks?[](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[VectorStoreRetrieverInput](/docs/api/vectorstores_base/interfaces/VectorStoreRetrieverInput).[callbacks](/docs/api/vectorstores_base/interfaces/VectorStoreRetrieverInput#callbacks)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:16](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/retriever.ts#L16)

### filter?[](#filter "Direct link to filter?")

> **filter**: `V`\["FilterType"\]

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[VectorStoreRetrieverInput](/docs/api/vectorstores_base/interfaces/VectorStoreRetrieverInput).[filter](/docs/api/vectorstores_base/interfaces/VectorStoreRetrieverInput#filter)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:17](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/base.ts#L17)

### k?[](#k "Direct link to k?")

> **k**: `number`

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[VectorStoreRetrieverInput](/docs/api/vectorstores_base/interfaces/VectorStoreRetrieverInput).[k](/docs/api/vectorstores_base/interfaces/VectorStoreRetrieverInput#k)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:16](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/base.ts#L16)

### metadata?[](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[VectorStoreRetrieverInput](/docs/api/vectorstores_base/interfaces/VectorStoreRetrieverInput).[metadata](/docs/api/vectorstores_base/interfaces/VectorStoreRetrieverInput#metadata)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:18](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/retriever.ts#L18)

### promptTemplate?[](#prompttemplate "Direct link to promptTemplate?")

> **promptTemplate**: [`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)<[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\> | [`PromptKey`](/docs/api/retrievers_hyde/types/PromptKey)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/retrievers/hyde.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/hyde.ts#L26)

### tags?[](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[VectorStoreRetrieverInput](/docs/api/vectorstores_base/interfaces/VectorStoreRetrieverInput).[tags](/docs/api/vectorstores_base/interfaces/VectorStoreRetrieverInput#tags)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:17](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/retriever.ts#L17)

### verbose?[](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[VectorStoreRetrieverInput](/docs/api/vectorstores_base/interfaces/VectorStoreRetrieverInput).[verbose](/docs/api/vectorstores_base/interfaces/VectorStoreRetrieverInput#verbose)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:19](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/retriever.ts#L19)