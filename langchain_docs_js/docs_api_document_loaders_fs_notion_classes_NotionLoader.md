NotionLoader
============

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`DirectoryLoader`](/docs/api/document_loaders_fs_directory/classes/DirectoryLoader).**NotionLoader**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new NotionLoader**(`directoryPath`: `string`): [`NotionLoader`](/docs/api/document_loaders_fs_notion/classes/NotionLoader)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`directoryPath`

`string`

#### Returns[](#returns "Direct link to Returns")

[`NotionLoader`](/docs/api/document_loaders_fs_notion/classes/NotionLoader)

#### Overrides[](#overrides "Direct link to Overrides")

[DirectoryLoader](/docs/api/document_loaders_fs_directory/classes/DirectoryLoader).[constructor](/docs/api/document_loaders_fs_directory/classes/DirectoryLoader#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/document\_loaders/fs/notion.ts:5](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/fs/notion.ts#L5)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### directoryPath[](#directorypath "Direct link to directoryPath")

> **directoryPath**: `string`

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[DirectoryLoader](/docs/api/document_loaders_fs_directory/classes/DirectoryLoader).[directoryPath](/docs/api/document_loaders_fs_directory/classes/DirectoryLoader#directorypath)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/directory.ts:24](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/fs/directory.ts#L24)

### loaders[](#loaders "Direct link to loaders")

> **loaders**: [`LoadersMapping`](/docs/api/document_loaders_fs_directory/interfaces/LoadersMapping)

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[DirectoryLoader](/docs/api/document_loaders_fs_directory/classes/DirectoryLoader).[loaders](/docs/api/document_loaders_fs_directory/classes/DirectoryLoader#loaders)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/directory.ts:25](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/fs/directory.ts#L25)

### recursive[](#recursive "Direct link to recursive")

> **recursive**: `boolean` = `true`

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[DirectoryLoader](/docs/api/document_loaders_fs_directory/classes/DirectoryLoader).[recursive](/docs/api/document_loaders_fs_directory/classes/DirectoryLoader#recursive)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/directory.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/fs/directory.ts#L26)

### unknown[](#unknown "Direct link to unknown")

> **unknown**: [`UnknownHandling`](/docs/api/document_loaders_fs_directory/variables/UnknownHandling) = `UnknownHandling.Warn`

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[DirectoryLoader](/docs/api/document_loaders_fs_directory/classes/DirectoryLoader).[unknown](/docs/api/document_loaders_fs_directory/classes/DirectoryLoader#unknown)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/directory.ts:27](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/fs/directory.ts#L27)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### load()[](#load "Direct link to load()")

> **load**(): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Returns[](#returns-1 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[DirectoryLoader](/docs/api/document_loaders_fs_directory/classes/DirectoryLoader).[load](/docs/api/document_loaders_fs_directory/classes/DirectoryLoader#load)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/directory.ts:43](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/fs/directory.ts#L43)

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

[DirectoryLoader](/docs/api/document_loaders_fs_directory/classes/DirectoryLoader).[loadAndSplit](/docs/api/document_loaders_fs_directory/classes/DirectoryLoader#loadandsplit)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/document\_loaders/base.ts:15](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/base.ts#L15)

### imports()[](#imports "Direct link to imports()")

> `Static` **imports**(): `Promise`<{`extname`: (`path`: `string`) => `string`; `readdir`: (`path`: `PathLike`, `options?`: null | `BufferEncoding` | `ObjectEncodingOptions` & {}) => `Promise`<`string`\[\]\>(`path`: `PathLike`, `options`: "buffer" | {}) => `Promise`<`Buffer`\[\]\>(`path`: `PathLike`, `options?`: null | `BufferEncoding` | `ObjectEncodingOptions` & {}) => `Promise`<`string`\[\] | `Buffer`\[\]\>(`path`: `PathLike`, `options`: `ObjectEncodingOptions` & {}) => `Promise`<`Dirent`\[\]\>; `resolve`: (...`paths`: `string`\[\]) => `string`;}\>

#### Returns[](#returns-3 "Direct link to Returns")

`Promise`<{`extname`: (`path`: `string`) => `string`; `readdir`: (`path`: `PathLike`, `options?`: null | `BufferEncoding` | `ObjectEncodingOptions` & {}) => `Promise`<`string`\[\]\>(`path`: `PathLike`, `options`: "buffer" | {}) => `Promise`<`Buffer`\[\]\>(`path`: `PathLike`, `options?`: null | `BufferEncoding` | `ObjectEncodingOptions` & {}) => `Promise`<`string`\[\] | `Buffer`\[\]\>(`path`: `PathLike`, `options`: `ObjectEncodingOptions` & {}) => `Promise`<`Dirent`\[\]\>; `resolve`: (...`paths`: `string`\[\]) => `string`;}\>

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[DirectoryLoader](/docs/api/document_loaders_fs_directory/classes/DirectoryLoader).[imports](/docs/api/document_loaders_fs_directory/classes/DirectoryLoader#imports)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/directory.ts:87](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/fs/directory.ts#L87)