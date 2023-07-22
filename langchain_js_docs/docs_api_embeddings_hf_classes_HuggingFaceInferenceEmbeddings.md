HuggingFaceInferenceEmbeddings
==============================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`Embeddings`](/docs/api/embeddings_base/classes/Embeddings).**HuggingFaceInferenceEmbeddings**

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   [`HuggingFaceInferenceEmbeddingsParams`](/docs/api/embeddings_hf/interfaces/HuggingFaceInferenceEmbeddingsParams)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new HuggingFaceInferenceEmbeddings**(`fields`?: [`HuggingFaceInferenceEmbeddingsParams`](/docs/api/embeddings_hf/interfaces/HuggingFaceInferenceEmbeddingsParams)): [`HuggingFaceInferenceEmbeddings`](/docs/api/embeddings_hf/classes/HuggingFaceInferenceEmbeddings)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields?`

[`HuggingFaceInferenceEmbeddingsParams`](/docs/api/embeddings_hf/interfaces/HuggingFaceInferenceEmbeddingsParams)

#### Returns[​](#returns "Direct link to Returns")

[`HuggingFaceInferenceEmbeddings`](/docs/api/embeddings_hf/classes/HuggingFaceInferenceEmbeddings)

#### Overrides[​](#overrides "Direct link to Overrides")

[Embeddings](/docs/api/embeddings_base/classes/Embeddings).[constructor](/docs/api/embeddings_base/classes/Embeddings#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/embeddings/hf.ts:20](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/hf.ts#L20)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### caller[​](#caller "Direct link to caller")

> **caller**: `AsyncCaller`

The async caller should be used by subclasses to make any async calls, which will thus benefit from the concurrency and retry logic.

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[Embeddings](/docs/api/embeddings_base/classes/Embeddings).[caller](/docs/api/embeddings_base/classes/Embeddings#caller)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/embeddings/base.ts:10](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/base.ts#L10)

### client[​](#client "Direct link to client")

> **client**: `HfInference`

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/embeddings/hf.ts:18](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/hf.ts#L18)

### model[​](#model "Direct link to model")

> **model**: `string`

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

[HuggingFaceInferenceEmbeddingsParams](/docs/api/embeddings_hf/interfaces/HuggingFaceInferenceEmbeddingsParams).[model](/docs/api/embeddings_hf/interfaces/HuggingFaceInferenceEmbeddingsParams#model)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/embeddings/hf.ts:16](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/hf.ts#L16)

### apiKey?[​](#apikey "Direct link to apiKey?")

> **apiKey**: `string`

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

[HuggingFaceInferenceEmbeddingsParams](/docs/api/embeddings_hf/interfaces/HuggingFaceInferenceEmbeddingsParams).[apiKey](/docs/api/embeddings_hf/interfaces/HuggingFaceInferenceEmbeddingsParams#apikey)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/embeddings/hf.ts:14](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/hf.ts#L14)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### \_embed()[​](#_embed "Direct link to _embed")

> **\_embed**(`texts`: `string`\[\]): `Promise`<`number`\[\]\[\]\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`texts`

`string`\[\]

#### Returns[​](#returns-1 "Direct link to Returns")

`Promise`<`number`\[\]\[\]\>

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/embeddings/hf.ts:30](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/hf.ts#L30)

### embedDocuments()[​](#embeddocuments "Direct link to embedDocuments()")

> **embedDocuments**(`documents`: `string`\[\]): `Promise`<`number`\[\]\[\]\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`documents`

`string`\[\]

#### Returns[​](#returns-2 "Direct link to Returns")

`Promise`<`number`\[\]\[\]\>

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[Embeddings](/docs/api/embeddings_base/classes/Embeddings).[embedDocuments](/docs/api/embeddings_base/classes/Embeddings#embeddocuments)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/embeddings/hf.ts:45](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/hf.ts#L45)

### embedQuery()[​](#embedquery "Direct link to embedQuery()")

> **embedQuery**(`document`: `string`): `Promise`<`number`\[\]\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`document`

`string`

#### Returns[​](#returns-3 "Direct link to Returns")

`Promise`<`number`\[\]\>

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[Embeddings](/docs/api/embeddings_base/classes/Embeddings).[embedQuery](/docs/api/embeddings_base/classes/Embeddings#embedquery)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/embeddings/hf.ts:41](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/hf.ts#L41)