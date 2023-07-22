SortXYZBlockchainLoader
=======================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseDocumentLoader`](/docs/api/document_loaders_base/classes/BaseDocumentLoader).**SortXYZBlockchainLoader**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new SortXYZBlockchainLoader**(«destructured»: [`SortXYZBlockchainLoaderParams`](/docs/api/document_loaders_web_sort_xyz_blockchain/interfaces/SortXYZBlockchainLoaderParams)): [`SortXYZBlockchainLoader`](/docs/api/document_loaders_web_sort_xyz_blockchain/classes/SortXYZBlockchainLoader)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`«destructured»`

[`SortXYZBlockchainLoaderParams`](/docs/api/document_loaders_web_sort_xyz_blockchain/interfaces/SortXYZBlockchainLoaderParams)

#### Returns[​](#returns "Direct link to Returns")

[`SortXYZBlockchainLoader`](/docs/api/document_loaders_web_sort_xyz_blockchain/classes/SortXYZBlockchainLoader)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[constructor](/docs/api/document_loaders_base/classes/BaseDocumentLoader#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/document\_loaders/web/sort\_xyz\_blockchain.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/sort_xyz_blockchain.ts#L46)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### apiKey[​](#apikey "Direct link to apiKey")

> `Readonly` **apiKey**: `string`

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/document\_loaders/web/sort\_xyz\_blockchain.ts:38](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/sort_xyz_blockchain.ts#L38)

### blockchain[​](#blockchain "Direct link to blockchain")

> `Readonly` **blockchain**: `string`

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/document\_loaders/web/sort\_xyz\_blockchain.ts:36](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/sort_xyz_blockchain.ts#L36)

### contractAddress[​](#contractaddress "Direct link to contractAddress")

> `Readonly` **contractAddress**: `string`

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/document\_loaders/web/sort\_xyz\_blockchain.ts:34](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/sort_xyz_blockchain.ts#L34)

### limit[​](#limit "Direct link to limit")

> `Readonly` **limit**: `number`

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/document\_loaders/web/sort\_xyz\_blockchain.ts:44](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/sort_xyz_blockchain.ts#L44)

### queryType[​](#querytype "Direct link to queryType")

> `Readonly` **queryType**: `string`

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/document\_loaders/web/sort\_xyz\_blockchain.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/sort_xyz_blockchain.ts#L40)

### sql[​](#sql "Direct link to sql")

> `Readonly` **sql**: `string`

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/document\_loaders/web/sort\_xyz\_blockchain.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/sort_xyz_blockchain.ts#L42)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### load()[​](#load "Direct link to load()")

> **load**(): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Returns[​](#returns-1 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[load](/docs/api/document_loaders_base/classes/BaseDocumentLoader#load)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/document\_loaders/web/sort\_xyz\_blockchain.ts:67](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/sort_xyz_blockchain.ts#L67)

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

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/document\_loaders/base.ts:15](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/base.ts#L15)