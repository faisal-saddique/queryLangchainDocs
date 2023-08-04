RunnablePassthrough<RunInput\>
==============================

Type parameters[](#type-parameters "Direct link to Type parameters")
---------------------------------------------------------------------

*   `RunInput`

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`Runnable`](/docs/api/schema_runnable/classes/Runnable)<`RunInput`, `RunInput`\>.**RunnablePassthrough**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new RunnablePassthrough**<RunInput\>(`kwargs`?: `SerializedFields`, ...`_args`?: `never`\[\]): [`RunnablePassthrough`](/docs/api/schema_runnable/classes/RunnablePassthrough)<`RunInput`\>

#### Type parameters[](#type-parameters-1 "Direct link to Type parameters")

*   `RunInput`

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`kwargs?`

`SerializedFields`

`..._args?`

`never`\[\]

#### Returns[](#returns "Direct link to Returns")

[`RunnablePassthrough`](/docs/api/schema_runnable/classes/RunnablePassthrough)<`RunInput`\>

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[constructor](/docs/api/schema_runnable/classes/Runnable#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/load/serializable.ts:94](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L94)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### lc\_kwargs[](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[lc\_kwargs](/docs/api/schema_runnable/classes/Runnable#lc_kwargs)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L57)

### lc\_namespace[](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Overrides[](#overrides "Direct link to Overrides")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[lc\_namespace](/docs/api/schema_runnable/classes/Runnable#lc_namespace)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:481](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L481)

### lc\_serializable[](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `true`

#### Overrides[](#overrides-1 "Direct link to Overrides")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[lc\_serializable](/docs/api/schema_runnable/classes/Runnable#lc_serializable)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:483](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L483)

### lc\_runnable[](#lc_runnable "Direct link to lc_runnable")

> `Protected` **lc\_runnable**: `boolean` = `true`

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[lc\_runnable](/docs/api/schema_runnable/classes/Runnable#lc_runnable)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:34](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L34)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[](#returns-1 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

Runnable.lc\_aliases

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[lc\_aliases](/docs/api/schema_runnable/classes/Runnable#lc_aliases)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

### lc\_attributes[](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[](#returns-2 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

Runnable.lc\_attributes

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L80)

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[lc\_attributes](/docs/api/schema_runnable/classes/Runnable#lc_attributes)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L80)

### lc\_secrets[](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

Runnable.lc\_secrets

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[lc\_secrets](/docs/api/schema_runnable/classes/Runnable#lc_secrets)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

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

#### Returns[](#returns-4 "Direct link to Returns")

`Partial`<`BaseCallbackConfig`\>

#### Inherited from[](#inherited-from-9 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[\_patchConfig](/docs/api/schema_runnable/classes/Runnable#_patchconfig)

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:146](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L146)

### \_streamIterator()[](#_streamiterator "Direct link to _streamiterator")

> **\_streamIterator**(`input`: `RunInput`, `options`?: `Partial`<`BaseCallbackConfig`\>): `AsyncGenerator`<`RunInput`, `any`, `unknown`\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`input`

`RunInput`

`options?`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-5 "Direct link to Returns")

`AsyncGenerator`<`RunInput`, `any`, `unknown`\>

#### Inherited from[](#inherited-from-10 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[\_streamIterator](/docs/api/schema_runnable/classes/Runnable#_streamiterator)

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:86](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L86)

### batch()[](#batch "Direct link to batch()")

> **batch**(`inputs`: `RunInput`\[\], `options`?: `Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\], `batchOptions`?: `object`): `Promise`<`RunInput`\[\]\>

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

`inputs`

`RunInput`\[\]

`options?`

`Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\]

`batchOptions?`

`object`

`batchOptions.maxConcurrency?`

`number`

#### Returns[](#returns-6 "Direct link to Returns")

`Promise`<`RunInput`\[\]\>

#### Inherited from[](#inherited-from-11 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[batch](/docs/api/schema_runnable/classes/Runnable#batch)

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:63](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L63)

### bind()[](#bind "Direct link to bind()")

> **bind**(`kwargs`: `Partial`<`BaseCallbackConfig`\>): [`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<`RunInput`, `RunInput`, `BaseCallbackConfig`\>

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

`kwargs`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-7 "Direct link to Returns")

[`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<`RunInput`, `RunInput`, `BaseCallbackConfig`\>

#### Inherited from[](#inherited-from-12 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[bind](/docs/api/schema_runnable/classes/Runnable#bind)

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:41](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L41)

### invoke()[](#invoke "Direct link to invoke()")

> **invoke**(`input`: `RunInput`, `options`?: `Partial`<`BaseCallbackConfig`\>): `Promise`<`RunInput`\>

#### Parameters[](#parameters-5 "Direct link to Parameters")

Parameter

Type

`input`

`RunInput`

`options?`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-8 "Direct link to Returns")

`Promise`<`RunInput`\>

#### Overrides[](#overrides-2 "Direct link to Overrides")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[invoke](/docs/api/schema_runnable/classes/Runnable#invoke)

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:485](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L485)

### pipe()[](#pipe "Direct link to pipe()")

> **pipe**<NewRunOutput\>(`coerceable`: [`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<`RunInput`, `NewRunOutput`\>): [`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<`RunInput`, `NewRunOutput`\>

#### Type parameters[](#type-parameters-2 "Direct link to Type parameters")

*   `NewRunOutput`

#### Parameters[](#parameters-6 "Direct link to Parameters")

Parameter

Type

`coerceable`

[`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<`RunInput`, `NewRunOutput`\>

#### Returns[](#returns-9 "Direct link to Returns")

[`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<`RunInput`, `NewRunOutput`\>

#### Inherited from[](#inherited-from-13 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[pipe](/docs/api/schema_runnable/classes/Runnable#pipe)

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:153](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L153)

### stream()[](#stream "Direct link to stream()")

> **stream**(`input`: `RunInput`, `options`?: `Partial`<`BaseCallbackConfig`\>): `Promise`<`IterableReadableStream`<`RunInput`\>\>

#### Parameters[](#parameters-7 "Direct link to Parameters")

Parameter

Type

`input`

`RunInput`

`options?`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-10 "Direct link to Returns")

`Promise`<`IterableReadableStream`<`RunInput`\>\>

#### Inherited from[](#inherited-from-14 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[stream](/docs/api/schema_runnable/classes/Runnable#stream)

#### Defined in[](#defined-in-17 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:93](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L93)

### toJSON()[](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[](#returns-11 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[](#inherited-from-15 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[toJSON](/docs/api/schema_runnable/classes/Runnable#tojson)

#### Defined in[](#defined-in-18 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[](#returns-12 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[](#inherited-from-16 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[toJSONNotImplemented](/docs/api/schema_runnable/classes/Runnable#tojsonnotimplemented)

#### Defined in[](#defined-in-19 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L151)

### isRunnable()[](#isrunnable "Direct link to isRunnable()")

> `Static` **isRunnable**(`thing`: `any`): thing is Runnable<any, any, BaseCallbackConfig\>

#### Parameters[](#parameters-8 "Direct link to Parameters")

Parameter

Type

`thing`

`any`

#### Returns[](#returns-13 "Direct link to Returns")

thing is Runnable<any, any, BaseCallbackConfig\>

#### Inherited from[](#inherited-from-17 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[isRunnable](/docs/api/schema_runnable/classes/Runnable#isrunnable)

#### Defined in[](#defined-in-20 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:164](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L164)

### \_callWithConfig()[](#_callwithconfig "Direct link to _callwithconfig")

> `Protected` **\_callWithConfig**<T\>(`func`: `Function`, `input`: `T`, `options`?: `BaseCallbackConfig` & {`runType`?: `string`;}): `Promise`<`RunInput`\>

#### Type parameters[](#type-parameters-3 "Direct link to Type parameters")

*   `T`

#### Parameters[](#parameters-9 "Direct link to Parameters")

Parameter

Type

`func`

(`input`: `T`) => `Promise`<`RunInput`\>

`input`

`T`

`options?`

`BaseCallbackConfig` & {`runType`?: `string`;}

#### Returns[](#returns-14 "Direct link to Returns")

`Promise`<`RunInput`\>

#### Inherited from[](#inherited-from-18 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[\_callWithConfig](/docs/api/schema_runnable/classes/Runnable#_callwithconfig)

#### Defined in[](#defined-in-21 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:117](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L117)

### \_getOptionsList()[](#_getoptionslist "Direct link to _getoptionslist")

> `Protected` **\_getOptionsList**(`options`: `Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\], `length`: `number` = `0`): `Partial`<`BaseCallbackConfig`\>\[\]

#### Parameters[](#parameters-10 "Direct link to Parameters")

Parameter

Type

Default value

`options`

`Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\]

`undefined`

`length`

`number`

`0`

#### Returns[](#returns-15 "Direct link to Returns")

`Partial`<`BaseCallbackConfig`\>\[\]

#### Inherited from[](#inherited-from-19 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[\_getOptionsList](/docs/api/schema_runnable/classes/Runnable#_getoptionslist)

#### Defined in[](#defined-in-22 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L48)

### \_separateRunnableConfigFromCallOptions()[](#_separaterunnableconfigfromcalloptions "Direct link to _separaterunnableconfigfromcalloptions")

> `Protected` **\_separateRunnableConfigFromCallOptions**(`options`: `Partial`<`BaseCallbackConfig`\> = `{}`): \[`BaseCallbackConfig`, `Omit`<`Partial`<`BaseCallbackConfig`\>, _keyof_ `BaseCallbackConfig`\>\]

#### Parameters[](#parameters-11 "Direct link to Parameters")

Parameter

Type

`options`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-16 "Direct link to Returns")

\[`BaseCallbackConfig`, `Omit`<`Partial`<`BaseCallbackConfig`\>, _keyof_ `BaseCallbackConfig`\>\]

#### Inherited from[](#inherited-from-20 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[\_separateRunnableConfigFromCallOptions](/docs/api/schema_runnable/classes/Runnable#_separaterunnableconfigfromcalloptions)

#### Defined in[](#defined-in-23 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:102](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L102)