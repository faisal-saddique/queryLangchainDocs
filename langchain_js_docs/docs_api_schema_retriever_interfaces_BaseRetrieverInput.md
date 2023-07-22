BaseRetrieverInput
==================

Base Index class. All indexes should extend this class.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`VectorStoreRetrieverInput`](/docs/api/vectorstores_base/interfaces/VectorStoreRetrieverInput)
*   [`SupabaseLibArgs`](/docs/api/retrievers_supabase/interfaces/SupabaseLibArgs)
*   [`ZepRetrieverConfig`](/docs/api/retrievers_zep/interfaces/ZepRetrieverConfig)
*   [`MetalRetrieverFields`](/docs/api/retrievers_metal/interfaces/MetalRetrieverFields)
*   [`DataberryRetrieverArgs`](/docs/api/retrievers_databerry/interfaces/DataberryRetrieverArgs)
*   [`ContextualCompressionRetrieverArgs`](/docs/api/retrievers_contextual_compression/interfaces/ContextualCompressionRetrieverArgs)
*   [`TimeWeightedVectorStoreRetrieverFields`](/docs/api/retrievers_time_weighted/interfaces/TimeWeightedVectorStoreRetrieverFields)
*   [`SelfQueryRetrieverArgs`](/docs/api/retrievers_self_query/interfaces/SelfQueryRetrieverArgs)
*   [`RemoteRetrieverParams`](/docs/api/retrievers_remote/interfaces/RemoteRetrieverParams)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/schema/retriever.ts:16](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L16)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:18](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L18)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:17](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L17)

### verbose?[​](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:19](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L19)