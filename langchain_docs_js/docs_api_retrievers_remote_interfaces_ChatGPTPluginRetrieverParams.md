ChatGPTPluginRetrieverParams
============================

Base Index class. All indexes should extend this class.

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`RemoteRetrieverParams`](/docs/api/retrievers_remote/interfaces/RemoteRetrieverParams).**ChatGPTPluginRetrieverParams**

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### auth[](#auth "Direct link to auth")

> **auth**: [`RemoteRetrieverAuth`](/docs/api/retrievers_remote/types/RemoteRetrieverAuth)

The authentication method to use, currently implemented is

*   false: no authentication
*   { bearer: string }: Bearer token authentication

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[RemoteRetrieverParams](/docs/api/retrievers_remote/interfaces/RemoteRetrieverParams).[auth](/docs/api/retrievers_remote/interfaces/RemoteRetrieverParams#auth)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/retrievers/remote/base.ts:22](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/remote/base.ts#L22)

### url[](#url "Direct link to url")

> **url**: `string`

The URL of the remote retriever server

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[RemoteRetrieverParams](/docs/api/retrievers_remote/interfaces/RemoteRetrieverParams).[url](/docs/api/retrievers_remote/interfaces/RemoteRetrieverParams#url)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/retrievers/remote/base.ts:15](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/remote/base.ts#L15)

### callbacks?[](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[RemoteRetrieverParams](/docs/api/retrievers_remote/interfaces/RemoteRetrieverParams).[callbacks](/docs/api/retrievers_remote/interfaces/RemoteRetrieverParams#callbacks)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:16](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/retriever.ts#L16)

### filter?[](#filter "Direct link to filter?")

> **filter**: [`ChatGPTPluginRetrieverFilter`](/docs/api/retrievers_remote/interfaces/ChatGPTPluginRetrieverFilter)

The filter to use when querying the ChatGPTRetrievalPlugin server

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/retrievers/remote/chatgpt-plugin.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/remote/chatgpt-plugin.ts#L26)

### maxConcurrency?[](#maxconcurrency "Direct link to maxConcurrency?")

> **maxConcurrency**: `number`

The maximum number of concurrent calls that can be made. Defaults to `Infinity`, which means no limit.

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[RemoteRetrieverParams](/docs/api/retrievers_remote/interfaces/RemoteRetrieverParams).[maxConcurrency](/docs/api/retrievers_remote/interfaces/RemoteRetrieverParams#maxconcurrency)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:21](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/util/async_caller.ts#L21)

### maxRetries?[](#maxretries "Direct link to maxRetries?")

> **maxRetries**: `number`

The maximum number of retries that can be made for a single call, with an exponential backoff between each attempt. Defaults to 6.

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[RemoteRetrieverParams](/docs/api/retrievers_remote/interfaces/RemoteRetrieverParams).[maxRetries](/docs/api/retrievers_remote/interfaces/RemoteRetrieverParams#maxretries)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/util/async_caller.ts#L26)

### metadata?[](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[RemoteRetrieverParams](/docs/api/retrievers_remote/interfaces/RemoteRetrieverParams).[metadata](/docs/api/retrievers_remote/interfaces/RemoteRetrieverParams#metadata)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:18](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/retriever.ts#L18)

### tags?[](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[RemoteRetrieverParams](/docs/api/retrievers_remote/interfaces/RemoteRetrieverParams).[tags](/docs/api/retrievers_remote/interfaces/RemoteRetrieverParams#tags)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:17](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/retriever.ts#L17)

### topK?[](#topk "Direct link to topK?")

> **topK**: `number`

The number of results to request from the ChatGPTRetrievalPlugin server

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/retrievers/remote/chatgpt-plugin.ts:21](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/remote/chatgpt-plugin.ts#L21)

### verbose?[](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

[RemoteRetrieverParams](/docs/api/retrievers_remote/interfaces/RemoteRetrieverParams).[verbose](/docs/api/retrievers_remote/interfaces/RemoteRetrieverParams#verbose)

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:19](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/retriever.ts#L19)