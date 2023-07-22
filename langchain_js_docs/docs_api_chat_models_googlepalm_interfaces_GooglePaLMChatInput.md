GooglePaLMChatInput
===================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseChatModelParams`](/docs/api/chat_models_base/types/BaseChatModelParams).**GooglePaLMChatInput**

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### apiKey?[​](#apikey "Direct link to apiKey?")

> **apiKey**: `string`

Google Palm API key to use

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/chat\_models/googlepalm.ts:60](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/googlepalm.ts#L60)

### callbackManager?[​](#callbackmanager "Direct link to callbackManager?")

> **callbackManager**: [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Deprecated[​](#deprecated "Direct link to Deprecated")

Use `callbacks` instead

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

BaseChatModelParams.callbackManager

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:73](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L73)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

BaseChatModelParams.callbacks

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L23)

### examples?[​](#examples "Direct link to examples?")

> **examples**: `IExample`\[\]

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/chat\_models/googlepalm.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/googlepalm.ts#L55)

### maxConcurrency?[​](#maxconcurrency "Direct link to maxConcurrency?")

> **maxConcurrency**: `number`

The maximum number of concurrent calls that can be made. Defaults to `Infinity`, which means no limit.

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

BaseChatModelParams.maxConcurrency

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:21](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/util/async_caller.ts#L21)

### maxRetries?[​](#maxretries "Direct link to maxRetries?")

> **maxRetries**: `number`

The maximum number of retries that can be made for a single call, with an exponential backoff between each attempt. Defaults to 6.

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

BaseChatModelParams.maxRetries

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:26](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/util/async_caller.ts#L26)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

BaseChatModelParams.metadata

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:25](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L25)

### modelName?[​](#modelname "Direct link to modelName?")

> **modelName**: `string`

Model Name to use

Note: The format must follow the pattern - `models/{model}`

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/chat\_models/googlepalm.ts:15](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/googlepalm.ts#L15)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

BaseChatModelParams.tags

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:24](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L24)

### temperature?[​](#temperature "Direct link to temperature?")

> **temperature**: `number`

Controls the randomness of the output.

Values can range from \[0.0,1.0\], inclusive. A value closer to 1.0 will produce responses that are more varied and creative, while a value closer to 0.0 will typically result in less surprising responses from the model.

Note: The default value varies by model

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/chat\_models/googlepalm.ts:27](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/googlepalm.ts#L27)

### topK?[​](#topk "Direct link to topK?")

> **topK**: `number`

Top-k changes how the model selects tokens for output.

A top-k of 1 means the selected token is the most probable among all tokens in the model’s vocabulary (also called greedy decoding), while a top-k of 3 means that the next token is selected from among the 3 most probable tokens (using temperature).

Note: The default value varies by model

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/chat\_models/googlepalm.ts:53](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/googlepalm.ts#L53)

### topP?[​](#topp "Direct link to topP?")

> **topP**: `number`

Top-p changes how the model selects tokens for output.

Tokens are selected from most probable to least until the sum of their probabilities equals the top-p value.

For example, if tokens A, B, and C have a probability of .3, .2, and .1 and the top-p value is .5, then the model will select either A or B as the next token (using temperature).

Note: The default value varies by model

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/chat\_models/googlepalm.ts:41](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/googlepalm.ts#L41)

### verbose?[​](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

BaseChatModelParams.verbose

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L22)