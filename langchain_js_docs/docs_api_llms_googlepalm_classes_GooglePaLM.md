GooglePaLM
==========

Google Palm 2 Language Model Wrapper to generate texts

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`LLM`](/docs/api/llms_base/classes/LLM).**GooglePaLM**

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   [`GooglePaLMTextInput`](/docs/api/llms_googlepalm/interfaces/GooglePaLMTextInput)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new GooglePaLM**(`fields`?: [`GooglePaLMTextInput`](/docs/api/llms_googlepalm/interfaces/GooglePaLMTextInput)): [`GooglePaLM`](/docs/api/llms_googlepalm/classes/GooglePaLM)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields?`

[`GooglePaLMTextInput`](/docs/api/llms_googlepalm/interfaces/GooglePaLMTextInput)

#### Returns[​](#returns "Direct link to Returns")

[`GooglePaLM`](/docs/api/llms_googlepalm/classes/GooglePaLM)

#### Overrides[​](#overrides "Direct link to Overrides")

[LLM](/docs/api/llms_base/classes/LLM).[constructor](/docs/api/llms_base/classes/LLM#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/llms/googlepalm.ts:111](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/googlepalm.ts#L111)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### CallOptions[​](#calloptions "Direct link to CallOptions")

> **CallOptions**: [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[CallOptions](/docs/api/llms_base/classes/LLM#calloptions)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/llms/base.ts:44](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L44)

### ParsedCallOptions[​](#parsedcalloptions "Direct link to ParsedCallOptions")

> **ParsedCallOptions**: `Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[ParsedCallOptions](/docs/api/llms_base/classes/LLM#parsedcalloptions)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/llms/base.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L46)

### caller[​](#caller "Direct link to caller")

> **caller**: `AsyncCaller`

The async caller should be used by subclasses to make any async calls, which will thus benefit from the concurrency and retry logic.

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[caller](/docs/api/llms_base/classes/LLM#caller)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:116](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L116)

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_kwargs](/docs/api/llms_base/classes/LLM#lc_kwargs)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_namespace](/docs/api/llms_base/classes/LLM#lc_namespace)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/llms/base.ts:51](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L51)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_serializable](/docs/api/llms_base/classes/LLM#lc_serializable)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L55)

### modelName[​](#modelname "Direct link to modelName")

> **modelName**: `string` = `"models/text-bison-001"`

Model Name to use

Note: The format must follow the pattern - `models/{model}`

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

[GooglePaLMTextInput](/docs/api/llms_googlepalm/interfaces/GooglePaLMTextInput).[modelName](/docs/api/llms_googlepalm/interfaces/GooglePaLMTextInput#modelname)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/llms/googlepalm.ts:93](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/googlepalm.ts#L93)

### stopSequences[​](#stopsequences "Direct link to stopSequences")

> **stopSequences**: `string`\[\] = `[]`

The set of character sequences (up to 5) that will stop output generation. If specified, the API will stop at the first appearance of a stop sequence.

Note: The stop sequence will not be included as part of the response.

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

[GooglePaLMTextInput](/docs/api/llms_googlepalm/interfaces/GooglePaLMTextInput).[stopSequences](/docs/api/llms_googlepalm/interfaces/GooglePaLMTextInput#stopsequences)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/llms/googlepalm.ts:103](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/googlepalm.ts#L103)

### verbose[​](#verbose "Direct link to verbose")

> **verbose**: `boolean`

Whether to print out response text.

#### Implementation of[​](#implementation-of-2 "Direct link to Implementation of")

[GooglePaLMTextInput](/docs/api/llms_googlepalm/interfaces/GooglePaLMTextInput).[verbose](/docs/api/llms_googlepalm/interfaces/GooglePaLMTextInput#verbose)

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[verbose](/docs/api/llms_base/classes/LLM#verbose)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:38](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L38)

### apiKey?[​](#apikey "Direct link to apiKey?")

> **apiKey**: `string`

Google Palm API key to use

#### Implementation of[​](#implementation-of-3 "Direct link to Implementation of")

[GooglePaLMTextInput](/docs/api/llms_googlepalm/interfaces/GooglePaLMTextInput).[apiKey](/docs/api/llms_googlepalm/interfaces/GooglePaLMTextInput#apikey)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/llms/googlepalm.ts:107](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/googlepalm.ts#L107)

### cache?[​](#cache "Direct link to cache?")

> **cache**: [`BaseCache`](/docs/api/schema/classes/BaseCache)<[`Generation`](/docs/api/schema/interfaces/Generation)\[\]\>

#### Implementation of[​](#implementation-of-4 "Direct link to Implementation of")

[GooglePaLMTextInput](/docs/api/llms_googlepalm/interfaces/GooglePaLMTextInput).[cache](/docs/api/llms_googlepalm/interfaces/GooglePaLMTextInput#cache)

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[cache](/docs/api/llms_base/classes/LLM#cache)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/llms/base.ts:53](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L53)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Implementation of[​](#implementation-of-5 "Direct link to Implementation of")

[GooglePaLMTextInput](/docs/api/llms_googlepalm/interfaces/GooglePaLMTextInput).[callbacks](/docs/api/llms_googlepalm/interfaces/GooglePaLMTextInput#callbacks)

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[callbacks](/docs/api/llms_base/classes/LLM#callbacks)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L40)

### maxOutputTokens?[​](#maxoutputtokens "Direct link to maxOutputTokens?")

> **maxOutputTokens**: `number`

Maximum number of tokens to generate in the completion.

#### Implementation of[​](#implementation-of-6 "Direct link to Implementation of")

[GooglePaLMTextInput](/docs/api/llms_googlepalm/interfaces/GooglePaLMTextInput).[maxOutputTokens](/docs/api/llms_googlepalm/interfaces/GooglePaLMTextInput#maxoutputtokens)

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/llms/googlepalm.ts:97](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/googlepalm.ts#L97)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Implementation of[​](#implementation-of-7 "Direct link to Implementation of")

[GooglePaLMTextInput](/docs/api/llms_googlepalm/interfaces/GooglePaLMTextInput).[metadata](/docs/api/llms_googlepalm/interfaces/GooglePaLMTextInput#metadata)

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[metadata](/docs/api/llms_base/classes/LLM#metadata)

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:44](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L44)

### safetySettings?[​](#safetysettings "Direct link to safetySettings?")

> **safetySettings**: `ISafetySetting`\[\]

A list of unique `SafetySetting` instances for blocking unsafe content. The API will block any prompts and responses that fail to meet the thresholds set by these settings. If there is no `SafetySetting` for a given `SafetyCategory` provided in the list, the API will use the default safety setting for that category.

#### Implementation of[​](#implementation-of-8 "Direct link to Implementation of")

[GooglePaLMTextInput](/docs/api/llms_googlepalm/interfaces/GooglePaLMTextInput).[safetySettings](/docs/api/llms_googlepalm/interfaces/GooglePaLMTextInput#safetysettings)

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/llms/googlepalm.ts:105](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/googlepalm.ts#L105)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Implementation of[​](#implementation-of-9 "Direct link to Implementation of")

[GooglePaLMTextInput](/docs/api/llms_googlepalm/interfaces/GooglePaLMTextInput).[tags](/docs/api/llms_googlepalm/interfaces/GooglePaLMTextInput#tags)

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[tags](/docs/api/llms_base/classes/LLM#tags)

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L42)

### temperature?[​](#temperature "Direct link to temperature?")

> **temperature**: `number`

Controls the randomness of the output.

Values can range from \[0.0,1.0\], inclusive. A value closer to 1.0 will produce responses that are more varied and creative, while a value closer to 0.0 will typically result in more straightforward responses from the model.

Note: The default value varies by model

#### Implementation of[​](#implementation-of-10 "Direct link to Implementation of")

[GooglePaLMTextInput](/docs/api/llms_googlepalm/interfaces/GooglePaLMTextInput).[temperature](/docs/api/llms_googlepalm/interfaces/GooglePaLMTextInput#temperature)

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/llms/googlepalm.ts:95](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/googlepalm.ts#L95)

### topK?[​](#topk "Direct link to topK?")

> **topK**: `number`

Top-k changes how the model selects tokens for output.

A top-k of 1 means the selected token is the most probable among all tokens in the model’s vocabulary (also called greedy decoding), while a top-k of 3 means that the next token is selected from among the 3 most probable tokens (using temperature).

Note: The default value varies by model

#### Implementation of[​](#implementation-of-11 "Direct link to Implementation of")

[GooglePaLMTextInput](/docs/api/llms_googlepalm/interfaces/GooglePaLMTextInput).[topK](/docs/api/llms_googlepalm/interfaces/GooglePaLMTextInput#topk)

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/llms/googlepalm.ts:101](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/googlepalm.ts#L101)

### topP?[​](#topp "Direct link to topP?")

> **topP**: `number`

Top-p changes how the model selects tokens for output.

Tokens are selected from most probable to least until the sum of their probabilities equals the top-p value.

For example, if tokens A, B, and C have a probability of .3, .2, and .1 and the top-p value is .5, then the model will select either A or B as the next token (using temperature).

Note: The default value varies by model

#### Implementation of[​](#implementation-of-12 "Direct link to Implementation of")

[GooglePaLMTextInput](/docs/api/llms_googlepalm/interfaces/GooglePaLMTextInput).[topP](/docs/api/llms_googlepalm/interfaces/GooglePaLMTextInput#topp)

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/llms/googlepalm.ts:99](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/googlepalm.ts#L99)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### callKeys[​](#callkeys "Direct link to callKeys")

Keys that the language model accepts as call options.

> **callKeys**(): `string`\[\]

#### Returns[​](#returns-1 "Direct link to Returns")

`string`\[\]

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

LLM.callKeys

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:108](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L108)

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[callKeys](/docs/api/llms_base/classes/LLM#callkeys)

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:108](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L108)

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

LLM.lc\_aliases

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_aliases](/docs/api/llms_base/classes/LLM#lc_aliases)

#### Defined in[​](#defined-in-23 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-15 "Direct link to Inherited from")

LLM.lc\_attributes

#### Defined in[​](#defined-in-24 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

#### Inherited from[​](#inherited-from-16 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_attributes](/docs/api/llms_base/classes/LLM#lc_attributes)

#### Defined in[​](#defined-in-25 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-4 "Direct link to Returns")

`undefined` | {}

#### Overrides[​](#overrides-1 "Direct link to Overrides")

LLM.lc\_secrets

#### Defined in[​](#defined-in-26 "Direct link to Defined in")

[langchain/src/llms/googlepalm.ts:87](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/googlepalm.ts#L87)

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_secrets](/docs/api/llms_base/classes/LLM#lc_secrets)

#### Defined in[​](#defined-in-27 "Direct link to Defined in")

[langchain/src/llms/googlepalm.ts:87](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/googlepalm.ts#L87)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### \_call()[​](#_call "Direct link to _call")

Run the LLM on the given prompt and input.

> **\_call**(`prompt`: `string`, `options`: `Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>): `Promise`<`string`\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`prompt`

`string`

`options`

`Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>

#### Returns[​](#returns-5 "Direct link to Returns")

`Promise`<`string`\>

#### Overrides[​](#overrides-3 "Direct link to Overrides")

[LLM](/docs/api/llms_base/classes/LLM).[\_call](/docs/api/llms_base/classes/LLM#_call)

#### Defined in[​](#defined-in-28 "Direct link to Defined in")

[langchain/src/llms/googlepalm.ts:167](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/googlepalm.ts#L167)

### \_flattenLLMResult()[​](#_flattenllmresult "Direct link to _flattenllmresult")

> **\_flattenLLMResult**(`llmResult`: [`LLMResult`](/docs/api/schema/types/LLMResult)): [`LLMResult`](/docs/api/schema/types/LLMResult)\[\]

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`llmResult`

[`LLMResult`](/docs/api/schema/types/LLMResult)

#### Returns[​](#returns-6 "Direct link to Returns")

[`LLMResult`](/docs/api/schema/types/LLMResult)\[\]

#### Inherited from[​](#inherited-from-17 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[\_flattenLLMResult](/docs/api/llms_base/classes/LLM#_flattenllmresult)

#### Defined in[​](#defined-in-29 "Direct link to Defined in")

[langchain/src/llms/base.ts:94](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L94)

### \_generate()[​](#_generate "Direct link to _generate")

Run the LLM on the given prompts and input.

> **\_generate**(`prompts`: `string`\[\], `options`: `Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>, `runManager`?: [`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`prompts`

`string`\[\]

`options`

`Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>

`runManager?`

[`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)

#### Returns[​](#returns-7 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[​](#inherited-from-18 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[\_generate](/docs/api/llms_base/classes/LLM#_generate)

#### Defined in[​](#defined-in-30 "Direct link to Defined in")

[langchain/src/llms/base.ts:343](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L343)

### \_identifyingParams()[​](#_identifyingparams "Direct link to _identifyingparams")

Get the identifying parameters of the LLM.

> **\_identifyingParams**(): `Record`<`string`, `any`\>

#### Returns[​](#returns-8 "Direct link to Returns")

`Record`<`string`, `any`\>

#### Inherited from[​](#inherited-from-19 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[\_identifyingParams](/docs/api/llms_base/classes/LLM#_identifyingparams)

#### Defined in[​](#defined-in-31 "Direct link to Defined in")

[langchain/src/llms/base.ts:284](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L284)

### \_llmType()[​](#_llmtype "Direct link to _llmtype")

Return the string type key uniquely identifying this class of LLM.

> **\_llmType**(): `string`

#### Returns[​](#returns-9 "Direct link to Returns")

`string`

#### Overrides[​](#overrides-4 "Direct link to Overrides")

[LLM](/docs/api/llms_base/classes/LLM).[\_llmType](/docs/api/llms_base/classes/LLM#_llmtype)

#### Defined in[​](#defined-in-32 "Direct link to Defined in")

[langchain/src/llms/googlepalm.ts:163](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/googlepalm.ts#L163)

### \_modelType()[​](#_modeltype "Direct link to _modeltype")

> **\_modelType**(): `string`

#### Returns[​](#returns-10 "Direct link to Returns")

`string`

#### Inherited from[​](#inherited-from-20 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[\_modelType](/docs/api/llms_base/classes/LLM#_modeltype)

#### Defined in[​](#defined-in-33 "Direct link to Defined in")

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

#### Inherited from[​](#inherited-from-21 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[call](/docs/api/llms_base/classes/LLM#call)

#### Defined in[​](#defined-in-34 "Direct link to Defined in")

[langchain/src/llms/base.ts:249](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L249)

### generate()[​](#generate "Direct link to generate()")

Run the LLM on the given propmts an input, handling caching.

> **generate**(`prompts`: `string`\[\], `options`?: `string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[​](#parameters-5 "Direct link to Parameters")

Parameter

Type

`prompts`

`string`\[\]

`options?`

`string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-12 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[​](#inherited-from-22 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[generate](/docs/api/llms_base/classes/LLM#generate)

#### Defined in[​](#defined-in-35 "Direct link to Defined in")

[langchain/src/llms/base.ts:177](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L177)

### generatePrompt()[​](#generateprompt "Direct link to generatePrompt()")

> **generatePrompt**(`promptValues`: [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\[\], `options`?: `string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[​](#parameters-6 "Direct link to Parameters")

Parameter

Type

`promptValues`

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\[\]

`options?`

`string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-13 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[​](#inherited-from-23 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[generatePrompt](/docs/api/llms_base/classes/LLM#generateprompt)

#### Defined in[​](#defined-in-36 "Direct link to Defined in")

[langchain/src/llms/base.ts:66](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L66)

### getNumTokens()[​](#getnumtokens "Direct link to getNumTokens()")

> **getNumTokens**(`text`: `string`): `Promise`<`number`\>

#### Parameters[​](#parameters-7 "Direct link to Parameters")

Parameter

Type

`text`

`string`

#### Returns[​](#returns-14 "Direct link to Returns")

`Promise`<`number`\>

#### Inherited from[​](#inherited-from-24 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[getNumTokens](/docs/api/llms_base/classes/LLM#getnumtokens)

#### Defined in[​](#defined-in-37 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:154](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L154)

### invocationParams()[​](#invocationparams "Direct link to invocationParams()")

Get the parameters used to invoke the model

> **invocationParams**(`_options`?: `Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>): `any`

#### Parameters[​](#parameters-8 "Direct link to Parameters")

Parameter

Type

`_options?`

`Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>

#### Returns[​](#returns-15 "Direct link to Returns")

`any`

#### Inherited from[​](#inherited-from-25 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[invocationParams](/docs/api/llms_base/classes/LLM#invocationparams)

#### Defined in[​](#defined-in-38 "Direct link to Defined in")

[langchain/src/llms/base.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L90)

### predict()[​](#predict "Direct link to predict()")

> **predict**(`text`: `string`, `options`?: `string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\>

#### Parameters[​](#parameters-9 "Direct link to Parameters")

Parameter

Type

`text`

`string`

`options?`

`string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-16 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[​](#inherited-from-26 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[predict](/docs/api/llms_base/classes/LLM#predict)

#### Defined in[​](#defined-in-39 "Direct link to Defined in")

[langchain/src/llms/base.ts:262](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L262)

### predictMessages()[​](#predictmessages "Direct link to predictMessages()")

> **predictMessages**(`messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\], `options`?: `string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Parameters[​](#parameters-10 "Direct link to Parameters")

Parameter

Type

`messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]

`options?`

`string`\[\] | [`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-17 "Direct link to Returns")

`Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Inherited from[​](#inherited-from-27 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[predictMessages](/docs/api/llms_base/classes/LLM#predictmessages)

#### Defined in[​](#defined-in-40 "Direct link to Defined in")

[langchain/src/llms/base.ts:270](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L270)

### serialize()[​](#serialize "Direct link to serialize()")

Return a json-like object representing this LLM.

> **serialize**(): [`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Returns[​](#returns-18 "Direct link to Returns")

[`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Inherited from[​](#inherited-from-28 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[serialize](/docs/api/llms_base/classes/LLM#serialize)

#### Defined in[​](#defined-in-41 "Direct link to Defined in")

[langchain/src/llms/base.ts:296](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L296)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-19 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-29 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[toJSON](/docs/api/llms_base/classes/LLM#tojson)

#### Defined in[​](#defined-in-42 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-20 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-30 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[toJSONNotImplemented](/docs/api/llms_base/classes/LLM#tojsonnotimplemented)

#### Defined in[​](#defined-in-43 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)

### deserialize()[​](#deserialize "Direct link to deserialize()")

Load an LLM from a json-like object describing it.

> `Static` **deserialize**(`data`: [`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)): `Promise`<[`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)\>

#### Parameters[​](#parameters-11 "Direct link to Parameters")

Parameter

Type

`data`

[`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Returns[​](#returns-21 "Direct link to Returns")

`Promise`<[`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)\>

#### Inherited from[​](#inherited-from-31 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[deserialize](/docs/api/llms_base/classes/LLM#deserialize)

#### Defined in[​](#defined-in-44 "Direct link to Defined in")

[langchain/src/llms/base.ts:311](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L311)

### \_generateText()[​](#_generatetext "Direct link to _generatetext")

> `Protected` **\_generateText**(`prompt`: `string`): `Promise`<`undefined` | null | `string`\>

#### Parameters[​](#parameters-12 "Direct link to Parameters")

Parameter

Type

`prompt`

`string`

#### Returns[​](#returns-22 "Direct link to Returns")

`Promise`<`undefined` | null | `string`\>

#### Defined in[​](#defined-in-45 "Direct link to Defined in")

[langchain/src/llms/googlepalm.ts:179](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/googlepalm.ts#L179)