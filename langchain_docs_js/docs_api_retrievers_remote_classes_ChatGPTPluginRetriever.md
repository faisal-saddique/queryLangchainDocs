ChatGPTPluginRetriever
======================

Base Index class. All indexes should extend this class.

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`RemoteRetriever`](/docs/api/retrievers_remote/classes/RemoteRetriever).**ChatGPTPluginRetriever**

Implements[](#implements "Direct link to Implements")
------------------------------------------------------

*   [`ChatGPTPluginRetrieverParams`](/docs/api/retrievers_remote/interfaces/ChatGPTPluginRetrieverParams)

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new ChatGPTPluginRetriever**(«destructured»: [`ChatGPTPluginRetrieverParams`](/docs/api/retrievers_remote/interfaces/ChatGPTPluginRetrieverParams)): [`ChatGPTPluginRetriever`](/docs/api/retrievers_remote/classes/ChatGPTPluginRetriever)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`«destructured»`

[`ChatGPTPluginRetrieverParams`](/docs/api/retrievers_remote/interfaces/ChatGPTPluginRetrieverParams)

#### Returns[](#returns "Direct link to Returns")

[`ChatGPTPluginRetriever`](/docs/api/retrievers_remote/classes/ChatGPTPluginRetriever)

#### Overrides[](#overrides "Direct link to Overrides")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[constructor](/docs/api/retrievers_remote/classes/RemoteRetriever#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/retrievers/remote/chatgpt-plugin.ts:39](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/remote/chatgpt-plugin.ts#L39)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### asyncCaller[](#asynccaller "Direct link to asyncCaller")

> **asyncCaller**: `AsyncCaller`

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[asyncCaller](/docs/api/retrievers_remote/classes/RemoteRetriever#asynccaller)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/retrievers/remote/base.ts:41](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/remote/base.ts#L41)

### auth[](#auth "Direct link to auth")

> **auth**: [`RemoteRetrieverAuth`](/docs/api/retrievers_remote/types/RemoteRetrieverAuth)

The authentication method to use, currently implemented is

*   false: no authentication
*   { bearer: string }: Bearer token authentication

#### Implementation of[](#implementation-of "Direct link to Implementation of")

[ChatGPTPluginRetrieverParams](/docs/api/retrievers_remote/interfaces/ChatGPTPluginRetrieverParams).[auth](/docs/api/retrievers_remote/interfaces/ChatGPTPluginRetrieverParams#auth)

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[auth](/docs/api/retrievers_remote/classes/RemoteRetriever#auth)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/retrievers/remote/base.ts:37](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/remote/base.ts#L37)

### headers[](#headers "Direct link to headers")

> **headers**: `Record`<`string`, `string`\>

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[headers](/docs/api/retrievers_remote/classes/RemoteRetriever#headers)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/retrievers/remote/base.ts:39](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/remote/base.ts#L39)

### lc\_kwargs[](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[lc\_kwargs](/docs/api/retrievers_remote/classes/RemoteRetriever#lc_kwargs)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L57)

### lc\_namespace[](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Overrides[](#overrides-1 "Direct link to Overrides")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[lc\_namespace](/docs/api/retrievers_remote/classes/RemoteRetriever#lc_namespace)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/retrievers/remote/chatgpt-plugin.ts:33](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/remote/chatgpt-plugin.ts#L33)

### lc\_serializable[](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[lc\_serializable](/docs/api/retrievers_remote/classes/RemoteRetriever#lc_serializable)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L55)

### topK[](#topk "Direct link to topK")

> **topK**: `number`

The number of results to request from the ChatGPTRetrievalPlugin server

#### Implementation of[](#implementation-of-1 "Direct link to Implementation of")

[ChatGPTPluginRetrieverParams](/docs/api/retrievers_remote/interfaces/ChatGPTPluginRetrieverParams).[topK](/docs/api/retrievers_remote/interfaces/ChatGPTPluginRetrieverParams#topk)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/retrievers/remote/chatgpt-plugin.ts:35](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/remote/chatgpt-plugin.ts#L35)

### url[](#url "Direct link to url")

> **url**: `string`

The URL of the remote retriever server

#### Implementation of[](#implementation-of-2 "Direct link to Implementation of")

[ChatGPTPluginRetrieverParams](/docs/api/retrievers_remote/interfaces/ChatGPTPluginRetrieverParams).[url](/docs/api/retrievers_remote/interfaces/ChatGPTPluginRetrieverParams#url)

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[url](/docs/api/retrievers_remote/classes/RemoteRetriever#url)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/retrievers/remote/base.ts:35](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/remote/base.ts#L35)

### callbacks?[](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Implementation of[](#implementation-of-3 "Direct link to Implementation of")

[ChatGPTPluginRetrieverParams](/docs/api/retrievers_remote/interfaces/ChatGPTPluginRetrieverParams).[callbacks](/docs/api/retrievers_remote/interfaces/ChatGPTPluginRetrieverParams#callbacks)

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[callbacks](/docs/api/retrievers_remote/classes/RemoteRetriever#callbacks)

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:23](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/retriever.ts#L23)

### filter?[](#filter "Direct link to filter?")

> **filter**: [`ChatGPTPluginRetrieverFilter`](/docs/api/retrievers_remote/interfaces/ChatGPTPluginRetrieverFilter)

The filter to use when querying the ChatGPTRetrievalPlugin server

#### Implementation of[](#implementation-of-4 "Direct link to Implementation of")

[ChatGPTPluginRetrieverParams](/docs/api/retrievers_remote/interfaces/ChatGPTPluginRetrieverParams).[filter](/docs/api/retrievers_remote/interfaces/ChatGPTPluginRetrieverParams#filter)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/retrievers/remote/chatgpt-plugin.ts:37](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/remote/chatgpt-plugin.ts#L37)

### metadata?[](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Implementation of[](#implementation-of-5 "Direct link to Implementation of")

[ChatGPTPluginRetrieverParams](/docs/api/retrievers_remote/interfaces/ChatGPTPluginRetrieverParams).[metadata](/docs/api/retrievers_remote/interfaces/ChatGPTPluginRetrieverParams#metadata)

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[metadata](/docs/api/retrievers_remote/classes/RemoteRetriever#metadata)

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:27](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/retriever.ts#L27)

### tags?[](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Implementation of[](#implementation-of-6 "Direct link to Implementation of")

[ChatGPTPluginRetrieverParams](/docs/api/retrievers_remote/interfaces/ChatGPTPluginRetrieverParams).[tags](/docs/api/retrievers_remote/interfaces/ChatGPTPluginRetrieverParams#tags)

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[tags](/docs/api/retrievers_remote/classes/RemoteRetriever#tags)

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:25](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/retriever.ts#L25)

### verbose?[](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Implementation of[](#implementation-of-7 "Direct link to Implementation of")

[ChatGPTPluginRetrieverParams](/docs/api/retrievers_remote/interfaces/ChatGPTPluginRetrieverParams).[verbose](/docs/api/retrievers_remote/interfaces/ChatGPTPluginRetrieverParams#verbose)

#### Inherited from[](#inherited-from-9 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[verbose](/docs/api/retrievers_remote/classes/RemoteRetriever#verbose)

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:29](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/retriever.ts#L29)

### lc\_runnable[](#lc_runnable "Direct link to lc_runnable")

> `Protected` **lc\_runnable**: `boolean` = `true`

#### Inherited from[](#inherited-from-10 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[lc\_runnable](/docs/api/retrievers_remote/classes/RemoteRetriever#lc_runnable)

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:34](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L34)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[](#returns-1 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-11 "Direct link to Inherited from")

RemoteRetriever.lc\_aliases

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

#### Inherited from[](#inherited-from-12 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[lc\_aliases](/docs/api/retrievers_remote/classes/RemoteRetriever#lc_aliases)

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

### lc\_attributes[](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[](#returns-2 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[](#inherited-from-13 "Direct link to Inherited from")

RemoteRetriever.lc\_attributes

#### Defined in[](#defined-in-17 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L80)

#### Inherited from[](#inherited-from-14 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[lc\_attributes](/docs/api/retrievers_remote/classes/RemoteRetriever#lc_attributes)

#### Defined in[](#defined-in-18 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L80)

### lc\_secrets[](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-15 "Direct link to Inherited from")

RemoteRetriever.lc\_secrets

#### Defined in[](#defined-in-19 "Direct link to Defined in")

[langchain/src/retrievers/remote/base.ts:29](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/remote/base.ts#L29)

#### Inherited from[](#inherited-from-16 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[lc\_secrets](/docs/api/retrievers_remote/classes/RemoteRetriever#lc_secrets)

#### Defined in[](#defined-in-20 "Direct link to Defined in")

[langchain/src/retrievers/remote/base.ts:29](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/remote/base.ts#L29)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### \_getRelevantDocuments()[](#_getrelevantdocuments "Direct link to _getrelevantdocuments")

TODO: This should be an abstract method, but we'd like to avoid breaking changes to people currently using subclassed custom retrievers. Change it on next major release.

> **\_getRelevantDocuments**(`query`: `string`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`query`

`string`

#### Returns[](#returns-4 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Inherited from[](#inherited-from-17 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[\_getRelevantDocuments](/docs/api/retrievers_remote/classes/RemoteRetriever#_getrelevantdocuments)

#### Defined in[](#defined-in-21 "Direct link to Defined in")

[langchain/src/retrievers/remote/base.ts:62](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/remote/base.ts#L62)

### \_patchConfig()[](#_patchconfig "Direct link to _patchconfig")

> **\_patchConfig**(`config`: `Partial`<`BaseCallbackConfig`\> = `{}`, `callbackManager`: `undefined` | [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager) = `undefined`): `Partial`<`BaseCallbackConfig`\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

Default value

`config`

`Partial`<`BaseCallbackConfig`\>

`{}`

`callbackManager`

`undefined` | [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

`undefined`

#### Returns[](#returns-5 "Direct link to Returns")

`Partial`<`BaseCallbackConfig`\>

#### Inherited from[](#inherited-from-18 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[\_patchConfig](/docs/api/retrievers_remote/classes/RemoteRetriever#_patchconfig)

#### Defined in[](#defined-in-22 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:146](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L146)

### \_streamIterator()[](#_streamiterator "Direct link to _streamiterator")

> **\_streamIterator**(`input`: `string`, `options`?: `Partial`<`BaseCallbackConfig`\>): `AsyncGenerator`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], `any`, `unknown`\>

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

`input`

`string`

`options?`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-6 "Direct link to Returns")

`AsyncGenerator`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], `any`, `unknown`\>

#### Inherited from[](#inherited-from-19 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[\_streamIterator](/docs/api/retrievers_remote/classes/RemoteRetriever#_streamiterator)

#### Defined in[](#defined-in-23 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:86](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L86)

### batch()[](#batch "Direct link to batch()")

> **batch**(`inputs`: `string`\[\], `options`?: `Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\], `batchOptions`?: `object`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\[\]\>

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

`inputs`

`string`\[\]

`options?`

`Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\]

`batchOptions?`

`object`

`batchOptions.maxConcurrency?`

`number`

#### Returns[](#returns-7 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\[\]\>

#### Inherited from[](#inherited-from-20 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[batch](/docs/api/retrievers_remote/classes/RemoteRetriever#batch)

#### Defined in[](#defined-in-24 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:63](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L63)

### bind()[](#bind "Direct link to bind()")

> **bind**(`kwargs`: `Partial`<`BaseCallbackConfig`\>): [`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<`string`, [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], `BaseCallbackConfig`\>

#### Parameters[](#parameters-5 "Direct link to Parameters")

Parameter

Type

`kwargs`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-8 "Direct link to Returns")

[`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<`string`, [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], `BaseCallbackConfig`\>

#### Inherited from[](#inherited-from-21 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[bind](/docs/api/retrievers_remote/classes/RemoteRetriever#bind)

#### Defined in[](#defined-in-25 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:41](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L41)

### createJsonBody()[](#createjsonbody "Direct link to createJsonBody()")

> **createJsonBody**(`query`: `string`): [`RemoteRetrieverValues`](/docs/api/retrievers_remote/types/RemoteRetrieverValues)

#### Parameters[](#parameters-6 "Direct link to Parameters")

Parameter

Type

`query`

`string`

#### Returns[](#returns-9 "Direct link to Returns")

[`RemoteRetrieverValues`](/docs/api/retrievers_remote/types/RemoteRetrieverValues)

#### Overrides[](#overrides-2 "Direct link to Overrides")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[createJsonBody](/docs/api/retrievers_remote/classes/RemoteRetriever#createjsonbody)

#### Defined in[](#defined-in-26 "Direct link to Defined in")

[langchain/src/retrievers/remote/chatgpt-plugin.ts:45](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/remote/chatgpt-plugin.ts#L45)

### getRelevantDocuments()[](#getrelevantdocuments "Direct link to getRelevantDocuments()")

> **getRelevantDocuments**(`query`: `string`, `config`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[](#parameters-7 "Direct link to Parameters")

Parameter

Type

`query`

`string`

`config?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`

#### Returns[](#returns-10 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Inherited from[](#inherited-from-22 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[getRelevantDocuments](/docs/api/retrievers_remote/classes/RemoteRetriever#getrelevantdocuments)

#### Defined in[](#defined-in-27 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:55](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/retriever.ts#L55)

### invoke()[](#invoke "Direct link to invoke()")

> **invoke**(`input`: `string`, `options`?: `BaseCallbackConfig`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[](#parameters-8 "Direct link to Parameters")

Parameter

Type

`input`

`string`

`options?`

`BaseCallbackConfig`

#### Returns[](#returns-11 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Inherited from[](#inherited-from-23 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[invoke](/docs/api/retrievers_remote/classes/RemoteRetriever#invoke)

#### Defined in[](#defined-in-28 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:51](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/retriever.ts#L51)

### pipe()[](#pipe "Direct link to pipe()")

> **pipe**<NewRunOutput\>(`coerceable`: [`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], `NewRunOutput`\>): [`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<`string`, `NewRunOutput`\>

#### Type parameters[](#type-parameters "Direct link to Type parameters")

*   `NewRunOutput`

#### Parameters[](#parameters-9 "Direct link to Parameters")

Parameter

Type

`coerceable`

[`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], `NewRunOutput`\>

#### Returns[](#returns-12 "Direct link to Returns")

[`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<`string`, `NewRunOutput`\>

#### Inherited from[](#inherited-from-24 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[pipe](/docs/api/retrievers_remote/classes/RemoteRetriever#pipe)

#### Defined in[](#defined-in-29 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:153](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L153)

### processJsonResponse()[](#processjsonresponse "Direct link to processJsonResponse()")

> **processJsonResponse**(`json`: [`RemoteRetrieverValues`](/docs/api/retrievers_remote/types/RemoteRetrieverValues)): [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

#### Parameters[](#parameters-10 "Direct link to Parameters")

Parameter

Type

`json`

[`RemoteRetrieverValues`](/docs/api/retrievers_remote/types/RemoteRetrieverValues)

#### Returns[](#returns-13 "Direct link to Returns")

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

#### Overrides[](#overrides-3 "Direct link to Overrides")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[processJsonResponse](/docs/api/retrievers_remote/classes/RemoteRetriever#processjsonresponse)

#### Defined in[](#defined-in-30 "Direct link to Defined in")

[langchain/src/retrievers/remote/chatgpt-plugin.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/remote/chatgpt-plugin.ts#L57)

### stream()[](#stream "Direct link to stream()")

> **stream**(`input`: `string`, `options`?: `Partial`<`BaseCallbackConfig`\>): `Promise`<`IterableReadableStream`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>\>

#### Parameters[](#parameters-11 "Direct link to Parameters")

Parameter

Type

`input`

`string`

`options?`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-14 "Direct link to Returns")

`Promise`<`IterableReadableStream`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>\>

#### Inherited from[](#inherited-from-25 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[stream](/docs/api/retrievers_remote/classes/RemoteRetriever#stream)

#### Defined in[](#defined-in-31 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:93](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L93)

### toJSON()[](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[](#returns-15 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[](#inherited-from-26 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[toJSON](/docs/api/retrievers_remote/classes/RemoteRetriever#tojson)

#### Defined in[](#defined-in-32 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[](#returns-16 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[](#inherited-from-27 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[toJSONNotImplemented](/docs/api/retrievers_remote/classes/RemoteRetriever#tojsonnotimplemented)

#### Defined in[](#defined-in-33 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L151)

### isRunnable()[](#isrunnable "Direct link to isRunnable()")

> `Static` **isRunnable**(`thing`: `any`): thing is Runnable<any, any, BaseCallbackConfig\>

#### Parameters[](#parameters-12 "Direct link to Parameters")

Parameter

Type

`thing`

`any`

#### Returns[](#returns-17 "Direct link to Returns")

thing is Runnable<any, any, BaseCallbackConfig\>

#### Inherited from[](#inherited-from-28 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[isRunnable](/docs/api/retrievers_remote/classes/RemoteRetriever#isrunnable)

#### Defined in[](#defined-in-34 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:164](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L164)

### \_callWithConfig()[](#_callwithconfig "Direct link to _callwithconfig")

> `Protected` **\_callWithConfig**<T\>(`func`: `Function`, `input`: `T`, `options`?: `BaseCallbackConfig` & {`runType`?: `string`;}): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Type parameters[](#type-parameters-1 "Direct link to Type parameters")

*   `T` _extends_ `string`

#### Parameters[](#parameters-13 "Direct link to Parameters")

Parameter

Type

`func`

(`input`: `T`) => `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

`input`

`T`

`options?`

`BaseCallbackConfig` & {`runType`?: `string`;}

#### Returns[](#returns-18 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Inherited from[](#inherited-from-29 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[\_callWithConfig](/docs/api/retrievers_remote/classes/RemoteRetriever#_callwithconfig)

#### Defined in[](#defined-in-35 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:117](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L117)

### \_getOptionsList()[](#_getoptionslist "Direct link to _getoptionslist")

> `Protected` **\_getOptionsList**(`options`: `Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\], `length`: `number` = `0`): `Partial`<`BaseCallbackConfig`\>\[\]

#### Parameters[](#parameters-14 "Direct link to Parameters")

Parameter

Type

Default value

`options`

`Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\]

`undefined`

`length`

`number`

`0`

#### Returns[](#returns-19 "Direct link to Returns")

`Partial`<`BaseCallbackConfig`\>\[\]

#### Inherited from[](#inherited-from-30 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[\_getOptionsList](/docs/api/retrievers_remote/classes/RemoteRetriever#_getoptionslist)

#### Defined in[](#defined-in-36 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L48)

### \_separateRunnableConfigFromCallOptions()[](#_separaterunnableconfigfromcalloptions "Direct link to _separaterunnableconfigfromcalloptions")

> `Protected` **\_separateRunnableConfigFromCallOptions**(`options`: `Partial`<`BaseCallbackConfig`\> = `{}`): \[`BaseCallbackConfig`, `Omit`<`Partial`<`BaseCallbackConfig`\>, _keyof_ `BaseCallbackConfig`\>\]

#### Parameters[](#parameters-15 "Direct link to Parameters")

Parameter

Type

`options`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-20 "Direct link to Returns")

\[`BaseCallbackConfig`, `Omit`<`Partial`<`BaseCallbackConfig`\>, _keyof_ `BaseCallbackConfig`\>\]

#### Inherited from[](#inherited-from-31 "Direct link to Inherited from")

[RemoteRetriever](/docs/api/retrievers_remote/classes/RemoteRetriever).[\_separateRunnableConfigFromCallOptions](/docs/api/retrievers_remote/classes/RemoteRetriever#_separaterunnableconfigfromcalloptions)

#### Defined in[](#defined-in-37 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:102](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L102)