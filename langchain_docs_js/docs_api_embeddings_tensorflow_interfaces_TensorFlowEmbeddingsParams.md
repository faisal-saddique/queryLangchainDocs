TensorFlowEmbeddingsParams
==========================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`EmbeddingsParams`](/docs/api/embeddings_base/types/EmbeddingsParams).**TensorFlowEmbeddingsParams**

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### maxConcurrency?[](#maxconcurrency "Direct link to maxConcurrency?")

> **maxConcurrency**: `number`

The maximum number of concurrent calls that can be made. Defaults to `Infinity`, which means no limit.

#### Inherited from[](#inherited-from "Direct link to Inherited from")

EmbeddingsParams.maxConcurrency

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:21](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/util/async_caller.ts#L21)

### maxRetries?[](#maxretries "Direct link to maxRetries?")

> **maxRetries**: `number`

The maximum number of retries that can be made for a single call, with an exponential backoff between each attempt. Defaults to 6.

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

EmbeddingsParams.maxRetries

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/util/async_caller.ts#L26)