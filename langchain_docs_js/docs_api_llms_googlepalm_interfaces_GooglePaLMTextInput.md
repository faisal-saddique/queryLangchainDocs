GooglePaLMTextInput
===================

Input for Text generation for Google Palm

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseLLMParams`](/docs/api/llms_base/interfaces/BaseLLMParams).**GooglePaLMTextInput**

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### apiKey?[](#apikey "Direct link to apiKey?")

> **apiKey**: `string`

Google Palm API key to use

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/llms/googlepalm.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/googlepalm.ts#L80)

### cache?[](#cache "Direct link to cache?")

> **cache**: `boolean` | [`BaseCache`](/docs/api/schema/classes/BaseCache)<[`Generation`](/docs/api/schema/interfaces/Generation)\[\]\>

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[cache](/docs/api/llms_base/interfaces/BaseLLMParams#cache)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/llms/base.ts:38](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L38)

### callbackManager?[](#callbackmanager "Direct link to callbackManager?")

> **callbackManager**: [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Deprecated[](#deprecated "Direct link to Deprecated")

Use `callbacks` instead

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[callbackManager](/docs/api/llms_base/interfaces/BaseLLMParams#callbackmanager)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:79](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L79)

### callbacks?[](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[callbacks](/docs/api/llms_base/interfaces/BaseLLMParams#callbacks)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:25](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L25)

### concurrency?[](#concurrency "Direct link to concurrency?")

> **concurrency**: `number`

#### Deprecated[](#deprecated-1 "Direct link to Deprecated")

Use `maxConcurrency` instead

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[concurrency](/docs/api/llms_base/interfaces/BaseLLMParams#concurrency)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/llms/base.ts:37](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L37)

### maxConcurrency?[](#maxconcurrency "Direct link to maxConcurrency?")

> **maxConcurrency**: `number`

The maximum number of concurrent calls that can be made. Defaults to `Infinity`, which means no limit.

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[maxConcurrency](/docs/api/llms_base/interfaces/BaseLLMParams#maxconcurrency)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:21](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/util/async_caller.ts#L21)

### maxOutputTokens?[](#maxoutputtokens "Direct link to maxOutputTokens?")

> **maxOutputTokens**: `number`

Maximum number of tokens to generate in the completion.

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/llms/googlepalm.ts:32](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/googlepalm.ts#L32)

### maxRetries?[](#maxretries "Direct link to maxRetries?")

> **maxRetries**: `number`

The maximum number of retries that can be made for a single call, with an exponential backoff between each attempt. Defaults to 6.

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[maxRetries](/docs/api/llms_base/interfaces/BaseLLMParams#maxretries)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/util/async_caller.ts#L26)

### metadata?[](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[metadata](/docs/api/llms_base/interfaces/BaseLLMParams#metadata)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:27](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L27)

### modelName?[](#modelname "Direct link to modelName?")

> **modelName**: `string`

Model Name to use

Note: The format must follow the pattern - `models/{model}`

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/llms/googlepalm.ts:15](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/googlepalm.ts#L15)

### safetySettings?[](#safetysettings "Direct link to safetySettings?")

> **safetySettings**: `ISafetySetting`\[\]

A list of unique `SafetySetting` instances for blocking unsafe content. The API will block any prompts and responses that fail to meet the thresholds set by these settings. If there is no `SafetySetting` for a given `SafetyCategory` provided in the list, the API will use the default safety setting for that category.

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/llms/googlepalm.ts:75](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/googlepalm.ts#L75)

### stopSequences?[](#stopsequences "Direct link to stopSequences?")

> **stopSequences**: `string`\[\]

The set of character sequences (up to 5) that will stop output generation. If specified, the API will stop at the first appearance of a stop sequence.

Note: The stop sequence will not be included as part of the response.

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/llms/googlepalm.ts:67](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/googlepalm.ts#L67)

### tags?[](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[tags](/docs/api/llms_base/interfaces/BaseLLMParams#tags)

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L26)

### temperature?[](#temperature "Direct link to temperature?")

> **temperature**: `number`

Controls the randomness of the output.

Values can range from \[0.0,1.0\], inclusive. A value closer to 1.0 will produce responses that are more varied and creative, while a value closer to 0.0 will typically result in more straightforward responses from the model.

Note: The default value varies by model

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/llms/googlepalm.ts:27](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/googlepalm.ts#L27)

### topK?[](#topk "Direct link to topK?")

> **topK**: `number`

Top-k changes how the model selects tokens for output.

A top-k of 1 means the selected token is the most probable among all tokens in the model’s vocabulary (also called greedy decoding), while a top-k of 3 means that the next token is selected from among the 3 most probable tokens (using temperature).

Note: The default value varies by model

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/llms/googlepalm.ts:58](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/googlepalm.ts#L58)

### topP?[](#topp "Direct link to topP?")

> **topP**: `number`

Top-p changes how the model selects tokens for output.

Tokens are selected from most probable to least until the sum of their probabilities equals the top-p value.

For example, if tokens A, B, and C have a probability of .3, .2, and .1 and the top-p value is .5, then the model will select either A or B as the next token (using temperature).

Note: The default value varies by model

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/llms/googlepalm.ts:46](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/googlepalm.ts#L46)

### verbose?[](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[verbose](/docs/api/llms_base/interfaces/BaseLLMParams#verbose)

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:24](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L24)