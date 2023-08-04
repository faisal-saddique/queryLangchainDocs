UnstructuredLoader
==================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseDocumentLoader`](/docs/api/document_loaders_base/classes/BaseDocumentLoader).**UnstructuredLoader**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new UnstructuredLoader**(`filePathOrLegacyApiUrl`: `string`, `optionsOrLegacyFilePath`: `string` | [`UnstructuredLoaderOptions`](/docs/api/document_loaders_fs_unstructured/types/UnstructuredLoaderOptions) = `{}`): [`UnstructuredLoader`](/docs/api/document_loaders_fs_unstructured/classes/UnstructuredLoader)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`filePathOrLegacyApiUrl`

`string`

`optionsOrLegacyFilePath`

`string` | [`UnstructuredLoaderOptions`](/docs/api/document_loaders_fs_unstructured/types/UnstructuredLoaderOptions)

#### Returns[](#returns "Direct link to Returns")

[`UnstructuredLoader`](/docs/api/document_loaders_fs_unstructured/classes/UnstructuredLoader)

#### Overrides[](#overrides "Direct link to Overrides")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[constructor](/docs/api/document_loaders_base/classes/BaseDocumentLoader#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/document\_loaders/fs/unstructured.ts:87](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/fs/unstructured.ts#L87)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### filePath[](#filepath "Direct link to filePath")

> **filePath**: `string`

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/unstructured.ts:68](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/fs/unstructured.ts#L68)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### \_partition()[](#_partition "Direct link to _partition")

> **\_partition**(): `Promise`<`Element`\[\]\>

#### Returns[](#returns-1 "Direct link to Returns")

`Promise`<`Element`\[\]\>

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/unstructured.ts:113](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/fs/unstructured.ts#L113)

### imports()[](#imports "Direct link to imports()")

> **imports**(): `Promise`<{`basename`: (`path`: `string`, `suffix?`: `string`) => `string`; `readFile`: (`path`: `PathLike` | `FileHandle`, `options?`: null | {} & `Abortable`) => `Promise`<`Buffer`\>(`path`: `PathLike` | `FileHandle`, `options`: {} & `Abortable` | `BufferEncoding`) => `Promise`<`string`\>(`path`: `PathLike` | `FileHandle`, `options?`: null | `BufferEncoding` | `ObjectEncodingOptions` & `Abortable` & {}) => `Promise`<`string` | `Buffer`\>;}\>

#### Returns[](#returns-2 "Direct link to Returns")

`Promise`<{`basename`: (`path`: `string`, `suffix?`: `string`) => `string`; `readFile`: (`path`: `PathLike` | `FileHandle`, `options?`: null | {} & `Abortable`) => `Promise`<`Buffer`\>(`path`: `PathLike` | `FileHandle`, `options`: {} & `Abortable` | `BufferEncoding`) => `Promise`<`string`\>(`path`: `PathLike` | `FileHandle`, `options?`: null | `BufferEncoding` | `ObjectEncodingOptions` & `Abortable` & {}) => `Promise`<`string` | `Buffer`\>;}\>

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/unstructured.ts:190](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/fs/unstructured.ts#L190)

### load()[](#load "Direct link to load()")

> **load**(): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Returns[](#returns-3 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Overrides[](#overrides-1 "Direct link to Overrides")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[load](/docs/api/document_loaders_base/classes/BaseDocumentLoader#load)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/unstructured.ts:168](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/fs/unstructured.ts#L168)

### loadAndSplit()[](#loadandsplit "Direct link to loadAndSplit()")

> **loadAndSplit**(`splitter`: [`TextSplitter`](/docs/api/text_splitter/classes/TextSplitter) = `...`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`splitter`

[`TextSplitter`](/docs/api/text_splitter/classes/TextSplitter)

#### Returns[](#returns-4 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[loadAndSplit](/docs/api/document_loaders_base/classes/BaseDocumentLoader#loadandsplit)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/document\_loaders/base.ts:15](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/base.ts#L15)