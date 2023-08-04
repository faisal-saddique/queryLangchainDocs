PromptLayerOpenAIChat
=====================

PromptLayer wrapper to OpenAIChat

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`OpenAIChat`](/docs/api/llms_openai/classes/OpenAIChat).**PromptLayerOpenAIChat**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new PromptLayerOpenAIChat**(`fields`?: `Partial`<[`OpenAIChatInput`](/docs/api/chat_models_openai/interfaces/OpenAIChatInput)\> & `Partial`<[`AzureOpenAIInput`](/docs/api/llms_openai/interfaces/AzureOpenAIInput)\> & [`BaseLLMParams`](/docs/api/llms_base/interfaces/BaseLLMParams) & {`configuration`?: `ConfigurationParameters`;} & {`plTags`?: `string`\[\]; `promptLayerApiKey`?: `string`; `returnPromptLayerId`?: `boolean`;}): [`PromptLayerOpenAIChat`](/docs/api/llms_openai/classes/PromptLayerOpenAIChat)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`fields?`

`Partial`<[`OpenAIChatInput`](/docs/api/chat_models_openai/interfaces/OpenAIChatInput)\> & `Partial`<[`AzureOpenAIInput`](/docs/api/llms_openai/interfaces/AzureOpenAIInput)\> & [`BaseLLMParams`](/docs/api/llms_base/interfaces/BaseLLMParams) & {`configuration`?: `ConfigurationParameters`;} & {`plTags`?: `string`\[\];  
`promptLayerApiKey`?: `string`;  
`returnPromptLayerId`?: `boolean`;}

#### Returns[](#returns "Direct link to Returns")

[`PromptLayerOpenAIChat`](/docs/api/llms_openai/classes/PromptLayerOpenAIChat)

#### Overrides[](#overrides "Direct link to Overrides")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[constructor](/docs/api/llms_openai/classes/OpenAIChat#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:556](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L556)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### CallOptions[](#calloptions "Direct link to CallOptions")

> **CallOptions**: `OpenAIChatCallOptions`

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[CallOptions](/docs/api/llms_openai/classes/OpenAIChat#calloptions)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:110](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L110) [langchain/src/base\_language/index.ts:115](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L115)

### ParsedCallOptions[](#parsedcalloptions "Direct link to ParsedCallOptions")

> **ParsedCallOptions**: `Omit`<`OpenAIChatCallOptions`, `never`\>

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[ParsedCallOptions](/docs/api/llms_openai/classes/OpenAIChat#parsedcalloptions)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/llms/base.ts:49](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L49)

### caller[](#caller "Direct link to caller")

> **caller**: `AsyncCaller`

The async caller should be used by subclasses to make any async calls, which will thus benefit from the concurrency and retry logic.

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[caller](/docs/api/llms_openai/classes/OpenAIChat#caller)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:128](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L128)

### frequencyPenalty[](#frequencypenalty "Direct link to frequencyPenalty")

> **frequencyPenalty**: `number` = `0`

Penalizes repeated tokens according to frequency

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[frequencyPenalty](/docs/api/llms_openai/classes/OpenAIChat#frequencypenalty)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:89](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L89)

### lc\_kwargs[](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[lc\_kwargs](/docs/api/llms_openai/classes/OpenAIChat#lc_kwargs)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L57)

### lc\_namespace[](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[lc\_namespace](/docs/api/llms_openai/classes/OpenAIChat#lc_namespace)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/llms/base.ts:54](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L54)

### lc\_serializable[](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Overrides[](#overrides-1 "Direct link to Overrides")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[lc\_serializable](/docs/api/llms_openai/classes/OpenAIChat#lc_serializable)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:548](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L548)

### modelName[](#modelname "Direct link to modelName")

> **modelName**: `string` = `"gpt-3.5-turbo"`

Model name to use

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[modelName](/docs/api/llms_openai/classes/OpenAIChat#modelname)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:99](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L99)

### n[](#n "Direct link to n")

> **n**: `number` = `1`

Number of completions to generate for each prompt

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[n](/docs/api/llms_openai/classes/OpenAIChat#n)

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:93](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L93)

### presencePenalty[](#presencepenalty "Direct link to presencePenalty")

> **presencePenalty**: `number` = `0`

Penalizes repeated tokens

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[presencePenalty](/docs/api/llms_openai/classes/OpenAIChat#presencepenalty)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:91](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L91)

### streaming[](#streaming "Direct link to streaming")

> **streaming**: `boolean` = `false`

Whether to stream the results or not. Enabling disables tokenUsage reporting

#### Inherited from[](#inherited-from-9 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[streaming](/docs/api/llms_openai/classes/OpenAIChat#streaming)

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:109](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L109)

### temperature[](#temperature "Direct link to temperature")

> **temperature**: `number` = `1`

Sampling temperature to use

#### Inherited from[](#inherited-from-10 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[temperature](/docs/api/llms_openai/classes/OpenAIChat#temperature)

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:85](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L85)

### topP[](#topp "Direct link to topP")

> **topP**: `number` = `1`

Total probability mass of tokens to consider at each step

#### Inherited from[](#inherited-from-11 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[topP](/docs/api/llms_openai/classes/OpenAIChat#topp)

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:87](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L87)

### verbose[](#verbose "Direct link to verbose")

> **verbose**: `boolean`

Whether to print out response text.

#### Inherited from[](#inherited-from-12 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[verbose](/docs/api/llms_openai/classes/OpenAIChat#verbose)

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:44](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L44)

### azureOpenAIApiDeploymentName?[](#azureopenaiapideploymentname "Direct link to azureOpenAIApiDeploymentName?")

> **azureOpenAIApiDeploymentName**: `string`

Azure OpenAI API deployment name to use for completions when making requests to Azure OpenAI. This is the name of the deployment you created in the Azure portal. e.g. "my-openai-deployment" this will be used in the endpoint URL: https://{InstanceName}.openai.azure.com/openai/deployments/my-openai-deployment/

#### Inherited from[](#inherited-from-13 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[azureOpenAIApiDeploymentName](/docs/api/llms_openai/classes/OpenAIChat#azureopenaiapideploymentname)

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:119](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L119)

### azureOpenAIApiInstanceName?[](#azureopenaiapiinstancename "Direct link to azureOpenAIApiInstanceName?")

> **azureOpenAIApiInstanceName**: `string`

Azure OpenAI API instance name to use when making requests to Azure OpenAI. this is the name of the instance you created in the Azure portal. e.g. "my-openai-instance" this will be used in the endpoint URL: [https://my-openai-instance.openai.azure.com/openai/deployments/{DeploymentName}/](https://my-openai-instance.openai.azure.com/openai/deployments/%7BDeploymentName%7D/)

#### Inherited from[](#inherited-from-14 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[azureOpenAIApiInstanceName](/docs/api/llms_openai/classes/OpenAIChat#azureopenaiapiinstancename)

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:117](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L117)

### azureOpenAIApiKey?[](#azureopenaiapikey "Direct link to azureOpenAIApiKey?")

> **azureOpenAIApiKey**: `string`

API key to use when making requests to Azure OpenAI.

#### Inherited from[](#inherited-from-15 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[azureOpenAIApiKey](/docs/api/llms_openai/classes/OpenAIChat#azureopenaiapikey)

#### Defined in[](#defined-in-17 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:115](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L115)

### azureOpenAIApiVersion?[](#azureopenaiapiversion "Direct link to azureOpenAIApiVersion?")

> **azureOpenAIApiVersion**: `string`

API version to use when making requests to Azure OpenAI.

#### Inherited from[](#inherited-from-16 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[azureOpenAIApiVersion](/docs/api/llms_openai/classes/OpenAIChat#azureopenaiapiversion)

#### Defined in[](#defined-in-18 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:113](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L113)

### azureOpenAIBasePath?[](#azureopenaibasepath "Direct link to azureOpenAIBasePath?")

> **azureOpenAIBasePath**: `string`

Custom endpoint for Azure OpenAI API. This is useful in case you have a deployment in another region. e.g. setting this value to "[https://westeurope.api.cognitive.microsoft.com/openai/deployments"](https://westeurope.api.cognitive.microsoft.com/openai/deployments%22) will be result in the endpoint URL: [https://westeurope.api.cognitive.microsoft.com/openai/deployments/{DeploymentName}/](https://westeurope.api.cognitive.microsoft.com/openai/deployments/%7BDeploymentName%7D/)

#### Inherited from[](#inherited-from-17 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[azureOpenAIBasePath](/docs/api/llms_openai/classes/OpenAIChat#azureopenaibasepath)

#### Defined in[](#defined-in-19 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:121](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L121)

### cache?[](#cache "Direct link to cache?")

> **cache**: [`BaseCache`](/docs/api/schema/classes/BaseCache)<[`Generation`](/docs/api/schema/interfaces/Generation)\[\]\>

#### Inherited from[](#inherited-from-18 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[cache](/docs/api/llms_openai/classes/OpenAIChat#cache)

#### Defined in[](#defined-in-20 "Direct link to Defined in")

[langchain/src/llms/base.ts:56](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L56)

### callbacks?[](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[](#inherited-from-19 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[callbacks](/docs/api/llms_openai/classes/OpenAIChat#callbacks)

#### Defined in[](#defined-in-21 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L46)

### logitBias?[](#logitbias "Direct link to logitBias?")

> **logitBias**: `Record`<`string`, `number`\>

Dictionary used to adjust the probability of specific tokens being generated

#### Inherited from[](#inherited-from-20 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[logitBias](/docs/api/llms_openai/classes/OpenAIChat#logitbias)

#### Defined in[](#defined-in-22 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:95](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L95)

### maxTokens?[](#maxtokens "Direct link to maxTokens?")

> **maxTokens**: `number`

Maximum number of tokens to generate in the completion. -1 returns as many tokens as possible given the prompt and the model's maximum context size.

#### Inherited from[](#inherited-from-21 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[maxTokens](/docs/api/llms_openai/classes/OpenAIChat#maxtokens)

#### Defined in[](#defined-in-23 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:97](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L97)

### metadata?[](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[](#inherited-from-22 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[metadata](/docs/api/llms_openai/classes/OpenAIChat#metadata)

#### Defined in[](#defined-in-24 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:50](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L50)

### modelKwargs?[](#modelkwargs "Direct link to modelKwargs?")

> **modelKwargs**: `Record`<`string`, `any`\>

Holds any additional parameters that are valid to pass to [`openai.createCompletion`](https://platform.openai.com/docs/api-reference/completions/create) that are not explicitly specified on this class.

#### Inherited from[](#inherited-from-23 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[modelKwargs](/docs/api/llms_openai/classes/OpenAIChat#modelkwargs)

#### Defined in[](#defined-in-25 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:103](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L103)

### openAIApiKey?[](#openaiapikey "Direct link to openAIApiKey?")

> **openAIApiKey**: `string`

API key to use when making requests to OpenAI. Defaults to the value of `OPENAI_API_KEY` environment variable.

#### Inherited from[](#inherited-from-24 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[openAIApiKey](/docs/api/llms_openai/classes/OpenAIChat#openaiapikey)

#### Defined in[](#defined-in-26 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:111](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L111)

### plTags?[](#pltags "Direct link to plTags?")

> **plTags**: `string`\[\]

#### Defined in[](#defined-in-27 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:552](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L552)

### prefixMessages?[](#prefixmessages "Direct link to prefixMessages?")

> **prefixMessages**: `ChatCompletionRequestMessage`\[\]

ChatGPT messages to pass as a prefix to the prompt

#### Inherited from[](#inherited-from-25 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[prefixMessages](/docs/api/llms_openai/classes/OpenAIChat#prefixmessages)

#### Defined in[](#defined-in-28 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:101](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L101)

### promptLayerApiKey?[](#promptlayerapikey "Direct link to promptLayerApiKey?")

> **promptLayerApiKey**: `string`

#### Defined in[](#defined-in-29 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:550](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L550)

### returnPromptLayerId?[](#returnpromptlayerid "Direct link to returnPromptLayerId?")

> **returnPromptLayerId**: `boolean`

#### Defined in[](#defined-in-30 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:554](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L554)

### stop?[](#stop "Direct link to stop?")

> **stop**: `string`\[\]

List of stop words to use when generating

#### Inherited from[](#inherited-from-26 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[stop](/docs/api/llms_openai/classes/OpenAIChat#stop)

#### Defined in[](#defined-in-31 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:107](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L107)

### tags?[](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[](#inherited-from-27 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[tags](/docs/api/llms_openai/classes/OpenAIChat#tags)

#### Defined in[](#defined-in-32 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L48)

### timeout?[](#timeout "Direct link to timeout?")

> **timeout**: `number`

Timeout to use when making requests to OpenAI.

#### Inherited from[](#inherited-from-28 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[timeout](/docs/api/llms_openai/classes/OpenAIChat#timeout)

#### Defined in[](#defined-in-33 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:105](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L105)

### lc\_runnable[](#lc_runnable "Direct link to lc_runnable")

> `Protected` **lc\_runnable**: `boolean` = `true`

#### Inherited from[](#inherited-from-29 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[lc\_runnable](/docs/api/llms_openai/classes/OpenAIChat#lc_runnable)

#### Defined in[](#defined-in-34 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:34](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L34)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### callKeys[](#callkeys "Direct link to callKeys")

Keys that the language model accepts as call options.

> **callKeys**(): _keyof_ `OpenAIChatCallOptions`\[\]

#### Returns[](#returns-1 "Direct link to Returns")

_keyof_ `OpenAIChatCallOptions`\[\]

#### Inherited from[](#inherited-from-30 "Direct link to Inherited from")

OpenAIChat.callKeys

#### Defined in[](#defined-in-35 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L57)

#### Inherited from[](#inherited-from-31 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[callKeys](/docs/api/llms_openai/classes/OpenAIChat#callkeys)

#### Defined in[](#defined-in-36 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L57)

### lc\_aliases[](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `Record`<`string`, `string`\>

#### Returns[](#returns-2 "Direct link to Returns")

`Record`<`string`, `string`\>

#### Inherited from[](#inherited-from-32 "Direct link to Inherited from")

OpenAIChat.lc\_aliases

#### Defined in[](#defined-in-37 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:74](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L74)

#### Inherited from[](#inherited-from-33 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[lc\_aliases](/docs/api/llms_openai/classes/OpenAIChat#lc_aliases)

#### Defined in[](#defined-in-38 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:74](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L74)

### lc\_attributes[](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-34 "Direct link to Inherited from")

OpenAIChat.lc\_attributes

#### Defined in[](#defined-in-39 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:52](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L52)

#### Inherited from[](#inherited-from-35 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[lc\_attributes](/docs/api/llms_openai/classes/OpenAIChat#lc_attributes)

#### Defined in[](#defined-in-40 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:52](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L52)

### lc\_secrets[](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[](#returns-4 "Direct link to Returns")

`undefined` | {}

#### Overrides[](#overrides-2 "Direct link to Overrides")

OpenAIChat.lc\_secrets

#### Defined in[](#defined-in-41 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:542](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L542)

#### Overrides[](#overrides-3 "Direct link to Overrides")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[lc\_secrets](/docs/api/llms_openai/classes/OpenAIChat#lc_secrets)

#### Defined in[](#defined-in-42 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:542](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L542)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### \_flattenLLMResult()[](#_flattenllmresult "Direct link to _flattenllmresult")

> **\_flattenLLMResult**(`llmResult`: [`LLMResult`](/docs/api/schema/types/LLMResult)): [`LLMResult`](/docs/api/schema/types/LLMResult)\[\]

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`llmResult`

[`LLMResult`](/docs/api/schema/types/LLMResult)

#### Returns[](#returns-5 "Direct link to Returns")

[`LLMResult`](/docs/api/schema/types/LLMResult)\[\]

#### Inherited from[](#inherited-from-36 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[\_flattenLLMResult](/docs/api/llms_openai/classes/OpenAIChat#_flattenllmresult)

#### Defined in[](#defined-in-43 "Direct link to Defined in")

[langchain/src/llms/base.ts:197](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L197)

### \_generate()[](#_generate "Direct link to _generate")

Run the LLM on the given prompts and input.

> **\_generate**(`prompts`: `string`\[\], `options`: `Omit`<`OpenAIChatCallOptions`, `never`\>, `runManager`?: [`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`prompts`

`string`\[\]

`options`

`Omit`<`OpenAIChatCallOptions`, `never`\>

`runManager?`

[`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)

#### Returns[](#returns-6 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Overrides[](#overrides-4 "Direct link to Overrides")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[\_generate](/docs/api/llms_openai/classes/OpenAIChat#_generate)

#### Defined in[](#defined-in-44 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:589](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L589)

### \_llmType()[](#_llmtype "Direct link to _llmtype")

Return the string type key uniquely identifying this class of LLM.

> **\_llmType**(): `string`

#### Returns[](#returns-7 "Direct link to Returns")

`string`

#### Inherited from[](#inherited-from-37 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[\_llmType](/docs/api/llms_openai/classes/OpenAIChat#_llmtype)

#### Defined in[](#defined-in-45 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:533](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L533)

### \_modelType()[](#_modeltype "Direct link to _modeltype")

> **\_modelType**(): `string`

#### Returns[](#returns-8 "Direct link to Returns")

`string`

#### Inherited from[](#inherited-from-38 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[\_modelType](/docs/api/llms_openai/classes/OpenAIChat#_modeltype)

#### Defined in[](#defined-in-46 "Direct link to Defined in")

[langchain/src/llms/base.ts:394](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L394)

### \_patchConfig()[](#_patchconfig "Direct link to _patchconfig")

> **\_patchConfig**(`config`: `Partial`<`OpenAIChatCallOptions`\> = `{}`, `callbackManager`: `undefined` | [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager) = `undefined`): `Partial`<`OpenAIChatCallOptions`\>

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

Default value

`config`

`Partial`<`OpenAIChatCallOptions`\>

`{}`

`callbackManager`

`undefined` | [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

`undefined`

#### Returns[](#returns-9 "Direct link to Returns")

`Partial`<`OpenAIChatCallOptions`\>

#### Inherited from[](#inherited-from-39 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[\_patchConfig](/docs/api/llms_openai/classes/OpenAIChat#_patchconfig)

#### Defined in[](#defined-in-47 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:146](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L146)

### \_streamIterator()[](#_streamiterator "Direct link to _streamiterator")

> **\_streamIterator**(`input`: [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `options`?: `OpenAIChatCallOptions`): `AsyncGenerator`<`string`, `any`, `unknown`\>

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

`input`

[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)

`options?`

`OpenAIChatCallOptions`

#### Returns[](#returns-10 "Direct link to Returns")

`AsyncGenerator`<`string`, `any`, `unknown`\>

#### Inherited from[](#inherited-from-40 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[\_streamIterator](/docs/api/llms_openai/classes/OpenAIChat#_streamiterator)

#### Defined in[](#defined-in-48 "Direct link to Defined in")

[langchain/src/llms/base.ts:102](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L102)

### \_streamResponseChunks()[](#_streamresponsechunks "Direct link to _streamresponsechunks")

> **\_streamResponseChunks**(`prompt`: `string`, `options`: `Omit`<`OpenAIChatCallOptions`, `never`\>, `runManager`?: [`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)): `AsyncGenerator`<[`GenerationChunk`](/docs/api/schema/classes/GenerationChunk), `any`, `unknown`\>

#### Parameters[](#parameters-5 "Direct link to Parameters")

Parameter

Type

`prompt`

`string`

`options`

`Omit`<`OpenAIChatCallOptions`, `never`\>

`runManager?`

[`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)

#### Returns[](#returns-11 "Direct link to Returns")

`AsyncGenerator`<[`GenerationChunk`](/docs/api/schema/classes/GenerationChunk), `any`, `unknown`\>

#### Inherited from[](#inherited-from-41 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[\_streamResponseChunks](/docs/api/llms_openai/classes/OpenAIChat#_streamresponsechunks)

#### Defined in[](#defined-in-49 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:259](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L259)

### batch()[](#batch "Direct link to batch()")

> **batch**(`inputs`: [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)\[\], `options`?: `Partial`<`OpenAIChatCallOptions`\> | `Partial`<`OpenAIChatCallOptions`\>\[\], `batchOptions`?: `object`): `Promise`<`string`\[\]\>

#### Parameters[](#parameters-6 "Direct link to Parameters")

Parameter

Type

`inputs`

[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)\[\]

`options?`

`Partial`<`OpenAIChatCallOptions`\> | `Partial`<`OpenAIChatCallOptions`\>\[\]

`batchOptions?`

`object`

`batchOptions.maxConcurrency?`

`number`

#### Returns[](#returns-12 "Direct link to Returns")

`Promise`<`string`\[\]\>

#### Inherited from[](#inherited-from-42 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[batch](/docs/api/llms_openai/classes/OpenAIChat#batch)

#### Defined in[](#defined-in-50 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:63](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L63)

### bind()[](#bind "Direct link to bind()")

> **bind**(`kwargs`: `Partial`<`OpenAIChatCallOptions`\>): [`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `string`, `OpenAIChatCallOptions`\>

#### Parameters[](#parameters-7 "Direct link to Parameters")

Parameter

Type

`kwargs`

`Partial`<`OpenAIChatCallOptions`\>

#### Returns[](#returns-13 "Direct link to Returns")

[`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `string`, `OpenAIChatCallOptions`\>

#### Inherited from[](#inherited-from-43 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[bind](/docs/api/llms_openai/classes/OpenAIChat#bind)

#### Defined in[](#defined-in-51 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:41](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L41)

### call()[](#call "Direct link to call()")

Convenience wrapper for [generate](/docs/api/llms_base/classes/BaseLLM#generate) that takes in a single string prompt and returns a single string output.

> **call**(`prompt`: `string`, `options`?: `string`\[\] | `OpenAIChatCallOptions`, `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\>

#### Parameters[](#parameters-8 "Direct link to Parameters")

Parameter

Type

`prompt`

`string`

`options?`

`string`\[\] | `OpenAIChatCallOptions`

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-14 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[](#inherited-from-44 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[call](/docs/api/llms_openai/classes/OpenAIChat#call)

#### Defined in[](#defined-in-52 "Direct link to Defined in")

[langchain/src/llms/base.ts:343](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L343)

### completionWithRetry()[](#completionwithretry "Direct link to completionWithRetry()")

> **completionWithRetry**(`request`: `CreateChatCompletionRequest`, `options`?: `StreamingAxiosConfiguration`): `Promise`<`CreateChatCompletionResponse`\>

#### Parameters[](#parameters-9 "Direct link to Parameters")

Parameter

Type

`request`

`CreateChatCompletionRequest`

`options?`

`StreamingAxiosConfiguration`

#### Returns[](#returns-15 "Direct link to Returns")

`Promise`<`CreateChatCompletionResponse`\>

#### Overrides[](#overrides-5 "Direct link to Overrides")

OpenAIChat.completionWithRetry

#### Defined in[](#defined-in-53 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:576](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L576)

### generate()[](#generate "Direct link to generate()")

Run the LLM on the given prompts and input, handling caching.

> **generate**(`prompts`: `string`\[\], `options`?: `string`\[\] | `OpenAIChatCallOptions`, `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[](#parameters-10 "Direct link to Parameters")

Parameter

Type

`prompts`

`string`\[\]

`options?`

`string`\[\] | `OpenAIChatCallOptions`

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-16 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[](#inherited-from-45 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[generate](/docs/api/llms_openai/classes/OpenAIChat#generate)

#### Defined in[](#defined-in-54 "Direct link to Defined in")

[langchain/src/llms/base.ts:280](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L280)

### generatePrompt()[](#generateprompt "Direct link to generatePrompt()")

> **generatePrompt**(`promptValues`: [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\[\], `options`?: `string`\[\] | `OpenAIChatCallOptions`, `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[](#parameters-11 "Direct link to Parameters")

Parameter

Type

`promptValues`

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\[\]

`options?`

`string`\[\] | `OpenAIChatCallOptions`

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-17 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[](#inherited-from-46 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[generatePrompt](/docs/api/llms_openai/classes/OpenAIChat#generateprompt)

#### Defined in[](#defined-in-55 "Direct link to Defined in")

[langchain/src/llms/base.ts:169](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L169)

### getNumTokens()[](#getnumtokens "Direct link to getNumTokens()")

> **getNumTokens**(`text`: `string`): `Promise`<`number`\>

#### Parameters[](#parameters-12 "Direct link to Parameters")

Parameter

Type

`text`

`string`

#### Returns[](#returns-18 "Direct link to Returns")

`Promise`<`number`\>

#### Inherited from[](#inherited-from-47 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[getNumTokens](/docs/api/llms_openai/classes/OpenAIChat#getnumtokens)

#### Defined in[](#defined-in-56 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:166](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L166)

### identifyingParams()[](#identifyingparams "Direct link to identifyingParams()")

Get the identifying parameters for the model

> **identifyingParams**(): `object`

#### Returns[](#returns-19 "Direct link to Returns")

`object`

Member

Type

`model_name`

`string`

#### Inherited from[](#inherited-from-48 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[identifyingParams](/docs/api/llms_openai/classes/OpenAIChat#identifyingparams)

#### Defined in[](#defined-in-57 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:241](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L241)

### invocationParams()[](#invocationparams "Direct link to invocationParams()")

Get the parameters used to invoke the model

> **invocationParams**(`options`?: `Omit`<`OpenAIChatCallOptions`, `never`\>): `Omit`<`CreateChatCompletionRequest`, "messages"\>

#### Parameters[](#parameters-13 "Direct link to Parameters")

Parameter

Type

`options?`

`Omit`<`OpenAIChatCallOptions`, `never`\>

#### Returns[](#returns-20 "Direct link to Returns")

`Omit`<`CreateChatCompletionRequest`, "messages"\>

#### Inherited from[](#inherited-from-49 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[invocationParams](/docs/api/llms_openai/classes/OpenAIChat#invocationparams)

#### Defined in[](#defined-in-58 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:211](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L211)

### invoke()[](#invoke "Direct link to invoke()")

> **invoke**(`input`: [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `options`?: `OpenAIChatCallOptions`): `Promise`<`string`\>

#### Parameters[](#parameters-14 "Direct link to Parameters")

Parameter

Type

`input`

[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)

`options?`

`OpenAIChatCallOptions`

#### Returns[](#returns-21 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[](#inherited-from-50 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[invoke](/docs/api/llms_openai/classes/OpenAIChat#invoke)

#### Defined in[](#defined-in-59 "Direct link to Defined in")

[langchain/src/llms/base.ts:69](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L69)

### pipe()[](#pipe "Direct link to pipe()")

> **pipe**<NewRunOutput\>(`coerceable`: [`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<`string`, `NewRunOutput`\>): [`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `NewRunOutput`\>

#### Type parameters[](#type-parameters "Direct link to Type parameters")

*   `NewRunOutput`

#### Parameters[](#parameters-15 "Direct link to Parameters")

Parameter

Type

`coerceable`

[`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<`string`, `NewRunOutput`\>

#### Returns[](#returns-22 "Direct link to Returns")

[`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `NewRunOutput`\>

#### Inherited from[](#inherited-from-51 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[pipe](/docs/api/llms_openai/classes/OpenAIChat#pipe)

#### Defined in[](#defined-in-60 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:153](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L153)

### predict()[](#predict "Direct link to predict()")

> **predict**(`text`: `string`, `options`?: `string`\[\] | `OpenAIChatCallOptions`, `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\>

#### Parameters[](#parameters-16 "Direct link to Parameters")

Parameter

Type

`text`

`string`

`options?`

`string`\[\] | `OpenAIChatCallOptions`

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-23 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[](#inherited-from-52 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[predict](/docs/api/llms_openai/classes/OpenAIChat#predict)

#### Defined in[](#defined-in-61 "Direct link to Defined in")

[langchain/src/llms/base.ts:352](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L352)

### predictMessages()[](#predictmessages "Direct link to predictMessages()")

> **predictMessages**(`messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\], `options`?: `string`\[\] | `OpenAIChatCallOptions`, `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Parameters[](#parameters-17 "Direct link to Parameters")

Parameter

Type

`messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]

`options?`

`string`\[\] | `OpenAIChatCallOptions`

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-24 "Direct link to Returns")

`Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Inherited from[](#inherited-from-53 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[predictMessages](/docs/api/llms_openai/classes/OpenAIChat#predictmessages)

#### Defined in[](#defined-in-62 "Direct link to Defined in")

[langchain/src/llms/base.ts:360](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L360)

### serialize()[](#serialize "Direct link to serialize()")

Return a json-like object representing this LLM.

> **serialize**(): [`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Returns[](#returns-25 "Direct link to Returns")

[`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Inherited from[](#inherited-from-54 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[serialize](/docs/api/llms_openai/classes/OpenAIChat#serialize)

#### Defined in[](#defined-in-63 "Direct link to Defined in")

[langchain/src/llms/base.ts:386](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L386)

### startStream()[](#startstream "Direct link to startStream()")

> **startStream**(`request`: `CreateChatCompletionRequest`, `options`?: `StreamingAxiosConfiguration`): `object`

#### Parameters[](#parameters-18 "Direct link to Parameters")

Parameter

Type

`request`

`CreateChatCompletionRequest`

`options?`

`StreamingAxiosConfiguration`

#### Returns[](#returns-26 "Direct link to Returns")

`object`

Member

Type

`[asyncIterator]`

Method \[asyncIterator\]

`next`

Method next

#### Inherited from[](#inherited-from-55 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[startStream](/docs/api/llms_openai/classes/OpenAIChat#startstream)

#### Defined in[](#defined-in-64 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:298](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai-chat.ts#L298)

### stream()[](#stream "Direct link to stream()")

> **stream**(`input`: [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `options`?: `Partial`<`OpenAIChatCallOptions`\>): `Promise`<`IterableReadableStream`<`string`\>\>

#### Parameters[](#parameters-19 "Direct link to Parameters")

Parameter

Type

`input`

[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)

`options?`

`Partial`<`OpenAIChatCallOptions`\>

#### Returns[](#returns-27 "Direct link to Returns")

`Promise`<`IterableReadableStream`<`string`\>\>

#### Inherited from[](#inherited-from-56 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[stream](/docs/api/llms_openai/classes/OpenAIChat#stream)

#### Defined in[](#defined-in-65 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:93](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L93)

### toJSON()[](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[](#returns-28 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[](#inherited-from-57 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[toJSON](/docs/api/llms_openai/classes/OpenAIChat#tojson)

#### Defined in[](#defined-in-66 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[](#returns-29 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[](#inherited-from-58 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[toJSONNotImplemented](/docs/api/llms_openai/classes/OpenAIChat#tojsonnotimplemented)

#### Defined in[](#defined-in-67 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L151)

### deserialize()[](#deserialize "Direct link to deserialize()")

Load an LLM from a json-like object describing it.

> `Static` **deserialize**(`data`: [`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)): `Promise`<[`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>\>

#### Parameters[](#parameters-20 "Direct link to Parameters")

Parameter

Type

`data`

[`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Returns[](#returns-30 "Direct link to Returns")

`Promise`<[`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>\>

#### Inherited from[](#inherited-from-59 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[deserialize](/docs/api/llms_openai/classes/OpenAIChat#deserialize)

#### Defined in[](#defined-in-68 "Direct link to Defined in")

[langchain/src/llms/base.ts:401](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L401)

### isRunnable()[](#isrunnable "Direct link to isRunnable()")

> `Static` **isRunnable**(`thing`: `any`): thing is Runnable<any, any, BaseCallbackConfig\>

#### Parameters[](#parameters-21 "Direct link to Parameters")

Parameter

Type

`thing`

`any`

#### Returns[](#returns-31 "Direct link to Returns")

thing is Runnable<any, any, BaseCallbackConfig\>

#### Inherited from[](#inherited-from-60 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[isRunnable](/docs/api/llms_openai/classes/OpenAIChat#isrunnable)

#### Defined in[](#defined-in-69 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:164](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L164)

### \_callWithConfig()[](#_callwithconfig "Direct link to _callwithconfig")

> `Protected` **\_callWithConfig**<T\>(`func`: `Function`, `input`: `T`, `options`?: `BaseCallbackConfig` & {`runType`?: `string`;}): `Promise`<`string`\>

#### Type parameters[](#type-parameters-1 "Direct link to Type parameters")

*   `T` _extends_ [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)

#### Parameters[](#parameters-22 "Direct link to Parameters")

Parameter

Type

`func`

(`input`: `T`) => `Promise`<`string`\>

`input`

`T`

`options?`

`BaseCallbackConfig` & {`runType`?: `string`;}

#### Returns[](#returns-32 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[](#inherited-from-61 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[\_callWithConfig](/docs/api/llms_openai/classes/OpenAIChat#_callwithconfig)

#### Defined in[](#defined-in-70 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:117](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L117)

### \_getOptionsList()[](#_getoptionslist "Direct link to _getoptionslist")

> `Protected` **\_getOptionsList**(`options`: `Partial`<`OpenAIChatCallOptions`\> | `Partial`<`OpenAIChatCallOptions`\>\[\], `length`: `number` = `0`): `Partial`<`OpenAIChatCallOptions`\>\[\]

#### Parameters[](#parameters-23 "Direct link to Parameters")

Parameter

Type

Default value

`options`

`Partial`<`OpenAIChatCallOptions`\> | `Partial`<`OpenAIChatCallOptions`\>\[\]

`undefined`

`length`

`number`

`0`

#### Returns[](#returns-33 "Direct link to Returns")

`Partial`<`OpenAIChatCallOptions`\>\[\]

#### Inherited from[](#inherited-from-62 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[\_getOptionsList](/docs/api/llms_openai/classes/OpenAIChat#_getoptionslist)

#### Defined in[](#defined-in-71 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L48)

### \_separateRunnableConfigFromCallOptions()[](#_separaterunnableconfigfromcalloptions "Direct link to _separaterunnableconfigfromcalloptions")

> `Protected` **\_separateRunnableConfigFromCallOptions**(`options`?: `Partial`<`OpenAIChatCallOptions`\>): \[`BaseCallbackConfig`, `Omit`<`OpenAIChatCallOptions`, `never`\>\]

#### Parameters[](#parameters-24 "Direct link to Parameters")

Parameter

Type

`options?`

`Partial`<`OpenAIChatCallOptions`\>

#### Returns[](#returns-34 "Direct link to Returns")

\[`BaseCallbackConfig`, `Omit`<`OpenAIChatCallOptions`, `never`\>\]

#### Inherited from[](#inherited-from-63 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[\_separateRunnableConfigFromCallOptions](/docs/api/llms_openai/classes/OpenAIChat#_separaterunnableconfigfromcalloptions)

#### Defined in[](#defined-in-72 "Direct link to Defined in")

[langchain/src/llms/base.ts:91](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L91)

### \_convertInputToPromptValue()[](#_convertinputtopromptvalue "Direct link to _convertinputtopromptvalue")

> `Static` `Protected` **\_convertInputToPromptValue**(`input`: [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)): [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)

#### Parameters[](#parameters-25 "Direct link to Parameters")

Parameter

Type

`input`

[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)

#### Returns[](#returns-35 "Direct link to Returns")

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)

#### Inherited from[](#inherited-from-64 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[\_convertInputToPromptValue](/docs/api/llms_openai/classes/OpenAIChat#_convertinputtopromptvalue)

#### Defined in[](#defined-in-73 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:192](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L192)