PromptLayerOpenAI
=================

PromptLayer wrapper to OpenAI

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`OpenAI`](/docs/api/llms_openai/classes/OpenAI).**PromptLayerOpenAI**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new PromptLayerOpenAI**(`fields`?: `Partial`<[`OpenAIInput`](/docs/api/llms_openai/interfaces/OpenAIInput)\> & `Partial`<[`AzureOpenAIInput`](/docs/api/llms_openai/interfaces/AzureOpenAIInput)\> & [`BaseLLMParams`](/docs/api/llms_base/interfaces/BaseLLMParams) & {`configuration`?: `ConfigurationParameters`;} & {`plTags`?: `string`\[\]; `promptLayerApiKey`?: `string`; `returnPromptLayerId`?: `boolean`;}): [`PromptLayerOpenAI`](/docs/api/llms_openai/classes/PromptLayerOpenAI)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields?`

`Partial`<[`OpenAIInput`](/docs/api/llms_openai/interfaces/OpenAIInput)\> & `Partial`<[`AzureOpenAIInput`](/docs/api/llms_openai/interfaces/AzureOpenAIInput)\> & [`BaseLLMParams`](/docs/api/llms_base/interfaces/BaseLLMParams) & {`configuration`?: `ConfigurationParameters`;} & {`plTags`?: `string`\[\];  
`promptLayerApiKey`?: `string`;  
`returnPromptLayerId`?: `boolean`;}

#### Returns[​](#returns "Direct link to Returns")

[`PromptLayerOpenAI`](/docs/api/llms_openai/classes/PromptLayerOpenAI)

#### Overrides[​](#overrides "Direct link to Overrides")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[constructor](/docs/api/llms_openai/classes/OpenAI#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/llms/openai.ts:503](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L503)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### CallOptions[​](#calloptions "Direct link to CallOptions")

> **CallOptions**: [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[CallOptions](/docs/api/llms_openai/classes/OpenAI#calloptions)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/llms/openai.ts:54](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L54)

### ParsedCallOptions[​](#parsedcalloptions "Direct link to ParsedCallOptions")

> **ParsedCallOptions**: `Omit`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[ParsedCallOptions](/docs/api/llms_openai/classes/OpenAI#parsedcalloptions)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/llms/base.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L46)

### batchSize[​](#batchsize "Direct link to batchSize")

> **batchSize**: `number` = `20`

Batch size to use when passing multiple documents to generate

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[batchSize](/docs/api/llms_openai/classes/OpenAI#batchsize)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/llms/openai.ts:100](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L100)

### caller[​](#caller "Direct link to caller")

> **caller**: `AsyncCaller`

The async caller should be used by subclasses to make any async calls, which will thus benefit from the concurrency and retry logic.

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[caller](/docs/api/llms_openai/classes/OpenAI#caller)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:116](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L116)

### frequencyPenalty[​](#frequencypenalty "Direct link to frequencyPenalty")

> **frequencyPenalty**: `number` = `0`

Penalizes repeated tokens according to frequency

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[frequencyPenalty](/docs/api/llms_openai/classes/OpenAI#frequencypenalty)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/llms/openai.ts:86](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L86)

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[lc\_kwargs](/docs/api/llms_openai/classes/OpenAI#lc_kwargs)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[lc\_namespace](/docs/api/llms_openai/classes/OpenAI#lc_namespace)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/llms/base.ts:51](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L51)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[lc\_serializable](/docs/api/llms_openai/classes/OpenAI#lc_serializable)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/llms/openai.ts:495](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L495)

### maxTokens[​](#maxtokens "Direct link to maxTokens")

> **maxTokens**: `number` = `256`

Maximum number of tokens to generate in the completion. -1 returns as many tokens as possible given the prompt and the model's maximum context size.

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[maxTokens](/docs/api/llms_openai/classes/OpenAI#maxtokens)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/llms/openai.ts:82](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L82)

### modelName[​](#modelname "Direct link to modelName")

> **modelName**: `string` = `"text-davinci-003"`

Model name to use

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[modelName](/docs/api/llms_openai/classes/OpenAI#modelname)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/llms/openai.ts:96](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L96)

### n[​](#n "Direct link to n")

> **n**: `number` = `1`

Number of completions to generate for each prompt

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[n](/docs/api/llms_openai/classes/OpenAI#n)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/llms/openai.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L90)

### presencePenalty[​](#presencepenalty "Direct link to presencePenalty")

> **presencePenalty**: `number` = `0`

Penalizes repeated tokens

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[presencePenalty](/docs/api/llms_openai/classes/OpenAI#presencepenalty)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/llms/openai.ts:88](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L88)

### streaming[​](#streaming "Direct link to streaming")

> **streaming**: `boolean` = `false`

Whether to stream the results or not. Enabling disables tokenUsage reporting

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[streaming](/docs/api/llms_openai/classes/OpenAI#streaming)

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/llms/openai.ts:106](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L106)

### temperature[​](#temperature "Direct link to temperature")

> **temperature**: `number` = `0.7`

Sampling temperature to use

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[temperature](/docs/api/llms_openai/classes/OpenAI#temperature)

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/llms/openai.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L80)

### topP[​](#topp "Direct link to topP")

> **topP**: `number` = `1`

Total probability mass of tokens to consider at each step

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[topP](/docs/api/llms_openai/classes/OpenAI#topp)

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/llms/openai.ts:84](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L84)

### verbose[​](#verbose "Direct link to verbose")

> **verbose**: `boolean`

Whether to print out response text.

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[verbose](/docs/api/llms_openai/classes/OpenAI#verbose)

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:38](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L38)

### azureOpenAIApiDeploymentName?[​](#azureopenaiapideploymentname "Direct link to azureOpenAIApiDeploymentName?")

> **azureOpenAIApiDeploymentName**: `string`

Azure OpenAI API deployment name to use for completions when making requests to Azure OpenAI. This is the name of the deployment you created in the Azure portal. e.g. "my-openai-deployment" this will be used in the endpoint URL: https://{InstanceName}.openai.azure.com/openai/deployments/my-openai-deployment/

#### Inherited from[​](#inherited-from-15 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[azureOpenAIApiDeploymentName](/docs/api/llms_openai/classes/OpenAI#azureopenaiapideploymentname)

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/llms/openai.ts:116](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L116)

### azureOpenAIApiInstanceName?[​](#azureopenaiapiinstancename "Direct link to azureOpenAIApiInstanceName?")

> **azureOpenAIApiInstanceName**: `string`

Azure OpenAI API instance name to use when making requests to Azure OpenAI. this is the name of the instance you created in the Azure portal. e.g. "my-openai-instance" this will be used in the endpoint URL: [https://my-openai-instance.openai.azure.com/openai/deployments/{DeploymentName}/](https://my-openai-instance.openai.azure.com/openai/deployments/%7BDeploymentName%7D/)

#### Inherited from[​](#inherited-from-16 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[azureOpenAIApiInstanceName](/docs/api/llms_openai/classes/OpenAI#azureopenaiapiinstancename)

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/llms/openai.ts:114](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L114)

### azureOpenAIApiKey?[​](#azureopenaiapikey "Direct link to azureOpenAIApiKey?")

> **azureOpenAIApiKey**: `string`

API key to use when making requests to Azure OpenAI.

#### Inherited from[​](#inherited-from-17 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[azureOpenAIApiKey](/docs/api/llms_openai/classes/OpenAI#azureopenaiapikey)

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/llms/openai.ts:112](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L112)

### azureOpenAIApiVersion?[​](#azureopenaiapiversion "Direct link to azureOpenAIApiVersion?")

> **azureOpenAIApiVersion**: `string`

API version to use when making requests to Azure OpenAI.

#### Inherited from[​](#inherited-from-18 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[azureOpenAIApiVersion](/docs/api/llms_openai/classes/OpenAI#azureopenaiapiversion)

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/llms/openai.ts:110](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L110)

### azureOpenAIBasePath?[​](#azureopenaibasepath "Direct link to azureOpenAIBasePath?")

> **azureOpenAIBasePath**: `string`

Custom endpoint for Azure OpenAI API. This is useful in case you have a deployment in another region. e.g. setting this value to "[https://westeurope.api.cognitive.microsoft.com/openai/deployments"](https://westeurope.api.cognitive.microsoft.com/openai/deployments%22) will be result in the endpoint URL: [https://westeurope.api.cognitive.microsoft.com/openai/deployments/{DeploymentName}/](https://westeurope.api.cognitive.microsoft.com/openai/deployments/%7BDeploymentName%7D/)

#### Inherited from[​](#inherited-from-19 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[azureOpenAIBasePath](/docs/api/llms_openai/classes/OpenAI#azureopenaibasepath)

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/llms/openai.ts:118](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L118)

### bestOf?[​](#bestof "Direct link to bestOf?")

> **bestOf**: `number`

Generates `bestOf` completions server side and returns the "best"

#### Inherited from[​](#inherited-from-20 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[bestOf](/docs/api/llms_openai/classes/OpenAI#bestof)

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/llms/openai.ts:92](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L92)

### cache?[​](#cache "Direct link to cache?")

> **cache**: [`BaseCache`](/docs/api/schema/classes/BaseCache)<[`Generation`](/docs/api/schema/interfaces/Generation)\[\]\>

#### Inherited from[​](#inherited-from-21 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[cache](/docs/api/llms_openai/classes/OpenAI#cache)

#### Defined in[​](#defined-in-23 "Direct link to Defined in")

[langchain/src/llms/base.ts:53](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L53)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[​](#inherited-from-22 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[callbacks](/docs/api/llms_openai/classes/OpenAI#callbacks)

#### Defined in[​](#defined-in-24 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L40)

### logitBias?[​](#logitbias "Direct link to logitBias?")

> **logitBias**: `Record`<`string`, `number`\>

Dictionary used to adjust the probability of specific tokens being generated

#### Inherited from[​](#inherited-from-23 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[logitBias](/docs/api/llms_openai/classes/OpenAI#logitbias)

#### Defined in[​](#defined-in-25 "Direct link to Defined in")

[langchain/src/llms/openai.ts:94](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L94)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[​](#inherited-from-24 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[metadata](/docs/api/llms_openai/classes/OpenAI#metadata)

#### Defined in[​](#defined-in-26 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:44](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L44)

### modelKwargs?[​](#modelkwargs "Direct link to modelKwargs?")

> **modelKwargs**: `Record`<`string`, `any`\>

Holds any additional parameters that are valid to pass to [`openai.createCompletion`](https://platform.openai.com/docs/api-reference/completions/create) that are not explicitly specified on this class.

#### Inherited from[​](#inherited-from-25 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[modelKwargs](/docs/api/llms_openai/classes/OpenAI#modelkwargs)

#### Defined in[​](#defined-in-27 "Direct link to Defined in")

[langchain/src/llms/openai.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L98)

### openAIApiKey?[​](#openaiapikey "Direct link to openAIApiKey?")

> **openAIApiKey**: `string`

API key to use when making requests to OpenAI. Defaults to the value of `OPENAI_API_KEY` environment variable.

#### Inherited from[​](#inherited-from-26 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[openAIApiKey](/docs/api/llms_openai/classes/OpenAI#openaiapikey)

#### Defined in[​](#defined-in-28 "Direct link to Defined in")

[langchain/src/llms/openai.ts:108](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L108)

### plTags?[​](#pltags "Direct link to plTags?")

> **plTags**: `string`\[\]

#### Defined in[​](#defined-in-29 "Direct link to Defined in")

[langchain/src/llms/openai.ts:499](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L499)

### promptLayerApiKey?[​](#promptlayerapikey "Direct link to promptLayerApiKey?")

> **promptLayerApiKey**: `string`

#### Defined in[​](#defined-in-30 "Direct link to Defined in")

[langchain/src/llms/openai.ts:497](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L497)

### returnPromptLayerId?[​](#returnpromptlayerid "Direct link to returnPromptLayerId?")

> **returnPromptLayerId**: `boolean`

#### Defined in[​](#defined-in-31 "Direct link to Defined in")

[langchain/src/llms/openai.ts:501](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L501)

### stop?[​](#stop "Direct link to stop?")

> **stop**: `string`\[\]

List of stop words to use when generating

#### Inherited from[​](#inherited-from-27 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[stop](/docs/api/llms_openai/classes/OpenAI#stop)

#### Defined in[​](#defined-in-32 "Direct link to Defined in")

[langchain/src/llms/openai.ts:104](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L104)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[​](#inherited-from-28 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[tags](/docs/api/llms_openai/classes/OpenAI#tags)

#### Defined in[​](#defined-in-33 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L42)

### timeout?[​](#timeout "Direct link to timeout?")

> **timeout**: `number`

Timeout to use when making requests to OpenAI.

#### Inherited from[​](#inherited-from-29 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[timeout](/docs/api/llms_openai/classes/OpenAI#timeout)

#### Defined in[​](#defined-in-34 "Direct link to Defined in")

[langchain/src/llms/openai.ts:102](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L102)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### callKeys[​](#callkeys "Direct link to callKeys")

Keys that the language model accepts as call options.

> **callKeys**(): _keyof_ [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)\[\]

#### Returns[​](#returns-1 "Direct link to Returns")

_keyof_ [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)\[\]

#### Inherited from[​](#inherited-from-30 "Direct link to Inherited from")

OpenAI.callKeys

#### Defined in[​](#defined-in-35 "Direct link to Defined in")

[langchain/src/llms/openai.ts:56](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L56)

#### Inherited from[​](#inherited-from-31 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[callKeys](/docs/api/llms_openai/classes/OpenAI#callkeys)

#### Defined in[​](#defined-in-36 "Direct link to Defined in")

[langchain/src/llms/openai.ts:56](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L56)

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `Record`<`string`, `string`\>

#### Returns[​](#returns-2 "Direct link to Returns")

`Record`<`string`, `string`\>

#### Inherited from[​](#inherited-from-32 "Direct link to Inherited from")

OpenAI.lc\_aliases

#### Defined in[​](#defined-in-37 "Direct link to Defined in")

[langchain/src/llms/openai.ts:69](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L69)

#### Inherited from[​](#inherited-from-33 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[lc\_aliases](/docs/api/llms_openai/classes/OpenAI#lc_aliases)

#### Defined in[​](#defined-in-38 "Direct link to Defined in")

[langchain/src/llms/openai.ts:69](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L69)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-34 "Direct link to Inherited from")

OpenAI.lc\_attributes

#### Defined in[​](#defined-in-39 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

#### Inherited from[​](#inherited-from-35 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[lc\_attributes](/docs/api/llms_openai/classes/OpenAI#lc_attributes)

#### Defined in[​](#defined-in-40 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-4 "Direct link to Returns")

`undefined` | {}

#### Overrides[​](#overrides-2 "Direct link to Overrides")

OpenAI.lc\_secrets

#### Defined in[​](#defined-in-41 "Direct link to Defined in")

[langchain/src/llms/openai.ts:489](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L489)

#### Overrides[​](#overrides-3 "Direct link to Overrides")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[lc\_secrets](/docs/api/llms_openai/classes/OpenAI#lc_secrets)

#### Defined in[​](#defined-in-42 "Direct link to Defined in")

[langchain/src/llms/openai.ts:489](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L489)

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

#### Inherited from[​](#inherited-from-36 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[\_flattenLLMResult](/docs/api/llms_openai/classes/OpenAI#_flattenllmresult)

#### Defined in[​](#defined-in-43 "Direct link to Defined in")

[langchain/src/llms/base.ts:94](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L94)

### \_generate()[​](#_generate "Direct link to _generate")

Call out to OpenAI's endpoint with k unique prompts

#### Example[​](#example "Direct link to Example")

    import { OpenAI } from "langchain/llms/openai";const openai = new OpenAI();const response = await openai.generate(["Tell me a joke."]);

> **\_generate**(`prompts`: `string`\[\], `options`: `Omit`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>, `runManager`?: [`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

Description

`prompts`

`string`\[\]

The prompts to pass into the model.

`options`

`Omit`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>

Optional list of stop words to use when generating.

`runManager?`

[`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)

Optional callback manager to use when generating.

#### Returns[​](#returns-6 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

The full LLM output.

#### Overrides[​](#overrides-4 "Direct link to Overrides")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[\_generate](/docs/api/llms_openai/classes/OpenAI#_generate)

#### Defined in[​](#defined-in-44 "Direct link to Defined in")

[langchain/src/llms/openai.ts:536](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L536)

### \_identifyingParams()[​](#_identifyingparams "Direct link to _identifyingparams")

Get the identifying parameters of the LLM.

> **\_identifyingParams**(): `object`

#### Returns[​](#returns-7 "Direct link to Returns")

`object`

Member

Type

`model_name`

`string`

#### Inherited from[​](#inherited-from-37 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[\_identifyingParams](/docs/api/llms_openai/classes/OpenAI#_identifyingparams)

#### Defined in[​](#defined-in-45 "Direct link to Defined in")

[langchain/src/llms/openai.ts:234](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L234)

### \_llmType()[​](#_llmtype "Direct link to _llmtype")

Return the string type key uniquely identifying this class of LLM.

> **\_llmType**(): `string`

#### Returns[​](#returns-8 "Direct link to Returns")

`string`

#### Inherited from[​](#inherited-from-38 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[\_llmType](/docs/api/llms_openai/classes/OpenAI#_llmtype)

#### Defined in[​](#defined-in-46 "Direct link to Defined in")

[langchain/src/llms/openai.ts:479](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L479)

### \_modelType()[​](#_modeltype "Direct link to _modeltype")

> **\_modelType**(): `string`

#### Returns[​](#returns-9 "Direct link to Returns")

`string`

#### Inherited from[​](#inherited-from-39 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[\_modelType](/docs/api/llms_openai/classes/OpenAI#_modeltype)

#### Defined in[​](#defined-in-47 "Direct link to Defined in")

[langchain/src/llms/base.ts:304](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L304)

### call()[​](#call "Direct link to call()")

Convenience wrapper for [generate](/docs/api/llms_base/classes/BaseLLM#generate) that takes in a single string prompt and returns a single string output.

> **call**(`prompt`: `string`, `options`?: `string`\[\] | [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`prompt`

`string`

`options?`

`string`\[\] | [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-10 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[​](#inherited-from-40 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[call](/docs/api/llms_openai/classes/OpenAI#call)

#### Defined in[​](#defined-in-48 "Direct link to Defined in")

[langchain/src/llms/base.ts:249](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L249)

### completionWithRetry()[​](#completionwithretry "Direct link to completionWithRetry()")

> **completionWithRetry**(`request`: `CreateCompletionRequest`, `options`?: `StreamingAxiosConfiguration`): `Promise`<`CreateCompletionResponse`\>

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`request`

`CreateCompletionRequest`

`options?`

`StreamingAxiosConfiguration`

#### Returns[​](#returns-11 "Direct link to Returns")

`Promise`<`CreateCompletionResponse`\>

#### Overrides[​](#overrides-5 "Direct link to Overrides")

OpenAI.completionWithRetry

#### Defined in[​](#defined-in-49 "Direct link to Defined in")

[langchain/src/llms/openai.ts:523](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L523)

### generate()[​](#generate "Direct link to generate()")

Run the LLM on the given propmts an input, handling caching.

> **generate**(`prompts`: `string`\[\], `options`?: `string`\[\] | [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[​](#parameters-5 "Direct link to Parameters")

Parameter

Type

`prompts`

`string`\[\]

`options?`

`string`\[\] | [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-12 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[​](#inherited-from-41 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[generate](/docs/api/llms_openai/classes/OpenAI#generate)

#### Defined in[​](#defined-in-50 "Direct link to Defined in")

[langchain/src/llms/base.ts:177](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L177)

### generatePrompt()[​](#generateprompt "Direct link to generatePrompt()")

> **generatePrompt**(`promptValues`: [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\[\], `options`?: `string`\[\] | [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[​](#parameters-6 "Direct link to Parameters")

Parameter

Type

`promptValues`

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\[\]

`options?`

`string`\[\] | [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-13 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[​](#inherited-from-42 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[generatePrompt](/docs/api/llms_openai/classes/OpenAI#generateprompt)

#### Defined in[​](#defined-in-51 "Direct link to Defined in")

[langchain/src/llms/base.ts:66](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L66)

### getNumTokens()[​](#getnumtokens "Direct link to getNumTokens()")

> **getNumTokens**(`text`: `string`): `Promise`<`number`\>

#### Parameters[​](#parameters-7 "Direct link to Parameters")

Parameter

Type

`text`

`string`

#### Returns[​](#returns-14 "Direct link to Returns")

`Promise`<`number`\>

#### Inherited from[​](#inherited-from-43 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[getNumTokens](/docs/api/llms_openai/classes/OpenAI#getnumtokens)

#### Defined in[​](#defined-in-52 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:154](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L154)

### identifyingParams()[​](#identifyingparams "Direct link to identifyingParams()")

Get the identifying parameters for the model

> **identifyingParams**(): `object`

#### Returns[​](#returns-15 "Direct link to Returns")

`object`

Member

Type

`model_name`

`string`

#### Inherited from[​](#inherited-from-44 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[identifyingParams](/docs/api/llms_openai/classes/OpenAI#identifyingparams)

#### Defined in[​](#defined-in-53 "Direct link to Defined in")

[langchain/src/llms/openai.ts:245](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L245)

### invocationParams()[​](#invocationparams "Direct link to invocationParams()")

Get the parameters used to invoke the model

> **invocationParams**(`options`?: `Omit`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>): `CreateCompletionRequest`

#### Parameters[​](#parameters-8 "Direct link to Parameters")

Parameter

Type

`options?`

`Omit`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions), "callbacks" | "metadata" | "tags" | "timeout"\>

#### Returns[​](#returns-16 "Direct link to Returns")

`CreateCompletionRequest`

#### Inherited from[​](#inherited-from-45 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[invocationParams](/docs/api/llms_openai/classes/OpenAI#invocationparams)

#### Defined in[​](#defined-in-54 "Direct link to Defined in")

[langchain/src/llms/openai.ts:215](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai.ts#L215)

### predict()[​](#predict "Direct link to predict()")

> **predict**(`text`: `string`, `options`?: `string`\[\] | [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\>

#### Parameters[​](#parameters-9 "Direct link to Parameters")

Parameter

Type

`text`

`string`

`options?`

`string`\[\] | [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-17 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[​](#inherited-from-46 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[predict](/docs/api/llms_openai/classes/OpenAI#predict)

#### Defined in[​](#defined-in-55 "Direct link to Defined in")

[langchain/src/llms/base.ts:262](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L262)

### predictMessages()[​](#predictmessages "Direct link to predictMessages()")

> **predictMessages**(`messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\], `options`?: `string`\[\] | [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Parameters[​](#parameters-10 "Direct link to Parameters")

Parameter

Type

`messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]

`options?`

`string`\[\] | [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-18 "Direct link to Returns")

`Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Inherited from[​](#inherited-from-47 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[predictMessages](/docs/api/llms_openai/classes/OpenAI#predictmessages)

#### Defined in[​](#defined-in-56 "Direct link to Defined in")

[langchain/src/llms/base.ts:270](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L270)

### serialize()[​](#serialize "Direct link to serialize()")

Return a json-like object representing this LLM.

> **serialize**(): [`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Returns[​](#returns-19 "Direct link to Returns")

[`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Inherited from[​](#inherited-from-48 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[serialize](/docs/api/llms_openai/classes/OpenAI#serialize)

#### Defined in[​](#defined-in-57 "Direct link to Defined in")

[langchain/src/llms/base.ts:296](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L296)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-20 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-49 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[toJSON](/docs/api/llms_openai/classes/OpenAI#tojson)

#### Defined in[​](#defined-in-58 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-21 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-50 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[toJSONNotImplemented](/docs/api/llms_openai/classes/OpenAI#tojsonnotimplemented)

#### Defined in[​](#defined-in-59 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)

### deserialize()[​](#deserialize "Direct link to deserialize()")

Load an LLM from a json-like object describing it.

> `Static` **deserialize**(`data`: [`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)): `Promise`<[`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)\>

#### Parameters[​](#parameters-11 "Direct link to Parameters")

Parameter

Type

`data`

[`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Returns[​](#returns-22 "Direct link to Returns")

`Promise`<[`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)\>

#### Inherited from[​](#inherited-from-51 "Direct link to Inherited from")

[OpenAI](/docs/api/llms_openai/classes/OpenAI).[deserialize](/docs/api/llms_openai/classes/OpenAI#deserialize)

#### Defined in[​](#defined-in-60 "Direct link to Defined in")

[langchain/src/llms/base.ts:311](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L311)