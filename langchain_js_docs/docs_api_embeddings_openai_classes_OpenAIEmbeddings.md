OpenAIEmbeddings
================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`Embeddings`](/docs/api/embeddings_base/classes/Embeddings).**OpenAIEmbeddings**

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   [`OpenAIEmbeddingsParams`](/docs/api/embeddings_openai/interfaces/OpenAIEmbeddingsParams)
*   [`AzureOpenAIInput`](/docs/api/llms_openai/interfaces/AzureOpenAIInput)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new OpenAIEmbeddings**(`fields`?: `Partial`<[`OpenAIEmbeddingsParams`](/docs/api/embeddings_openai/interfaces/OpenAIEmbeddingsParams)\> & `Partial`<[`AzureOpenAIInput`](/docs/api/llms_openai/interfaces/AzureOpenAIInput)\> & {`openAIApiKey`?: `string`; `verbose`?: `boolean`;}, `configuration`?: `ConfigurationParameters`): [`OpenAIEmbeddings`](/docs/api/embeddings_openai/classes/OpenAIEmbeddings)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields?`

`Partial`<[`OpenAIEmbeddingsParams`](/docs/api/embeddings_openai/interfaces/OpenAIEmbeddingsParams)\> & `Partial`<[`AzureOpenAIInput`](/docs/api/llms_openai/interfaces/AzureOpenAIInput)\> & {`openAIApiKey`?: `string`;  
`verbose`?: `boolean`;}

`configuration?`

`ConfigurationParameters`

#### Returns[​](#returns "Direct link to Returns")

[`OpenAIEmbeddings`](/docs/api/embeddings_openai/classes/OpenAIEmbeddings)

#### Overrides[​](#overrides "Direct link to Overrides")

[Embeddings](/docs/api/embeddings_base/classes/Embeddings).[constructor](/docs/api/embeddings_base/classes/Embeddings#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/embeddings/openai.ts:63](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/openai.ts#L63)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### batchSize[​](#batchsize "Direct link to batchSize")

> **batchSize**: `number` = `512`

The maximum number of documents to embed in a single request. This is limited by the OpenAI API to a maximum of 2048.

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

[OpenAIEmbeddingsParams](/docs/api/embeddings_openai/interfaces/OpenAIEmbeddingsParams).[batchSize](/docs/api/embeddings_openai/interfaces/OpenAIEmbeddingsParams#batchsize)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/embeddings/openai.ts:43](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/openai.ts#L43)

### caller[​](#caller "Direct link to caller")

> **caller**: `AsyncCaller`

The async caller should be used by subclasses to make any async calls, which will thus benefit from the concurrency and retry logic.

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[Embeddings](/docs/api/embeddings_base/classes/Embeddings).[caller](/docs/api/embeddings_base/classes/Embeddings#caller)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/embeddings/base.ts:10](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/base.ts#L10)

### modelName[​](#modelname "Direct link to modelName")

> **modelName**: `string` = `"text-embedding-ada-002"`

Model name to use

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

[OpenAIEmbeddingsParams](/docs/api/embeddings_openai/interfaces/OpenAIEmbeddingsParams).[modelName](/docs/api/embeddings_openai/interfaces/OpenAIEmbeddingsParams#modelname)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/embeddings/openai.ts:41](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/openai.ts#L41)

### stripNewLines[​](#stripnewlines "Direct link to stripNewLines")

> **stripNewLines**: `boolean` = `true`

Whether to strip new lines from the input text. This is recommended by OpenAI, but may not be suitable for all use cases.

#### Implementation of[​](#implementation-of-2 "Direct link to Implementation of")

[OpenAIEmbeddingsParams](/docs/api/embeddings_openai/interfaces/OpenAIEmbeddingsParams).[stripNewLines](/docs/api/embeddings_openai/interfaces/OpenAIEmbeddingsParams#stripnewlines)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/embeddings/openai.ts:45](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/openai.ts#L45)

### azureOpenAIApiDeploymentName?[​](#azureopenaiapideploymentname "Direct link to azureOpenAIApiDeploymentName?")

> **azureOpenAIApiDeploymentName**: `string`

Azure OpenAI API deployment name to use for completions when making requests to Azure OpenAI. This is the name of the deployment you created in the Azure portal. e.g. "my-openai-deployment" this will be used in the endpoint URL: https://{InstanceName}.openai.azure.com/openai/deployments/my-openai-deployment/

#### Implementation of[​](#implementation-of-3 "Direct link to Implementation of")

[AzureOpenAIInput](/docs/api/llms_openai/interfaces/AzureOpenAIInput).[azureOpenAIApiDeploymentName](/docs/api/llms_openai/interfaces/AzureOpenAIInput#azureopenaiapideploymentname)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/embeddings/openai.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/openai.ts#L55)

### azureOpenAIApiInstanceName?[​](#azureopenaiapiinstancename "Direct link to azureOpenAIApiInstanceName?")

> **azureOpenAIApiInstanceName**: `string`

Azure OpenAI API instance name to use when making requests to Azure OpenAI. this is the name of the instance you created in the Azure portal. e.g. "my-openai-instance" this will be used in the endpoint URL: [https://my-openai-instance.openai.azure.com/openai/deployments/{DeploymentName}/](https://my-openai-instance.openai.azure.com/openai/deployments/%7BDeploymentName%7D/)

#### Implementation of[​](#implementation-of-4 "Direct link to Implementation of")

[AzureOpenAIInput](/docs/api/llms_openai/interfaces/AzureOpenAIInput).[azureOpenAIApiInstanceName](/docs/api/llms_openai/interfaces/AzureOpenAIInput#azureopenaiapiinstancename)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/embeddings/openai.ts:53](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/openai.ts#L53)

### azureOpenAIApiKey?[​](#azureopenaiapikey "Direct link to azureOpenAIApiKey?")

> **azureOpenAIApiKey**: `string`

API key to use when making requests to Azure OpenAI.

#### Implementation of[​](#implementation-of-5 "Direct link to Implementation of")

[AzureOpenAIInput](/docs/api/llms_openai/interfaces/AzureOpenAIInput).[azureOpenAIApiKey](/docs/api/llms_openai/interfaces/AzureOpenAIInput#azureopenaiapikey)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/embeddings/openai.ts:51](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/openai.ts#L51)

### azureOpenAIApiVersion?[​](#azureopenaiapiversion "Direct link to azureOpenAIApiVersion?")

> **azureOpenAIApiVersion**: `string`

API version to use when making requests to Azure OpenAI.

#### Implementation of[​](#implementation-of-6 "Direct link to Implementation of")

[AzureOpenAIInput](/docs/api/llms_openai/interfaces/AzureOpenAIInput).[azureOpenAIApiVersion](/docs/api/llms_openai/interfaces/AzureOpenAIInput#azureopenaiapiversion)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/embeddings/openai.ts:49](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/openai.ts#L49)

### azureOpenAIBasePath?[​](#azureopenaibasepath "Direct link to azureOpenAIBasePath?")

> **azureOpenAIBasePath**: `string`

Custom endpoint for Azure OpenAI API. This is useful in case you have a deployment in another region. e.g. setting this value to "[https://westeurope.api.cognitive.microsoft.com/openai/deployments"](https://westeurope.api.cognitive.microsoft.com/openai/deployments%22) will be result in the endpoint URL: [https://westeurope.api.cognitive.microsoft.com/openai/deployments/{DeploymentName}/](https://westeurope.api.cognitive.microsoft.com/openai/deployments/%7BDeploymentName%7D/)

#### Implementation of[​](#implementation-of-7 "Direct link to Implementation of")

[AzureOpenAIInput](/docs/api/llms_openai/interfaces/AzureOpenAIInput).[azureOpenAIBasePath](/docs/api/llms_openai/interfaces/AzureOpenAIInput#azureopenaibasepath)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/embeddings/openai.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/openai.ts#L57)

### timeout?[​](#timeout "Direct link to timeout?")

> **timeout**: `number`

Timeout to use when making requests to OpenAI.

#### Implementation of[​](#implementation-of-8 "Direct link to Implementation of")

[OpenAIEmbeddingsParams](/docs/api/embeddings_openai/interfaces/OpenAIEmbeddingsParams).[timeout](/docs/api/embeddings_openai/interfaces/OpenAIEmbeddingsParams#timeout)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/embeddings/openai.ts:47](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/openai.ts#L47)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### embedDocuments()[​](#embeddocuments "Direct link to embedDocuments()")

> **embedDocuments**(`texts`: `string`\[\]): `Promise`<`number`\[\]\[\]\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`texts`

`string`\[\]

#### Returns[​](#returns-1 "Direct link to Returns")

`Promise`<`number`\[\]\[\]\>

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[Embeddings](/docs/api/embeddings_base/classes/Embeddings).[embedDocuments](/docs/api/embeddings_base/classes/Embeddings#embeddocuments)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/embeddings/openai.ts:129](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/openai.ts#L129)

### embedQuery()[​](#embedquery "Direct link to embedQuery()")

> **embedQuery**(`text`: `string`): `Promise`<`number`\[\]\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`text`

`string`

#### Returns[​](#returns-2 "Direct link to Returns")

`Promise`<`number`\[\]\>

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[Embeddings](/docs/api/embeddings_base/classes/Embeddings).[embedQuery](/docs/api/embeddings_base/classes/Embeddings#embedquery)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/embeddings/openai.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/embeddings/openai.ts#L151)