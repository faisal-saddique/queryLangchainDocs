AzureBlobStorageContainerLoader
===============================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseDocumentLoader`](/docs/api/document_loaders_base/classes/BaseDocumentLoader).**AzureBlobStorageContainerLoader**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new AzureBlobStorageContainerLoader**(«destructured»: `AzureBlobStorageContainerLoaderConfig`): [`AzureBlobStorageContainerLoader`](/docs/api/document_loaders_web_azure_blob_storage_container/classes/AzureBlobStorageContainerLoader)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`«destructured»`

`AzureBlobStorageContainerLoaderConfig`

#### Returns[](#returns "Direct link to Returns")

[`AzureBlobStorageContainerLoader`](/docs/api/document_loaders_web_azure_blob_storage_container/classes/AzureBlobStorageContainerLoader)

#### Overrides[](#overrides "Direct link to Overrides")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[constructor](/docs/api/document_loaders_base/classes/BaseDocumentLoader#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/document\_loaders/web/azure\_blob\_storage\_container.ts:24](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/azure_blob_storage_container.ts#L24)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### load()[](#load "Direct link to load()")

> **load**(): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Returns[](#returns-1 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Overrides[](#overrides-1 "Direct link to Overrides")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[load](/docs/api/document_loaders_base/classes/BaseDocumentLoader#load)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/document\_loaders/web/azure\_blob\_storage\_container.ts:34](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/azure_blob_storage_container.ts#L34)

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

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/document\_loaders/base.ts:15](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/base.ts#L15)