BaseDocumentCompressor
======================

Base Document Compression class. All compressors should extend this class.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`LLMChainExtractor`](/docs/api/retrievers_document_compressors_chain_extract/classes/LLMChainExtractor)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new BaseDocumentCompressor**(): [`BaseDocumentCompressor`](/docs/api/retrievers_document_compressors/classes/BaseDocumentCompressor)

#### Returns[​](#returns "Direct link to Returns")

[`BaseDocumentCompressor`](/docs/api/retrievers_document_compressors/classes/BaseDocumentCompressor)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### compressDocuments()[​](#compressdocuments "Direct link to compressDocuments()")

> `Abstract` **compressDocuments**(`documents`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], `query`: `string`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`documents`

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

`query`

`string`

#### Returns[​](#returns-1 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/retrievers/document\_compressors/index.ts:7](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/document_compressors/index.ts#L7)