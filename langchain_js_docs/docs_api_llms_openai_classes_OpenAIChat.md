OpenAIChat
==========

Wrapper around OpenAI large language models that use the Chat endpoint.

To use you should have the `openai` package installed, with the `OPENAI_API_KEY` environment variable set.

To use with Azure you should have the `openai` package installed, with the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_API_INSTANCE_NAME`, `AZURE_OPENAI_API_DEPLOYMENT_NAME` and `AZURE_OPENAI_API_VERSION` environment variable set.

Remarks[​](#remarks "Direct link to Remarks")
---------------------------------------------

Any parameters that are valid to be passed to [`openai.createCompletion`](https://platform.openai.com/docs/api-reference/chat/create) can be passed through [modelKwargs](/docs/api/llms_openai/classes/OpenAIChat#modelkwargs), even if not explicitly available on this class.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`LLM`](/docs/api/llms_base/classes/LLM).**OpenAIChat**

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   [`OpenAIChatInput`](/docs/api/chat_models_openai/interfaces/OpenAIChatInput)
*   [`AzureOpenAIInput`](/docs/api/llms_openai/interfaces/AzureOpenAIInput)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new OpenAIChat**(`fields`?: `Partial`<[`OpenAIChatInput`](/docs/api/chat_models_openai/interfaces/OpenAIChatInput)\> & `Partial`<[`AzureOpenAIInput`](/docs/api/llms_openai/interfaces/AzureOpenAIInput)\> & [`BaseLLMParams`](/docs/api/llms_base/interfaces/BaseLLMParams) & {`configuration`?: `ConfigurationParameters`;}, `configuration`?: `ConfigurationParameters`): [`OpenAIChat`](/docs/api/llms_openai/classes/OpenAIChat)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

Description

`fields?`

`Partial`<[`OpenAIChatInput`](/docs/api/chat_models_openai/interfaces/OpenAIChatInput)\> & `Partial`<[`AzureOpenAIInput`](/docs/api/llms_openai/interfaces/AzureOpenAIInput)\> & [`BaseLLMParams`](/docs/api/llms_base/interfaces/BaseLLMParams) & {`configuration`?: `ConfigurationParameters`;}

\-

`configuration?`

`ConfigurationParameters`

`Deprecated`  
  

#### Returns[​](#returns "Direct link to Returns")

[`OpenAIChat`](/docs/api/llms_openai/classes/OpenAIChat)

#### Overrides[​](#overrides "Direct link to Overrides")

[LLM](/docs/api/llms_base/classes/LLM).[constructor](/docs/api/llms_base/classes/LLM#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:128](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L128)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### CallOptions[​](#calloptions "Direct link to CallOptions")

> **CallOptions**: `OpenAIChatCallOptions`

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[LLM](/docs/api/llms_base/classes/LLM).[CallOptions](/docs/api/llms_base/classes/LLM#calloptions)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:56](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L56)

### ParsedCallOptions[​](#parsedcalloptions "Direct link to ParsedCallOptions")

> **ParsedCallOptions**: `Omit`<`OpenAIChatCallOptions`, "callbacks" | "metadata" | "tags" | "timeout"\>

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[ParsedCallOptions](/docs/api/llms_base/classes/LLM#parsedcalloptions)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/llms/base.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L46)

### caller[​](#caller "Direct link to caller")

> **caller**: `AsyncCaller`

The async caller should be used by subclasses to make any async calls, which will thus benefit from the concurrency and retry logic.

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[caller](/docs/api/llms_base/classes/LLM#caller)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:116](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L116)

### frequencyPenalty[​](#frequencypenalty "Direct link to frequencyPenalty")

> **frequencyPenalty**: `number` = `0`

Penalizes repeated tokens according to frequency

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

[OpenAIChatInput](/docs/api/chat_models_openai/interfaces/OpenAIChatInput).[frequencyPenalty](/docs/api/chat_models_openai/interfaces/OpenAIChatInput#frequencypenalty)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L90)

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_kwargs](/docs/api/llms_base/classes/LLM#lc_kwargs)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_namespace](/docs/api/llms_base/classes/LLM#lc_namespace)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/llms/base.ts:51](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L51)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `true`

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_serializable](/docs/api/llms_base/classes/LLM#lc_serializable)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:66](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L66)

### modelName[​](#modelname "Direct link to modelName")

> **modelName**: `string` = `"gpt-3.5-turbo"`

Model name to use

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

[OpenAIChatInput](/docs/api/chat_models_openai/interfaces/OpenAIChatInput).[modelName](/docs/api/chat_models_openai/interfaces/OpenAIChatInput#modelname)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:100](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L100)

### n[​](#n "Direct link to n")

> **n**: `number` = `1`

Number of completions to generate for each prompt

#### Implementation of[​](#implementation-of-2 "Direct link to Implementation of")

[OpenAIChatInput](/docs/api/chat_models_openai/interfaces/OpenAIChatInput).[n](/docs/api/chat_models_openai/interfaces/OpenAIChatInput#n)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:94](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L94)

### presencePenalty[​](#presencepenalty "Direct link to presencePenalty")

> **presencePenalty**: `number` = `0`

Penalizes repeated tokens

#### Implementation of[​](#implementation-of-3 "Direct link to Implementation of")

[OpenAIChatInput](/docs/api/chat_models_openai/interfaces/OpenAIChatInput).[presencePenalty](/docs/api/chat_models_openai/interfaces/OpenAIChatInput#presencepenalty)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:92](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L92)

### streaming[​](#streaming "Direct link to streaming")

> **streaming**: `boolean` = `false`

Whether to stream the results or not. Enabling disables tokenUsage reporting

#### Implementation of[​](#implementation-of-4 "Direct link to Implementation of")

[OpenAIChatInput](/docs/api/chat_models_openai/interfaces/OpenAIChatInput).[streaming](/docs/api/chat_models_openai/interfaces/OpenAIChatInput#streaming)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:110](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L110)

### temperature[​](#temperature "Direct link to temperature")

> **temperature**: `number` = `1`

Sampling temperature to use

#### Implementation of[​](#implementation-of-5 "Direct link to Implementation of")

[OpenAIChatInput](/docs/api/chat_models_openai/interfaces/OpenAIChatInput).[temperature](/docs/api/chat_models_openai/interfaces/OpenAIChatInput#temperature)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:86](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L86)

### topP[​](#topp "Direct link to topP")

> **topP**: `number` = `1`

Total probability mass of tokens to consider at each step

#### Implementation of[​](#implementation-of-6 "Direct link to Implementation of")

[OpenAIChatInput](/docs/api/chat_models_openai/interfaces/OpenAIChatInput).[topP](/docs/api/chat_models_openai/interfaces/OpenAIChatInput#topp)

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:88](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L88)

### verbose[​](#verbose "Direct link to verbose")

> **verbose**: `boolean`

Whether to print out response text.

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[verbose](/docs/api/llms_base/classes/LLM#verbose)

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:38](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L38)

### azureOpenAIApiDeploymentName?[​](#azureopenaiapideploymentname "Direct link to azureOpenAIApiDeploymentName?")

> **azureOpenAIApiDeploymentName**: `string`

Azure OpenAI API deployment name to use for completions when making requests to Azure OpenAI. This is the name of the deployment you created in the Azure portal. e.g. "my-openai-deployment" this will be used in the endpoint URL: https://{InstanceName}.openai.azure.com/openai/deployments/my-openai-deployment/

#### Implementation of[​](#implementation-of-7 "Direct link to Implementation of")

[AzureOpenAIInput](/docs/api/llms_openai/interfaces/AzureOpenAIInput).[azureOpenAIApiDeploymentName](/docs/api/llms_openai/interfaces/AzureOpenAIInput#azureopenaiapideploymentname)

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:120](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L120)

### azureOpenAIApiInstanceName?[​](#azureopenaiapiinstancename "Direct link to azureOpenAIApiInstanceName?")

> **azureOpenAIApiInstanceName**: `string`

Azure OpenAI API instance name to use when making requests to Azure OpenAI. this is the name of the instance you created in the Azure portal. e.g. "my-openai-instance" this will be used in the endpoint URL: [https://my-openai-instance.openai.azure.com/openai/deployments/{DeploymentName}/](https://my-openai-instance.openai.azure.com/openai/deployments/%7BDeploymentName%7D/)

#### Implementation of[​](#implementation-of-8 "Direct link to Implementation of")

[AzureOpenAIInput](/docs/api/llms_openai/interfaces/AzureOpenAIInput).[azureOpenAIApiInstanceName](/docs/api/llms_openai/interfaces/AzureOpenAIInput#azureopenaiapiinstancename)

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:118](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L118)

### azureOpenAIApiKey?[​](#azureopenaiapikey "Direct link to azureOpenAIApiKey?")

> **azureOpenAIApiKey**: `string`

API key to use when making requests to Azure OpenAI.

#### Implementation of[​](#implementation-of-9 "Direct link to Implementation of")

[AzureOpenAIInput](/docs/api/llms_openai/interfaces/AzureOpenAIInput).[azureOpenAIApiKey](/docs/api/llms_openai/interfaces/AzureOpenAIInput#azureopenaiapikey)

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:116](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L116)

### azureOpenAIApiVersion?[​](#azureopenaiapiversion "Direct link to azureOpenAIApiVersion?")

> **azureOpenAIApiVersion**: `string`

API version to use when making requests to Azure OpenAI.

#### Implementation of[​](#implementation-of-10 "Direct link to Implementation of")

[AzureOpenAIInput](/docs/api/llms_openai/interfaces/AzureOpenAIInput).[azureOpenAIApiVersion](/docs/api/llms_openai/interfaces/AzureOpenAIInput#azureopenaiapiversion)

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:114](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L114)

### azureOpenAIBasePath?[​](#azureopenaibasepath "Direct link to azureOpenAIBasePath?")

> **azureOpenAIBasePath**: `string`

Custom endpoint for Azure OpenAI API. This is useful in case you have a deployment in another region. e.g. setting this value to "[https://westeurope.api.cognitive.microsoft.com/openai/deployments"](https://westeurope.api.cognitive.microsoft.com/openai/deployments%22) will be result in the endpoint URL: [https://westeurope.api.cognitive.microsoft.com/openai/deployments/{DeploymentName}/](https://westeurope.api.cognitive.microsoft.com/openai/deployments/%7BDeploymentName%7D/)

#### Implementation of[​](#implementation-of-11 "Direct link to Implementation of")

[AzureOpenAIInput](/docs/api/llms_openai/interfaces/AzureOpenAIInput).[azureOpenAIBasePath](/docs/api/llms_openai/interfaces/AzureOpenAIInput#azureopenaibasepath)

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:122](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L122)

### cache?[​](#cache "Direct link to cache?")

> **cache**: [`BaseCache`](/docs/api/schema/classes/BaseCache)<[`Generation`](/docs/api/schema/interfaces/Generation)\[\]\>

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[cache](/docs/api/llms_base/classes/LLM#cache)

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/llms/base.ts:53](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L53)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[callbacks](/docs/api/llms_base/classes/LLM#callbacks)

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L40)

### logitBias?[​](#logitbias "Direct link to logitBias?")

> **logitBias**: `Record`<`string`, `number`\>

Dictionary used to adjust the probability of specific tokens being generated

#### Implementation of[​](#implementation-of-12 "Direct link to Implementation of")

[OpenAIChatInput](/docs/api/chat_models_openai/interfaces/OpenAIChatInput).[logitBias](/docs/api/chat_models_openai/interfaces/OpenAIChatInput#logitbias)

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:96](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L96)

### maxTokens?[​](#maxtokens "Direct link to maxTokens?")

> **maxTokens**: `number`

Maximum number of tokens to generate in the completion. -1 returns as many tokens as possible given the prompt and the model's maximum context size.

#### Implementation of[​](#implementation-of-13 "Direct link to Implementation of")

[OpenAIChatInput](/docs/api/chat_models_openai/interfaces/OpenAIChatInput).[maxTokens](/docs/api/chat_models_openai/interfaces/OpenAIChatInput#maxtokens)

#### Defined in[​](#defined-in-23 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L98)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[metadata](/docs/api/llms_base/classes/LLM#metadata)

#### Defined in[​](#defined-in-24 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:44](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L44)

### modelKwargs?[​](#modelkwargs "Direct link to modelKwargs?")

> **modelKwargs**: `Record`<`string`, `any`\>

Holds any additional parameters that are valid to pass to [`openai.createCompletion`](https://platform.openai.com/docs/api-reference/completions/create) that are not explicitly specified on this class.

#### Implementation of[​](#implementation-of-14 "Direct link to Implementation of")

[OpenAIChatInput](/docs/api/chat_models_openai/interfaces/OpenAIChatInput).[modelKwargs](/docs/api/chat_models_openai/interfaces/OpenAIChatInput#modelkwargs)

#### Defined in[​](#defined-in-25 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:104](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L104)

### openAIApiKey?[​](#openaiapikey "Direct link to openAIApiKey?")

> **openAIApiKey**: `string`

API key to use when making requests to OpenAI. Defaults to the value of `OPENAI_API_KEY` environment variable.

#### Implementation of[​](#implementation-of-15 "Direct link to Implementation of")

[OpenAIChatInput](/docs/api/chat_models_openai/interfaces/OpenAIChatInput).[openAIApiKey](/docs/api/chat_models_openai/interfaces/OpenAIChatInput#openaiapikey)

#### Defined in[​](#defined-in-26 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:112](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L112)

### prefixMessages?[​](#prefixmessages "Direct link to prefixMessages?")

> **prefixMessages**: `ChatCompletionRequestMessage`\[\]

ChatGPT messages to pass as a prefix to the prompt

#### Implementation of[​](#implementation-of-16 "Direct link to Implementation of")

[OpenAIChatInput](/docs/api/chat_models_openai/interfaces/OpenAIChatInput).[prefixMessages](/docs/api/chat_models_openai/interfaces/OpenAIChatInput#prefixmessages)

#### Defined in[​](#defined-in-27 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:102](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L102)

### stop?[​](#stop "Direct link to stop?")

> **stop**: `string`\[\]

List of stop words to use when generating

#### Implementation of[​](#implementation-of-17 "Direct link to Implementation of")

[OpenAIChatInput](/docs/api/chat_models_openai/interfaces/OpenAIChatInput).[stop](/docs/api/chat_models_openai/interfaces/OpenAIChatInput#stop)

#### Defined in[​](#defined-in-28 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:108](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L108)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[tags](/docs/api/llms_base/classes/LLM#tags)

#### Defined in[​](#defined-in-29 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L42)

### timeout?[​](#timeout "Direct link to timeout?")

> **timeout**: `number`

Timeout to use when making requests to OpenAI.

#### Implementation of[​](#implementation-of-18 "Direct link to Implementation of")

[OpenAIChatInput](/docs/api/chat_models_openai/interfaces/OpenAIChatInput).[timeout](/docs/api/chat_models_openai/interfaces/OpenAIChatInput#timeout)

#### Defined in[​](#defined-in-30 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:106](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L106)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### callKeys[​](#callkeys "Direct link to callKeys")

Keys that the language model accepts as call options.

> **callKeys**(): _keyof_ `OpenAIChatCallOptions`\[\]

#### Returns[​](#returns-1 "Direct link to Returns")

_keyof_ `OpenAIChatCallOptions`\[\]

#### Overrides[​](#overrides-3 "Direct link to Overrides")

LLM.callKeys

#### Defined in[​](#defined-in-31 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:58](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L58)

#### Overrides[​](#overrides-4 "Direct link to Overrides")

[LLM](/docs/api/llms_base/classes/LLM).[callKeys](/docs/api/llms_base/classes/LLM#callkeys)

#### Defined in[​](#defined-in-32 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:58](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L58)

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `Record`<`string`, `string`\>

#### Returns[​](#returns-2 "Direct link to Returns")

`Record`<`string`, `string`\>

#### Overrides[​](#overrides-5 "Direct link to Overrides")

LLM.lc\_aliases

#### Defined in[​](#defined-in-33 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:75](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L75)

#### Overrides[​](#overrides-6 "Direct link to Overrides")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_aliases](/docs/api/llms_base/classes/LLM#lc_aliases)

#### Defined in[​](#defined-in-34 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:75](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L75)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

LLM.lc\_attributes

#### Defined in[​](#defined-in-35 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_attributes](/docs/api/llms_base/classes/LLM#lc_attributes)

#### Defined in[​](#defined-in-36 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-4 "Direct link to Returns")

`undefined` | {}

#### Overrides[​](#overrides-7 "Direct link to Overrides")

LLM.lc\_secrets

#### Defined in[​](#defined-in-37 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:68](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L68)

#### Overrides[​](#overrides-8 "Direct link to Overrides")

[LLM](/docs/api/llms_base/classes/LLM).[lc\_secrets](/docs/api/llms_base/classes/LLM#lc_secrets)

#### Defined in[​](#defined-in-38 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:68](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L68)

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

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[\_flattenLLMResult](/docs/api/llms_base/classes/LLM#_flattenllmresult)

#### Defined in[​](#defined-in-39 "Direct link to Defined in")

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

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[\_generate](/docs/api/llms_base/classes/LLM#_generate)

#### Defined in[​](#defined-in-40 "Direct link to Defined in")

[langchain/src/llms/base.ts:343](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L343)

### \_llmType()[​](#_llmtype "Direct link to _llmtype")

Return the string type key uniquely identifying this class of LLM.

> **\_llmType**(): `string`

#### Returns[​](#returns-7 "Direct link to Returns")

`string`

#### Overrides[​](#overrides-9 "Direct link to Overrides")

[LLM](/docs/api/llms_base/classes/LLM).[\_llmType](/docs/api/llms_base/classes/LLM#_llmtype)

#### Defined in[​](#defined-in-41 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:441](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L441)

### \_modelType()[​](#_modeltype "Direct link to _modeltype")

> **\_modelType**(): `string`

#### Returns[​](#returns-8 "Direct link to Returns")

`string`

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[\_modelType](/docs/api/llms_base/classes/LLM#_modeltype)

#### Defined in[​](#defined-in-42 "Direct link to Defined in")

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

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[call](/docs/api/llms_base/classes/LLM#call)

#### Defined in[​](#defined-in-43 "Direct link to Defined in")

[langchain/src/llms/base.ts:249](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L249)

### generate()[​](#generate "Direct link to generate()")

Run the LLM on the given propmts an input, handling caching.

> **generate**(`prompts`: `string`\[\], `options`?: `string`\[\] | `OpenAIChatCallOptions`, `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`prompts`

`string`\[\]

`options?`

`string`\[\] | `OpenAIChatCallOptions`

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-10 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[​](#inherited-from-15 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[generate](/docs/api/llms_base/classes/LLM#generate)

#### Defined in[​](#defined-in-44 "Direct link to Defined in")

[langchain/src/llms/base.ts:177](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L177)

### generatePrompt()[​](#generateprompt "Direct link to generatePrompt()")

> **generatePrompt**(`promptValues`: [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\[\], `options`?: `string`\[\] | `OpenAIChatCallOptions`, `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[​](#parameters-5 "Direct link to Parameters")

Parameter

Type

`promptValues`

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\[\]

`options?`

`string`\[\] | `OpenAIChatCallOptions`

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-11 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[​](#inherited-from-16 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[generatePrompt](/docs/api/llms_base/classes/LLM#generateprompt)

#### Defined in[​](#defined-in-45 "Direct link to Defined in")

[langchain/src/llms/base.ts:66](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L66)

### getNumTokens()[​](#getnumtokens "Direct link to getNumTokens()")

> **getNumTokens**(`text`: `string`): `Promise`<`number`\>

#### Parameters[​](#parameters-6 "Direct link to Parameters")

Parameter

Type

`text`

`string`

#### Returns[​](#returns-12 "Direct link to Returns")

`Promise`<`number`\>

#### Inherited from[​](#inherited-from-17 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[getNumTokens](/docs/api/llms_base/classes/LLM#getnumtokens)

#### Defined in[​](#defined-in-46 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:154](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L154)

### identifyingParams()[​](#identifyingparams "Direct link to identifyingParams()")

Get the identifying parameters for the model

> **identifyingParams**(): `object`

#### Returns[​](#returns-13 "Direct link to Returns")

`object`

Member

Type

`model_name`

`string`

#### Defined in[​](#defined-in-47 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:242](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L242)

### invocationParams()[​](#invocationparams "Direct link to invocationParams()")

Get the parameters used to invoke the model

> **invocationParams**(`options`?: `Omit`<`OpenAIChatCallOptions`, "callbacks" | "metadata" | "tags" | "timeout"\>): `Omit`<`CreateChatCompletionRequest`, "messages"\>

#### Parameters[​](#parameters-7 "Direct link to Parameters")

Parameter

Type

`options?`

`Omit`<`OpenAIChatCallOptions`, "callbacks" | "metadata" | "tags" | "timeout"\>

#### Returns[​](#returns-14 "Direct link to Returns")

`Omit`<`CreateChatCompletionRequest`, "messages"\>

#### Overrides[​](#overrides-10 "Direct link to Overrides")

[LLM](/docs/api/llms_base/classes/LLM).[invocationParams](/docs/api/llms_base/classes/LLM#invocationparams)

#### Defined in[​](#defined-in-48 "Direct link to Defined in")

[langchain/src/llms/openai-chat.ts:212](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/openai-chat.ts#L212)

### predict()[​](#predict "Direct link to predict()")

> **predict**(`text`: `string`, `options`?: `string`\[\] | `OpenAIChatCallOptions`, `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\>

#### Parameters[​](#parameters-8 "Direct link to Parameters")

Parameter

Type

`text`

`string`

`options?`

`string`\[\] | `OpenAIChatCallOptions`

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-15 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[​](#inherited-from-18 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[predict](/docs/api/llms_base/classes/LLM#predict)

#### Defined in[​](#defined-in-49 "Direct link to Defined in")

[langchain/src/llms/base.ts:262](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L262)

### predictMessages()[​](#predictmessages "Direct link to predictMessages()")

> **predictMessages**(`messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\], `options`?: `string`\[\] | `OpenAIChatCallOptions`, `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Parameters[​](#parameters-9 "Direct link to Parameters")

Parameter

Type

`messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]

`options?`

`string`\[\] | `OpenAIChatCallOptions`

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-16 "Direct link to Returns")

`Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Inherited from[​](#inherited-from-19 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[predictMessages](/docs/api/llms_base/classes/LLM#predictmessages)

#### Defined in[​](#defined-in-50 "Direct link to Defined in")

[langchain/src/llms/base.ts:270](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L270)

### serialize()[​](#serialize "Direct link to serialize()")

Return a json-like object representing this LLM.

> **serialize**(): [`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Returns[​](#returns-17 "Direct link to Returns")

[`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Inherited from[​](#inherited-from-20 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[serialize](/docs/api/llms_base/classes/LLM#serialize)

#### Defined in[​](#defined-in-51 "Direct link to Defined in")

[langchain/src/llms/base.ts:296](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L296)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-18 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-21 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[toJSON](/docs/api/llms_base/classes/LLM#tojson)

#### Defined in[​](#defined-in-52 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-19 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-22 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[toJSONNotImplemented](/docs/api/llms_base/classes/LLM#tojsonnotimplemented)

#### Defined in[​](#defined-in-53 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)

### deserialize()[​](#deserialize "Direct link to deserialize()")

Load an LLM from a json-like object describing it.

> `Static` **deserialize**(`data`: [`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)): `Promise`<[`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)\>

#### Parameters[​](#parameters-10 "Direct link to Parameters")

Parameter

Type

`data`

[`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Returns[​](#returns-20 "Direct link to Returns")

`Promise`<[`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)\>

#### Inherited from[​](#inherited-from-23 "Direct link to Inherited from")

[LLM](/docs/api/llms_base/classes/LLM).[deserialize](/docs/api/llms_base/classes/LLM#deserialize)

#### Defined in[​](#defined-in-54 "Direct link to Defined in")

[langchain/src/llms/base.ts:311](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/base.ts#L311)