NotionDBLoader
==============

Deprecated[](#deprecated "Direct link to Deprecated")
------------------------------------------------------

use the `NotionAPILoader` class instead.

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseDocumentLoader`](/docs/api/document_loaders_base/classes/BaseDocumentLoader).**NotionDBLoader**

Implements[](#implements "Direct link to Implements")
------------------------------------------------------

*   [`NotionDBLoaderParams`](/docs/api/document_loaders_web_notiondb/interfaces/NotionDBLoaderParams)

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new NotionDBLoader**(«destructured»: [`NotionDBLoaderParams`](/docs/api/document_loaders_web_notiondb/interfaces/NotionDBLoaderParams)): [`NotionDBLoader`](/docs/api/document_loaders_web_notiondb/classes/NotionDBLoader)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`«destructured»`

[`NotionDBLoaderParams`](/docs/api/document_loaders_web_notiondb/interfaces/NotionDBLoaderParams)

#### Returns[](#returns "Direct link to Returns")

[`NotionDBLoader`](/docs/api/document_loaders_web_notiondb/classes/NotionDBLoader)

#### Overrides[](#overrides "Direct link to Overrides")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[constructor](/docs/api/document_loaders_base/classes/BaseDocumentLoader#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/document\_loaders/web/notiondb.ts:47](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/notiondb.ts#L47)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### databaseId[](#databaseid "Direct link to databaseId")

> **databaseId**: `string`

#### Implementation of[](#implementation-of "Direct link to Implementation of")

[NotionDBLoaderParams](/docs/api/document_loaders_web_notiondb/interfaces/NotionDBLoaderParams).[databaseId](/docs/api/document_loaders_web_notiondb/interfaces/NotionDBLoaderParams#databaseid)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/document\_loaders/web/notiondb.ts:39](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/notiondb.ts#L39)

### integrationToken[](#integrationtoken "Direct link to integrationToken")

> **integrationToken**: `string`

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/document\_loaders/web/notiondb.ts:37](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/notiondb.ts#L37)

### notionApiVersion[](#notionapiversion "Direct link to notionApiVersion")

> **notionApiVersion**: `string`

#### Implementation of[](#implementation-of-1 "Direct link to Implementation of")

[NotionDBLoaderParams](/docs/api/document_loaders_web_notiondb/interfaces/NotionDBLoaderParams).[notionApiVersion](/docs/api/document_loaders_web_notiondb/interfaces/NotionDBLoaderParams#notionapiversion)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/document\_loaders/web/notiondb.ts:41](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/notiondb.ts#L41)

### pageSizeLimit[](#pagesizelimit "Direct link to pageSizeLimit")

> **pageSizeLimit**: `number`

#### Implementation of[](#implementation-of-2 "Direct link to Implementation of")

[NotionDBLoaderParams](/docs/api/document_loaders_web_notiondb/interfaces/NotionDBLoaderParams).[pageSizeLimit](/docs/api/document_loaders_web_notiondb/interfaces/NotionDBLoaderParams#pagesizelimit)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/document\_loaders/web/notiondb.ts:43](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/notiondb.ts#L43)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### load()[](#load "Direct link to load()")

> **load**(): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Returns[](#returns-1 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Overrides[](#overrides-1 "Direct link to Overrides")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[load](/docs/api/document_loaders_base/classes/BaseDocumentLoader#load)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/document\_loaders/web/notiondb.ts:71](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/notiondb.ts#L71)

### loadAndSplit()[](#loadandsplit "Direct link to loadAndSplit()")

> **loadAndSplit**(`splitter`: [`TextSplitter`](/docs/api/text_splitter/classes/TextSplitter) = `...`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`splitter`

[`TextSplitter`](/docs/api/text_splitter/classes/TextSplitter)

#### Returns[](#returns-2 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[loadAndSplit](/docs/api/document_loaders_base/classes/BaseDocumentLoader#loadandsplit)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/document\_loaders/base.ts:15](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/base.ts#L15)