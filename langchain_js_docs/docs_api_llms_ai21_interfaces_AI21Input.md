AI21Input
=========

Base interface for language model parameters. A subclass of [BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel) should have a constructor that takes in a parameter that extends this interface.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseLLMParams`](/docs/api/llms_base/interfaces/BaseLLMParams).**AI21Input**

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### ai21ApiKey?[​](#ai21apikey "Direct link to ai21ApiKey?")

> **ai21ApiKey**: `string`

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/llms/ai21.ts:14](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L14)

### baseUrl?[​](#baseurl "Direct link to baseUrl?")

> **baseUrl**: `string`

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:26](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L26)

### cache?[​](#cache "Direct link to cache?")

> **cache**: `boolean` | [`BaseCache`](/docs/api/schema/classes/BaseCache)<[`Generation`](/docs/api/schema/interfaces/Generation)\[\]\>

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[cache](/docs/api/llms_base/interfaces/BaseLLMParams#cache)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/llms/base.ts:35](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L35)

### callbackManager?[​](#callbackmanager "Direct link to callbackManager?")

> **callbackManager**: [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Deprecated[​](#deprecated "Direct link to Deprecated")

Use `callbacks` instead

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[callbackManager](/docs/api/llms_base/interfaces/BaseLLMParams#callbackmanager)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:73](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L73)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[callbacks](/docs/api/llms_base/interfaces/BaseLLMParams#callbacks)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L23)

### concurrency?[​](#concurrency "Direct link to concurrency?")

> **concurrency**: `number`

#### Deprecated[​](#deprecated-1 "Direct link to Deprecated")

Use `maxConcurrency` instead

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[concurrency](/docs/api/llms_base/interfaces/BaseLLMParams#concurrency)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/llms/base.ts:34](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L34)

### countPenalty?[​](#countpenalty "Direct link to countPenalty?")

> **countPenalty**: [`AI21PenaltyData`](/docs/api/llms_ai21/types/AI21PenaltyData)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:21](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L21)

### frequencyPenalty?[​](#frequencypenalty "Direct link to frequencyPenalty?")

> **frequencyPenalty**: [`AI21PenaltyData`](/docs/api/llms_ai21/types/AI21PenaltyData)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L22)

### logitBias?[​](#logitbias "Direct link to logitBias?")

> **logitBias**: `Record`<`string`, `number`\>

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:24](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L24)

### maxConcurrency?[​](#maxconcurrency "Direct link to maxConcurrency?")

> **maxConcurrency**: `number`

The maximum number of concurrent calls that can be made. Defaults to `Infinity`, which means no limit.

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[maxConcurrency](/docs/api/llms_base/interfaces/BaseLLMParams#maxconcurrency)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:21](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/util/async_caller.ts#L21)

### maxRetries?[​](#maxretries "Direct link to maxRetries?")

> **maxRetries**: `number`

The maximum number of retries that can be made for a single call, with an exponential backoff between each attempt. Defaults to 6.

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[maxRetries](/docs/api/llms_base/interfaces/BaseLLMParams#maxretries)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:26](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/util/async_caller.ts#L26)

### maxTokens?[​](#maxtokens "Direct link to maxTokens?")

> **maxTokens**: `number`

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:18](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L18)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[metadata](/docs/api/llms_base/interfaces/BaseLLMParams#metadata)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:25](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L25)

### minTokens?[​](#mintokens "Direct link to minTokens?")

> **minTokens**: `number`

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:17](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L17)

### model?[​](#model "Direct link to model?")

> **model**: `string`

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:15](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L15)

### numResults?[​](#numresults "Direct link to numResults?")

> **numResults**: `number`

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L23)

### presencePenalty?[​](#presencepenalty "Direct link to presencePenalty?")

> **presencePenalty**: [`AI21PenaltyData`](/docs/api/llms_ai21/types/AI21PenaltyData)

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:20](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L20)

### stop?[​](#stop "Direct link to stop?")

> **stop**: `string`\[\]

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:25](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L25)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[tags](/docs/api/llms_base/interfaces/BaseLLMParams#tags)

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:24](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L24)

### temperature?[​](#temperature "Direct link to temperature?")

> **temperature**: `number`

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:16](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L16)

### topP?[​](#topp "Direct link to topP?")

> **topP**: `number`

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/llms/ai21.ts:19](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/ai21.ts#L19)

### verbose?[​](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[verbose](/docs/api/llms_base/interfaces/BaseLLMParams#verbose)

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L22)