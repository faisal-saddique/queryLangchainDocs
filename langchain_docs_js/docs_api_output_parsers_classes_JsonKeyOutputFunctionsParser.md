JsonKeyOutputFunctionsParser<T\>
================================

Type parameters[](#type-parameters "Direct link to Type parameters")
---------------------------------------------------------------------

*   `T` = `object`

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseLLMOutputParser`](/docs/api/schema_output_parser/classes/BaseLLMOutputParser)<`T`\>.**JsonKeyOutputFunctionsParser**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new JsonKeyOutputFunctionsParser**<T\>(`fields`: `object`): [`JsonKeyOutputFunctionsParser`](/docs/api/output_parsers/classes/JsonKeyOutputFunctionsParser)<`T`\>

#### Type parameters[](#type-parameters-1 "Direct link to Type parameters")

*   `T` = `object`

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`fields`

`object`

`fields.attrName`

`string`

#### Returns[](#returns "Direct link to Returns")

[`JsonKeyOutputFunctionsParser`](/docs/api/output_parsers/classes/JsonKeyOutputFunctionsParser)<`T`\>

#### Overrides[](#overrides "Direct link to Overrides")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[constructor](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/output\_parsers/openai\_functions.ts:95](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/output_parsers/openai_functions.ts#L95)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### attrName[](#attrname "Direct link to attrName")

> **attrName**: `string`

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/output\_parsers/openai\_functions.ts:93](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/output_parsers/openai_functions.ts#L93)

### lc\_kwargs[](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[lc\_kwargs](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#lc_kwargs)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L57)

### lc\_namespace[](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Overrides[](#overrides-1 "Direct link to Overrides")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[lc\_namespace](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#lc_namespace)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/output\_parsers/openai\_functions.ts:87](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/output_parsers/openai_functions.ts#L87)

### lc\_serializable[](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `true`

#### Overrides[](#overrides-2 "Direct link to Overrides")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[lc\_serializable](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#lc_serializable)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/output\_parsers/openai\_functions.ts:89](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/output_parsers/openai_functions.ts#L89)

### outputParser[](#outputparser "Direct link to outputParser")

> **outputParser**: [`JsonOutputFunctionsParser`](/docs/api/output_parsers/classes/JsonOutputFunctionsParser)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/output\_parsers/openai\_functions.ts:91](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/output_parsers/openai_functions.ts#L91)

### lc\_runnable[](#lc_runnable "Direct link to lc_runnable")

> `Protected` **lc\_runnable**: `boolean` = `true`

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[lc\_runnable](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#lc_runnable)

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

BaseLLMOutputParser.lc\_aliases

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[lc\_aliases](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#lc_aliases)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

### lc\_attributes[](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[](#returns-2 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

BaseLLMOutputParser.lc\_attributes

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L80)

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[lc\_attributes](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#lc_attributes)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L80)

### lc\_secrets[](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

BaseLLMOutputParser.lc\_secrets

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[lc\_secrets](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#lc_secrets)

#### Defined in[](#defined-in-12 "Direct link to Defined in")

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

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[\_patchConfig](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#_patchconfig)

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:146](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L146)

### \_streamIterator()[](#_streamiterator "Direct link to _streamiterator")

> **\_streamIterator**(`input`: `string` | [`BaseMessage`](/docs/api/schema/classes/BaseMessage), `options`?: `Partial`<`BaseCallbackConfig`\>): `AsyncGenerator`<`T`, `any`, `unknown`\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`input`

`string` | [`BaseMessage`](/docs/api/schema/classes/BaseMessage)

`options?`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-5 "Direct link to Returns")

`AsyncGenerator`<`T`, `any`, `unknown`\>

#### Inherited from[](#inherited-from-9 "Direct link to Inherited from")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[\_streamIterator](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#_streamiterator)

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:86](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L86)

### batch()[](#batch "Direct link to batch()")

> **batch**(`inputs`: (`string` | [`BaseMessage`](/docs/api/schema/classes/BaseMessage))\[\], `options`?: `Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\], `batchOptions`?: `object`): `Promise`<`T`\[\]\>

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

#### Returns[](#returns-6 "Direct link to Returns")

`Promise`<`T`\[\]\>

#### Inherited from[](#inherited-from-10 "Direct link to Inherited from")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[batch](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#batch)

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:63](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L63)

### bind()[](#bind "Direct link to bind()")

> **bind**(`kwargs`: `Partial`<`BaseCallbackConfig`\>): [`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<`string` | [`BaseMessage`](/docs/api/schema/classes/BaseMessage), `T`, `BaseCallbackConfig`\>

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

`kwargs`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-7 "Direct link to Returns")

[`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<`string` | [`BaseMessage`](/docs/api/schema/classes/BaseMessage), `T`, `BaseCallbackConfig`\>

#### Inherited from[](#inherited-from-11 "Direct link to Inherited from")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[bind](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#bind)

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:41](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L41)

### invoke()[](#invoke "Direct link to invoke()")

> **invoke**(`input`: `string` | [`BaseMessage`](/docs/api/schema/classes/BaseMessage), `options`?: `BaseCallbackConfig`): `Promise`<`T`\>

#### Parameters[](#parameters-5 "Direct link to Parameters")

Parameter

Type

`input`

`string` | [`BaseMessage`](/docs/api/schema/classes/BaseMessage)

`options?`

`BaseCallbackConfig`

#### Returns[](#returns-8 "Direct link to Returns")

`Promise`<`T`\>

#### Inherited from[](#inherited-from-12 "Direct link to Inherited from")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[invoke](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#invoke)

#### Defined in[](#defined-in-17 "Direct link to Defined in")

[langchain/src/schema/output\_parser.ts:32](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/output_parser.ts#L32)

### parseResult()[](#parseresult "Direct link to parseResult()")

> **parseResult**(`generations`: [`Generation`](/docs/api/schema/interfaces/Generation)\[\] | [`ChatGeneration`](/docs/api/schema/interfaces/ChatGeneration)\[\]): `Promise`<`T`\>

#### Parameters[](#parameters-6 "Direct link to Parameters")

Parameter

Type

`generations`

[`Generation`](/docs/api/schema/interfaces/Generation)\[\] | [`ChatGeneration`](/docs/api/schema/interfaces/ChatGeneration)\[\]

#### Returns[](#returns-9 "Direct link to Returns")

`Promise`<`T`\>

#### Overrides[](#overrides-3 "Direct link to Overrides")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[parseResult](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#parseresult)

#### Defined in[](#defined-in-18 "Direct link to Defined in")

[langchain/src/output\_parsers/openai\_functions.ts:100](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/output_parsers/openai_functions.ts#L100)

### parseResultWithPrompt()[](#parseresultwithprompt "Direct link to parseResultWithPrompt()")

> **parseResultWithPrompt**(`generations`: [`Generation`](/docs/api/schema/interfaces/Generation)\[\] | [`ChatGeneration`](/docs/api/schema/interfaces/ChatGeneration)\[\], `_prompt`: [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`T`\>

#### Parameters[](#parameters-7 "Direct link to Parameters")

Parameter

Type

`generations`

[`Generation`](/docs/api/schema/interfaces/Generation)\[\] | [`ChatGeneration`](/docs/api/schema/interfaces/ChatGeneration)\[\]

`_prompt`

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-10 "Direct link to Returns")

`Promise`<`T`\>

#### Inherited from[](#inherited-from-13 "Direct link to Inherited from")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[parseResultWithPrompt](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#parseresultwithprompt)

#### Defined in[](#defined-in-19 "Direct link to Defined in")

[langchain/src/schema/output\_parser.ts:24](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/output_parser.ts#L24)

### pipe()[](#pipe "Direct link to pipe()")

> **pipe**<NewRunOutput\>(`coerceable`: [`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<`T`, `NewRunOutput`\>): [`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<`string` | [`BaseMessage`](/docs/api/schema/classes/BaseMessage), `NewRunOutput`\>

#### Type parameters[](#type-parameters-2 "Direct link to Type parameters")

*   `NewRunOutput`

#### Parameters[](#parameters-8 "Direct link to Parameters")

Parameter

Type

`coerceable`

[`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<`T`, `NewRunOutput`\>

#### Returns[](#returns-11 "Direct link to Returns")

[`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<`string` | [`BaseMessage`](/docs/api/schema/classes/BaseMessage), `NewRunOutput`\>

#### Inherited from[](#inherited-from-14 "Direct link to Inherited from")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[pipe](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#pipe)

#### Defined in[](#defined-in-20 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:153](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L153)

### stream()[](#stream "Direct link to stream()")

> **stream**(`input`: `string` | [`BaseMessage`](/docs/api/schema/classes/BaseMessage), `options`?: `Partial`<`BaseCallbackConfig`\>): `Promise`<`IterableReadableStream`<`T`\>\>

#### Parameters[](#parameters-9 "Direct link to Parameters")

Parameter

Type

`input`

`string` | [`BaseMessage`](/docs/api/schema/classes/BaseMessage)

`options?`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-12 "Direct link to Returns")

`Promise`<`IterableReadableStream`<`T`\>\>

#### Inherited from[](#inherited-from-15 "Direct link to Inherited from")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[stream](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#stream)

#### Defined in[](#defined-in-21 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:93](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L93)

### toJSON()[](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[](#returns-13 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[](#inherited-from-16 "Direct link to Inherited from")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[toJSON](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#tojson)

#### Defined in[](#defined-in-22 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[](#returns-14 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[](#inherited-from-17 "Direct link to Inherited from")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[toJSONNotImplemented](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#tojsonnotimplemented)

#### Defined in[](#defined-in-23 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L151)

### isRunnable()[](#isrunnable "Direct link to isRunnable()")

> `Static` **isRunnable**(`thing`: `any`): thing is Runnable<any, any, BaseCallbackConfig\>

#### Parameters[](#parameters-10 "Direct link to Parameters")

Parameter

Type

`thing`

`any`

#### Returns[](#returns-15 "Direct link to Returns")

thing is Runnable<any, any, BaseCallbackConfig\>

#### Inherited from[](#inherited-from-18 "Direct link to Inherited from")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[isRunnable](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#isrunnable)

#### Defined in[](#defined-in-24 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:164](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L164)

### \_callWithConfig()[](#_callwithconfig "Direct link to _callwithconfig")

> `Protected` **\_callWithConfig**<T\>(`func`: `Function`, `input`: `T`, `options`?: `BaseCallbackConfig` & {`runType`?: `string`;}): `Promise`<`T`\>

#### Type parameters[](#type-parameters-3 "Direct link to Type parameters")

*   `T` _extends_ `string` | [`BaseMessage`](/docs/api/schema/classes/BaseMessage)

#### Parameters[](#parameters-11 "Direct link to Parameters")

Parameter

Type

`func`

(`input`: `T`) => `Promise`<`T`\>

`input`

`T`

`options?`

`BaseCallbackConfig` & {`runType`?: `string`;}

#### Returns[](#returns-16 "Direct link to Returns")

`Promise`<`T`\>

#### Inherited from[](#inherited-from-19 "Direct link to Inherited from")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[\_callWithConfig](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#_callwithconfig)

#### Defined in[](#defined-in-25 "Direct link to Defined in")

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

#### Returns[](#returns-17 "Direct link to Returns")

`Partial`<`BaseCallbackConfig`\>\[\]

#### Inherited from[](#inherited-from-20 "Direct link to Inherited from")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[\_getOptionsList](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#_getoptionslist)

#### Defined in[](#defined-in-26 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L48)

### \_separateRunnableConfigFromCallOptions()[](#_separaterunnableconfigfromcalloptions "Direct link to _separaterunnableconfigfromcalloptions")

> `Protected` **\_separateRunnableConfigFromCallOptions**(`options`: `Partial`<`BaseCallbackConfig`\> = `{}`): \[`BaseCallbackConfig`, `Omit`<`Partial`<`BaseCallbackConfig`\>, _keyof_ `BaseCallbackConfig`\>\]

#### Parameters[](#parameters-13 "Direct link to Parameters")

Parameter

Type

`options`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-18 "Direct link to Returns")

\[`BaseCallbackConfig`, `Omit`<`Partial`<`BaseCallbackConfig`\>, _keyof_ `BaseCallbackConfig`\>\]

#### Inherited from[](#inherited-from-21 "Direct link to Inherited from")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[\_separateRunnableConfigFromCallOptions](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#_separaterunnableconfigfromcalloptions)

#### Defined in[](#defined-in-27 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:102](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L102)