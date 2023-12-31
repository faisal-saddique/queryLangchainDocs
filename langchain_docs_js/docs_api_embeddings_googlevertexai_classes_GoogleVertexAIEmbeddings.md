GoogleVertexAIEmbeddings
========================

Enables calls to the Google Cloud's Vertex AI API to access the embeddings generated by Large Language Models.

To use, you will need to have one of the following authentication methods in place:

*   You are logged into an account permitted to the Google Cloud project using Vertex AI.
*   You are running this on a machine using a service account permitted to the Google Cloud project using Vertex AI.
*   The `GOOGLE_APPLICATION_CREDENTIALS` environment variable is set to the path of a credentials file for a service account permitted to the Google Cloud project using Vertex AI.

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`Embeddings`](/docs/api/embeddings_base/classes/Embeddings).**GoogleVertexAIEmbeddings**

Implements[](#implements "Direct link to Implements")
------------------------------------------------------

*   [`GoogleVertexAIEmbeddingsParams`](/docs/api/embeddings_googlevertexai/interfaces/GoogleVertexAIEmbeddingsParams)

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new GoogleVertexAIEmbeddings**(`fields`?: [`GoogleVertexAIEmbeddingsParams`](/docs/api/embeddings_googlevertexai/interfaces/GoogleVertexAIEmbeddingsParams)): [`GoogleVertexAIEmbeddings`](/docs/api/embeddings_googlevertexai/classes/GoogleVertexAIEmbeddings)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`fields?`

[`GoogleVertexAIEmbeddingsParams`](/docs/api/embeddings_googlevertexai/interfaces/GoogleVertexAIEmbeddingsParams)

#### Returns[](#returns "Direct link to Returns")

[`GoogleVertexAIEmbeddings`](/docs/api/embeddings_googlevertexai/classes/GoogleVertexAIEmbeddings)

#### Overrides[](#overrides "Direct link to Overrides")

[Embeddings](/docs/api/embeddings_base/classes/Embeddings).[constructor](/docs/api/embeddings_base/classes/Embeddings#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/embeddings/googlevertexai.ts:56](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/embeddings/googlevertexai.ts#L56)

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

> **model**: `string` = `"textembedding-gecko"`

Model to use

#### Implementation of[](#implementation-of "Direct link to Implementation of")

[GoogleVertexAIEmbeddingsParams](/docs/api/embeddings_googlevertexai/interfaces/GoogleVertexAIEmbeddingsParams).[model](/docs/api/embeddings_googlevertexai/interfaces/GoogleVertexAIEmbeddingsParams#model)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/embeddings/googlevertexai.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/embeddings/googlevertexai.ts#L48)

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

[langchain/src/embeddings/googlevertexai.ts:67](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/embeddings/googlevertexai.ts#L67)

### embedQuery()[](#embedquery "Direct link to embedQuery()")

> **embedQuery**(`document`: `string`): `Promise`<`number`\[\]\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`document`

`string`

#### Returns[](#returns-2 "Direct link to Returns")

`Promise`<`number`\[\]\>

#### Overrides[](#overrides-2 "Direct link to Overrides")

[Embeddings](/docs/api/embeddings_base/classes/Embeddings).[embedQuery](/docs/api/embeddings_base/classes/Embeddings#embedquery)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/embeddings/googlevertexai.ts:93](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/embeddings/googlevertexai.ts#L93)