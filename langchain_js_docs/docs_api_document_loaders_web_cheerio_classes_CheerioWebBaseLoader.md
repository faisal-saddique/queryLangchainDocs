CheerioWebBaseLoader
====================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseDocumentLoader`](/docs/api/document_loaders_base/classes/BaseDocumentLoader).**CheerioWebBaseLoader**

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   [`DocumentLoader`](/docs/api/document_loaders_base/interfaces/DocumentLoader)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new CheerioWebBaseLoader**(`webPath`: `string`, `fields`?: [`WebBaseLoaderParams`](/docs/api/document_loaders_web_cheerio/interfaces/WebBaseLoaderParams)): [`CheerioWebBaseLoader`](/docs/api/document_loaders_web_cheerio/classes/CheerioWebBaseLoader)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`webPath`

`string`

`fields?`

[`WebBaseLoaderParams`](/docs/api/document_loaders_web_cheerio/interfaces/WebBaseLoaderParams)

#### Returns[​](#returns "Direct link to Returns")

[`CheerioWebBaseLoader`](/docs/api/document_loaders_web_cheerio/classes/CheerioWebBaseLoader)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[constructor](/docs/api/document_loaders_base/classes/BaseDocumentLoader#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/document\_loaders/web/cheerio.ts:37](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/cheerio.ts#L37)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### caller[​](#caller "Direct link to caller")

> **caller**: `AsyncCaller`

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/document\_loaders/web/cheerio.ts:31](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/cheerio.ts#L31)

### timeout[​](#timeout "Direct link to timeout")

> **timeout**: `number`

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/document\_loaders/web/cheerio.ts:29](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/cheerio.ts#L29)

### webPath[​](#webpath "Direct link to webPath")

> **webPath**: `string`

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/document\_loaders/web/cheerio.ts:37](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/cheerio.ts#L37)

### selector?[​](#selector "Direct link to selector?")

> **selector**: `SelectorType`

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/document\_loaders/web/cheerio.ts:33](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/cheerio.ts#L33)

### textDecoder?[​](#textdecoder "Direct link to textDecoder?")

> **textDecoder**: `TextDecoder`

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/document\_loaders/web/cheerio.ts:35](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/cheerio.ts#L35)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### load()[​](#load "Direct link to load()")

> **load**(): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Returns[​](#returns-1 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

[DocumentLoader](/docs/api/document_loaders_base/interfaces/DocumentLoader).[load](/docs/api/document_loaders_base/interfaces/DocumentLoader#load)

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[load](/docs/api/document_loaders_base/classes/BaseDocumentLoader#load)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/document\_loaders/web/cheerio.ts:72](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/cheerio.ts#L72)

### loadAndSplit()[​](#loadandsplit "Direct link to loadAndSplit()")

> **loadAndSplit**(`splitter`: [`TextSplitter`](/docs/api/text_splitter/classes/TextSplitter) = `...`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`splitter`

[`TextSplitter`](/docs/api/text_splitter/classes/TextSplitter)

#### Returns[​](#returns-2 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

[DocumentLoader](/docs/api/document_loaders_base/interfaces/DocumentLoader).[loadAndSplit](/docs/api/document_loaders_base/interfaces/DocumentLoader#loadandsplit)

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[loadAndSplit](/docs/api/document_loaders_base/classes/BaseDocumentLoader#loadandsplit)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/document\_loaders/base.ts:15](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/base.ts#L15)

### scrape()[​](#scrape "Direct link to scrape()")

> **scrape**(): `Promise`<`CheerioAPI`\>

#### Returns[​](#returns-3 "Direct link to Returns")

`Promise`<`CheerioAPI`\>

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/document\_loaders/web/cheerio.ts:63](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/cheerio.ts#L63)

### \_scrape()[​](#_scrape "Direct link to _scrape")

> `Static` **\_scrape**(`url`: `string`, `caller`: `AsyncCaller`, `timeout`: `undefined` | `number`, `textDecoder`?: `TextDecoder`): `Promise`<`CheerioAPI`\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`url`

`string`

`caller`

`AsyncCaller`

`timeout`

`undefined` | `number`

`textDecoder?`

`TextDecoder`

#### Returns[​](#returns-4 "Direct link to Returns")

`Promise`<`CheerioAPI`\>

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/document\_loaders/web/cheerio.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/cheerio.ts#L46)

### imports()[​](#imports "Direct link to imports()")

> `Static` **imports**(): `Promise`<{`load`: (`content`: `string` | `Buffer` | `AnyNode` | `AnyNode`\[\], `options?`: null | `CheerioOptions`, `isDocument?`: `boolean`) => `CheerioAPI`;}\>

#### Returns[​](#returns-5 "Direct link to Returns")

`Promise`<{`load`: (`content`: `string` | `Buffer` | `AnyNode` | `AnyNode`\[\], `options?`: null | `CheerioOptions`, `isDocument?`: `boolean`) => `CheerioAPI`;}\>

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/document\_loaders/web/cheerio.ts:79](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/cheerio.ts#L79)