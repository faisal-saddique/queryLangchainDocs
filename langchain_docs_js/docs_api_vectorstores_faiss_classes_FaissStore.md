FaissStore
==========

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`SaveableVectorStore`](/docs/api/vectorstores_base/classes/SaveableVectorStore).**FaissStore**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new FaissStore**(`embeddings`: [`Embeddings`](/docs/api/embeddings_base/classes/Embeddings), `args`: [`FaissLibArgs`](/docs/api/vectorstores_faiss/interfaces/FaissLibArgs)): [`FaissStore`](/docs/api/vectorstores_faiss/classes/FaissStore)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`embeddings`

[`Embeddings`](/docs/api/embeddings_base/classes/Embeddings)

`args`

[`FaissLibArgs`](/docs/api/vectorstores_faiss/interfaces/FaissLibArgs)

#### Returns[](#returns "Direct link to Returns")

[`FaissStore`](/docs/api/vectorstores_faiss/classes/FaissStore)

#### Overrides[](#overrides "Direct link to Overrides")

[SaveableVectorStore](/docs/api/vectorstores_base/classes/SaveableVectorStore).[constructor](/docs/api/vectorstores_base/classes/SaveableVectorStore#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/vectorstores/faiss.ts:28](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/faiss.ts#L28)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### FilterType[](#filtertype "Direct link to FilterType")

> **FilterType**: `string` | `object`

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[SaveableVectorStore](/docs/api/vectorstores_base/classes/SaveableVectorStore).[FilterType](/docs/api/vectorstores_base/classes/SaveableVectorStore#filtertype)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:65](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/base.ts#L65)

### \_mapping[](#_mapping "Direct link to _mapping")

> **\_mapping**: `Record`<`number`, `string`\>

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/vectorstores/faiss.ts:18](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/faiss.ts#L18)

### args[](#args "Direct link to args")

> **args**: [`FaissLibArgs`](/docs/api/vectorstores_faiss/interfaces/FaissLibArgs)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/vectorstores/faiss.ts:22](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/faiss.ts#L22)

### docstore[](#docstore "Direct link to docstore")

> **docstore**: [`SynchronousInMemoryDocstore`](/docs/api/stores_doc_in_memory/classes/SynchronousInMemoryDocstore)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/vectorstores/faiss.ts:20](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/faiss.ts#L20)

### embeddings[](#embeddings "Direct link to embeddings")

> **embeddings**: [`Embeddings`](/docs/api/embeddings_base/classes/Embeddings)

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[SaveableVectorStore](/docs/api/vectorstores_base/classes/SaveableVectorStore).[embeddings](/docs/api/vectorstores_base/classes/SaveableVectorStore#embeddings)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:69](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/base.ts#L69)

### lc\_kwargs[](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[SaveableVectorStore](/docs/api/vectorstores_base/classes/SaveableVectorStore).[lc\_kwargs](/docs/api/vectorstores_base/classes/SaveableVectorStore#lc_kwargs)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L57)

### lc\_namespace[](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[SaveableVectorStore](/docs/api/vectorstores_base/classes/SaveableVectorStore).[lc\_namespace](/docs/api/vectorstores_base/classes/SaveableVectorStore#lc_namespace)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:67](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/base.ts#L67)

### lc\_serializable[](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[SaveableVectorStore](/docs/api/vectorstores_base/classes/SaveableVectorStore).[lc\_serializable](/docs/api/vectorstores_base/classes/SaveableVectorStore#lc_serializable)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L55)

### \_index?[](#_index "Direct link to _index")

> **\_index**: `IndexFlatL2`

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/vectorstores/faiss.ts:16](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/faiss.ts#L16)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### index[](#index "Direct link to index")

> **index**(): `IndexFlatL2`

#### Returns[](#returns-1 "Direct link to Returns")

`IndexFlatL2`

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/vectorstores/faiss.ts:45](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/faiss.ts#L45)

> **index**(`index`: `IndexFlatL2`): `void`

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`index`

`IndexFlatL2`

#### Returns[](#returns-2 "Direct link to Returns")

`void`

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/vectorstores/faiss.ts:54](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/faiss.ts#L54)

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/vectorstores/faiss.ts:45](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/faiss.ts#L45) [langchain/src/vectorstores/faiss.ts:54](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/faiss.ts#L54)

### lc\_aliases[](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

SaveableVectorStore.lc\_aliases

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[SaveableVectorStore](/docs/api/vectorstores_base/classes/SaveableVectorStore).[lc\_aliases](/docs/api/vectorstores_base/classes/SaveableVectorStore#lc_aliases)

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

### lc\_attributes[](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[](#returns-4 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

SaveableVectorStore.lc\_attributes

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L80)

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

[SaveableVectorStore](/docs/api/vectorstores_base/classes/SaveableVectorStore).[lc\_attributes](/docs/api/vectorstores_base/classes/SaveableVectorStore#lc_attributes)

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L80)

### lc\_secrets[](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[](#returns-5 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-9 "Direct link to Inherited from")

SaveableVectorStore.lc\_secrets

#### Defined in[](#defined-in-17 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

#### Inherited from[](#inherited-from-10 "Direct link to Inherited from")

[SaveableVectorStore](/docs/api/vectorstores_base/classes/SaveableVectorStore).[lc\_secrets](/docs/api/vectorstores_base/classes/SaveableVectorStore#lc_secrets)

#### Defined in[](#defined-in-18 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### \_vectorstoreType()[](#_vectorstoretype "Direct link to _vectorstoretype")

> **\_vectorstoreType**(): `string`

#### Returns[](#returns-6 "Direct link to Returns")

`string`

#### Overrides[](#overrides-1 "Direct link to Overrides")

[SaveableVectorStore](/docs/api/vectorstores_base/classes/SaveableVectorStore).[\_vectorstoreType](/docs/api/vectorstores_base/classes/SaveableVectorStore#_vectorstoretype)

#### Defined in[](#defined-in-19 "Direct link to Defined in")

[langchain/src/vectorstores/faiss.ts:24](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/faiss.ts#L24)

### addDocuments()[](#adddocuments "Direct link to addDocuments()")

> **addDocuments**(`documents`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]): `Promise`<`string`\[\]\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`documents`

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

#### Returns[](#returns-7 "Direct link to Returns")

`Promise`<`string`\[\]\>

#### Overrides[](#overrides-2 "Direct link to Overrides")

[SaveableVectorStore](/docs/api/vectorstores_base/classes/SaveableVectorStore).[addDocuments](/docs/api/vectorstores_base/classes/SaveableVectorStore#adddocuments)

#### Defined in[](#defined-in-20 "Direct link to Defined in")

[langchain/src/vectorstores/faiss.ts:37](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/faiss.ts#L37)

### addVectors()[](#addvectors "Direct link to addVectors()")

> **addVectors**(`vectors`: `number`\[\]\[\], `documents`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]): `Promise`<`string`\[\]\>

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

`vectors`

`number`\[\]\[\]

`documents`

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

#### Returns[](#returns-8 "Direct link to Returns")

`Promise`<`string`\[\]\>

#### Overrides[](#overrides-3 "Direct link to Overrides")

[SaveableVectorStore](/docs/api/vectorstores_base/classes/SaveableVectorStore).[addVectors](/docs/api/vectorstores_base/classes/SaveableVectorStore#addvectors)

#### Defined in[](#defined-in-21 "Direct link to Defined in")

[langchain/src/vectorstores/faiss.ts:58](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/faiss.ts#L58)

### asRetriever()[](#asretriever "Direct link to asRetriever()")

> **asRetriever**(`kOrFields`?: `number` | `Partial`<[`VectorStoreRetrieverInput`](/docs/api/vectorstores_base/interfaces/VectorStoreRetrieverInput)<[`FaissStore`](/docs/api/vectorstores_faiss/classes/FaissStore)\>\>, `filter`?: `string` | `object`, `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks), `tags`?: `string`\[\], `metadata`?: `Record`<`string`, `unknown`\>, `verbose`?: `boolean`): [`VectorStoreRetriever`](/docs/api/vectorstores_base/classes/VectorStoreRetriever)<[`FaissStore`](/docs/api/vectorstores_faiss/classes/FaissStore)\>

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

`kOrFields?`

`number` | `Partial`<[`VectorStoreRetrieverInput`](/docs/api/vectorstores_base/interfaces/VectorStoreRetrieverInput)<[`FaissStore`](/docs/api/vectorstores_faiss/classes/FaissStore)\>\>

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

#### Returns[](#returns-9 "Direct link to Returns")

[`VectorStoreRetriever`](/docs/api/vectorstores_base/classes/VectorStoreRetriever)<[`FaissStore`](/docs/api/vectorstores_faiss/classes/FaissStore)\>

#### Inherited from[](#inherited-from-11 "Direct link to Inherited from")

[SaveableVectorStore](/docs/api/vectorstores_base/classes/SaveableVectorStore).[asRetriever](/docs/api/vectorstores_base/classes/SaveableVectorStore#asretriever)

#### Defined in[](#defined-in-22 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:152](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/base.ts#L152)

### delete()[](#delete "Direct link to delete()")

> **delete**(`_params`?: `Record`<`string`, `any`\>): `Promise`<`void`\>

#### Parameters[](#parameters-5 "Direct link to Parameters")

Parameter

Type

`_params?`

`Record`<`string`, `any`\>

#### Returns[](#returns-10 "Direct link to Returns")

`Promise`<`void`\>

#### Inherited from[](#inherited-from-12 "Direct link to Inherited from")

[SaveableVectorStore](/docs/api/vectorstores_base/classes/SaveableVectorStore).[delete](/docs/api/vectorstores_base/classes/SaveableVectorStore#delete)

#### Defined in[](#defined-in-23 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:91](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/base.ts#L91)

### save()[](#save "Direct link to save()")

> **save**(`directory`: `string`): `Promise`<`void`\>

#### Parameters[](#parameters-6 "Direct link to Parameters")

Parameter

Type

`directory`

`string`

#### Returns[](#returns-11 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[](#overrides-4 "Direct link to Overrides")

[SaveableVectorStore](/docs/api/vectorstores_base/classes/SaveableVectorStore).[save](/docs/api/vectorstores_base/classes/SaveableVectorStore#save)

#### Defined in[](#defined-in-24 "Direct link to Defined in")

[langchain/src/vectorstores/faiss.ts:115](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/faiss.ts#L115)

### similaritySearch()[](#similaritysearch "Direct link to similaritySearch()")

> **similaritySearch**(`query`: `string`, `k`: `number` = `4`, `filter`: `undefined` | `string` | `object` = `undefined`, `_callbacks`: `undefined` | [`Callbacks`](/docs/api/callbacks/types/Callbacks) = `undefined`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[](#parameters-7 "Direct link to Parameters")

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

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Inherited from[](#inherited-from-13 "Direct link to Inherited from")

[SaveableVectorStore](/docs/api/vectorstores_base/classes/SaveableVectorStore).[similaritySearch](/docs/api/vectorstores_base/classes/SaveableVectorStore#similaritysearch)

#### Defined in[](#defined-in-25 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:101](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/base.ts#L101)

### similaritySearchVectorWithScore()[](#similaritysearchvectorwithscore "Direct link to similaritySearchVectorWithScore()")

> **similaritySearchVectorWithScore**(`query`: `number`\[\], `k`: `number`): `Promise`<\[[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>, `number`\]\[\]\>

#### Parameters[](#parameters-8 "Direct link to Parameters")

Parameter

Type

`query`

`number`\[\]

`k`

`number`

#### Returns[](#returns-13 "Direct link to Returns")

`Promise`<\[[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>, `number`\]\[\]\>

#### Overrides[](#overrides-5 "Direct link to Overrides")

[SaveableVectorStore](/docs/api/vectorstores_base/classes/SaveableVectorStore).[similaritySearchVectorWithScore](/docs/api/vectorstores_base/classes/SaveableVectorStore#similaritysearchvectorwithscore)

#### Defined in[](#defined-in-26 "Direct link to Defined in")

[langchain/src/vectorstores/faiss.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/faiss.ts#L90)

### similaritySearchWithScore()[](#similaritysearchwithscore "Direct link to similaritySearchWithScore()")

> **similaritySearchWithScore**(`query`: `string`, `k`: `number` = `4`, `filter`: `undefined` | `string` | `object` = `undefined`, `_callbacks`: `undefined` | [`Callbacks`](/docs/api/callbacks/types/Callbacks) = `undefined`): `Promise`<\[[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>, `number`\]\[\]\>

#### Parameters[](#parameters-9 "Direct link to Parameters")

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

#### Returns[](#returns-14 "Direct link to Returns")

`Promise`<\[[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>, `number`\]\[\]\>

#### Inherited from[](#inherited-from-14 "Direct link to Inherited from")

[SaveableVectorStore](/docs/api/vectorstores_base/classes/SaveableVectorStore).[similaritySearchWithScore](/docs/api/vectorstores_base/classes/SaveableVectorStore#similaritysearchwithscore)

#### Defined in[](#defined-in-27 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:116](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/base.ts#L116)

### toJSON()[](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[](#returns-15 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[](#inherited-from-15 "Direct link to Inherited from")

[SaveableVectorStore](/docs/api/vectorstores_base/classes/SaveableVectorStore).[toJSON](/docs/api/vectorstores_base/classes/SaveableVectorStore#tojson)

#### Defined in[](#defined-in-28 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[](#returns-16 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[](#inherited-from-16 "Direct link to Inherited from")

[SaveableVectorStore](/docs/api/vectorstores_base/classes/SaveableVectorStore).[toJSONNotImplemented](/docs/api/vectorstores_base/classes/SaveableVectorStore#tojsonnotimplemented)

#### Defined in[](#defined-in-29 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L151)

### fromDocuments()[](#fromdocuments "Direct link to fromDocuments()")

> `Static` **fromDocuments**(`docs`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], `embeddings`: [`Embeddings`](/docs/api/embeddings_base/classes/Embeddings), `dbConfig`?: `object`): `Promise`<[`FaissStore`](/docs/api/vectorstores_faiss/classes/FaissStore)\>

#### Parameters[](#parameters-10 "Direct link to Parameters")

Parameter

Type

`docs`

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

`embeddings`

[`Embeddings`](/docs/api/embeddings_base/classes/Embeddings)

`dbConfig?`

`object`

`dbConfig.docstore?`

[`SynchronousInMemoryDocstore`](/docs/api/stores_doc_in_memory/classes/SynchronousInMemoryDocstore)

#### Returns[](#returns-17 "Direct link to Returns")

`Promise`<[`FaissStore`](/docs/api/vectorstores_faiss/classes/FaissStore)\>

#### Overrides[](#overrides-6 "Direct link to Overrides")

[SaveableVectorStore](/docs/api/vectorstores_base/classes/SaveableVectorStore).[fromDocuments](/docs/api/vectorstores_base/classes/SaveableVectorStore#fromdocuments)

#### Defined in[](#defined-in-30 "Direct link to Defined in")

[langchain/src/vectorstores/faiss.ts:241](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/faiss.ts#L241)

### fromTexts()[](#fromtexts "Direct link to fromTexts()")

> `Static` **fromTexts**(`texts`: `string`\[\], `metadatas`: `object` | `object`\[\], `embeddings`: [`Embeddings`](/docs/api/embeddings_base/classes/Embeddings), `dbConfig`?: `object`): `Promise`<[`FaissStore`](/docs/api/vectorstores_faiss/classes/FaissStore)\>

#### Parameters[](#parameters-11 "Direct link to Parameters")

Parameter

Type

`texts`

`string`\[\]

`metadatas`

`object` | `object`\[\]

`embeddings`

[`Embeddings`](/docs/api/embeddings_base/classes/Embeddings)

`dbConfig?`

`object`

`dbConfig.docstore?`

[`SynchronousInMemoryDocstore`](/docs/api/stores_doc_in_memory/classes/SynchronousInMemoryDocstore)

#### Returns[](#returns-18 "Direct link to Returns")

`Promise`<[`FaissStore`](/docs/api/vectorstores_faiss/classes/FaissStore)\>

#### Overrides[](#overrides-7 "Direct link to Overrides")

[SaveableVectorStore](/docs/api/vectorstores_base/classes/SaveableVectorStore).[fromTexts](/docs/api/vectorstores_base/classes/SaveableVectorStore#fromtexts)

#### Defined in[](#defined-in-31 "Direct link to Defined in")

[langchain/src/vectorstores/faiss.ts:221](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/faiss.ts#L221)

### importFaiss()[](#importfaiss "Direct link to importFaiss()")

> `Static` **importFaiss**(): `Promise`<{`IndexFlatL2`: _typeof_ `IndexFlatL2`;}\>

#### Returns[](#returns-19 "Direct link to Returns")

`Promise`<{`IndexFlatL2`: _typeof_ `IndexFlatL2`;}\>

#### Defined in[](#defined-in-32 "Direct link to Defined in")

[langchain/src/vectorstores/faiss.ts:256](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/faiss.ts#L256)

### importPickleparser()[](#importpickleparser "Direct link to importPickleparser()")

> `Static` **importPickleparser**(): `Promise`<{`NameRegistry`: _typeof_ `NameRegistry`; `Parser`: _typeof_ `Parser`;}\>

#### Returns[](#returns-20 "Direct link to Returns")

`Promise`<{`NameRegistry`: _typeof_ `NameRegistry`; `Parser`: _typeof_ `Parser`;}\>

#### Defined in[](#defined-in-33 "Direct link to Defined in")

[langchain/src/vectorstores/faiss.ts:271](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/faiss.ts#L271)

### load()[](#load "Direct link to load()")

> `Static` **load**(`directory`: `string`, `embeddings`: [`Embeddings`](/docs/api/embeddings_base/classes/Embeddings)): `Promise`<[`FaissStore`](/docs/api/vectorstores_faiss/classes/FaissStore)\>

#### Parameters[](#parameters-12 "Direct link to Parameters")

Parameter

Type

`directory`

`string`

`embeddings`

[`Embeddings`](/docs/api/embeddings_base/classes/Embeddings)

#### Returns[](#returns-21 "Direct link to Returns")

`Promise`<[`FaissStore`](/docs/api/vectorstores_faiss/classes/FaissStore)\>

#### Overrides[](#overrides-8 "Direct link to Overrides")

[SaveableVectorStore](/docs/api/vectorstores_base/classes/SaveableVectorStore).[load](/docs/api/vectorstores_base/classes/SaveableVectorStore#load)

#### Defined in[](#defined-in-34 "Direct link to Defined in")

[langchain/src/vectorstores/faiss.ts:131](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/faiss.ts#L131)

### loadFromPython()[](#loadfrompython "Direct link to loadFromPython()")

> `Static` **loadFromPython**(`directory`: `string`, `embeddings`: [`Embeddings`](/docs/api/embeddings_base/classes/Embeddings)): `Promise`<[`FaissStore`](/docs/api/vectorstores_faiss/classes/FaissStore)\>

#### Parameters[](#parameters-13 "Direct link to Parameters")

Parameter

Type

`directory`

`string`

`embeddings`

[`Embeddings`](/docs/api/embeddings_base/classes/Embeddings)

#### Returns[](#returns-22 "Direct link to Returns")

`Promise`<[`FaissStore`](/docs/api/vectorstores_faiss/classes/FaissStore)\>

#### Defined in[](#defined-in-35 "Direct link to Defined in")

[langchain/src/vectorstores/faiss.ts:152](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/faiss.ts#L152)