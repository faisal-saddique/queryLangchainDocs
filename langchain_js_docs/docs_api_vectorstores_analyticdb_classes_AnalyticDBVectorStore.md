AnalyticDBVectorStore
=====================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`VectorStore`](/docs/api/vectorstores_base/classes/VectorStore).**AnalyticDBVectorStore**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new AnalyticDBVectorStore**(`embeddings`: [`Embeddings`](/docs/api/embeddings_base/classes/Embeddings), `args`: [`AnalyticDBArgs`](/docs/api/vectorstores_analyticdb/interfaces/AnalyticDBArgs)): [`AnalyticDBVectorStore`](/docs/api/vectorstores_analyticdb/classes/AnalyticDBVectorStore)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`embeddings`

[`Embeddings`](/docs/api/embeddings_base/classes/Embeddings)

`args`

[`AnalyticDBArgs`](/docs/api/vectorstores_analyticdb/interfaces/AnalyticDBArgs)

#### Returns[​](#returns "Direct link to Returns")

[`AnalyticDBVectorStore`](/docs/api/vectorstores_analyticdb/classes/AnalyticDBVectorStore)

#### Overrides[​](#overrides "Direct link to Overrides")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[constructor](/docs/api/vectorstores_base/classes/VectorStore#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/vectorstores/analyticdb.ts:47](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/analyticdb.ts#L47)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### FilterType[​](#filtertype "Direct link to FilterType")

> **FilterType**: `Record`<`string`, `any`\>

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[FilterType](/docs/api/vectorstores_base/classes/VectorStore#filtertype)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/vectorstores/analyticdb.ts:31](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/analyticdb.ts#L31)

### embeddings[​](#embeddings "Direct link to embeddings")

> **embeddings**: [`Embeddings`](/docs/api/embeddings_base/classes/Embeddings)

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[embeddings](/docs/api/vectorstores_base/classes/VectorStore#embeddings)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:69](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/base.ts#L69)

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[lc\_kwargs](/docs/api/vectorstores_base/classes/VectorStore#lc_kwargs)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[lc\_namespace](/docs/api/vectorstores_base/classes/VectorStore#lc_namespace)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:67](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/base.ts#L67)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[lc\_serializable](/docs/api/vectorstores_base/classes/VectorStore#lc_serializable)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L55)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-1 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

VectorStore.lc\_aliases

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[lc\_aliases](/docs/api/vectorstores_base/classes/VectorStore#lc_aliases)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

VectorStore.lc\_attributes

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[lc\_attributes](/docs/api/vectorstores_base/classes/VectorStore#lc_attributes)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

VectorStore.lc\_secrets

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[lc\_secrets](/docs/api/vectorstores_base/classes/VectorStore#lc_secrets)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### \_vectorstoreType()[​](#_vectorstoretype "Direct link to _vectorstoretype")

> **\_vectorstoreType**(): `string`

#### Returns[​](#returns-4 "Direct link to Returns")

`string`

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[\_vectorstoreType](/docs/api/vectorstores_base/classes/VectorStore#_vectorstoretype)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/vectorstores/analyticdb.ts:43](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/analyticdb.ts#L43)

### addDocuments()[​](#adddocuments "Direct link to addDocuments()")

> **addDocuments**(`documents`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]): `Promise`<`void`\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`documents`

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

#### Returns[​](#returns-5 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[​](#overrides-3 "Direct link to Overrides")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[addDocuments](/docs/api/vectorstores_base/classes/VectorStore#adddocuments)

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/vectorstores/analyticdb.ts:125](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/analyticdb.ts#L125)

### addVectors()[​](#addvectors "Direct link to addVectors()")

> **addVectors**(`vectors`: `number`\[\]\[\], `documents`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]): `Promise`<`void`\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`vectors`

`number`\[\]\[\]

`documents`

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

#### Returns[​](#returns-6 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[​](#overrides-4 "Direct link to Overrides")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[addVectors](/docs/api/vectorstores_base/classes/VectorStore#addvectors)

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/vectorstores/analyticdb.ts:133](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/analyticdb.ts#L133)

### asRetriever()[​](#asretriever "Direct link to asRetriever()")

> **asRetriever**(`kOrFields`?: `number` | [`VectorStoreRetrieverInput`](/docs/api/vectorstores_base/interfaces/VectorStoreRetrieverInput)<[`AnalyticDBVectorStore`](/docs/api/vectorstores_analyticdb/classes/AnalyticDBVectorStore)\>, `filter`?: `Record`<`string`, `any`\>, `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks), `tags`?: `string`\[\], `metadata`?: `Record`<`string`, `unknown`\>, `verbose`?: `boolean`): [`VectorStoreRetriever`](/docs/api/vectorstores_base/classes/VectorStoreRetriever)<[`AnalyticDBVectorStore`](/docs/api/vectorstores_analyticdb/classes/AnalyticDBVectorStore)\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`kOrFields?`

`number` | [`VectorStoreRetrieverInput`](/docs/api/vectorstores_base/interfaces/VectorStoreRetrieverInput)<[`AnalyticDBVectorStore`](/docs/api/vectorstores_analyticdb/classes/AnalyticDBVectorStore)\>

`filter?`

`Record`<`string`, `any`\>

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

`tags?`

`string`\[\]

`metadata?`

`Record`<`string`, `unknown`\>

`verbose?`

`boolean`

#### Returns[​](#returns-7 "Direct link to Returns")

[`VectorStoreRetriever`](/docs/api/vectorstores_base/classes/VectorStoreRetriever)<[`AnalyticDBVectorStore`](/docs/api/vectorstores_analyticdb/classes/AnalyticDBVectorStore)\>

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[asRetriever](/docs/api/vectorstores_base/classes/VectorStore#asretriever)

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:152](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/base.ts#L152)

### createCollection()[​](#createcollection "Direct link to createCollection()")

> **createCollection**(): `Promise`<`void`\>

#### Returns[​](#returns-8 "Direct link to Returns")

`Promise`<`void`\>

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/vectorstores/analyticdb.ts:117](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/analyticdb.ts#L117)

### createTableIfNotExists()[​](#createtableifnotexists "Direct link to createTableIfNotExists()")

> **createTableIfNotExists**(): `Promise`<`void`\>

#### Returns[​](#returns-9 "Direct link to Returns")

`Promise`<`void`\>

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/vectorstores/analyticdb.ts:68](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/analyticdb.ts#L68)

### delete()[​](#delete "Direct link to delete()")

> **delete**(`_params`?: `Record`<`string`, `any`\>): `Promise`<`void`\>

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`_params?`

`Record`<`string`, `any`\>

#### Returns[​](#returns-10 "Direct link to Returns")

`Promise`<`void`\>

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[delete](/docs/api/vectorstores_base/classes/VectorStore#delete)

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:91](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/base.ts#L91)

### deleteCollection()[​](#deletecollection "Direct link to deleteCollection()")

> **deleteCollection**(): `Promise`<`void`\>

#### Returns[​](#returns-11 "Direct link to Returns")

`Promise`<`void`\>

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/vectorstores/analyticdb.ts:112](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/analyticdb.ts#L112)

### end()[​](#end "Direct link to end()")

> **end**(): `Promise`<`void`\>

#### Returns[​](#returns-12 "Direct link to Returns")

`Promise`<`void`\>

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/vectorstores/analyticdb.ts:64](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/analyticdb.ts#L64)

### similaritySearch()[​](#similaritysearch "Direct link to similaritySearch()")

> **similaritySearch**(`query`: `string`, `k`: `number` = `4`, `filter`: `undefined` | `Record`<`string`, `any`\> = `undefined`, `_callbacks`: `undefined` | [`Callbacks`](/docs/api/callbacks/types/Callbacks) = `undefined`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[​](#parameters-5 "Direct link to Parameters")

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

`undefined` | `Record`<`string`, `any`\>

`undefined`

`_callbacks`

`undefined` | [`Callbacks`](/docs/api/callbacks/types/Callbacks)

`undefined`

#### Returns[​](#returns-13 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[similaritySearch](/docs/api/vectorstores_base/classes/VectorStore#similaritysearch)

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:101](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/base.ts#L101)

### similaritySearchVectorWithScore()[​](#similaritysearchvectorwithscore "Direct link to similaritySearchVectorWithScore()")

> **similaritySearchVectorWithScore**(`query`: `number`\[\], `k`: `number`, `filter`?: `Record`<`string`, `any`\>): `Promise`<\[[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>, `number`\]\[\]\>

#### Parameters[​](#parameters-6 "Direct link to Parameters")

Parameter

Type

`query`

`number`\[\]

`k`

`number`

`filter?`

`Record`<`string`, `any`\>

#### Returns[​](#returns-14 "Direct link to Returns")

`Promise`<\[[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>, `number`\]\[\]\>

#### Overrides[​](#overrides-5 "Direct link to Overrides")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[similaritySearchVectorWithScore](/docs/api/vectorstores_base/classes/VectorStore#similaritysearchvectorwithscore)

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/vectorstores/analyticdb.ts:221](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/analyticdb.ts#L221)

### similaritySearchWithScore()[​](#similaritysearchwithscore "Direct link to similaritySearchWithScore()")

> **similaritySearchWithScore**(`query`: `string`, `k`: `number` = `4`, `filter`: `undefined` | `Record`<`string`, `any`\> = `undefined`, `_callbacks`: `undefined` | [`Callbacks`](/docs/api/callbacks/types/Callbacks) = `undefined`): `Promise`<\[[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>, `number`\]\[\]\>

#### Parameters[​](#parameters-7 "Direct link to Parameters")

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

`undefined` | `Record`<`string`, `any`\>

`undefined`

`_callbacks`

`undefined` | [`Callbacks`](/docs/api/callbacks/types/Callbacks)

`undefined`

#### Returns[​](#returns-15 "Direct link to Returns")

`Promise`<\[[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>, `number`\]\[\]\>

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[similaritySearchWithScore](/docs/api/vectorstores_base/classes/VectorStore#similaritysearchwithscore)

#### Defined in[​](#defined-in-23 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:116](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/base.ts#L116)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-16 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[toJSON](/docs/api/vectorstores_base/classes/VectorStore#tojson)

#### Defined in[​](#defined-in-24 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-17 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-15 "Direct link to Inherited from")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[toJSONNotImplemented](/docs/api/vectorstores_base/classes/VectorStore#tojsonnotimplemented)

#### Defined in[​](#defined-in-25 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)

### fromDocuments()[​](#fromdocuments "Direct link to fromDocuments()")

> `Static` **fromDocuments**(`docs`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], `embeddings`: [`Embeddings`](/docs/api/embeddings_base/classes/Embeddings), `dbConfig`: [`AnalyticDBArgs`](/docs/api/vectorstores_analyticdb/interfaces/AnalyticDBArgs)): `Promise`<[`AnalyticDBVectorStore`](/docs/api/vectorstores_analyticdb/classes/AnalyticDBVectorStore)\>

#### Parameters[​](#parameters-8 "Direct link to Parameters")

Parameter

Type

`docs`

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

`embeddings`

[`Embeddings`](/docs/api/embeddings_base/classes/Embeddings)

`dbConfig`

[`AnalyticDBArgs`](/docs/api/vectorstores_analyticdb/interfaces/AnalyticDBArgs)

#### Returns[​](#returns-18 "Direct link to Returns")

`Promise`<[`AnalyticDBVectorStore`](/docs/api/vectorstores_analyticdb/classes/AnalyticDBVectorStore)\>

#### Overrides[​](#overrides-6 "Direct link to Overrides")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[fromDocuments](/docs/api/vectorstores_base/classes/VectorStore#fromdocuments)

#### Defined in[​](#defined-in-26 "Direct link to Defined in")

[langchain/src/vectorstores/analyticdb.ts:280](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/analyticdb.ts#L280)

### fromExistingIndex()[​](#fromexistingindex "Direct link to fromExistingIndex()")

> `Static` **fromExistingIndex**(`embeddings`: [`Embeddings`](/docs/api/embeddings_base/classes/Embeddings), `dbConfig`: [`AnalyticDBArgs`](/docs/api/vectorstores_analyticdb/interfaces/AnalyticDBArgs)): `Promise`<[`AnalyticDBVectorStore`](/docs/api/vectorstores_analyticdb/classes/AnalyticDBVectorStore)\>

#### Parameters[​](#parameters-9 "Direct link to Parameters")

Parameter

Type

`embeddings`

[`Embeddings`](/docs/api/embeddings_base/classes/Embeddings)

`dbConfig`

[`AnalyticDBArgs`](/docs/api/vectorstores_analyticdb/interfaces/AnalyticDBArgs)

#### Returns[​](#returns-19 "Direct link to Returns")

`Promise`<[`AnalyticDBVectorStore`](/docs/api/vectorstores_analyticdb/classes/AnalyticDBVectorStore)\>

#### Defined in[​](#defined-in-27 "Direct link to Defined in")

[langchain/src/vectorstores/analyticdb.ts:290](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/analyticdb.ts#L290)

### fromTexts()[​](#fromtexts "Direct link to fromTexts()")

> `Static` **fromTexts**(`texts`: `string`\[\], `metadatas`: `object` | `object`\[\], `embeddings`: [`Embeddings`](/docs/api/embeddings_base/classes/Embeddings), `dbConfig`: [`AnalyticDBArgs`](/docs/api/vectorstores_analyticdb/interfaces/AnalyticDBArgs)): `Promise`<[`AnalyticDBVectorStore`](/docs/api/vectorstores_analyticdb/classes/AnalyticDBVectorStore)\>

#### Parameters[​](#parameters-10 "Direct link to Parameters")

Parameter

Type

`texts`

`string`\[\]

`metadatas`

`object` | `object`\[\]

`embeddings`

[`Embeddings`](/docs/api/embeddings_base/classes/Embeddings)

`dbConfig`

[`AnalyticDBArgs`](/docs/api/vectorstores_analyticdb/interfaces/AnalyticDBArgs)

#### Returns[​](#returns-20 "Direct link to Returns")

`Promise`<[`AnalyticDBVectorStore`](/docs/api/vectorstores_analyticdb/classes/AnalyticDBVectorStore)\>

#### Overrides[​](#overrides-7 "Direct link to Overrides")

[VectorStore](/docs/api/vectorstores_base/classes/VectorStore).[fromTexts](/docs/api/vectorstores_base/classes/VectorStore#fromtexts)

#### Defined in[​](#defined-in-28 "Direct link to Defined in")

[langchain/src/vectorstores/analyticdb.ts:262](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/analyticdb.ts#L262)