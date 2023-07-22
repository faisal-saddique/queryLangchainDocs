AlephAlpha
==========

Base interface for language model parameters. A subclass of [BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel) should have a constructor that takes in a parameter that extends this interface.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`LLM`](/docs/api/llms_base/classes/LLM).**AlephAlpha**

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   [`AlephAlphaInput`](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new AlephAlpha**(`fields`: `Partial`<[`AlephAlpha`](/docs/api/llms_aleph_alpha/classes/AlephAlpha)\>): [`AlephAlpha`](/docs/api/llms_aleph_alpha/classes/AlephAlpha)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields`

`Partial`<[`AlephAlpha`](/docs/api/llms_aleph_alpha/classes/AlephAlpha)\>

#### Returns[​](#returns "Direct link to Returns")

[`AlephAlpha`](/docs/api/llms_aleph_alpha/classes/AlephAlpha)

#### Overrides[​](#overrides "Direct link to Overrides")

[LLM](/docs/api/llms_base/classes/LLM).[constructor](/docs/api/llms_base/classes/LLM#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:113](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L113)

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

### base\_url[​](#base_url "Direct link to base_url")

> **base\_url**: `string` = `"https://api.aleph-alpha.com/complete"`

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[base\_url](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#base_url)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:111](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L111)

### caller[​](#caller "Direct link to caller")

> **caller**: `AsyncCaller`

The async caller should be used by subclasses to make any async calls, which will thus benefit from the concurrency and retry logic.

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[caller](/docs/api/llms_base/classes/LLM#caller)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:116](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L116)

### completion\_bias\_exclusion\_first\_token\_only[​](#completion_bias_exclusion_first_token_only "Direct link to completion_bias_exclusion_first_token_only")

> **completion\_bias\_exclusion\_first\_token\_only**: `boolean`

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[completion\_bias\_exclusion\_first\_token\_only](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#completion_bias_exclusion_first_token_only)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:101](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L101)

### completion\_bias\_inclusion\_first\_token\_only[​](#completion_bias_inclusion_first_token_only "Direct link to completion_bias_inclusion_first_token_only")

> **completion\_bias\_inclusion\_first\_token\_only**: `boolean`

#### Implementation of[​](#implementation-of-2 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[completion\_bias\_inclusion\_first\_token\_only](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#completion_bias_inclusion_first_token_only)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:97](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L97)

### control\_log\_additive[​](#control_log_additive "Direct link to control_log_additive")

> **control\_log\_additive**: `boolean`

#### Implementation of[​](#implementation-of-3 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[control\_log\_additive](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#control_log_additive)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:105](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L105)

### echo[​](#echo "Direct link to echo")

> **echo**: `boolean`

#### Implementation of[​](#implementation-of-4 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[echo](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#echo)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:49](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L49)

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_kwargs](/docs/api/llms_base/classes/LLM#lc_kwargs)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_namespace](/docs/api/llms_base/classes/LLM#lc_namespace)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/llms/base.ts:51](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L51)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_serializable](/docs/api/llms_base/classes/LLM#lc_serializable)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L55)

### maximum\_tokens[​](#maximum_tokens "Direct link to maximum_tokens")

> **maximum\_tokens**: `number` = `64`

#### Implementation of[​](#implementation-of-5 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[maximum\_tokens](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#maximum_tokens)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:45](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L45)

### minimum\_tokens[​](#minimum_tokens "Direct link to minimum_tokens")

> **minimum\_tokens**: `number` = `0`

#### Implementation of[​](#implementation-of-6 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[minimum\_tokens](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#minimum_tokens)

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:47](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L47)

### model[​](#model "Direct link to model")

> **model**: `string` = `"luminous-base"`

#### Implementation of[​](#implementation-of-7 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[model](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#model)

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:43](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L43)

### raw\_completion[​](#raw_completion "Direct link to raw_completion")

> **raw\_completion**: `boolean`

#### Implementation of[​](#implementation-of-8 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[raw\_completion](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#raw_completion)

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:91](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L91)

### temperature[​](#temperature "Direct link to temperature")

> **temperature**: `number` = `0.0`

#### Implementation of[​](#implementation-of-9 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[temperature](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#temperature)

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:51](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L51)

### top\_k[​](#top_k "Direct link to top_k")

> **top\_k**: `number`

#### Implementation of[​](#implementation-of-10 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[top\_k](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#top_k)

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:53](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L53)

### top\_p[​](#top_p "Direct link to top_p")

> **top\_p**: `number` = `0.0`

#### Implementation of[​](#implementation-of-11 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[top\_p](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#top_p)

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L55)

### verbose[​](#verbose "Direct link to verbose")

> **verbose**: `boolean`

Whether to print out response text.

#### Implementation of[​](#implementation-of-12 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[verbose](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#verbose)

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[verbose](/docs/api/llms_base/classes/LLM#verbose)

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:38](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L38)

### aleph\_alpha\_api\_key?[​](#aleph_alpha_api_key "Direct link to aleph_alpha_api_key?")

> **aleph\_alpha\_api\_key**: `string`

#### Implementation of[​](#implementation-of-13 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[aleph\_alpha\_api\_key](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#aleph_alpha_api_key)

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:107](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L107)

### best\_of?[​](#best_of "Direct link to best_of?")

> **best\_of**: `number`

#### Implementation of[​](#implementation-of-14 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[best\_of](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#best_of)

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:81](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L81)

### cache?[​](#cache "Direct link to cache?")

> **cache**: [`BaseCache`](/docs/api/schema/classes/BaseCache)<[`Generation`](/docs/api/schema/interfaces/Generation)\[\]\>

#### Implementation of[​](#implementation-of-15 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[cache](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#cache)

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[cache](/docs/api/llms_base/classes/LLM#cache)

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/llms/base.ts:53](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L53)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Implementation of[​](#implementation-of-16 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[callbacks](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#callbacks)

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[callbacks](/docs/api/llms_base/classes/LLM#callbacks)

#### Defined in[​](#defined-in-23 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L40)

### completion\_bias\_exclusion?[​](#completion_bias_exclusion "Direct link to completion_bias_exclusion?")

> **completion\_bias\_exclusion**: `string`\[\]

#### Implementation of[​](#implementation-of-17 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[completion\_bias\_exclusion](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#completion_bias_exclusion)

#### Defined in[​](#defined-in-24 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:99](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L99)

### completion\_bias\_inclusion?[​](#completion_bias_inclusion "Direct link to completion_bias_inclusion?")

> **completion\_bias\_inclusion**: `string`\[\]

#### Implementation of[​](#implementation-of-18 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[completion\_bias\_inclusion](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#completion_bias_inclusion)

#### Defined in[​](#defined-in-25 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:95](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L95)

### contextual\_control\_threshold?[​](#contextual_control_threshold "Direct link to contextual_control_threshold?")

> **contextual\_control\_threshold**: `number`

#### Implementation of[​](#implementation-of-19 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[contextual\_control\_threshold](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#contextual_control_threshold)

#### Defined in[​](#defined-in-26 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:103](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L103)

### disable\_optimizations?[​](#disable_optimizations "Direct link to disable_optimizations?")

> **disable\_optimizations**: `boolean`

#### Implementation of[​](#implementation-of-20 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[disable\_optimizations](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#disable_optimizations)

#### Defined in[​](#defined-in-27 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:93](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L93)

### frequency\_penalty?[​](#frequency_penalty "Direct link to frequency_penalty?")

> **frequency\_penalty**: `number`

#### Implementation of[​](#implementation-of-21 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[frequency\_penalty](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#frequency_penalty)

#### Defined in[​](#defined-in-28 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:59](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L59)

### log\_probs?[​](#log_probs "Direct link to log_probs?")

> **log\_probs**: `number`

#### Implementation of[​](#implementation-of-22 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[log\_probs](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#log_probs)

#### Defined in[​](#defined-in-29 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:87](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L87)

### logit\_bias?[​](#logit_bias "Direct link to logit_bias?")

> **logit\_bias**: `object`

#### Implementation of[​](#implementation-of-23 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[logit\_bias](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#logit_bias)

#### Defined in[​](#defined-in-30 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:85](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L85)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Implementation of[​](#implementation-of-24 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[metadata](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#metadata)

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[metadata](/docs/api/llms_base/classes/LLM#metadata)

#### Defined in[​](#defined-in-31 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:44](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L44)

### n?[​](#n "Direct link to n?")

> **n**: `number`

#### Implementation of[​](#implementation-of-25 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[n](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#n)

#### Defined in[​](#defined-in-32 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:83](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L83)

### penalty\_bias?[​](#penalty_bias "Direct link to penalty_bias?")

> **penalty\_bias**: `string`

#### Implementation of[​](#implementation-of-26 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[penalty\_bias](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#penalty_bias)

#### Defined in[​](#defined-in-33 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:75](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L75)

### penalty\_exceptions?[​](#penalty_exceptions "Direct link to penalty_exceptions?")

> **penalty\_exceptions**: `string`\[\]

#### Implementation of[​](#implementation-of-27 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[penalty\_exceptions](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#penalty_exceptions)

#### Defined in[​](#defined-in-34 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:77](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L77)

### penalty\_exceptions\_include\_stop\_sequences?[​](#penalty_exceptions_include_stop_sequences "Direct link to penalty_exceptions_include_stop_sequences?")

> **penalty\_exceptions\_include\_stop\_sequences**: `boolean`

#### Implementation of[​](#implementation-of-28 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[penalty\_exceptions\_include\_stop\_sequences](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#penalty_exceptions_include_stop_sequences)

#### Defined in[​](#defined-in-35 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:79](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L79)

### presence\_penalty?[​](#presence_penalty "Direct link to presence_penalty?")

> **presence\_penalty**: `number`

#### Implementation of[​](#implementation-of-29 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[presence\_penalty](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#presence_penalty)

#### Defined in[​](#defined-in-36 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L57)

### repetition\_penalties\_include\_completion?[​](#repetition_penalties_include_completion "Direct link to repetition_penalties_include_completion?")

> **repetition\_penalties\_include\_completion**: `boolean`

#### Implementation of[​](#implementation-of-30 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[repetition\_penalties\_include\_completion](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#repetition_penalties_include_completion)

#### Defined in[​](#defined-in-37 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:67](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L67)

### repetition\_penalties\_include\_prompt?[​](#repetition_penalties_include_prompt "Direct link to repetition_penalties_include_prompt?")

> **repetition\_penalties\_include\_prompt**: `boolean`

#### Implementation of[​](#implementation-of-31 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[repetition\_penalties\_include\_prompt](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#repetition_penalties_include_prompt)

#### Defined in[​](#defined-in-38 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:65](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L65)

### sequence\_penalty?[​](#sequence_penalty "Direct link to sequence_penalty?")

> **sequence\_penalty**: `number`

#### Implementation of[​](#implementation-of-32 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[sequence\_penalty](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#sequence_penalty)

#### Defined in[​](#defined-in-39 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:61](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L61)

### sequence\_penalty\_min\_length?[​](#sequence_penalty_min_length "Direct link to sequence_penalty_min_length?")

> **sequence\_penalty\_min\_length**: `number`

#### Implementation of[​](#implementation-of-33 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[sequence\_penalty\_min\_length](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#sequence_penalty_min_length)

#### Defined in[​](#defined-in-40 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:63](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L63)

### stop?[​](#stop "Direct link to stop?")

> **stop**: `string`\[\]

#### Implementation of[​](#implementation-of-34 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[stop](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#stop)

#### Defined in[​](#defined-in-41 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:109](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L109)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Implementation of[​](#implementation-of-35 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[tags](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#tags)

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[tags](/docs/api/llms_base/classes/LLM#tags)

#### Defined in[​](#defined-in-42 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L42)

### tokens?[​](#tokens "Direct link to tokens?")

> **tokens**: `boolean`

#### Implementation of[​](#implementation-of-36 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[tokens](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#tokens)

#### Defined in[​](#defined-in-43 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:89](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L89)

### use\_multiplicative\_frequency\_penalty?[​](#use_multiplicative_frequency_penalty "Direct link to use_multiplicative_frequency_penalty?")

> **use\_multiplicative\_frequency\_penalty**: `boolean`

#### Implementation of[​](#implementation-of-37 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[use\_multiplicative\_frequency\_penalty](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#use_multiplicative_frequency_penalty)

#### Defined in[​](#defined-in-44 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:71](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L71)

### use\_multiplicative\_presence\_penalty?[​](#use_multiplicative_presence_penalty "Direct link to use_multiplicative_presence_penalty?")

> **use\_multiplicative\_presence\_penalty**: `boolean`

#### Implementation of[​](#implementation-of-38 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[use\_multiplicative\_presence\_penalty](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#use_multiplicative_presence_penalty)

#### Defined in[​](#defined-in-45 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:69](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L69)

### use\_multiplicative\_sequence\_penalty?[​](#use_multiplicative_sequence_penalty "Direct link to use_multiplicative_sequence_penalty?")

> **use\_multiplicative\_sequence\_penalty**: `boolean`

#### Implementation of[​](#implementation-of-39 "Direct link to Implementation of")

[AlephAlphaInput](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput).[use\_multiplicative\_sequence\_penalty](/docs/api/llms_aleph_alpha/interfaces/AlephAlphaInput#use_multiplicative_sequence_penalty)

#### Defined in[​](#defined-in-46 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:73](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L73)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### callKeys[​](#callkeys "Direct link to callKeys")

Keys that the language model accepts as call options.

> **callKeys**(): `string`\[\]

#### Returns[​](#returns-1 "Direct link to Returns")

`string`\[\]

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

LLM.callKeys

#### Defined in[​](#defined-in-47 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:108](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L108)

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[callKeys](/docs/api/llms_base/classes/LLM#callkeys)

#### Defined in[​](#defined-in-48 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:108](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L108)

### defaultParams[​](#defaultparams "Direct link to defaultParams")

Get the default parameters for calling Aleph Alpha API.

> **defaultParams**(): `object`

#### Returns[​](#returns-2 "Direct link to Returns")

`object`

Member

Type

`best_of`

`undefined` | `number`

`completion_bias_exclusion`

`undefined` | `string`\[\]

`completion_bias_exclusion_first_token_only`

`boolean`

`completion_bias_inclusion`

`undefined` | `string`\[\]

`completion_bias_inclusion_first_token_only`

`boolean`

`contextual_control_threshold`

`undefined` | `number`

`control_log_additive`

`boolean`

`disable_optimizations`

`undefined` | `boolean`

`frequency_penalty`

`undefined` | `number`

`log_probs`

`undefined` | `number`

`logit_bias`

`undefined` | `object`

`maximum_tokens`

`number`

`minimum_tokens`

`number`

`model`

`string`

`n`

`undefined` | `number`

`penalty_bias`

`undefined` | `string`

`penalty_exceptions`

`undefined` | `string`\[\]

`penalty_exceptions_include_stop_sequences`

`undefined` | `boolean`

`presence_penalty`

`undefined` | `number`

`raw_completion`

`boolean`

`repetition_penalties_include_completion`

`undefined` | `boolean`

`repetition_penalties_include_prompt`

`undefined` | `boolean`

`sequence_penalty`

`undefined` | `number`

`sequence_penalty_min_length`

`undefined` | `number`

`temperature`

`number`

`tokens`

`undefined` | `boolean`

`top_k`

`number`

`top_p`

`number`

`use_multiplicative_frequency_penalty`

`undefined` | `boolean`

`use_multiplicative_presence_penalty`

`undefined` | `boolean`

`use_multiplicative_sequence_penalty`

`undefined` | `boolean`

#### Defined in[​](#defined-in-49 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:184](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L184)

#### Defined in[​](#defined-in-50 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:184](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L184)

### identifyingParams[​](#identifyingparams "Direct link to identifyingParams")

Get the identifying parameters for this LLM.

> **identifyingParams**(): `object`

#### Returns[​](#returns-3 "Direct link to Returns")

`object`

Member

Type

`best_of`

`undefined` | `number`

`completion_bias_exclusion`

`undefined` | `string`\[\]

`completion_bias_exclusion_first_token_only`

`boolean`

`completion_bias_inclusion`

`undefined` | `string`\[\]

`completion_bias_inclusion_first_token_only`

`boolean`

`contextual_control_threshold`

`undefined` | `number`

`control_log_additive`

`boolean`

`disable_optimizations`

`undefined` | `boolean`

`frequency_penalty`

`undefined` | `number`

`log_probs`

`undefined` | `number`

`logit_bias`

`undefined` | `object`

`maximum_tokens`

`number`

`minimum_tokens`

`number`

`model`

`string`

`n`

`undefined` | `number`

`penalty_bias`

`undefined` | `string`

`penalty_exceptions`

`undefined` | `string`\[\]

`penalty_exceptions_include_stop_sequences`

`undefined` | `boolean`

`presence_penalty`

`undefined` | `number`

`raw_completion`

`boolean`

`repetition_penalties_include_completion`

`undefined` | `boolean`

`repetition_penalties_include_prompt`

`undefined` | `boolean`

`sequence_penalty`

`undefined` | `number`

`sequence_penalty_min_length`

`undefined` | `number`

`temperature`

`number`

`tokens`

`undefined` | `boolean`

`top_k`

`number`

`top_p`

`number`

`use_multiplicative_frequency_penalty`

`undefined` | `boolean`

`use_multiplicative_presence_penalty`

`undefined` | `boolean`

`use_multiplicative_sequence_penalty`

`undefined` | `boolean`

#### Defined in[​](#defined-in-51 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:229](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L229)

#### Defined in[​](#defined-in-52 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:229](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L229)

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-4 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

LLM.lc\_aliases

#### Defined in[​](#defined-in-53 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_aliases](/docs/api/llms_base/classes/LLM#lc_aliases)

#### Defined in[​](#defined-in-54 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[​](#returns-5 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-15 "Direct link to Inherited from")

LLM.lc\_attributes

#### Defined in[​](#defined-in-55 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

#### Inherited from[​](#inherited-from-16 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_attributes](/docs/api/llms_base/classes/LLM#lc_attributes)

#### Defined in[​](#defined-in-56 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-6 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-17 "Direct link to Inherited from")

LLM.lc\_secrets

#### Defined in[​](#defined-in-57 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-18 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_secrets](/docs/api/llms_base/classes/LLM#lc_secrets)

#### Defined in[​](#defined-in-58 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

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

#### Returns[​](#returns-7 "Direct link to Returns")

`Promise`<`string`\>

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[LLM](/docs/api/llms_base/classes/LLM).[\_call](/docs/api/llms_base/classes/LLM#_call)

#### Defined in[​](#defined-in-59 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:238](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L238)

### \_flattenLLMResult()[​](#_flattenllmresult "Direct link to _flattenllmresult")

> **\_flattenLLMResult**(`llmResult`: [`LLMResult`](/docs/api/schema/types/LLMResult)): [`LLMResult`](/docs/api/schema/types/LLMResult)\[\]

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`llmResult`

[`LLMResult`](/docs/api/schema/types/LLMResult)

#### Returns[​](#returns-8 "Direct link to Returns")

[`LLMResult`](/docs/api/schema/types/LLMResult)\[\]

#### Inherited from[​](#inherited-from-19 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[\_flattenLLMResult](/docs/api/llms_base/classes/LLM#_flattenllmresult)

#### Defined in[​](#defined-in-60 "Direct link to Defined in")

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

#### Returns[​](#returns-9 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[​](#inherited-from-20 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[\_generate](/docs/api/llms_base/classes/LLM#_generate)

#### Defined in[​](#defined-in-61 "Direct link to Defined in")

[langchain/src/llms/base.ts:343](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L343)

### \_identifyingParams()[​](#_identifyingparams "Direct link to _identifyingparams")

Get the identifying parameters of the LLM.

> **\_identifyingParams**(): `Record`<`string`, `any`\>

#### Returns[​](#returns-10 "Direct link to Returns")

`Record`<`string`, `any`\>

#### Inherited from[​](#inherited-from-21 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[\_identifyingParams](/docs/api/llms_base/classes/LLM#_identifyingparams)

#### Defined in[​](#defined-in-62 "Direct link to Defined in")

[langchain/src/llms/base.ts:284](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L284)

### \_llmType()[​](#_llmtype "Direct link to _llmtype")

Get the type of LLM.

> **\_llmType**(): `string`

#### Returns[​](#returns-11 "Direct link to Returns")

`string`

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[LLM](/docs/api/llms_base/classes/LLM).[\_llmType](/docs/api/llms_base/classes/LLM#_llmtype)

#### Defined in[​](#defined-in-63 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:234](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L234)

### \_modelType()[​](#_modeltype "Direct link to _modeltype")

> **\_modelType**(): `string`

#### Returns[​](#returns-12 "Direct link to Returns")

`string`

#### Inherited from[​](#inherited-from-22 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[\_modelType](/docs/api/llms_base/classes/LLM#_modeltype)

#### Defined in[​](#defined-in-64 "Direct link to Defined in")

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

#### Returns[​](#returns-13 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[​](#inherited-from-23 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[call](/docs/api/llms_base/classes/LLM#call)

#### Defined in[​](#defined-in-65 "Direct link to Defined in")

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

#### Returns[​](#returns-14 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[​](#inherited-from-24 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[generate](/docs/api/llms_base/classes/LLM#generate)

#### Defined in[​](#defined-in-66 "Direct link to Defined in")

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

#### Returns[​](#returns-15 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[​](#inherited-from-25 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[generatePrompt](/docs/api/llms_base/classes/LLM#generateprompt)

#### Defined in[​](#defined-in-67 "Direct link to Defined in")

[langchain/src/llms/base.ts:66](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L66)

### getNumTokens()[​](#getnumtokens "Direct link to getNumTokens()")

> **getNumTokens**(`text`: `string`): `Promise`<`number`\>

#### Parameters[​](#parameters-7 "Direct link to Parameters")

Parameter

Type

`text`

`string`

#### Returns[​](#returns-16 "Direct link to Returns")

`Promise`<`number`\>

#### Inherited from[​](#inherited-from-26 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[getNumTokens](/docs/api/llms_base/classes/LLM#getnumtokens)

#### Defined in[​](#defined-in-68 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:154](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L154)

### invocationParams()[​](#invocationparams "Direct link to invocationParams()")

Get the parameters used to invoke the model

> **invocationParams**(`_options`?: `Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>): `any`

#### Parameters[​](#parameters-8 "Direct link to Parameters")

Parameter

Type

`_options?`

`Omit`<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>

#### Returns[​](#returns-17 "Direct link to Returns")

`any`

#### Inherited from[​](#inherited-from-27 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[invocationParams](/docs/api/llms_base/classes/LLM#invocationparams)

#### Defined in[​](#defined-in-69 "Direct link to Defined in")

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

#### Returns[​](#returns-18 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[​](#inherited-from-28 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[predict](/docs/api/llms_base/classes/LLM#predict)

#### Defined in[​](#defined-in-70 "Direct link to Defined in")

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

#### Returns[​](#returns-19 "Direct link to Returns")

`Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Inherited from[​](#inherited-from-29 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[predictMessages](/docs/api/llms_base/classes/LLM#predictmessages)

#### Defined in[​](#defined-in-71 "Direct link to Defined in")

[langchain/src/llms/base.ts:270](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L270)

### serialize()[​](#serialize "Direct link to serialize()")

Return a json-like object representing this LLM.

> **serialize**(): [`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Returns[​](#returns-20 "Direct link to Returns")

[`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Inherited from[​](#inherited-from-30 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[serialize](/docs/api/llms_base/classes/LLM#serialize)

#### Defined in[​](#defined-in-72 "Direct link to Defined in")

[langchain/src/llms/base.ts:296](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L296)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-21 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-31 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[toJSON](/docs/api/llms_base/classes/LLM#tojson)

#### Defined in[​](#defined-in-73 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-22 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-32 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[toJSONNotImplemented](/docs/api/llms_base/classes/LLM#tojsonnotimplemented)

#### Defined in[​](#defined-in-74 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)

### validateEnvironment()[​](#validateenvironment "Direct link to validateEnvironment()")

> **validateEnvironment**(): `void`

#### Returns[​](#returns-23 "Direct link to Returns")

`void`

#### Defined in[​](#defined-in-75 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:175](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/aleph_alpha.ts#L175)

### deserialize()[​](#deserialize "Direct link to deserialize()")

Load an LLM from a json-like object describing it.

> `Static` **deserialize**(`data`: [`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)): `Promise`<[`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)\>

#### Parameters[​](#parameters-11 "Direct link to Parameters")

Parameter

Type

`data`

[`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Returns[​](#returns-24 "Direct link to Returns")

`Promise`<[`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)\>

#### Inherited from[​](#inherited-from-33 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[deserialize](/docs/api/llms_base/classes/LLM#deserialize)

#### Defined in[​](#defined-in-76 "Direct link to Defined in")

[langchain/src/llms/base.ts:311](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L311)