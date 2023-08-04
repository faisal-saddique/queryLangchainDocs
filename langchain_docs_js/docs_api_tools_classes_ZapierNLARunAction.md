ZapierNLARunAction
==================

Base class for Tools that accept input as a string.

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`Tool`](/docs/api/tools/classes/Tool).**ZapierNLARunAction**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new ZapierNLARunAction**(`apiWrapper`: [`ZapierNLAWrapper`](/docs/api/tools/classes/ZapierNLAWrapper), `actionId`: `string`, `zapierDescription`: `string`, `paramsSchema`: `ZapierValues`, `params`?: `ZapierValues`): [`ZapierNLARunAction`](/docs/api/tools/classes/ZapierNLARunAction)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`apiWrapper`

[`ZapierNLAWrapper`](/docs/api/tools/classes/ZapierNLAWrapper)

`actionId`

`string`

`zapierDescription`

`string`

`paramsSchema`

`ZapierValues`

`params?`

`ZapierValues`

#### Returns[](#returns "Direct link to Returns")

[`ZapierNLARunAction`](/docs/api/tools/classes/ZapierNLARunAction)

#### Overrides[](#overrides "Direct link to Overrides")

[Tool](/docs/api/tools/classes/Tool).[constructor](/docs/api/tools/classes/Tool#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/tools/zapier.ts:252](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/zapier.ts#L252)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### actionId[](#actionid "Direct link to actionId")

> **actionId**: `string`

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/tools/zapier.ts:244](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/zapier.ts#L244)

### apiWrapper[](#apiwrapper "Direct link to apiWrapper")

> **apiWrapper**: [`ZapierNLAWrapper`](/docs/api/tools/classes/ZapierNLAWrapper)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/tools/zapier.ts:242](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/zapier.ts#L242)

### description[](#description "Direct link to description")

> **description**: `string`

#### Overrides[](#overrides-1 "Direct link to Overrides")

[Tool](/docs/api/tools/classes/Tool).[description](/docs/api/tools/classes/Tool#description)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/tools/zapier.ts:250](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/zapier.ts#L250)

### lc\_kwargs[](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[lc\_kwargs](/docs/api/tools/classes/Tool#lc_kwargs)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L57)

### lc\_serializable[](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[lc\_serializable](/docs/api/tools/classes/Tool#lc_serializable)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L55)

### name[](#name "Direct link to name")

> **name**: `string`

#### Overrides[](#overrides-2 "Direct link to Overrides")

[Tool](/docs/api/tools/classes/Tool).[name](/docs/api/tools/classes/Tool#name)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/tools/zapier.ts:248](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/zapier.ts#L248)

### returnDirect[](#returndirect "Direct link to returnDirect")

> **returnDirect**: `boolean` = `false`

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[returnDirect](/docs/api/tools/classes/Tool#returndirect)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/tools/base.ts:81](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/base.ts#L81)

### schema[](#schema "Direct link to schema")

> **schema**: `ZodEffects`<`ZodObject`<{`input`: `ZodOptional`<`ZodString`\>;}, "strip", `ZodTypeAny`, {`input`?: `string`;}, {`input`?: `string`;}\>, `undefined` | `string`, {`input`?: `string`;}\>

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[schema](/docs/api/tools/classes/Tool#schema)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/tools/base.ts:88](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/base.ts#L88)

### verbose[](#verbose "Direct link to verbose")

> **verbose**: `boolean`

Whether to print out response text.

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[verbose](/docs/api/tools/classes/Tool#verbose)

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:44](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L44)

### callbacks?[](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[callbacks](/docs/api/tools/classes/Tool#callbacks)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L46)

### metadata?[](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[metadata](/docs/api/tools/classes/Tool#metadata)

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:50](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L50)

### params?[](#params "Direct link to params?")

> **params**: `ZapierValues`

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/tools/zapier.ts:246](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/zapier.ts#L246)

### tags?[](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[tags](/docs/api/tools/classes/Tool#tags)

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L48)

### lc\_runnable[](#lc_runnable "Direct link to lc_runnable")

> `Protected` **lc\_runnable**: `boolean` = `true`

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[lc\_runnable](/docs/api/tools/classes/Tool#lc_runnable)

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:34](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L34)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[](#returns-1 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-9 "Direct link to Inherited from")

Tool.lc\_aliases

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

#### Inherited from[](#inherited-from-10 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[lc\_aliases](/docs/api/tools/classes/Tool#lc_aliases)

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

### lc\_attributes[](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[](#returns-2 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-11 "Direct link to Inherited from")

Tool.lc\_attributes

#### Defined in[](#defined-in-17 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:52](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L52)

#### Inherited from[](#inherited-from-12 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[lc\_attributes](/docs/api/tools/classes/Tool#lc_attributes)

#### Defined in[](#defined-in-18 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:52](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L52)

### lc\_namespace[](#lc_namespace "Direct link to lc_namespace")

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

> **lc\_namespace**(): `string`\[\]

#### Returns[](#returns-3 "Direct link to Returns")

`string`\[\]

#### Inherited from[](#inherited-from-13 "Direct link to Inherited from")

Tool.lc\_namespace

#### Defined in[](#defined-in-19 "Direct link to Defined in")

[langchain/src/tools/base.ts:25](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/base.ts#L25)

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[](#inherited-from-14 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[lc\_namespace](/docs/api/tools/classes/Tool#lc_namespace)

#### Defined in[](#defined-in-20 "Direct link to Defined in")

[langchain/src/tools/base.ts:25](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/base.ts#L25)

### lc\_secrets[](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[](#returns-4 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-15 "Direct link to Inherited from")

Tool.lc\_secrets

#### Defined in[](#defined-in-21 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

#### Inherited from[](#inherited-from-16 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[lc\_secrets](/docs/api/tools/classes/Tool#lc_secrets)

#### Defined in[](#defined-in-22 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### \_patchConfig()[](#_patchconfig "Direct link to _patchconfig")

> **\_patchConfig**(`config`: `Partial`<`BaseCallbackConfig`\> = `{}`, `callbackManager`: `undefined` | [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager) = `undefined`): `Partial`<`BaseCallbackConfig`\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

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

#### Inherited from[](#inherited-from-17 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[\_patchConfig](/docs/api/tools/classes/Tool#_patchconfig)

#### Defined in[](#defined-in-23 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:146](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L146)

### \_streamIterator()[](#_streamiterator "Direct link to _streamiterator")

> **\_streamIterator**(`input`: `string` | {}, `options`?: `Partial`<`BaseCallbackConfig`\>): `AsyncGenerator`<`string`, `any`, `unknown`\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`input`

`string` | {}

`options?`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-6 "Direct link to Returns")

`AsyncGenerator`<`string`, `any`, `unknown`\>

#### Inherited from[](#inherited-from-18 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[\_streamIterator](/docs/api/tools/classes/Tool#_streamiterator)

#### Defined in[](#defined-in-24 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:86](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L86)

### batch()[](#batch "Direct link to batch()")

> **batch**(`inputs`: (`string` | {})\[\], `options`?: `Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\], `batchOptions`?: `object`): `Promise`<`string`\[\]\>

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

`inputs`

(`string` | {})\[\]

`options?`

`Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\]

`batchOptions?`

`object`

`batchOptions.maxConcurrency?`

`number`

#### Returns[](#returns-7 "Direct link to Returns")

`Promise`<`string`\[\]\>

#### Inherited from[](#inherited-from-19 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[batch](/docs/api/tools/classes/Tool#batch)

#### Defined in[](#defined-in-25 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:63](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L63)

### bind()[](#bind "Direct link to bind()")

> **bind**(`kwargs`: `Partial`<`BaseCallbackConfig`\>): [`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<`string` | {}, `string`, `BaseCallbackConfig`\>

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

`kwargs`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-8 "Direct link to Returns")

[`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<`string` | {}, `string`, `BaseCallbackConfig`\>

#### Inherited from[](#inherited-from-20 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[bind](/docs/api/tools/classes/Tool#bind)

#### Defined in[](#defined-in-26 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:41](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L41)

### call()[](#call "Direct link to call()")

> **call**(`arg`: `undefined` | `string` | {`input`?: `string`;}, `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\>

#### Parameters[](#parameters-5 "Direct link to Parameters")

Parameter

Type

`arg`

`undefined` | `string` | {`input`?: `string`;}

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-9 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[](#inherited-from-21 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[call](/docs/api/tools/classes/Tool#call)

#### Defined in[](#defined-in-27 "Direct link to Defined in")

[langchain/src/tools/base.ts:96](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/base.ts#L96)

### invoke()[](#invoke "Direct link to invoke()")

> **invoke**(`input`: `string` | {}, `config`?: `BaseCallbackConfig`): `Promise`<`string`\>

#### Parameters[](#parameters-6 "Direct link to Parameters")

Parameter

Type

`input`

`string` | {}

`config?`

`BaseCallbackConfig`

#### Returns[](#returns-10 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[](#inherited-from-22 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[invoke](/docs/api/tools/classes/Tool#invoke)

#### Defined in[](#defined-in-28 "Direct link to Defined in")

[langchain/src/tools/base.ts:38](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/base.ts#L38)

### pipe()[](#pipe "Direct link to pipe()")

> **pipe**<NewRunOutput\>(`coerceable`: [`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<`string`, `NewRunOutput`\>): [`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<`string` | {}, `NewRunOutput`\>

#### Type parameters[](#type-parameters "Direct link to Type parameters")

*   `NewRunOutput`

#### Parameters[](#parameters-7 "Direct link to Parameters")

Parameter

Type

`coerceable`

[`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<`string`, `NewRunOutput`\>

#### Returns[](#returns-11 "Direct link to Returns")

[`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<`string` | {}, `NewRunOutput`\>

#### Inherited from[](#inherited-from-23 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[pipe](/docs/api/tools/classes/Tool#pipe)

#### Defined in[](#defined-in-29 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:153](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L153)

### stream()[](#stream "Direct link to stream()")

> **stream**(`input`: `string` | {}, `options`?: `Partial`<`BaseCallbackConfig`\>): `Promise`<`IterableReadableStream`<`string`\>\>

#### Parameters[](#parameters-8 "Direct link to Parameters")

Parameter

Type

`input`

`string` | {}

`options?`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-12 "Direct link to Returns")

`Promise`<`IterableReadableStream`<`string`\>\>

#### Inherited from[](#inherited-from-24 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[stream](/docs/api/tools/classes/Tool#stream)

#### Defined in[](#defined-in-30 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:93](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L93)

### toJSON()[](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[](#returns-13 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[](#inherited-from-25 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[toJSON](/docs/api/tools/classes/Tool#tojson)

#### Defined in[](#defined-in-31 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[](#returns-14 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[](#inherited-from-26 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[toJSONNotImplemented](/docs/api/tools/classes/Tool#tojsonnotimplemented)

#### Defined in[](#defined-in-32 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L151)

### isRunnable()[](#isrunnable "Direct link to isRunnable()")

> `Static` **isRunnable**(`thing`: `any`): thing is Runnable<any, any, BaseCallbackConfig\>

#### Parameters[](#parameters-9 "Direct link to Parameters")

Parameter

Type

`thing`

`any`

#### Returns[](#returns-15 "Direct link to Returns")

thing is Runnable<any, any, BaseCallbackConfig\>

#### Inherited from[](#inherited-from-27 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[isRunnable](/docs/api/tools/classes/Tool#isrunnable)

#### Defined in[](#defined-in-33 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:164](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L164)

### \_callWithConfig()[](#_callwithconfig "Direct link to _callwithconfig")

> `Protected` **\_callWithConfig**<T\>(`func`: `Function`, `input`: `T`, `options`?: `BaseCallbackConfig` & {`runType`?: `string`;}): `Promise`<`string`\>

#### Type parameters[](#type-parameters-1 "Direct link to Type parameters")

*   `T` _extends_ `string` | {}

#### Parameters[](#parameters-10 "Direct link to Parameters")

Parameter

Type

`func`

(`input`: `T`) => `Promise`<`string`\>

`input`

`T`

`options?`

`BaseCallbackConfig` & {`runType`?: `string`;}

#### Returns[](#returns-16 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[](#inherited-from-28 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[\_callWithConfig](/docs/api/tools/classes/Tool#_callwithconfig)

#### Defined in[](#defined-in-34 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:117](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L117)

### \_getOptionsList()[](#_getoptionslist "Direct link to _getoptionslist")

> `Protected` **\_getOptionsList**(`options`: `Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\], `length`: `number` = `0`): `Partial`<`BaseCallbackConfig`\>\[\]

#### Parameters[](#parameters-11 "Direct link to Parameters")

Parameter

Type

Default value

`options`

`Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\]

`undefined`

`length`

`number`

`0`

#### Returns[](#returns-17 "Direct link to Returns")

`Partial`<`BaseCallbackConfig`\>\[\]

#### Inherited from[](#inherited-from-29 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[\_getOptionsList](/docs/api/tools/classes/Tool#_getoptionslist)

#### Defined in[](#defined-in-35 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L48)

### \_separateRunnableConfigFromCallOptions()[](#_separaterunnableconfigfromcalloptions "Direct link to _separaterunnableconfigfromcalloptions")

> `Protected` **\_separateRunnableConfigFromCallOptions**(`options`: `Partial`<`BaseCallbackConfig`\> = `{}`): \[`BaseCallbackConfig`, `Omit`<`Partial`<`BaseCallbackConfig`\>, _keyof_ `BaseCallbackConfig`\>\]

#### Parameters[](#parameters-12 "Direct link to Parameters")

Parameter

Type

`options`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-18 "Direct link to Returns")

\[`BaseCallbackConfig`, `Omit`<`Partial`<`BaseCallbackConfig`\>, _keyof_ `BaseCallbackConfig`\>\]

#### Inherited from[](#inherited-from-30 "Direct link to Inherited from")

[Tool](/docs/api/tools/classes/Tool).[\_separateRunnableConfigFromCallOptions](/docs/api/tools/classes/Tool#_separaterunnableconfigfromcalloptions)

#### Defined in[](#defined-in-36 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:102](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L102)