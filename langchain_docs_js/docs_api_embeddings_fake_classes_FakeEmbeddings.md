FakeEmbeddings
==============

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`Embeddings`](/docs/api/embeddings_base/classes/Embeddings).**FakeEmbeddings**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new FakeEmbeddings**(`params`?: `AsyncCallerParams`): [`FakeEmbeddings`](/docs/api/embeddings_fake/classes/FakeEmbeddings)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`params?`

`AsyncCallerParams`

#### Returns[](#returns "Direct link to Returns")

[`FakeEmbeddings`](/docs/api/embeddings_fake/classes/FakeEmbeddings)

#### Overrides[](#overrides "Direct link to Overrides")

[Embeddings](/docs/api/embeddings_base/classes/Embeddings).[constructor](/docs/api/embeddings_base/classes/Embeddings#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/embeddings/fake.ts:4](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/embeddings/fake.ts#L4)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### caller[](#caller "Direct link to caller")

> **caller**: `AsyncCaller`

The async caller should be used by subclasses to make any async calls, which will thus benefit from the concurrency and retry logic.

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[Embeddings](/docs/api/embeddings_base/classes/Embeddings).[caller](/docs/api/embeddings_base/classes/Embeddings#caller)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/embeddings/base.ts:10](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/embeddings/base.ts#L10)

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

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/embeddings/fake.ts:8](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/embeddings/fake.ts#L8)

### embedQuery()[](#embedquery "Direct link to embedQuery()")

> **embedQuery**(`_`: `string`): `Promise`<`number`\[\]\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`_`

`string`

#### Returns[](#returns-2 "Direct link to Returns")

`Promise`<`number`\[\]\>

#### Overrides[](#overrides-2 "Direct link to Overrides")

[Embeddings](/docs/api/embeddings_base/classes/Embeddings).[embedQuery](/docs/api/embeddings_base/classes/Embeddings#embedquery)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/embeddings/fake.ts:12](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/embeddings/fake.ts#L12)