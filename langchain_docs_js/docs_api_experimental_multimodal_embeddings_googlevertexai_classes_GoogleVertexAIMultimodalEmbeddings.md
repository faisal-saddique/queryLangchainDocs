GoogleVertexAIMultimodalEmbeddings
==================================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`Embeddings`](/docs/api/embeddings_base/classes/Embeddings).**GoogleVertexAIMultimodalEmbeddings**

Implements[](#implements "Direct link to Implements")
------------------------------------------------------

*   [`GoogleVertexAIMultimodalEmbeddingsParams`](/docs/api/experimental_multimodal_embeddings_googlevertexai/interfaces/GoogleVertexAIMultimodalEmbeddingsParams)

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new GoogleVertexAIMultimodalEmbeddings**(`fields`?: [`GoogleVertexAIMultimodalEmbeddingsParams`](/docs/api/experimental_multimodal_embeddings_googlevertexai/interfaces/GoogleVertexAIMultimodalEmbeddingsParams)): [`GoogleVertexAIMultimodalEmbeddings`](/docs/api/experimental_multimodal_embeddings_googlevertexai/classes/GoogleVertexAIMultimodalEmbeddings)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`fields?`

[`GoogleVertexAIMultimodalEmbeddingsParams`](/docs/api/experimental_multimodal_embeddings_googlevertexai/interfaces/GoogleVertexAIMultimodalEmbeddingsParams)

#### Returns[](#returns "Direct link to Returns")

[`GoogleVertexAIMultimodalEmbeddings`](/docs/api/experimental_multimodal_embeddings_googlevertexai/classes/GoogleVertexAIMultimodalEmbeddings)

#### Overrides[](#overrides "Direct link to Overrides")

[Embeddings](/docs/api/embeddings_base/classes/Embeddings).[constructor](/docs/api/embeddings_base/classes/Embeddings#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/experimental/multimodal\_embeddings/googlevertexai.ts:60](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/multimodal_embeddings/googlevertexai.ts#L60)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### caller[](#caller "Direct link to caller")

> **caller**: `AsyncCaller`

The async caller should be used by subclasses to make any async calls, which will thus benefit from the concurrency and retry logic.

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[Embeddings](/docs/api/embeddings_base/classes/Embeddings).[caller](/docs/api/embeddings_base/classes/Embeddings#caller)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/embeddings/base.ts:10](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/embeddings/base.ts#L10)

### model[](#model "Direct link to model")

> **model**: `string` = `"multimodalembedding@001"`

Model to use

#### Implementation of[](#implementation-of "Direct link to Implementation of")

[GoogleVertexAIMultimodalEmbeddingsParams](/docs/api/experimental_multimodal_embeddings_googlevertexai/interfaces/GoogleVertexAIMultimodalEmbeddingsParams).[model](/docs/api/experimental_multimodal_embeddings_googlevertexai/interfaces/GoogleVertexAIMultimodalEmbeddingsParams#model)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/experimental/multimodal\_embeddings/googlevertexai.ts:52](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/multimodal_embeddings/googlevertexai.ts#L52)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### embedDocuments()[](#embeddocuments "Direct link to embedDocuments()")

> **embedDocuments**(`documents`: `string`\[\]): `Promise`<`number`\[\]\[\]\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`documents`

`string`\[\]

#### Returns[](#returns-1 "Direct link to Returns")

`Promise`<`number`\[\]\[\]\>

#### Overrides[](#overrides-1 "Direct link to Overrides")

[Embeddings](/docs/api/embeddings_base/classes/Embeddings).[embedDocuments](/docs/api/embeddings_base/classes/Embeddings#embeddocuments)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/experimental/multimodal\_embeddings/googlevertexai.ts:132](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/multimodal_embeddings/googlevertexai.ts#L132)

### embedImage()[](#embedimage "Direct link to embedImage()")

> **embedImage**(`images`: `Buffer`\[\]): `Promise`<`number`\[\]\[\]\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`images`

`Buffer`\[\]

#### Returns[](#returns-2 "Direct link to Returns")

`Promise`<`number`\[\]\[\]\>

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/experimental/multimodal\_embeddings/googlevertexai.ts:120](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/multimodal_embeddings/googlevertexai.ts#L120)

### embedImageQuery()[](#embedimagequery "Direct link to embedImageQuery()")

> **embedImageQuery**(`image`: `Buffer`): `Promise`<`number`\[\]\>

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

`image`

`Buffer`

#### Returns[](#returns-3 "Direct link to Returns")

`Promise`<`number`\[\]\>

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/experimental/multimodal\_embeddings/googlevertexai.ts:126](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/multimodal_embeddings/googlevertexai.ts#L126)

### embedMedia()[](#embedmedia "Direct link to embedMedia()")

> **embedMedia**(`media`: [`GoogleVertexAIMedia`](/docs/api/experimental_multimodal_embeddings_googlevertexai/types/GoogleVertexAIMedia)\[\]): `Promise`<[`MediaEmbeddings`](/docs/api/experimental_multimodal_embeddings_googlevertexai/types/MediaEmbeddings)\[\]\>

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

`media`

[`GoogleVertexAIMedia`](/docs/api/experimental_multimodal_embeddings_googlevertexai/types/GoogleVertexAIMedia)\[\]

#### Returns[](#returns-4 "Direct link to Returns")

`Promise`<[`MediaEmbeddings`](/docs/api/experimental_multimodal_embeddings_googlevertexai/types/MediaEmbeddings)\[\]\>

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/experimental/multimodal\_embeddings/googlevertexai.ts:98](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/multimodal_embeddings/googlevertexai.ts#L98)

### embedMediaQuery()[](#embedmediaquery "Direct link to embedMediaQuery()")

> **embedMediaQuery**(`media`: [`GoogleVertexAIMedia`](/docs/api/experimental_multimodal_embeddings_googlevertexai/types/GoogleVertexAIMedia)): `Promise`<[`MediaEmbeddings`](/docs/api/experimental_multimodal_embeddings_googlevertexai/types/MediaEmbeddings)\>

#### Parameters[](#parameters-5 "Direct link to Parameters")

Parameter

Type

`media`

[`GoogleVertexAIMedia`](/docs/api/experimental_multimodal_embeddings_googlevertexai/types/GoogleVertexAIMedia)

#### Returns[](#returns-5 "Direct link to Returns")

`Promise`<[`MediaEmbeddings`](/docs/api/experimental_multimodal_embeddings_googlevertexai/types/MediaEmbeddings)\>

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/experimental/multimodal\_embeddings/googlevertexai.ts:103](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/multimodal_embeddings/googlevertexai.ts#L103)

### embedQuery()[](#embedquery "Direct link to embedQuery()")

> **embedQuery**(`document`: `string`): `Promise`<`number`\[\]\>

#### Parameters[](#parameters-6 "Direct link to Parameters")

Parameter

Type

`document`

`string`

#### Returns[](#returns-6 "Direct link to Returns")

`Promise`<`number`\[\]\>

#### Overrides[](#overrides-2 "Direct link to Overrides")

[Embeddings](/docs/api/embeddings_base/classes/Embeddings).[embedQuery](/docs/api/embeddings_base/classes/Embeddings#embedquery)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/experimental/multimodal\_embeddings/googlevertexai.ts:138](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/multimodal_embeddings/googlevertexai.ts#L138)

### mediaToInstance()[](#mediatoinstance "Direct link to mediaToInstance()")

> **mediaToInstance**(`media`: [`GoogleVertexAIMedia`](/docs/api/experimental_multimodal_embeddings_googlevertexai/types/GoogleVertexAIMedia)): `GoogleVertexAIMultimodalEmbeddingsInstance`

#### Parameters[](#parameters-7 "Direct link to Parameters")

Parameter

Type

`media`

[`GoogleVertexAIMedia`](/docs/api/experimental_multimodal_embeddings_googlevertexai/types/GoogleVertexAIMedia)

#### Returns[](#returns-7 "Direct link to Returns")

`GoogleVertexAIMultimodalEmbeddingsInstance`

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/experimental/multimodal\_embeddings/googlevertexai.ts:71](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/multimodal_embeddings/googlevertexai.ts#L71)

### responseToEmbeddings()[](#responsetoembeddings "Direct link to responseToEmbeddings()")

> **responseToEmbeddings**(`response`: `GoogleVertexAILLMResponse`<`GoogleVertexAIMultimodalEmbeddingsResults`\>): [`MediaEmbeddings`](/docs/api/experimental_multimodal_embeddings_googlevertexai/types/MediaEmbeddings)\[\]

#### Parameters[](#parameters-8 "Direct link to Parameters")

Parameter

Type

`response`

`GoogleVertexAILLMResponse`<`GoogleVertexAIMultimodalEmbeddingsResults`\>

#### Returns[](#returns-8 "Direct link to Returns")

[`MediaEmbeddings`](/docs/api/experimental_multimodal_embeddings_googlevertexai/types/MediaEmbeddings)\[\]

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/experimental/multimodal\_embeddings/googlevertexai.ts:89](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/multimodal_embeddings/googlevertexai.ts#L89)