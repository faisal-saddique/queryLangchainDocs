CohereInput
===========

Base interface for language model parameters. A subclass of [BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel) should have a constructor that takes in a parameter that extends this interface.

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseLLMParams`](/docs/api/llms_base/interfaces/BaseLLMParams).**CohereInput**

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### apiKey?[](#apikey "Direct link to apiKey?")

> **apiKey**: `string`

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/llms/cohere.ts:16](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/cohere.ts#L16)

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

### maxRetries?[](#maxretries "Direct link to maxRetries?")

> **maxRetries**: `number`

The maximum number of retries that can be made for a single call, with an exponential backoff between each attempt. Defaults to 6.

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[maxRetries](/docs/api/llms_base/interfaces/BaseLLMParams#maxretries)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/util/async_caller.ts#L26)

### maxTokens?[](#maxtokens "Direct link to maxTokens?")

> **maxTokens**: `number`

Maximum number of tokens to generate in the completion.

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/llms/cohere.ts:11](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/cohere.ts#L11)

### metadata?[](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[metadata](/docs/api/llms_base/interfaces/BaseLLMParams#metadata)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:27](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L27)

### model?[](#model "Direct link to model?")

> **model**: `string`

Model to use

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/llms/cohere.ts:14](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/cohere.ts#L14)

### tags?[](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[tags](/docs/api/llms_base/interfaces/BaseLLMParams#tags)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L26)

### temperature?[](#temperature "Direct link to temperature?")

> **temperature**: `number`

Sampling temperature to use

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/llms/cohere.ts:6](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/cohere.ts#L6)

### verbose?[](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[verbose](/docs/api/llms_base/interfaces/BaseLLMParams#verbose)

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:24](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L24)