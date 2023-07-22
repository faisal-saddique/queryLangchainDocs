BaseLanguageModel
=================

Base class for language models.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseLangChain`](/docs/api/base_language/classes/BaseLangChain).**BaseLanguageModel**

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   [`BaseLanguageModelParams`](/docs/api/base_language/interfaces/BaseLanguageModelParams)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new BaseLanguageModel**(«destructured»: [`BaseLanguageModelParams`](/docs/api/base_language/interfaces/BaseLanguageModelParams)): [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`«destructured»`

[`BaseLanguageModelParams`](/docs/api/base_language/interfaces/BaseLanguageModelParams)

#### Returns[​](#returns "Direct link to Returns")

[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[constructor](/docs/api/base_language/classes/BaseLangChain#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/base\_language/index.ts:118](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L118)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### CallOptions[​](#calloptions "Direct link to CallOptions")

> **CallOptions**: [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:103](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L103)

### caller[​](#caller "Direct link to caller")

> **caller**: `AsyncCaller`

The async caller should be used by subclasses to make any async calls, which will thus benefit from the concurrency and retry logic.

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:116](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L116)

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[lc\_kwargs](/docs/api/base_language/classes/BaseLangChain#lc_kwargs)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

> `Abstract` **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[lc\_namespace](/docs/api/base_language/classes/BaseLangChain#lc_namespace)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/load/serializable.ts:63](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L63)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[lc\_serializable](/docs/api/base_language/classes/BaseLangChain#lc_serializable)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L55)

### verbose[​](#verbose "Direct link to verbose")

> **verbose**: `boolean`

Whether to print out response text.

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

[BaseLanguageModelParams](/docs/api/base_language/interfaces/BaseLanguageModelParams).[verbose](/docs/api/base_language/interfaces/BaseLanguageModelParams#verbose)

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[verbose](/docs/api/base_language/classes/BaseLangChain#verbose)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:38](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L38)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

[BaseLanguageModelParams](/docs/api/base_language/interfaces/BaseLanguageModelParams).[callbacks](/docs/api/base_language/interfaces/BaseLanguageModelParams#callbacks)

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[callbacks](/docs/api/base_language/classes/BaseLangChain#callbacks)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L40)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Implementation of[​](#implementation-of-2 "Direct link to Implementation of")

[BaseLanguageModelParams](/docs/api/base_language/interfaces/BaseLanguageModelParams).[metadata](/docs/api/base_language/interfaces/BaseLanguageModelParams#metadata)

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[metadata](/docs/api/base_language/classes/BaseLangChain#metadata)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:44](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L44)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Implementation of[​](#implementation-of-3 "Direct link to Implementation of")

[BaseLanguageModelParams](/docs/api/base_language/interfaces/BaseLanguageModelParams).[tags](/docs/api/base_language/interfaces/BaseLanguageModelParams#tags)

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[tags](/docs/api/base_language/classes/BaseLangChain#tags)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L42)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### callKeys[​](#callkeys "Direct link to callKeys")

Keys that the language model accepts as call options.

> **callKeys**(): `string`\[\]

#### Returns[​](#returns-1 "Direct link to Returns")

`string`\[\]

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:108](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L108)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:108](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L108)

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

BaseLangChain.lc\_aliases

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[lc\_aliases](/docs/api/base_language/classes/BaseLangChain#lc_aliases)

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

BaseLangChain.lc\_attributes

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[lc\_attributes](/docs/api/base_language/classes/BaseLangChain#lc_attributes)

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-4 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

BaseLangChain.lc\_secrets

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[lc\_secrets](/docs/api/base_language/classes/BaseLangChain#lc_secrets)

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### \_identifyingParams()[​](#_identifyingparams "Direct link to _identifyingparams")

Get the identifying parameters of the LLM.

> **\_identifyingParams**(): `Record`<`string`, `any`\>

#### Returns[​](#returns-5 "Direct link to Returns")

`Record`<`string`, `any`\>

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:184](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L184)

### \_llmType()[​](#_llmtype "Direct link to _llmtype")

> `Abstract` **\_llmType**(): `string`

#### Returns[​](#returns-6 "Direct link to Returns")

`string`

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:150](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L150)

### \_modelType()[​](#_modeltype "Direct link to _modeltype")

> `Abstract` **\_modelType**(): `string`

#### Returns[​](#returns-7 "Direct link to Returns")

`string`

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:148](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L148)

### generatePrompt()[​](#generateprompt "Direct link to generatePrompt()")

> `Abstract` **generatePrompt**(`promptValues`: [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\[\], `options`?: `string`\[\] | [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`promptValues`

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\[\]

`options?`

`string`\[\] | [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-8 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:130](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L130)

### getNumTokens()[​](#getnumtokens "Direct link to getNumTokens()")

> **getNumTokens**(`text`: `string`): `Promise`<`number`\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`text`

`string`

#### Returns[​](#returns-9 "Direct link to Returns")

`Promise`<`number`\>

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:154](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L154)

### predict()[​](#predict "Direct link to predict()")

> `Abstract` **predict**(`text`: `string`, `options`?: `string`\[\] | [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`text`

`string`

`options?`

`string`\[\] | [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-10 "Direct link to Returns")

`Promise`<`string`\>

#### Defined in[​](#defined-in-23 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:136](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L136)

### predictMessages()[​](#predictmessages "Direct link to predictMessages()")

> `Abstract` **predictMessages**(`messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\], `options`?: `string`\[\] | [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]

`options?`

`string`\[\] | [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-11 "Direct link to Returns")

`Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Defined in[​](#defined-in-24 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:142](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L142)

### serialize()[​](#serialize "Direct link to serialize()")

#### Deprecated[​](#deprecated "Direct link to Deprecated")

Return a json-like object representing this LLM.

> **serialize**(): [`SerializedLLM`](/docs/api/base_language/types/SerializedLLM)

#### Returns[​](#returns-12 "Direct link to Returns")

[`SerializedLLM`](/docs/api/base_language/types/SerializedLLM)

#### Defined in[​](#defined-in-25 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:192](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L192)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-13 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[toJSON](/docs/api/base_language/classes/BaseLangChain#tojson)

#### Defined in[​](#defined-in-26 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-14 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[toJSONNotImplemented](/docs/api/base_language/classes/BaseLangChain#tojsonnotimplemented)

#### Defined in[​](#defined-in-27 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)

### deserialize()[​](#deserialize "Direct link to deserialize()")

#### Deprecated[​](#deprecated-1 "Direct link to Deprecated")

Load an LLM from a json-like object describing it.

> `Static` **deserialize**(`data`: [`SerializedLLM`](/docs/api/base_language/types/SerializedLLM)): `Promise`<[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>

#### Parameters[​](#parameters-5 "Direct link to Parameters")

Parameter

Type

`data`

[`SerializedLLM`](/docs/api/base_language/types/SerializedLLM)

#### Returns[​](#returns-15 "Direct link to Returns")

`Promise`<[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>

#### Defined in[​](#defined-in-28 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:204](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L204)