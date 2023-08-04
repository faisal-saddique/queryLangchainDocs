DocxLoader
==========

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BufferLoader`](/docs/api/document_loaders_fs_buffer/classes/BufferLoader).**DocxLoader**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new DocxLoader**(`filePathOrBlob`: `string` | `Blob`): [`DocxLoader`](/docs/api/document_loaders_fs_docx/classes/DocxLoader)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`filePathOrBlob`

`string` | `Blob`

#### Returns[](#returns "Direct link to Returns")

[`DocxLoader`](/docs/api/document_loaders_fs_docx/classes/DocxLoader)

#### Overrides[](#overrides "Direct link to Overrides")

[BufferLoader](/docs/api/document_loaders_fs_buffer/classes/BufferLoader).[constructor](/docs/api/document_loaders_fs_buffer/classes/BufferLoader#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/document\_loaders/fs/docx.ts:5](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/fs/docx.ts#L5)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### filePathOrBlob[](#filepathorblob "Direct link to filePathOrBlob")

> **filePathOrBlob**: `string` | `Blob`

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BufferLoader](/docs/api/document_loaders_fs_buffer/classes/BufferLoader).[filePathOrBlob](/docs/api/document_loaders_fs_buffer/classes/BufferLoader#filepathorblob)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/buffer.ts:7](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/fs/buffer.ts#L7)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### load()[](#load "Direct link to load()")

> **load**(): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Returns[](#returns-1 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[BufferLoader](/docs/api/document_loaders_fs_buffer/classes/BufferLoader).[load](/docs/api/document_loaders_fs_buffer/classes/BufferLoader#load)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/buffer.ts:16](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/fs/buffer.ts#L16)

### loadAndSplit()[](#loadandsplit "Direct link to loadAndSplit()")

> **loadAndSplit**(`splitter`: [`TextSplitter`](/docs/api/text_splitter/classes/TextSplitter) = `...`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`splitter`

[`TextSplitter`](/docs/api/text_splitter/classes/TextSplitter)

#### Returns[](#returns-2 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[BufferLoader](/docs/api/document_loaders_fs_buffer/classes/BufferLoader).[loadAndSplit](/docs/api/document_loaders_fs_buffer/classes/BufferLoader#loadandsplit)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/document\_loaders/base.ts:15](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/base.ts#L15)

### parse()[](#parse "Direct link to parse()")

> **parse**(`raw`: `Buffer`, `metadata`: `Record`<`string`, `any`\>): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`raw`

`Buffer`

`metadata`

`Record`<`string`, `any`\>

#### Returns[](#returns-3 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Overrides[](#overrides-1 "Direct link to Overrides")

[BufferLoader](/docs/api/document_loaders_fs_buffer/classes/BufferLoader).[parse](/docs/api/document_loaders_fs_buffer/classes/BufferLoader#parse)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/docx.ts:9](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/fs/docx.ts#L9)

### imports()[](#imports "Direct link to imports()")

> `Static` **imports**(): `Promise`<{`readFile`: (`path`: `PathLike` | `FileHandle`, `options?`: null | {} & `Abortable`) => `Promise`<`Buffer`\>(`path`: `PathLike` | `FileHandle`, `options`: {} & `Abortable` | `BufferEncoding`) => `Promise`<`string`\>(`path`: `PathLike` | `FileHandle`, `options?`: null | `BufferEncoding` | `ObjectEncodingOptions` & `Abortable` & {}) => `Promise`<`string` | `Buffer`\>;}\>

#### Returns[](#returns-4 "Direct link to Returns")

`Promise`<{`readFile`: (`path`: `PathLike` | `FileHandle`, `options?`: null | {} & `Abortable`) => `Promise`<`Buffer`\>(`path`: `PathLike` | `FileHandle`, `options`: {} & `Abortable` | `BufferEncoding`) => `Promise`<`string`\>(`path`: `PathLike` | `FileHandle`, `options?`: null | `BufferEncoding` | `ObjectEncodingOptions` & `Abortable` & {}) => `Promise`<`string` | `Buffer`\>;}\>

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[BufferLoader](/docs/api/document_loaders_fs_buffer/classes/BufferLoader).[imports](/docs/api/document_loaders_fs_buffer/classes/BufferLoader#imports)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/buffer.ts:32](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/fs/buffer.ts#L32)