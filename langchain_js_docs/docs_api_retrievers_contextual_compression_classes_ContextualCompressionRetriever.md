ContextualCompressionRetriever
==============================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseRetriever`](/docs/api/schema_retriever/classes/BaseRetriever).**ContextualCompressionRetriever**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new ContextualCompressionRetriever**(`fields`: [`ContextualCompressionRetrieverArgs`](/docs/api/retrievers_contextual_compression/interfaces/ContextualCompressionRetrieverArgs)): [`ContextualCompressionRetriever`](/docs/api/retrievers_contextual_compression/classes/ContextualCompressionRetriever)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields`

[`ContextualCompressionRetrieverArgs`](/docs/api/retrievers_contextual_compression/interfaces/ContextualCompressionRetrieverArgs)

#### Returns[​](#returns "Direct link to Returns")

[`ContextualCompressionRetriever`](/docs/api/retrievers_contextual_compression/classes/ContextualCompressionRetriever)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[constructor](/docs/api/schema_retriever/classes/BaseRetriever#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/retrievers/contextual\_compression.ts:18](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/contextual_compression.ts#L18)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### baseCompressor[​](#basecompressor "Direct link to baseCompressor")

> **baseCompressor**: [`BaseDocumentCompressor`](/docs/api/retrievers_document_compressors/classes/BaseDocumentCompressor)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/retrievers/contextual\_compression.ts:14](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/contextual_compression.ts#L14)

### baseRetriever[​](#baseretriever "Direct link to baseRetriever")

> **baseRetriever**: [`BaseRetriever`](/docs/api/schema_retriever/classes/BaseRetriever)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/retrievers/contextual\_compression.ts:16](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/contextual_compression.ts#L16)

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[lc\_kwargs](/docs/api/schema_retriever/classes/BaseRetriever#lc_kwargs)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[lc\_namespace](/docs/api/schema_retriever/classes/BaseRetriever#lc_namespace)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/retrievers/contextual\_compression.ts:12](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/contextual_compression.ts#L12)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[lc\_serializable](/docs/api/schema_retriever/classes/BaseRetriever#lc_serializable)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L55)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[callbacks](/docs/api/schema_retriever/classes/BaseRetriever#callbacks)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L23)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[metadata](/docs/api/schema_retriever/classes/BaseRetriever#metadata)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:27](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L27)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[tags](/docs/api/schema_retriever/classes/BaseRetriever#tags)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:25](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L25)

### verbose?[​](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[verbose](/docs/api/schema_retriever/classes/BaseRetriever#verbose)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:29](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L29)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-1 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

BaseRetriever.lc\_aliases

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[lc\_aliases](/docs/api/schema_retriever/classes/BaseRetriever#lc_aliases)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

BaseRetriever.lc\_attributes

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[lc\_attributes](/docs/api/schema_retriever/classes/BaseRetriever#lc_attributes)

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

BaseRetriever.lc\_secrets

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[lc\_secrets](/docs/api/schema_retriever/classes/BaseRetriever#lc_secrets)

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

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

#### Returns[​](#returns-4 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[\_getRelevantDocuments](/docs/api/schema_retriever/classes/BaseRetriever#_getrelevantdocuments)

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/retrievers/contextual\_compression.ts:25](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/contextual_compression.ts#L25)

### getRelevantDocuments()[​](#getrelevantdocuments "Direct link to getRelevantDocuments()")

> **getRelevantDocuments**(`query`: `string`, `config`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`query`

`string`

`config?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`

#### Returns[​](#returns-5 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[getRelevantDocuments](/docs/api/schema_retriever/classes/BaseRetriever#getrelevantdocuments)

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:51](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L51)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-6 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[toJSON](/docs/api/schema_retriever/classes/BaseRetriever#tojson)

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-7 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[toJSONNotImplemented](/docs/api/schema_retriever/classes/BaseRetriever#tojsonnotimplemented)

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)