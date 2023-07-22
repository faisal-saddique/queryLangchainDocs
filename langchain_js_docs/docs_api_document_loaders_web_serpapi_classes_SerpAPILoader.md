SerpAPILoader
=============

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseDocumentLoader`](/docs/api/document_loaders_base/classes/BaseDocumentLoader).**SerpAPILoader**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new SerpAPILoader**(`params`: `SerpAPIParameters`): [`SerpAPILoader`](/docs/api/document_loaders_web_serpapi/classes/SerpAPILoader)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`params`

`SerpAPIParameters`

#### Returns[​](#returns "Direct link to Returns")

[`SerpAPILoader`](/docs/api/document_loaders_web_serpapi/classes/SerpAPILoader)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[constructor](/docs/api/document_loaders_base/classes/BaseDocumentLoader#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/document\_loaders/web/serpapi.ts:18](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/serpapi.ts#L18)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### buildUrl()[​](#buildurl "Direct link to buildUrl()")

Builds the URL for the SerpAPI search request.

> **buildUrl**(): `string`

#### Returns[​](#returns-1 "Direct link to Returns")

`string`

The URL for the search request.

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/document\_loaders/web/serpapi.ts:35](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/serpapi.ts#L35)

### load()[​](#load "Direct link to load()")

Loads the search results from the SerpAPI.

#### Throws[​](#throws "Direct link to Throws")

An error if the search results could not be loaded.

> **load**(): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Returns[​](#returns-2 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

An array of Documents representing the search results.

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[load](/docs/api/document_loaders_base/classes/BaseDocumentLoader#load)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/document\_loaders/web/serpapi.ts:111](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/serpapi.ts#L111)

### loadAndSplit()[​](#loadandsplit "Direct link to loadAndSplit()")

> **loadAndSplit**(`splitter`: [`TextSplitter`](/docs/api/text_splitter/classes/TextSplitter) = `...`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`splitter`

[`TextSplitter`](/docs/api/text_splitter/classes/TextSplitter)

#### Returns[​](#returns-3 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[loadAndSplit](/docs/api/document_loaders_base/classes/BaseDocumentLoader#loadandsplit)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/document\_loaders/base.ts:15](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/base.ts#L15)

### processResponseData()[​](#processresponsedata "Direct link to processResponseData()")

Processes the response data from the SerpAPI search request and converts it into an array of Documents.

> **processResponseData**(`data`: `Record`<`string`, `unknown`\>): [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

Description

`data`

`Record`<`string`, `unknown`\>

The response data from the SerpAPI search request.

#### Returns[​](#returns-4 "Direct link to Returns")

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

An array of Documents.

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/document\_loaders/web/serpapi.ts:67](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/serpapi.ts#L67)