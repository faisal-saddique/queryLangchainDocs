DirectoryLoader
===============

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseDocumentLoader`](/docs/api/document_loaders_base/classes/BaseDocumentLoader).**DirectoryLoader**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new DirectoryLoader**(`directoryPath`: `string`, `loaders`: [`LoadersMapping`](/docs/api/document_loaders_fs_directory/interfaces/LoadersMapping), `recursive`: `boolean` = `true`, `unknown`: [`UnknownHandling`](/docs/api/document_loaders_fs_directory/variables/UnknownHandling) = `UnknownHandling.Warn`): [`DirectoryLoader`](/docs/api/document_loaders_fs_directory/classes/DirectoryLoader)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

Default value

`directoryPath`

`string`

`undefined`

`loaders`

[`LoadersMapping`](/docs/api/document_loaders_fs_directory/interfaces/LoadersMapping)

`undefined`

`recursive`

`boolean`

`true`

`unknown`

[`UnknownHandling`](/docs/api/document_loaders_fs_directory/variables/UnknownHandling)

`UnknownHandling.Warn`

#### Returns[​](#returns "Direct link to Returns")

[`DirectoryLoader`](/docs/api/document_loaders_fs_directory/classes/DirectoryLoader)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[constructor](/docs/api/document_loaders_base/classes/BaseDocumentLoader#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/document\_loaders/fs/directory.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/fs/directory.ts#L23)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### directoryPath[​](#directorypath "Direct link to directoryPath")

> **directoryPath**: `string`

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/directory.ts:24](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/fs/directory.ts#L24)

### loaders[​](#loaders "Direct link to loaders")

> **loaders**: [`LoadersMapping`](/docs/api/document_loaders_fs_directory/interfaces/LoadersMapping)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/directory.ts:25](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/fs/directory.ts#L25)

### recursive[​](#recursive "Direct link to recursive")

> **recursive**: `boolean` = `true`

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/directory.ts:26](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/fs/directory.ts#L26)

### unknown[​](#unknown "Direct link to unknown")

> **unknown**: [`UnknownHandling`](/docs/api/document_loaders_fs_directory/variables/UnknownHandling) = `UnknownHandling.Warn`

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/directory.ts:27](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/fs/directory.ts#L27)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### load()[​](#load "Direct link to load()")

> **load**(): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Returns[​](#returns-1 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[load](/docs/api/document_loaders_base/classes/BaseDocumentLoader#load)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/directory.ts:43](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/fs/directory.ts#L43)

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

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/document\_loaders/base.ts:15](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/base.ts#L15)

### imports()[​](#imports "Direct link to imports()")

> `Static` **imports**(): `Promise`<{`extname`: (`path`: `string`) => `string`; `readdir`: (`path`: `PathLike`, `options?`: null | `BufferEncoding` | `ObjectEncodingOptions` & {}) => `Promise`<`string`\[\]\>(`path`: `PathLike`, `options`: "buffer" | {}) => `Promise`<`Buffer`\[\]\>(`path`: `PathLike`, `options?`: null | `BufferEncoding` | `ObjectEncodingOptions` & {}) => `Promise`<`string`\[\] | `Buffer`\[\]\>(`path`: `PathLike`, `options`: `ObjectEncodingOptions` & {}) => `Promise`<`Dirent`\[\]\>; `resolve`: (...`paths`: `string`\[\]) => `string`;}\>

#### Returns[​](#returns-3 "Direct link to Returns")

`Promise`<{`extname`: (`path`: `string`) => `string`; `readdir`: (`path`: `PathLike`, `options?`: null | `BufferEncoding` | `ObjectEncodingOptions` & {}) => `Promise`<`string`\[\]\>(`path`: `PathLike`, `options`: "buffer" | {}) => `Promise`<`Buffer`\[\]\>(`path`: `PathLike`, `options?`: null | `BufferEncoding` | `ObjectEncodingOptions` & {}) => `Promise`<`string`\[\] | `Buffer`\[\]\>(`path`: `PathLike`, `options`: `ObjectEncodingOptions` & {}) => `Promise`<`Dirent`\[\]\>; `resolve`: (...`paths`: `string`\[\]) => `string`;}\>

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/directory.ts:87](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/fs/directory.ts#L87)