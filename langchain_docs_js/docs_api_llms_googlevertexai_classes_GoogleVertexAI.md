GoogleVertexAI
==============

Enables calls to the Google Cloud's Vertex AI API to access Large Language Models.

To use, you will need to have one of the following authentication methods in place:

*   You are logged into an account permitted to the Google Cloud project using Vertex AI.
*   You are running this on a machine using a service account permitted to the Google Cloud project using Vertex AI.
*   The `GOOGLE_APPLICATION_CREDENTIALS` environment variable is set to the path of a credentials file for a service account permitted to the Google Cloud project using Vertex AI.

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseLLM`](/docs/api/llms_base/classes/BaseLLM).**GoogleVertexAI**

Implements[](#implements "Direct link to Implements")
------------------------------------------------------

*   [`GoogleVertexAITextInput`](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput)

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new GoogleVertexAI**(`fields`?: [`GoogleVertexAITextInput`](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput)): [`GoogleVertexAI`](/docs/api/llms_googlevertexai/classes/GoogleVertexAI)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`fields?`

[`GoogleVertexAITextInput`](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput)

#### Returns[](#returns "Direct link to Returns")

[`GoogleVertexAI`](/docs/api/llms_googlevertexai/classes/GoogleVertexAI)

#### Overrides[](#overrides "Direct link to Overrides")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[constructor](/docs/api/llms_base/classes/BaseLLM#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/llms/googlevertexai.ts:64](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/googlevertexai.ts#L64)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### CallOptions[](#calloptions "Direct link to CallOptions")

> **CallOptions**: [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[CallOptions](/docs/api/llms_base/classes/BaseLLM#calloptions)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:110](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L110) [langchain/src/base\_language/index.ts:115](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L115)

### ParsedCallOptions[](#parsedcalloptions "Direct link to ParsedCallOptions")

> **ParsedCallOptions**: `Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `never`\>

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[ParsedCallOptions](/docs/api/llms_base/classes/BaseLLM#parsedcalloptions)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/llms/base.ts:49](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L49)

### caller[](#caller "Direct link to caller")

> **caller**: `AsyncCaller`

The async caller should be used by subclasses to make any async calls, which will thus benefit from the concurrency and retry logic.

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[caller](/docs/api/llms_base/classes/BaseLLM#caller)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:128](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L128)

### lc\_kwargs[](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[lc\_kwargs](/docs/api/llms_base/classes/BaseLLM#lc_kwargs)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L57)

### lc\_namespace[](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[lc\_namespace](/docs/api/llms_base/classes/BaseLLM#lc_namespace)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/llms/base.ts:54](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L54)

### lc\_serializable[](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[lc\_serializable](/docs/api/llms_base/classes/BaseLLM#lc_serializable)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L55)

### maxOutputTokens[](#maxoutputtokens "Direct link to maxOutputTokens")

> **maxOutputTokens**: `number` = `1024`

Maximum number of tokens to generate in the completion.

#### Implementation of[](#implementation-of "Direct link to Implementation of")

[GoogleVertexAITextInput](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput).[maxOutputTokens](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput#maxoutputtokens)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/llms/googlevertexai.ts:52](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/googlevertexai.ts#L52)

### model[](#model "Direct link to model")

> **model**: `string` = `"text-bison"`

Model to use

#### Implementation of[](#implementation-of-1 "Direct link to Implementation of")

[GoogleVertexAITextInput](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput).[model](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput#model)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/llms/googlevertexai.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/googlevertexai.ts#L48)

### temperature[](#temperature "Direct link to temperature")

> **temperature**: `number` = `0.7`

Sampling temperature to use

#### Implementation of[](#implementation-of-2 "Direct link to Implementation of")

[GoogleVertexAITextInput](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput).[temperature](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput#temperature)

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/llms/googlevertexai.ts:50](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/googlevertexai.ts#L50)

### topK[](#topk "Direct link to topK")

> **topK**: `number` = `40`

Top-k changes how the model selects tokens for output.

A top-k of 1 means the selected token is the most probable among all tokens in the model’s vocabulary (also called greedy decoding), while a top-k of 3 means that the next token is selected from among the 3 most probable tokens (using temperature).

#### Implementation of[](#implementation-of-3 "Direct link to Implementation of")

[GoogleVertexAITextInput](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput).[topK](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput#topk)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/llms/googlevertexai.ts:56](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/googlevertexai.ts#L56)

### topP[](#topp "Direct link to topP")

> **topP**: `number` = `0.8`

Top-p changes how the model selects tokens for output.

Tokens are selected from most probable to least until the sum of their probabilities equals the top-p value.

For example, if tokens A, B, and C have a probability of .3, .2, and .1 and the top-p value is .5, then the model will select either A or B as the next token (using temperature).

#### Implementation of[](#implementation-of-4 "Direct link to Implementation of")

[GoogleVertexAITextInput](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput).[topP](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput#topp)

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/llms/googlevertexai.ts:54](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/googlevertexai.ts#L54)

### verbose[](#verbose "Direct link to verbose")

> **verbose**: `boolean`

Whether to print out response text.

#### Implementation of[](#implementation-of-5 "Direct link to Implementation of")

[GoogleVertexAITextInput](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput).[verbose](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput#verbose)

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[verbose](/docs/api/llms_base/classes/BaseLLM#verbose)

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:44](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L44)

### cache?[](#cache "Direct link to cache?")

> **cache**: [`BaseCache`](/docs/api/schema/classes/BaseCache)<[`Generation`](/docs/api/schema/interfaces/Generation)\[\]\>

#### Implementation of[](#implementation-of-6 "Direct link to Implementation of")

[GoogleVertexAITextInput](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput).[cache](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput#cache)

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[cache](/docs/api/llms_base/classes/BaseLLM#cache)

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/llms/base.ts:56](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L56)

### callbacks?[](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Implementation of[](#implementation-of-7 "Direct link to Implementation of")

[GoogleVertexAITextInput](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput).[callbacks](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput#callbacks)

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[callbacks](/docs/api/llms_base/classes/BaseLLM#callbacks)

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L46)

### metadata?[](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Implementation of[](#implementation-of-8 "Direct link to Implementation of")

[GoogleVertexAITextInput](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput).[metadata](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput#metadata)

#### Inherited from[](#inherited-from-9 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[metadata](/docs/api/llms_base/classes/BaseLLM#metadata)

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:50](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L50)

### tags?[](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Implementation of[](#implementation-of-9 "Direct link to Implementation of")

[GoogleVertexAITextInput](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput).[tags](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput#tags)

#### Inherited from[](#inherited-from-10 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[tags](/docs/api/llms_base/classes/BaseLLM#tags)

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L48)

### lc\_runnable[](#lc_runnable "Direct link to lc_runnable")

> `Protected` **lc\_runnable**: `boolean` = `true`

#### Inherited from[](#inherited-from-11 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[lc\_runnable](/docs/api/llms_base/classes/BaseLLM#lc_runnable)

#### Defined in[](#defined-in-17 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:34](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L34)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### callKeys[](#callkeys "Direct link to callKeys")

Keys that the language model accepts as call options.

> **callKeys**(): `string`\[\]

#### Returns[](#returns-1 "Direct link to Returns")

`string`\[\]

#### Inherited from[](#inherited-from-12 "Direct link to Inherited from")

BaseLLM.callKeys

#### Defined in[](#defined-in-18 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:120](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L120)

#### Inherited from[](#inherited-from-13 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[callKeys](/docs/api/llms_base/classes/BaseLLM#callkeys)

#### Defined in[](#defined-in-19 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:120](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L120)

### lc\_aliases[](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[](#returns-2 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-14 "Direct link to Inherited from")

BaseLLM.lc\_aliases

#### Defined in[](#defined-in-20 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

#### Inherited from[](#inherited-from-15 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[lc\_aliases](/docs/api/llms_base/classes/BaseLLM#lc_aliases)

#### Defined in[](#defined-in-21 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

### lc\_attributes[](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-16 "Direct link to Inherited from")

BaseLLM.lc\_attributes

#### Defined in[](#defined-in-22 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:52](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L52)

#### Inherited from[](#inherited-from-17 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[lc\_attributes](/docs/api/llms_base/classes/BaseLLM#lc_attributes)

#### Defined in[](#defined-in-23 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:52](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L52)

### lc\_secrets[](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[](#returns-4 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-18 "Direct link to Inherited from")

BaseLLM.lc\_secrets

#### Defined in[](#defined-in-24 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

#### Inherited from[](#inherited-from-19 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[lc\_secrets](/docs/api/llms_base/classes/BaseLLM#lc_secrets)

#### Defined in[](#defined-in-25 "Direct link to Defined in")

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

#### Inherited from[](#inherited-from-20 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[\_flattenLLMResult](/docs/api/llms_base/classes/BaseLLM#_flattenllmresult)

#### Defined in[](#defined-in-26 "Direct link to Defined in")

[langchain/src/llms/base.ts:197](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L197)

### \_generate()[](#_generate "Direct link to _generate")

Run the LLM on the given prompts and input.

> **\_generate**(`prompts`: `string`\[\], `options`: `Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `never`\>): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`prompts`

`string`\[\]

`options`

`Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `never`\>

#### Returns[](#returns-6 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Overrides[](#overrides-1 "Direct link to Overrides")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[\_generate](/docs/api/llms_base/classes/BaseLLM#_generate)

#### Defined in[](#defined-in-27 "Direct link to Defined in")

[langchain/src/llms/googlevertexai.ts:92](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/googlevertexai.ts#L92)

### \_generatePrompt()[](#_generateprompt "Direct link to _generateprompt")

> **\_generatePrompt**(`prompt`: `string`, `options`: `Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `never`\>): `Promise`<[`Generation`](/docs/api/schema/interfaces/Generation)\[\]\>

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

`prompt`

`string`

`options`

`Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `never`\>

#### Returns[](#returns-7 "Direct link to Returns")

`Promise`<[`Generation`](/docs/api/schema/interfaces/Generation)\[\]\>

#### Defined in[](#defined-in-28 "Direct link to Defined in")

[langchain/src/llms/googlevertexai.ts:102](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/googlevertexai.ts#L102)

### \_identifyingParams()[](#_identifyingparams "Direct link to _identifyingparams")

Get the identifying parameters of the LLM.

> **\_identifyingParams**(): `Record`<`string`, `any`\>

#### Returns[](#returns-8 "Direct link to Returns")

`Record`<`string`, `any`\>

#### Inherited from[](#inherited-from-21 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[\_identifyingParams](/docs/api/llms_base/classes/BaseLLM#_identifyingparams)

#### Defined in[](#defined-in-29 "Direct link to Defined in")

[langchain/src/llms/base.ts:374](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L374)

### \_llmType()[](#_llmtype "Direct link to _llmtype")

Return the string type key uniquely identifying this class of LLM.

> **\_llmType**(): `string`

#### Returns[](#returns-9 "Direct link to Returns")

`string`

#### Overrides[](#overrides-2 "Direct link to Overrides")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[\_llmType](/docs/api/llms_base/classes/BaseLLM#_llmtype)

#### Defined in[](#defined-in-30 "Direct link to Defined in")

[langchain/src/llms/googlevertexai.ts:88](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/googlevertexai.ts#L88)

### \_modelType()[](#_modeltype "Direct link to _modeltype")

> **\_modelType**(): `string`

#### Returns[](#returns-10 "Direct link to Returns")

`string`

#### Inherited from[](#inherited-from-22 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[\_modelType](/docs/api/llms_base/classes/BaseLLM#_modeltype)

#### Defined in[](#defined-in-31 "Direct link to Defined in")

[langchain/src/llms/base.ts:394](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L394)

### \_patchConfig()[](#_patchconfig "Direct link to _patchconfig")

> **\_patchConfig**(`config`: `Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\> = `{}`, `callbackManager`: `undefined` | [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager) = `undefined`): `Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

Default value

`config`

`Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>

`{}`

`callbackManager`

`undefined` | [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

`undefined`

#### Returns[](#returns-11 "Direct link to Returns")

`Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>

#### Inherited from[](#inherited-from-23 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[\_patchConfig](/docs/api/llms_base/classes/BaseLLM#_patchconfig)

#### Defined in[](#defined-in-32 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:146](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L146)

### \_streamIterator()[](#_streamiterator "Direct link to _streamiterator")

> **\_streamIterator**(`input`: [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `options`?: [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)): `AsyncGenerator`<`string`, `any`, `unknown`\>

#### Parameters[](#parameters-5 "Direct link to Parameters")

Parameter

Type

`input`

[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)

`options?`

[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

#### Returns[](#returns-12 "Direct link to Returns")

`AsyncGenerator`<`string`, `any`, `unknown`\>

#### Inherited from[](#inherited-from-24 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[\_streamIterator](/docs/api/llms_base/classes/BaseLLM#_streamiterator)

#### Defined in[](#defined-in-33 "Direct link to Defined in")

[langchain/src/llms/base.ts:102](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L102)

### \_streamResponseChunks()[](#_streamresponsechunks "Direct link to _streamresponsechunks")

> **\_streamResponseChunks**(`_input`: `string`, `_options`: `Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `never`\>, `_runManager`?: [`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)): `AsyncGenerator`<[`GenerationChunk`](/docs/api/schema/classes/GenerationChunk), `any`, `unknown`\>

#### Parameters[](#parameters-6 "Direct link to Parameters")

Parameter

Type

`_input`

`string`

`_options`

`Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `never`\>

`_runManager?`

[`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)

#### Returns[](#returns-13 "Direct link to Returns")

`AsyncGenerator`<[`GenerationChunk`](/docs/api/schema/classes/GenerationChunk), `any`, `unknown`\>

#### Inherited from[](#inherited-from-25 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[\_streamResponseChunks](/docs/api/llms_base/classes/BaseLLM#_streamresponsechunks)

#### Defined in[](#defined-in-34 "Direct link to Defined in")

[langchain/src/llms/base.ts:83](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L83)

### batch()[](#batch "Direct link to batch()")

> **batch**(`inputs`: [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)\[\], `options`?: `Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\> | `Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>\[\], `batchOptions`?: `object`): `Promise`<`string`\[\]\>

#### Parameters[](#parameters-7 "Direct link to Parameters")

Parameter

Type

`inputs`

[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)\[\]

`options?`

`Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\> | `Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>\[\]

`batchOptions?`

`object`

`batchOptions.maxConcurrency?`

`number`

#### Returns[](#returns-14 "Direct link to Returns")

`Promise`<`string`\[\]\>

#### Inherited from[](#inherited-from-26 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[batch](/docs/api/llms_base/classes/BaseLLM#batch)

#### Defined in[](#defined-in-35 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:63](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L63)

### bind()[](#bind "Direct link to bind()")

> **bind**(`kwargs`: `Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>): [`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `string`, [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>

#### Parameters[](#parameters-8 "Direct link to Parameters")

Parameter

Type

`kwargs`

`Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>

#### Returns[](#returns-15 "Direct link to Returns")

[`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `string`, [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>

#### Inherited from[](#inherited-from-27 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[bind](/docs/api/llms_base/classes/BaseLLM#bind)

#### Defined in[](#defined-in-36 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:41](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L41)

### call()[](#call "Direct link to call()")

Convenience wrapper for [generate](/docs/api/llms_base/classes/BaseLLM#generate) that takes in a single string prompt and returns a single string output.

> **call**(`prompt`: `string`, `options`?: `string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\>

#### Parameters[](#parameters-9 "Direct link to Parameters")

Parameter

Type

`prompt`

`string`

`options?`

`string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-16 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[](#inherited-from-28 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[call](/docs/api/llms_base/classes/BaseLLM#call)

#### Defined in[](#defined-in-37 "Direct link to Defined in")

[langchain/src/llms/base.ts:343](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L343)

### extractPredictionFromResponse()[](#extractpredictionfromresponse "Direct link to extractPredictionFromResponse()")

> **extractPredictionFromResponse**(`result`: `GoogleVertexAILLMResponse`<`TextPrediction`\>): `TextPrediction`

#### Parameters[](#parameters-10 "Direct link to Parameters")

Parameter

Type

`result`

`GoogleVertexAILLMResponse`<`TextPrediction`\>

#### Returns[](#returns-17 "Direct link to Returns")

`TextPrediction`

#### Defined in[](#defined-in-38 "Direct link to Defined in")

[langchain/src/llms/googlevertexai.ts:141](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/googlevertexai.ts#L141)

### formatInstance()[](#formatinstance "Direct link to formatInstance()")

> **formatInstance**(`prompt`: `string`): `GoogleVertexAILLMInstance`

#### Parameters[](#parameters-11 "Direct link to Parameters")

Parameter

Type

`prompt`

`string`

#### Returns[](#returns-18 "Direct link to Returns")

`GoogleVertexAILLMInstance`

#### Defined in[](#defined-in-39 "Direct link to Defined in")

[langchain/src/llms/googlevertexai.ts:135](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/googlevertexai.ts#L135)

### formatInstanceCode()[](#formatinstancecode "Direct link to formatInstanceCode()")

> **formatInstanceCode**(`prompt`: `string`): `GoogleVertexAILLMInstance`

#### Parameters[](#parameters-12 "Direct link to Parameters")

Parameter

Type

`prompt`

`string`

#### Returns[](#returns-19 "Direct link to Returns")

`GoogleVertexAILLMInstance`

#### Defined in[](#defined-in-40 "Direct link to Defined in")

[langchain/src/llms/googlevertexai.ts:131](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/googlevertexai.ts#L131)

### formatInstanceText()[](#formatinstancetext "Direct link to formatInstanceText()")

> **formatInstanceText**(`prompt`: `string`): `GoogleVertexAILLMInstance`

#### Parameters[](#parameters-13 "Direct link to Parameters")

Parameter

Type

`prompt`

`string`

#### Returns[](#returns-20 "Direct link to Returns")

`GoogleVertexAILLMInstance`

#### Defined in[](#defined-in-41 "Direct link to Defined in")

[langchain/src/llms/googlevertexai.ts:127](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/googlevertexai.ts#L127)

### generate()[](#generate "Direct link to generate()")

Run the LLM on the given prompts and input, handling caching.

> **generate**(`prompts`: `string`\[\], `options`?: `string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[](#parameters-14 "Direct link to Parameters")

Parameter

Type

`prompts`

`string`\[\]

`options?`

`string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-21 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[](#inherited-from-29 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[generate](/docs/api/llms_base/classes/BaseLLM#generate)

#### Defined in[](#defined-in-42 "Direct link to Defined in")

[langchain/src/llms/base.ts:280](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L280)

### generatePrompt()[](#generateprompt "Direct link to generatePrompt()")

> **generatePrompt**(`promptValues`: [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\[\], `options`?: `string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[](#parameters-15 "Direct link to Parameters")

Parameter

Type

`promptValues`

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\[\]

`options?`

`string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-22 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[](#inherited-from-30 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[generatePrompt](/docs/api/llms_base/classes/BaseLLM#generateprompt)

#### Defined in[](#defined-in-43 "Direct link to Defined in")

[langchain/src/llms/base.ts:169](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L169)

### getNumTokens()[](#getnumtokens "Direct link to getNumTokens()")

> **getNumTokens**(`text`: `string`): `Promise`<`number`\>

#### Parameters[](#parameters-16 "Direct link to Parameters")

Parameter

Type

`text`

`string`

#### Returns[](#returns-23 "Direct link to Returns")

`Promise`<`number`\>

#### Inherited from[](#inherited-from-31 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[getNumTokens](/docs/api/llms_base/classes/BaseLLM#getnumtokens)

#### Defined in[](#defined-in-44 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:166](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L166)

### invocationParams()[](#invocationparams "Direct link to invocationParams()")

Get the parameters used to invoke the model

> **invocationParams**(`_options`?: `Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `never`\>): `any`

#### Parameters[](#parameters-17 "Direct link to Parameters")

Parameter

Type

`_options?`

`Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `never`\>

#### Returns[](#returns-24 "Direct link to Returns")

`any`

#### Inherited from[](#inherited-from-32 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[invocationParams](/docs/api/llms_base/classes/BaseLLM#invocationparams)

#### Defined in[](#defined-in-45 "Direct link to Defined in")

[langchain/src/llms/base.ts:193](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L193)

### invoke()[](#invoke "Direct link to invoke()")

> **invoke**(`input`: [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `options`?: [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)): `Promise`<`string`\>

#### Parameters[](#parameters-18 "Direct link to Parameters")

Parameter

Type

`input`

[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)

`options?`

[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

#### Returns[](#returns-25 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[](#inherited-from-33 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[invoke](/docs/api/llms_base/classes/BaseLLM#invoke)

#### Defined in[](#defined-in-46 "Direct link to Defined in")

[langchain/src/llms/base.ts:69](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L69)

### pipe()[](#pipe "Direct link to pipe()")

> **pipe**<NewRunOutput\>(`coerceable`: [`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<`string`, `NewRunOutput`\>): [`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `NewRunOutput`\>

#### Type parameters[](#type-parameters "Direct link to Type parameters")

*   `NewRunOutput`

#### Parameters[](#parameters-19 "Direct link to Parameters")

Parameter

Type

`coerceable`

[`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<`string`, `NewRunOutput`\>

#### Returns[](#returns-26 "Direct link to Returns")

[`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `NewRunOutput`\>

#### Inherited from[](#inherited-from-34 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[pipe](/docs/api/llms_base/classes/BaseLLM#pipe)

#### Defined in[](#defined-in-47 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:153](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L153)

### predict()[](#predict "Direct link to predict()")

> **predict**(`text`: `string`, `options`?: `string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\>

#### Parameters[](#parameters-20 "Direct link to Parameters")

Parameter

Type

`text`

`string`

`options?`

`string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-27 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[](#inherited-from-35 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[predict](/docs/api/llms_base/classes/BaseLLM#predict)

#### Defined in[](#defined-in-48 "Direct link to Defined in")

[langchain/src/llms/base.ts:352](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L352)

### predictMessages()[](#predictmessages "Direct link to predictMessages()")

> **predictMessages**(`messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\], `options`?: `string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Parameters[](#parameters-21 "Direct link to Parameters")

Parameter

Type

`messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]

`options?`

`string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-28 "Direct link to Returns")

`Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Inherited from[](#inherited-from-36 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[predictMessages](/docs/api/llms_base/classes/BaseLLM#predictmessages)

#### Defined in[](#defined-in-49 "Direct link to Defined in")

[langchain/src/llms/base.ts:360](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L360)

### serialize()[](#serialize "Direct link to serialize()")

Return a json-like object representing this LLM.

> **serialize**(): [`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Returns[](#returns-29 "Direct link to Returns")

[`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Inherited from[](#inherited-from-37 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[serialize](/docs/api/llms_base/classes/BaseLLM#serialize)

#### Defined in[](#defined-in-50 "Direct link to Defined in")

[langchain/src/llms/base.ts:386](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L386)

### stream()[](#stream "Direct link to stream()")

> **stream**(`input`: [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `options`?: `Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>): `Promise`<`IterableReadableStream`<`string`\>\>

#### Parameters[](#parameters-22 "Direct link to Parameters")

Parameter

Type

`input`

[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)

`options?`

`Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>

#### Returns[](#returns-30 "Direct link to Returns")

`Promise`<`IterableReadableStream`<`string`\>\>

#### Inherited from[](#inherited-from-38 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[stream](/docs/api/llms_base/classes/BaseLLM#stream)

#### Defined in[](#defined-in-51 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:93](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L93)

### toJSON()[](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[](#returns-31 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[](#inherited-from-39 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[toJSON](/docs/api/llms_base/classes/BaseLLM#tojson)

#### Defined in[](#defined-in-52 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[](#returns-32 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[](#inherited-from-40 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[toJSONNotImplemented](/docs/api/llms_base/classes/BaseLLM#tojsonnotimplemented)

#### Defined in[](#defined-in-53 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L151)

### deserialize()[](#deserialize "Direct link to deserialize()")

Load an LLM from a json-like object describing it.

> `Static` **deserialize**(`data`: [`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)): `Promise`<[`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>\>

#### Parameters[](#parameters-23 "Direct link to Parameters")

Parameter

Type

`data`

[`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Returns[](#returns-33 "Direct link to Returns")

`Promise`<[`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>\>

#### Inherited from[](#inherited-from-41 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[deserialize](/docs/api/llms_base/classes/BaseLLM#deserialize)

#### Defined in[](#defined-in-54 "Direct link to Defined in")

[langchain/src/llms/base.ts:401](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L401)

### isRunnable()[](#isrunnable "Direct link to isRunnable()")

> `Static` **isRunnable**(`thing`: `any`): thing is Runnable<any, any, BaseCallbackConfig\>

#### Parameters[](#parameters-24 "Direct link to Parameters")

Parameter

Type

`thing`

`any`

#### Returns[](#returns-34 "Direct link to Returns")

thing is Runnable<any, any, BaseCallbackConfig\>

#### Inherited from[](#inherited-from-42 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[isRunnable](/docs/api/llms_base/classes/BaseLLM#isrunnable)

#### Defined in[](#defined-in-55 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:164](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L164)

### \_callWithConfig()[](#_callwithconfig "Direct link to _callwithconfig")

> `Protected` **\_callWithConfig**<T\>(`func`: `Function`, `input`: `T`, `options`?: `BaseCallbackConfig` & {`runType`?: `string`;}): `Promise`<`string`\>

#### Type parameters[](#type-parameters-1 "Direct link to Type parameters")

*   `T` _extends_ [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)

#### Parameters[](#parameters-25 "Direct link to Parameters")

Parameter

Type

`func`

(`input`: `T`) => `Promise`<`string`\>

`input`

`T`

`options?`

`BaseCallbackConfig` & {`runType`?: `string`;}

#### Returns[](#returns-35 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[](#inherited-from-43 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[\_callWithConfig](/docs/api/llms_base/classes/BaseLLM#_callwithconfig)

#### Defined in[](#defined-in-56 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:117](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L117)

### \_getOptionsList()[](#_getoptionslist "Direct link to _getoptionslist")

> `Protected` **\_getOptionsList**(`options`: `Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\> | `Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>\[\], `length`: `number` = `0`): `Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>\[\]

#### Parameters[](#parameters-26 "Direct link to Parameters")

Parameter

Type

Default value

`options`

`Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\> | `Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>\[\]

`undefined`

`length`

`number`

`0`

#### Returns[](#returns-36 "Direct link to Returns")

`Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>\[\]

#### Inherited from[](#inherited-from-44 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[\_getOptionsList](/docs/api/llms_base/classes/BaseLLM#_getoptionslist)

#### Defined in[](#defined-in-57 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L48)

### \_separateRunnableConfigFromCallOptions()[](#_separaterunnableconfigfromcalloptions "Direct link to _separaterunnableconfigfromcalloptions")

> `Protected` **\_separateRunnableConfigFromCallOptions**(`options`?: `Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>): \[`BaseCallbackConfig`, `Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `never`\>\]

#### Parameters[](#parameters-27 "Direct link to Parameters")

Parameter

Type

`options?`

`Partial`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>

#### Returns[](#returns-37 "Direct link to Returns")

\[`BaseCallbackConfig`, `Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `never`\>\]

#### Inherited from[](#inherited-from-45 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[\_separateRunnableConfigFromCallOptions](/docs/api/llms_base/classes/BaseLLM#_separaterunnableconfigfromcalloptions)

#### Defined in[](#defined-in-58 "Direct link to Defined in")

[langchain/src/llms/base.ts:91](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L91)

### \_convertInputToPromptValue()[](#_convertinputtopromptvalue "Direct link to _convertinputtopromptvalue")

> `Static` `Protected` **\_convertInputToPromptValue**(`input`: [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)): [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)

#### Parameters[](#parameters-28 "Direct link to Parameters")

Parameter

Type

`input`

[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)

#### Returns[](#returns-38 "Direct link to Returns")

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)

#### Inherited from[](#inherited-from-46 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[\_convertInputToPromptValue](/docs/api/llms_base/classes/BaseLLM#_convertinputtopromptvalue)

#### Defined in[](#defined-in-59 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:192](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L192)