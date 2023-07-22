GooglePaLMEmbeddings
====================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`Embeddings`](/docs/api/embeddings_base/classes/Embeddings).**GooglePaLMEmbeddings**

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   [`GooglePaLMEmbeddingsParams`](/docs/api/embeddings_googlepalm/interfaces/GooglePaLMEmbeddingsParams)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new GooglePaLMEmbeddings**(`fields`?: [`GooglePaLMEmbeddingsParams`](/docs/api/embeddings_googlepalm/interfaces/GooglePaLMEmbeddingsParams)): [`GooglePaLMEmbeddings`](/docs/api/embeddings_googlepalm/classes/GooglePaLMEmbeddings)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields?`

[`GooglePaLMEmbeddingsParams`](/docs/api/embeddings_googlepalm/interfaces/GooglePaLMEmbeddingsParams)

#### Returns[​](#returns "Direct link to Returns")

[`GooglePaLMEmbeddings`](/docs/api/embeddings_googlepalm/classes/GooglePaLMEmbeddings)

#### Overrides[​](#overrides "Direct link to Overrides")

[Embeddings](/docs/api/embeddings_base/classes/Embeddings).[constructor](/docs/api/embeddings_base/classes/Embeddings#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/embeddings/googlepalm.ts:29](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/googlepalm.ts#L29)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### caller[​](#caller "Direct link to caller")

> **caller**: `AsyncCaller`

The async caller should be used by subclasses to make any async calls, which will thus benefit from the concurrency and retry logic.

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[Embeddings](/docs/api/embeddings_base/classes/Embeddings).[caller](/docs/api/embeddings_base/classes/Embeddings#caller)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/embeddings/base.ts:10](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/base.ts#L10)

### modelName[​](#modelname "Direct link to modelName")

> **modelName**: `string` = `"models/embedding-gecko-001"`

Model Name to use

Note: The format must follow the pattern - `models/{model}`

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

[GooglePaLMEmbeddingsParams](/docs/api/embeddings_googlepalm/interfaces/GooglePaLMEmbeddingsParams).[modelName](/docs/api/embeddings_googlepalm/interfaces/GooglePaLMEmbeddingsParams#modelname)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/embeddings/googlepalm.ts:25](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/googlepalm.ts#L25)

### apiKey?[​](#apikey "Direct link to apiKey?")

> **apiKey**: `string`

Google Palm API key to use

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

[GooglePaLMEmbeddingsParams](/docs/api/embeddings_googlepalm/interfaces/GooglePaLMEmbeddingsParams).[apiKey](/docs/api/embeddings_googlepalm/interfaces/GooglePaLMEmbeddingsParams#apikey)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/embeddings/googlepalm.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/googlepalm.ts#L23)

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

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/embeddings/googlepalm.ts:65](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/googlepalm.ts#L65)

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

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/embeddings/googlepalm.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/googlepalm.ts#L57)

### \_embedText()[​](#_embedtext "Direct link to _embedtext")

> `Protected` **\_embedText**(`text`: `string`): `Promise`<`number`\[\]\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`text`

`string`

#### Returns[​](#returns-3 "Direct link to Returns")

`Promise`<`number`\[\]\>

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/embeddings/googlepalm.ts:47](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/googlepalm.ts#L47)