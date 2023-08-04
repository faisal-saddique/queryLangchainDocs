AzureOpenAIInput
================

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### azureOpenAIApiCompletionsDeploymentName?[](#azureopenaiapicompletionsdeploymentname "Direct link to azureOpenAIApiCompletionsDeploymentName?")

> **azureOpenAIApiCompletionsDeploymentName**: `string`

Azure OpenAI API deployment name to use for completions when making requests to Azure OpenAI. Completions are only available for gpt-3.5-turbo and text-davinci-003 deployments. This is the name of the deployment you created in the Azure portal. This will fallback to azureOpenAIApiDeploymentName if not provided. e.g. "my-openai-deployment" this will be used in the endpoint URL: https://{InstanceName}.openai.azure.com/openai/deployments/my-openai-deployment/

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/types/openai-types.ts:126](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/types/openai-types.ts#L126)

### azureOpenAIApiDeploymentName?[](#azureopenaiapideploymentname "Direct link to azureOpenAIApiDeploymentName?")

> **azureOpenAIApiDeploymentName**: `string`

Azure OpenAI API deployment name to use for completions when making requests to Azure OpenAI. This is the name of the deployment you created in the Azure portal. e.g. "my-openai-deployment" this will be used in the endpoint URL: https://{InstanceName}.openai.azure.com/openai/deployments/my-openai-deployment/

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/types/openai-types.ts:107](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/types/openai-types.ts#L107)

### azureOpenAIApiEmbeddingsDeploymentName?[](#azureopenaiapiembeddingsdeploymentname "Direct link to azureOpenAIApiEmbeddingsDeploymentName?")

> **azureOpenAIApiEmbeddingsDeploymentName**: `string`

Azure OpenAI API deployment name to use for embedding when making requests to Azure OpenAI. This is the name of the deployment you created in the Azure portal. This will fallback to azureOpenAIApiDeploymentName if not provided. e.g. "my-openai-deployment" this will be used in the endpoint URL: https://{InstanceName}.openai.azure.com/openai/deployments/my-openai-deployment/

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/types/openai-types.ts:116](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/types/openai-types.ts#L116)

### azureOpenAIApiInstanceName?[](#azureopenaiapiinstancename "Direct link to azureOpenAIApiInstanceName?")

> **azureOpenAIApiInstanceName**: `string`

Azure OpenAI API instance name to use when making requests to Azure OpenAI. this is the name of the instance you created in the Azure portal. e.g. "my-openai-instance" this will be used in the endpoint URL: [https://my-openai-instance.openai.azure.com/openai/deployments/{DeploymentName}/](https://my-openai-instance.openai.azure.com/openai/deployments/%7BDeploymentName%7D/)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/types/openai-types.ts:99](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/types/openai-types.ts#L99)

### azureOpenAIApiKey?[](#azureopenaiapikey "Direct link to azureOpenAIApiKey?")

> **azureOpenAIApiKey**: `string`

API key to use when making requests to Azure OpenAI.

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/types/openai-types.ts:91](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/types/openai-types.ts#L91)

### azureOpenAIApiVersion?[](#azureopenaiapiversion "Direct link to azureOpenAIApiVersion?")

> **azureOpenAIApiVersion**: `string`

API version to use when making requests to Azure OpenAI.

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/types/openai-types.ts:86](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/types/openai-types.ts#L86)

### azureOpenAIBasePath?[](#azureopenaibasepath "Direct link to azureOpenAIBasePath?")

> **azureOpenAIBasePath**: `string`

Custom endpoint for Azure OpenAI API. This is useful in case you have a deployment in another region. e.g. setting this value to "[https://westeurope.api.cognitive.microsoft.com/openai/deployments"](https://westeurope.api.cognitive.microsoft.com/openai/deployments%22) will be result in the endpoint URL: [https://westeurope.api.cognitive.microsoft.com/openai/deployments/{DeploymentName}/](https://westeurope.api.cognitive.microsoft.com/openai/deployments/%7BDeploymentName%7D/)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/types/openai-types.ts:133](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/types/openai-types.ts#L133)