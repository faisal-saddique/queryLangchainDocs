Embeddings
==========

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`FakeEmbeddings`](/docs/api/embeddings_fake/classes/FakeEmbeddings)
*   [`SyntheticEmbeddings`](/docs/api/embeddings_fake/classes/SyntheticEmbeddings)
*   [`OpenAIEmbeddings`](/docs/api/embeddings_openai/classes/OpenAIEmbeddings)
*   [`CohereEmbeddings`](/docs/api/embeddings_cohere/classes/CohereEmbeddings)
*   [`TensorFlowEmbeddings`](/docs/api/embeddings_tensorflow/classes/TensorFlowEmbeddings)
*   [`HuggingFaceInferenceEmbeddings`](/docs/api/embeddings_hf/classes/HuggingFaceInferenceEmbeddings)
*   [`GoogleVertexAIEmbeddings`](/docs/api/embeddings_googlevertexai/classes/GoogleVertexAIEmbeddings)
*   [`GooglePaLMEmbeddings`](/docs/api/embeddings_googlepalm/classes/GooglePaLMEmbeddings)
*   [`GoogleVertexAIMultimodalEmbeddings`](/docs/api/experimental_multimodal_embeddings_googlevertexai/classes/GoogleVertexAIMultimodalEmbeddings)

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new Embeddings**(`params`: `AsyncCallerParams`): [`Embeddings`](/docs/api/embeddings_base/classes/Embeddings)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`params`

`AsyncCallerParams`

#### Returns[](#returns "Direct link to Returns")

[`Embeddings`](/docs/api/embeddings_base/classes/Embeddings)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/embeddings/base.ts:12](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/embeddings/base.ts#L12)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### caller[](#caller "Direct link to caller")

> **caller**: `AsyncCaller`

The async caller should be used by subclasses to make any async calls, which will thus benefit from the concurrency and retry logic.

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/embeddings/base.ts:10](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/embeddings/base.ts#L10)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### embedDocuments()[](#embeddocuments "Direct link to embedDocuments()")

> `Abstract` **embedDocuments**(`documents`: `string`\[\]): `Promise`<`number`\[\]\[\]\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`documents`

`string`\[\]

#### Returns[](#returns-1 "Direct link to Returns")

`Promise`<`number`\[\]\[\]\>

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/embeddings/base.ts:16](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/embeddings/base.ts#L16)

### embedQuery()[](#embedquery "Direct link to embedQuery()")

> `Abstract` **embedQuery**(`document`: `string`): `Promise`<`number`\[\]\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`document`

`string`

#### Returns[](#returns-2 "Direct link to Returns")

`Promise`<`number`\[\]\>

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/embeddings/base.ts:18](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/embeddings/base.ts#L18)