ChatAnthropic
=============

Wrapper around Anthropic large language models.

To use you should have the `@anthropic-ai/sdk` package installed, with the `ANTHROPIC_API_KEY` environment variable set.

Remarks[​](#remarks "Direct link to Remarks")
---------------------------------------------

Any parameters that are valid to be passed to [`anthropic.complete`](https://console.anthropic.com/docs/api/reference) can be passed through [invocationKwargs](/docs/api/chat_models_anthropic/classes/ChatAnthropic#invocationkwargs), even if not explicitly available on this class.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseChatModel`](/docs/api/chat_models_base/classes/BaseChatModel).**ChatAnthropic**

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   [`AnthropicInput`](/docs/api/chat_models_anthropic/interfaces/AnthropicInput)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new ChatAnthropic**(`fields`?: `Partial`<[`AnthropicInput`](/docs/api/chat_models_anthropic/interfaces/AnthropicInput)\> & [`BaseLanguageModelParams`](/docs/api/base_language/interfaces/BaseLanguageModelParams)): [`ChatAnthropic`](/docs/api/chat_models_anthropic/classes/ChatAnthropic)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields?`

`Partial`<[`AnthropicInput`](/docs/api/chat_models_anthropic/interfaces/AnthropicInput)\> & [`BaseLanguageModelParams`](/docs/api/base_language/interfaces/BaseLanguageModelParams)

#### Returns[​](#returns "Direct link to Returns")

[`ChatAnthropic`](/docs/api/chat_models_anthropic/classes/ChatAnthropic)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[constructor](/docs/api/chat_models_base/classes/BaseChatModel#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/chat\_models/anthropic.ts:145](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/anthropic.ts#L145)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### CallOptions[​](#calloptions "Direct link to CallOptions")

> **CallOptions**: [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[CallOptions](/docs/api/chat_models_base/classes/BaseChatModel#calloptions)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/chat\_models/anthropic.ts:103](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/anthropic.ts#L103)

### ParsedCallOptions[​](#parsedcalloptions "Direct link to ParsedCallOptions")

> **ParsedCallOptions**: `Omit`<[`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[ParsedCallOptions](/docs/api/chat_models_base/classes/BaseChatModel#parsedcalloptions)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:43](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/base.ts#L43)

### caller[​](#caller "Direct link to caller")

> **caller**: `AsyncCaller`

The async caller should be used by subclasses to make any async calls, which will thus benefit from the concurrency and retry logic.

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[caller](/docs/api/chat_models_base/classes/BaseChatModel#caller)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:116](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L116)

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[lc\_kwargs](/docs/api/chat_models_base/classes/BaseChatModel#lc_kwargs)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[lc\_namespace](/docs/api/chat_models_base/classes/BaseChatModel#lc_namespace)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:48](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/base.ts#L48)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `true`

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[lc\_serializable](/docs/api/chat_models_base/classes/BaseChatModel#lc_serializable)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/chat\_models/anthropic.ts:117](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/anthropic.ts#L117)

### maxTokensToSample[​](#maxtokenstosample "Direct link to maxTokensToSample")

> **maxTokensToSample**: `number` = `2048`

A maximum number of tokens to generate before stopping.

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

[AnthropicInput](/docs/api/chat_models_anthropic/interfaces/AnthropicInput).[maxTokensToSample](/docs/api/chat_models_anthropic/interfaces/AnthropicInput#maxtokenstosample)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/chat\_models/anthropic.ts:129](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/anthropic.ts#L129)

### modelName[​](#modelname "Direct link to modelName")

> **modelName**: `string` = `"claude-v1"`

Model name to use

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

[AnthropicInput](/docs/api/chat_models_anthropic/interfaces/AnthropicInput).[modelName](/docs/api/chat_models_anthropic/interfaces/AnthropicInput#modelname)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/chat\_models/anthropic.ts:131](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/anthropic.ts#L131)

### streaming[​](#streaming "Direct link to streaming")

> **streaming**: `boolean` = `false`

Whether to stream the results or not

#### Implementation of[​](#implementation-of-2 "Direct link to Implementation of")

[AnthropicInput](/docs/api/chat_models_anthropic/interfaces/AnthropicInput).[streaming](/docs/api/chat_models_anthropic/interfaces/AnthropicInput#streaming)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/chat\_models/anthropic.ts:137](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/anthropic.ts#L137)

### temperature[​](#temperature "Direct link to temperature")

> **temperature**: `number` = `1`

Amount of randomness injected into the response. Ranges from 0 to 1. Use temp closer to 0 for analytical / multiple choice, and temp closer to 1 for creative and generative tasks.

#### Implementation of[​](#implementation-of-3 "Direct link to Implementation of")

[AnthropicInput](/docs/api/chat_models_anthropic/interfaces/AnthropicInput).[temperature](/docs/api/chat_models_anthropic/interfaces/AnthropicInput#temperature)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/chat\_models/anthropic.ts:123](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/anthropic.ts#L123)

### topK[​](#topk "Direct link to topK")

> **topK**: `number` = `-1`

Only sample from the top K options for each subsequent token. Used to remove "long tail" low probability responses. Defaults to -1, which disables it.

#### Implementation of[​](#implementation-of-4 "Direct link to Implementation of")

[AnthropicInput](/docs/api/chat_models_anthropic/interfaces/AnthropicInput).[topK](/docs/api/chat_models_anthropic/interfaces/AnthropicInput#topk)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/chat\_models/anthropic.ts:125](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/anthropic.ts#L125)

### topP[​](#topp "Direct link to topP")

> **topP**: `number` = `-1`

Does nucleus sampling, in which we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by top\_p. Defaults to -1, which disables it. Note that you should either alter temperature or top\_p, but not both.

#### Implementation of[​](#implementation-of-5 "Direct link to Implementation of")

[AnthropicInput](/docs/api/chat_models_anthropic/interfaces/AnthropicInput).[topP](/docs/api/chat_models_anthropic/interfaces/AnthropicInput#topp)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/chat\_models/anthropic.ts:127](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/anthropic.ts#L127)

### verbose[​](#verbose "Direct link to verbose")

> **verbose**: `boolean`

Whether to print out response text.

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[verbose](/docs/api/chat_models_base/classes/BaseChatModel#verbose)

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:38](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L38)

### anthropicApiKey?[​](#anthropicapikey "Direct link to anthropicApiKey?")

> **anthropicApiKey**: `string`

Anthropic API key

#### Implementation of[​](#implementation-of-6 "Direct link to Implementation of")

[AnthropicInput](/docs/api/chat_models_anthropic/interfaces/AnthropicInput).[anthropicApiKey](/docs/api/chat_models_anthropic/interfaces/AnthropicInput#anthropicapikey)

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/chat\_models/anthropic.ts:119](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/anthropic.ts#L119)

### apiUrl?[​](#apiurl "Direct link to apiUrl?")

> **apiUrl**: `string`

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/chat\_models/anthropic.ts:121](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/anthropic.ts#L121)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[callbacks](/docs/api/chat_models_base/classes/BaseChatModel#callbacks)

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L40)

### invocationKwargs?[​](#invocationkwargs "Direct link to invocationKwargs?")

> **invocationKwargs**: `Kwargs`

Holds any additional parameters that are valid to pass to [`anthropic.complete`](https://console.anthropic.com/docs/api/reference) that are not explicitly specified on this class.

#### Implementation of[​](#implementation-of-7 "Direct link to Implementation of")

[AnthropicInput](/docs/api/chat_models_anthropic/interfaces/AnthropicInput).[invocationKwargs](/docs/api/chat_models_anthropic/interfaces/AnthropicInput#invocationkwargs)

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/chat\_models/anthropic.ts:133](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/anthropic.ts#L133)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[metadata](/docs/api/chat_models_base/classes/BaseChatModel#metadata)

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:44](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L44)

### stopSequences?[​](#stopsequences "Direct link to stopSequences?")

> **stopSequences**: `string`\[\]

A list of strings upon which to stop generating. You probably want `["\n\nHuman:"]`, as that's the cue for the next turn in the dialog agent.

#### Implementation of[​](#implementation-of-8 "Direct link to Implementation of")

[AnthropicInput](/docs/api/chat_models_anthropic/interfaces/AnthropicInput).[stopSequences](/docs/api/chat_models_anthropic/interfaces/AnthropicInput#stopsequences)

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/chat\_models/anthropic.ts:135](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/anthropic.ts#L135)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[tags](/docs/api/chat_models_base/classes/BaseChatModel#tags)

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L42)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### callKeys[​](#callkeys "Direct link to callKeys")

Keys that the language model accepts as call options.

> **callKeys**(): `string`\[\]

#### Returns[​](#returns-1 "Direct link to Returns")

`string`\[\]

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

BaseChatModel.callKeys

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:108](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L108)

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[callKeys](/docs/api/chat_models_base/classes/BaseChatModel#callkeys)

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:108](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L108)

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `Record`<`string`, `string`\>

#### Returns[​](#returns-2 "Direct link to Returns")

`Record`<`string`, `string`\>

#### Overrides[​](#overrides-3 "Direct link to Overrides")

BaseChatModel.lc\_aliases

#### Defined in[​](#defined-in-23 "Direct link to Defined in")

[langchain/src/chat\_models/anthropic.ts:111](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/anthropic.ts#L111)

#### Overrides[​](#overrides-4 "Direct link to Overrides")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[lc\_aliases](/docs/api/chat_models_base/classes/BaseChatModel#lc_aliases)

#### Defined in[​](#defined-in-24 "Direct link to Defined in")

[langchain/src/chat\_models/anthropic.ts:111](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/anthropic.ts#L111)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

BaseChatModel.lc\_attributes

#### Defined in[​](#defined-in-25 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[lc\_attributes](/docs/api/chat_models_base/classes/BaseChatModel#lc_attributes)

#### Defined in[​](#defined-in-26 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-4 "Direct link to Returns")

`undefined` | {}

#### Overrides[​](#overrides-5 "Direct link to Overrides")

BaseChatModel.lc\_secrets

#### Defined in[​](#defined-in-27 "Direct link to Defined in")

[langchain/src/chat\_models/anthropic.ts:105](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/anthropic.ts#L105)

#### Overrides[​](#overrides-6 "Direct link to Overrides")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[lc\_secrets](/docs/api/chat_models_base/classes/BaseChatModel#lc_secrets)

#### Defined in[​](#defined-in-28 "Direct link to Defined in")

[langchain/src/chat\_models/anthropic.ts:105](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/anthropic.ts#L105)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### \_llmType()[​](#_llmtype "Direct link to _llmtype")

> **\_llmType**(): `string`

#### Returns[​](#returns-5 "Direct link to Returns")

`string`

#### Overrides[​](#overrides-7 "Direct link to Overrides")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[\_llmType](/docs/api/chat_models_base/classes/BaseChatModel#_llmtype)

#### Defined in[​](#defined-in-29 "Direct link to Defined in")

[langchain/src/chat\_models/anthropic.ts:327](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/anthropic.ts#L327)

### \_modelType()[​](#_modeltype "Direct link to _modeltype")

> **\_modelType**(): `string`

#### Returns[​](#returns-6 "Direct link to Returns")

`string`

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[\_modelType](/docs/api/chat_models_base/classes/BaseChatModel#_modeltype)

#### Defined in[​](#defined-in-30 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:158](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/base.ts#L158)

### call()[​](#call "Direct link to call()")

> **call**(`messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\], `options`?: `string`\[\] | [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]

`options?`

`string`\[\] | [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-7 "Direct link to Returns")

`Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[call](/docs/api/chat_models_base/classes/BaseChatModel#call)

#### Defined in[​](#defined-in-31 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:181](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/base.ts#L181)

### callPrompt()[​](#callprompt "Direct link to callPrompt()")

> **callPrompt**(`promptValue`: [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue), `options`?: `string`\[\] | [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`promptValue`

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)

`options?`

`string`\[\] | [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-8 "Direct link to Returns")

`Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[callPrompt](/docs/api/chat_models_base/classes/BaseChatModel#callprompt)

#### Defined in[​](#defined-in-32 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:191](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/base.ts#L191)

### generate()[​](#generate "Direct link to generate()")

> **generate**(`messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]\[\], `options`?: `string`\[\] | [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]\[\]

`options?`

`string`\[\] | [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-9 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[​](#inherited-from-15 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[generate](/docs/api/chat_models_base/classes/BaseChatModel#generate)

#### Defined in[​](#defined-in-33 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:58](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/base.ts#L58)

### generatePrompt()[​](#generateprompt "Direct link to generatePrompt()")

> **generatePrompt**(`promptValues`: [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\[\], `options`?: `string`\[\] | [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`promptValues`

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\[\]

`options?`

`string`\[\] | [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-10 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[​](#inherited-from-16 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[generatePrompt](/docs/api/chat_models_base/classes/BaseChatModel#generateprompt)

#### Defined in[​](#defined-in-34 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:164](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/base.ts#L164)

### getNumTokens()[​](#getnumtokens "Direct link to getNumTokens()")

> **getNumTokens**(`text`: `string`): `Promise`<`number`\>

#### Parameters[​](#parameters-5 "Direct link to Parameters")

Parameter

Type

`text`

`string`

#### Returns[​](#returns-11 "Direct link to Returns")

`Promise`<`number`\>

#### Inherited from[​](#inherited-from-17 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[getNumTokens](/docs/api/chat_models_base/classes/BaseChatModel#getnumtokens)

#### Defined in[​](#defined-in-35 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:154](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L154)

### identifyingParams()[​](#identifyingparams "Direct link to identifyingParams()")

Get the identifying parameters for the model

> **identifyingParams**(): `object`

#### Returns[​](#returns-12 "Direct link to Returns")

`object`

Member

Type

`model_name`

`string`

#### Defined in[​](#defined-in-36 "Direct link to Defined in")

[langchain/src/chat\_models/anthropic.ts:202](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/anthropic.ts#L202)

### invocationParams()[​](#invocationparams "Direct link to invocationParams()")

Get the parameters used to invoke the model

> **invocationParams**(`options`?: `Omit`<[`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>): `Omit`<`CompletionCreateParams`, "prompt"\> & `Kwargs`

#### Parameters[​](#parameters-6 "Direct link to Parameters")

Parameter

Type

`options?`

`Omit`<[`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>

#### Returns[​](#returns-13 "Direct link to Returns")

`Omit`<`CompletionCreateParams`, "prompt"\> & `Kwargs`

#### Overrides[​](#overrides-8 "Direct link to Overrides")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[invocationParams](/docs/api/chat_models_base/classes/BaseChatModel#invocationparams)

#### Defined in[​](#defined-in-37 "Direct link to Defined in")

[langchain/src/chat\_models/anthropic.ts:173](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/anthropic.ts#L173)

### predict()[​](#predict "Direct link to predict()")

> **predict**(`text`: `string`, `options`?: `string`\[\] | [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\>

#### Parameters[​](#parameters-7 "Direct link to Parameters")

Parameter

Type

`text`

`string`

`options?`

`string`\[\] | [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-14 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[​](#inherited-from-18 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[predict](/docs/api/chat_models_base/classes/BaseChatModel#predict)

#### Defined in[​](#defined-in-38 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:208](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/base.ts#L208)

### predictMessages()[​](#predictmessages "Direct link to predictMessages()")

> **predictMessages**(`messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\], `options`?: `string`\[\] | [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Parameters[​](#parameters-8 "Direct link to Parameters")

Parameter

Type

`messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]

`options?`

`string`\[\] | [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-15 "Direct link to Returns")

`Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Inherited from[​](#inherited-from-19 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[predictMessages](/docs/api/chat_models_base/classes/BaseChatModel#predictmessages)

#### Defined in[​](#defined-in-39 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:200](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chat_models/base.ts#L200)

### serialize()[​](#serialize "Direct link to serialize()")

#### Deprecated[​](#deprecated "Direct link to Deprecated")

Return a json-like object representing this LLM.

> **serialize**(): [`SerializedLLM`](/docs/api/base_language/types/SerializedLLM)

#### Returns[​](#returns-16 "Direct link to Returns")

[`SerializedLLM`](/docs/api/base_language/types/SerializedLLM)

#### Inherited from[​](#inherited-from-20 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[serialize](/docs/api/chat_models_base/classes/BaseChatModel#serialize)

#### Defined in[​](#defined-in-40 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:192](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L192)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-17 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-21 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[toJSON](/docs/api/chat_models_base/classes/BaseChatModel#tojson)

#### Defined in[​](#defined-in-41 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-18 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-22 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[toJSONNotImplemented](/docs/api/chat_models_base/classes/BaseChatModel#tojsonnotimplemented)

#### Defined in[​](#defined-in-42 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)

### deserialize()[​](#deserialize "Direct link to deserialize()")

#### Deprecated[​](#deprecated-1 "Direct link to Deprecated")

Load an LLM from a json-like object describing it.

> `Static` **deserialize**(`data`: [`SerializedLLM`](/docs/api/base_language/types/SerializedLLM)): `Promise`<[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>

#### Parameters[​](#parameters-9 "Direct link to Parameters")

Parameter

Type

`data`

[`SerializedLLM`](/docs/api/base_language/types/SerializedLLM)

#### Returns[​](#returns-19 "Direct link to Returns")

`Promise`<[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>

#### Inherited from[​](#inherited-from-23 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[deserialize](/docs/api/chat_models_base/classes/BaseChatModel#deserialize)

#### Defined in[​](#defined-in-43 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:204](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L204)