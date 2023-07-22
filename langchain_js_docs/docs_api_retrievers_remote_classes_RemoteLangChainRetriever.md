RemoteLangChainRetriever
========================

Base Index class. All indexes should extend this class.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`RemoteRetriever`](/docs/api/retrievers_remote/classes/RemoteRetriever).**RemoteLangChainRetriever**

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   [`RemoteLangChainRetrieverParams`](/docs/api/retrievers_remote/interfaces/RemoteLangChainRetrieverParams)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new RemoteLangChainRetriever**(«destructured»: [`RemoteLangChainRetrieverParams`](/docs/api/retrievers_remote/interfaces/RemoteLangChainRetrieverParams)): [`RemoteLangChainRetriever`](/docs/api/retrievers_remote/classes/RemoteLangChainRetriever)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`«destructured»`

[`RemoteLangChainRetrieverParams`](/docs/api/retrievers_remote/interfaces/RemoteLangChainRetrieverParams)

#### Returns[​](#returns "Direct link to Returns")

[`RemoteLangChainRetriever`](/docs/api/retrievers_remote/classes/RemoteLangChainRetriever)

#### Overrides[​](#overrides "Direct link to Overrides")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[constructor](/docs/api/retrievers_remote/classes/RemoteRetriever#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/retrievers/remote/remote-retriever.ts:41](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/remote/remote-retriever.ts#L41)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### asyncCaller[​](#asynccaller "Direct link to asyncCaller")

> **asyncCaller**: `AsyncCaller`

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[asyncCaller](/docs/api/retrievers_remote/classes/RemoteRetriever#asynccaller)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/retrievers/remote/base.ts:41](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/remote/base.ts#L41)

### auth[​](#auth "Direct link to auth")

> **auth**: [`RemoteRetrieverAuth`](/docs/api/retrievers_remote/types/RemoteRetrieverAuth)

The authentication method to use, currently implemented is

*   false: no authentication
*   { bearer: string }: Bearer token authentication

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

[RemoteLangChainRetrieverParams](/docs/api/retrievers_remote/interfaces/RemoteLangChainRetrieverParams).[auth](/docs/api/retrievers_remote/interfaces/RemoteLangChainRetrieverParams#auth)

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[auth](/docs/api/retrievers_remote/classes/RemoteRetriever#auth)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/retrievers/remote/base.ts:37](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/remote/base.ts#L37)

### headers[​](#headers "Direct link to headers")

> **headers**: `Record`<`string`, `string`\>

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[headers](/docs/api/retrievers_remote/classes/RemoteRetriever#headers)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/retrievers/remote/base.ts:39](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/remote/base.ts#L39)

### inputKey[​](#inputkey "Direct link to inputKey")

> **inputKey**: `string`

The key in the JSON body to put the query in

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

[RemoteLangChainRetrieverParams](/docs/api/retrievers_remote/interfaces/RemoteLangChainRetrieverParams).[inputKey](/docs/api/retrievers_remote/interfaces/RemoteLangChainRetrieverParams#inputkey)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/retrievers/remote/remote-retriever.ts:33](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/remote/remote-retriever.ts#L33)

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[lc\_kwargs](/docs/api/retrievers_remote/classes/RemoteRetriever#lc_kwargs)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[lc\_namespace](/docs/api/retrievers_remote/classes/RemoteRetriever#lc_namespace)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/retrievers/remote/remote-retriever.ts:31](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/remote/remote-retriever.ts#L31)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[lc\_serializable](/docs/api/retrievers_remote/classes/RemoteRetriever#lc_serializable)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L55)

### metadataKey[​](#metadatakey "Direct link to metadataKey")

> **metadataKey**: `string`

The key in the JSON response to get the metadata from

#### Implementation of[​](#implementation-of-2 "Direct link to Implementation of")

[RemoteLangChainRetrieverParams](/docs/api/retrievers_remote/interfaces/RemoteLangChainRetrieverParams).[metadataKey](/docs/api/retrievers_remote/interfaces/RemoteLangChainRetrieverParams#metadatakey)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/retrievers/remote/remote-retriever.ts:39](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/remote/remote-retriever.ts#L39)

### pageContentKey[​](#pagecontentkey "Direct link to pageContentKey")

> **pageContentKey**: `string`

The key in the JSON response to get the page content from

#### Implementation of[​](#implementation-of-3 "Direct link to Implementation of")

[RemoteLangChainRetrieverParams](/docs/api/retrievers_remote/interfaces/RemoteLangChainRetrieverParams).[pageContentKey](/docs/api/retrievers_remote/interfaces/RemoteLangChainRetrieverParams#pagecontentkey)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/retrievers/remote/remote-retriever.ts:37](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/remote/remote-retriever.ts#L37)

### responseKey[​](#responsekey "Direct link to responseKey")

> **responseKey**: `string`

The key in the JSON response to get the response from

#### Implementation of[​](#implementation-of-4 "Direct link to Implementation of")

[RemoteLangChainRetrieverParams](/docs/api/retrievers_remote/interfaces/RemoteLangChainRetrieverParams).[responseKey](/docs/api/retrievers_remote/interfaces/RemoteLangChainRetrieverParams#responsekey)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/retrievers/remote/remote-retriever.ts:35](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/remote/remote-retriever.ts#L35)

### url[​](#url "Direct link to url")

> **url**: `string`

The URL of the remote retriever server

#### Implementation of[​](#implementation-of-5 "Direct link to Implementation of")

[RemoteLangChainRetrieverParams](/docs/api/retrievers_remote/interfaces/RemoteLangChainRetrieverParams).[url](/docs/api/retrievers_remote/interfaces/RemoteLangChainRetrieverParams#url)

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[url](/docs/api/retrievers_remote/classes/RemoteRetriever#url)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/retrievers/remote/base.ts:35](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/remote/base.ts#L35)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Implementation of[​](#implementation-of-6 "Direct link to Implementation of")

[RemoteLangChainRetrieverParams](/docs/api/retrievers_remote/interfaces/RemoteLangChainRetrieverParams).[callbacks](/docs/api/retrievers_remote/interfaces/RemoteLangChainRetrieverParams#callbacks)

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[callbacks](/docs/api/retrievers_remote/classes/RemoteRetriever#callbacks)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L23)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Implementation of[​](#implementation-of-7 "Direct link to Implementation of")

[RemoteLangChainRetrieverParams](/docs/api/retrievers_remote/interfaces/RemoteLangChainRetrieverParams).[metadata](/docs/api/retrievers_remote/interfaces/RemoteLangChainRetrieverParams#metadata)

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[metadata](/docs/api/retrievers_remote/classes/RemoteRetriever#metadata)

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:27](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L27)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Implementation of[​](#implementation-of-8 "Direct link to Implementation of")

[RemoteLangChainRetrieverParams](/docs/api/retrievers_remote/interfaces/RemoteLangChainRetrieverParams).[tags](/docs/api/retrievers_remote/interfaces/RemoteLangChainRetrieverParams#tags)

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[tags](/docs/api/retrievers_remote/classes/RemoteRetriever#tags)

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:25](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L25)

### verbose?[​](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Implementation of[​](#implementation-of-9 "Direct link to Implementation of")

[RemoteLangChainRetrieverParams](/docs/api/retrievers_remote/interfaces/RemoteLangChainRetrieverParams).[verbose](/docs/api/retrievers_remote/interfaces/RemoteLangChainRetrieverParams#verbose)

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[verbose](/docs/api/retrievers_remote/classes/RemoteRetriever#verbose)

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:29](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L29)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-1 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

RemoteRetriever.lc\_aliases

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[lc\_aliases](/docs/api/retrievers_remote/classes/RemoteRetriever#lc_aliases)

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

RemoteRetriever.lc\_attributes

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[lc\_attributes](/docs/api/retrievers_remote/classes/RemoteRetriever#lc_attributes)

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

RemoteRetriever.lc\_secrets

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/retrievers/remote/base.ts:29](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/remote/base.ts#L29)

#### Inherited from[​](#inherited-from-15 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[lc\_secrets](/docs/api/retrievers_remote/classes/RemoteRetriever#lc_secrets)

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/retrievers/remote/base.ts:29](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/remote/base.ts#L29)

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

#### Inherited from[​](#inherited-from-16 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[\_getRelevantDocuments](/docs/api/retrievers_remote/classes/RemoteRetriever#_getrelevantdocuments)

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/retrievers/remote/base.ts:62](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/remote/base.ts#L62)

### createJsonBody()[​](#createjsonbody "Direct link to createJsonBody()")

> **createJsonBody**(`query`: `string`): [`RemoteRetrieverValues`](/docs/api/retrievers_remote/types/RemoteRetrieverValues)

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`query`

`string`

#### Returns[​](#returns-5 "Direct link to Returns")

[`RemoteRetrieverValues`](/docs/api/retrievers_remote/types/RemoteRetrieverValues)

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[createJsonBody](/docs/api/retrievers_remote/classes/RemoteRetriever#createjsonbody)

#### Defined in[​](#defined-in-23 "Direct link to Defined in")

[langchain/src/retrievers/remote/remote-retriever.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/remote/remote-retriever.ts#L55)

### getRelevantDocuments()[​](#getrelevantdocuments "Direct link to getRelevantDocuments()")

> **getRelevantDocuments**(`query`: `string`, `config`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`query`

`string`

`config?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`

#### Returns[​](#returns-6 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Inherited from[​](#inherited-from-17 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[getRelevantDocuments](/docs/api/retrievers_remote/classes/RemoteRetriever#getrelevantdocuments)

#### Defined in[​](#defined-in-24 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:51](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L51)

### processJsonResponse()[​](#processjsonresponse "Direct link to processJsonResponse()")

> **processJsonResponse**(`json`: [`RemoteRetrieverValues`](/docs/api/retrievers_remote/types/RemoteRetrieverValues)): [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`json`

[`RemoteRetrieverValues`](/docs/api/retrievers_remote/types/RemoteRetrieverValues)

#### Returns[​](#returns-7 "Direct link to Returns")

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

#### Overrides[​](#overrides-3 "Direct link to Overrides")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[processJsonResponse](/docs/api/retrievers_remote/classes/RemoteRetriever#processjsonresponse)

#### Defined in[​](#defined-in-25 "Direct link to Defined in")

[langchain/src/retrievers/remote/remote-retriever.ts:61](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/remote/remote-retriever.ts#L61)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-8 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-18 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[toJSON](/docs/api/retrievers_remote/classes/RemoteRetriever#tojson)

#### Defined in[​](#defined-in-26 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-9 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-19 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[toJSONNotImplemented](/docs/api/retrievers_remote/classes/RemoteRetriever#tojsonnotimplemented)

#### Defined in[​](#defined-in-27 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)