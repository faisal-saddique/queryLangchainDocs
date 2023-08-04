CustomListOutputParser
======================

Class to parse the output of an LLM call to a list with a specific length and separator.

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`ListOutputParser`](/docs/api/output_parsers/classes/ListOutputParser).**CustomListOutputParser**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new CustomListOutputParser**(«destructured»: `object`): [`CustomListOutputParser`](/docs/api/output_parsers/classes/CustomListOutputParser)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`«destructured»`

`object`

› `length?`

`number`

› `separator?`

`string`

#### Returns[](#returns "Direct link to Returns")

[`CustomListOutputParser`](/docs/api/output_parsers/classes/CustomListOutputParser)

#### Overrides[](#overrides "Direct link to Overrides")

[ListOutputParser](/docs/api/output_parsers/classes/ListOutputParser).[constructor](/docs/api/output_parsers/classes/ListOutputParser#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/output\_parsers/list.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/output_parsers/list.ts#L48)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### lc\_kwargs[](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[ListOutputParser](/docs/api/output_parsers/classes/ListOutputParser).[lc\_kwargs](/docs/api/output_parsers/classes/ListOutputParser#lc_kwargs)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L57)

### lc\_namespace[](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Overrides[](#overrides-1 "Direct link to Overrides")

[ListOutputParser](/docs/api/output_parsers/classes/ListOutputParser).[lc\_namespace](/docs/api/output_parsers/classes/ListOutputParser#lc_namespace)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/output\_parsers/list.ts:42](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/output_parsers/list.ts#L42)

### lc\_serializable[](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[ListOutputParser](/docs/api/output_parsers/classes/ListOutputParser).[lc\_serializable](/docs/api/output_parsers/classes/ListOutputParser#lc_serializable)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L55)

### lc\_runnable[](#lc_runnable "Direct link to lc_runnable")

> `Protected` **lc\_runnable**: `boolean` = `true`

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[ListOutputParser](/docs/api/output_parsers/classes/ListOutputParser).[lc\_runnable](/docs/api/output_parsers/classes/ListOutputParser#lc_runnable)

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

ListOutputParser.lc\_aliases

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[ListOutputParser](/docs/api/output_parsers/classes/ListOutputParser).[lc\_aliases](/docs/api/output_parsers/classes/ListOutputParser#lc_aliases)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

### lc\_attributes[](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[](#returns-2 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

ListOutputParser.lc\_attributes

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L80)

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[ListOutputParser](/docs/api/output_parsers/classes/ListOutputParser).[lc\_attributes](/docs/api/output_parsers/classes/ListOutputParser#lc_attributes)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L80)

### lc\_secrets[](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

ListOutputParser.lc\_secrets

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

[ListOutputParser](/docs/api/output_parsers/classes/ListOutputParser).[lc\_secrets](/docs/api/output_parsers/classes/ListOutputParser#lc_secrets)

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

[ListOutputParser](/docs/api/output_parsers/classes/ListOutputParser).[\_patchConfig](/docs/api/output_parsers/classes/ListOutputParser#_patchconfig)

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:146](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L146)

### \_streamIterator()[](#_streamiterator "Direct link to _streamiterator")

> **\_streamIterator**(`input`: `string` | [`BaseMessage`](/docs/api/schema/classes/BaseMessage), `options`?: `Partial`<`BaseCallbackConfig`\>): `AsyncGenerator`<`string`\[\], `any`, `unknown`\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`input`

`string` | [`BaseMessage`](/docs/api/schema/classes/BaseMessage)

`options?`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-5 "Direct link to Returns")

`AsyncGenerator`<`string`\[\], `any`, `unknown`\>

#### Inherited from[](#inherited-from-10 "Direct link to Inherited from")

[ListOutputParser](/docs/api/output_parsers/classes/ListOutputParser).[\_streamIterator](/docs/api/output_parsers/classes/ListOutputParser#_streamiterator)

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:86](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L86)

### \_type()[](#_type "Direct link to _type")

Return the string type key uniquely identifying this class of parser

> **\_type**(): `string`

#### Returns[](#returns-6 "Direct link to Returns")

`string`

#### Inherited from[](#inherited-from-11 "Direct link to Inherited from")

[ListOutputParser](/docs/api/output_parsers/classes/ListOutputParser).[\_type](/docs/api/output_parsers/classes/ListOutputParser#_type)

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/schema/output\_parser.ts:99](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/output_parser.ts#L99)

### batch()[](#batch "Direct link to batch()")

> **batch**(`inputs`: (`string` | [`BaseMessage`](/docs/api/schema/classes/BaseMessage))\[\], `options`?: `Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\], `batchOptions`?: `object`): `Promise`<`string`\[\]\[\]\>

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

`inputs`

(`string` | [`BaseMessage`](/docs/api/schema/classes/BaseMessage))\[\]

`options?`

`Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\]

`batchOptions?`

`object`

`batchOptions.maxConcurrency?`

`number`

#### Returns[](#returns-7 "Direct link to Returns")

`Promise`<`string`\[\]\[\]\>

#### Inherited from[](#inherited-from-12 "Direct link to Inherited from")

[ListOutputParser](/docs/api/output_parsers/classes/ListOutputParser).[batch](/docs/api/output_parsers/classes/ListOutputParser#batch)

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:63](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L63)

### bind()[](#bind "Direct link to bind()")

> **bind**(`kwargs`: `Partial`<`BaseCallbackConfig`\>): [`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<`string` | [`BaseMessage`](/docs/api/schema/classes/BaseMessage), `string`\[\], `BaseCallbackConfig`\>

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

`kwargs`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-8 "Direct link to Returns")

[`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<`string` | [`BaseMessage`](/docs/api/schema/classes/BaseMessage), `string`\[\], `BaseCallbackConfig`\>

#### Inherited from[](#inherited-from-13 "Direct link to Inherited from")

[ListOutputParser](/docs/api/output_parsers/classes/ListOutputParser).[bind](/docs/api/output_parsers/classes/ListOutputParser#bind)

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:41](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L41)

### getFormatInstructions()[](#getformatinstructions "Direct link to getFormatInstructions()")

Return a string describing the format of the output.

#### Example[](#example "Direct link to Example")

    {  "foo": "bar"}

> **getFormatInstructions**(): `string`

#### Returns[](#returns-9 "Direct link to Returns")

`string`

Format instructions.

#### Overrides[](#overrides-2 "Direct link to Overrides")

[ListOutputParser](/docs/api/output_parsers/classes/ListOutputParser).[getFormatInstructions](/docs/api/output_parsers/classes/ListOutputParser#getformatinstructions)

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/output\_parsers/list.ts:74](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/output_parsers/list.ts#L74)

### invoke()[](#invoke "Direct link to invoke()")

> **invoke**(`input`: `string` | [`BaseMessage`](/docs/api/schema/classes/BaseMessage), `options`?: `BaseCallbackConfig`): `Promise`<`string`\[\]\>

#### Parameters[](#parameters-5 "Direct link to Parameters")

Parameter

Type

`input`

`string` | [`BaseMessage`](/docs/api/schema/classes/BaseMessage)

`options?`

`BaseCallbackConfig`

#### Returns[](#returns-10 "Direct link to Returns")

`Promise`<`string`\[\]\>

#### Inherited from[](#inherited-from-14 "Direct link to Inherited from")

[ListOutputParser](/docs/api/output_parsers/classes/ListOutputParser).[invoke](/docs/api/output_parsers/classes/ListOutputParser#invoke)

#### Defined in[](#defined-in-17 "Direct link to Defined in")

[langchain/src/schema/output\_parser.ts:32](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/output_parser.ts#L32)

### parse()[](#parse "Direct link to parse()")

Parse the output of an LLM call.

> **parse**(`text`: `string`): `Promise`<`string`\[\]\>

#### Parameters[](#parameters-6 "Direct link to Parameters")

Parameter

Type

Description

`text`

`string`

LLM output to parse.

#### Returns[](#returns-11 "Direct link to Returns")

`Promise`<`string`\[\]\>

Parsed output.

#### Overrides[](#overrides-3 "Direct link to Overrides")

[ListOutputParser](/docs/api/output_parsers/classes/ListOutputParser).[parse](/docs/api/output_parsers/classes/ListOutputParser#parse)

#### Defined in[](#defined-in-18 "Direct link to Defined in")

[langchain/src/output\_parsers/list.ts:54](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/output_parsers/list.ts#L54)

### parseResult()[](#parseresult "Direct link to parseResult()")

> **parseResult**(`generations`: [`Generation`](/docs/api/schema/interfaces/Generation)\[\] | [`ChatGeneration`](/docs/api/schema/interfaces/ChatGeneration)\[\], `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\[\]\>

#### Parameters[](#parameters-7 "Direct link to Parameters")

Parameter

Type

`generations`

[`Generation`](/docs/api/schema/interfaces/Generation)\[\] | [`ChatGeneration`](/docs/api/schema/interfaces/ChatGeneration)\[\]

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-12 "Direct link to Returns")

`Promise`<`string`\[\]\>

#### Inherited from[](#inherited-from-15 "Direct link to Inherited from")

[ListOutputParser](/docs/api/output_parsers/classes/ListOutputParser).[parseResult](/docs/api/output_parsers/classes/ListOutputParser#parseresult)

#### Defined in[](#defined-in-19 "Direct link to Defined in")

[langchain/src/schema/output\_parser.ts:60](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/output_parser.ts#L60)

### parseResultWithPrompt()[](#parseresultwithprompt "Direct link to parseResultWithPrompt()")

> **parseResultWithPrompt**(`generations`: [`Generation`](/docs/api/schema/interfaces/Generation)\[\] | [`ChatGeneration`](/docs/api/schema/interfaces/ChatGeneration)\[\], `_prompt`: [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\[\]\>

#### Parameters[](#parameters-8 "Direct link to Parameters")

Parameter

Type

`generations`

[`Generation`](/docs/api/schema/interfaces/Generation)\[\] | [`ChatGeneration`](/docs/api/schema/interfaces/ChatGeneration)\[\]

`_prompt`

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-13 "Direct link to Returns")

`Promise`<`string`\[\]\>

#### Inherited from[](#inherited-from-16 "Direct link to Inherited from")

[ListOutputParser](/docs/api/output_parsers/classes/ListOutputParser).[parseResultWithPrompt](/docs/api/output_parsers/classes/ListOutputParser#parseresultwithprompt)

#### Defined in[](#defined-in-20 "Direct link to Defined in")

[langchain/src/schema/output\_parser.ts:24](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/output_parser.ts#L24)

### parseWithPrompt()[](#parsewithprompt "Direct link to parseWithPrompt()")

> **parseWithPrompt**(`text`: `string`, `_prompt`: [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\[\]\>

#### Parameters[](#parameters-9 "Direct link to Parameters")

Parameter

Type

`text`

`string`

`_prompt`

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-14 "Direct link to Returns")

`Promise`<`string`\[\]\>

#### Inherited from[](#inherited-from-17 "Direct link to Inherited from")

[ListOutputParser](/docs/api/output_parsers/classes/ListOutputParser).[parseWithPrompt](/docs/api/output_parsers/classes/ListOutputParser#parsewithprompt)

#### Defined in[](#defined-in-21 "Direct link to Defined in")

[langchain/src/schema/output\_parser.ts:75](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/output_parser.ts#L75)

### pipe()[](#pipe "Direct link to pipe()")

> **pipe**<NewRunOutput\>(`coerceable`: [`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<`string`\[\], `NewRunOutput`\>): [`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<`string` | [`BaseMessage`](/docs/api/schema/classes/BaseMessage), `NewRunOutput`\>

#### Type parameters[](#type-parameters "Direct link to Type parameters")

*   `NewRunOutput`

#### Parameters[](#parameters-10 "Direct link to Parameters")

Parameter

Type

`coerceable`

[`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<`string`\[\], `NewRunOutput`\>

#### Returns[](#returns-15 "Direct link to Returns")

[`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<`string` | [`BaseMessage`](/docs/api/schema/classes/BaseMessage), `NewRunOutput`\>

#### Inherited from[](#inherited-from-18 "Direct link to Inherited from")

[ListOutputParser](/docs/api/output_parsers/classes/ListOutputParser).[pipe](/docs/api/output_parsers/classes/ListOutputParser#pipe)

#### Defined in[](#defined-in-22 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:153](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L153)

### stream()[](#stream "Direct link to stream()")

> **stream**(`input`: `string` | [`BaseMessage`](/docs/api/schema/classes/BaseMessage), `options`?: `Partial`<`BaseCallbackConfig`\>): `Promise`<`IterableReadableStream`<`string`\[\]\>\>

#### Parameters[](#parameters-11 "Direct link to Parameters")

Parameter

Type

`input`

`string` | [`BaseMessage`](/docs/api/schema/classes/BaseMessage)

`options?`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-16 "Direct link to Returns")

`Promise`<`IterableReadableStream`<`string`\[\]\>\>

#### Inherited from[](#inherited-from-19 "Direct link to Inherited from")

[ListOutputParser](/docs/api/output_parsers/classes/ListOutputParser).[stream](/docs/api/output_parsers/classes/ListOutputParser#stream)

#### Defined in[](#defined-in-23 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:93](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L93)

### toJSON()[](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[](#returns-17 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[](#inherited-from-20 "Direct link to Inherited from")

[ListOutputParser](/docs/api/output_parsers/classes/ListOutputParser).[toJSON](/docs/api/output_parsers/classes/ListOutputParser#tojson)

#### Defined in[](#defined-in-24 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[](#returns-18 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[](#inherited-from-21 "Direct link to Inherited from")

[ListOutputParser](/docs/api/output_parsers/classes/ListOutputParser).[toJSONNotImplemented](/docs/api/output_parsers/classes/ListOutputParser#tojsonnotimplemented)

#### Defined in[](#defined-in-25 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L151)

### isRunnable()[](#isrunnable "Direct link to isRunnable()")

> `Static` **isRunnable**(`thing`: `any`): thing is Runnable<any, any, BaseCallbackConfig\>

#### Parameters[](#parameters-12 "Direct link to Parameters")

Parameter

Type

`thing`

`any`

#### Returns[](#returns-19 "Direct link to Returns")

thing is Runnable<any, any, BaseCallbackConfig\>

#### Inherited from[](#inherited-from-22 "Direct link to Inherited from")

[ListOutputParser](/docs/api/output_parsers/classes/ListOutputParser).[isRunnable](/docs/api/output_parsers/classes/ListOutputParser#isrunnable)

#### Defined in[](#defined-in-26 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:164](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L164)

### \_callWithConfig()[](#_callwithconfig "Direct link to _callwithconfig")

> `Protected` **\_callWithConfig**<T\>(`func`: `Function`, `input`: `T`, `options`?: `BaseCallbackConfig` & {`runType`?: `string`;}): `Promise`<`string`\[\]\>

#### Type parameters[](#type-parameters-1 "Direct link to Type parameters")

*   `T` _extends_ `string` | [`BaseMessage`](/docs/api/schema/classes/BaseMessage)

#### Parameters[](#parameters-13 "Direct link to Parameters")

Parameter

Type

`func`

(`input`: `T`) => `Promise`<`string`\[\]\>

`input`

`T`

`options?`

`BaseCallbackConfig` & {`runType`?: `string`;}

#### Returns[](#returns-20 "Direct link to Returns")

`Promise`<`string`\[\]\>

#### Inherited from[](#inherited-from-23 "Direct link to Inherited from")

[ListOutputParser](/docs/api/output_parsers/classes/ListOutputParser).[\_callWithConfig](/docs/api/output_parsers/classes/ListOutputParser#_callwithconfig)

#### Defined in[](#defined-in-27 "Direct link to Defined in")

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

#### Returns[](#returns-21 "Direct link to Returns")

`Partial`<`BaseCallbackConfig`\>\[\]

#### Inherited from[](#inherited-from-24 "Direct link to Inherited from")

[ListOutputParser](/docs/api/output_parsers/classes/ListOutputParser).[\_getOptionsList](/docs/api/output_parsers/classes/ListOutputParser#_getoptionslist)

#### Defined in[](#defined-in-28 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L48)

### \_separateRunnableConfigFromCallOptions()[](#_separaterunnableconfigfromcalloptions "Direct link to _separaterunnableconfigfromcalloptions")

> `Protected` **\_separateRunnableConfigFromCallOptions**(`options`: `Partial`<`BaseCallbackConfig`\> = `{}`): \[`BaseCallbackConfig`, `Omit`<`Partial`<`BaseCallbackConfig`\>, _keyof_ `BaseCallbackConfig`\>\]

#### Parameters[](#parameters-15 "Direct link to Parameters")

Parameter

Type

`options`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-22 "Direct link to Returns")

\[`BaseCallbackConfig`, `Omit`<`Partial`<`BaseCallbackConfig`\>, _keyof_ `BaseCallbackConfig`\>\]

#### Inherited from[](#inherited-from-25 "Direct link to Inherited from")

[ListOutputParser](/docs/api/output_parsers/classes/ListOutputParser).[\_separateRunnableConfigFromCallOptions](/docs/api/output_parsers/classes/ListOutputParser#_separaterunnableconfigfromcalloptions)

#### Defined in[](#defined-in-29 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:102](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L102)