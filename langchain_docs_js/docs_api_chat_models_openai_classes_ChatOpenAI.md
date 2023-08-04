ChatOpenAI
==========

Wrapper around OpenAI large language models that use the Chat endpoint.

To use you should have the `openai` package installed, with the `OPENAI_API_KEY` environment variable set.

To use with Azure you should have the `openai` package installed, with the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_API_INSTANCE_NAME`, `AZURE_OPENAI_API_DEPLOYMENT_NAME` and `AZURE_OPENAI_API_VERSION` environment variable set. `AZURE_OPENAI_BASE_PATH` is optional and will override `AZURE_OPENAI_API_INSTANCE_NAME` if you need to use a custom endpoint.

Remarks[](#remarks "Direct link to Remarks")
---------------------------------------------

Any parameters that are valid to be passed to [`openai.createChatCompletion`](https://platform.openai.com/docs/api-reference/chat/create) can be passed through [modelKwargs](/docs/api/chat_models_openai/classes/ChatOpenAI#modelkwargs), even if not explicitly available on this class.

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseChatModel`](/docs/api/chat_models_base/classes/BaseChatModel)<[`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)\>.**ChatOpenAI**

Implements[](#implements "Direct link to Implements")
------------------------------------------------------

*   [`OpenAIChatInput`](/docs/api/chat_models_openai/interfaces/OpenAIChatInput)
*   [`AzureOpenAIInput`](/docs/api/llms_openai/interfaces/AzureOpenAIInput)

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new ChatOpenAI**(`fields`?: `Partial`<[`OpenAIChatInput`](/docs/api/chat_models_openai/interfaces/OpenAIChatInput)\> & `Partial`<[`AzureOpenAIInput`](/docs/api/llms_openai/interfaces/AzureOpenAIInput)\> & [`BaseLanguageModelParams`](/docs/api/base_language/interfaces/BaseLanguageModelParams) & {`configuration`?: `ConfigurationParameters`;}, `configuration`?: `ConfigurationParameters`): [`ChatOpenAI`](/docs/api/chat_models_openai/classes/ChatOpenAI)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

Description

`fields?`

`Partial`<[`OpenAIChatInput`](/docs/api/chat_models_openai/interfaces/OpenAIChatInput)\> & `Partial`<[`AzureOpenAIInput`](/docs/api/llms_openai/interfaces/AzureOpenAIInput)\> & [`BaseLanguageModelParams`](/docs/api/base_language/interfaces/BaseLanguageModelParams) & {`configuration`?: `ConfigurationParameters`;}

\-

`configuration?`

`ConfigurationParameters`

`Deprecated`  
  

#### Returns[](#returns "Direct link to Returns")

[`ChatOpenAI`](/docs/api/chat_models_openai/classes/ChatOpenAI)

#### Overrides[](#overrides "Direct link to Overrides")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[constructor](/docs/api/chat_models_base/classes/BaseChatModel#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:244](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L244)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### CallOptions[](#calloptions "Direct link to CallOptions")

> **CallOptions**: [`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[CallOptions](/docs/api/chat_models_base/classes/BaseChatModel#calloptions)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:110](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L110) [langchain/src/base\_language/index.ts:115](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L115)

### ParsedCallOptions[](#parsedcalloptions "Direct link to ParsedCallOptions")

> **ParsedCallOptions**: `Omit`<[`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions), `never`\>

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[ParsedCallOptions](/docs/api/chat_models_base/classes/BaseChatModel#parsedcalloptions)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:55](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/base.ts#L55)

### caller[](#caller "Direct link to caller")

> **caller**: `AsyncCaller`

The async caller should be used by subclasses to make any async calls, which will thus benefit from the concurrency and retry logic.

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[caller](/docs/api/chat_models_base/classes/BaseChatModel#caller)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:128](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L128)

### frequencyPenalty[](#frequencypenalty "Direct link to frequencyPenalty")

> **frequencyPenalty**: `number` = `0`

Penalizes repeated tokens according to frequency

#### Implementation of[](#implementation-of "Direct link to Implementation of")

[OpenAIChatInput](/docs/api/chat_models_openai/interfaces/OpenAIChatInput).[frequencyPenalty](/docs/api/chat_models_openai/interfaces/OpenAIChatInput#frequencypenalty)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:208](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L208)

### lc\_kwargs[](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[lc\_kwargs](/docs/api/chat_models_base/classes/BaseChatModel#lc_kwargs)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L57)

### lc\_namespace[](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[lc\_namespace](/docs/api/chat_models_base/classes/BaseChatModel#lc_namespace)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:60](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/base.ts#L60)

### lc\_serializable[](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `true`

#### Overrides[](#overrides-1 "Direct link to Overrides")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[lc\_serializable](/docs/api/chat_models_base/classes/BaseChatModel#lc_serializable)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:184](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L184)

### modelName[](#modelname "Direct link to modelName")

> **modelName**: `string` = `"gpt-3.5-turbo"`

Model name to use

#### Implementation of[](#implementation-of-1 "Direct link to Implementation of")

[OpenAIChatInput](/docs/api/chat_models_openai/interfaces/OpenAIChatInput).[modelName](/docs/api/chat_models_openai/interfaces/OpenAIChatInput#modelname)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:216](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L216)

### n[](#n "Direct link to n")

> **n**: `number` = `1`

Number of completions to generate for each prompt

#### Implementation of[](#implementation-of-2 "Direct link to Implementation of")

[OpenAIChatInput](/docs/api/chat_models_openai/interfaces/OpenAIChatInput).[n](/docs/api/chat_models_openai/interfaces/OpenAIChatInput#n)

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:212](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L212)

### presencePenalty[](#presencepenalty "Direct link to presencePenalty")

> **presencePenalty**: `number` = `0`

Penalizes repeated tokens

#### Implementation of[](#implementation-of-3 "Direct link to Implementation of")

[OpenAIChatInput](/docs/api/chat_models_openai/interfaces/OpenAIChatInput).[presencePenalty](/docs/api/chat_models_openai/interfaces/OpenAIChatInput#presencepenalty)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:210](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L210)

### streaming[](#streaming "Direct link to streaming")

> **streaming**: `boolean` = `false`

Whether to stream the results or not. Enabling disables tokenUsage reporting

#### Implementation of[](#implementation-of-4 "Direct link to Implementation of")

[OpenAIChatInput](/docs/api/chat_models_openai/interfaces/OpenAIChatInput).[streaming](/docs/api/chat_models_openai/interfaces/OpenAIChatInput#streaming)

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:224](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L224)

### temperature[](#temperature "Direct link to temperature")

> **temperature**: `number` = `1`

Sampling temperature to use

#### Implementation of[](#implementation-of-5 "Direct link to Implementation of")

[OpenAIChatInput](/docs/api/chat_models_openai/interfaces/OpenAIChatInput).[temperature](/docs/api/chat_models_openai/interfaces/OpenAIChatInput#temperature)

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:204](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L204)

### topP[](#topp "Direct link to topP")

> **topP**: `number` = `1`

Total probability mass of tokens to consider at each step

#### Implementation of[](#implementation-of-6 "Direct link to Implementation of")

[OpenAIChatInput](/docs/api/chat_models_openai/interfaces/OpenAIChatInput).[topP](/docs/api/chat_models_openai/interfaces/OpenAIChatInput#topp)

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:206](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L206)

### verbose[](#verbose "Direct link to verbose")

> **verbose**: `boolean`

Whether to print out response text.

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[verbose](/docs/api/chat_models_base/classes/BaseChatModel#verbose)

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:44](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L44)

### azureOpenAIApiDeploymentName?[](#azureopenaiapideploymentname "Direct link to azureOpenAIApiDeploymentName?")

> **azureOpenAIApiDeploymentName**: `string`

Azure OpenAI API deployment name to use for completions when making requests to Azure OpenAI. This is the name of the deployment you created in the Azure portal. e.g. "my-openai-deployment" this will be used in the endpoint URL: https://{InstanceName}.openai.azure.com/openai/deployments/my-openai-deployment/

#### Implementation of[](#implementation-of-7 "Direct link to Implementation of")

[AzureOpenAIInput](/docs/api/llms_openai/interfaces/AzureOpenAIInput).[azureOpenAIApiDeploymentName](/docs/api/llms_openai/interfaces/AzureOpenAIInput#azureopenaiapideploymentname)

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:236](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L236)

### azureOpenAIApiInstanceName?[](#azureopenaiapiinstancename "Direct link to azureOpenAIApiInstanceName?")

> **azureOpenAIApiInstanceName**: `string`

Azure OpenAI API instance name to use when making requests to Azure OpenAI. this is the name of the instance you created in the Azure portal. e.g. "my-openai-instance" this will be used in the endpoint URL: [https://my-openai-instance.openai.azure.com/openai/deployments/{DeploymentName}/](https://my-openai-instance.openai.azure.com/openai/deployments/%7BDeploymentName%7D/)

#### Implementation of[](#implementation-of-8 "Direct link to Implementation of")

[AzureOpenAIInput](/docs/api/llms_openai/interfaces/AzureOpenAIInput).[azureOpenAIApiInstanceName](/docs/api/llms_openai/interfaces/AzureOpenAIInput#azureopenaiapiinstancename)

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:234](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L234)

### azureOpenAIApiKey?[](#azureopenaiapikey "Direct link to azureOpenAIApiKey?")

> **azureOpenAIApiKey**: `string`

API key to use when making requests to Azure OpenAI.

#### Implementation of[](#implementation-of-9 "Direct link to Implementation of")

[AzureOpenAIInput](/docs/api/llms_openai/interfaces/AzureOpenAIInput).[azureOpenAIApiKey](/docs/api/llms_openai/interfaces/AzureOpenAIInput#azureopenaiapikey)

#### Defined in[](#defined-in-17 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:232](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L232)

### azureOpenAIApiVersion?[](#azureopenaiapiversion "Direct link to azureOpenAIApiVersion?")

> **azureOpenAIApiVersion**: `string`

API version to use when making requests to Azure OpenAI.

#### Implementation of[](#implementation-of-10 "Direct link to Implementation of")

[AzureOpenAIInput](/docs/api/llms_openai/interfaces/AzureOpenAIInput).[azureOpenAIApiVersion](/docs/api/llms_openai/interfaces/AzureOpenAIInput#azureopenaiapiversion)

#### Defined in[](#defined-in-18 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:230](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L230)

### azureOpenAIBasePath?[](#azureopenaibasepath "Direct link to azureOpenAIBasePath?")

> **azureOpenAIBasePath**: `string`

Custom endpoint for Azure OpenAI API. This is useful in case you have a deployment in another region. e.g. setting this value to "[https://westeurope.api.cognitive.microsoft.com/openai/deployments"](https://westeurope.api.cognitive.microsoft.com/openai/deployments%22) will be result in the endpoint URL: [https://westeurope.api.cognitive.microsoft.com/openai/deployments/{DeploymentName}/](https://westeurope.api.cognitive.microsoft.com/openai/deployments/%7BDeploymentName%7D/)

#### Implementation of[](#implementation-of-11 "Direct link to Implementation of")

[AzureOpenAIInput](/docs/api/llms_openai/interfaces/AzureOpenAIInput).[azureOpenAIBasePath](/docs/api/llms_openai/interfaces/AzureOpenAIInput#azureopenaibasepath)

#### Defined in[](#defined-in-19 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:238](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L238)

### callbacks?[](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[callbacks](/docs/api/chat_models_base/classes/BaseChatModel#callbacks)

#### Defined in[](#defined-in-20 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L46)

### logitBias?[](#logitbias "Direct link to logitBias?")

> **logitBias**: `Record`<`string`, `number`\>

Dictionary used to adjust the probability of specific tokens being generated

#### Implementation of[](#implementation-of-12 "Direct link to Implementation of")

[OpenAIChatInput](/docs/api/chat_models_openai/interfaces/OpenAIChatInput).[logitBias](/docs/api/chat_models_openai/interfaces/OpenAIChatInput#logitbias)

#### Defined in[](#defined-in-21 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:214](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L214)

### maxTokens?[](#maxtokens "Direct link to maxTokens?")

> **maxTokens**: `number`

Maximum number of tokens to generate in the completion. -1 returns as many tokens as possible given the prompt and the model's maximum context size.

#### Implementation of[](#implementation-of-13 "Direct link to Implementation of")

[OpenAIChatInput](/docs/api/chat_models_openai/interfaces/OpenAIChatInput).[maxTokens](/docs/api/chat_models_openai/interfaces/OpenAIChatInput#maxtokens)

#### Defined in[](#defined-in-22 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:226](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L226)

### metadata?[](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[metadata](/docs/api/chat_models_base/classes/BaseChatModel#metadata)

#### Defined in[](#defined-in-23 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:50](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L50)

### modelKwargs?[](#modelkwargs "Direct link to modelKwargs?")

> **modelKwargs**: `Record`<`string`, `any`\>

Holds any additional parameters that are valid to pass to [`openai.createCompletion`](https://platform.openai.com/docs/api-reference/completions/create) that are not explicitly specified on this class.

#### Implementation of[](#implementation-of-14 "Direct link to Implementation of")

[OpenAIChatInput](/docs/api/chat_models_openai/interfaces/OpenAIChatInput).[modelKwargs](/docs/api/chat_models_openai/interfaces/OpenAIChatInput#modelkwargs)

#### Defined in[](#defined-in-24 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:218](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L218)

### openAIApiKey?[](#openaiapikey "Direct link to openAIApiKey?")

> **openAIApiKey**: `string`

API key to use when making requests to OpenAI. Defaults to the value of `OPENAI_API_KEY` environment variable.

#### Implementation of[](#implementation-of-15 "Direct link to Implementation of")

[OpenAIChatInput](/docs/api/chat_models_openai/interfaces/OpenAIChatInput).[openAIApiKey](/docs/api/chat_models_openai/interfaces/OpenAIChatInput#openaiapikey)

#### Defined in[](#defined-in-25 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:228](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L228)

### stop?[](#stop "Direct link to stop?")

> **stop**: `string`\[\]

List of stop words to use when generating

#### Implementation of[](#implementation-of-16 "Direct link to Implementation of")

[OpenAIChatInput](/docs/api/chat_models_openai/interfaces/OpenAIChatInput).[stop](/docs/api/chat_models_openai/interfaces/OpenAIChatInput#stop)

#### Defined in[](#defined-in-26 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:220](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L220)

### tags?[](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[tags](/docs/api/chat_models_base/classes/BaseChatModel#tags)

#### Defined in[](#defined-in-27 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L48)

### timeout?[](#timeout "Direct link to timeout?")

> **timeout**: `number`

Timeout to use when making requests to OpenAI.

#### Implementation of[](#implementation-of-17 "Direct link to Implementation of")

[OpenAIChatInput](/docs/api/chat_models_openai/interfaces/OpenAIChatInput).[timeout](/docs/api/chat_models_openai/interfaces/OpenAIChatInput#timeout)

#### Defined in[](#defined-in-28 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:222](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L222)

### lc\_runnable[](#lc_runnable "Direct link to lc_runnable")

> `Protected` **lc\_runnable**: `boolean` = `true`

#### Inherited from[](#inherited-from-9 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[lc\_runnable](/docs/api/chat_models_base/classes/BaseChatModel#lc_runnable)

#### Defined in[](#defined-in-29 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:34](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L34)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### callKeys[](#callkeys "Direct link to callKeys")

Keys that the language model accepts as call options.

> **callKeys**(): _keyof_ [`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)\[\]

#### Returns[](#returns-1 "Direct link to Returns")

_keyof_ [`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)\[\]

#### Overrides[](#overrides-2 "Direct link to Overrides")

BaseChatModel.callKeys

#### Defined in[](#defined-in-30 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:173](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L173)

#### Overrides[](#overrides-3 "Direct link to Overrides")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[callKeys](/docs/api/chat_models_base/classes/BaseChatModel#callkeys)

#### Defined in[](#defined-in-31 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:173](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L173)

### lc\_aliases[](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `Record`<`string`, `string`\>

#### Returns[](#returns-2 "Direct link to Returns")

`Record`<`string`, `string`\>

#### Overrides[](#overrides-4 "Direct link to Overrides")

BaseChatModel.lc\_aliases

#### Defined in[](#defined-in-32 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:193](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L193)

#### Overrides[](#overrides-5 "Direct link to Overrides")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[lc\_aliases](/docs/api/chat_models_base/classes/BaseChatModel#lc_aliases)

#### Defined in[](#defined-in-33 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:193](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L193)

### lc\_attributes[](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-10 "Direct link to Inherited from")

BaseChatModel.lc\_attributes

#### Defined in[](#defined-in-34 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:52](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L52)

#### Inherited from[](#inherited-from-11 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[lc\_attributes](/docs/api/chat_models_base/classes/BaseChatModel#lc_attributes)

#### Defined in[](#defined-in-35 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:52](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L52)

### lc\_secrets[](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[](#returns-4 "Direct link to Returns")

`undefined` | {}

#### Overrides[](#overrides-6 "Direct link to Overrides")

BaseChatModel.lc\_secrets

#### Defined in[](#defined-in-36 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:186](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L186)

#### Overrides[](#overrides-7 "Direct link to Overrides")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[lc\_secrets](/docs/api/chat_models_base/classes/BaseChatModel#lc_secrets)

#### Defined in[](#defined-in-37 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:186](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L186)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### \_llmType()[](#_llmtype "Direct link to _llmtype")

> **\_llmType**(): `string`

#### Returns[](#returns-5 "Direct link to Returns")

`string`

#### Overrides[](#overrides-8 "Direct link to Overrides")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[\_llmType](/docs/api/chat_models_base/classes/BaseChatModel#_llmtype)

#### Defined in[](#defined-in-38 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:751](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L751)

### \_modelType()[](#_modeltype "Direct link to _modeltype")

> **\_modelType**(): `string`

#### Returns[](#returns-6 "Direct link to Returns")

`string`

#### Inherited from[](#inherited-from-12 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[\_modelType](/docs/api/chat_models_base/classes/BaseChatModel#_modeltype)

#### Defined in[](#defined-in-39 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:263](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/base.ts#L263)

### \_patchConfig()[](#_patchconfig "Direct link to _patchconfig")

> **\_patchConfig**(`config`: `Partial`<[`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)\> = `{}`, `callbackManager`: `undefined` | [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager) = `undefined`): `Partial`<[`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

Default value

`config`

`Partial`<[`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)\>

`{}`

`callbackManager`

`undefined` | [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

`undefined`

#### Returns[](#returns-7 "Direct link to Returns")

`Partial`<[`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)\>

#### Inherited from[](#inherited-from-13 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[\_patchConfig](/docs/api/chat_models_base/classes/BaseChatModel#_patchconfig)

#### Defined in[](#defined-in-40 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:146](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L146)

### \_streamIterator()[](#_streamiterator "Direct link to _streamiterator")

> **\_streamIterator**(`input`: [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `options`?: [`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)): `AsyncGenerator`<[`BaseMessageChunk`](/docs/api/schema/classes/BaseMessageChunk), `any`, `unknown`\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`input`

[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)

`options?`

[`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)

#### Returns[](#returns-8 "Direct link to Returns")

`AsyncGenerator`<[`BaseMessageChunk`](/docs/api/schema/classes/BaseMessageChunk), `any`, `unknown`\>

#### Inherited from[](#inherited-from-14 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[\_streamIterator](/docs/api/chat_models_base/classes/BaseChatModel#_streamiterator)

#### Defined in[](#defined-in-41 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:105](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/base.ts#L105)

### \_streamResponseChunks()[](#_streamresponsechunks "Direct link to _streamresponsechunks")

> **\_streamResponseChunks**(`messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\], `options`: `Omit`<[`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions), `never`\>, `runManager`?: [`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)): `AsyncGenerator`<[`ChatGenerationChunk`](/docs/api/schema/classes/ChatGenerationChunk), `any`, `unknown`\>

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

`messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]

`options`

`Omit`<[`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions), `never`\>

`runManager?`

[`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)

#### Returns[](#returns-9 "Direct link to Returns")

`AsyncGenerator`<[`ChatGenerationChunk`](/docs/api/schema/classes/ChatGenerationChunk), `any`, `unknown`\>

#### Overrides[](#overrides-9 "Direct link to Overrides")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[\_streamResponseChunks](/docs/api/chat_models_base/classes/BaseChatModel#_streamresponsechunks)

#### Defined in[](#defined-in-42 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:354](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L354)

### batch()[](#batch "Direct link to batch()")

> **batch**(`inputs`: [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)\[\], `options`?: `Partial`<[`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)\> | `Partial`<[`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)\>\[\], `batchOptions`?: `object`): `Promise`<[`BaseMessageChunk`](/docs/api/schema/classes/BaseMessageChunk)\[\]\>

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

`inputs`

[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)\[\]

`options?`

`Partial`<[`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)\> | `Partial`<[`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)\>\[\]

`batchOptions?`

`object`

`batchOptions.maxConcurrency?`

`number`

#### Returns[](#returns-10 "Direct link to Returns")

`Promise`<[`BaseMessageChunk`](/docs/api/schema/classes/BaseMessageChunk)\[\]\>

#### Inherited from[](#inherited-from-15 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[batch](/docs/api/chat_models_base/classes/BaseChatModel#batch)

#### Defined in[](#defined-in-43 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:63](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L63)

### bind()[](#bind "Direct link to bind()")

> **bind**(`kwargs`: `Partial`<[`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)\>): [`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), [`BaseMessageChunk`](/docs/api/schema/classes/BaseMessageChunk), [`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)\>

#### Parameters[](#parameters-5 "Direct link to Parameters")

Parameter

Type

`kwargs`

`Partial`<[`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)\>

#### Returns[](#returns-11 "Direct link to Returns")

[`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), [`BaseMessageChunk`](/docs/api/schema/classes/BaseMessageChunk), [`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)\>

#### Inherited from[](#inherited-from-16 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[bind](/docs/api/chat_models_base/classes/BaseChatModel#bind)

#### Defined in[](#defined-in-44 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:41](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L41)

### call()[](#call "Direct link to call()")

> **call**(`messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\], `options`?: `string`\[\] | [`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Parameters[](#parameters-6 "Direct link to Parameters")

Parameter

Type

`messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]

`options?`

`string`\[\] | [`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-12 "Direct link to Returns")

`Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Inherited from[](#inherited-from-17 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[call](/docs/api/chat_models_base/classes/BaseChatModel#call)

#### Defined in[](#defined-in-45 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:286](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/base.ts#L286)

### callPrompt()[](#callprompt "Direct link to callPrompt()")

> **callPrompt**(`promptValue`: [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue), `options`?: `string`\[\] | [`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Parameters[](#parameters-7 "Direct link to Parameters")

Parameter

Type

`promptValue`

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)

`options?`

`string`\[\] | [`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-13 "Direct link to Returns")

`Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Inherited from[](#inherited-from-18 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[callPrompt](/docs/api/chat_models_base/classes/BaseChatModel#callprompt)

#### Defined in[](#defined-in-46 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:296](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/base.ts#L296)

### generate()[](#generate "Direct link to generate()")

> **generate**(`messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]\[\], `options`?: `string`\[\] | [`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[](#parameters-8 "Direct link to Parameters")

Parameter

Type

`messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]\[\]

`options?`

`string`\[\] | [`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-14 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[](#inherited-from-19 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[generate](/docs/api/chat_models_base/classes/BaseChatModel#generate)

#### Defined in[](#defined-in-47 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:173](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/base.ts#L173)

### generatePrompt()[](#generateprompt "Direct link to generatePrompt()")

> **generatePrompt**(`promptValues`: [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\[\], `options`?: `string`\[\] | [`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[](#parameters-9 "Direct link to Parameters")

Parameter

Type

`promptValues`

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\[\]

`options?`

`string`\[\] | [`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-15 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[](#inherited-from-20 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[generatePrompt](/docs/api/chat_models_base/classes/BaseChatModel#generateprompt)

#### Defined in[](#defined-in-48 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:269](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/base.ts#L269)

### getNumTokens()[](#getnumtokens "Direct link to getNumTokens()")

> **getNumTokens**(`text`: `string`): `Promise`<`number`\>

#### Parameters[](#parameters-10 "Direct link to Parameters")

Parameter

Type

`text`

`string`

#### Returns[](#returns-16 "Direct link to Returns")

`Promise`<`number`\>

#### Inherited from[](#inherited-from-21 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[getNumTokens](/docs/api/chat_models_base/classes/BaseChatModel#getnumtokens)

#### Defined in[](#defined-in-49 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:166](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L166)

### getNumTokensFromMessages()[](#getnumtokensfrommessages "Direct link to getNumTokensFromMessages()")

> **getNumTokensFromMessages**(`messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]): `Promise`<{`countPerMessage`: `number`\[\]; `totalCount`: `number`;}\>

#### Parameters[](#parameters-11 "Direct link to Parameters")

Parameter

Type

`messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]

#### Returns[](#returns-17 "Direct link to Returns")

`Promise`<{`countPerMessage`: `number`\[\]; `totalCount`: `number`;}\>

#### Defined in[](#defined-in-50 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:662](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L662)

### identifyingParams()[](#identifyingparams "Direct link to identifyingParams()")

Get the identifying parameters for the model

> **identifyingParams**(): `object`

#### Returns[](#returns-18 "Direct link to Returns")

`object`

Member

Type

`model_name`

`string`

#### Defined in[](#defined-in-51 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:462](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L462)

### invocationParams()[](#invocationparams "Direct link to invocationParams()")

Get the parameters used to invoke the model

> **invocationParams**(`options`?: `Omit`<[`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions), `never`\>): `Omit`<`CreateChatCompletionRequest`, "messages"\>

#### Parameters[](#parameters-12 "Direct link to Parameters")

Parameter

Type

`options?`

`Omit`<[`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions), `never`\>

#### Returns[](#returns-19 "Direct link to Returns")

`Omit`<`CreateChatCompletionRequest`, "messages"\>

#### Overrides[](#overrides-10 "Direct link to Overrides")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[invocationParams](/docs/api/chat_models_base/classes/BaseChatModel#invocationparams)

#### Defined in[](#defined-in-52 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:319](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L319)

### invoke()[](#invoke "Direct link to invoke()")

> **invoke**(`input`: [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `options`?: [`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)): `Promise`<[`BaseMessageChunk`](/docs/api/schema/classes/BaseMessageChunk)\>

#### Parameters[](#parameters-13 "Direct link to Parameters")

Parameter

Type

`input`

[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)

`options?`

[`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)

#### Returns[](#returns-20 "Direct link to Returns")

`Promise`<[`BaseMessageChunk`](/docs/api/schema/classes/BaseMessageChunk)\>

#### Inherited from[](#inherited-from-22 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[invoke](/docs/api/chat_models_base/classes/BaseChatModel#invoke)

#### Defined in[](#defined-in-53 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:81](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/base.ts#L81)

### pipe()[](#pipe "Direct link to pipe()")

> **pipe**<NewRunOutput\>(`coerceable`: [`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<[`BaseMessageChunk`](/docs/api/schema/classes/BaseMessageChunk), `NewRunOutput`\>): [`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `NewRunOutput`\>

#### Type parameters[](#type-parameters "Direct link to Type parameters")

*   `NewRunOutput`

#### Parameters[](#parameters-14 "Direct link to Parameters")

Parameter

Type

`coerceable`

[`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<[`BaseMessageChunk`](/docs/api/schema/classes/BaseMessageChunk), `NewRunOutput`\>

#### Returns[](#returns-21 "Direct link to Returns")

[`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `NewRunOutput`\>

#### Inherited from[](#inherited-from-23 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[pipe](/docs/api/chat_models_base/classes/BaseChatModel#pipe)

#### Defined in[](#defined-in-54 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:153](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L153)

### predict()[](#predict "Direct link to predict()")

> **predict**(`text`: `string`, `options`?: `string`\[\] | [`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\>

#### Parameters[](#parameters-15 "Direct link to Parameters")

Parameter

Type

`text`

`string`

`options?`

`string`\[\] | [`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-22 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[](#inherited-from-24 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[predict](/docs/api/chat_models_base/classes/BaseChatModel#predict)

#### Defined in[](#defined-in-55 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:313](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/base.ts#L313)

### predictMessages()[](#predictmessages "Direct link to predictMessages()")

> **predictMessages**(`messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\], `options`?: `string`\[\] | [`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Parameters[](#parameters-16 "Direct link to Parameters")

Parameter

Type

`messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]

`options?`

`string`\[\] | [`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-23 "Direct link to Returns")

`Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Inherited from[](#inherited-from-25 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[predictMessages](/docs/api/chat_models_base/classes/BaseChatModel#predictmessages)

#### Defined in[](#defined-in-56 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:305](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/base.ts#L305)

### serialize()[](#serialize "Direct link to serialize()")

#### Deprecated[](#deprecated "Direct link to Deprecated")

Return a json-like object representing this LLM.

> **serialize**(): [`SerializedLLM`](/docs/api/base_language/types/SerializedLLM)

#### Returns[](#returns-24 "Direct link to Returns")

[`SerializedLLM`](/docs/api/base_language/types/SerializedLLM)

#### Inherited from[](#inherited-from-26 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[serialize](/docs/api/chat_models_base/classes/BaseChatModel#serialize)

#### Defined in[](#defined-in-57 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:216](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L216)

### startStream()[](#startstream "Direct link to startStream()")

> **startStream**(`request`: `CreateChatCompletionRequest`, `options`?: `StreamingAxiosConfiguration`): `object`

#### Parameters[](#parameters-17 "Direct link to Parameters")

Parameter

Type

`request`

`CreateChatCompletionRequest`

`options?`

`StreamingAxiosConfiguration`

#### Returns[](#returns-25 "Direct link to Returns")

`object`

Member

Type

`[asyncIterator]`

Method \[asyncIterator\]

`next`

Method next

#### Defined in[](#defined-in-58 "Direct link to Defined in")

[langchain/src/chat\_models/openai.ts:407](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/openai.ts#L407)

### stream()[](#stream "Direct link to stream()")

> **stream**(`input`: [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `options`?: `Partial`<[`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)\>): `Promise`<`IterableReadableStream`<[`BaseMessageChunk`](/docs/api/schema/classes/BaseMessageChunk)\>\>

#### Parameters[](#parameters-18 "Direct link to Parameters")

Parameter

Type

`input`

[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)

`options?`

`Partial`<[`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)\>

#### Returns[](#returns-26 "Direct link to Returns")

`Promise`<`IterableReadableStream`<[`BaseMessageChunk`](/docs/api/schema/classes/BaseMessageChunk)\>\>

#### Inherited from[](#inherited-from-27 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[stream](/docs/api/chat_models_base/classes/BaseChatModel#stream)

#### Defined in[](#defined-in-59 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:93](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L93)

### toJSON()[](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[](#returns-27 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[](#inherited-from-28 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[toJSON](/docs/api/chat_models_base/classes/BaseChatModel#tojson)

#### Defined in[](#defined-in-60 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[](#returns-28 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[](#inherited-from-29 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[toJSONNotImplemented](/docs/api/chat_models_base/classes/BaseChatModel#tojsonnotimplemented)

#### Defined in[](#defined-in-61 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L151)

### deserialize()[](#deserialize "Direct link to deserialize()")

#### Deprecated[](#deprecated-1 "Direct link to Deprecated")

Load an LLM from a json-like object describing it.

> `Static` **deserialize**(`data`: [`SerializedLLM`](/docs/api/base_language/types/SerializedLLM)): `Promise`<[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>\>

#### Parameters[](#parameters-19 "Direct link to Parameters")

Parameter

Type

`data`

[`SerializedLLM`](/docs/api/base_language/types/SerializedLLM)

#### Returns[](#returns-29 "Direct link to Returns")

`Promise`<[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>\>

#### Inherited from[](#inherited-from-30 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[deserialize](/docs/api/chat_models_base/classes/BaseChatModel#deserialize)

#### Defined in[](#defined-in-62 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:228](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L228)

### isRunnable()[](#isrunnable "Direct link to isRunnable()")

> `Static` **isRunnable**(`thing`: `any`): thing is Runnable<any, any, BaseCallbackConfig\>

#### Parameters[](#parameters-20 "Direct link to Parameters")

Parameter

Type

`thing`

`any`

#### Returns[](#returns-30 "Direct link to Returns")

thing is Runnable<any, any, BaseCallbackConfig\>

#### Inherited from[](#inherited-from-31 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[isRunnable](/docs/api/chat_models_base/classes/BaseChatModel#isrunnable)

#### Defined in[](#defined-in-63 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:164](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L164)

### \_callWithConfig()[](#_callwithconfig "Direct link to _callwithconfig")

> `Protected` **\_callWithConfig**<T\>(`func`: `Function`, `input`: `T`, `options`?: `BaseCallbackConfig` & {`runType`?: `string`;}): `Promise`<[`BaseMessageChunk`](/docs/api/schema/classes/BaseMessageChunk)\>

#### Type parameters[](#type-parameters-1 "Direct link to Type parameters")

*   `T` _extends_ [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)

#### Parameters[](#parameters-21 "Direct link to Parameters")

Parameter

Type

`func`

(`input`: `T`) => `Promise`<[`BaseMessageChunk`](/docs/api/schema/classes/BaseMessageChunk)\>

`input`

`T`

`options?`

`BaseCallbackConfig` & {`runType`?: `string`;}

#### Returns[](#returns-31 "Direct link to Returns")

`Promise`<[`BaseMessageChunk`](/docs/api/schema/classes/BaseMessageChunk)\>

#### Inherited from[](#inherited-from-32 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[\_callWithConfig](/docs/api/chat_models_base/classes/BaseChatModel#_callwithconfig)

#### Defined in[](#defined-in-64 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:117](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L117)

### \_getOptionsList()[](#_getoptionslist "Direct link to _getoptionslist")

> `Protected` **\_getOptionsList**(`options`: `Partial`<[`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)\> | `Partial`<[`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)\>\[\], `length`: `number` = `0`): `Partial`<[`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)\>\[\]

#### Parameters[](#parameters-22 "Direct link to Parameters")

Parameter

Type

Default value

`options`

`Partial`<[`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)\> | `Partial`<[`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)\>\[\]

`undefined`

`length`

`number`

`0`

#### Returns[](#returns-32 "Direct link to Returns")

`Partial`<[`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)\>\[\]

#### Inherited from[](#inherited-from-33 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[\_getOptionsList](/docs/api/chat_models_base/classes/BaseChatModel#_getoptionslist)

#### Defined in[](#defined-in-65 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L48)

### \_separateRunnableConfigFromCallOptions()[](#_separaterunnableconfigfromcalloptions "Direct link to _separaterunnableconfigfromcalloptions")

> `Protected` **\_separateRunnableConfigFromCallOptions**(`options`?: `Partial`<[`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)\>): \[`BaseCallbackConfig`, `Omit`<[`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions), `never`\>\]

#### Parameters[](#parameters-23 "Direct link to Parameters")

Parameter

Type

`options?`

`Partial`<[`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions)\>

#### Returns[](#returns-33 "Direct link to Returns")

\[`BaseCallbackConfig`, `Omit`<[`ChatOpenAICallOptions`](/docs/api/chat_models_openai/interfaces/ChatOpenAICallOptions), `never`\>\]

#### Inherited from[](#inherited-from-34 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[\_separateRunnableConfigFromCallOptions](/docs/api/chat_models_base/classes/BaseChatModel#_separaterunnableconfigfromcalloptions)

#### Defined in[](#defined-in-66 "Direct link to Defined in")

[langchain/src/chat\_models/base.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chat_models/base.ts#L70)

### \_convertInputToPromptValue()[](#_convertinputtopromptvalue "Direct link to _convertinputtopromptvalue")

> `Static` `Protected` **\_convertInputToPromptValue**(`input`: [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)): [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)

#### Parameters[](#parameters-24 "Direct link to Parameters")

Parameter

Type

`input`

[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)

#### Returns[](#returns-34 "Direct link to Returns")

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)

#### Inherited from[](#inherited-from-35 "Direct link to Inherited from")

[BaseChatModel](/docs/api/chat_models_base/classes/BaseChatModel).[\_convertInputToPromptValue](/docs/api/chat_models_base/classes/BaseChatModel#_convertinputtopromptvalue)

#### Defined in[](#defined-in-67 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:192](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L192)