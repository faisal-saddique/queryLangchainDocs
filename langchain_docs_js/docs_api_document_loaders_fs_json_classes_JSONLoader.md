JSONLoader
==========

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`TextLoader`](/docs/api/document_loaders_fs_text/classes/TextLoader).**JSONLoader**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new JSONLoader**(`filePathOrBlob`: `string` | `Blob`, `pointers`: `string` | `string`\[\] = `[]`): [`JSONLoader`](/docs/api/document_loaders_fs_json/classes/JSONLoader)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

Default value

`filePathOrBlob`

`string` | `Blob`

`undefined`

`pointers`

`string` | `string`\[\]

`[]`

#### Returns[](#returns "Direct link to Returns")

[`JSONLoader`](/docs/api/document_loaders_fs_json/classes/JSONLoader)

#### Overrides[](#overrides "Direct link to Overrides")

[TextLoader](/docs/api/document_loaders_fs_text/classes/TextLoader).[constructor](/docs/api/document_loaders_fs_text/classes/TextLoader#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/document\_loaders/fs/json.ts:7](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/fs/json.ts#L7)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### filePathOrBlob[](#filepathorblob "Direct link to filePathOrBlob")

> **filePathOrBlob**: `string` | `Blob`

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[TextLoader](/docs/api/document_loaders_fs_text/classes/TextLoader).[filePathOrBlob](/docs/api/document_loaders_fs_text/classes/TextLoader#filepathorblob)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/text.ts:7](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/fs/text.ts#L7)

### pointers[](#pointers "Direct link to pointers")

> **pointers**: `string`\[\]

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/json.ts:5](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/fs/json.ts#L5)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### load()[](#load "Direct link to load()")

> **load**(): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Returns[](#returns-1 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[TextLoader](/docs/api/document_loaders_fs_text/classes/TextLoader).[load](/docs/api/document_loaders_fs_text/classes/TextLoader#load)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/text.ts:15](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/fs/text.ts#L15)

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

[TextLoader](/docs/api/document_loaders_fs_text/classes/TextLoader).[loadAndSplit](/docs/api/document_loaders_fs_text/classes/TextLoader#loadandsplit)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/document\_loaders/base.ts:15](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/base.ts#L15)

### imports()[](#imports "Direct link to imports()")

> `Static` **imports**(): `Promise`<{`readFile`: (`path`: `PathLike` | `FileHandle`, `options?`: null | {} & `Abortable`) => `Promise`<`Buffer`\>(`path`: `PathLike` | `FileHandle`, `options`: {} & `Abortable` | `BufferEncoding`) => `Promise`<`string`\>(`path`: `PathLike` | `FileHandle`, `options?`: null | `BufferEncoding` | `ObjectEncodingOptions` & `Abortable` & {}) => `Promise`<`string` | `Buffer`\>;}\>

#### Returns[](#returns-3 "Direct link to Returns")

`Promise`<{`readFile`: (`path`: `PathLike` | `FileHandle`, `options?`: null | {} & `Abortable`) => `Promise`<`Buffer`\>(`path`: `PathLike` | `FileHandle`, `options`: {} & `Abortable` | `BufferEncoding`) => `Promise`<`string`\>(`path`: `PathLike` | `FileHandle`, `options?`: null | `BufferEncoding` | `ObjectEncodingOptions` & `Abortable` & {}) => `Promise`<`string` | `Buffer`\>;}\>

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[TextLoader](/docs/api/document_loaders_fs_text/classes/TextLoader).[imports](/docs/api/document_loaders_fs_text/classes/TextLoader#imports)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/text.ts:49](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/fs/text.ts#L49)

### parse()[](#parse "Direct link to parse()")

> `Protected` **parse**(`raw`: `string`): `Promise`<`string`\[\]\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`raw`

`string`

#### Returns[](#returns-4 "Direct link to Returns")

`Promise`<`string`\[\]\>

#### Overrides[](#overrides-1 "Direct link to Overrides")

[TextLoader](/docs/api/document_loaders_fs_text/classes/TextLoader).[parse](/docs/api/document_loaders_fs_text/classes/TextLoader#parse)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/document\_loaders/fs/json.ts:12](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/fs/json.ts#L12)