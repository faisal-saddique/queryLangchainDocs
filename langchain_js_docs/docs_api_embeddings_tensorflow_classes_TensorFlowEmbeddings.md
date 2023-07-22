TensorFlowEmbeddings
====================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`Embeddings`](/docs/api/embeddings_base/classes/Embeddings).**TensorFlowEmbeddings**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new TensorFlowEmbeddings**(`fields`?: [`TensorFlowEmbeddingsParams`](/docs/api/embeddings_tensorflow/interfaces/TensorFlowEmbeddingsParams)): [`TensorFlowEmbeddings`](/docs/api/embeddings_tensorflow/classes/TensorFlowEmbeddings)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields?`

[`TensorFlowEmbeddingsParams`](/docs/api/embeddings_tensorflow/interfaces/TensorFlowEmbeddingsParams)

#### Returns[​](#returns "Direct link to Returns")

[`TensorFlowEmbeddings`](/docs/api/embeddings_tensorflow/classes/TensorFlowEmbeddings)

#### Overrides[​](#overrides "Direct link to Overrides")

[Embeddings](/docs/api/embeddings_base/classes/Embeddings).[constructor](/docs/api/embeddings_base/classes/Embeddings#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/embeddings/tensorflow.ts:9](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/tensorflow.ts#L9)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### \_cached[​](#_cached "Direct link to _cached")

> **\_cached**: `Promise`<`UniversalSentenceEncoder`\>

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/embeddings/tensorflow.ts:19](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/tensorflow.ts#L19)

### caller[​](#caller "Direct link to caller")

> **caller**: `AsyncCaller`

The async caller should be used by subclasses to make any async calls, which will thus benefit from the concurrency and retry logic.

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[Embeddings](/docs/api/embeddings_base/classes/Embeddings).[caller](/docs/api/embeddings_base/classes/Embeddings#caller)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/embeddings/base.ts:10](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/base.ts#L10)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### embedDocuments()[​](#embeddocuments "Direct link to embedDocuments()")

> **embedDocuments**(`documents`: `string`\[\]): `Promise`<`number`\[\]\[\]\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`documents`

`string`\[\]

#### Returns[​](#returns-1 "Direct link to Returns")

`Promise`<`number`\[\]\[\]\>

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[Embeddings](/docs/api/embeddings_base/classes/Embeddings).[embedDocuments](/docs/api/embeddings_base/classes/Embeddings#embeddocuments)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/embeddings/tensorflow.ts:41](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/tensorflow.ts#L41)

### embedQuery()[​](#embedquery "Direct link to embedQuery()")

> **embedQuery**(`document`: `string`): `Promise`<`number`\[\]\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`document`

`string`

#### Returns[​](#returns-2 "Direct link to Returns")

`Promise`<`number`\[\]\>

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[Embeddings](/docs/api/embeddings_base/classes/Embeddings).[embedQuery](/docs/api/embeddings_base/classes/Embeddings#embedquery)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/embeddings/tensorflow.ts:35](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/tensorflow.ts#L35)