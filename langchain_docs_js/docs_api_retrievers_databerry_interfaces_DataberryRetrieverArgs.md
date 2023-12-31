DataberryRetrieverArgs
======================

Base Index class. All indexes should extend this class.

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   `AsyncCallerParams`.[`BaseRetrieverInput`](/docs/api/schema_retriever/interfaces/BaseRetrieverInput).**DataberryRetrieverArgs**

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### datastoreUrl[](#datastoreurl "Direct link to datastoreUrl")

> **datastoreUrl**: `string`

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/retrievers/databerry.ts:8](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/databerry.ts#L8)

### apiKey?[](#apikey "Direct link to apiKey?")

> **apiKey**: `string`

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/retrievers/databerry.ts:10](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/databerry.ts#L10)

### callbacks?[](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BaseRetrieverInput](/docs/api/schema_retriever/interfaces/BaseRetrieverInput).[callbacks](/docs/api/schema_retriever/interfaces/BaseRetrieverInput#callbacks)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:16](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/retriever.ts#L16)

### maxConcurrency?[](#maxconcurrency "Direct link to maxConcurrency?")

> **maxConcurrency**: `number`

The maximum number of concurrent calls that can be made. Defaults to `Infinity`, which means no limit.

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

AsyncCallerParams.maxConcurrency

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:21](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/util/async_caller.ts#L21)

### maxRetries?[](#maxretries "Direct link to maxRetries?")

> **maxRetries**: `number`

The maximum number of retries that can be made for a single call, with an exponential backoff between each attempt. Defaults to 6.

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

AsyncCallerParams.maxRetries

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/util/async_caller.ts#L26)

### metadata?[](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[BaseRetrieverInput](/docs/api/schema_retriever/interfaces/BaseRetrieverInput).[metadata](/docs/api/schema_retriever/interfaces/BaseRetrieverInput#metadata)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:18](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/retriever.ts#L18)

### tags?[](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[BaseRetrieverInput](/docs/api/schema_retriever/interfaces/BaseRetrieverInput).[tags](/docs/api/schema_retriever/interfaces/BaseRetrieverInput#tags)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:17](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/retriever.ts#L17)

### topK?[](#topk "Direct link to topK?")

> **topK**: `number`

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/retrievers/databerry.ts:9](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/databerry.ts#L9)

### verbose?[](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[BaseRetrieverInput](/docs/api/schema_retriever/interfaces/BaseRetrieverInput).[verbose](/docs/api/schema_retriever/interfaces/BaseRetrieverInput#verbose)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:19](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/retriever.ts#L19)