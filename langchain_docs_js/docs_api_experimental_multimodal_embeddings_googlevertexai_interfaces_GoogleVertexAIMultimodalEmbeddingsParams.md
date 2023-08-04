GoogleVertexAIMultimodalEmbeddingsParams
========================================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`EmbeddingsParams`](/docs/api/embeddings_base/types/EmbeddingsParams).`GoogleVertexAIConnectionParams`.**GoogleVertexAIMultimodalEmbeddingsParams**

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### authOptions?[](#authoptions "Direct link to authOptions?")

> **authOptions**: `GoogleAuthOptions`<`JSONClient`\>

#### Inherited from[](#inherited-from "Direct link to Inherited from")

GoogleVertexAIConnectionParams.authOptions

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/types/googlevertexai-types.ts:8](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/types/googlevertexai-types.ts#L8)

### endpoint?[](#endpoint "Direct link to endpoint?")

> **endpoint**: `string`

Hostname for the API call

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

GoogleVertexAIConnectionParams.endpoint

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/types/googlevertexai-types.ts:6](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/types/googlevertexai-types.ts#L6)

### location?[](#location "Direct link to location?")

> **location**: `string`

Region where the LLM is stored

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

GoogleVertexAIConnectionParams.location

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/types/googlevertexai-types.ts:11](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/types/googlevertexai-types.ts#L11)

### maxConcurrency?[](#maxconcurrency "Direct link to maxConcurrency?")

> **maxConcurrency**: `number`

The maximum number of concurrent calls that can be made. Defaults to `Infinity`, which means no limit.

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

EmbeddingsParams.maxConcurrency

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:21](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/util/async_caller.ts#L21)

### maxRetries?[](#maxretries "Direct link to maxRetries?")

> **maxRetries**: `number`

The maximum number of retries that can be made for a single call, with an exponential backoff between each attempt. Defaults to 6.

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

EmbeddingsParams.maxRetries

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/util/async_caller.ts#L26)

### model?[](#model "Direct link to model?")

> **model**: `string`

Model to use

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

GoogleVertexAIConnectionParams.model

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/types/googlevertexai-types.ts:14](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/types/googlevertexai-types.ts#L14)