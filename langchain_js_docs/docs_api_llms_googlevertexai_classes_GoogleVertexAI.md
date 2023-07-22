GoogleVertexAI
==============

Enables calls to the Google Cloud's Vertex AI API to access Large Language Models.

To use, you will need to have one of the following authentication methods in place:

*   You are logged into an account permitted to the Google Cloud project using Vertex AI.
*   You are running this on a machine using a service account permitted to the Google Cloud project using Vertex AI.
*   The `GOOGLE_APPLICATION_CREDENTIALS` environment variable is set to the path of a credentials file for a service account permitted to the Google Cloud project using Vertex AI.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseLLM`](/docs/api/llms_base/classes/BaseLLM).**GoogleVertexAI**

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   [`GoogleVertexAITextInput`](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new GoogleVertexAI**(`fields`?: [`GoogleVertexAITextInput`](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput)): [`GoogleVertexAI`](/docs/api/llms_googlevertexai/classes/GoogleVertexAI)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields?`

[`GoogleVertexAITextInput`](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput)

#### Returns[​](#returns "Direct link to Returns")

[`GoogleVertexAI`](/docs/api/llms_googlevertexai/classes/GoogleVertexAI)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[constructor](/docs/api/llms_base/classes/BaseLLM#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/llms/googlevertexai.ts:63](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/googlevertexai.ts#L63)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### CallOptions[​](#calloptions "Direct link to CallOptions")

> **CallOptions**: [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[CallOptions](/docs/api/llms_base/classes/BaseLLM#calloptions)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/llms/base.ts:44](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L44)

### ParsedCallOptions[​](#parsedcalloptions "Direct link to ParsedCallOptions")

> **ParsedCallOptions**: `Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[ParsedCallOptions](/docs/api/llms_base/classes/BaseLLM#parsedcalloptions)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/llms/base.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L46)

### caller[​](#caller "Direct link to caller")

> **caller**: `AsyncCaller`

The async caller should be used by subclasses to make any async calls, which will thus benefit from the concurrency and retry logic.

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[caller](/docs/api/llms_base/classes/BaseLLM#caller)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:116](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L116)

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[lc\_kwargs](/docs/api/llms_base/classes/BaseLLM#lc_kwargs)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[lc\_namespace](/docs/api/llms_base/classes/BaseLLM#lc_namespace)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/llms/base.ts:51](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L51)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[lc\_serializable](/docs/api/llms_base/classes/BaseLLM#lc_serializable)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L55)

### maxOutputTokens[​](#maxoutputtokens "Direct link to maxOutputTokens")

> **maxOutputTokens**: `number` = `1024`

Maximum number of tokens to generate in the completion.

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

[GoogleVertexAITextInput](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput).[maxOutputTokens](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput#maxoutputtokens)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/llms/googlevertexai.ts:51](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/googlevertexai.ts#L51)

### model[​](#model "Direct link to model")

> **model**: `string` = `"text-bison"`

Model to use

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

[GoogleVertexAITextInput](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput).[model](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput#model)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/llms/googlevertexai.ts:47](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/googlevertexai.ts#L47)

### temperature[​](#temperature "Direct link to temperature")

> **temperature**: `number` = `0.7`

Sampling temperature to use

#### Implementation of[​](#implementation-of-2 "Direct link to Implementation of")

[GoogleVertexAITextInput](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput).[temperature](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput#temperature)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/llms/googlevertexai.ts:49](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/googlevertexai.ts#L49)

### topK[​](#topk "Direct link to topK")

> **topK**: `number` = `40`

Top-k changes how the model selects tokens for output.

A top-k of 1 means the selected token is the most probable among all tokens in the model’s vocabulary (also called greedy decoding), while a top-k of 3 means that the next token is selected from among the 3 most probable tokens (using temperature).

#### Implementation of[​](#implementation-of-3 "Direct link to Implementation of")

[GoogleVertexAITextInput](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput).[topK](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput#topk)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/llms/googlevertexai.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/googlevertexai.ts#L55)

### topP[​](#topp "Direct link to topP")

> **topP**: `number` = `0.8`

Top-p changes how the model selects tokens for output.

Tokens are selected from most probable to least until the sum of their probabilities equals the top-p value.

For example, if tokens A, B, and C have a probability of .3, .2, and .1 and the top-p value is .5, then the model will select either A or B as the next token (using temperature).

#### Implementation of[​](#implementation-of-4 "Direct link to Implementation of")

[GoogleVertexAITextInput](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput).[topP](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput#topp)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/llms/googlevertexai.ts:53](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/googlevertexai.ts#L53)

### verbose[​](#verbose "Direct link to verbose")

> **verbose**: `boolean`

Whether to print out response text.

#### Implementation of[​](#implementation-of-5 "Direct link to Implementation of")

[GoogleVertexAITextInput](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput).[verbose](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput#verbose)

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[verbose](/docs/api/llms_base/classes/BaseLLM#verbose)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:38](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L38)

### cache?[​](#cache "Direct link to cache?")

> **cache**: [`BaseCache`](/docs/api/schema/classes/BaseCache)<[`Generation`](/docs/api/schema/interfaces/Generation)\[\]\>

#### Implementation of[​](#implementation-of-6 "Direct link to Implementation of")

[GoogleVertexAITextInput](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput).[cache](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput#cache)

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[cache](/docs/api/llms_base/classes/BaseLLM#cache)

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/llms/base.ts:53](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L53)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Implementation of[​](#implementation-of-7 "Direct link to Implementation of")

[GoogleVertexAITextInput](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput).[callbacks](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput#callbacks)

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[callbacks](/docs/api/llms_base/classes/BaseLLM#callbacks)

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L40)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Implementation of[​](#implementation-of-8 "Direct link to Implementation of")

[GoogleVertexAITextInput](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput).[metadata](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput#metadata)

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[metadata](/docs/api/llms_base/classes/BaseLLM#metadata)

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:44](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L44)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Implementation of[​](#implementation-of-9 "Direct link to Implementation of")

[GoogleVertexAITextInput](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput).[tags](/docs/api/llms_googlevertexai/interfaces/GoogleVertexAITextInput#tags)

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[tags](/docs/api/llms_base/classes/BaseLLM#tags)

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L42)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### callKeys[​](#callkeys "Direct link to callKeys")

Keys that the language model accepts as call options.

> **callKeys**(): `string`\[\]

#### Returns[​](#returns-1 "Direct link to Returns")

`string`\[\]

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

BaseLLM.callKeys

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:108](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L108)

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[callKeys](/docs/api/llms_base/classes/BaseLLM#callkeys)

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:108](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L108)

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

BaseLLM.lc\_aliases

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[lc\_aliases](/docs/api/llms_base/classes/BaseLLM#lc_aliases)

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-15 "Direct link to Inherited from")

BaseLLM.lc\_attributes

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

#### Inherited from[​](#inherited-from-16 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[lc\_attributes](/docs/api/llms_base/classes/BaseLLM#lc_attributes)

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-4 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-17 "Direct link to Inherited from")

BaseLLM.lc\_secrets

#### Defined in[​](#defined-in-23 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-18 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[lc\_secrets](/docs/api/llms_base/classes/BaseLLM#lc_secrets)

#### Defined in[​](#defined-in-24 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### \_flattenLLMResult()[​](#_flattenllmresult "Direct link to _flattenllmresult")

> **\_flattenLLMResult**(`llmResult`: [`LLMResult`](/docs/api/schema/types/LLMResult)): [`LLMResult`](/docs/api/schema/types/LLMResult)\[\]

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`llmResult`

[`LLMResult`](/docs/api/schema/types/LLMResult)

#### Returns[​](#returns-5 "Direct link to Returns")

[`LLMResult`](/docs/api/schema/types/LLMResult)\[\]

#### Inherited from[​](#inherited-from-19 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[\_flattenLLMResult](/docs/api/llms_base/classes/BaseLLM#_flattenllmresult)

#### Defined in[​](#defined-in-25 "Direct link to Defined in")

[langchain/src/llms/base.ts:94](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L94)

### \_generate()[​](#_generate "Direct link to _generate")

Run the LLM on the given prompts and input.

> **\_generate**(`prompts`: `string`\[\], `options`: `Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`prompts`

`string`\[\]

`options`

`Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>

#### Returns[​](#returns-6 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[\_generate](/docs/api/llms_base/classes/BaseLLM#_generate)

#### Defined in[​](#defined-in-26 "Direct link to Defined in")

[langchain/src/llms/googlevertexai.ts:91](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/googlevertexai.ts#L91)

### \_generatePrompt()[​](#_generateprompt "Direct link to _generateprompt")

> **\_generatePrompt**(`prompt`: `string`, `options`: `Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>): `Promise`<[`Generation`](/docs/api/schema/interfaces/Generation)\[\]\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`prompt`

`string`

`options`

`Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>

#### Returns[​](#returns-7 "Direct link to Returns")

`Promise`<[`Generation`](/docs/api/schema/interfaces/Generation)\[\]\>

#### Defined in[​](#defined-in-27 "Direct link to Defined in")

[langchain/src/llms/googlevertexai.ts:101](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/googlevertexai.ts#L101)

### \_identifyingParams()[​](#_identifyingparams "Direct link to _identifyingparams")

Get the identifying parameters of the LLM.

> **\_identifyingParams**(): `Record`<`string`, `any`\>

#### Returns[​](#returns-8 "Direct link to Returns")

`Record`<`string`, `any`\>

#### Inherited from[​](#inherited-from-20 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[\_identifyingParams](/docs/api/llms_base/classes/BaseLLM#_identifyingparams)

#### Defined in[​](#defined-in-28 "Direct link to Defined in")

[langchain/src/llms/base.ts:284](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L284)

### \_llmType()[​](#_llmtype "Direct link to _llmtype")

Return the string type key uniquely identifying this class of LLM.

> **\_llmType**(): `string`

#### Returns[​](#returns-9 "Direct link to Returns")

`string`

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[\_llmType](/docs/api/llms_base/classes/BaseLLM#_llmtype)

#### Defined in[​](#defined-in-29 "Direct link to Defined in")

[langchain/src/llms/googlevertexai.ts:87](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/googlevertexai.ts#L87)

### \_modelType()[​](#_modeltype "Direct link to _modeltype")

> **\_modelType**(): `string`

#### Returns[​](#returns-10 "Direct link to Returns")

`string`

#### Inherited from[​](#inherited-from-21 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[\_modelType](/docs/api/llms_base/classes/BaseLLM#_modeltype)

#### Defined in[​](#defined-in-30 "Direct link to Defined in")

[langchain/src/llms/base.ts:304](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L304)

### call()[​](#call "Direct link to call()")

Convenience wrapper for [generate](/docs/api/llms_base/classes/BaseLLM#generate) that takes in a single string prompt and returns a single string output.

> **call**(`prompt`: `string`, `options`?: `string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\>

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`prompt`

`string`

`options?`

`string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-11 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[​](#inherited-from-22 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[call](/docs/api/llms_base/classes/BaseLLM#call)

#### Defined in[​](#defined-in-31 "Direct link to Defined in")

[langchain/src/llms/base.ts:249](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L249)

### extractPredictionFromResponse()[​](#extractpredictionfromresponse "Direct link to extractPredictionFromResponse()")

> **extractPredictionFromResponse**(`result`: `GoogleVertexAILLMResponse`<`TextPrediction`\>): `TextPrediction`

#### Parameters[​](#parameters-5 "Direct link to Parameters")

Parameter

Type

`result`

`GoogleVertexAILLMResponse`<`TextPrediction`\>

#### Returns[​](#returns-12 "Direct link to Returns")

`TextPrediction`

#### Defined in[​](#defined-in-32 "Direct link to Defined in")

[langchain/src/llms/googlevertexai.ts:140](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/googlevertexai.ts#L140)

### formatInstance()[​](#formatinstance "Direct link to formatInstance()")

> **formatInstance**(`prompt`: `string`): `GoogleVertexAILLMInstance`

#### Parameters[​](#parameters-6 "Direct link to Parameters")

Parameter

Type

`prompt`

`string`

#### Returns[​](#returns-13 "Direct link to Returns")

`GoogleVertexAILLMInstance`

#### Defined in[​](#defined-in-33 "Direct link to Defined in")

[langchain/src/llms/googlevertexai.ts:134](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/googlevertexai.ts#L134)

### formatInstanceCode()[​](#formatinstancecode "Direct link to formatInstanceCode()")

> **formatInstanceCode**(`prompt`: `string`): `GoogleVertexAILLMInstance`

#### Parameters[​](#parameters-7 "Direct link to Parameters")

Parameter

Type

`prompt`

`string`

#### Returns[​](#returns-14 "Direct link to Returns")

`GoogleVertexAILLMInstance`

#### Defined in[​](#defined-in-34 "Direct link to Defined in")

[langchain/src/llms/googlevertexai.ts:130](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/googlevertexai.ts#L130)

### formatInstanceText()[​](#formatinstancetext "Direct link to formatInstanceText()")

> **formatInstanceText**(`prompt`: `string`): `GoogleVertexAILLMInstance`

#### Parameters[​](#parameters-8 "Direct link to Parameters")

Parameter

Type

`prompt`

`string`

#### Returns[​](#returns-15 "Direct link to Returns")

`GoogleVertexAILLMInstance`

#### Defined in[​](#defined-in-35 "Direct link to Defined in")

[langchain/src/llms/googlevertexai.ts:126](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/googlevertexai.ts#L126)

### generate()[​](#generate "Direct link to generate()")

Run the LLM on the given propmts an input, handling caching.

> **generate**(`prompts`: `string`\[\], `options`?: `string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[​](#parameters-9 "Direct link to Parameters")

Parameter

Type

`prompts`

`string`\[\]

`options?`

`string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-16 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[​](#inherited-from-23 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[generate](/docs/api/llms_base/classes/BaseLLM#generate)

#### Defined in[​](#defined-in-36 "Direct link to Defined in")

[langchain/src/llms/base.ts:177](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L177)

### generatePrompt()[​](#generateprompt "Direct link to generatePrompt()")

> **generatePrompt**(`promptValues`: [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\[\], `options`?: `string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[​](#parameters-10 "Direct link to Parameters")

Parameter

Type

`promptValues`

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\[\]

`options?`

`string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-17 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[​](#inherited-from-24 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[generatePrompt](/docs/api/llms_base/classes/BaseLLM#generateprompt)

#### Defined in[​](#defined-in-37 "Direct link to Defined in")

[langchain/src/llms/base.ts:66](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L66)

### getNumTokens()[​](#getnumtokens "Direct link to getNumTokens()")

> **getNumTokens**(`text`: `string`): `Promise`<`number`\>

#### Parameters[​](#parameters-11 "Direct link to Parameters")

Parameter

Type

`text`

`string`

#### Returns[​](#returns-18 "Direct link to Returns")

`Promise`<`number`\>

#### Inherited from[​](#inherited-from-25 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[getNumTokens](/docs/api/llms_base/classes/BaseLLM#getnumtokens)

#### Defined in[​](#defined-in-38 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:154](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L154)

### invocationParams()[​](#invocationparams "Direct link to invocationParams()")

Get the parameters used to invoke the model

> **invocationParams**(`_options`?: `Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>): `any`

#### Parameters[​](#parameters-12 "Direct link to Parameters")

Parameter

Type

`_options?`

`Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>

#### Returns[​](#returns-19 "Direct link to Returns")

`any`

#### Inherited from[​](#inherited-from-26 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[invocationParams](/docs/api/llms_base/classes/BaseLLM#invocationparams)

#### Defined in[​](#defined-in-39 "Direct link to Defined in")

[langchain/src/llms/base.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L90)

### predict()[​](#predict "Direct link to predict()")

> **predict**(`text`: `string`, `options`?: `string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\>

#### Parameters[​](#parameters-13 "Direct link to Parameters")

Parameter

Type

`text`

`string`

`options?`

`string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-20 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[​](#inherited-from-27 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[predict](/docs/api/llms_base/classes/BaseLLM#predict)

#### Defined in[​](#defined-in-40 "Direct link to Defined in")

[langchain/src/llms/base.ts:262](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L262)

### predictMessages()[​](#predictmessages "Direct link to predictMessages()")

> **predictMessages**(`messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\], `options`?: `string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Parameters[​](#parameters-14 "Direct link to Parameters")

Parameter

Type

`messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]

`options?`

`string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-21 "Direct link to Returns")

`Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Inherited from[​](#inherited-from-28 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[predictMessages](/docs/api/llms_base/classes/BaseLLM#predictmessages)

#### Defined in[​](#defined-in-41 "Direct link to Defined in")

[langchain/src/llms/base.ts:270](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L270)

### serialize()[​](#serialize "Direct link to serialize()")

Return a json-like object representing this LLM.

> **serialize**(): [`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Returns[​](#returns-22 "Direct link to Returns")

[`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Inherited from[​](#inherited-from-29 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[serialize](/docs/api/llms_base/classes/BaseLLM#serialize)

#### Defined in[​](#defined-in-42 "Direct link to Defined in")

[langchain/src/llms/base.ts:296](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L296)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-23 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-30 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[toJSON](/docs/api/llms_base/classes/BaseLLM#tojson)

#### Defined in[​](#defined-in-43 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-24 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-31 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[toJSONNotImplemented](/docs/api/llms_base/classes/BaseLLM#tojsonnotimplemented)

#### Defined in[​](#defined-in-44 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)

### deserialize()[​](#deserialize "Direct link to deserialize()")

Load an LLM from a json-like object describing it.

> `Static` **deserialize**(`data`: [`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)): `Promise`<[`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)\>

#### Parameters[​](#parameters-15 "Direct link to Parameters")

Parameter

Type

`data`

[`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Returns[​](#returns-25 "Direct link to Returns")

`Promise`<[`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)\>

#### Inherited from[​](#inherited-from-32 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[deserialize](/docs/api/llms_base/classes/BaseLLM#deserialize)

#### Defined in[​](#defined-in-45 "Direct link to Defined in")

[langchain/src/llms/base.ts:311](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L311)