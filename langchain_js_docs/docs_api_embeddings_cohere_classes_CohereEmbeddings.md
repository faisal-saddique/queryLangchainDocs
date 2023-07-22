CohereEmbeddings
================

A class for generating embeddings using the Cohere API.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`Embeddings`](/docs/api/embeddings_base/classes/Embeddings).**CohereEmbeddings**

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   [`CohereEmbeddingsParams`](/docs/api/embeddings_cohere/interfaces/CohereEmbeddingsParams)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

Constructor for the CohereEmbeddings class.

> **new CohereEmbeddings**(`fields`?: `Partial`<[`CohereEmbeddingsParams`](/docs/api/embeddings_cohere/interfaces/CohereEmbeddingsParams)\> & {`apiKey`?: `string`; `verbose`?: `boolean`;}): [`CohereEmbeddings`](/docs/api/embeddings_cohere/classes/CohereEmbeddings)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

Description

`fields?`

`Partial`<[`CohereEmbeddingsParams`](/docs/api/embeddings_cohere/interfaces/CohereEmbeddingsParams)\> & {`apiKey`?: `string`;  
`verbose`?: `boolean`;}

An optional object with properties to configure the instance.

#### Returns[​](#returns "Direct link to Returns")

[`CohereEmbeddings`](/docs/api/embeddings_cohere/classes/CohereEmbeddings)

#### Overrides[​](#overrides "Direct link to Overrides")

[Embeddings](/docs/api/embeddings_base/classes/Embeddings).[constructor](/docs/api/embeddings_base/classes/Embeddings#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/embeddings/cohere.ts:34](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/cohere.ts#L34)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### batchSize[​](#batchsize "Direct link to batchSize")

> **batchSize**: `number` = `48`

The maximum number of documents to embed in a single request. This is limited by the Cohere API to a maximum of 96.

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

[CohereEmbeddingsParams](/docs/api/embeddings_cohere/interfaces/CohereEmbeddingsParams).[batchSize](/docs/api/embeddings_cohere/interfaces/CohereEmbeddingsParams#batchsize)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/embeddings/cohere.ts:24](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/cohere.ts#L24)

### caller[​](#caller "Direct link to caller")

> **caller**: `AsyncCaller`

The async caller should be used by subclasses to make any async calls, which will thus benefit from the concurrency and retry logic.

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[Embeddings](/docs/api/embeddings_base/classes/Embeddings).[caller](/docs/api/embeddings_base/classes/Embeddings#caller)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/embeddings/base.ts:10](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/base.ts#L10)

### modelName[​](#modelname "Direct link to modelName")

> **modelName**: `string` = `"small"`

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

[CohereEmbeddingsParams](/docs/api/embeddings_cohere/interfaces/CohereEmbeddingsParams).[modelName](/docs/api/embeddings_cohere/interfaces/CohereEmbeddingsParams#modelname)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/embeddings/cohere.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/cohere.ts#L22)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### embedDocuments()[​](#embeddocuments "Direct link to embedDocuments()")

Generates embeddings for an array of texts.

> **embedDocuments**(`texts`: `string`\[\]): `Promise`<`number`\[\]\[\]\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

Description

`texts`

`string`\[\]

An array of strings to generate embeddings for.

#### Returns[​](#returns-1 "Direct link to Returns")

`Promise`<`number`\[\]\[\]\>

A Promise that resolves to an array of embeddings.

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[Embeddings](/docs/api/embeddings_base/classes/Embeddings).[embedDocuments](/docs/api/embeddings_base/classes/Embeddings#embeddocuments)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/embeddings/cohere.ts:58](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/cohere.ts#L58)

### embedQuery()[​](#embedquery "Direct link to embedQuery()")

Generates an embedding for a single text.

> **embedQuery**(`text`: `string`): `Promise`<`number`\[\]\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

Description

`text`

`string`

A string to generate an embedding for.

#### Returns[​](#returns-2 "Direct link to Returns")

`Promise`<`number`\[\]\>

A Promise that resolves to an array of numbers representing the embedding.

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[Embeddings](/docs/api/embeddings_base/classes/Embeddings).[embedQuery](/docs/api/embeddings_base/classes/Embeddings#embedquery)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/embeddings/cohere.ts:84](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/cohere.ts#L84)