SageMakerEndpointInput
======================

Base interface for language model parameters. A subclass of [BaseLanguageModel](/docs/api/base_language/classes/BaseLanguageModel) should have a constructor that takes in a parameter that extends this interface.

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseLLMParams`](/docs/api/llms_base/interfaces/BaseLLMParams).**SageMakerEndpointInput**

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### clientOptions[](#clientoptions "Direct link to clientOptions")

> **clientOptions**: `SageMakerRuntimeClientConfig`

Options passed to the SageMaker client.

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/llms/sagemaker\_endpoint.ts:74](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/sagemaker_endpoint.ts#L74)

### contentHandler[](#contenthandler "Direct link to contentHandler")

> **contentHandler**: [`SageMakerLLMContentHandler`](/docs/api/llms_sagemaker_endpoint/types/SageMakerLLMContentHandler)

The content handler class that provides an input and output transform functions to handle formats between LLM and the endpoint.

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/llms/sagemaker\_endpoint.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/sagemaker_endpoint.ts#L80)

### endpointName[](#endpointname "Direct link to endpointName")

> **endpointName**: `string`

The name of the endpoint from the deployed SageMaker model. Must be unique within an AWS Region.

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/llms/sagemaker\_endpoint.ts:69](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/sagemaker_endpoint.ts#L69)

### cache?[](#cache "Direct link to cache?")

> **cache**: `boolean` | [`BaseCache`](/docs/api/schema/classes/BaseCache)<[`Generation`](/docs/api/schema/interfaces/Generation)\[\]\>

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[cache](/docs/api/llms_base/interfaces/BaseLLMParams#cache)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/llms/base.ts:38](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L38)

### callbackManager?[](#callbackmanager "Direct link to callbackManager?")

> **callbackManager**: [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Deprecated[](#deprecated "Direct link to Deprecated")

Use `callbacks` instead

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[callbackManager](/docs/api/llms_base/interfaces/BaseLLMParams#callbackmanager)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:79](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L79)

### callbacks?[](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[callbacks](/docs/api/llms_base/interfaces/BaseLLMParams#callbacks)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:25](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L25)

### concurrency?[](#concurrency "Direct link to concurrency?")

> **concurrency**: `number`

#### Deprecated[](#deprecated-1 "Direct link to Deprecated")

Use `maxConcurrency` instead

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[concurrency](/docs/api/llms_base/interfaces/BaseLLMParams#concurrency)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/llms/base.ts:37](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/base.ts#L37)

### endpointKwargs?[](#endpointkwargs "Direct link to endpointKwargs?")

> **endpointKwargs**: `Record`<`string`, `unknown`\>

Optional attributes passed to the InvokeEndpointCommand

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/llms/sagemaker\_endpoint.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/sagemaker_endpoint.ts#L90)

### maxConcurrency?[](#maxconcurrency "Direct link to maxConcurrency?")

> **maxConcurrency**: `number`

The maximum number of concurrent calls that can be made. Defaults to `Infinity`, which means no limit.

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[maxConcurrency](/docs/api/llms_base/interfaces/BaseLLMParams#maxconcurrency)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:21](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/util/async_caller.ts#L21)

### maxRetries?[](#maxretries "Direct link to maxRetries?")

> **maxRetries**: `number`

The maximum number of retries that can be made for a single call, with an exponential backoff between each attempt. Defaults to 6.

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[maxRetries](/docs/api/llms_base/interfaces/BaseLLMParams#maxretries)

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/util/async_caller.ts#L26)

### metadata?[](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[metadata](/docs/api/llms_base/interfaces/BaseLLMParams#metadata)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:27](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L27)

### modelKwargs?[](#modelkwargs "Direct link to modelKwargs?")

> **modelKwargs**: `Record`<`string`, `unknown`\>

Key word arguments to pass to the model.

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/llms/sagemaker\_endpoint.ts:85](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/llms/sagemaker_endpoint.ts#L85)

### tags?[](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[tags](/docs/api/llms_base/interfaces/BaseLLMParams#tags)

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L26)

### verbose?[](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

[BaseLLMParams](/docs/api/llms_base/interfaces/BaseLLMParams).[verbose](/docs/api/llms_base/interfaces/BaseLLMParams#verbose)

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:24](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L24)