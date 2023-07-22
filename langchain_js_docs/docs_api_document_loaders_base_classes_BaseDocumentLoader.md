BaseDocumentLoader
==================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`ApifyDatasetLoader`](/docs/api/document_loaders_web_apify_dataset/classes/ApifyDatasetLoader)
*   [`CheerioWebBaseLoader`](/docs/api/document_loaders_web_cheerio/classes/CheerioWebBaseLoader)
*   [`PuppeteerWebBaseLoader`](/docs/api/document_loaders_web_puppeteer/classes/PuppeteerWebBaseLoader)
*   [`PlaywrightWebBaseLoader`](/docs/api/document_loaders_web_playwright/classes/PlaywrightWebBaseLoader)
*   [`FigmaFileLoader`](/docs/api/document_loaders_web_figma/classes/FigmaFileLoader)
*   [`GithubRepoLoader`](/docs/api/document_loaders_web_github/classes/GithubRepoLoader)
*   [`NotionDBLoader`](/docs/api/document_loaders_web_notiondb/classes/NotionDBLoader)
*   [`NotionAPILoader`](/docs/api/document_loaders_web_notionapi/classes/NotionAPILoader)
*   [`S3Loader`](/docs/api/document_loaders_web_s3/classes/S3Loader)
*   [`SonixAudioTranscriptionLoader`](/docs/api/document_loaders_web_sonix_audio/classes/SonixAudioTranscriptionLoader)
*   [`ConfluencePagesLoader`](/docs/api/document_loaders_web_confluence/classes/ConfluencePagesLoader)
*   [`SerpAPILoader`](/docs/api/document_loaders_web_serpapi/classes/SerpAPILoader)
*   [`SortXYZBlockchainLoader`](/docs/api/document_loaders_web_sort_xyz_blockchain/classes/SortXYZBlockchainLoader)
*   [`DirectoryLoader`](/docs/api/document_loaders_fs_directory/classes/DirectoryLoader)
*   [`BufferLoader`](/docs/api/document_loaders_fs_buffer/classes/BufferLoader)
*   [`TextLoader`](/docs/api/document_loaders_fs_text/classes/TextLoader)
*   [`EPubLoader`](/docs/api/document_loaders_fs_epub/classes/EPubLoader)
*   [`UnstructuredLoader`](/docs/api/document_loaders_fs_unstructured/classes/UnstructuredLoader)

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   [`DocumentLoader`](/docs/api/document_loaders_base/interfaces/DocumentLoader)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new BaseDocumentLoader**(): [`BaseDocumentLoader`](/docs/api/document_loaders_base/classes/BaseDocumentLoader)

#### Returns[​](#returns "Direct link to Returns")

[`BaseDocumentLoader`](/docs/api/document_loaders_base/classes/BaseDocumentLoader)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### load()[​](#load "Direct link to load()")

> `Abstract` **load**(): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Returns[​](#returns-1 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

[DocumentLoader](/docs/api/document_loaders_base/interfaces/DocumentLoader).[load](/docs/api/document_loaders_base/interfaces/DocumentLoader#load)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/document\_loaders/base.ts:13](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/base.ts#L13)

### loadAndSplit()[​](#loadandsplit "Direct link to loadAndSplit()")

> **loadAndSplit**(`splitter`: [`TextSplitter`](/docs/api/text_splitter/classes/TextSplitter) = `...`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`splitter`

[`TextSplitter`](/docs/api/text_splitter/classes/TextSplitter)

#### Returns[​](#returns-2 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

[DocumentLoader](/docs/api/document_loaders_base/interfaces/DocumentLoader).[loadAndSplit](/docs/api/document_loaders_base/interfaces/DocumentLoader#loadandsplit)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/document\_loaders/base.ts:15](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/base.ts#L15)