PromptLayerOpenAIChat
=====================

PromptLayer wrapper to OpenAIChat

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`OpenAIChat`](/docs/api/llms_openai/classes/OpenAIChat).**PromptLayerOpenAIChat**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new PromptLayerOpenAIChat**(`fields`?: `Partial`<[`OpenAIChatInput`](/docs/api/chat_models_openai/interfaces/OpenAIChatInput)\> & `Partial`<[`AzureOpenAIInput`](/docs/api/llms_openai/interfaces/AzureOpenAIInput)\> & [`BaseLLMParams`](/docs/api/llms_base/interfaces/BaseLLMParams) & {`configuration`?: `ConfigurationParameters`;} & {`plTags`?: `string`\[\]; `promptLayerApiKey`?: `string`; `returnPromptLayerId`?: `boolean`;}): [`PromptLayerOpenAIChat`](/docs/api/llms_openai/classes/PromptLayerOpenAIChat)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields?`

`Partial`<[`OpenAIChatInput`](/docs/api/chat_models_openai/interfaces/OpenAIChatInput)\> & `Partial`<[`AzureOpenAIInput`](/docs/api/llms_openai/interfaces/AzureOpenAIInput)\> & [`BaseLLMParams`](/docs/api/llms_base/interfaces/BaseLLMParams) & {`configuration`?: `ConfigurationParameters`;} & {`plTags`?: `string`\[\];  
`promptLayerApiKey`?: `string`;  
`returnPromptLayerId`?: `boolean`;}

#### Returns[​](#returns "Direct link to Returns")

[`PromptLayerOpenAIChat`](/docs/api/llms_openai/classes/PromptLayerOpenAIChat)

#### Overrides[​](#overrides "Direct link to Overrides")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[constructor](/docs/api/llms_openai/classes/OpenAIChat#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:464](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L464)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### CallOptions[​](#calloptions "Direct link to CallOptions")

> **CallOptions**: `OpenAIChatCallOptions`

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[CallOptions](/docs/api/llms_openai/classes/OpenAIChat#calloptions)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:56](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L56)

### ParsedCallOptions[​](#parsedcalloptions "Direct link to ParsedCallOptions")

> **ParsedCallOptions**: `Omit`<`OpenAIChatCallOptions`, "callbacks" | "metadata" | "tags" | "timeout"\>

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[ParsedCallOptions](/docs/api/llms_openai/classes/OpenAIChat#parsedcalloptions)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/llms/base.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L46)

### caller[​](#caller "Direct link to caller")

> **caller**: `AsyncCaller`

The async caller should be used by subclasses to make any async calls, which will thus benefit from the concurrency and retry logic.

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[caller](/docs/api/llms_openai/classes/OpenAIChat#caller)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:116](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L116)

### frequencyPenalty[​](#frequencypenalty "Direct link to frequencyPenalty")

> **frequencyPenalty**: `number` = `0`

Penalizes repeated tokens according to frequency

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[frequencyPenalty](/docs/api/llms_openai/classes/OpenAIChat#frequencypenalty)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L90)

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[lc\_kwargs](/docs/api/llms_openai/classes/OpenAIChat#lc_kwargs)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[lc\_namespace](/docs/api/llms_openai/classes/OpenAIChat#lc_namespace)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/llms/base.ts:51](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L51)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[lc\_serializable](/docs/api/llms_openai/classes/OpenAIChat#lc_serializable)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:456](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L456)

### modelName[​](#modelname "Direct link to modelName")

> **modelName**: `string` = `"gpt-3.5-turbo"`

Model name to use

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[modelName](/docs/api/llms_openai/classes/OpenAIChat#modelname)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:100](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L100)

### n[​](#n "Direct link to n")

> **n**: `number` = `1`

Number of completions to generate for each prompt

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[n](/docs/api/llms_openai/classes/OpenAIChat#n)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:94](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L94)

### presencePenalty[​](#presencepenalty "Direct link to presencePenalty")

> **presencePenalty**: `number` = `0`

Penalizes repeated tokens

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[presencePenalty](/docs/api/llms_openai/classes/OpenAIChat#presencepenalty)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:92](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L92)

### streaming[​](#streaming "Direct link to streaming")

> **streaming**: `boolean` = `false`

Whether to stream the results or not. Enabling disables tokenUsage reporting

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[streaming](/docs/api/llms_openai/classes/OpenAIChat#streaming)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:110](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L110)

### temperature[​](#temperature "Direct link to temperature")

> **temperature**: `number` = `1`

Sampling temperature to use

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[temperature](/docs/api/llms_openai/classes/OpenAIChat#temperature)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:86](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L86)

### topP[​](#topp "Direct link to topP")

> **topP**: `number` = `1`

Total probability mass of tokens to consider at each step

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[topP](/docs/api/llms_openai/classes/OpenAIChat#topp)

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:88](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L88)

### verbose[​](#verbose "Direct link to verbose")

> **verbose**: `boolean`

Whether to print out response text.

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[verbose](/docs/api/llms_openai/classes/OpenAIChat#verbose)

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:38](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L38)

### azureOpenAIApiDeploymentName?[​](#azureopenaiapideploymentname "Direct link to azureOpenAIApiDeploymentName?")

> **azureOpenAIApiDeploymentName**: `string`

Azure OpenAI API deployment name to use for completions when making requests to Azure OpenAI. This is the name of the deployment you created in the Azure portal. e.g. "my-openai-deployment" this will be used in the endpoint URL: https://{InstanceName}.openai.azure.com/openai/deployments/my-openai-deployment/

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[azureOpenAIApiDeploymentName](/docs/api/llms_openai/classes/OpenAIChat#azureopenaiapideploymentname)

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:120](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L120)

### azureOpenAIApiInstanceName?[​](#azureopenaiapiinstancename "Direct link to azureOpenAIApiInstanceName?")

> **azureOpenAIApiInstanceName**: `string`

Azure OpenAI API instance name to use when making requests to Azure OpenAI. this is the name of the instance you created in the Azure portal. e.g. "my-openai-instance" this will be used in the endpoint URL: [https://my-openai-instance.openai.azure.com/openai/deployments/{DeploymentName}/](https://my-openai-instance.openai.azure.com/openai/deployments/%7BDeploymentName%7D/)

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[azureOpenAIApiInstanceName](/docs/api/llms_openai/classes/OpenAIChat#azureopenaiapiinstancename)

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:118](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L118)

### azureOpenAIApiKey?[​](#azureopenaiapikey "Direct link to azureOpenAIApiKey?")

> **azureOpenAIApiKey**: `string`

API key to use when making requests to Azure OpenAI.

#### Inherited from[​](#inherited-from-15 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[azureOpenAIApiKey](/docs/api/llms_openai/classes/OpenAIChat#azureopenaiapikey)

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:116](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L116)

### azureOpenAIApiVersion?[​](#azureopenaiapiversion "Direct link to azureOpenAIApiVersion?")

> **azureOpenAIApiVersion**: `string`

API version to use when making requests to Azure OpenAI.

#### Inherited from[​](#inherited-from-16 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[azureOpenAIApiVersion](/docs/api/llms_openai/classes/OpenAIChat#azureopenaiapiversion)

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:114](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L114)

### azureOpenAIBasePath?[​](#azureopenaibasepath "Direct link to azureOpenAIBasePath?")

> **azureOpenAIBasePath**: `string`

Custom endpoint for Azure OpenAI API. This is useful in case you have a deployment in another region. e.g. setting this value to "[https://westeurope.api.cognitive.microsoft.com/openai/deployments"](https://westeurope.api.cognitive.microsoft.com/openai/deployments%22) will be result in the endpoint URL: [https://westeurope.api.cognitive.microsoft.com/openai/deployments/{DeploymentName}/](https://westeurope.api.cognitive.microsoft.com/openai/deployments/%7BDeploymentName%7D/)

#### Inherited from[​](#inherited-from-17 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[azureOpenAIBasePath](/docs/api/llms_openai/classes/OpenAIChat#azureopenaibasepath)

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:122](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L122)

### cache?[​](#cache "Direct link to cache?")

> **cache**: [`BaseCache`](/docs/api/schema/classes/BaseCache)<[`Generation`](/docs/api/schema/interfaces/Generation)\[\]\>

#### Inherited from[​](#inherited-from-18 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[cache](/docs/api/llms_openai/classes/OpenAIChat#cache)

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/llms/base.ts:53](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L53)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[​](#inherited-from-19 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[callbacks](/docs/api/llms_openai/classes/OpenAIChat#callbacks)

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L40)

### logitBias?[​](#logitbias "Direct link to logitBias?")

> **logitBias**: `Record`<`string`, `number`\>

Dictionary used to adjust the probability of specific tokens being generated

#### Inherited from[​](#inherited-from-20 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[logitBias](/docs/api/llms_openai/classes/OpenAIChat#logitbias)

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:96](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L96)

### maxTokens?[​](#maxtokens "Direct link to maxTokens?")

> **maxTokens**: `number`

Maximum number of tokens to generate in the completion. -1 returns as many tokens as possible given the prompt and the model's maximum context size.

#### Inherited from[​](#inherited-from-21 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[maxTokens](/docs/api/llms_openai/classes/OpenAIChat#maxtokens)

#### Defined in[​](#defined-in-23 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L98)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[​](#inherited-from-22 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[metadata](/docs/api/llms_openai/classes/OpenAIChat#metadata)

#### Defined in[​](#defined-in-24 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:44](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L44)

### modelKwargs?[​](#modelkwargs "Direct link to modelKwargs?")

> **modelKwargs**: `Record`<`string`, `any`\>

Holds any additional parameters that are valid to pass to [`openai.createCompletion`](https://platform.openai.com/docs/api-reference/completions/create) that are not explicitly specified on this class.

#### Inherited from[​](#inherited-from-23 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[modelKwargs](/docs/api/llms_openai/classes/OpenAIChat#modelkwargs)

#### Defined in[​](#defined-in-25 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:104](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L104)

### openAIApiKey?[​](#openaiapikey "Direct link to openAIApiKey?")

> **openAIApiKey**: `string`

API key to use when making requests to OpenAI. Defaults to the value of `OPENAI_API_KEY` environment variable.

#### Inherited from[​](#inherited-from-24 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[openAIApiKey](/docs/api/llms_openai/classes/OpenAIChat#openaiapikey)

#### Defined in[​](#defined-in-26 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:112](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L112)

### plTags?[​](#pltags "Direct link to plTags?")

> **plTags**: `string`\[\]

#### Defined in[​](#defined-in-27 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:460](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L460)

### prefixMessages?[​](#prefixmessages "Direct link to prefixMessages?")

> **prefixMessages**: `ChatCompletionRequestMessage`\[\]

ChatGPT messages to pass as a prefix to the prompt

#### Inherited from[​](#inherited-from-25 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[prefixMessages](/docs/api/llms_openai/classes/OpenAIChat#prefixmessages)

#### Defined in[​](#defined-in-28 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:102](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L102)

### promptLayerApiKey?[​](#promptlayerapikey "Direct link to promptLayerApiKey?")

> **promptLayerApiKey**: `string`

#### Defined in[​](#defined-in-29 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:458](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L458)

### returnPromptLayerId?[​](#returnpromptlayerid "Direct link to returnPromptLayerId?")

> **returnPromptLayerId**: `boolean`

#### Defined in[​](#defined-in-30 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:462](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L462)

### stop?[​](#stop "Direct link to stop?")

> **stop**: `string`\[\]

List of stop words to use when generating

#### Inherited from[​](#inherited-from-26 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[stop](/docs/api/llms_openai/classes/OpenAIChat#stop)

#### Defined in[​](#defined-in-31 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:108](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L108)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[​](#inherited-from-27 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[tags](/docs/api/llms_openai/classes/OpenAIChat#tags)

#### Defined in[​](#defined-in-32 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L42)

### timeout?[​](#timeout "Direct link to timeout?")

> **timeout**: `number`

Timeout to use when making requests to OpenAI.

#### Inherited from[​](#inherited-from-28 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[timeout](/docs/api/llms_openai/classes/OpenAIChat#timeout)

#### Defined in[​](#defined-in-33 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:106](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L106)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### callKeys[​](#callkeys "Direct link to callKeys")

Keys that the language model accepts as call options.

> **callKeys**(): _keyof_ `OpenAIChatCallOptions`\[\]

#### Returns[​](#returns-1 "Direct link to Returns")

_keyof_ `OpenAIChatCallOptions`\[\]

#### Inherited from[​](#inherited-from-29 "Direct link to Inherited from")

OpenAIChat.callKeys

#### Defined in[​](#defined-in-34 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:58](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L58)

#### Inherited from[​](#inherited-from-30 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[callKeys](/docs/api/llms_openai/classes/OpenAIChat#callkeys)

#### Defined in[​](#defined-in-35 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:58](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L58)

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `Record`<`string`, `string`\>

#### Returns[​](#returns-2 "Direct link to Returns")

`Record`<`string`, `string`\>

#### Inherited from[​](#inherited-from-31 "Direct link to Inherited from")

OpenAIChat.lc\_aliases

#### Defined in[​](#defined-in-36 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:75](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L75)

#### Inherited from[​](#inherited-from-32 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[lc\_aliases](/docs/api/llms_openai/classes/OpenAIChat#lc_aliases)

#### Defined in[​](#defined-in-37 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:75](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L75)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-33 "Direct link to Inherited from")

OpenAIChat.lc\_attributes

#### Defined in[​](#defined-in-38 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

#### Inherited from[​](#inherited-from-34 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[lc\_attributes](/docs/api/llms_openai/classes/OpenAIChat#lc_attributes)

#### Defined in[​](#defined-in-39 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-4 "Direct link to Returns")

`undefined` | {}

#### Overrides[​](#overrides-2 "Direct link to Overrides")

OpenAIChat.lc\_secrets

#### Defined in[​](#defined-in-40 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:450](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L450)

#### Overrides[​](#overrides-3 "Direct link to Overrides")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[lc\_secrets](/docs/api/llms_openai/classes/OpenAIChat#lc_secrets)

#### Defined in[​](#defined-in-41 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:450](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L450)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### \_flattenLLMResult()[​](#_flattenllmresult "Direct link to _flattenllmresult")

> **\_flattenLLMResult**(`llmResult`: [`LLMResult`](/docs/api/schema/types/LLMResult)): [`LLMResult`](/docs/api/schema/types/LLMResult)\[\]

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`llmResult`

[`LLMResult`](/docs/api/schema/types/LLMResult)

#### Returns[​](#returns-5 "Direct link to Returns")

[`LLMResult`](/docs/api/schema/types/LLMResult)\[\]

#### Inherited from[​](#inherited-from-35 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[\_flattenLLMResult](/docs/api/llms_openai/classes/OpenAIChat#_flattenllmresult)

#### Defined in[​](#defined-in-42 "Direct link to Defined in")

[langchain/src/llms/base.ts:94](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L94)

### \_generate()[​](#_generate "Direct link to _generate")

Run the LLM on the given prompts and input.

> **\_generate**(`prompts`: `string`\[\], `options`: `Omit`<`OpenAIChatCallOptions`, "callbacks" | "metadata" | "tags" | "timeout"\>, `runManager`?: [`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`prompts`

`string`\[\]

`options`

`Omit`<`OpenAIChatCallOptions`, "callbacks" | "metadata" | "tags" | "timeout"\>

`runManager?`

[`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)

#### Returns[​](#returns-6 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Overrides[​](#overrides-4 "Direct link to Overrides")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[\_generate](/docs/api/llms_openai/classes/OpenAIChat#_generate)

#### Defined in[​](#defined-in-43 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:497](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L497)

### \_llmType()[​](#_llmtype "Direct link to _llmtype")

Return the string type key uniquely identifying this class of LLM.

> **\_llmType**(): `string`

#### Returns[​](#returns-7 "Direct link to Returns")

`string`

#### Inherited from[​](#inherited-from-36 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[\_llmType](/docs/api/llms_openai/classes/OpenAIChat#_llmtype)

#### Defined in[​](#defined-in-44 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:441](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L441)

### \_modelType()[​](#_modeltype "Direct link to _modeltype")

> **\_modelType**(): `string`

#### Returns[​](#returns-8 "Direct link to Returns")

`string`

#### Inherited from[​](#inherited-from-37 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[\_modelType](/docs/api/llms_openai/classes/OpenAIChat#_modeltype)

#### Defined in[​](#defined-in-45 "Direct link to Defined in")

[langchain/src/llms/base.ts:304](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L304)

### call()[​](#call "Direct link to call()")

Convenience wrapper for [generate](/docs/api/llms_base/classes/BaseLLM#generate) that takes in a single string prompt and returns a single string output.

> **call**(`prompt`: `string`, `options`?: `string`\[\] | `OpenAIChatCallOptions`, `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`prompt`

`string`

`options?`

`string`\[\] | `OpenAIChatCallOptions`

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-9 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[​](#inherited-from-38 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[call](/docs/api/llms_openai/classes/OpenAIChat#call)

#### Defined in[​](#defined-in-46 "Direct link to Defined in")

[langchain/src/llms/base.ts:249](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L249)

### completionWithRetry()[​](#completionwithretry "Direct link to completionWithRetry()")

> **completionWithRetry**(`request`: `CreateChatCompletionRequest`, `options`?: `StreamingAxiosConfiguration`): `Promise`<`CreateChatCompletionResponse`\>

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`request`

`CreateChatCompletionRequest`

`options?`

`StreamingAxiosConfiguration`

#### Returns[​](#returns-10 "Direct link to Returns")

`Promise`<`CreateChatCompletionResponse`\>

#### Overrides[​](#overrides-5 "Direct link to Overrides")

OpenAIChat.completionWithRetry

#### Defined in[​](#defined-in-47 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:484](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L484)

### generate()[​](#generate "Direct link to generate()")

Run the LLM on the given propmts an input, handling caching.

> **generate**(`prompts`: `string`\[\], `options`?: `string`\[\] | `OpenAIChatCallOptions`, `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[​](#parameters-5 "Direct link to Parameters")

Parameter

Type

`prompts`

`string`\[\]

`options?`

`string`\[\] | `OpenAIChatCallOptions`

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-11 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[​](#inherited-from-39 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[generate](/docs/api/llms_openai/classes/OpenAIChat#generate)

#### Defined in[​](#defined-in-48 "Direct link to Defined in")

[langchain/src/llms/base.ts:177](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L177)

### generatePrompt()[​](#generateprompt "Direct link to generatePrompt()")

> **generatePrompt**(`promptValues`: [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\[\], `options`?: `string`\[\] | `OpenAIChatCallOptions`, `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[​](#parameters-6 "Direct link to Parameters")

Parameter

Type

`promptValues`

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\[\]

`options?`

`string`\[\] | `OpenAIChatCallOptions`

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-12 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[​](#inherited-from-40 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[generatePrompt](/docs/api/llms_openai/classes/OpenAIChat#generateprompt)

#### Defined in[​](#defined-in-49 "Direct link to Defined in")

[langchain/src/llms/base.ts:66](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L66)

### getNumTokens()[​](#getnumtokens "Direct link to getNumTokens()")

> **getNumTokens**(`text`: `string`): `Promise`<`number`\>

#### Parameters[​](#parameters-7 "Direct link to Parameters")

Parameter

Type

`text`

`string`

#### Returns[​](#returns-13 "Direct link to Returns")

`Promise`<`number`\>

#### Inherited from[​](#inherited-from-41 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[getNumTokens](/docs/api/llms_openai/classes/OpenAIChat#getnumtokens)

#### Defined in[​](#defined-in-50 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:154](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L154)

### identifyingParams()[​](#identifyingparams "Direct link to identifyingParams()")

Get the identifying parameters for the model

> **identifyingParams**(): `object`

#### Returns[​](#returns-14 "Direct link to Returns")

`object`

Member

Type

`model_name`

`string`

#### Inherited from[​](#inherited-from-42 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[identifyingParams](/docs/api/llms_openai/classes/OpenAIChat#identifyingparams)

#### Defined in[​](#defined-in-51 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:242](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L242)

### invocationParams()[​](#invocationparams "Direct link to invocationParams()")

Get the parameters used to invoke the model

> **invocationParams**(`options`?: `Omit`<`OpenAIChatCallOptions`, "callbacks" | "metadata" | "tags" | "timeout"\>): `Omit`<`CreateChatCompletionRequest`, "messages"\>

#### Parameters[​](#parameters-8 "Direct link to Parameters")

Parameter

Type

`options?`

`Omit`<`OpenAIChatCallOptions`, "callbacks" | "metadata" | "tags" | "timeout"\>

#### Returns[​](#returns-15 "Direct link to Returns")

`Omit`<`CreateChatCompletionRequest`, "messages"\>

#### Inherited from[​](#inherited-from-43 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[invocationParams](/docs/api/llms_openai/classes/OpenAIChat#invocationparams)

#### Defined in[​](#defined-in-52 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:212](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L212)

### predict()[​](#predict "Direct link to predict()")

> **predict**(`text`: `string`, `options`?: `string`\[\] | `OpenAIChatCallOptions`, `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\>

#### Parameters[​](#parameters-9 "Direct link to Parameters")

Parameter

Type

`text`

`string`

`options?`

`string`\[\] | `OpenAIChatCallOptions`

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-16 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[​](#inherited-from-44 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[predict](/docs/api/llms_openai/classes/OpenAIChat#predict)

#### Defined in[​](#defined-in-53 "Direct link to Defined in")

[langchain/src/llms/base.ts:262](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L262)

### predictMessages()[​](#predictmessages "Direct link to predictMessages()")

> **predictMessages**(`messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\], `options`?: `string`\[\] | `OpenAIChatCallOptions`, `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Parameters[​](#parameters-10 "Direct link to Parameters")

Parameter

Type

`messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]

`options?`

`string`\[\] | `OpenAIChatCallOptions`

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-17 "Direct link to Returns")

`Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Inherited from[​](#inherited-from-45 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[predictMessages](/docs/api/llms_openai/classes/OpenAIChat#predictmessages)

#### Defined in[​](#defined-in-54 "Direct link to Defined in")

[langchain/src/llms/base.ts:270](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L270)

### serialize()[​](#serialize "Direct link to serialize()")

Return a json-like object representing this LLM.

> **serialize**(): [`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Returns[​](#returns-18 "Direct link to Returns")

[`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Inherited from[​](#inherited-from-46 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[serialize](/docs/api/llms_openai/classes/OpenAIChat#serialize)

#### Defined in[​](#defined-in-55 "Direct link to Defined in")

[langchain/src/llms/base.ts:296](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L296)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-19 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-47 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[toJSON](/docs/api/llms_openai/classes/OpenAIChat#tojson)

#### Defined in[​](#defined-in-56 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-20 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-48 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[toJSONNotImplemented](/docs/api/llms_openai/classes/OpenAIChat#tojsonnotimplemented)

#### Defined in[​](#defined-in-57 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)

### deserialize()[​](#deserialize "Direct link to deserialize()")

Load an LLM from a json-like object describing it.

> `Static` **deserialize**(`data`: [`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)): `Promise`<[`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)\>

#### Parameters[​](#parameters-11 "Direct link to Parameters")

Parameter

Type

`data`

[`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Returns[​](#returns-21 "Direct link to Returns")

`Promise`<[`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)\>

#### Inherited from[​](#inherited-from-49 "Direct link to Inherited from")

[OpenAIChat](/docs/api/llms_openai/classes/OpenAIChat).[deserialize](/docs/api/llms_openai/classes/OpenAIChat#deserialize)

#### Defined in[​](#defined-in-58 "Direct link to Defined in")

[langchain/src/llms/base.ts:311](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L311)