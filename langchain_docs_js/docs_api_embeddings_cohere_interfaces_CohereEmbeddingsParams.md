CohereEmbeddingsParams
======================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`EmbeddingsParams`](/docs/api/embeddings_base/types/EmbeddingsParams).**CohereEmbeddingsParams**

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### modelName[](#modelname "Direct link to modelName")

> **modelName**: `string`

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/embeddings/cohere.ts:6](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/embeddings/cohere.ts#L6)

### batchSize?[](#batchsize "Direct link to batchSize?")

> **batchSize**: `number`

The maximum number of documents to embed in a single request. This is limited by the Cohere API to a maximum of 96.

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/embeddings/cohere.ts:12](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/embeddings/cohere.ts#L12)

### maxConcurrency?[](#maxconcurrency "Direct link to maxConcurrency?")

> **maxConcurrency**: `number`

The maximum number of concurrent calls that can be made. Defaults to `Infinity`, which means no limit.

#### Inherited from[](#inherited-from "Direct link to Inherited from")

EmbeddingsParams.maxConcurrency

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:21](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/util/async_caller.ts#L21)

### maxRetries?[](#maxretries "Direct link to maxRetries?")

> **maxRetries**: `number`

The maximum number of retries that can be made for a single call, with an exponential backoff between each attempt. Defaults to 6.

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

EmbeddingsParams.maxRetries

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/util/async_caller.ts#L26)