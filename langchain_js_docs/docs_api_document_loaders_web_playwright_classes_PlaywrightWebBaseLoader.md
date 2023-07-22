PlaywrightWebBaseLoader
=======================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseDocumentLoader`](/docs/api/document_loaders_base/classes/BaseDocumentLoader).**PlaywrightWebBaseLoader**

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   [`DocumentLoader`](/docs/api/document_loaders_base/interfaces/DocumentLoader)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new PlaywrightWebBaseLoader**(`webPath`: `string`, `options`?: [`PlaywrightWebBaseLoaderOptions`](/docs/api/document_loaders_web_playwright/types/PlaywrightWebBaseLoaderOptions)): [`PlaywrightWebBaseLoader`](/docs/api/document_loaders_web_playwright/classes/PlaywrightWebBaseLoader)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`webPath`

`string`

`options?`

[`PlaywrightWebBaseLoaderOptions`](/docs/api/document_loaders_web_playwright/types/PlaywrightWebBaseLoaderOptions)

#### Returns[​](#returns "Direct link to Returns")

[`PlaywrightWebBaseLoader`](/docs/api/document_loaders_web_playwright/classes/PlaywrightWebBaseLoader)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[constructor](/docs/api/document_loaders_base/classes/BaseDocumentLoader#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/document\_loaders/web/playwright.ts:32](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/playwright.ts#L32)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### options[​](#options "Direct link to options")

> **options**: `undefined` | [`PlaywrightWebBaseLoaderOptions`](/docs/api/document_loaders_web_playwright/types/PlaywrightWebBaseLoaderOptions)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/document\_loaders/web/playwright.ts:30](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/playwright.ts#L30)

### webPath[​](#webpath "Direct link to webPath")

> **webPath**: `string`

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/document\_loaders/web/playwright.ts:33](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/playwright.ts#L33)

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

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/document\_loaders/web/playwright.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/playwright.ts#L70)

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

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/document\_loaders/base.ts:15](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/base.ts#L15)

### scrape()[​](#scrape "Direct link to scrape()")

> **scrape**(): `Promise`<`string`\>

#### Returns[​](#returns-3 "Direct link to Returns")

`Promise`<`string`\>

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/document\_loaders/web/playwright.ts:66](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/playwright.ts#L66)

### \_scrape()[​](#_scrape "Direct link to _scrape")

> `Static` **\_scrape**(`url`: `string`, `options`?: [`PlaywrightWebBaseLoaderOptions`](/docs/api/document_loaders_web_playwright/types/PlaywrightWebBaseLoaderOptions)): `Promise`<`string`\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`url`

`string`

`options?`

[`PlaywrightWebBaseLoaderOptions`](/docs/api/document_loaders_web_playwright/types/PlaywrightWebBaseLoaderOptions)

#### Returns[​](#returns-4 "Direct link to Returns")

`Promise`<`string`\>

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/document\_loaders/web/playwright.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/playwright.ts#L40)

### imports()[​](#imports "Direct link to imports()")

> `Static` **imports**(): `Promise`<{`chromium`: `BrowserType`<{}\>;}\>

#### Returns[​](#returns-5 "Direct link to Returns")

`Promise`<{`chromium`: `BrowserType`<{}\>;}\>

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/document\_loaders/web/playwright.ts:77](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/playwright.ts#L77)