DataForSeoAPISearch
===================

Description[​](#description "Direct link to Description")
---------------------------------------------------------

Represents a wrapper class to work with DataForSEO SERP API.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`Tool`](/docs/api/tools/classes/Tool).**DataForSeoAPISearch**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

#### Description[​](#description-1 "Direct link to Description")

Sets up the class, throws an error if the API login/password isn't provided.

> **new DataForSeoAPISearch**(`config`: [`DataForSeoApiConfig`](/docs/api/tools/interfaces/DataForSeoApiConfig) = `{}`): [`DataForSeoAPISearch`](/docs/api/tools/classes/DataForSeoAPISearch)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`config`

[`DataForSeoApiConfig`](/docs/api/tools/interfaces/DataForSeoApiConfig)

#### Returns[​](#returns "Direct link to Returns")

[`DataForSeoAPISearch`](/docs/api/tools/classes/DataForSeoAPISearch)

#### Overrides[​](#overrides "Direct link to Overrides")

[Tool](/docs/api/tools/classes/Tool).[constructor](/docs/api/tools/classes/Tool#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/tools/dataforseo\_api\_search.ts:128](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/dataforseo_api_search.ts#L128)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### description[​](#description-2 "Direct link to description")

> **description**: `string` = `"A robust Google Search API provided by DataForSeo. This tool is handy when you need information about trending topics or current events."`

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[Tool](/docs/api/tools/classes/Tool).[description](/docs/api/tools/classes/Tool#description)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/tools/dataforseo\_api\_search.ts:93](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/dataforseo_api_search.ts#L93)

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[lc\_kwargs](/docs/api/tools/classes/Tool#lc_kwargs)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[lc\_serializable](/docs/api/tools/classes/Tool#lc_serializable)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L55)

### name[​](#name "Direct link to name")

> **name**: `string` = `"dataforseo-api-wrapper"`

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[Tool](/docs/api/tools/classes/Tool).[name](/docs/api/tools/classes/Tool#name)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/tools/dataforseo\_api\_search.ts:91](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/dataforseo_api_search.ts#L91)

### returnDirect[​](#returndirect "Direct link to returnDirect")

> **returnDirect**: `boolean` = `false`

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[returnDirect](/docs/api/tools/classes/Tool#returndirect)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/tools/base.ts:71](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/base.ts#L71)

### schema[​](#schema "Direct link to schema")

> **schema**: `ZodEffects`<`ZodObject`<{`input`: `ZodOptional`<`ZodString`\>;}, "strip", `ZodTypeAny`, {`input`?: `string`;}, {`input`?: `string`;}\>, `undefined` | `string`, {`input`?: `string`;}\>

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[schema](/docs/api/tools/classes/Tool#schema)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/tools/base.ts:78](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/base.ts#L78)

### verbose[​](#verbose "Direct link to verbose")

> **verbose**: `boolean`

Whether to print out response text.

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[verbose](/docs/api/tools/classes/Tool#verbose)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:38](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L38)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[callbacks](/docs/api/tools/classes/Tool#callbacks)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L40)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[metadata](/docs/api/tools/classes/Tool#metadata)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:44](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L44)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[tags](/docs/api/tools/classes/Tool#tags)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L42)

### apiLogin[​](#apilogin "Direct link to apiLogin")

> `Protected` **apiLogin**: `string`

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/tools/dataforseo\_api\_search.ts:96](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/dataforseo_api_search.ts#L96)

### apiPassword[​](#apipassword "Direct link to apiPassword")

> `Protected` **apiPassword**: `string`

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/tools/dataforseo\_api\_search.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/dataforseo_api_search.ts#L98)

### defaultParams[​](#defaultparams "Direct link to defaultParams")

> `Protected` **defaultParams**: `Record`<`string`, `string` | `number` | `boolean`\>

#### Description[​](#description-3 "Direct link to Description")

These are the default parameters to be used when making an API request.

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/tools/dataforseo\_api\_search.ts:105](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/dataforseo_api_search.ts#L105)

### jsonResultFields[​](#jsonresultfields "Direct link to jsonResultFields")

> `Protected` **jsonResultFields**: `undefined` | `string`\[\]

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/tools/dataforseo\_api\_search.ts:117](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/dataforseo_api_search.ts#L117)

### jsonResultTypes[​](#jsonresulttypes "Direct link to jsonResultTypes")

> `Protected` **jsonResultTypes**: `undefined` | `string`\[\]

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/tools/dataforseo\_api\_search.ts:115](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/dataforseo_api_search.ts#L115)

### params[​](#params "Direct link to params")

> `Protected` **params**: `Record`<`string`, `string` | `number` | `boolean`\> = `{}`

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/tools/dataforseo\_api\_search.ts:113](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/dataforseo_api_search.ts#L113)

### topCount[​](#topcount "Direct link to topCount")

> `Protected` **topCount**: `undefined` | `number`

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/tools/dataforseo\_api\_search.ts:119](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/dataforseo_api_search.ts#L119)

### useJsonOutput[​](#usejsonoutput "Direct link to useJsonOutput")

> `Protected` **useJsonOutput**: `boolean` = `false`

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/tools/dataforseo\_api\_search.ts:121](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/dataforseo_api_search.ts#L121)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-1 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

Tool.lc\_aliases

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[lc\_aliases](/docs/api/tools/classes/Tool#lc_aliases)

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

Tool.lc\_attributes

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[lc\_attributes](/docs/api/tools/classes/Tool#lc_attributes)

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

> **lc\_namespace**(): `string`\[\]

#### Returns[​](#returns-3 "Direct link to Returns")

`string`\[\]

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

Tool.lc\_namespace

#### Defined in[​](#defined-in-23 "Direct link to Defined in")

[langchain/src/tools/base.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/base.ts#L22)

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[lc\_namespace](/docs/api/tools/classes/Tool#lc_namespace)

#### Defined in[​](#defined-in-24 "Direct link to Defined in")

[langchain/src/tools/base.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/base.ts#L22)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-4 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

Tool.lc\_secrets

#### Defined in[​](#defined-in-25 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-15 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[lc\_secrets](/docs/api/tools/classes/Tool#lc_secrets)

#### Defined in[​](#defined-in-26 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### \_call()[​](#_call "Direct link to _call")

#### Method[​](#method "Direct link to Method")

\_call

#### Description[​](#description-4 "Direct link to Description")

Initiates a call to the API and processes the response.

> **\_call**(`keyword`: `string`): `Promise`<`string`\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`keyword`

`string`

#### Returns[​](#returns-5 "Direct link to Returns")

`Promise`<`string`\>

#### Overrides[​](#overrides-3 "Direct link to Overrides")

[Tool](/docs/api/tools/classes/Tool).[\_call](/docs/api/tools/classes/Tool#_call)

#### Defined in[​](#defined-in-27 "Direct link to Defined in")

[langchain/src/tools/dataforseo\_api\_search.ts:155](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/dataforseo_api_search.ts#L155)

### call()[​](#call "Direct link to call()")

> **call**(`arg`: `undefined` | `string` | {`input`?: `string`;}, `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`arg`

`undefined` | `string` | {`input`?: `string`;}

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-6 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[​](#inherited-from-16 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[call](/docs/api/tools/classes/Tool#call)

#### Defined in[​](#defined-in-28 "Direct link to Defined in")

[langchain/src/tools/base.ts:86](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/base.ts#L86)

### results()[​](#results "Direct link to results()")

#### Method[​](#method-1 "Direct link to Method")

results

#### Description[​](#description-5 "Direct link to Description")

Fetches the results from the API for the given keyword.

> **results**(`keyword`: `string`): `Promise`<`any`\[\]\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`keyword`

`string`

#### Returns[​](#returns-7 "Direct link to Returns")

`Promise`<`any`\[\]\>

#### Defined in[​](#defined-in-29 "Direct link to Defined in")

[langchain/src/tools/dataforseo\_api\_search.ts:168](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/dataforseo_api_search.ts#L168)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-8 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-17 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[toJSON](/docs/api/tools/classes/Tool#tojson)

#### Defined in[​](#defined-in-30 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-9 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-18 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[toJSONNotImplemented](/docs/api/tools/classes/Tool#tojsonnotimplemented)

#### Defined in[​](#defined-in-31 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)

### getResponseJson()[​](#getresponsejson "Direct link to getResponseJson()")

#### Method[​](#method-2 "Direct link to Method")

getResponseJson

#### Description[​](#description-6 "Direct link to Description")

Executes a POST request to the provided URL and returns a parsed JSON response.

> `Protected` **getResponseJson**(`keyword`: `string`): `Promise`<`ApiResponse`\>

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`keyword`

`string`

#### Returns[​](#returns-10 "Direct link to Returns")

`Promise`<`ApiResponse`\>

#### Defined in[​](#defined-in-32 "Direct link to Defined in")

[langchain/src/tools/dataforseo\_api\_search.ts:214](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/dataforseo_api_search.ts#L214)

### prepareRequest()[​](#preparerequest "Direct link to prepareRequest()")

#### Method[​](#method-3 "Direct link to Method")

prepareRequest

#### Description[​](#description-7 "Direct link to Description")

Prepares the request details for the API call.

> `Protected` **prepareRequest**(`keyword`: `string`): `object`

#### Parameters[​](#parameters-5 "Direct link to Parameters")

Parameter

Type

`keyword`

`string`

#### Returns[​](#returns-11 "Direct link to Returns")

`object`

Member

Type

`data`

`BodyInit`

`headers`

`HeadersInit`

`url`

`string`

#### Defined in[​](#defined-in-33 "Direct link to Defined in")

[langchain/src/tools/dataforseo\_api\_search.ts:179](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/dataforseo_api_search.ts#L179)

### processResponse()[​](#processresponse "Direct link to processResponse()")

#### Method[​](#method-4 "Direct link to Method")

processResponse

#### Description[​](#description-8 "Direct link to Description")

Processes the response to extract meaningful data.

> `Protected` **processResponse**(`res`: `ApiResponse`): `string`

#### Parameters[​](#parameters-6 "Direct link to Parameters")

Parameter

Type

`res`

`ApiResponse`

#### Returns[​](#returns-12 "Direct link to Returns")

`string`

#### Defined in[​](#defined-in-34 "Direct link to Defined in")

[langchain/src/tools/dataforseo\_api\_search.ts:328](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/dataforseo_api_search.ts#L328)