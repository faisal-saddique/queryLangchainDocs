BaseLLM<CallOptions\>
=====================

LLM Wrapper. Provides an [call](/docs/api/llms_base/classes/BaseLLM#call) (an [generate](/docs/api/llms_base/classes/BaseLLM#generate)) function that takes in a prompt (or prompts) and returns a string.

Type parameters[](#type-parameters "Direct link to Type parameters")
---------------------------------------------------------------------

*   `CallOptions` _extends_ [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions) = [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`string`, `CallOptions`\>.**BaseLLM**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new BaseLLM**<CallOptions\>(«destructured»: [`BaseLLMParams`](/docs/api/llms_base/interfaces/BaseLLMParams)): [`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)<`CallOptions`\>

#### Type parameters[](#type-parameters-1 "Direct link to Type parameters")

*   `CallOptions` _extends_ [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions) = [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`«destructured»`

[`BaseLLMParams`](/docs/api/llms_base/interfaces/BaseLLMParams)

#### Returns[](#returns "Direct link to Returns")

[`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)<`CallOptions`\>

#### Overrides[](#overrides "Direct link to Overrides")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[constructor](/docs/api/base_language/classes/BaseLanguageModel#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/llms/base.ts:58](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L58)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### CallOptions[](#calloptions "Direct link to CallOptions")

> **CallOptions**: `CallOptions`

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[CallOptions](/docs/api/base_language/classes/BaseLanguageModel#calloptions)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:110](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L110) [langchain/src/base\_language/index.ts:115](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L115)

### ParsedCallOptions[](#parsedcalloptions "Direct link to ParsedCallOptions")

> **ParsedCallOptions**: `Omit`<`CallOptions`, `never`\>

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/llms/base.ts:49](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L49)

### caller[](#caller "Direct link to caller")

> **caller**: `AsyncCaller`

The async caller should be used by subclasses to make any async calls, which will thus benefit from the concurrency and retry logic.

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[caller](/docs/api/base_language/classes/BaseLanguageModel#caller)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:128](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L128)

### lc\_kwargs[](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[lc\_kwargs](/docs/api/base_language/classes/BaseLanguageModel#lc_kwargs)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L57)

### lc\_namespace[](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Overrides[](#overrides-1 "Direct link to Overrides")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[lc\_namespace](/docs/api/base_language/classes/BaseLanguageModel#lc_namespace)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/llms/base.ts:54](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L54)

### lc\_serializable[](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[lc\_serializable](/docs/api/base_language/classes/BaseLanguageModel#lc_serializable)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L55)

### verbose[](#verbose "Direct link to verbose")

> **verbose**: `boolean`

Whether to print out response text.

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[verbose](/docs/api/base_language/classes/BaseLanguageModel#verbose)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:44](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L44)

### cache?[](#cache "Direct link to cache?")

> **cache**: [`BaseCache`](/docs/api/schema/classes/BaseCache)<[`Generation`](/docs/api/schema/interfaces/Generation)\[\]\>

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/llms/base.ts:56](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L56)

### callbacks?[](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[callbacks](/docs/api/base_language/classes/BaseLanguageModel#callbacks)

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L46)

### metadata?[](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[metadata](/docs/api/base_language/classes/BaseLanguageModel#metadata)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:50](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L50)

### tags?[](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[tags](/docs/api/base_language/classes/BaseLanguageModel#tags)

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L48)

### lc\_runnable[](#lc_runnable "Direct link to lc_runnable")

> `Protected` **lc\_runnable**: `boolean` = `true`

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[lc\_runnable](/docs/api/base_language/classes/BaseLanguageModel#lc_runnable)

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:34](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L34)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### callKeys[](#callkeys "Direct link to callKeys")

Keys that the language model accepts as call options.

> **callKeys**(): `string`\[\]

#### Returns[](#returns-1 "Direct link to Returns")

`string`\[\]

#### Inherited from[](#inherited-from-9 "Direct link to Inherited from")

BaseLanguageModel.callKeys

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:120](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L120)

#### Inherited from[](#inherited-from-10 "Direct link to Inherited from")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[callKeys](/docs/api/base_language/classes/BaseLanguageModel#callkeys)

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:120](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L120)

### lc\_aliases[](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[](#returns-2 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-11 "Direct link to Inherited from")

BaseLanguageModel.lc\_aliases

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

#### Inherited from[](#inherited-from-12 "Direct link to Inherited from")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[lc\_aliases](/docs/api/base_language/classes/BaseLanguageModel#lc_aliases)

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

### lc\_attributes[](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-13 "Direct link to Inherited from")

BaseLanguageModel.lc\_attributes

#### Defined in[](#defined-in-17 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:52](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L52)

#### Inherited from[](#inherited-from-14 "Direct link to Inherited from")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[lc\_attributes](/docs/api/base_language/classes/BaseLanguageModel#lc_attributes)

#### Defined in[](#defined-in-18 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:52](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L52)

### lc\_secrets[](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[](#returns-4 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-15 "Direct link to Inherited from")

BaseLanguageModel.lc\_secrets

#### Defined in[](#defined-in-19 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

#### Inherited from[](#inherited-from-16 "Direct link to Inherited from")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[lc\_secrets](/docs/api/base_language/classes/BaseLanguageModel#lc_secrets)

#### Defined in[](#defined-in-20 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### \_flattenLLMResult()[](#_flattenllmresult "Direct link to _flattenllmresult")

> **\_flattenLLMResult**(`llmResult`: [`LLMResult`](/docs/api/schema/types/LLMResult)): [`LLMResult`](/docs/api/schema/types/LLMResult)\[\]

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`llmResult`

[`LLMResult`](/docs/api/schema/types/LLMResult)

#### Returns[](#returns-5 "Direct link to Returns")

[`LLMResult`](/docs/api/schema/types/LLMResult)\[\]

#### Defined in[](#defined-in-21 "Direct link to Defined in")

[langchain/src/llms/base.ts:197](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L197)

### \_generate()[](#_generate "Direct link to _generate")

Run the LLM on the given prompts and input.

> `Abstract` **\_generate**(`prompts`: `string`\[\], `options`: `Omit`<`CallOptions`, `never`\>, `runManager`?: [`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`prompts`

`string`\[\]

`options`

`Omit`<`CallOptions`, `never`\>

`runManager?`

[`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)

#### Returns[](#returns-6 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Defined in[](#defined-in-22 "Direct link to Defined in")

[langchain/src/llms/base.ts:183](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L183)

### \_identifyingParams()[](#_identifyingparams "Direct link to _identifyingparams")

Get the identifying parameters of the LLM.

> **\_identifyingParams**(): `Record`<`string`, `any`\>

#### Returns[](#returns-7 "Direct link to Returns")

`Record`<`string`, `any`\>

#### Overrides[](#overrides-2 "Direct link to Overrides")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[\_identifyingParams](/docs/api/base_language/classes/BaseLanguageModel#_identifyingparams)

#### Defined in[](#defined-in-23 "Direct link to Defined in")

[langchain/src/llms/base.ts:374](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L374)

### \_llmType()[](#_llmtype "Direct link to _llmtype")

Return the string type key uniquely identifying this class of LLM.

> `Abstract` **\_llmType**(): `string`

#### Returns[](#returns-8 "Direct link to Returns")

`string`

#### Overrides[](#overrides-3 "Direct link to Overrides")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[\_llmType](/docs/api/base_language/classes/BaseLanguageModel#_llmtype)

#### Defined in[](#defined-in-24 "Direct link to Defined in")

[langchain/src/llms/base.ts:381](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L381)

### \_modelType()[](#_modeltype "Direct link to _modeltype")

> **\_modelType**(): `string`

#### Returns[](#returns-9 "Direct link to Returns")

`string`

#### Overrides[](#overrides-4 "Direct link to Overrides")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[\_modelType](/docs/api/base_language/classes/BaseLanguageModel#_modeltype)

#### Defined in[](#defined-in-25 "Direct link to Defined in")

[langchain/src/llms/base.ts:394](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L394)

### \_patchConfig()[](#_patchconfig "Direct link to _patchconfig")

> **\_patchConfig**(`config`: `Partial`<`CallOptions`\> = `{}`, `callbackManager`: `undefined` | [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager) = `undefined`): `Partial`<`CallOptions`\>

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

Default value

`config`

`Partial`<`CallOptions`\>

`{}`

`callbackManager`

`undefined` | [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

`undefined`

#### Returns[](#returns-10 "Direct link to Returns")

`Partial`<`CallOptions`\>

#### Inherited from[](#inherited-from-17 "Direct link to Inherited from")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[\_patchConfig](/docs/api/base_language/classes/BaseLanguageModel#_patchconfig)

#### Defined in[](#defined-in-26 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:146](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L146)

### \_streamIterator()[](#_streamiterator "Direct link to _streamiterator")

> **\_streamIterator**(`input`: [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `options`?: `CallOptions`): `AsyncGenerator`<`string`, `any`, `unknown`\>

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

`input`

[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)

`options?`

`CallOptions`

#### Returns[](#returns-11 "Direct link to Returns")

`AsyncGenerator`<`string`, `any`, `unknown`\>

#### Overrides[](#overrides-5 "Direct link to Overrides")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[\_streamIterator](/docs/api/base_language/classes/BaseLanguageModel#_streamiterator)

#### Defined in[](#defined-in-27 "Direct link to Defined in")

[langchain/src/llms/base.ts:102](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L102)

### \_streamResponseChunks()[](#_streamresponsechunks "Direct link to _streamresponsechunks")

> **\_streamResponseChunks**(`_input`: `string`, `_options`: `Omit`<`CallOptions`, `never`\>, `_runManager`?: [`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)): `AsyncGenerator`<[`GenerationChunk`](/docs/api/schema/classes/GenerationChunk), `any`, `unknown`\>

#### Parameters[](#parameters-5 "Direct link to Parameters")

Parameter

Type

`_input`

`string`

`_options`

`Omit`<`CallOptions`, `never`\>

`_runManager?`

[`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)

#### Returns[](#returns-12 "Direct link to Returns")

`AsyncGenerator`<[`GenerationChunk`](/docs/api/schema/classes/GenerationChunk), `any`, `unknown`\>

#### Defined in[](#defined-in-28 "Direct link to Defined in")

[langchain/src/llms/base.ts:83](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L83)

### batch()[](#batch "Direct link to batch()")

> **batch**(`inputs`: [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)\[\], `options`?: `Partial`<`CallOptions`\> | `Partial`<`CallOptions`\>\[\], `batchOptions`?: `object`): `Promise`<`string`\[\]\>

#### Parameters[](#parameters-6 "Direct link to Parameters")

Parameter

Type

`inputs`

[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)\[\]

`options?`

`Partial`<`CallOptions`\> | `Partial`<`CallOptions`\>\[\]

`batchOptions?`

`object`

`batchOptions.maxConcurrency?`

`number`

#### Returns[](#returns-13 "Direct link to Returns")

`Promise`<`string`\[\]\>

#### Inherited from[](#inherited-from-18 "Direct link to Inherited from")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[batch](/docs/api/base_language/classes/BaseLanguageModel#batch)

#### Defined in[](#defined-in-29 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:63](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L63)

### bind()[](#bind "Direct link to bind()")

> **bind**(`kwargs`: `Partial`<`CallOptions`\>): [`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `string`, `CallOptions`\>

#### Parameters[](#parameters-7 "Direct link to Parameters")

Parameter

Type

`kwargs`

`Partial`<`CallOptions`\>

#### Returns[](#returns-14 "Direct link to Returns")

[`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `string`, `CallOptions`\>

#### Inherited from[](#inherited-from-19 "Direct link to Inherited from")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[bind](/docs/api/base_language/classes/BaseLanguageModel#bind)

#### Defined in[](#defined-in-30 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:41](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L41)

### call()[](#call "Direct link to call()")

Convenience wrapper for [generate](/docs/api/llms_base/classes/BaseLLM#generate) that takes in a single string prompt and returns a single string output.

> **call**(`prompt`: `string`, `options`?: `string`\[\] | `CallOptions`, `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\>

#### Parameters[](#parameters-8 "Direct link to Parameters")

Parameter

Type

`prompt`

`string`

`options?`

`string`\[\] | `CallOptions`

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-15 "Direct link to Returns")

`Promise`<`string`\>

#### Defined in[](#defined-in-31 "Direct link to Defined in")

[langchain/src/llms/base.ts:343](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L343)

### generate()[](#generate "Direct link to generate()")

Run the LLM on the given prompts and input, handling caching.

> **generate**(`prompts`: `string`\[\], `options`?: `string`\[\] | `CallOptions`, `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[](#parameters-9 "Direct link to Parameters")

Parameter

Type

`prompts`

`string`\[\]

`options?`

`string`\[\] | `CallOptions`

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-16 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Defined in[](#defined-in-32 "Direct link to Defined in")

[langchain/src/llms/base.ts:280](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L280)

### generatePrompt()[](#generateprompt "Direct link to generatePrompt()")

> **generatePrompt**(`promptValues`: [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\[\], `options`?: `string`\[\] | `CallOptions`, `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[](#parameters-10 "Direct link to Parameters")

Parameter

Type

`promptValues`

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\[\]

`options?`

`string`\[\] | `CallOptions`

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-17 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Overrides[](#overrides-6 "Direct link to Overrides")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[generatePrompt](/docs/api/base_language/classes/BaseLanguageModel#generateprompt)

#### Defined in[](#defined-in-33 "Direct link to Defined in")

[langchain/src/llms/base.ts:169](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L169)

### getNumTokens()[](#getnumtokens "Direct link to getNumTokens()")

> **getNumTokens**(`text`: `string`): `Promise`<`number`\>

#### Parameters[](#parameters-11 "Direct link to Parameters")

Parameter

Type

`text`

`string`

#### Returns[](#returns-18 "Direct link to Returns")

`Promise`<`number`\>

#### Inherited from[](#inherited-from-20 "Direct link to Inherited from")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[getNumTokens](/docs/api/base_language/classes/BaseLanguageModel#getnumtokens)

#### Defined in[](#defined-in-34 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:166](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L166)

### invocationParams()[](#invocationparams "Direct link to invocationParams()")

Get the parameters used to invoke the model

> **invocationParams**(`_options`?: `Omit`<`CallOptions`, `never`\>): `any`

#### Parameters[](#parameters-12 "Direct link to Parameters")

Parameter

Type

`_options?`

`Omit`<`CallOptions`, `never`\>

#### Returns[](#returns-19 "Direct link to Returns")

`any`

#### Defined in[](#defined-in-35 "Direct link to Defined in")

[langchain/src/llms/base.ts:193](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L193)

### invoke()[](#invoke "Direct link to invoke()")

> **invoke**(`input`: [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `options`?: `CallOptions`): `Promise`<`string`\>

#### Parameters[](#parameters-13 "Direct link to Parameters")

Parameter

Type

`input`

[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)

`options?`

`CallOptions`

#### Returns[](#returns-20 "Direct link to Returns")

`Promise`<`string`\>

#### Overrides[](#overrides-7 "Direct link to Overrides")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[invoke](/docs/api/base_language/classes/BaseLanguageModel#invoke)

#### Defined in[](#defined-in-36 "Direct link to Defined in")

[langchain/src/llms/base.ts:69](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L69)

### pipe()[](#pipe "Direct link to pipe()")

> **pipe**<NewRunOutput\>(`coerceable`: [`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<`string`, `NewRunOutput`\>): [`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `NewRunOutput`\>

#### Type parameters[](#type-parameters-2 "Direct link to Type parameters")

*   `NewRunOutput`

#### Parameters[](#parameters-14 "Direct link to Parameters")

Parameter

Type

`coerceable`

[`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<`string`, `NewRunOutput`\>

#### Returns[](#returns-21 "Direct link to Returns")

[`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `NewRunOutput`\>

#### Inherited from[](#inherited-from-21 "Direct link to Inherited from")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[pipe](/docs/api/base_language/classes/BaseLanguageModel#pipe)

#### Defined in[](#defined-in-37 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:153](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L153)

### predict()[](#predict "Direct link to predict()")

> **predict**(`text`: `string`, `options`?: `string`\[\] | `CallOptions`, `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\>

#### Parameters[](#parameters-15 "Direct link to Parameters")

Parameter

Type

`text`

`string`

`options?`

`string`\[\] | `CallOptions`

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-22 "Direct link to Returns")

`Promise`<`string`\>

#### Overrides[](#overrides-8 "Direct link to Overrides")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[predict](/docs/api/base_language/classes/BaseLanguageModel#predict)

#### Defined in[](#defined-in-38 "Direct link to Defined in")

[langchain/src/llms/base.ts:352](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L352)

### predictMessages()[](#predictmessages "Direct link to predictMessages()")

> **predictMessages**(`messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\], `options`?: `string`\[\] | `CallOptions`, `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Parameters[](#parameters-16 "Direct link to Parameters")

Parameter

Type

`messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]

`options?`

`string`\[\] | `CallOptions`

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-23 "Direct link to Returns")

`Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Overrides[](#overrides-9 "Direct link to Overrides")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[predictMessages](/docs/api/base_language/classes/BaseLanguageModel#predictmessages)

#### Defined in[](#defined-in-39 "Direct link to Defined in")

[langchain/src/llms/base.ts:360](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L360)

### serialize()[](#serialize "Direct link to serialize()")

Return a json-like object representing this LLM.

> **serialize**(): [`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Returns[](#returns-24 "Direct link to Returns")

[`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Overrides[](#overrides-10 "Direct link to Overrides")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[serialize](/docs/api/base_language/classes/BaseLanguageModel#serialize)

#### Defined in[](#defined-in-40 "Direct link to Defined in")

[langchain/src/llms/base.ts:386](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L386)

### stream()[](#stream "Direct link to stream()")

> **stream**(`input`: [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `options`?: `Partial`<`CallOptions`\>): `Promise`<`IterableReadableStream`<`string`\>\>

#### Parameters[](#parameters-17 "Direct link to Parameters")

Parameter

Type

`input`

[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)

`options?`

`Partial`<`CallOptions`\>

#### Returns[](#returns-25 "Direct link to Returns")

`Promise`<`IterableReadableStream`<`string`\>\>

#### Inherited from[](#inherited-from-22 "Direct link to Inherited from")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[stream](/docs/api/base_language/classes/BaseLanguageModel#stream)

#### Defined in[](#defined-in-41 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:93](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L93)

### toJSON()[](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[](#returns-26 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[](#inherited-from-23 "Direct link to Inherited from")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[toJSON](/docs/api/base_language/classes/BaseLanguageModel#tojson)

#### Defined in[](#defined-in-42 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[](#returns-27 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[](#inherited-from-24 "Direct link to Inherited from")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[toJSONNotImplemented](/docs/api/base_language/classes/BaseLanguageModel#tojsonnotimplemented)

#### Defined in[](#defined-in-43 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L151)

### deserialize()[](#deserialize "Direct link to deserialize()")

Load an LLM from a json-like object describing it.

> `Static` **deserialize**(`data`: [`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)): `Promise`<[`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>\>

#### Parameters[](#parameters-18 "Direct link to Parameters")

Parameter

Type

`data`

[`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Returns[](#returns-28 "Direct link to Returns")

`Promise`<[`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>\>

#### Overrides[](#overrides-11 "Direct link to Overrides")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[deserialize](/docs/api/base_language/classes/BaseLanguageModel#deserialize)

#### Defined in[](#defined-in-44 "Direct link to Defined in")

[langchain/src/llms/base.ts:401](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L401)

### isRunnable()[](#isrunnable "Direct link to isRunnable()")

> `Static` **isRunnable**(`thing`: `any`): thing is Runnable<any, any, BaseCallbackConfig\>

#### Parameters[](#parameters-19 "Direct link to Parameters")

Parameter

Type

`thing`

`any`

#### Returns[](#returns-29 "Direct link to Returns")

thing is Runnable<any, any, BaseCallbackConfig\>

#### Inherited from[](#inherited-from-25 "Direct link to Inherited from")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[isRunnable](/docs/api/base_language/classes/BaseLanguageModel#isrunnable)

#### Defined in[](#defined-in-45 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:164](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L164)

### \_callWithConfig()[](#_callwithconfig "Direct link to _callwithconfig")

> `Protected` **\_callWithConfig**<T\>(`func`: `Function`, `input`: `T`, `options`?: `BaseCallbackConfig` & {`runType`?: `string`;}): `Promise`<`string`\>

#### Type parameters[](#type-parameters-3 "Direct link to Type parameters")

*   `T` _extends_ [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)

#### Parameters[](#parameters-20 "Direct link to Parameters")

Parameter

Type

`func`

(`input`: `T`) => `Promise`<`string`\>

`input`

`T`

`options?`

`BaseCallbackConfig` & {`runType`?: `string`;}

#### Returns[](#returns-30 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[](#inherited-from-26 "Direct link to Inherited from")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[\_callWithConfig](/docs/api/base_language/classes/BaseLanguageModel#_callwithconfig)

#### Defined in[](#defined-in-46 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:117](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L117)

### \_getOptionsList()[](#_getoptionslist "Direct link to _getoptionslist")

> `Protected` **\_getOptionsList**(`options`: `Partial`<`CallOptions`\> | `Partial`<`CallOptions`\>\[\], `length`: `number` = `0`): `Partial`<`CallOptions`\>\[\]

#### Parameters[](#parameters-21 "Direct link to Parameters")

Parameter

Type

Default value

`options`

`Partial`<`CallOptions`\> | `Partial`<`CallOptions`\>\[\]

`undefined`

`length`

`number`

`0`

#### Returns[](#returns-31 "Direct link to Returns")

`Partial`<`CallOptions`\>\[\]

#### Inherited from[](#inherited-from-27 "Direct link to Inherited from")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[\_getOptionsList](/docs/api/base_language/classes/BaseLanguageModel#_getoptionslist)

#### Defined in[](#defined-in-47 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L48)

### \_separateRunnableConfigFromCallOptions()[](#_separaterunnableconfigfromcalloptions "Direct link to _separaterunnableconfigfromcalloptions")

> `Protected` **\_separateRunnableConfigFromCallOptions**(`options`?: `Partial`<`CallOptions`\>): \[`BaseCallbackConfig`, `Omit`<`CallOptions`, `never`\>\]

#### Parameters[](#parameters-22 "Direct link to Parameters")

Parameter

Type

`options?`

`Partial`<`CallOptions`\>

#### Returns[](#returns-32 "Direct link to Returns")

\[`BaseCallbackConfig`, `Omit`<`CallOptions`, `never`\>\]

#### Overrides[](#overrides-12 "Direct link to Overrides")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[\_separateRunnableConfigFromCallOptions](/docs/api/base_language/classes/BaseLanguageModel#_separaterunnableconfigfromcalloptions)

#### Defined in[](#defined-in-48 "Direct link to Defined in")

[langchain/src/llms/base.ts:91](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L91)

### \_convertInputToPromptValue()[](#_convertinputtopromptvalue "Direct link to _convertinputtopromptvalue")

> `Static` `Protected` **\_convertInputToPromptValue**(`input`: [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)): [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)

#### Parameters[](#parameters-23 "Direct link to Parameters")

Parameter

Type

`input`

[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)

#### Returns[](#returns-33 "Direct link to Returns")

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)

#### Inherited from[](#inherited-from-28 "Direct link to Inherited from")

[BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel).[\_convertInputToPromptValue](/docs/api/base_language/classes/BaseLanguageModel#_convertinputtopromptvalue)

#### Defined in[](#defined-in-49 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:192](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L192)