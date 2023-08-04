GithubRepoLoader
================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseDocumentLoader`](/docs/api/document_loaders_base/classes/BaseDocumentLoader).**GithubRepoLoader**

Implements[](#implements "Direct link to Implements")
------------------------------------------------------

*   [`GithubRepoLoaderParams`](/docs/api/document_loaders_web_github/interfaces/GithubRepoLoaderParams)

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new GithubRepoLoader**(`githubUrl`: `string`, «destructured»: [`GithubRepoLoaderParams`](/docs/api/document_loaders_web_github/interfaces/GithubRepoLoaderParams) = `{}`): [`GithubRepoLoader`](/docs/api/document_loaders_web_github/classes/GithubRepoLoader)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`githubUrl`

`string`

`«destructured»`

[`GithubRepoLoaderParams`](/docs/api/document_loaders_web_github/interfaces/GithubRepoLoaderParams)

#### Returns[](#returns "Direct link to Returns")

[`GithubRepoLoader`](/docs/api/document_loaders_web_github/classes/GithubRepoLoader)

#### Overrides[](#overrides "Direct link to Overrides")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[constructor](/docs/api/document_loaders_base/classes/BaseDocumentLoader#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/document\_loaders/web/github.ts:65](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/github.ts#L65)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### branch[](#branch "Direct link to branch")

> **branch**: `string`

#### Implementation of[](#implementation-of "Direct link to Implementation of")

[GithubRepoLoaderParams](/docs/api/document_loaders_web_github/interfaces/GithubRepoLoaderParams).[branch](/docs/api/document_loaders_web_github/interfaces/GithubRepoLoaderParams#branch)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/document\_loaders/web/github.ts:53](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/github.ts#L53)

### ignoreFiles[](#ignorefiles "Direct link to ignoreFiles")

> **ignoreFiles**: (`string` | `RegExp`)\[\]

#### Implementation of[](#implementation-of-1 "Direct link to Implementation of")

[GithubRepoLoaderParams](/docs/api/document_loaders_web_github/interfaces/GithubRepoLoaderParams).[ignoreFiles](/docs/api/document_loaders_web_github/interfaces/GithubRepoLoaderParams#ignorefiles)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/document\_loaders/web/github.ts:61](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/github.ts#L61)

### recursive[](#recursive "Direct link to recursive")

> **recursive**: `boolean`

#### Implementation of[](#implementation-of-2 "Direct link to Implementation of")

[GithubRepoLoaderParams](/docs/api/document_loaders_web_github/interfaces/GithubRepoLoaderParams).[recursive](/docs/api/document_loaders_web_github/interfaces/GithubRepoLoaderParams#recursive)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/document\_loaders/web/github.ts:55](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/github.ts#L55)

### unknown[](#unknown "Direct link to unknown")

> **unknown**: [`UnknownHandling`](/docs/api/document_loaders_fs_directory/variables/UnknownHandling)

#### Implementation of[](#implementation-of-3 "Direct link to Implementation of")

[GithubRepoLoaderParams](/docs/api/document_loaders_web_github/interfaces/GithubRepoLoaderParams).[unknown](/docs/api/document_loaders_web_github/interfaces/GithubRepoLoaderParams#unknown)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/document\_loaders/web/github.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/github.ts#L57)

### accessToken?[](#accesstoken "Direct link to accessToken?")

> **accessToken**: `string`

#### Implementation of[](#implementation-of-4 "Direct link to Implementation of")

[GithubRepoLoaderParams](/docs/api/document_loaders_web_github/interfaces/GithubRepoLoaderParams).[accessToken](/docs/api/document_loaders_web_github/interfaces/GithubRepoLoaderParams#accesstoken)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/document\_loaders/web/github.ts:59](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/github.ts#L59)

### ignore?[](#ignore "Direct link to ignore?")

> **ignore**: `Ignore`

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/document\_loaders/web/github.ts:63](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/github.ts#L63)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### load()[](#load "Direct link to load()")

> **load**(): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Returns[](#returns-1 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Overrides[](#overrides-1 "Direct link to Overrides")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[load](/docs/api/document_loaders_base/classes/BaseDocumentLoader#load)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/document\_loaders/web/github.ts:112](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/github.ts#L112)

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

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/document\_loaders/base.ts:15](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/base.ts#L15)

### shouldIgnore()[](#shouldignore "Direct link to shouldIgnore()")

> `Protected` **shouldIgnore**(`path`: `string`, `fileType`: `string`): `Promise`<`boolean`\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`path`

`string`

`fileType`

`string`

#### Returns[](#returns-3 "Direct link to Returns")

`Promise`<`boolean`\>

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/document\_loaders/web/github.ts:118](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/github.ts#L118)