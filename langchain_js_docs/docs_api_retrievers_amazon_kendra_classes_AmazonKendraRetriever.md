AmazonKendraRetriever
=====================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseRetriever`](/docs/api/schema_retriever/classes/BaseRetriever).**AmazonKendraRetriever**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new AmazonKendraRetriever**(«destructured»: [`AmazonKendraRetrieverArgs`](/docs/api/retrievers_amazon_kendra/interfaces/AmazonKendraRetrieverArgs)): [`AmazonKendraRetriever`](/docs/api/retrievers_amazon_kendra/classes/AmazonKendraRetriever)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`«destructured»`

[`AmazonKendraRetrieverArgs`](/docs/api/retrievers_amazon_kendra/interfaces/AmazonKendraRetrieverArgs)

#### Returns[​](#returns "Direct link to Returns")

[`AmazonKendraRetriever`](/docs/api/retrievers_amazon_kendra/classes/AmazonKendraRetriever)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[constructor](/docs/api/schema_retriever/classes/BaseRetriever#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/retrievers/amazon\_kendra.ts:37](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/amazon_kendra.ts#L37)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### indexId[​](#indexid "Direct link to indexId")

> **indexId**: `string`

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/retrievers/amazon\_kendra.ts:29](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/amazon_kendra.ts#L29)

### kendraClient[​](#kendraclient "Direct link to kendraClient")

> **kendraClient**: `KendraClient`

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/retrievers/amazon\_kendra.ts:33](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/amazon_kendra.ts#L33)

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

[langchain/src/retrievers/amazon\_kendra.ts:27](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/amazon_kendra.ts#L27)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[lc\_serializable](/docs/api/schema_retriever/classes/BaseRetriever#lc_serializable)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L55)

### topK[​](#topk "Direct link to topK")

> **topK**: `number`

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/retrievers/amazon\_kendra.ts:31](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/amazon_kendra.ts#L31)

### attributeFilter?[​](#attributefilter "Direct link to attributeFilter?")

> **attributeFilter**: `AttributeFilter`

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/retrievers/amazon\_kendra.ts:35](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/amazon_kendra.ts#L35)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[callbacks](/docs/api/schema_retriever/classes/BaseRetriever#callbacks)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L23)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[metadata](/docs/api/schema_retriever/classes/BaseRetriever#metadata)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:27](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L27)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[tags](/docs/api/schema_retriever/classes/BaseRetriever#tags)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:25](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L25)

### verbose?[​](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[verbose](/docs/api/schema_retriever/classes/BaseRetriever#verbose)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

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

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[lc\_aliases](/docs/api/schema_retriever/classes/BaseRetriever#lc_aliases)

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

BaseRetriever.lc\_attributes

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[lc\_attributes](/docs/api/schema_retriever/classes/BaseRetriever#lc_attributes)

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

BaseRetriever.lc\_secrets

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[lc\_secrets](/docs/api/schema_retriever/classes/BaseRetriever#lc_secrets)

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### \_getRelevantDocuments()[​](#_getrelevantdocuments "Direct link to _getrelevantdocuments")

TODO: This should be an abstract method, but we'd like to avoid breaking changes to people currently using subclassed custom retrievers. Change it on next major release.

> **\_getRelevantDocuments**(`query`: `string`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`query`

`string`

#### Returns[​](#returns-4 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[\_getRelevantDocuments](/docs/api/schema_retriever/classes/BaseRetriever#_getrelevantdocuments)

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/retrievers/amazon\_kendra.ts:226](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/amazon_kendra.ts#L226)

### cleanResult()[​](#cleanresult "Direct link to cleanResult()")

> **cleanResult**(`resText`: `string`): `string`

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`resText`

`string`

#### Returns[​](#returns-5 "Direct link to Returns")

`string`

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/retrievers/amazon\_kendra.ts:76](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/amazon_kendra.ts#L76)

### combineText()[​](#combinetext "Direct link to combineText()")

> **combineText**(`title`?: `string`, `excerpt`?: `string`): `string`

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`title?`

`string`

`excerpt?`

`string`

#### Returns[​](#returns-6 "Direct link to Returns")

`string`

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/retrievers/amazon\_kendra.ts:64](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/amazon_kendra.ts#L64)

### convertQueryItem()[​](#convertqueryitem "Direct link to convertQueryItem()")

> **convertQueryItem**(`item`: `QueryResultItem`): [`Document`](/docs/api/document/classes/Document)<{`document_attributes`: {}; `excerpt`: `string`; `source`: `undefined` | `string`; `title`: `string`;}\>

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`item`

`QueryResultItem`

#### Returns[​](#returns-7 "Direct link to Returns")

[`Document`](/docs/api/document/classes/Document)<{`document_attributes`: {}; `excerpt`: `string`; `source`: `undefined` | `string`; `title`: `string`;}\>

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/retrievers/amazon\_kendra.ts:168](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/amazon_kendra.ts#L168)

### convertRetrieverItem()[​](#convertretrieveritem "Direct link to convertRetrieverItem()")

> **convertRetrieverItem**(`item`: `RetrieveResultItem`): [`Document`](/docs/api/document/classes/Document)<{`document_attributes`: {}; `excerpt`: `string`; `source`: `undefined` | `string`; `title`: `string`;}\>

#### Parameters[​](#parameters-5 "Direct link to Parameters")

Parameter

Type

`item`

`RetrieveResultItem`

#### Returns[​](#returns-8 "Direct link to Returns")

[`Document`](/docs/api/document/classes/Document)<{`document_attributes`: {}; `excerpt`: `string`; `source`: `undefined` | `string`; `title`: `string`;}\>

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/retrievers/amazon\_kendra.ts:114](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/amazon_kendra.ts#L114)

### getDocAttributeValue()[​](#getdocattributevalue "Direct link to getDocAttributeValue()")

> **getDocAttributeValue**(`value`: `DocumentAttributeValue`): `string` | `number` | `string`\[\] | `Date`

#### Parameters[​](#parameters-6 "Direct link to Parameters")

Parameter

Type

`value`

`DocumentAttributeValue`

#### Returns[​](#returns-9 "Direct link to Returns")

`string` | `number` | `string`\[\] | `Date`

#### Defined in[​](#defined-in-23 "Direct link to Defined in")

[langchain/src/retrievers/amazon\_kendra.ts:82](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/amazon_kendra.ts#L82)

### getDocAttributes()[​](#getdocattributes "Direct link to getDocAttributes()")

> **getDocAttributes**(`documentAttributes`?: `DocumentAttribute`\[\]): `object`

#### Parameters[​](#parameters-7 "Direct link to Parameters")

Parameter

Type

`documentAttributes?`

`DocumentAttribute`\[\]

#### Returns[​](#returns-10 "Direct link to Returns")

`object`

#### Defined in[​](#defined-in-24 "Direct link to Defined in")

[langchain/src/retrievers/amazon\_kendra.ts:99](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/amazon_kendra.ts#L99)

### getQueryDocs()[​](#getquerydocs "Direct link to getQueryDocs()")

> **getQueryDocs**(`response`: `QueryCommandOutput`, `pageSize`: `number`): [`Document`](/docs/api/document/classes/Document)<{`document_attributes`: {}; `excerpt`: `string`; `source`: `undefined` | `string`; `title`: `string`;}\>\[\]

#### Parameters[​](#parameters-8 "Direct link to Parameters")

Parameter

Type

`response`

`QueryCommandOutput`

`pageSize`

`number`

#### Returns[​](#returns-11 "Direct link to Returns")

[`Document`](/docs/api/document/classes/Document)<{`document_attributes`: {}; `excerpt`: `string`; `source`: `undefined` | `string`; `title`: `string`;}\>\[\]

#### Defined in[​](#defined-in-25 "Direct link to Defined in")

[langchain/src/retrievers/amazon\_kendra.ts:185](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/amazon_kendra.ts#L185)

### getQueryItemExcerpt()[​](#getqueryitemexcerpt "Direct link to getQueryItemExcerpt()")

> **getQueryItemExcerpt**(`item`: `QueryResultItem`): `string`

#### Parameters[​](#parameters-9 "Direct link to Parameters")

Parameter

Type

`item`

`QueryResultItem`

#### Returns[​](#returns-12 "Direct link to Returns")

`string`

#### Defined in[​](#defined-in-26 "Direct link to Defined in")

[langchain/src/retrievers/amazon\_kendra.ts:145](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/amazon_kendra.ts#L145)

### getRelevantDocuments()[​](#getrelevantdocuments "Direct link to getRelevantDocuments()")

> **getRelevantDocuments**(`query`: `string`, `config`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[​](#parameters-10 "Direct link to Parameters")

Parameter

Type

`query`

`string`

`config?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`

#### Returns[​](#returns-13 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[getRelevantDocuments](/docs/api/schema_retriever/classes/BaseRetriever#getrelevantdocuments)

#### Defined in[​](#defined-in-27 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:51](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L51)

### getRetrieverDocs()[​](#getretrieverdocs "Direct link to getRetrieverDocs()")

> **getRetrieverDocs**(`response`: `RetrieveCommandOutput`, `pageSize`: `number`): [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

#### Parameters[​](#parameters-11 "Direct link to Parameters")

Parameter

Type

`response`

`RetrieveCommandOutput`

`pageSize`

`number`

#### Returns[​](#returns-14 "Direct link to Returns")

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

#### Defined in[​](#defined-in-28 "Direct link to Defined in")

[langchain/src/retrievers/amazon\_kendra.ts:131](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/amazon_kendra.ts#L131)

### queryKendra()[​](#querykendra "Direct link to queryKendra()")

> **queryKendra**(`query`: `string`, `topK`: `number`, `attributeFilter`?: `AttributeFilter`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\] | [`Document`](/docs/api/document/classes/Document)<{`document_attributes`: {}; `excerpt`: `string`; `source`: `undefined` | `string`; `title`: `string`;}\>\[\]\>

#### Parameters[​](#parameters-12 "Direct link to Parameters")

Parameter

Type

`query`

`string`

`topK`

`number`

`attributeFilter?`

`AttributeFilter`

#### Returns[​](#returns-15 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\] | [`Document`](/docs/api/document/classes/Document)<{`document_attributes`: {}; `excerpt`: `string`; `source`: `undefined` | `string`; `title`: `string`;}\>\[\]\>

#### Defined in[​](#defined-in-29 "Direct link to Defined in")

[langchain/src/retrievers/amazon\_kendra.ts:195](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/amazon_kendra.ts#L195)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-16 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[toJSON](/docs/api/schema_retriever/classes/BaseRetriever#tojson)

#### Defined in[​](#defined-in-30 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-17 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[toJSONNotImplemented](/docs/api/schema_retriever/classes/BaseRetriever#tojsonnotimplemented)

#### Defined in[​](#defined-in-31 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)