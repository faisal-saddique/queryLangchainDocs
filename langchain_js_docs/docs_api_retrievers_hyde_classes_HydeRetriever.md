HydeRetriever<V\>
=================

Type parameters[​](#type-parameters "Direct link to Type parameters")
---------------------------------------------------------------------

*   `V` _extends_ [`VectorStore`](/docs/api/vectorstores_base/classes/VectorStore) = [`VectorStore`](/docs/api/vectorstores_base/classes/VectorStore)

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`VectorStoreRetriever`](/docs/api/vectorstores_base/classes/VectorStoreRetriever)<`V`\>.**HydeRetriever**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new HydeRetriever**<V\>(`fields`: [`HydeRetrieverOptions`](/docs/api/retrievers_hyde/interfaces/HydeRetrieverOptions)<`V`\>): [`HydeRetriever`](/docs/api/retrievers_hyde/classes/HydeRetriever)<`V`\>

#### Type parameters[​](#type-parameters-1 "Direct link to Type parameters")

*   `V` _extends_ [`VectorStore`](/docs/api/vectorstores_base/classes/VectorStore)<`V`\> = [`VectorStore`](/docs/api/vectorstores_base/classes/VectorStore)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields`

[`HydeRetrieverOptions`](/docs/api/retrievers_hyde/interfaces/HydeRetrieverOptions)<`V`\>

#### Returns[​](#returns "Direct link to Returns")

[`HydeRetriever`](/docs/api/retrievers_hyde/classes/HydeRetriever)<`V`\>

#### Overrides[​](#overrides "Direct link to Overrides")

[VectorStoreRetriever](/docs/api/vectorstores_base/classes/VectorStoreRetriever).[constructor](/docs/api/vectorstores_base/classes/VectorStoreRetriever#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/retrievers/hyde.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/hyde.ts#L40)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### k[​](#k "Direct link to k")

> **k**: `number` = `4`

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[VectorStoreRetriever](/docs/api/vectorstores_base/classes/VectorStoreRetriever).[k](/docs/api/vectorstores_base/classes/VectorStoreRetriever#k)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:29](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/base.ts#L29)

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[VectorStoreRetriever](/docs/api/vectorstores_base/classes/VectorStoreRetriever).[lc\_kwargs](/docs/api/vectorstores_base/classes/VectorStoreRetriever#lc_kwargs)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[VectorStoreRetriever](/docs/api/vectorstores_base/classes/VectorStoreRetriever).[lc\_serializable](/docs/api/vectorstores_base/classes/VectorStoreRetriever#lc_serializable)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L55)

### llm[​](#llm "Direct link to llm")

> **llm**: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/retrievers/hyde.ts:36](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/hyde.ts#L36)

### vectorStore[​](#vectorstore "Direct link to vectorStore")

> **vectorStore**: `V`

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[VectorStoreRetriever](/docs/api/vectorstores_base/classes/VectorStoreRetriever).[vectorStore](/docs/api/vectorstores_base/classes/VectorStoreRetriever#vectorstore)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:27](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/base.ts#L27)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[VectorStoreRetriever](/docs/api/vectorstores_base/classes/VectorStoreRetriever).[callbacks](/docs/api/vectorstores_base/classes/VectorStoreRetriever#callbacks)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L23)

### filter?[​](#filter "Direct link to filter?")

> **filter**: `V`\["FilterType"\]

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[VectorStoreRetriever](/docs/api/vectorstores_base/classes/VectorStoreRetriever).[filter](/docs/api/vectorstores_base/classes/VectorStoreRetriever#filter)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:31](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/base.ts#L31)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[VectorStoreRetriever](/docs/api/vectorstores_base/classes/VectorStoreRetriever).[metadata](/docs/api/vectorstores_base/classes/VectorStoreRetriever#metadata)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:27](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L27)

### promptTemplate?[​](#prompttemplate "Direct link to promptTemplate?")

> **promptTemplate**: [`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/retrievers/hyde.ts:38](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/hyde.ts#L38)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

[VectorStoreRetriever](/docs/api/vectorstores_base/classes/VectorStoreRetriever).[tags](/docs/api/vectorstores_base/classes/VectorStoreRetriever#tags)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:25](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L25)

### verbose?[​](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[VectorStoreRetriever](/docs/api/vectorstores_base/classes/VectorStoreRetriever).[verbose](/docs/api/vectorstores_base/classes/VectorStoreRetriever#verbose)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:29](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L29)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-1 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

VectorStoreRetriever.lc\_aliases

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

[VectorStoreRetriever](/docs/api/vectorstores_base/classes/VectorStoreRetriever).[lc\_aliases](/docs/api/vectorstores_base/classes/VectorStoreRetriever#lc_aliases)

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

VectorStoreRetriever.lc\_attributes

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

[VectorStoreRetriever](/docs/api/vectorstores_base/classes/VectorStoreRetriever).[lc\_attributes](/docs/api/vectorstores_base/classes/VectorStoreRetriever#lc_attributes)

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

> **lc\_namespace**(): `string`\[\]

#### Returns[​](#returns-3 "Direct link to Returns")

`string`\[\]

#### Overrides[​](#overrides-1 "Direct link to Overrides")

VectorStoreRetriever.lc\_namespace

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/retrievers/hyde.ts:32](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/hyde.ts#L32)

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[VectorStoreRetriever](/docs/api/vectorstores_base/classes/VectorStoreRetriever).[lc\_namespace](/docs/api/vectorstores_base/classes/VectorStoreRetriever#lc_namespace)

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/retrievers/hyde.ts:32](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/hyde.ts#L32)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-4 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

VectorStoreRetriever.lc\_secrets

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

[VectorStoreRetriever](/docs/api/vectorstores_base/classes/VectorStoreRetriever).[lc\_secrets](/docs/api/vectorstores_base/classes/VectorStoreRetriever#lc_secrets)

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### \_getRelevantDocuments()[​](#_getrelevantdocuments "Direct link to _getrelevantdocuments")

TODO: This should be an abstract method, but we'd like to avoid breaking changes to people currently using subclassed custom retrievers. Change it on next major release.

> **\_getRelevantDocuments**(`query`: `string`, `runManager`?: `CallbackManagerForRetrieverRun`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`query`

`string`

`runManager?`

`CallbackManagerForRetrieverRun`

#### Returns[​](#returns-5 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Overrides[​](#overrides-3 "Direct link to Overrides")

[VectorStoreRetriever](/docs/api/vectorstores_base/classes/VectorStoreRetriever).[\_getRelevantDocuments](/docs/api/vectorstores_base/classes/VectorStoreRetriever#_getrelevantdocuments)

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/retrievers/hyde.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/hyde.ts#L57)

### \_vectorstoreType()[​](#_vectorstoretype "Direct link to _vectorstoretype")

> **\_vectorstoreType**(): `string`

#### Returns[​](#returns-6 "Direct link to Returns")

`string`

#### Inherited from[​](#inherited-from-15 "Direct link to Inherited from")

[VectorStoreRetriever](/docs/api/vectorstores_base/classes/VectorStoreRetriever).[\_vectorstoreType](/docs/api/vectorstores_base/classes/VectorStoreRetriever#_vectorstoretype)

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:33](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/base.ts#L33)

### addDocuments()[​](#adddocuments "Direct link to addDocuments()")

> **addDocuments**(`documents`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], `options`?: `AddDocumentOptions`): `Promise`<`void` | `string`\[\]\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`documents`

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

`options?`

`AddDocumentOptions`

#### Returns[​](#returns-7 "Direct link to Returns")

`Promise`<`void` | `string`\[\]\>

#### Inherited from[​](#inherited-from-16 "Direct link to Inherited from")

[VectorStoreRetriever](/docs/api/vectorstores_base/classes/VectorStoreRetriever).[addDocuments](/docs/api/vectorstores_base/classes/VectorStoreRetriever#adddocuments)

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/vectorstores/base.ts:56](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/base.ts#L56)

### getRelevantDocuments()[​](#getrelevantdocuments "Direct link to getRelevantDocuments()")

> **getRelevantDocuments**(`query`: `string`, `config`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`query`

`string`

`config?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`

#### Returns[​](#returns-8 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Inherited from[​](#inherited-from-17 "Direct link to Inherited from")

[VectorStoreRetriever](/docs/api/vectorstores_base/classes/VectorStoreRetriever).[getRelevantDocuments](/docs/api/vectorstores_base/classes/VectorStoreRetriever#getrelevantdocuments)

#### Defined in[​](#defined-in-23 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:51](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L51)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-9 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-18 "Direct link to Inherited from")

[VectorStoreRetriever](/docs/api/vectorstores_base/classes/VectorStoreRetriever).[toJSON](/docs/api/vectorstores_base/classes/VectorStoreRetriever#tojson)

#### Defined in[​](#defined-in-24 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-10 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-19 "Direct link to Inherited from")

[VectorStoreRetriever](/docs/api/vectorstores_base/classes/VectorStoreRetriever).[toJSONNotImplemented](/docs/api/vectorstores_base/classes/VectorStoreRetriever#tojsonnotimplemented)

#### Defined in[​](#defined-in-25 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)