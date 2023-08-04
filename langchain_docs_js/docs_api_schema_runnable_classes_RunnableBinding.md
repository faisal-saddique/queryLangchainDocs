RunnableBinding<RunInput, RunOutput, CallOptions\>
==================================================

Type parameters[](#type-parameters "Direct link to Type parameters")
---------------------------------------------------------------------

*   `RunInput`
*   `RunOutput`
*   `CallOptions` _extends_ `BaseCallbackConfig`

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`Runnable`](/docs/api/schema_runnable/classes/Runnable)<`RunInput`, `RunOutput`, `CallOptions`\>.**RunnableBinding**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new RunnableBinding**<RunInput, RunOutput, CallOptions\>(`fields`: `object`): [`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<`RunInput`, `RunOutput`, `CallOptions`\>

#### Type parameters[](#type-parameters-1 "Direct link to Type parameters")

*   `RunInput`
*   `RunOutput`
*   `CallOptions` _extends_ `BaseCallbackConfig`

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`fields`

`object`

`fields.bound`

[`Runnable`](/docs/api/schema_runnable/classes/Runnable)<`RunInput`, `RunOutput`, `CallOptions`\>

`fields.kwargs`

`Partial`<`CallOptions`\>

#### Returns[](#returns "Direct link to Returns")

[`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<`RunInput`, `RunOutput`, `CallOptions`\>

#### Overrides[](#overrides "Direct link to Overrides")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[constructor](/docs/api/schema_runnable/classes/Runnable#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/schema/runnable.ts:533](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L533)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### lc\_kwargs[](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[lc\_kwargs](/docs/api/schema_runnable/classes/Runnable#lc_kwargs)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L57)

### lc\_namespace[](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Overrides[](#overrides-1 "Direct link to Overrides")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[lc\_namespace](/docs/api/schema_runnable/classes/Runnable#lc_namespace)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:525](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L525)

### lc\_serializable[](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `true`

#### Overrides[](#overrides-2 "Direct link to Overrides")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[lc\_serializable](/docs/api/schema_runnable/classes/Runnable#lc_serializable)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:527](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L527)

### bound[](#bound "Direct link to bound")

> `Protected` **bound**: [`Runnable`](/docs/api/schema_runnable/classes/Runnable)<`RunInput`, `RunOutput`, `CallOptions`\>

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:529](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L529)

### kwargs[](#kwargs "Direct link to kwargs")

> `Protected` **kwargs**: `Partial`<`CallOptions`\>

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:531](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L531)

### lc\_runnable[](#lc_runnable "Direct link to lc_runnable")

> `Protected` **lc\_runnable**: `boolean` = `true`

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[lc\_runnable](/docs/api/schema_runnable/classes/Runnable#lc_runnable)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:34](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L34)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[](#returns-1 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

Runnable.lc\_aliases

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[lc\_aliases](/docs/api/schema_runnable/classes/Runnable#lc_aliases)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

### lc\_attributes[](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[](#returns-2 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

Runnable.lc\_attributes

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L80)

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[lc\_attributes](/docs/api/schema_runnable/classes/Runnable#lc_attributes)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L80)

### lc\_secrets[](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

Runnable.lc\_secrets

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[lc\_secrets](/docs/api/schema_runnable/classes/Runnable#lc_secrets)

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### \_patchConfig()[](#_patchconfig "Direct link to _patchconfig")

> **\_patchConfig**(`config`: `Partial`<`CallOptions`\> = `{}`, `callbackManager`: `undefined` | [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager) = `undefined`): `Partial`<`CallOptions`\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

Default value

`config`

`Partial`<`CallOptions`\>

`{}`

`callbackManager`

`undefined` | [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

`undefined`

#### Returns[](#returns-4 "Direct link to Returns")

`Partial`<`CallOptions`\>

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[\_patchConfig](/docs/api/schema_runnable/classes/Runnable#_patchconfig)

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:146](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L146)

### \_streamIterator()[](#_streamiterator "Direct link to _streamiterator")

> **\_streamIterator**(`input`: `RunInput`, `options`?: `Partial`<`CallOptions`\>): `AsyncGenerator`<`RunOutput`, `any`, `unknown`\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`input`

`RunInput`

`options?`

`Partial`<`CallOptions`\>

#### Returns[](#returns-5 "Direct link to Returns")

`AsyncGenerator`<`RunOutput`, `any`, `unknown`\>

#### Inherited from[](#inherited-from-9 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[\_streamIterator](/docs/api/schema_runnable/classes/Runnable#_streamiterator)

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:86](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L86)

### batch()[](#batch "Direct link to batch()")

> **batch**(`inputs`: `RunInput`\[\], `options`?: `Partial`<`CallOptions`\> | `Partial`<`CallOptions`\>\[\], `batchOptions`?: `object`): `Promise`<`RunOutput`\[\]\>

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

`inputs`

`RunInput`\[\]

`options?`

`Partial`<`CallOptions`\> | `Partial`<`CallOptions`\>\[\]

`batchOptions?`

`object`

`batchOptions.maxConcurrency?`

`number`

#### Returns[](#returns-6 "Direct link to Returns")

`Promise`<`RunOutput`\[\]\>

#### Overrides[](#overrides-3 "Direct link to Overrides")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[batch](/docs/api/schema_runnable/classes/Runnable#batch)

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:558](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L558)

### bind()[](#bind "Direct link to bind()")

> **bind**(`kwargs`: `Partial`<`CallOptions`\>): [`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<`RunInput`, `RunOutput`, `CallOptions`\>

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

`kwargs`

`Partial`<`CallOptions`\>

#### Returns[](#returns-7 "Direct link to Returns")

[`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<`RunInput`, `RunOutput`, `CallOptions`\>

#### Overrides[](#overrides-4 "Direct link to Overrides")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[bind](/docs/api/schema_runnable/classes/Runnable#bind)

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:542](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L542)

### invoke()[](#invoke "Direct link to invoke()")

> **invoke**(`input`: `RunInput`, `options`?: `Partial`<`CallOptions`\>): `Promise`<`RunOutput`\>

#### Parameters[](#parameters-5 "Direct link to Parameters")

Parameter

Type

`input`

`RunInput`

`options?`

`Partial`<`CallOptions`\>

#### Returns[](#returns-8 "Direct link to Returns")

`Promise`<`RunOutput`\>

#### Overrides[](#overrides-5 "Direct link to Overrides")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[invoke](/docs/api/schema_runnable/classes/Runnable#invoke)

#### Defined in[](#defined-in-17 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:551](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L551)

### pipe()[](#pipe "Direct link to pipe()")

> **pipe**<NewRunOutput\>(`coerceable`: [`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<`RunOutput`, `NewRunOutput`\>): [`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<`RunInput`, `NewRunOutput`\>

#### Type parameters[](#type-parameters-2 "Direct link to Type parameters")

*   `NewRunOutput`

#### Parameters[](#parameters-6 "Direct link to Parameters")

Parameter

Type

`coerceable`

[`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<`RunOutput`, `NewRunOutput`\>

#### Returns[](#returns-9 "Direct link to Returns")

[`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<`RunInput`, `NewRunOutput`\>

#### Inherited from[](#inherited-from-10 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[pipe](/docs/api/schema_runnable/classes/Runnable#pipe)

#### Defined in[](#defined-in-18 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:153](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L153)

### stream()[](#stream "Direct link to stream()")

> **stream**(`input`: `RunInput`, `options`?: `Partial`<`CallOptions`\>): `Promise`<`IterableReadableStream`<`RunOutput`\>\>

#### Parameters[](#parameters-7 "Direct link to Parameters")

Parameter

Type

`input`

`RunInput`

`options?`

`Partial`<`CallOptions`\>

#### Returns[](#returns-10 "Direct link to Returns")

`Promise`<`IterableReadableStream`<`RunOutput`\>\>

#### Overrides[](#overrides-6 "Direct link to Overrides")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[stream](/docs/api/schema_runnable/classes/Runnable#stream)

#### Defined in[](#defined-in-19 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:572](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L572)

### toJSON()[](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[](#returns-11 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[](#inherited-from-11 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[toJSON](/docs/api/schema_runnable/classes/Runnable#tojson)

#### Defined in[](#defined-in-20 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[](#returns-12 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[](#inherited-from-12 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[toJSONNotImplemented](/docs/api/schema_runnable/classes/Runnable#tojsonnotimplemented)

#### Defined in[](#defined-in-21 "Direct link to Defined in")

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

#### Inherited from[](#inherited-from-13 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[isRunnable](/docs/api/schema_runnable/classes/Runnable#isrunnable)

#### Defined in[](#defined-in-22 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:164](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L164)

### \_callWithConfig()[](#_callwithconfig "Direct link to _callwithconfig")

> `Protected` **\_callWithConfig**<T\>(`func`: `Function`, `input`: `T`, `options`?: `BaseCallbackConfig` & {`runType`?: `string`;}): `Promise`<`RunOutput`\>

#### Type parameters[](#type-parameters-3 "Direct link to Type parameters")

*   `T`

#### Parameters[](#parameters-9 "Direct link to Parameters")

Parameter

Type

`func`

(`input`: `T`) => `Promise`<`RunOutput`\>

`input`

`T`

`options?`

`BaseCallbackConfig` & {`runType`?: `string`;}

#### Returns[](#returns-14 "Direct link to Returns")

`Promise`<`RunOutput`\>

#### Inherited from[](#inherited-from-14 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[\_callWithConfig](/docs/api/schema_runnable/classes/Runnable#_callwithconfig)

#### Defined in[](#defined-in-23 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:117](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L117)

### \_getOptionsList()[](#_getoptionslist "Direct link to _getoptionslist")

> `Protected` **\_getOptionsList**(`options`: `Partial`<`CallOptions`\> | `Partial`<`CallOptions`\>\[\], `length`: `number` = `0`): `Partial`<`CallOptions`\>\[\]

#### Parameters[](#parameters-10 "Direct link to Parameters")

Parameter

Type

Default value

`options`

`Partial`<`CallOptions`\> | `Partial`<`CallOptions`\>\[\]

`undefined`

`length`

`number`

`0`

#### Returns[](#returns-15 "Direct link to Returns")

`Partial`<`CallOptions`\>\[\]

#### Inherited from[](#inherited-from-15 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[\_getOptionsList](/docs/api/schema_runnable/classes/Runnable#_getoptionslist)

#### Defined in[](#defined-in-24 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L48)

### \_separateRunnableConfigFromCallOptions()[](#_separaterunnableconfigfromcalloptions "Direct link to _separaterunnableconfigfromcalloptions")

> `Protected` **\_separateRunnableConfigFromCallOptions**(`options`: `Partial`<`CallOptions`\> = `{}`): \[`BaseCallbackConfig`, `Omit`<`Partial`<`CallOptions`\>, _keyof_ `BaseCallbackConfig`\>\]

#### Parameters[](#parameters-11 "Direct link to Parameters")

Parameter

Type

`options`

`Partial`<`CallOptions`\>

#### Returns[](#returns-16 "Direct link to Returns")

\[`BaseCallbackConfig`, `Omit`<`Partial`<`CallOptions`\>, _keyof_ `BaseCallbackConfig`\>\]

#### Inherited from[](#inherited-from-16 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[\_separateRunnableConfigFromCallOptions](/docs/api/schema_runnable/classes/Runnable#_separaterunnableconfigfromcalloptions)

#### Defined in[](#defined-in-25 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:102](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L102)