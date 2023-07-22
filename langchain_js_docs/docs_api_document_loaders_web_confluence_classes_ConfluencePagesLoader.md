ConfluencePagesLoader
=====================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseDocumentLoader`](/docs/api/document_loaders_base/classes/BaseDocumentLoader).**ConfluencePagesLoader**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new ConfluencePagesLoader**(«destructured»: [`ConfluencePagesLoaderParams`](/docs/api/document_loaders_web_confluence/interfaces/ConfluencePagesLoaderParams)): [`ConfluencePagesLoader`](/docs/api/document_loaders_web_confluence/classes/ConfluencePagesLoader)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`«destructured»`

[`ConfluencePagesLoaderParams`](/docs/api/document_loaders_web_confluence/interfaces/ConfluencePagesLoaderParams)

#### Returns[​](#returns "Direct link to Returns")

[`ConfluencePagesLoader`](/docs/api/document_loaders_web_confluence/classes/ConfluencePagesLoader)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[constructor](/docs/api/document_loaders_base/classes/BaseDocumentLoader#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/document\_loaders/web/confluence.ts:39](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/confluence.ts#L39)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### accessToken[​](#accesstoken "Direct link to accessToken")

> `Readonly` **accessToken**: `string`

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/document\_loaders/web/confluence.ts:35](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/confluence.ts#L35)

### baseUrl[​](#baseurl "Direct link to baseUrl")

> `Readonly` **baseUrl**: `string`

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/document\_loaders/web/confluence.ts:29](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/confluence.ts#L29)

### limit[​](#limit "Direct link to limit")

> `Readonly` **limit**: `number`

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/document\_loaders/web/confluence.ts:37](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/confluence.ts#L37)

### spaceKey[​](#spacekey "Direct link to spaceKey")

> `Readonly` **spaceKey**: `string`

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/document\_loaders/web/confluence.ts:31](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/confluence.ts#L31)

### username[​](#username "Direct link to username")

> `Readonly` **username**: `string`

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/document\_loaders/web/confluence.ts:33](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/confluence.ts#L33)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### load()[​](#load "Direct link to load()")

> **load**(): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Returns[​](#returns-1 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[load](/docs/api/document_loaders_base/classes/BaseDocumentLoader#load)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/document\_loaders/web/confluence.ts:54](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/confluence.ts#L54)

### loadAndSplit()[​](#loadandsplit "Direct link to loadAndSplit()")

> **loadAndSplit**(`splitter`: [`TextSplitter`](/docs/api/text_splitter/classes/TextSplitter) = `...`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`splitter`

[`TextSplitter`](/docs/api/text_splitter/classes/TextSplitter)

#### Returns[​](#returns-2 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[loadAndSplit](/docs/api/document_loaders_base/classes/BaseDocumentLoader#loadandsplit)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/document\_loaders/base.ts:15](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/base.ts#L15)

### fetchConfluenceData()[​](#fetchconfluencedata "Direct link to fetchConfluenceData()")

> `Protected` **fetchConfluenceData**(`url`: `string`): `Promise`<[`ConfluenceAPIResponse`](/docs/api/document_loaders_web_confluence/interfaces/ConfluenceAPIResponse)\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`url`

`string`

#### Returns[​](#returns-3 "Direct link to Returns")

`Promise`<[`ConfluenceAPIResponse`](/docs/api/document_loaders_web_confluence/interfaces/ConfluenceAPIResponse)\>

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/document\_loaders/web/confluence.ts:64](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/confluence.ts#L64)