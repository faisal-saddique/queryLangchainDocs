OpenAI
======

Wrapper around OpenAI large language models.

To use you should have the `openai` package installed, with the `OPENAI_API_KEY` environment variable set.

To use with Azure you should have the `openai` package installed, with the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_API_INSTANCE_NAME`, `AZURE_OPENAI_API_DEPLOYMENT_NAME` and `AZURE_OPENAI_API_VERSION` environment variable set.

Remarks[](#remarks "Direct link to Remarks")
---------------------------------------------

Any parameters that are valid to be passed to [`openai.createCompletion`](https://platform.openai.com/docs/api-reference/completions/create) can be passed through [modelKwargs](/docs/api/llms_openai/classes/OpenAI#modelkwargs), even if not explicitly available on this class.

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)\>.**OpenAI**

Implements[](#implements "Direct link to Implements")
------------------------------------------------------

*   [`OpenAIInput`](/docs/api/llms_openai/interfaces/OpenAIInput)
*   [`AzureOpenAIInput`](/docs/api/llms_openai/interfaces/AzureOpenAIInput)

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new OpenAI**(`fields`?: `Partial`<[`OpenAIInput`](/docs/api/llms_openai/interfaces/OpenAIInput)\> & `Partial`<[`AzureOpenAIInput`](/docs/api/llms_openai/interfaces/AzureOpenAIInput)\> & [`BaseLLMParams`](/docs/api/llms_base/interfaces/BaseLLMParams) & {`configuration`?: `ConfigurationParameters`;}, `configuration`?: `ConfigurationParameters`): [`OpenAI`](/docs/api/llms_openai/classes/OpenAI)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

Description

`fields?`

`Partial`<[`OpenAIInput`](/docs/api/llms_openai/interfaces/OpenAIInput)\> & `Partial`<[`AzureOpenAIInput`](/docs/api/llms_openai/interfaces/AzureOpenAIInput)\> & [`BaseLLMParams`](/docs/api/llms_base/interfaces/BaseLLMParams) & {`configuration`?: `ConfigurationParameters`;}

\-

`configuration?`

`ConfigurationParameters`

`Deprecated`  
  

#### Returns[](#returns "Direct link to Returns")

[`OpenAI`](/docs/api/llms_openai/classes/OpenAI)

#### Overrides[](#overrides "Direct link to Overrides")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[constructor](/docs/api/llms_base/classes/BaseLLM#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/llms/openai.ts:126](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L126)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### CallOptions[](#calloptions "Direct link to CallOptions")

> **CallOptions**: [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[CallOptions](/docs/api/llms_base/classes/BaseLLM#calloptions)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:110](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L110) [langchain/src/base\_language/index.ts:115](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L115)

### ParsedCallOptions[](#parsedcalloptions "Direct link to ParsedCallOptions")

> **ParsedCallOptions**: `Omit`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions), `never`\>

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[ParsedCallOptions](/docs/api/llms_base/classes/BaseLLM#parsedcalloptions)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/llms/base.ts:49](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L49)

### batchSize[](#batchsize "Direct link to batchSize")

> **batchSize**: `number` = `20`

Batch size to use when passing multiple documents to generate

#### Implementation of[](#implementation-of "Direct link to Implementation of")

[OpenAIInput](/docs/api/llms_openai/interfaces/OpenAIInput).[batchSize](/docs/api/llms_openai/interfaces/OpenAIInput#batchsize)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/llms/openai.ts:102](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L102)

### caller[](#caller "Direct link to caller")

> **caller**: `AsyncCaller`

The async caller should be used by subclasses to make any async calls, which will thus benefit from the concurrency and retry logic.

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[caller](/docs/api/llms_base/classes/BaseLLM#caller)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:128](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L128)

### frequencyPenalty[](#frequencypenalty "Direct link to frequencyPenalty")

> **frequencyPenalty**: `number` = `0`

Penalizes repeated tokens according to frequency

#### Implementation of[](#implementation-of-1 "Direct link to Implementation of")

[OpenAIInput](/docs/api/llms_openai/interfaces/OpenAIInput).[frequencyPenalty](/docs/api/llms_openai/interfaces/OpenAIInput#frequencypenalty)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/llms/openai.ts:88](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L88)

### lc\_kwargs[](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[lc\_kwargs](/docs/api/llms_base/classes/BaseLLM#lc_kwargs)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L57)

### lc\_namespace[](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[lc\_namespace](/docs/api/llms_base/classes/BaseLLM#lc_namespace)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/llms/base.ts:54](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L54)

### lc\_serializable[](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `true`

#### Overrides[](#overrides-1 "Direct link to Overrides")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[lc\_serializable](/docs/api/llms_base/classes/BaseLLM#lc_serializable)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/llms/openai.ts:62](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L62)

### maxTokens[](#maxtokens "Direct link to maxTokens")

> **maxTokens**: `number` = `256`

Maximum number of tokens to generate in the completion. -1 returns as many tokens as possible given the prompt and the model's maximum context size.

#### Implementation of[](#implementation-of-2 "Direct link to Implementation of")

[OpenAIInput](/docs/api/llms_openai/interfaces/OpenAIInput).[maxTokens](/docs/api/llms_openai/interfaces/OpenAIInput#maxtokens)

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/llms/openai.ts:84](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L84)

### modelName[](#modelname "Direct link to modelName")

> **modelName**: `string` = `"text-davinci-003"`

Model name to use

#### Implementation of[](#implementation-of-3 "Direct link to Implementation of")

[OpenAIInput](/docs/api/llms_openai/interfaces/OpenAIInput).[modelName](/docs/api/llms_openai/interfaces/OpenAIInput#modelname)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/llms/openai.ts:98](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L98)

### n[](#n "Direct link to n")

> **n**: `number` = `1`

Number of completions to generate for each prompt

#### Implementation of[](#implementation-of-4 "Direct link to Implementation of")

[OpenAIInput](/docs/api/llms_openai/interfaces/OpenAIInput).[n](/docs/api/llms_openai/interfaces/OpenAIInput#n)

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/llms/openai.ts:92](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L92)

### presencePenalty[](#presencepenalty "Direct link to presencePenalty")

> **presencePenalty**: `number` = `0`

Penalizes repeated tokens

#### Implementation of[](#implementation-of-5 "Direct link to Implementation of")

[OpenAIInput](/docs/api/llms_openai/interfaces/OpenAIInput).[presencePenalty](/docs/api/llms_openai/interfaces/OpenAIInput#presencepenalty)

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/llms/openai.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L90)

### streaming[](#streaming "Direct link to streaming")

> **streaming**: `boolean` = `false`

Whether to stream the results or not. Enabling disables tokenUsage reporting

#### Implementation of[](#implementation-of-6 "Direct link to Implementation of")

[OpenAIInput](/docs/api/llms_openai/interfaces/OpenAIInput).[streaming](/docs/api/llms_openai/interfaces/OpenAIInput#streaming)

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/llms/openai.ts:108](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L108)

### temperature[](#temperature "Direct link to temperature")

> **temperature**: `number` = `0.7`

Sampling temperature to use

#### Implementation of[](#implementation-of-7 "Direct link to Implementation of")

[OpenAIInput](/docs/api/llms_openai/interfaces/OpenAIInput).[temperature](/docs/api/llms_openai/interfaces/OpenAIInput#temperature)

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/llms/openai.ts:82](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L82)

### topP[](#topp "Direct link to topP")

> **topP**: `number` = `1`

Total probability mass of tokens to consider at each step

#### Implementation of[](#implementation-of-8 "Direct link to Implementation of")

[OpenAIInput](/docs/api/llms_openai/interfaces/OpenAIInput).[topP](/docs/api/llms_openai/interfaces/OpenAIInput#topp)

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/llms/openai.ts:86](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L86)

### verbose[](#verbose "Direct link to verbose")

> **verbose**: `boolean`

Whether to print out response text.

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[verbose](/docs/api/llms_base/classes/BaseLLM#verbose)

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:44](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L44)

### azureOpenAIApiDeploymentName?[](#azureopenaiapideploymentname "Direct link to azureOpenAIApiDeploymentName?")

> **azureOpenAIApiDeploymentName**: `string`

Azure OpenAI API deployment name to use for completions when making requests to Azure OpenAI. This is the name of the deployment you created in the Azure portal. e.g. "my-openai-deployment" this will be used in the endpoint URL: https://{InstanceName}.openai.azure.com/openai/deployments/my-openai-deployment/

#### Implementation of[](#implementation-of-9 "Direct link to Implementation of")

[AzureOpenAIInput](/docs/api/llms_openai/interfaces/AzureOpenAIInput).[azureOpenAIApiDeploymentName](/docs/api/llms_openai/interfaces/AzureOpenAIInput#azureopenaiapideploymentname)

#### Defined in[](#defined-in-17 "Direct link to Defined in")

[langchain/src/llms/openai.ts:118](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L118)

### azureOpenAIApiInstanceName?[](#azureopenaiapiinstancename "Direct link to azureOpenAIApiInstanceName?")

> **azureOpenAIApiInstanceName**: `string`

Azure OpenAI API instance name to use when making requests to Azure OpenAI. this is the name of the instance you created in the Azure portal. e.g. "my-openai-instance" this will be used in the endpoint URL: [https://my-openai-instance.openai.azure.com/openai/deployments/{DeploymentName}/](https://my-openai-instance.openai.azure.com/openai/deployments/%7BDeploymentName%7D/)

#### Implementation of[](#implementation-of-10 "Direct link to Implementation of")

[AzureOpenAIInput](/docs/api/llms_openai/interfaces/AzureOpenAIInput).[azureOpenAIApiInstanceName](/docs/api/llms_openai/interfaces/AzureOpenAIInput#azureopenaiapiinstancename)

#### Defined in[](#defined-in-18 "Direct link to Defined in")

[langchain/src/llms/openai.ts:116](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L116)

### azureOpenAIApiKey?[](#azureopenaiapikey "Direct link to azureOpenAIApiKey?")

> **azureOpenAIApiKey**: `string`

API key to use when making requests to Azure OpenAI.

#### Implementation of[](#implementation-of-11 "Direct link to Implementation of")

[AzureOpenAIInput](/docs/api/llms_openai/interfaces/AzureOpenAIInput).[azureOpenAIApiKey](/docs/api/llms_openai/interfaces/AzureOpenAIInput#azureopenaiapikey)

#### Defined in[](#defined-in-19 "Direct link to Defined in")

[langchain/src/llms/openai.ts:114](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L114)

### azureOpenAIApiVersion?[](#azureopenaiapiversion "Direct link to azureOpenAIApiVersion?")

> **azureOpenAIApiVersion**: `string`

API version to use when making requests to Azure OpenAI.

#### Implementation of[](#implementation-of-12 "Direct link to Implementation of")

[AzureOpenAIInput](/docs/api/llms_openai/interfaces/AzureOpenAIInput).[azureOpenAIApiVersion](/docs/api/llms_openai/interfaces/AzureOpenAIInput#azureopenaiapiversion)

#### Defined in[](#defined-in-20 "Direct link to Defined in")

[langchain/src/llms/openai.ts:112](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L112)

### azureOpenAIBasePath?[](#azureopenaibasepath "Direct link to azureOpenAIBasePath?")

> **azureOpenAIBasePath**: `string`

Custom endpoint for Azure OpenAI API. This is useful in case you have a deployment in another region. e.g. setting this value to "[https://westeurope.api.cognitive.microsoft.com/openai/deployments"](https://westeurope.api.cognitive.microsoft.com/openai/deployments%22) will be result in the endpoint URL: [https://westeurope.api.cognitive.microsoft.com/openai/deployments/{DeploymentName}/](https://westeurope.api.cognitive.microsoft.com/openai/deployments/%7BDeploymentName%7D/)

#### Implementation of[](#implementation-of-13 "Direct link to Implementation of")

[AzureOpenAIInput](/docs/api/llms_openai/interfaces/AzureOpenAIInput).[azureOpenAIBasePath](/docs/api/llms_openai/interfaces/AzureOpenAIInput#azureopenaibasepath)

#### Defined in[](#defined-in-21 "Direct link to Defined in")

[langchain/src/llms/openai.ts:120](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L120)

### bestOf?[](#bestof "Direct link to bestOf?")

> **bestOf**: `number`

Generates `bestOf` completions server side and returns the "best"

#### Implementation of[](#implementation-of-14 "Direct link to Implementation of")

[OpenAIInput](/docs/api/llms_openai/interfaces/OpenAIInput).[bestOf](/docs/api/llms_openai/interfaces/OpenAIInput#bestof)

#### Defined in[](#defined-in-22 "Direct link to Defined in")

[langchain/src/llms/openai.ts:94](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L94)

### cache?[](#cache "Direct link to cache?")

> **cache**: [`BaseCache`](/docs/api/schema/classes/BaseCache)<[`Generation`](/docs/api/schema/interfaces/Generation)\[\]\>

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[cache](/docs/api/llms_base/classes/BaseLLM#cache)

#### Defined in[](#defined-in-23 "Direct link to Defined in")

[langchain/src/llms/base.ts:56](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L56)

### callbacks?[](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[callbacks](/docs/api/llms_base/classes/BaseLLM#callbacks)

#### Defined in[](#defined-in-24 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L46)

### logitBias?[](#logitbias "Direct link to logitBias?")

> **logitBias**: `Record`<`string`, `number`\>

Dictionary used to adjust the probability of specific tokens being generated

#### Implementation of[](#implementation-of-15 "Direct link to Implementation of")

[OpenAIInput](/docs/api/llms_openai/interfaces/OpenAIInput).[logitBias](/docs/api/llms_openai/interfaces/OpenAIInput#logitbias)

#### Defined in[](#defined-in-25 "Direct link to Defined in")

[langchain/src/llms/openai.ts:96](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L96)

### metadata?[](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[metadata](/docs/api/llms_base/classes/BaseLLM#metadata)

#### Defined in[](#defined-in-26 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:50](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L50)

### modelKwargs?[](#modelkwargs "Direct link to modelKwargs?")

> **modelKwargs**: `Record`<`string`, `any`\>

Holds any additional parameters that are valid to pass to [`openai.createCompletion`](https://platform.openai.com/docs/api-reference/completions/create) that are not explicitly specified on this class.

#### Implementation of[](#implementation-of-16 "Direct link to Implementation of")

[OpenAIInput](/docs/api/llms_openai/interfaces/OpenAIInput).[modelKwargs](/docs/api/llms_openai/interfaces/OpenAIInput#modelkwargs)

#### Defined in[](#defined-in-27 "Direct link to Defined in")

[langchain/src/llms/openai.ts:100](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L100)

### openAIApiKey?[](#openaiapikey "Direct link to openAIApiKey?")

> **openAIApiKey**: `string`

API key to use when making requests to OpenAI. Defaults to the value of `OPENAI_API_KEY` environment variable.

#### Implementation of[](#implementation-of-17 "Direct link to Implementation of")

[OpenAIInput](/docs/api/llms_openai/interfaces/OpenAIInput).[openAIApiKey](/docs/api/llms_openai/interfaces/OpenAIInput#openaiapikey)

#### Defined in[](#defined-in-28 "Direct link to Defined in")

[langchain/src/llms/openai.ts:110](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L110)

### stop?[](#stop "Direct link to stop?")

> **stop**: `string`\[\]

List of stop words to use when generating

#### Implementation of[](#implementation-of-18 "Direct link to Implementation of")

[OpenAIInput](/docs/api/llms_openai/interfaces/OpenAIInput).[stop](/docs/api/llms_openai/interfaces/OpenAIInput#stop)

#### Defined in[](#defined-in-29 "Direct link to Defined in")

[langchain/src/llms/openai.ts:106](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L106)

### tags?[](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[](#inherited-from-9 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[tags](/docs/api/llms_base/classes/BaseLLM#tags)

#### Defined in[](#defined-in-30 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L48)

### timeout?[](#timeout "Direct link to timeout?")

> **timeout**: `number`

Timeout to use when making requests to OpenAI.

#### Implementation of[](#implementation-of-19 "Direct link to Implementation of")

[OpenAIInput](/docs/api/llms_openai/interfaces/OpenAIInput).[timeout](/docs/api/llms_openai/interfaces/OpenAIInput#timeout)

#### Defined in[](#defined-in-31 "Direct link to Defined in")

[langchain/src/llms/openai.ts:104](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L104)

### lc\_runnable[](#lc_runnable "Direct link to lc_runnable")

> `Protected` **lc\_runnable**: `boolean` = `true`

#### Inherited from[](#inherited-from-10 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[lc\_runnable](/docs/api/llms_base/classes/BaseLLM#lc_runnable)

#### Defined in[](#defined-in-32 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:34](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L34)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### callKeys[](#callkeys "Direct link to callKeys")

Keys that the language model accepts as call options.

> **callKeys**(): _keyof_ [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)\[\]

#### Returns[](#returns-1 "Direct link to Returns")

_keyof_ [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)\[\]

#### Overrides[](#overrides-2 "Direct link to Overrides")

BaseLLM.callKeys

#### Defined in[](#defined-in-33 "Direct link to Defined in")

[langchain/src/llms/openai.ts:58](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L58)

#### Overrides[](#overrides-3 "Direct link to Overrides")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[callKeys](/docs/api/llms_base/classes/BaseLLM#callkeys)

#### Defined in[](#defined-in-34 "Direct link to Defined in")

[langchain/src/llms/openai.ts:58](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L58)

### lc\_aliases[](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `Record`<`string`, `string`\>

#### Returns[](#returns-2 "Direct link to Returns")

`Record`<`string`, `string`\>

#### Overrides[](#overrides-4 "Direct link to Overrides")

BaseLLM.lc\_aliases

#### Defined in[](#defined-in-35 "Direct link to Defined in")

[langchain/src/llms/openai.ts:71](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L71)

#### Overrides[](#overrides-5 "Direct link to Overrides")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[lc\_aliases](/docs/api/llms_base/classes/BaseLLM#lc_aliases)

#### Defined in[](#defined-in-36 "Direct link to Defined in")

[langchain/src/llms/openai.ts:71](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L71)

### lc\_attributes[](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-11 "Direct link to Inherited from")

BaseLLM.lc\_attributes

#### Defined in[](#defined-in-37 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:52](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L52)

#### Inherited from[](#inherited-from-12 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[lc\_attributes](/docs/api/llms_base/classes/BaseLLM#lc_attributes)

#### Defined in[](#defined-in-38 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:52](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L52)

### lc\_secrets[](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[](#returns-4 "Direct link to Returns")

`undefined` | {}

#### Overrides[](#overrides-6 "Direct link to Overrides")

BaseLLM.lc\_secrets

#### Defined in[](#defined-in-39 "Direct link to Defined in")

[langchain/src/llms/openai.ts:64](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L64)

#### Overrides[](#overrides-7 "Direct link to Overrides")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[lc\_secrets](/docs/api/llms_base/classes/BaseLLM#lc_secrets)

#### Defined in[](#defined-in-40 "Direct link to Defined in")

[langchain/src/llms/openai.ts:64](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L64)

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

#### Inherited from[](#inherited-from-13 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[\_flattenLLMResult](/docs/api/llms_base/classes/BaseLLM#_flattenllmresult)

#### Defined in[](#defined-in-41 "Direct link to Defined in")

[langchain/src/llms/base.ts:197](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L197)

### \_generate()[](#_generate "Direct link to _generate")

Call out to OpenAI's endpoint with k unique prompts

#### Example[](#example "Direct link to Example")

    import { OpenAI } from "langchain/llms/openai";const openai = new OpenAI();const response = await openai.generate(["Tell me a joke."]);

> **\_generate**(`prompts`?: `string`\[\], `options`?: `Omit`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions), `never`\>, `runManager`?: [`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

Description

`prompts?`

`string`\[\]

The prompts to pass into the model.

`options?`

`Omit`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions), `never`\>

Optional list of stop words to use when generating.

`runManager?`

[`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)

Optional callback manager to use when generating.

#### Returns[](#returns-6 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

The full LLM output.

#### Overrides[](#overrides-8 "Direct link to Overrides")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[\_generate](/docs/api/llms_base/classes/BaseLLM#_generate)

#### Defined in[](#defined-in-42 "Direct link to Defined in")

[langchain/src/llms/openai.ts:267](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L267)

### \_identifyingParams()[](#_identifyingparams "Direct link to _identifyingparams")

Get the identifying parameters of the LLM.

> **\_identifyingParams**(): `object`

#### Returns[](#returns-7 "Direct link to Returns")

`object`

Member

Type

`model_name`

`string`

#### Overrides[](#overrides-9 "Direct link to Overrides")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[\_identifyingParams](/docs/api/llms_base/classes/BaseLLM#_identifyingparams)

#### Defined in[](#defined-in-43 "Direct link to Defined in")

[langchain/src/llms/openai.ts:236](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L236)

### \_llmType()[](#_llmtype "Direct link to _llmtype")

Return the string type key uniquely identifying this class of LLM.

> **\_llmType**(): `string`

#### Returns[](#returns-8 "Direct link to Returns")

`string`

#### Overrides[](#overrides-10 "Direct link to Overrides")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[\_llmType](/docs/api/llms_base/classes/BaseLLM#_llmtype)

#### Defined in[](#defined-in-44 "Direct link to Defined in")

[langchain/src/llms/openai.ts:565](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L565)

### \_modelType()[](#_modeltype "Direct link to _modeltype")

> **\_modelType**(): `string`

#### Returns[](#returns-9 "Direct link to Returns")

`string`

#### Inherited from[](#inherited-from-14 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[\_modelType](/docs/api/llms_base/classes/BaseLLM#_modeltype)

#### Defined in[](#defined-in-45 "Direct link to Defined in")

[langchain/src/llms/base.ts:394](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L394)

### \_patchConfig()[](#_patchconfig "Direct link to _patchconfig")

> **\_patchConfig**(`config`: `Partial`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)\> = `{}`, `callbackManager`: `undefined` | [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager) = `undefined`): `Partial`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)\>

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

Default value

`config`

`Partial`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)\>

`{}`

`callbackManager`

`undefined` | [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

`undefined`

#### Returns[](#returns-10 "Direct link to Returns")

`Partial`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)\>

#### Inherited from[](#inherited-from-15 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[\_patchConfig](/docs/api/llms_base/classes/BaseLLM#_patchconfig)

#### Defined in[](#defined-in-46 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:146](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L146)

### \_streamIterator()[](#_streamiterator "Direct link to _streamiterator")

> **\_streamIterator**(`input`: [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `options`?: [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)): `AsyncGenerator`<`string`, `any`, `unknown`\>

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

`input`

[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)

`options?`

[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)

#### Returns[](#returns-11 "Direct link to Returns")

`AsyncGenerator`<`string`, `any`, `unknown`\>

#### Inherited from[](#inherited-from-16 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[\_streamIterator](/docs/api/llms_base/classes/BaseLLM#_streamiterator)

#### Defined in[](#defined-in-47 "Direct link to Defined in")

[langchain/src/llms/base.ts:102](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L102)

### \_streamResponseChunks()[](#_streamresponsechunks "Direct link to _streamresponsechunks")

> **\_streamResponseChunks**(`input`: `string`, `options`: `Omit`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions), `never`\>, `runManager`?: [`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)): `AsyncGenerator`<[`GenerationChunk`](/docs/api/schema/classes/GenerationChunk), `any`, `unknown`\>

#### Parameters[](#parameters-5 "Direct link to Parameters")

Parameter

Type

`input`

`string`

`options`

`Omit`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions), `never`\>

`runManager?`

[`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)

#### Returns[](#returns-12 "Direct link to Returns")

`AsyncGenerator`<[`GenerationChunk`](/docs/api/schema/classes/GenerationChunk), `any`, `unknown`\>

#### Overrides[](#overrides-11 "Direct link to Overrides")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[\_streamResponseChunks](/docs/api/llms_base/classes/BaseLLM#_streamresponsechunks)

#### Defined in[](#defined-in-48 "Direct link to Defined in")

[langchain/src/llms/openai.ts:433](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L433)

### batch()[](#batch "Direct link to batch()")

> **batch**(`inputs`: [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)\[\], `options`?: `Partial`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)\> | `Partial`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)\>\[\], `batchOptions`?: `object`): `Promise`<`string`\[\]\>

#### Parameters[](#parameters-6 "Direct link to Parameters")

Parameter

Type

`inputs`

[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)\[\]

`options?`

`Partial`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)\> | `Partial`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)\>\[\]

`batchOptions?`

`object`

`batchOptions.maxConcurrency?`

`number`

#### Returns[](#returns-13 "Direct link to Returns")

`Promise`<`string`\[\]\>

#### Inherited from[](#inherited-from-17 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[batch](/docs/api/llms_base/classes/BaseLLM#batch)

#### Defined in[](#defined-in-49 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:63](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L63)

### bind()[](#bind "Direct link to bind()")

> **bind**(`kwargs`: `Partial`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)\>): [`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `string`, [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)\>

#### Parameters[](#parameters-7 "Direct link to Parameters")

Parameter

Type

`kwargs`

`Partial`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)\>

#### Returns[](#returns-14 "Direct link to Returns")

[`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `string`, [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)\>

#### Inherited from[](#inherited-from-18 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[bind](/docs/api/llms_base/classes/BaseLLM#bind)

#### Defined in[](#defined-in-50 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:41](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L41)

### call()[](#call "Direct link to call()")

Convenience wrapper for [generate](/docs/api/llms_base/classes/BaseLLM#generate) that takes in a single string prompt and returns a single string output.

> **call**(`prompt`: `string`, `options`?: `string`\[\] | [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\>

#### Parameters[](#parameters-8 "Direct link to Parameters")

Parameter

Type

`prompt`

`string`

`options?`

`string`\[\] | [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-15 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[](#inherited-from-19 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[call](/docs/api/llms_base/classes/BaseLLM#call)

#### Defined in[](#defined-in-51 "Direct link to Defined in")

[langchain/src/llms/base.ts:343](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L343)

### generate()[](#generate "Direct link to generate()")

Run the LLM on the given prompts and input, handling caching.

> **generate**(`prompts`: `string`\[\], `options`?: `string`\[\] | [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[](#parameters-9 "Direct link to Parameters")

Parameter

Type

`prompts`

`string`\[\]

`options?`

`string`\[\] | [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-16 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[](#inherited-from-20 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[generate](/docs/api/llms_base/classes/BaseLLM#generate)

#### Defined in[](#defined-in-52 "Direct link to Defined in")

[langchain/src/llms/base.ts:280](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L280)

### generatePrompt()[](#generateprompt "Direct link to generatePrompt()")

> **generatePrompt**(`promptValues`: [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\[\], `options`?: `string`\[\] | [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Parameters[](#parameters-10 "Direct link to Parameters")

Parameter

Type

`promptValues`

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\[\]

`options?`

`string`\[\] | [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-17 "Direct link to Returns")

`Promise`<[`LLMResult`](/docs/api/schema/types/LLMResult)\>

#### Inherited from[](#inherited-from-21 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[generatePrompt](/docs/api/llms_base/classes/BaseLLM#generateprompt)

#### Defined in[](#defined-in-53 "Direct link to Defined in")

[langchain/src/llms/base.ts:169](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L169)

### getNumTokens()[](#getnumtokens "Direct link to getNumTokens()")

> **getNumTokens**(`text`: `string`): `Promise`<`number`\>

#### Parameters[](#parameters-11 "Direct link to Parameters")

Parameter

Type

`text`

`string`

#### Returns[](#returns-18 "Direct link to Returns")

`Promise`<`number`\>

#### Inherited from[](#inherited-from-22 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[getNumTokens](/docs/api/llms_base/classes/BaseLLM#getnumtokens)

#### Defined in[](#defined-in-54 "Direct link to Defined in")

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

#### Defined in[](#defined-in-55 "Direct link to Defined in")

[langchain/src/llms/openai.ts:247](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L247)

### invocationParams()[](#invocationparams "Direct link to invocationParams()")

Get the parameters used to invoke the model

> **invocationParams**(`options`?: `Omit`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions), `never`\>): `CreateCompletionRequest`

#### Parameters[](#parameters-12 "Direct link to Parameters")

Parameter

Type

`options?`

`Omit`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions), `never`\>

#### Returns[](#returns-20 "Direct link to Returns")

`CreateCompletionRequest`

#### Overrides[](#overrides-12 "Direct link to Overrides")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[invocationParams](/docs/api/llms_base/classes/BaseLLM#invocationparams)

#### Defined in[](#defined-in-56 "Direct link to Defined in")

[langchain/src/llms/openai.ts:217](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L217)

### invoke()[](#invoke "Direct link to invoke()")

> **invoke**(`input`: [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `options`?: [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)): `Promise`<`string`\>

#### Parameters[](#parameters-13 "Direct link to Parameters")

Parameter

Type

`input`

[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)

`options?`

[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)

#### Returns[](#returns-21 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[](#inherited-from-23 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[invoke](/docs/api/llms_base/classes/BaseLLM#invoke)

#### Defined in[](#defined-in-57 "Direct link to Defined in")

[langchain/src/llms/base.ts:69](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L69)

### pipe()[](#pipe "Direct link to pipe()")

> **pipe**<NewRunOutput\>(`coerceable`: [`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<`string`, `NewRunOutput`\>): [`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `NewRunOutput`\>

#### Type parameters[](#type-parameters "Direct link to Type parameters")

*   `NewRunOutput`

#### Parameters[](#parameters-14 "Direct link to Parameters")

Parameter

Type

`coerceable`

[`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<`string`, `NewRunOutput`\>

#### Returns[](#returns-22 "Direct link to Returns")

[`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `NewRunOutput`\>

#### Inherited from[](#inherited-from-24 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[pipe](/docs/api/llms_base/classes/BaseLLM#pipe)

#### Defined in[](#defined-in-58 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:153](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L153)

### predict()[](#predict "Direct link to predict()")

> **predict**(`text`: `string`, `options`?: `string`\[\] | [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\>

#### Parameters[](#parameters-15 "Direct link to Parameters")

Parameter

Type

`text`

`string`

`options?`

`string`\[\] | [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-23 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[](#inherited-from-25 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[predict](/docs/api/llms_base/classes/BaseLLM#predict)

#### Defined in[](#defined-in-59 "Direct link to Defined in")

[langchain/src/llms/base.ts:352](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L352)

### predictMessages()[](#predictmessages "Direct link to predictMessages()")

> **predictMessages**(`messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\], `options`?: `string`\[\] | [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Parameters[](#parameters-16 "Direct link to Parameters")

Parameter

Type

`messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]

`options?`

`string`\[\] | [`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-24 "Direct link to Returns")

`Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Inherited from[](#inherited-from-26 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[predictMessages](/docs/api/llms_base/classes/BaseLLM#predictmessages)

#### Defined in[](#defined-in-60 "Direct link to Defined in")

[langchain/src/llms/base.ts:360](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L360)

### serialize()[](#serialize "Direct link to serialize()")

Return a json-like object representing this LLM.

> **serialize**(): [`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Returns[](#returns-25 "Direct link to Returns")

[`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Inherited from[](#inherited-from-27 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[serialize](/docs/api/llms_base/classes/BaseLLM#serialize)

#### Defined in[](#defined-in-61 "Direct link to Defined in")

[langchain/src/llms/base.ts:386](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L386)

### startStream()[](#startstream "Direct link to startStream()")

> **startStream**(`request`: `CreateCompletionRequest`, `options`?: `StreamingAxiosConfiguration`): `object`

#### Parameters[](#parameters-17 "Direct link to Parameters")

Parameter

Type

`request`

`CreateCompletionRequest`

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

#### Defined in[](#defined-in-62 "Direct link to Defined in")

[langchain/src/llms/openai.ts:463](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/openai.ts#L463)

### stream()[](#stream "Direct link to stream()")

> **stream**(`input`: [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput), `options`?: `Partial`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)\>): `Promise`<`IterableReadableStream`<`string`\>\>

#### Parameters[](#parameters-18 "Direct link to Parameters")

Parameter

Type

`input`

[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)

`options?`

`Partial`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)\>

#### Returns[](#returns-27 "Direct link to Returns")

`Promise`<`IterableReadableStream`<`string`\>\>

#### Inherited from[](#inherited-from-28 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[stream](/docs/api/llms_base/classes/BaseLLM#stream)

#### Defined in[](#defined-in-63 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:93](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L93)

### toJSON()[](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[](#returns-28 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[](#inherited-from-29 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[toJSON](/docs/api/llms_base/classes/BaseLLM#tojson)

#### Defined in[](#defined-in-64 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[](#returns-29 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[](#inherited-from-30 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[toJSONNotImplemented](/docs/api/llms_base/classes/BaseLLM#tojsonnotimplemented)

#### Defined in[](#defined-in-65 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L151)

### deserialize()[](#deserialize "Direct link to deserialize()")

Load an LLM from a json-like object describing it.

> `Static` **deserialize**(`data`: [`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)): `Promise`<[`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>\>

#### Parameters[](#parameters-19 "Direct link to Parameters")

Parameter

Type

`data`

[`SerializedLLM`](/docs/api/llms_base/types/SerializedLLM)

#### Returns[](#returns-30 "Direct link to Returns")

`Promise`<[`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)<[`BaseLLMCallOptions`](/docs/api/llms_base/interfaces/BaseLLMCallOptions)\>\>

#### Inherited from[](#inherited-from-31 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[deserialize](/docs/api/llms_base/classes/BaseLLM#deserialize)

#### Defined in[](#defined-in-66 "Direct link to Defined in")

[langchain/src/llms/base.ts:401](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L401)

### isRunnable()[](#isrunnable "Direct link to isRunnable()")

> `Static` **isRunnable**(`thing`: `any`): thing is Runnable<any, any, BaseCallbackConfig\>

#### Parameters[](#parameters-20 "Direct link to Parameters")

Parameter

Type

`thing`

`any`

#### Returns[](#returns-31 "Direct link to Returns")

thing is Runnable<any, any, BaseCallbackConfig\>

#### Inherited from[](#inherited-from-32 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[isRunnable](/docs/api/llms_base/classes/BaseLLM#isrunnable)

#### Defined in[](#defined-in-67 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:164](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L164)

### \_callWithConfig()[](#_callwithconfig "Direct link to _callwithconfig")

> `Protected` **\_callWithConfig**<T\>(`func`: `Function`, `input`: `T`, `options`?: `BaseCallbackConfig` & {`runType`?: `string`;}): `Promise`<`string`\>

#### Type parameters[](#type-parameters-1 "Direct link to Type parameters")

*   `T` _extends_ [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)

#### Parameters[](#parameters-21 "Direct link to Parameters")

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

#### Inherited from[](#inherited-from-33 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[\_callWithConfig](/docs/api/llms_base/classes/BaseLLM#_callwithconfig)

#### Defined in[](#defined-in-68 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:117](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L117)

### \_getOptionsList()[](#_getoptionslist "Direct link to _getoptionslist")

> `Protected` **\_getOptionsList**(`options`: `Partial`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)\> | `Partial`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)\>\[\], `length`: `number` = `0`): `Partial`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)\>\[\]

#### Parameters[](#parameters-22 "Direct link to Parameters")

Parameter

Type

Default value

`options`

`Partial`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)\> | `Partial`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)\>\[\]

`undefined`

`length`

`number`

`0`

#### Returns[](#returns-33 "Direct link to Returns")

`Partial`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)\>\[\]

#### Inherited from[](#inherited-from-34 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[\_getOptionsList](/docs/api/llms_base/classes/BaseLLM#_getoptionslist)

#### Defined in[](#defined-in-69 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L48)

### \_separateRunnableConfigFromCallOptions()[](#_separaterunnableconfigfromcalloptions "Direct link to _separaterunnableconfigfromcalloptions")

> `Protected` **\_separateRunnableConfigFromCallOptions**(`options`?: `Partial`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)\>): \[`BaseCallbackConfig`, `Omit`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions), `never`\>\]

#### Parameters[](#parameters-23 "Direct link to Parameters")

Parameter

Type

`options?`

`Partial`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions)\>

#### Returns[](#returns-34 "Direct link to Returns")

\[`BaseCallbackConfig`, `Omit`<[`OpenAICallOptions`](/docs/api/llms_openai/interfaces/OpenAICallOptions), `never`\>\]

#### Inherited from[](#inherited-from-35 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[\_separateRunnableConfigFromCallOptions](/docs/api/llms_base/classes/BaseLLM#_separaterunnableconfigfromcalloptions)

#### Defined in[](#defined-in-70 "Direct link to Defined in")

[langchain/src/llms/base.ts:91](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L91)

### \_convertInputToPromptValue()[](#_convertinputtopromptvalue "Direct link to _convertinputtopromptvalue")

> `Static` `Protected` **\_convertInputToPromptValue**(`input`: [`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)): [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)

#### Parameters[](#parameters-24 "Direct link to Parameters")

Parameter

Type

`input`

[`BaseLanguageModelInput`](/docs/api/base_language/types/BaseLanguageModelInput)

#### Returns[](#returns-35 "Direct link to Returns")

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)

#### Inherited from[](#inherited-from-36 "Direct link to Inherited from")

[BaseLLM](/docs/api/llms_base/classes/BaseLLM).[\_convertInputToPromptValue](/docs/api/llms_base/classes/BaseLLM#_convertinputtopromptvalue)

#### Defined in[](#defined-in-71 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:192](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L192)