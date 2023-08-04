SaveableVectorStore
===================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`VectorStore`](/docs/api/vectorstores_base/classes/VectorStore).**SaveableVectorStore**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new SaveableVectorStore**(`embeddings`: [`Embeddings`](/docs/api/embeddings_base/classes/Embeddings), `dbConfig`: `Record`<`string`, `any`\>): [`SaveableVectorStore`](/docs/api/vectorstores_base/classes/SaveableVectorStore)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`embeddings`

[`Embeddings`](/docs/api/embeddings_base/classes/Embeddings)

`dbConfig`

`Record`<`string`, `any`\>

#### Returns[](#returns "Direct link to Returns")

[`SaveableVectorStore`](/docs/api/vectorstores_base/classes/SaveableVectorStore)

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[constructor](/docs/api/vectorstores_base/classes/VectorStore#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:72](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/base.ts#L72)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### FilterType[](#filtertype "Direct link to FilterType")

> **FilterType**: `string` | `object`

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[FilterType](/docs/api/vectorstores_base/classes/VectorStore#filtertype)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:65](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/base.ts#L65)

### embeddings[](#embeddings "Direct link to embeddings")

> **embeddings**: [`Embeddings`](/docs/api/embeddings_base/classes/Embeddings)

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[embeddings](/docs/api/vectorstores_base/classes/VectorStore#embeddings)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:69](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/base.ts#L69)

### lc\_kwargs[](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[lc\_kwargs](/docs/api/vectorstores_base/classes/VectorStore#lc_kwargs)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L57)

### lc\_namespace[](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[lc\_namespace](/docs/api/vectorstores_base/classes/VectorStore#lc_namespace)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:67](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/base.ts#L67)

### lc\_serializable[](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[lc\_serializable](/docs/api/vectorstores_base/classes/VectorStore#lc_serializable)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L55)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[](#returns-1 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

VectorStore.lc\_aliases

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[lc\_aliases](/docs/api/vectorstores_base/classes/VectorStore#lc_aliases)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

### lc\_attributes[](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[](#returns-2 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

VectorStore.lc\_attributes

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L80)

#### Inherited from[](#inherited-from-9 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[lc\_attributes](/docs/api/vectorstores_base/classes/VectorStore#lc_attributes)

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L80)

### lc\_secrets[](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-10 "Direct link to Inherited from")

VectorStore.lc\_secrets

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

#### Inherited from[](#inherited-from-11 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[lc\_secrets](/docs/api/vectorstores_base/classes/VectorStore#lc_secrets)

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### \_vectorstoreType()[](#_vectorstoretype "Direct link to _vectorstoretype")

> `Abstract` **\_vectorstoreType**(): `string`

#### Returns[](#returns-4 "Direct link to Returns")

`string`

#### Inherited from[](#inherited-from-12 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[\_vectorstoreType](/docs/api/vectorstores_base/classes/VectorStore#_vectorstoretype)

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:77](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/base.ts#L77)

### addDocuments()[](#adddocuments "Direct link to addDocuments()")

> `Abstract` **addDocuments**(`documents`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], `options`?: `AddDocumentOptions`): `Promise`<`void` | `string`\[\]\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`documents`

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

`options?`

`AddDocumentOptions`

#### Returns[](#returns-5 "Direct link to Returns")

`Promise`<`void` | `string`\[\]\>

#### Inherited from[](#inherited-from-13 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[addDocuments](/docs/api/vectorstores_base/classes/VectorStore#adddocuments)

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:85](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/base.ts#L85)

### addVectors()[](#addvectors "Direct link to addVectors()")

> `Abstract` **addVectors**(`vectors`: `number`\[\]\[\], `documents`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], `options`?: `AddDocumentOptions`): `Promise`<`void` | `string`\[\]\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`vectors`

`number`\[\]\[\]

`documents`

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

`options?`

`AddDocumentOptions`

#### Returns[](#returns-6 "Direct link to Returns")

`Promise`<`void` | `string`\[\]\>

#### Inherited from[](#inherited-from-14 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[addVectors](/docs/api/vectorstores_base/classes/VectorStore#addvectors)

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:79](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/base.ts#L79)

### asRetriever()[](#asretriever "Direct link to asRetriever()")

> **asRetriever**(`kOrFields`?: `number` | `Partial`<[`VectorStoreRetrieverInput`](/docs/api/vectorstores_base/interfaces/VectorStoreRetrieverInput)<[`SaveableVectorStore`](/docs/api/vectorstores_base/classes/SaveableVectorStore)\>\>, `filter`?: `string` | `object`, `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks), `tags`?: `string`\[\], `metadata`?: `Record`<`string`, `unknown`\>, `verbose`?: `boolean`): [`VectorStoreRetriever`](/docs/api/vectorstores_base/classes/VectorStoreRetriever)<[`SaveableVectorStore`](/docs/api/vectorstores_base/classes/SaveableVectorStore)\>

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

`kOrFields?`

`number` | `Partial`<[`VectorStoreRetrieverInput`](/docs/api/vectorstores_base/interfaces/VectorStoreRetrieverInput)<[`SaveableVectorStore`](/docs/api/vectorstores_base/classes/SaveableVectorStore)\>\>

`filter?`

`string` | `object`

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

`tags?`

`string`\[\]

`metadata?`

`Record`<`string`, `unknown`\>

`verbose?`

`boolean`

#### Returns[](#returns-7 "Direct link to Returns")

[`VectorStoreRetriever`](/docs/api/vectorstores_base/classes/VectorStoreRetriever)<[`SaveableVectorStore`](/docs/api/vectorstores_base/classes/SaveableVectorStore)\>

#### Inherited from[](#inherited-from-15 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[asRetriever](/docs/api/vectorstores_base/classes/VectorStore#asretriever)

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:152](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/base.ts#L152)

### delete()[](#delete "Direct link to delete()")

> **delete**(`_params`?: `Record`<`string`, `any`\>): `Promise`<`void`\>

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

`_params?`

`Record`<`string`, `any`\>

#### Returns[](#returns-8 "Direct link to Returns")

`Promise`<`void`\>

#### Inherited from[](#inherited-from-16 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[delete](/docs/api/vectorstores_base/classes/VectorStore#delete)

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:91](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/base.ts#L91)

### save()[](#save "Direct link to save()")

> `Abstract` **save**(`directory`: `string`): `Promise`<`void`\>

#### Parameters[](#parameters-5 "Direct link to Parameters")

Parameter

Type

`directory`

`string`

#### Returns[](#returns-9 "Direct link to Returns")

`Promise`<`void`\>

#### Defined in[](#defined-in-17 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:185](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/base.ts#L185)

### similaritySearch()[](#similaritysearch "Direct link to similaritySearch()")

> **similaritySearch**(`query`: `string`, `k`: `number` = `4`, `filter`: `undefined` | `string` | `object` = `undefined`, `_callbacks`: `undefined` | [`Callbacks`](/docs/api/callbacks/types/Callbacks) = `undefined`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[](#parameters-6 "Direct link to Parameters")

Parameter

Type

Default value

`query`

`string`

`undefined`

`k`

`number`

`4`

`filter`

`undefined` | `string` | `object`

`undefined`

`_callbacks`

`undefined` | [`Callbacks`](/docs/api/callbacks/types/Callbacks)

`undefined`

#### Returns[](#returns-10 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Inherited from[](#inherited-from-17 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[similaritySearch](/docs/api/vectorstores_base/classes/VectorStore#similaritysearch)

#### Defined in[](#defined-in-18 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:101](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/base.ts#L101)

### similaritySearchVectorWithScore()[](#similaritysearchvectorwithscore "Direct link to similaritySearchVectorWithScore()")

> `Abstract` **similaritySearchVectorWithScore**(`query`: `number`\[\], `k`: `number`, `filter`?: `string` | `object`): `Promise`<\[[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>, `number`\]\[\]\>

#### Parameters[](#parameters-7 "Direct link to Parameters")

Parameter

Type

`query`

`number`\[\]

`k`

`number`

`filter?`

`string` | `object`

#### Returns[](#returns-11 "Direct link to Returns")

`Promise`<\[[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>, `number`\]\[\]\>

#### Inherited from[](#inherited-from-18 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[similaritySearchVectorWithScore](/docs/api/vectorstores_base/classes/VectorStore#similaritysearchvectorwithscore)

#### Defined in[](#defined-in-19 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:95](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/base.ts#L95)

### similaritySearchWithScore()[](#similaritysearchwithscore "Direct link to similaritySearchWithScore()")

> **similaritySearchWithScore**(`query`: `string`, `k`: `number` = `4`, `filter`: `undefined` | `string` | `object` = `undefined`, `_callbacks`: `undefined` | [`Callbacks`](/docs/api/callbacks/types/Callbacks) = `undefined`): `Promise`<\[[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>, `number`\]\[\]\>

#### Parameters[](#parameters-8 "Direct link to Parameters")

Parameter

Type

Default value

`query`

`string`

`undefined`

`k`

`number`

`4`

`filter`

`undefined` | `string` | `object`

`undefined`

`_callbacks`

`undefined` | [`Callbacks`](/docs/api/callbacks/types/Callbacks)

`undefined`

#### Returns[](#returns-12 "Direct link to Returns")

`Promise`<\[[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>, `number`\]\[\]\>

#### Inherited from[](#inherited-from-19 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[similaritySearchWithScore](/docs/api/vectorstores_base/classes/VectorStore#similaritysearchwithscore)

#### Defined in[](#defined-in-20 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:116](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/base.ts#L116)

### toJSON()[](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[](#returns-13 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[](#inherited-from-20 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[toJSON](/docs/api/vectorstores_base/classes/VectorStore#tojson)

#### Defined in[](#defined-in-21 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[](#returns-14 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[](#inherited-from-21 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[toJSONNotImplemented](/docs/api/vectorstores_base/classes/VectorStore#tojsonnotimplemented)

#### Defined in[](#defined-in-22 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L151)

### fromDocuments()[](#fromdocuments "Direct link to fromDocuments()")

> `Static` **fromDocuments**(`_docs`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], `_embeddings`: [`Embeddings`](/docs/api/embeddings_base/classes/Embeddings), `_dbConfig`: `Record`<`string`, `any`\>): `Promise`<[`VectorStore`](/docs/api/vectorstores_base/classes/VectorStore)\>

#### Parameters[](#parameters-9 "Direct link to Parameters")

Parameter

Type

`_docs`

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

`_embeddings`

[`Embeddings`](/docs/api/embeddings_base/classes/Embeddings)

`_dbConfig`

`Record`<`string`, `any`\>

#### Returns[](#returns-15 "Direct link to Returns")

`Promise`<[`VectorStore`](/docs/api/vectorstores_base/classes/VectorStore)\>

#### Inherited from[](#inherited-from-22 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[fromDocuments](/docs/api/vectorstores_base/classes/VectorStore#fromdocuments)

#### Defined in[](#defined-in-23 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:141](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/base.ts#L141)

### fromTexts()[](#fromtexts "Direct link to fromTexts()")

> `Static` **fromTexts**(`_texts`: `string`\[\], `_metadatas`: `object` | `object`\[\], `_embeddings`: [`Embeddings`](/docs/api/embeddings_base/classes/Embeddings), `_dbConfig`: `Record`<`string`, `any`\>): `Promise`<[`VectorStore`](/docs/api/vectorstores_base/classes/VectorStore)\>

#### Parameters[](#parameters-10 "Direct link to Parameters")

Parameter

Type

`_texts`

`string`\[\]

`_metadatas`

`object` | `object`\[\]

`_embeddings`

[`Embeddings`](/docs/api/embeddings_base/classes/Embeddings)

`_dbConfig`

`Record`<`string`, `any`\>

#### Returns[](#returns-16 "Direct link to Returns")

`Promise`<[`VectorStore`](/docs/api/vectorstores_base/classes/VectorStore)\>

#### Inherited from[](#inherited-from-23 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[fromTexts](/docs/api/vectorstores_base/classes/VectorStore#fromtexts)

#### Defined in[](#defined-in-24 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:129](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/base.ts#L129)

### load()[](#load "Direct link to load()")

> `Static` **load**(`_directory`: `string`, `_embeddings`: [`Embeddings`](/docs/api/embeddings_base/classes/Embeddings)): `Promise`<[`SaveableVectorStore`](/docs/api/vectorstores_base/classes/SaveableVectorStore)\>

#### Parameters[](#parameters-11 "Direct link to Parameters")

Parameter

Type

`_directory`

`string`

`_embeddings`

[`Embeddings`](/docs/api/embeddings_base/classes/Embeddings)

#### Returns[](#returns-17 "Direct link to Returns")

`Promise`<[`SaveableVectorStore`](/docs/api/vectorstores_base/classes/SaveableVectorStore)\>

#### Defined in[](#defined-in-25 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:187](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/base.ts#L187)