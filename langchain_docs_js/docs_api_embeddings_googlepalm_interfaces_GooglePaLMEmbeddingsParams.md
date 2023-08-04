GooglePaLMEmbeddingsParams
==========================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`EmbeddingsParams`](/docs/api/embeddings_base/types/EmbeddingsParams).**GooglePaLMEmbeddingsParams**

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### apiKey?[](#apikey "Direct link to apiKey?")

> **apiKey**: `string`

Google Palm API key to use

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/embeddings/googlepalm.ts:16](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/embeddings/googlepalm.ts#L16)

### maxConcurrency?[](#maxconcurrency "Direct link to maxConcurrency?")

> **maxConcurrency**: `number`

The maximum number of concurrent calls that can be made. Defaults to `Infinity`, which means no limit.

#### Inherited from[](#inherited-from "Direct link to Inherited from")

EmbeddingsParams.maxConcurrency

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:21](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/util/async_caller.ts#L21)

### maxRetries?[](#maxretries "Direct link to maxRetries?")

> **maxRetries**: `number`

The maximum number of retries that can be made for a single call, with an exponential backoff between each attempt. Defaults to 6.

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

EmbeddingsParams.maxRetries

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/util/async_caller.ts#L26)

### modelName?[](#modelname "Direct link to modelName?")

> **modelName**: `string`

Model Name to use

Note: The format must follow the pattern - `models/{model}`

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/embeddings/googlepalm.ts:12](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/embeddings/googlepalm.ts#L12)