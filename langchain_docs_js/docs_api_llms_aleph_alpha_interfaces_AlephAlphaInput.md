AlephAlphaInput
===============

Base interface for language model parameters. A subclass of [BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel) should have a constructor that takes in a parameter that extends this interface.

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseLLMParams`](/docs/api/llms_base/interfaces/BaseLLMParams).**AlephAlphaInput**

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### base\_url[](#base_url "Direct link to base_url")

> **base\_url**: `string`

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:39](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L39)

### completion\_bias\_exclusion\_first\_token\_only[](#completion_bias_exclusion_first_token_only "Direct link to completion_bias_exclusion_first_token_only")

> **completion\_bias\_exclusion\_first\_token\_only**: `boolean`

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:34](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L34)

### completion\_bias\_inclusion\_first\_token\_only[](#completion_bias_inclusion_first_token_only "Direct link to completion_bias_inclusion_first_token_only")

> **completion\_bias\_inclusion\_first\_token\_only**: `boolean`

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:32](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L32)

### control\_log\_additive[](#control_log_additive "Direct link to control_log_additive")

> **control\_log\_additive**: `boolean`

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:36](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L36)

### maximum\_tokens[](#maximum_tokens "Direct link to maximum_tokens")

> **maximum\_tokens**: `number`

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:6](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L6)

### model[](#model "Direct link to model")

> **model**: `string`

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:5](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L5)

### raw\_completion[](#raw_completion "Direct link to raw_completion")

> **raw\_completion**: `boolean`

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:29](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L29)

### aleph\_alpha\_api\_key?[](#aleph_alpha_api_key "Direct link to aleph_alpha_api_key?")

> **aleph\_alpha\_api\_key**: `string`

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:38](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L38)

### best\_of?[](#best_of "Direct link to best_of?")

> **best\_of**: `number`

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:24](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L24)

### cache?[](#cache "Direct link to cache?")

> **cache**: `boolean` | [`BaseCache`](/docs/api/schema/classes/BaseCache)<[`Generation`](/docs/api/schema/interfaces/Generation)\[\]\>

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[cache](/docs/api/llms_base/interfaces/BaseLLMParams#cache)

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/llms/base.ts:38](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L38)

### callbackManager?[](#callbackmanager "Direct link to callbackManager?")

> **callbackManager**: [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Deprecated[](#deprecated "Direct link to Deprecated")

Use `callbacks` instead

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[callbackManager](/docs/api/llms_base/interfaces/BaseLLMParams#callbackmanager)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:79](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L79)

### callbacks?[](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[callbacks](/docs/api/llms_base/interfaces/BaseLLMParams#callbacks)

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:25](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L25)

### completion\_bias\_exclusion?[](#completion_bias_exclusion "Direct link to completion_bias_exclusion?")

> **completion\_bias\_exclusion**: `string`\[\]

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:33](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L33)

### completion\_bias\_inclusion?[](#completion_bias_inclusion "Direct link to completion_bias_inclusion?")

> **completion\_bias\_inclusion**: `string`\[\]

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:31](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L31)

### concurrency?[](#concurrency "Direct link to concurrency?")

> **concurrency**: `number`

#### Deprecated[](#deprecated-1 "Direct link to Deprecated")

Use `maxConcurrency` instead

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[concurrency](/docs/api/llms_base/interfaces/BaseLLMParams#concurrency)

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/llms/base.ts:37](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L37)

### contextual\_control\_threshold?[](#contextual_control_threshold "Direct link to contextual_control_threshold?")

> **contextual\_control\_threshold**: `number`

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:35](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L35)

### disable\_optimizations?[](#disable_optimizations "Direct link to disable_optimizations?")

> **disable\_optimizations**: `boolean`

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:30](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L30)

### echo?[](#echo "Direct link to echo?")

> **echo**: `boolean`

#### Defined in[](#defined-in-17 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:8](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L8)

### frequency\_penalty?[](#frequency_penalty "Direct link to frequency_penalty?")

> **frequency\_penalty**: `number`

#### Defined in[](#defined-in-18 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:13](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L13)

### log\_probs?[](#log_probs "Direct link to log_probs?")

> **log\_probs**: `number`

#### Defined in[](#defined-in-19 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:27](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L27)

### logit\_bias?[](#logit_bias "Direct link to logit_bias?")

> **logit\_bias**: `object`

#### Defined in[](#defined-in-20 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L26)

### maxConcurrency?[](#maxconcurrency "Direct link to maxConcurrency?")

> **maxConcurrency**: `number`

The maximum number of concurrent calls that can be made. Defaults to `Infinity`, which means no limit.

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[maxConcurrency](/docs/api/llms_base/interfaces/BaseLLMParams#maxconcurrency)

#### Defined in[](#defined-in-21 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:21](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/util/async_caller.ts#L21)

### maxRetries?[](#maxretries "Direct link to maxRetries?")

> **maxRetries**: `number`

The maximum number of retries that can be made for a single call, with an exponential backoff between each attempt. Defaults to 6.

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[maxRetries](/docs/api/llms_base/interfaces/BaseLLMParams#maxretries)

#### Defined in[](#defined-in-22 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/util/async_caller.ts#L26)

### metadata?[](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[metadata](/docs/api/llms_base/interfaces/BaseLLMParams#metadata)

#### Defined in[](#defined-in-23 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:27](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L27)

### minimum\_tokens?[](#minimum_tokens "Direct link to minimum_tokens?")

> **minimum\_tokens**: `number`

#### Defined in[](#defined-in-24 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:7](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L7)

### n?[](#n "Direct link to n?")

> **n**: `number`

#### Defined in[](#defined-in-25 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:25](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L25)

### penalty\_bias?[](#penalty_bias "Direct link to penalty_bias?")

> **penalty\_bias**: `string`

#### Defined in[](#defined-in-26 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:21](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L21)

### penalty\_exceptions?[](#penalty_exceptions "Direct link to penalty_exceptions?")

> **penalty\_exceptions**: `string`\[\]

#### Defined in[](#defined-in-27 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:22](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L22)

### penalty\_exceptions\_include\_stop\_sequences?[](#penalty_exceptions_include_stop_sequences "Direct link to penalty_exceptions_include_stop_sequences?")

> **penalty\_exceptions\_include\_stop\_sequences**: `boolean`

#### Defined in[](#defined-in-28 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:23](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L23)

### presence\_penalty?[](#presence_penalty "Direct link to presence_penalty?")

> **presence\_penalty**: `number`

#### Defined in[](#defined-in-29 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:12](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L12)

### repetition\_penalties\_include\_completion?[](#repetition_penalties_include_completion "Direct link to repetition_penalties_include_completion?")

> **repetition\_penalties\_include\_completion**: `boolean`

#### Defined in[](#defined-in-30 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:17](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L17)

### repetition\_penalties\_include\_prompt?[](#repetition_penalties_include_prompt "Direct link to repetition_penalties_include_prompt?")

> **repetition\_penalties\_include\_prompt**: `boolean`

#### Defined in[](#defined-in-31 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:16](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L16)

### sequence\_penalty?[](#sequence_penalty "Direct link to sequence_penalty?")

> **sequence\_penalty**: `number`

#### Defined in[](#defined-in-32 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:14](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L14)

### sequence\_penalty\_min\_length?[](#sequence_penalty_min_length "Direct link to sequence_penalty_min_length?")

> **sequence\_penalty\_min\_length**: `number`

#### Defined in[](#defined-in-33 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:15](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L15)

### stop?[](#stop "Direct link to stop?")

> **stop**: `string`\[\]

#### Defined in[](#defined-in-34 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:37](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L37)

### tags?[](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[tags](/docs/api/llms_base/interfaces/BaseLLMParams#tags)

#### Defined in[](#defined-in-35 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L26)

### temperature?[](#temperature "Direct link to temperature?")

> **temperature**: `number`

#### Defined in[](#defined-in-36 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:9](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L9)

### tokens?[](#tokens "Direct link to tokens?")

> **tokens**: `boolean`

#### Defined in[](#defined-in-37 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:28](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L28)

### top\_k?[](#top_k "Direct link to top_k?")

> **top\_k**: `number`

#### Defined in[](#defined-in-38 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:10](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L10)

### top\_p?[](#top_p "Direct link to top_p?")

> **top\_p**: `number`

#### Defined in[](#defined-in-39 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:11](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L11)

### use\_multiplicative\_frequency\_penalty?[](#use_multiplicative_frequency_penalty "Direct link to use_multiplicative_frequency_penalty?")

> **use\_multiplicative\_frequency\_penalty**: `boolean`

#### Defined in[](#defined-in-40 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:19](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L19)

### use\_multiplicative\_presence\_penalty?[](#use_multiplicative_presence_penalty "Direct link to use_multiplicative_presence_penalty?")

> **use\_multiplicative\_presence\_penalty**: `boolean`

#### Defined in[](#defined-in-41 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:18](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L18)

### use\_multiplicative\_sequence\_penalty?[](#use_multiplicative_sequence_penalty "Direct link to use_multiplicative_sequence_penalty?")

> **use\_multiplicative\_sequence\_penalty**: `boolean`

#### Defined in[](#defined-in-42 "Direct link to Defined in")

[langchain/src/llms/aleph\_alpha.ts:20](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/aleph_alpha.ts#L20)

### verbose?[](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[verbose](/docs/api/llms_base/interfaces/BaseLLMParams#verbose)

#### Defined in[](#defined-in-43 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:24](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L24)