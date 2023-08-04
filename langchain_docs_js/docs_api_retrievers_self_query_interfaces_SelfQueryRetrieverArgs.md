SelfQueryRetrieverArgs
======================

Base Index class. All indexes should extend this class.

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseRetrieverInput`](/docs/api/schema_retriever/interfaces/BaseRetrieverInput).**SelfQueryRetrieverArgs**

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### llmChain[](#llmchain "Direct link to llmChain")

> **llmChain**: [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>\>

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/retrievers/self\_query/index.ts:19](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/index.ts#L19)

### structuredQueryTranslator[](#structuredquerytranslator "Direct link to structuredQueryTranslator")

> **structuredQueryTranslator**: [`BaseTranslator`](/docs/api/retrievers_self_query/classes/BaseTranslator)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/index.ts:18](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/index.ts#L18)

### vectorStore[](#vectorstore "Direct link to vectorStore")

> **vectorStore**: [`VectorStore`](/docs/api/vectorstores_base/classes/VectorStore)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/index.ts:17](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/index.ts#L17)

### callbacks?[](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BaseRetrieverInput](/docs/api/schema_retriever/interfaces/BaseRetrieverInput).[callbacks](/docs/api/schema_retriever/interfaces/BaseRetrieverInput#callbacks)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:16](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/retriever.ts#L16)

### metadata?[](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[BaseRetrieverInput](/docs/api/schema_retriever/interfaces/BaseRetrieverInput).[metadata](/docs/api/schema_retriever/interfaces/BaseRetrieverInput#metadata)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:18](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/retriever.ts#L18)

### searchParams?[](#searchparams "Direct link to searchParams?")

> **searchParams**: `object`

#### Type declaration[](#type-declaration "Direct link to Type declaration")

Member

Type

`filter`?

`string` | `object`

`k`?

`number`

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/index.ts:21](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/index.ts#L21)

### tags?[](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[BaseRetrieverInput](/docs/api/schema_retriever/interfaces/BaseRetrieverInput).[tags](/docs/api/schema_retriever/interfaces/BaseRetrieverInput#tags)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:17](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/retriever.ts#L17)

### verbose?[](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Overrides[](#overrides "Direct link to Overrides")

[BaseRetrieverInput](/docs/api/schema_retriever/interfaces/BaseRetrieverInput).[verbose](/docs/api/schema_retriever/interfaces/BaseRetrieverInput#verbose)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/index.ts:20](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/index.ts#L20)