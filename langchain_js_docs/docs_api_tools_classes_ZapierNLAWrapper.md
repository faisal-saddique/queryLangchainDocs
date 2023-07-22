ZapierNLAWrapper
================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`Serializable`](/docs/api/load_serializable/classes/Serializable).**ZapierNLAWrapper**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new ZapierNLAWrapper**(`params`?: [`ZapierNLAWrapperParams`](/docs/api/tools/interfaces/ZapierNLAWrapperParams)): [`ZapierNLAWrapper`](/docs/api/tools/classes/ZapierNLAWrapper)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`params?`

[`ZapierNLAWrapperParams`](/docs/api/tools/interfaces/ZapierNLAWrapperParams)

#### Returns[​](#returns "Direct link to Returns")

[`ZapierNLAWrapper`](/docs/api/tools/classes/ZapierNLAWrapper)

#### Overrides[​](#overrides "Direct link to Overrides")

[Serializable](/docs/api/load_serializable/classes/Serializable).[constructor](/docs/api/load_serializable/classes/Serializable#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/tools/zapier.ts:54](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/zapier.ts#L54)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### caller[​](#caller "Direct link to caller")

> **caller**: `AsyncCaller`

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/tools/zapier.ts:52](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/zapier.ts#L52)

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[Serializable](/docs/api/load_serializable/classes/Serializable).[lc\_kwargs](/docs/api/load_serializable/classes/Serializable#lc_kwargs)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[Serializable](/docs/api/load_serializable/classes/Serializable).[lc\_namespace](/docs/api/load_serializable/classes/Serializable#lc_namespace)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/tools/zapier.ts:38](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/zapier.ts#L38)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[Serializable](/docs/api/load_serializable/classes/Serializable).[lc\_serializable](/docs/api/load_serializable/classes/Serializable#lc_serializable)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L55)

### zapierNlaApiBase[​](#zapiernlaapibase "Direct link to zapierNlaApiBase")

> **zapierNlaApiBase**: `string` = `"https://nla.zapier.com/api/v1/"`

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/tools/zapier.ts:50](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/zapier.ts#L50)

### zapierNlaApiKey?[​](#zapiernlaapikey "Direct link to zapierNlaApiKey?")

> **zapierNlaApiKey**: `string`

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/tools/zapier.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/zapier.ts#L46)

### zapierNlaOAuthAccessToken?[​](#zapiernlaoauthaccesstoken "Direct link to zapierNlaOAuthAccessToken?")

> **zapierNlaOAuthAccessToken**: `string`

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/tools/zapier.ts:48](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/zapier.ts#L48)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-1 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

Serializable.lc\_aliases

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[Serializable](/docs/api/load_serializable/classes/Serializable).[lc\_aliases](/docs/api/load_serializable/classes/Serializable#lc_aliases)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

Serializable.lc\_attributes

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[Serializable](/docs/api/load_serializable/classes/Serializable).[lc\_attributes](/docs/api/load_serializable/classes/Serializable#lc_attributes)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Overrides[​](#overrides-2 "Direct link to Overrides")

Serializable.lc\_secrets

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/tools/zapier.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/zapier.ts#L40)

#### Overrides[​](#overrides-3 "Direct link to Overrides")

[Serializable](/docs/api/load_serializable/classes/Serializable).[lc\_secrets](/docs/api/load_serializable/classes/Serializable#lc_secrets)

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/tools/zapier.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/zapier.ts#L40)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### listActions()[​](#listactions "Direct link to listActions()")

Returns a list of all exposed (enabled) actions associated with current user (associated with the set api\_key or access token).

> **listActions**(): `Promise`<`ZapierValues`\[\]\>

#### Returns[​](#returns-4 "Direct link to Returns")

`Promise`<`ZapierValues`\[\]\>

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/tools/zapier.ts:176](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/zapier.ts#L176)

### listActionsAsString()[​](#listactionsasstring "Direct link to listActionsAsString()")

Same as list, but returns a stringified version of the result.

> **listActionsAsString**(): `Promise`<`string`\>

#### Returns[​](#returns-5 "Direct link to Returns")

`Promise`<`string`\>

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/tools/zapier.ts:235](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/zapier.ts#L235)

### previewAction()[​](#previewaction "Direct link to previewAction()")

Same as run, but instead of actually executing the action, will instead return a preview of params that have been guessed by the AI in case you need to explicitly review before executing.

> **previewAction**(`actionId`: `string`, `instructions`: `string`, `params`?: `ZapierValues`): `Promise`<`ZapierValues`\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`actionId`

`string`

`instructions`

`string`

`params?`

`ZapierValues`

#### Returns[​](#returns-6 "Direct link to Returns")

`Promise`<`ZapierValues`\>

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/tools/zapier.ts:161](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/zapier.ts#L161)

### previewAsString()[​](#previewasstring "Direct link to previewAsString()")

Same as preview, but returns a stringified version of the result.

> **previewAsString**(`actionId`: `string`, `instructions`: `string`, `params`?: `ZapierValues`): `Promise`<`string`\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`actionId`

`string`

`instructions`

`string`

`params?`

`ZapierValues`

#### Returns[​](#returns-7 "Direct link to Returns")

`Promise`<`string`\>

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/tools/zapier.ts:223](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/zapier.ts#L223)

### runAction()[​](#runaction "Direct link to runAction()")

Executes an action that is identified by action\_id, must be exposed (enabled) by the current user (associated with the set api\_key or access token).

> **runAction**(`actionId`: `string`, `instructions`: `string`, `params`?: `ZapierValues`): `Promise`<`ZapierValues`\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`actionId`

`string`

`instructions`

`string`

`params?`

`ZapierValues`

#### Returns[​](#returns-8 "Direct link to Returns")

`Promise`<`ZapierValues`\>

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/tools/zapier.ts:144](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/zapier.ts#L144)

### runAsString()[​](#runasstring "Direct link to runAsString()")

Same as run, but returns a stringified version of the result.

> **runAsString**(`actionId`: `string`, `instructions`: `string`, `params`?: `ZapierValues`): `Promise`<`string`\>

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`actionId`

`string`

`instructions`

`string`

`params?`

`ZapierValues`

#### Returns[​](#returns-9 "Direct link to Returns")

`Promise`<`string`\>

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/tools/zapier.ts:208](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/zapier.ts#L208)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-10 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[Serializable](/docs/api/load_serializable/classes/Serializable).[toJSON](/docs/api/load_serializable/classes/Serializable#tojson)

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-11 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

[Serializable](/docs/api/load_serializable/classes/Serializable).[toJSONNotImplemented](/docs/api/load_serializable/classes/Serializable#tojsonnotimplemented)

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)

### \_getActionRequest()[​](#_getactionrequest "Direct link to _getactionrequest")

> `Protected` **\_getActionRequest**(`actionId`: `string`, `instructions`: `string`, `params`?: `ZapierValues`): `Promise`<`ZapierValues`\>

#### Parameters[​](#parameters-5 "Direct link to Parameters")

Parameter

Type

`actionId`

`string`

`instructions`

`string`

`params?`

`ZapierValues`

#### Returns[​](#returns-12 "Direct link to Returns")

`Promise`<`ZapierValues`\>

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/tools/zapier.ts:102](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/zapier.ts#L102)

### \_getHeaders()[​](#_getheaders "Direct link to _getheaders")

> `Protected` **\_getHeaders**(): `Record`<`string`, `string`\>

#### Returns[​](#returns-13 "Direct link to Returns")

`Record`<`string`, `string`\>

#### Defined in[​](#defined-in-23 "Direct link to Defined in")

[langchain/src/tools/zapier.ts:82](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/zapier.ts#L82)