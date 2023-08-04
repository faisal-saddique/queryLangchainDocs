BasePromptTemplate<FormattedOutput\>
====================================

Base class for prompt templates. Exposes a format method that returns a string prompt given a set of input values.

Type parameters[](#type-parameters "Direct link to Type parameters")
---------------------------------------------------------------------

*   `FormattedOutput` _extends_ [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue) = [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`Runnable`](/docs/api/schema_runnable/classes/Runnable)<[`InputValues`](/docs/api/schema/types/InputValues), `FormattedOutput`\>.**BasePromptTemplate**

Implements[](#implements "Direct link to Implements")
------------------------------------------------------

*   [`BasePromptTemplateInput`](/docs/api/prompts/interfaces/BasePromptTemplateInput)

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new BasePromptTemplate**<FormattedOutput\>(`input`: [`BasePromptTemplateInput`](/docs/api/prompts/interfaces/BasePromptTemplateInput)): [`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)<`FormattedOutput`\>

#### Type parameters[](#type-parameters-1 "Direct link to Type parameters")

*   `FormattedOutput` _extends_ [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)<`FormattedOutput`\> = [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`input`

[`BasePromptTemplateInput`](/docs/api/prompts/interfaces/BasePromptTemplateInput)

#### Returns[](#returns "Direct link to Returns")

[`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)<`FormattedOutput`\>

#### Overrides[](#overrides "Direct link to Overrides")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[constructor](/docs/api/schema_runnable/classes/Runnable#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/prompts/base.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/base.ts#L80)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### PromptValueReturnType[](#promptvaluereturntype "Direct link to PromptValueReturnType")

> **PromptValueReturnType**: `FormattedOutput`

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/prompts/base.ts:62](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/base.ts#L62)

### inputVariables[](#inputvariables "Direct link to inputVariables")

> **inputVariables**: `string`\[\]

A list of variable names the prompt template expects

#### Implementation of[](#implementation-of "Direct link to Implementation of")

[BasePromptTemplateInput](/docs/api/prompts/interfaces/BasePromptTemplateInput).[inputVariables](/docs/api/prompts/interfaces/BasePromptTemplateInput#inputvariables)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/prompts/base.ts:74](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/base.ts#L74)

### lc\_kwargs[](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[lc\_kwargs](/docs/api/schema_runnable/classes/Runnable#lc_kwargs)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L57)

### lc\_namespace[](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Overrides[](#overrides-1 "Direct link to Overrides")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[lc\_namespace](/docs/api/schema_runnable/classes/Runnable#lc_namespace)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/prompts/base.ts:66](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/base.ts#L66)

### lc\_serializable[](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `true`

#### Overrides[](#overrides-2 "Direct link to Overrides")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[lc\_serializable](/docs/api/schema_runnable/classes/Runnable#lc_serializable)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/prompts/base.ts:64](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/base.ts#L64)

### partialVariables[](#partialvariables "Direct link to partialVariables")

> **partialVariables**: [`InputValues`](/docs/api/schema/types/InputValues) = `{}`

Partial variables

#### Implementation of[](#implementation-of-1 "Direct link to Implementation of")

[BasePromptTemplateInput](/docs/api/prompts/interfaces/BasePromptTemplateInput).[partialVariables](/docs/api/prompts/interfaces/BasePromptTemplateInput#partialvariables)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/prompts/base.ts:78](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/base.ts#L78)

### outputParser?[](#outputparser "Direct link to outputParser?")

> **outputParser**: [`BaseOutputParser`](/docs/api/schema_output_parser/classes/BaseOutputParser)<`unknown`\>

How to parse the output of calling an LLM on this formatted prompt

#### Implementation of[](#implementation-of-2 "Direct link to Implementation of")

[BasePromptTemplateInput](/docs/api/prompts/interfaces/BasePromptTemplateInput).[outputParser](/docs/api/prompts/interfaces/BasePromptTemplateInput#outputparser)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/prompts/base.ts:76](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/base.ts#L76)

### lc\_runnable[](#lc_runnable "Direct link to lc_runnable")

> `Protected` **lc\_runnable**: `boolean` = `true`

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[lc\_runnable](/docs/api/schema_runnable/classes/Runnable#lc_runnable)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

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

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[lc\_aliases](/docs/api/schema_runnable/classes/Runnable#lc_aliases)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

### lc\_attributes[](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[](#returns-2 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Overrides[](#overrides-3 "Direct link to Overrides")

Runnable.lc\_attributes

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/prompts/base.ts:68](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/base.ts#L68)

#### Overrides[](#overrides-4 "Direct link to Overrides")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[lc\_attributes](/docs/api/schema_runnable/classes/Runnable#lc_attributes)

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/prompts/base.ts:68](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/base.ts#L68)

### lc\_secrets[](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

Runnable.lc\_secrets

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[lc\_secrets](/docs/api/schema_runnable/classes/Runnable#lc_secrets)

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### \_getPromptType()[](#_getprompttype "Direct link to _getprompttype")

Return the string type key uniquely identifying this class of prompt template.

> `Abstract` **\_getPromptType**(): `string`

#### Returns[](#returns-4 "Direct link to Returns")

`string`

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/prompts/base.ts:145](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/base.ts#L145)

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

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[\_patchConfig](/docs/api/schema_runnable/classes/Runnable#_patchconfig)

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:146](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L146)

### \_streamIterator()[](#_streamiterator "Direct link to _streamiterator")

> **\_streamIterator**(`input`: [`InputValues`](/docs/api/schema/types/InputValues), `options`?: `Partial`<`BaseCallbackConfig`\>): `AsyncGenerator`<`FormattedOutput`, `any`, `unknown`\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`input`

[`InputValues`](/docs/api/schema/types/InputValues)

`options?`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-6 "Direct link to Returns")

`AsyncGenerator`<`FormattedOutput`, `any`, `unknown`\>

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[\_streamIterator](/docs/api/schema_runnable/classes/Runnable#_streamiterator)

#### Defined in[](#defined-in-17 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:86](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L86)

### batch()[](#batch "Direct link to batch()")

> **batch**(`inputs`: [`InputValues`](/docs/api/schema/types/InputValues)\[\], `options`?: `Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\], `batchOptions`?: `object`): `Promise`<`FormattedOutput`\[\]\>

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

`inputs`

[`InputValues`](/docs/api/schema/types/InputValues)\[\]

`options?`

`Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\]

`batchOptions?`

`object`

`batchOptions.maxConcurrency?`

`number`

#### Returns[](#returns-7 "Direct link to Returns")

`Promise`<`FormattedOutput`\[\]\>

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[batch](/docs/api/schema_runnable/classes/Runnable#batch)

#### Defined in[](#defined-in-18 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:63](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L63)

### bind()[](#bind "Direct link to bind()")

> **bind**(`kwargs`: `Partial`<`BaseCallbackConfig`\>): [`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<[`InputValues`](/docs/api/schema/types/InputValues), `FormattedOutput`, `BaseCallbackConfig`\>

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

`kwargs`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-8 "Direct link to Returns")

[`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<[`InputValues`](/docs/api/schema/types/InputValues), `FormattedOutput`, `BaseCallbackConfig`\>

#### Inherited from[](#inherited-from-9 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[bind](/docs/api/schema_runnable/classes/Runnable#bind)

#### Defined in[](#defined-in-19 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:41](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L41)

### format()[](#format "Direct link to format()")

Format the prompt given the input values.

#### Example[](#example "Direct link to Example")

    prompt.format({ foo: "bar" });

> `Abstract` **format**(`values`: [`InputValues`](/docs/api/schema/types/InputValues)): `Promise`<`string`\>

#### Parameters[](#parameters-5 "Direct link to Parameters")

Parameter

Type

Description

`values`

[`InputValues`](/docs/api/schema/types/InputValues)

A dictionary of arguments to be passed to the prompt template.

#### Returns[](#returns-9 "Direct link to Returns")

`Promise`<`string`\>

A formatted prompt string.

#### Defined in[](#defined-in-20 "Direct link to Defined in")

[langchain/src/prompts/base.ts:133](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/base.ts#L133)

### formatPromptValue()[](#formatpromptvalue "Direct link to formatPromptValue()")

Format the prompt given the input values and return a formatted prompt value.

> `Abstract` **formatPromptValue**(`values`: [`InputValues`](/docs/api/schema/types/InputValues)): `Promise`<`FormattedOutput`\>

#### Parameters[](#parameters-6 "Direct link to Parameters")

Parameter

Type

`values`

[`InputValues`](/docs/api/schema/types/InputValues)

#### Returns[](#returns-10 "Direct link to Returns")

`Promise`<`FormattedOutput`\>

A formatted PromptValue.

#### Defined in[](#defined-in-21 "Direct link to Defined in")

[langchain/src/prompts/base.ts:140](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/base.ts#L140)

### invoke()[](#invoke "Direct link to invoke()")

> **invoke**(`input`: [`InputValues`](/docs/api/schema/types/InputValues), `options`?: `BaseCallbackConfig`): `Promise`<`FormattedOutput`\>

#### Parameters[](#parameters-7 "Direct link to Parameters")

Parameter

Type

`input`

[`InputValues`](/docs/api/schema/types/InputValues)

`options?`

`BaseCallbackConfig`

#### Returns[](#returns-11 "Direct link to Returns")

`Promise`<`FormattedOutput`\>

#### Overrides[](#overrides-5 "Direct link to Overrides")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[invoke](/docs/api/schema_runnable/classes/Runnable#invoke)

#### Defined in[](#defined-in-22 "Direct link to Defined in")

[langchain/src/prompts/base.ts:111](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/base.ts#L111)

### mergePartialAndUserVariables()[](#mergepartialanduservariables "Direct link to mergePartialAndUserVariables()")

> **mergePartialAndUserVariables**(`userVariables`: [`InputValues`](/docs/api/schema/types/InputValues)): `Promise`<[`InputValues`](/docs/api/schema/types/InputValues)\>

#### Parameters[](#parameters-8 "Direct link to Parameters")

Parameter

Type

`userVariables`

[`InputValues`](/docs/api/schema/types/InputValues)

#### Returns[](#returns-12 "Direct link to Returns")

`Promise`<[`InputValues`](/docs/api/schema/types/InputValues)\>

#### Defined in[](#defined-in-23 "Direct link to Defined in")

[langchain/src/prompts/base.ts:93](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/base.ts#L93)

### partial()[](#partial "Direct link to partial()")

> `Abstract` **partial**(`values`: [`PartialValues`](/docs/api/schema/types/PartialValues)): `Promise`<[`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)<[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\>\>

#### Parameters[](#parameters-9 "Direct link to Parameters")

Parameter

Type

`values`

[`PartialValues`](/docs/api/schema/types/PartialValues)

#### Returns[](#returns-13 "Direct link to Returns")

`Promise`<[`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)<[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\>\>

#### Defined in[](#defined-in-24 "Direct link to Defined in")

[langchain/src/prompts/base.ts:91](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/base.ts#L91)

### pipe()[](#pipe "Direct link to pipe()")

> **pipe**<NewRunOutput\>(`coerceable`: [`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<`FormattedOutput`, `NewRunOutput`\>): [`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<[`InputValues`](/docs/api/schema/types/InputValues), `NewRunOutput`\>

#### Type parameters[](#type-parameters-2 "Direct link to Type parameters")

*   `NewRunOutput`

#### Parameters[](#parameters-10 "Direct link to Parameters")

Parameter

Type

`coerceable`

[`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<`FormattedOutput`, `NewRunOutput`\>

#### Returns[](#returns-14 "Direct link to Returns")

[`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<[`InputValues`](/docs/api/schema/types/InputValues), `NewRunOutput`\>

#### Inherited from[](#inherited-from-10 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[pipe](/docs/api/schema_runnable/classes/Runnable#pipe)

#### Defined in[](#defined-in-25 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:153](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L153)

### serialize()[](#serialize "Direct link to serialize()")

Return a json-like object representing this prompt template.

#### Deprecated[](#deprecated "Direct link to Deprecated")

> **serialize**(): [`SerializedBasePromptTemplate`](/docs/api/prompts/types/SerializedBasePromptTemplate)

#### Returns[](#returns-15 "Direct link to Returns")

[`SerializedBasePromptTemplate`](/docs/api/prompts/types/SerializedBasePromptTemplate)

#### Defined in[](#defined-in-26 "Direct link to Defined in")

[langchain/src/prompts/base.ts:151](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/base.ts#L151)

### stream()[](#stream "Direct link to stream()")

> **stream**(`input`: [`InputValues`](/docs/api/schema/types/InputValues), `options`?: `Partial`<`BaseCallbackConfig`\>): `Promise`<`IterableReadableStream`<`FormattedOutput`\>\>

#### Parameters[](#parameters-11 "Direct link to Parameters")

Parameter

Type

`input`

[`InputValues`](/docs/api/schema/types/InputValues)

`options?`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-16 "Direct link to Returns")

`Promise`<`IterableReadableStream`<`FormattedOutput`\>\>

#### Inherited from[](#inherited-from-11 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[stream](/docs/api/schema_runnable/classes/Runnable#stream)

#### Defined in[](#defined-in-27 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:93](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L93)

### toJSON()[](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[](#returns-17 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[](#inherited-from-12 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[toJSON](/docs/api/schema_runnable/classes/Runnable#tojson)

#### Defined in[](#defined-in-28 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[](#returns-18 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[](#inherited-from-13 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[toJSONNotImplemented](/docs/api/schema_runnable/classes/Runnable#tojsonnotimplemented)

#### Defined in[](#defined-in-29 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L151)

### deserialize()[](#deserialize "Direct link to deserialize()")

#### Deprecated[](#deprecated-1 "Direct link to Deprecated")

Load a prompt template from a json-like object describing it.

#### Remarks[](#remarks "Direct link to Remarks")

Deserializing needs to be async because templates (e.g. [FewShotPromptTemplate](/docs/api/prompts/classes/FewShotPromptTemplate)) can reference remote resources that we read asynchronously with a web request.

> `Static` **deserialize**(`data`: [`SerializedBasePromptTemplate`](/docs/api/prompts/types/SerializedBasePromptTemplate)): `Promise`<[`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)<[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\>\>

#### Parameters[](#parameters-12 "Direct link to Parameters")

Parameter

Type

`data`

[`SerializedBasePromptTemplate`](/docs/api/prompts/types/SerializedBasePromptTemplate)

#### Returns[](#returns-19 "Direct link to Returns")

`Promise`<[`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)<[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\>\>

#### Defined in[](#defined-in-30 "Direct link to Defined in")

[langchain/src/prompts/base.ts:164](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/base.ts#L164)

### isRunnable()[](#isrunnable "Direct link to isRunnable()")

> `Static` **isRunnable**(`thing`: `any`): thing is Runnable<any, any, BaseCallbackConfig\>

#### Parameters[](#parameters-13 "Direct link to Parameters")

Parameter

Type

`thing`

`any`

#### Returns[](#returns-20 "Direct link to Returns")

thing is Runnable<any, any, BaseCallbackConfig\>

#### Inherited from[](#inherited-from-14 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[isRunnable](/docs/api/schema_runnable/classes/Runnable#isrunnable)

#### Defined in[](#defined-in-31 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:164](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L164)

### \_callWithConfig()[](#_callwithconfig "Direct link to _callwithconfig")

> `Protected` **\_callWithConfig**<T\>(`func`: `Function`, `input`: `T`, `options`?: `BaseCallbackConfig` & {`runType`?: `string`;}): `Promise`<`FormattedOutput`\>

#### Type parameters[](#type-parameters-3 "Direct link to Type parameters")

*   `T` _extends_ [`InputValues`](/docs/api/schema/types/InputValues)

#### Parameters[](#parameters-14 "Direct link to Parameters")

Parameter

Type

`func`

(`input`: `T`) => `Promise`<`FormattedOutput`\>

`input`

`T`

`options?`

`BaseCallbackConfig` & {`runType`?: `string`;}

#### Returns[](#returns-21 "Direct link to Returns")

`Promise`<`FormattedOutput`\>

#### Inherited from[](#inherited-from-15 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[\_callWithConfig](/docs/api/schema_runnable/classes/Runnable#_callwithconfig)

#### Defined in[](#defined-in-32 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:117](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L117)

### \_getOptionsList()[](#_getoptionslist "Direct link to _getoptionslist")

> `Protected` **\_getOptionsList**(`options`: `Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\], `length`: `number` = `0`): `Partial`<`BaseCallbackConfig`\>\[\]

#### Parameters[](#parameters-15 "Direct link to Parameters")

Parameter

Type

Default value

`options`

`Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\]

`undefined`

`length`

`number`

`0`

#### Returns[](#returns-22 "Direct link to Returns")

`Partial`<`BaseCallbackConfig`\>\[\]

#### Inherited from[](#inherited-from-16 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[\_getOptionsList](/docs/api/schema_runnable/classes/Runnable#_getoptionslist)

#### Defined in[](#defined-in-33 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L48)

### \_separateRunnableConfigFromCallOptions()[](#_separaterunnableconfigfromcalloptions "Direct link to _separaterunnableconfigfromcalloptions")

> `Protected` **\_separateRunnableConfigFromCallOptions**(`options`: `Partial`<`BaseCallbackConfig`\> = `{}`): \[`BaseCallbackConfig`, `Omit`<`Partial`<`BaseCallbackConfig`\>, _keyof_ `BaseCallbackConfig`\>\]

#### Parameters[](#parameters-16 "Direct link to Parameters")

Parameter

Type

`options`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-23 "Direct link to Returns")

\[`BaseCallbackConfig`, `Omit`<`Partial`<`BaseCallbackConfig`\>, _keyof_ `BaseCallbackConfig`\>\]

#### Inherited from[](#inherited-from-17 "Direct link to Inherited from")

[Runnable](/docs/api/schema_runnable/classes/Runnable).[\_separateRunnableConfigFromCallOptions](/docs/api/schema_runnable/classes/Runnable#_separaterunnableconfigfromcalloptions)

#### Defined in[](#defined-in-34 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:102](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L102)