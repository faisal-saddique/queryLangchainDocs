OpenAIEmbeddingsParams
======================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`EmbeddingsParams`](/docs/api/embeddings_base/types/EmbeddingsParams).**OpenAIEmbeddingsParams**

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### modelName[](#modelname "Direct link to modelName")

> **modelName**: `string`

Model name to use

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/embeddings/openai.ts:17](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/embeddings/openai.ts#L17)

### batchSize?[](#batchsize "Direct link to batchSize?")

> **batchSize**: `number`

The maximum number of documents to embed in a single request. This is limited by the OpenAI API to a maximum of 2048.

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/embeddings/openai.ts:28](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/embeddings/openai.ts#L28)

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

### stripNewLines?[](#stripnewlines "Direct link to stripNewLines?")

> **stripNewLines**: `boolean`

Whether to strip new lines from the input text. This is recommended by OpenAI, but may not be suitable for all use cases.

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/embeddings/openai.ts:34](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/embeddings/openai.ts#L34)

### timeout?[](#timeout "Direct link to timeout?")

> **timeout**: `number`

Timeout to use when making requests to OpenAI.

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/embeddings/openai.ts:22](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/embeddings/openai.ts#L22)