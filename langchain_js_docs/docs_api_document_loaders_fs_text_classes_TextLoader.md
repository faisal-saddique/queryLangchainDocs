TextLoader
==========

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseDocumentLoader`](/docs/api/document_loaders_base/classes/BaseDocumentLoader).**TextLoader**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new TextLoader**(`filePathOrBlob`: `string` | `Blob`): [`TextLoader`](/docs/api/document_loaders_fs_text/classes/TextLoader)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`filePathOrBlob`

`string` | `Blob`

#### Returns[​](#returns "Direct link to Returns")

[`TextLoader`](/docs/api/document_loaders_fs_text/classes/TextLoader)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[constructor](/docs/api/document_loaders_base/classes/BaseDocumentLoader#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/document\_loaders/fs/text.ts:7](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/fs/text.ts#L7)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### filePathOrBlob[​](#filepathorblob "Direct link to filePathOrBlob")

> **filePathOrBlob**: `string` | `Blob`

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/text.ts:7](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/fs/text.ts#L7)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### load()[​](#load "Direct link to load()")

> **load**(): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Returns[​](#returns-1 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[load](/docs/api/document_loaders_base/classes/BaseDocumentLoader#load)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/text.ts:15](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/fs/text.ts#L15)

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

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/document\_loaders/base.ts:15](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/base.ts#L15)

### imports()[​](#imports "Direct link to imports()")

> `Static` **imports**(): `Promise`<{`readFile`: (`path`: `PathLike` | `FileHandle`, `options?`: null | {} & `Abortable`) => `Promise`<`Buffer`\>(`path`: `PathLike` | `FileHandle`, `options`: {} & `Abortable` | `BufferEncoding`) => `Promise`<`string`\>(`path`: `PathLike` | `FileHandle`, `options?`: null | `BufferEncoding` | `ObjectEncodingOptions` & `Abortable` & {}) => `Promise`<`string` | `Buffer`\>;}\>

#### Returns[​](#returns-3 "Direct link to Returns")

`Promise`<{`readFile`: (`path`: `PathLike` | `FileHandle`, `options?`: null | {} & `Abortable`) => `Promise`<`Buffer`\>(`path`: `PathLike` | `FileHandle`, `options`: {} & `Abortable` | `BufferEncoding`) => `Promise`<`string`\>(`path`: `PathLike` | `FileHandle`, `options?`: null | `BufferEncoding` | `ObjectEncodingOptions` & `Abortable` & {}) => `Promise`<`string` | `Buffer`\>;}\>

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/text.ts:49](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/fs/text.ts#L49)

### parse()[​](#parse "Direct link to parse()")

> `Protected` **parse**(`raw`: `string`): `Promise`<`string`\[\]\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`raw`

`string`

#### Returns[​](#returns-4 "Direct link to Returns")

`Promise`<`string`\[\]\>

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/text.ts:11](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/fs/text.ts#L11)