OpenAIInput
===========

Input to OpenAI class.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   `OpenAIBaseInput`.**OpenAIInput**

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### batchSize[​](#batchsize "Direct link to batchSize")

> **batchSize**: `number`

Batch size to use when passing multiple documents to generate

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/types/openai-types.ts:74](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/types/openai-types.ts#L74)

### frequencyPenalty[​](#frequencypenalty "Direct link to frequencyPenalty")

> **frequencyPenalty**: `number`

Penalizes repeated tokens according to frequency

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

OpenAIBaseInput.frequencyPenalty

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/types/openai-types.ts:20](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/types/openai-types.ts#L20)

### modelName[​](#modelname "Direct link to modelName")

> **modelName**: `string`

Model name to use

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

OpenAIBaseInput.modelName

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/types/openai-types.ts:35](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/types/openai-types.ts#L35)

### n[​](#n "Direct link to n")

> **n**: `number`

Number of completions to generate for each prompt

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

OpenAIBaseInput.n

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/types/openai-types.ts:26](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/types/openai-types.ts#L26)

### presencePenalty[​](#presencepenalty "Direct link to presencePenalty")

> **presencePenalty**: `number`

Penalizes repeated tokens

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

OpenAIBaseInput.presencePenalty

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/types/openai-types.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/types/openai-types.ts#L23)

### streaming[​](#streaming "Direct link to streaming")

> **streaming**: `boolean`

Whether to stream the results or not. Enabling disables tokenUsage reporting

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

OpenAIBaseInput.streaming

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/types/openai-types.ts:32](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/types/openai-types.ts#L32)

### temperature[​](#temperature "Direct link to temperature")

> **temperature**: `number`

Sampling temperature to use

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

OpenAIBaseInput.temperature

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/types/openai-types.ts:8](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/types/openai-types.ts#L8)

### topP[​](#topp "Direct link to topP")

> **topP**: `number`

Total probability mass of tokens to consider at each step

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

OpenAIBaseInput.topP

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/types/openai-types.ts:17](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/types/openai-types.ts#L17)

### bestOf?[​](#bestof "Direct link to bestOf?")

> **bestOf**: `number`

Generates `bestOf` completions server side and returns the "best"

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/types/openai-types.ts:71](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/types/openai-types.ts#L71)

### logitBias?[​](#logitbias "Direct link to logitBias?")

> **logitBias**: `Record`<`string`, `number`\>

Dictionary used to adjust the probability of specific tokens being generated

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

OpenAIBaseInput.logitBias

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/types/openai-types.ts:29](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/types/openai-types.ts#L29)

### maxTokens?[​](#maxtokens "Direct link to maxTokens?")

> **maxTokens**: `number`

Maximum number of tokens to generate in the completion. -1 returns as many tokens as possible given the prompt and the model's maximum context size.

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

OpenAIBaseInput.maxTokens

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/types/openai-types.ts:14](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/types/openai-types.ts#L14)

### modelKwargs?[​](#modelkwargs "Direct link to modelKwargs?")

> **modelKwargs**: `Record`<`string`, `any`\>

Holds any additional parameters that are valid to pass to [`openai.createCompletion`](https://platform.openai.com/docs/api-reference/completions/create) that are not explicitly specified on this class.

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

OpenAIBaseInput.modelKwargs

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/types/openai-types.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/types/openai-types.ts#L42)

### openAIApiKey?[​](#openaiapikey "Direct link to openAIApiKey?")

> **openAIApiKey**: `string`

API key to use when making requests to OpenAI. Defaults to the value of `OPENAI_API_KEY` environment variable.

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

OpenAIBaseInput.openAIApiKey

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/types/openai-types.ts:56](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/types/openai-types.ts#L56)

### stop?[​](#stop "Direct link to stop?")

> **stop**: `string`\[\]

List of stop words to use when generating

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

OpenAIBaseInput.stop

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/types/openai-types.ts:45](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/types/openai-types.ts#L45)

### timeout?[​](#timeout "Direct link to timeout?")

> **timeout**: `number`

Timeout to use when making requests to OpenAI.

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

OpenAIBaseInput.timeout

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/types/openai-types.ts:50](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/types/openai-types.ts#L50)