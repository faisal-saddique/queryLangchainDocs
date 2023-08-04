HNLoader
========

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`CheerioWebBaseLoader`](/docs/api/document_loaders_web_cheerio/classes/CheerioWebBaseLoader).**HNLoader**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new HNLoader**(`webPath`: `string`): [`HNLoader`](/docs/api/document_loaders_web_hn/classes/HNLoader)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`webPath`

`string`

#### Returns[](#returns "Direct link to Returns")

[`HNLoader`](/docs/api/document_loaders_web_hn/classes/HNLoader)

#### Overrides[](#overrides "Direct link to Overrides")

[CheerioWebBaseLoader](/docs/api/document_loaders_web_cheerio/classes/CheerioWebBaseLoader).[constructor](/docs/api/document_loaders_web_cheerio/classes/CheerioWebBaseLoader#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/document\_loaders/web/hn.ts:6](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/hn.ts#L6)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### caller[](#caller "Direct link to caller")

> **caller**: `AsyncCaller`

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[CheerioWebBaseLoader](/docs/api/document_loaders_web_cheerio/classes/CheerioWebBaseLoader).[caller](/docs/api/document_loaders_web_cheerio/classes/CheerioWebBaseLoader#caller)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/document\_loaders/web/cheerio.ts:31](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/cheerio.ts#L31)

### timeout[](#timeout "Direct link to timeout")

> **timeout**: `number`

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[CheerioWebBaseLoader](/docs/api/document_loaders_web_cheerio/classes/CheerioWebBaseLoader).[timeout](/docs/api/document_loaders_web_cheerio/classes/CheerioWebBaseLoader#timeout)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/document\_loaders/web/cheerio.ts:29](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/cheerio.ts#L29)

### webPath[](#webpath "Direct link to webPath")

> **webPath**: `string`

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[CheerioWebBaseLoader](/docs/api/document_loaders_web_cheerio/classes/CheerioWebBaseLoader).[webPath](/docs/api/document_loaders_web_cheerio/classes/CheerioWebBaseLoader#webpath)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/document\_loaders/web/hn.ts:6](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/hn.ts#L6)

### selector?[](#selector "Direct link to selector?")

> **selector**: `SelectorType`

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[CheerioWebBaseLoader](/docs/api/document_loaders_web_cheerio/classes/CheerioWebBaseLoader).[selector](/docs/api/document_loaders_web_cheerio/classes/CheerioWebBaseLoader#selector)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/document\_loaders/web/cheerio.ts:33](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/cheerio.ts#L33)

### textDecoder?[](#textdecoder "Direct link to textDecoder?")

> **textDecoder**: `TextDecoder`

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[CheerioWebBaseLoader](/docs/api/document_loaders_web_cheerio/classes/CheerioWebBaseLoader).[textDecoder](/docs/api/document_loaders_web_cheerio/classes/CheerioWebBaseLoader#textdecoder)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/document\_loaders/web/cheerio.ts:35](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/cheerio.ts#L35)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### load()[](#load "Direct link to load()")

> **load**(): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Returns[](#returns-1 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Overrides[](#overrides-1 "Direct link to Overrides")

[CheerioWebBaseLoader](/docs/api/document_loaders_web_cheerio/classes/CheerioWebBaseLoader).[load](/docs/api/document_loaders_web_cheerio/classes/CheerioWebBaseLoader#load)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/document\_loaders/web/hn.ts:10](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/hn.ts#L10)

### loadAndSplit()[](#loadandsplit "Direct link to loadAndSplit()")

> **loadAndSplit**(`splitter`: [`TextSplitter`](/docs/api/text_splitter/classes/TextSplitter) = `...`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`splitter`

[`TextSplitter`](/docs/api/text_splitter/classes/TextSplitter)

#### Returns[](#returns-2 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[CheerioWebBaseLoader](/docs/api/document_loaders_web_cheerio/classes/CheerioWebBaseLoader).[loadAndSplit](/docs/api/document_loaders_web_cheerio/classes/CheerioWebBaseLoader#loadandsplit)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/document\_loaders/base.ts:15](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/base.ts#L15)

### scrape()[](#scrape "Direct link to scrape()")

> **scrape**(): `Promise`<`CheerioAPI`\>

#### Returns[](#returns-3 "Direct link to Returns")

`Promise`<`CheerioAPI`\>

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[CheerioWebBaseLoader](/docs/api/document_loaders_web_cheerio/classes/CheerioWebBaseLoader).[scrape](/docs/api/document_loaders_web_cheerio/classes/CheerioWebBaseLoader#scrape)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/document\_loaders/web/cheerio.ts:63](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/cheerio.ts#L63)

### \_scrape()[](#_scrape "Direct link to _scrape")

> `Static` **\_scrape**(`url`: `string`, `caller`: `AsyncCaller`, `timeout`: `undefined` | `number`, `textDecoder`?: `TextDecoder`): `Promise`<`CheerioAPI`\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

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

#### Returns[](#returns-4 "Direct link to Returns")

`Promise`<`CheerioAPI`\>

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

[CheerioWebBaseLoader](/docs/api/document_loaders_web_cheerio/classes/CheerioWebBaseLoader).[\_scrape](/docs/api/document_loaders_web_cheerio/classes/CheerioWebBaseLoader#_scrape)

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/document\_loaders/web/cheerio.ts:46](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/cheerio.ts#L46)

### imports()[](#imports "Direct link to imports()")

> `Static` **imports**(): `Promise`<{`load`: (`content`: `string` | `Buffer` | `AnyNode` | `AnyNode`\[\], `options?`: null | `CheerioOptions`, `isDocument?`: `boolean`) => `CheerioAPI`;}\>

#### Returns[](#returns-5 "Direct link to Returns")

`Promise`<{`load`: (`content`: `string` | `Buffer` | `AnyNode` | `AnyNode`\[\], `options?`: null | `CheerioOptions`, `isDocument?`: `boolean`) => `CheerioAPI`;}\>

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

[CheerioWebBaseLoader](/docs/api/document_loaders_web_cheerio/classes/CheerioWebBaseLoader).[imports](/docs/api/document_loaders_web_cheerio/classes/CheerioWebBaseLoader#imports)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/document\_loaders/web/cheerio.ts:79](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/cheerio.ts#L79)