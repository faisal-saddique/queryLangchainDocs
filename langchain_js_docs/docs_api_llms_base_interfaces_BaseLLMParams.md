BaseLLMParams
=============

Base interface for language model parameters. A subclass of [BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel) should have a constructor that takes in a parameter that extends this interface.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseLanguageModelParams`](/docs/api/base_language/interfaces/BaseLanguageModelParams).**BaseLLMParams**

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### cache?[​](#cache "Direct link to cache?")

> **cache**: `boolean` | [`BaseCache`](/docs/api/schema/classes/BaseCache)<[`Generation`](/docs/api/schema/interfaces/Generation)\[\]\>

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/llms/base.ts:35](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L35)

### callbackManager?[​](#callbackmanager "Direct link to callbackManager?")

> **callbackManager**: [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Deprecated[​](#deprecated "Direct link to Deprecated")

Use `callbacks` instead

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BaseLanguageModelParams](/docs/api/base_language/interfaces/BaseLanguageModelParams).[callbackManager](/docs/api/base_language/interfaces/BaseLanguageModelParams#callbackmanager)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:73](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L73)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[BaseLanguageModelParams](/docs/api/base_language/interfaces/BaseLanguageModelParams).[callbacks](/docs/api/base_language/interfaces/BaseLanguageModelParams#callbacks)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L23)

### concurrency?[​](#concurrency "Direct link to concurrency?")

> **concurrency**: `number`

#### Deprecated[​](#deprecated-1 "Direct link to Deprecated")

Use `maxConcurrency` instead

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/llms/base.ts:34](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L34)

### maxConcurrency?[​](#maxconcurrency "Direct link to maxConcurrency?")

> **maxConcurrency**: `number`

The maximum number of concurrent calls that can be made. Defaults to `Infinity`, which means no limit.

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[BaseLanguageModelParams](/docs/api/base_language/interfaces/BaseLanguageModelParams).[maxConcurrency](/docs/api/base_language/interfaces/BaseLanguageModelParams#maxconcurrency)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:21](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/util/async_caller.ts#L21)

### maxRetries?[​](#maxretries "Direct link to maxRetries?")

> **maxRetries**: `number`

The maximum number of retries that can be made for a single call, with an exponential backoff between each attempt. Defaults to 6.

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[BaseLanguageModelParams](/docs/api/base_language/interfaces/BaseLanguageModelParams).[maxRetries](/docs/api/base_language/interfaces/BaseLanguageModelParams#maxretries)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:26](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/util/async_caller.ts#L26)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[BaseLanguageModelParams](/docs/api/base_language/interfaces/BaseLanguageModelParams).[metadata](/docs/api/base_language/interfaces/BaseLanguageModelParams#metadata)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:25](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L25)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[BaseLanguageModelParams](/docs/api/base_language/interfaces/BaseLanguageModelParams).[tags](/docs/api/base_language/interfaces/BaseLanguageModelParams#tags)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:24](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L24)

### verbose?[​](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[BaseLanguageModelParams](/docs/api/base_language/interfaces/BaseLanguageModelParams).[verbose](/docs/api/base_language/interfaces/BaseLanguageModelParams#verbose)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L22)