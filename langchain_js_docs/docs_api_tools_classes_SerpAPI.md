SerpAPI
=======

Wrapper around SerpAPI.

To use, you should have the `serpapi` package installed and the SERPAPI\_API\_KEY environment variable set.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`Tool`](/docs/api/tools/classes/Tool).**SerpAPI**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new SerpAPI**(`apiKey`: `undefined` | `string` = `...`, `params`: `Partial`<[`SerpAPIParameters`](/docs/api/tools/interfaces/SerpAPIParameters)\> = `{}`, `baseUrl`: `string` = `"https://serpapi.com"`): [`SerpAPI`](/docs/api/tools/classes/SerpAPI)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

Default value

`apiKey`

`undefined` | `string`

`undefined`

`params`

`Partial`<[`SerpAPIParameters`](/docs/api/tools/interfaces/SerpAPIParameters)\>

`{}`

`baseUrl`

`string`

`"https://serpapi.com"`

#### Returns[​](#returns "Direct link to Returns")

[`SerpAPI`](/docs/api/tools/classes/SerpAPI)

#### Overrides[​](#overrides "Direct link to Overrides")

[Tool](/docs/api/tools/classes/Tool).[constructor](/docs/api/tools/classes/Tool#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:303](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/serpapi.ts#L303)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### description[​](#description "Direct link to description")

> **description**: `string` = `"a search engine. useful for when you need to answer questions about current events. input should be a search query."`

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[Tool](/docs/api/tools/classes/Tool).[description](/docs/api/tools/classes/Tool#description)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:386](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/serpapi.ts#L386)

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

> **name**: `string` = `"search"`

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[Tool](/docs/api/tools/classes/Tool).[name](/docs/api/tools/classes/Tool#name)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:321](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/serpapi.ts#L321)

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

### baseUrl[​](#baseurl "Direct link to baseUrl")

> `Protected` **baseUrl**: `string`

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:301](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/serpapi.ts#L301)

### key[​](#key "Direct link to key")

> `Protected` **key**: `string`

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:297](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/serpapi.ts#L297)

### params[​](#params "Direct link to params")

> `Protected` **params**: `Partial`<[`SerpAPIParameters`](/docs/api/tools/interfaces/SerpAPIParameters)\>

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:299](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/serpapi.ts#L299)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-1 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

Tool.lc\_aliases

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[lc\_aliases](/docs/api/tools/classes/Tool#lc_aliases)

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

Tool.lc\_attributes

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[lc\_attributes](/docs/api/tools/classes/Tool#lc_attributes)

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

> **lc\_namespace**(): `string`\[\]

#### Returns[​](#returns-3 "Direct link to Returns")

`string`\[\]

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

Tool.lc\_namespace

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/tools/base.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/base.ts#L22)

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[lc\_namespace](/docs/api/tools/classes/Tool#lc_namespace)

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/tools/base.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/base.ts#L22)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-4 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

Tool.lc\_secrets

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-15 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[lc\_secrets](/docs/api/tools/classes/Tool#lc_secrets)

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### call()[​](#call "Direct link to call()")

> **call**(`arg`: `undefined` | `string` | {`input`?: `string`;}, `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`arg`

`undefined` | `string` | {`input`?: `string`;}

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-5 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[​](#inherited-from-16 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[call](/docs/api/tools/classes/Tool#call)

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/tools/base.ts:86](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/base.ts#L86)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-6 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Overrides[​](#overrides-3 "Direct link to Overrides")

[Tool](/docs/api/tools/classes/Tool).[toJSON](/docs/api/tools/classes/Tool#tojson)

#### Defined in[​](#defined-in-23 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:293](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/serpapi.ts#L293)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-7 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-17 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[toJSONNotImplemented](/docs/api/tools/classes/Tool#tojsonnotimplemented)

#### Defined in[​](#defined-in-24 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)

### buildUrl()[​](#buildurl "Direct link to buildUrl()")

> `Protected` **buildUrl**<P\>(`path`: `string`, `parameters`: `P`, `baseUrl`: `string`): `string`

#### Type parameters[​](#type-parameters "Direct link to Type parameters")

*   `P` _extends_ `UrlParameters`

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`path`

`string`

`parameters`

`P`

`baseUrl`

`string`

#### Returns[​](#returns-8 "Direct link to Returns")

`string`

#### Defined in[​](#defined-in-25 "Direct link to Defined in")

[langchain/src/tools/serpapi.ts:323](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/serpapi.ts#L323)