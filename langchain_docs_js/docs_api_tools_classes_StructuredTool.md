StructuredTool<T\>
==================

Base class for Tools that accept input of any shape defined by a Zod schema.

Type parameters[](#type-parameters "Direct link to Type parameters")
---------------------------------------------------------------------

*   `T` _extends_ `z.ZodObject`<`any`, `any`, `any`, `any`\> = `z.ZodObject`<`any`, `any`, `any`, `any`\>

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseLangChain`](/docs/api/base_language/classes/BaseLangChain)<`z.output`<`T`\> _extends_ `string` ? `string` : `never` | `z.input`<`T`\>, `string`\>.**StructuredTool**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new StructuredTool**<T\>(`fields`?: [`ToolParams`](/docs/api/tools/interfaces/ToolParams)): [`StructuredTool`](/docs/api/tools/classes/StructuredTool)<`T`\>

#### Type parameters[](#type-parameters-1 "Direct link to Type parameters")

*   `T` _extends_ `ZodObject`<`any`, `any`, `any`, `any`, {}, `T`\> = `ZodObject`<`any`, `any`, `any`, `any`, {}\>

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`fields?`

[`ToolParams`](/docs/api/tools/interfaces/ToolParams)

#### Returns[](#returns "Direct link to Returns")

[`StructuredTool`](/docs/api/tools/classes/StructuredTool)<`T`\>

#### Overrides[](#overrides "Direct link to Overrides")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[constructor](/docs/api/base_language/classes/BaseLangChain#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/tools/base.ts:29](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/base.ts#L29)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### description[](#description "Direct link to description")

> `Abstract` **description**: `string`

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/tools/base.ts:79](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/base.ts#L79)

### lc\_kwargs[](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[lc\_kwargs](/docs/api/base_language/classes/BaseLangChain#lc_kwargs)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L57)

### lc\_serializable[](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[lc\_serializable](/docs/api/base_language/classes/BaseLangChain#lc_serializable)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L55)

### name[](#name "Direct link to name")

> `Abstract` **name**: `string`

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/tools/base.ts:77](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/base.ts#L77)

### returnDirect[](#returndirect "Direct link to returnDirect")

> **returnDirect**: `boolean` = `false`

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/tools/base.ts:81](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/base.ts#L81)

### schema[](#schema "Direct link to schema")

> `Abstract` **schema**: `T` | `ZodEffects`<`T`, `output`<`T`\>, `input`<`T`\>\>

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/tools/base.ts:23](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/base.ts#L23)

### verbose[](#verbose "Direct link to verbose")

> **verbose**: `boolean`

Whether to print out response text.

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[verbose](/docs/api/base_language/classes/BaseLangChain#verbose)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:44](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L44)

### callbacks?[](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[callbacks](/docs/api/base_language/classes/BaseLangChain#callbacks)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L46)

### metadata?[](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[metadata](/docs/api/base_language/classes/BaseLangChain#metadata)

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:50](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L50)

### tags?[](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[tags](/docs/api/base_language/classes/BaseLangChain#tags)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L48)

### lc\_runnable[](#lc_runnable "Direct link to lc_runnable")

> `Protected` **lc\_runnable**: `boolean` = `true`

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[lc\_runnable](/docs/api/base_language/classes/BaseLangChain#lc_runnable)

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:34](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L34)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[](#returns-1 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

BaseLangChain.lc\_aliases

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[lc\_aliases](/docs/api/base_language/classes/BaseLangChain#lc_aliases)

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

### lc\_attributes[](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[](#returns-2 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-9 "Direct link to Inherited from")

BaseLangChain.lc\_attributes

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:52](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L52)

#### Inherited from[](#inherited-from-10 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[lc\_attributes](/docs/api/base_language/classes/BaseLangChain#lc_attributes)

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:52](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L52)

### lc\_namespace[](#lc_namespace "Direct link to lc_namespace")

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

> **lc\_namespace**(): `string`\[\]

#### Returns[](#returns-3 "Direct link to Returns")

`string`\[\]

#### Overrides[](#overrides-1 "Direct link to Overrides")

BaseLangChain.lc\_namespace

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/tools/base.ts:25](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/base.ts#L25)

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Overrides[](#overrides-2 "Direct link to Overrides")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[lc\_namespace](/docs/api/base_language/classes/BaseLangChain#lc_namespace)

#### Defined in[](#defined-in-17 "Direct link to Defined in")

[langchain/src/tools/base.ts:25](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/base.ts#L25)

### lc\_secrets[](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[](#returns-4 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-11 "Direct link to Inherited from")

BaseLangChain.lc\_secrets

#### Defined in[](#defined-in-18 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

#### Inherited from[](#inherited-from-12 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[lc\_secrets](/docs/api/base_language/classes/BaseLangChain#lc_secrets)

#### Defined in[](#defined-in-19 "Direct link to Defined in")

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

#### Inherited from[](#inherited-from-13 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[\_patchConfig](/docs/api/base_language/classes/BaseLangChain#_patchconfig)

#### Defined in[](#defined-in-20 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:146](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L146)

### \_streamIterator()[](#_streamiterator "Direct link to _streamiterator")

> **\_streamIterator**(`input`: `input`<`T`\> | `output`<`T`\> _extends_ `string` ? `string` : `never`, `options`?: `Partial`<`BaseCallbackConfig`\>): `AsyncGenerator`<`string`, `any`, `unknown`\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`input`

`input`<`T`\> | `output`<`T`\> _extends_ `string` ? `string` : `never`

`options?`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-6 "Direct link to Returns")

`AsyncGenerator`<`string`, `any`, `unknown`\>

#### Inherited from[](#inherited-from-14 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[\_streamIterator](/docs/api/base_language/classes/BaseLangChain#_streamiterator)

#### Defined in[](#defined-in-21 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:86](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L86)

### batch()[](#batch "Direct link to batch()")

> **batch**(`inputs`: (`input`<`T`\> | `output`<`T`\> _extends_ `string` ? `string` : `never`)\[\], `options`?: `Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\], `batchOptions`?: `object`): `Promise`<`string`\[\]\>

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

`inputs`

(`input`<`T`\> | `output`<`T`\> _extends_ `string` ? `string` : `never`)\[\]

`options?`

`Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\]

`batchOptions?`

`object`

`batchOptions.maxConcurrency?`

`number`

#### Returns[](#returns-7 "Direct link to Returns")

`Promise`<`string`\[\]\>

#### Inherited from[](#inherited-from-15 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[batch](/docs/api/base_language/classes/BaseLangChain#batch)

#### Defined in[](#defined-in-22 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:63](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L63)

### bind()[](#bind "Direct link to bind()")

> **bind**(`kwargs`: `Partial`<`BaseCallbackConfig`\>): [`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<`input`<`T`\> | `output`<`T`\> _extends_ `string` ? `string` : `never`, `string`, `BaseCallbackConfig`\>

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

`kwargs`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-8 "Direct link to Returns")

[`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<`input`<`T`\> | `output`<`T`\> _extends_ `string` ? `string` : `never`, `string`, `BaseCallbackConfig`\>

#### Inherited from[](#inherited-from-16 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[bind](/docs/api/base_language/classes/BaseLangChain#bind)

#### Defined in[](#defined-in-23 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:41](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L41)

### call()[](#call "Direct link to call()")

> **call**(`arg`: `input`<`T`\> | `output`<`T`\> _extends_ `string` ? `string` : `never`, `configArg`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`, `tags`?: `string`\[\]): `Promise`<`string`\>

#### Parameters[](#parameters-5 "Direct link to Parameters")

Parameter

Type

Description

`arg`

`input`<`T`\> | `output`<`T`\> _extends_ `string` ? `string` : `never`

\-

`configArg?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`

\-

`tags?`

`string`\[\]

`Deprecated`  
  

#### Returns[](#returns-9 "Direct link to Returns")

`Promise`<`string`\>

#### Defined in[](#defined-in-24 "Direct link to Defined in")

[langchain/src/tools/base.ts:45](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/base.ts#L45)

### invoke()[](#invoke "Direct link to invoke()")

> **invoke**(`input`: `input`<`T`\> | `output`<`T`\> _extends_ `string` ? `string` : `never`, `config`?: `BaseCallbackConfig`): `Promise`<`string`\>

#### Parameters[](#parameters-6 "Direct link to Parameters")

Parameter

Type

`input`

`input`<`T`\> | `output`<`T`\> _extends_ `string` ? `string` : `never`

`config?`

`BaseCallbackConfig`

#### Returns[](#returns-10 "Direct link to Returns")

`Promise`<`string`\>

#### Overrides[](#overrides-3 "Direct link to Overrides")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[invoke](/docs/api/base_language/classes/BaseLangChain#invoke)

#### Defined in[](#defined-in-25 "Direct link to Defined in")

[langchain/src/tools/base.ts:38](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/base.ts#L38)

### pipe()[](#pipe "Direct link to pipe()")

> **pipe**<NewRunOutput\>(`coerceable`: [`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<`string`, `NewRunOutput`\>): [`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<`input`<`T`\> | `output`<`T`\> _extends_ `string` ? `string` : `never`, `NewRunOutput`\>

#### Type parameters[](#type-parameters-2 "Direct link to Type parameters")

*   `NewRunOutput`

#### Parameters[](#parameters-7 "Direct link to Parameters")

Parameter

Type

`coerceable`

[`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<`string`, `NewRunOutput`\>

#### Returns[](#returns-11 "Direct link to Returns")

[`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<`input`<`T`\> | `output`<`T`\> _extends_ `string` ? `string` : `never`, `NewRunOutput`\>

#### Inherited from[](#inherited-from-17 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[pipe](/docs/api/base_language/classes/BaseLangChain#pipe)

#### Defined in[](#defined-in-26 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:153](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L153)

### stream()[](#stream "Direct link to stream()")

> **stream**(`input`: `input`<`T`\> | `output`<`T`\> _extends_ `string` ? `string` : `never`, `options`?: `Partial`<`BaseCallbackConfig`\>): `Promise`<`IterableReadableStream`<`string`\>\>

#### Parameters[](#parameters-8 "Direct link to Parameters")

Parameter

Type

`input`

`input`<`T`\> | `output`<`T`\> _extends_ `string` ? `string` : `never`

`options?`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-12 "Direct link to Returns")

`Promise`<`IterableReadableStream`<`string`\>\>

#### Inherited from[](#inherited-from-18 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[stream](/docs/api/base_language/classes/BaseLangChain#stream)

#### Defined in[](#defined-in-27 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:93](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L93)

### toJSON()[](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[](#returns-13 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[](#inherited-from-19 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[toJSON](/docs/api/base_language/classes/BaseLangChain#tojson)

#### Defined in[](#defined-in-28 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[](#returns-14 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[](#inherited-from-20 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[toJSONNotImplemented](/docs/api/base_language/classes/BaseLangChain#tojsonnotimplemented)

#### Defined in[](#defined-in-29 "Direct link to Defined in")

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

#### Inherited from[](#inherited-from-21 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[isRunnable](/docs/api/base_language/classes/BaseLangChain#isrunnable)

#### Defined in[](#defined-in-30 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:164](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L164)

### \_call()[](#_call "Direct link to _call")

> `Protected` `Abstract` **\_call**(`arg`: `output`<`T`\>, `runManager`?: [`CallbackManagerForToolRun`](/docs/api/callbacks/classes/CallbackManagerForToolRun)): `Promise`<`string`\>

#### Parameters[](#parameters-10 "Direct link to Parameters")

Parameter

Type

`arg`

`output`<`T`\>

`runManager?`

[`CallbackManagerForToolRun`](/docs/api/callbacks/classes/CallbackManagerForToolRun)

#### Returns[](#returns-16 "Direct link to Returns")

`Promise`<`string`\>

#### Defined in[](#defined-in-31 "Direct link to Defined in")

[langchain/src/tools/base.ts:33](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/base.ts#L33)

### \_callWithConfig()[](#_callwithconfig "Direct link to _callwithconfig")

> `Protected` **\_callWithConfig**<T\>(`func`: `Function`, `input`: `T`, `options`?: `BaseCallbackConfig` & {`runType`?: `string`;}): `Promise`<`string`\>

#### Type parameters[](#type-parameters-3 "Direct link to Type parameters")

*   `T` _extends_ `string` | {}

#### Parameters[](#parameters-11 "Direct link to Parameters")

Parameter

Type

`func`

(`input`: `T`) => `Promise`<`string`\>

`input`

`T`

`options?`

`BaseCallbackConfig` & {`runType`?: `string`;}

#### Returns[](#returns-17 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[](#inherited-from-22 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[\_callWithConfig](/docs/api/base_language/classes/BaseLangChain#_callwithconfig)

#### Defined in[](#defined-in-32 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:117](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L117)

### \_getOptionsList()[](#_getoptionslist "Direct link to _getoptionslist")

> `Protected` **\_getOptionsList**(`options`: `Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\], `length`: `number` = `0`): `Partial`<`BaseCallbackConfig`\>\[\]

#### Parameters[](#parameters-12 "Direct link to Parameters")

Parameter

Type

Default value

`options`

`Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\]

`undefined`

`length`

`number`

`0`

#### Returns[](#returns-18 "Direct link to Returns")

`Partial`<`BaseCallbackConfig`\>\[\]

#### Inherited from[](#inherited-from-23 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[\_getOptionsList](/docs/api/base_language/classes/BaseLangChain#_getoptionslist)

#### Defined in[](#defined-in-33 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L48)

### \_separateRunnableConfigFromCallOptions()[](#_separaterunnableconfigfromcalloptions "Direct link to _separaterunnableconfigfromcalloptions")

> `Protected` **\_separateRunnableConfigFromCallOptions**(`options`: `Partial`<`BaseCallbackConfig`\> = `{}`): \[`BaseCallbackConfig`, `Omit`<`Partial`<`BaseCallbackConfig`\>, _keyof_ `BaseCallbackConfig`\>\]

#### Parameters[](#parameters-13 "Direct link to Parameters")

Parameter

Type

`options`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-19 "Direct link to Returns")

\[`BaseCallbackConfig`, `Omit`<`Partial`<`BaseCallbackConfig`\>, _keyof_ `BaseCallbackConfig`\>\]

#### Inherited from[](#inherited-from-24 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[\_separateRunnableConfigFromCallOptions](/docs/api/base_language/classes/BaseLangChain#_separaterunnableconfigfromcalloptions)

#### Defined in[](#defined-in-34 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:102](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L102)