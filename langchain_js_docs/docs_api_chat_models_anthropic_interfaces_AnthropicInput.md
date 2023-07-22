AnthropicInput
==============

Input to AnthropicChat class.

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### maxTokensToSample[​](#maxtokenstosample "Direct link to maxTokensToSample")

> **maxTokensToSample**: `number`

A maximum number of tokens to generate before stopping.

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/chat\_models/anthropic.ts:59](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/anthropic.ts#L59)

### modelName[​](#modelname "Direct link to modelName")

> **modelName**: `string`

Model name to use

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/chat\_models/anthropic.ts:77](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/anthropic.ts#L77)

### anthropicApiKey?[​](#anthropicapikey "Direct link to anthropicApiKey?")

> **anthropicApiKey**: `string`

Anthropic API key

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/chat\_models/anthropic.ts:71](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/anthropic.ts#L71)

### anthropicApiUrl?[​](#anthropicapiurl "Direct link to anthropicApiUrl?")

> **anthropicApiUrl**: `string`

Anthropic API URL

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/chat\_models/anthropic.ts:74](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/anthropic.ts#L74)

### invocationKwargs?[​](#invocationkwargs "Direct link to invocationKwargs?")

> **invocationKwargs**: `Kwargs`

Holds any additional parameters that are valid to pass to [`anthropic.complete`](https://console.anthropic.com/docs/api/reference) that are not explicitly specified on this class.

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/chat\_models/anthropic.ts:83](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/anthropic.ts#L83)

### stopSequences?[​](#stopsequences "Direct link to stopSequences?")

> **stopSequences**: `string`\[\]

A list of strings upon which to stop generating. You probably want `["\n\nHuman:"]`, as that's the cue for the next turn in the dialog agent.

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/chat\_models/anthropic.ts:65](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/anthropic.ts#L65)

### streaming?[​](#streaming "Direct link to streaming?")

> **streaming**: `boolean`

Whether to stream the results or not

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/chat\_models/anthropic.ts:68](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/anthropic.ts#L68)

### temperature?[​](#temperature "Direct link to temperature?")

> **temperature**: `number`

Amount of randomness injected into the response. Ranges from 0 to 1. Use temp closer to 0 for analytical / multiple choice, and temp closer to 1 for creative and generative tasks.

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/chat\_models/anthropic.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/anthropic.ts#L40)

### topK?[​](#topk "Direct link to topK?")

> **topK**: `number`

Only sample from the top K options for each subsequent token. Used to remove "long tail" low probability responses. Defaults to -1, which disables it.

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/chat\_models/anthropic.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/anthropic.ts#L46)

### topP?[​](#topp "Direct link to topP?")

> **topP**: `number`

Does nucleus sampling, in which we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by top\_p. Defaults to -1, which disables it. Note that you should either alter temperature or top\_p, but not both.

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/chat\_models/anthropic.ts:56](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/anthropic.ts#L56)