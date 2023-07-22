GoogleVertexAITextInput
=======================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   `GoogleVertexAIBaseLLMInput`.**GoogleVertexAITextInput**

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### cache?[​](#cache "Direct link to cache?")

> **cache**: `boolean` | [`BaseCache`](/docs/api/schema/classes/BaseCache)<[`Generation`](/docs/api/schema/interfaces/Generation)\[\]\>

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

GoogleVertexAIBaseLLMInput.cache

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/llms/base.ts:35](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L35)

### callbackManager?[​](#callbackmanager "Direct link to callbackManager?")

> **callbackManager**: [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Deprecated[​](#deprecated "Direct link to Deprecated")

Use `callbacks` instead

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

GoogleVertexAIBaseLLMInput.callbackManager

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:73](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L73)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

GoogleVertexAIBaseLLMInput.callbacks

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L23)

### concurrency?[​](#concurrency "Direct link to concurrency?")

> **concurrency**: `number`

#### Deprecated[​](#deprecated-1 "Direct link to Deprecated")

Use `maxConcurrency` instead

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

GoogleVertexAIBaseLLMInput.concurrency

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/llms/base.ts:34](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L34)

### endpoint?[​](#endpoint "Direct link to endpoint?")

> **endpoint**: `string`

Hostname for the API call

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

GoogleVertexAIBaseLLMInput.endpoint

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/types/googlevertexai-types.ts:5](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/types/googlevertexai-types.ts#L5)

### location?[​](#location "Direct link to location?")

> **location**: `string`

Region where the LLM is stored

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

GoogleVertexAIBaseLLMInput.location

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/types/googlevertexai-types.ts:8](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/types/googlevertexai-types.ts#L8)

### maxConcurrency?[​](#maxconcurrency "Direct link to maxConcurrency?")

> **maxConcurrency**: `number`

The maximum number of concurrent calls that can be made. Defaults to `Infinity`, which means no limit.

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

GoogleVertexAIBaseLLMInput.maxConcurrency

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:21](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/util/async_caller.ts#L21)

### maxOutputTokens?[​](#maxoutputtokens "Direct link to maxOutputTokens?")

> **maxOutputTokens**: `number`

Maximum number of tokens to generate in the completion.

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

GoogleVertexAIBaseLLMInput.maxOutputTokens

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/types/googlevertexai-types.ts:21](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/types/googlevertexai-types.ts#L21)

### maxRetries?[​](#maxretries "Direct link to maxRetries?")

> **maxRetries**: `number`

The maximum number of retries that can be made for a single call, with an exponential backoff between each attempt. Defaults to 6.

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

GoogleVertexAIBaseLLMInput.maxRetries

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:26](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/util/async_caller.ts#L26)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

GoogleVertexAIBaseLLMInput.metadata

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:25](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L25)

### model?[​](#model "Direct link to model?")

> **model**: `string`

Model to use

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

GoogleVertexAIBaseLLMInput.model

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/types/googlevertexai-types.ts:11](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/types/googlevertexai-types.ts#L11)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

GoogleVertexAIBaseLLMInput.tags

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:24](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L24)

### temperature?[​](#temperature "Direct link to temperature?")

> **temperature**: `number`

Sampling temperature to use

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

GoogleVertexAIBaseLLMInput.temperature

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/types/googlevertexai-types.ts:16](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/types/googlevertexai-types.ts#L16)

### topK?[​](#topk "Direct link to topK?")

> **topK**: `number`

Top-k changes how the model selects tokens for output.

A top-k of 1 means the selected token is the most probable among all tokens in the model’s vocabulary (also called greedy decoding), while a top-k of 3 means that the next token is selected from among the 3 most probable tokens (using temperature).

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

GoogleVertexAIBaseLLMInput.topK

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/types/googlevertexai-types.ts:43](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/types/googlevertexai-types.ts#L43)

### topP?[​](#topp "Direct link to topP?")

> **topP**: `number`

Top-p changes how the model selects tokens for output.

Tokens are selected from most probable to least until the sum of their probabilities equals the top-p value.

For example, if tokens A, B, and C have a probability of .3, .2, and .1 and the top-p value is .5, then the model will select either A or B as the next token (using temperature).

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

GoogleVertexAIBaseLLMInput.topP

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/types/googlevertexai-types.ts:33](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/types/googlevertexai-types.ts#L33)

### verbose?[​](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Inherited from[​](#inherited-from-15 "Direct link to Inherited from")

GoogleVertexAIBaseLLMInput.verbose

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L22)