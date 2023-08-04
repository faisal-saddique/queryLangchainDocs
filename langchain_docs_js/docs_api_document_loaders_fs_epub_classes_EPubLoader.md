EPubLoader
==========

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseDocumentLoader`](/docs/api/document_loaders_base/classes/BaseDocumentLoader).**EPubLoader**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new EPubLoader**(`filePath`: `string`, «destructured»: `object` = `{}`): [`EPubLoader`](/docs/api/document_loaders_fs_epub/classes/EPubLoader)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`filePath`

`string`

`«destructured»`

`object`

› `splitChapters`

`undefined` | `boolean`

#### Returns[](#returns "Direct link to Returns")

[`EPubLoader`](/docs/api/document_loaders_fs_epub/classes/EPubLoader)

#### Overrides[](#overrides "Direct link to Overrides")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[constructor](/docs/api/document_loaders_base/classes/BaseDocumentLoader#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/document\_loaders/fs/epub.ts:8](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/fs/epub.ts#L8)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### filePath[](#filepath "Direct link to filePath")

> **filePath**: `string`

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/epub.ts:8](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/fs/epub.ts#L8)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### load()[](#load "Direct link to load()")

> **load**(): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Returns[](#returns-1 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Overrides[](#overrides-1 "Direct link to Overrides")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[load](/docs/api/document_loaders_base/classes/BaseDocumentLoader#load)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/epub.ts:36](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/fs/epub.ts#L36)

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

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/document\_loaders/base.ts:15](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/base.ts#L15)

### parse()[](#parse "Direct link to parse()")

> `Protected` **parse**(`epub`: `EPub`): `Promise`<{`pageContent`: `string`; `metadata`?: `object`;}\[\]\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`epub`

`EPub`

#### Returns[](#returns-3 "Direct link to Returns")

`Promise`<{`pageContent`: `string`; `metadata`?: `object`;}\[\]\>

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/epub.ts:13](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/fs/epub.ts#L13)