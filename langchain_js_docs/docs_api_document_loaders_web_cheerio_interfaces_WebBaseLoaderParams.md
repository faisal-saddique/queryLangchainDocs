WebBaseLoaderParams
===================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   `AsyncCallerParams`.**WebBaseLoaderParams**

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### maxConcurrency?[​](#maxconcurrency "Direct link to maxConcurrency?")

> **maxConcurrency**: `number`

The maximum number of concurrent calls that can be made. Defaults to `Infinity`, which means no limit.

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

AsyncCallerParams.maxConcurrency

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:21](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/util/async_caller.ts#L21)

### maxRetries?[​](#maxretries "Direct link to maxRetries?")

> **maxRetries**: `number`

The maximum number of retries that can be made for a single call, with an exponential backoff between each attempt. Defaults to 6.

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

AsyncCallerParams.maxRetries

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:26](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/util/async_caller.ts#L26)

### selector?[​](#selector "Direct link to selector?")

> **selector**: `SelectorType`

The selector to use to extract the text from the document. Defaults to "body".

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/document\_loaders/web/cheerio.ts:17](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/cheerio.ts#L17)

### textDecoder?[​](#textdecoder "Direct link to textDecoder?")

> **textDecoder**: `TextDecoder`

The text decoder to use to decode the response. Defaults to UTF-8.

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/document\_loaders/web/cheerio.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/cheerio.ts#L22)

### timeout?[​](#timeout "Direct link to timeout?")

> **timeout**: `number`

The timeout in milliseconds for the fetch request. Defaults to 10s.

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/document\_loaders/web/cheerio.ts:11](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/cheerio.ts#L11)