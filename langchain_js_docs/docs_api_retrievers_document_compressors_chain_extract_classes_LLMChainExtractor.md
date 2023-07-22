LLMChainExtractor
=================

Base Document Compression class. All compressors should extend this class.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseDocumentCompressor`](/docs/api/retrievers_document_compressors/classes/BaseDocumentCompressor).**LLMChainExtractor**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new LLMChainExtractor**(«destructured»: [`LLMChainExtractorArgs`](/docs/api/retrievers_document_compressors_chain_extract/interfaces/LLMChainExtractorArgs)): [`LLMChainExtractor`](/docs/api/retrievers_document_compressors_chain_extract/classes/LLMChainExtractor)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`«destructured»`

[`LLMChainExtractorArgs`](/docs/api/retrievers_document_compressors_chain_extract/interfaces/LLMChainExtractorArgs)

#### Returns[​](#returns "Direct link to Returns")

[`LLMChainExtractor`](/docs/api/retrievers_document_compressors_chain_extract/classes/LLMChainExtractor)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseDocumentCompressor](/docs/api/retrievers_document_compressors/classes/BaseDocumentCompressor).[constructor](/docs/api/retrievers_document_compressors/classes/BaseDocumentCompressor#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/retrievers/document\_compressors/chain\_extract.ts:60](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/document_compressors/chain_extract.ts#L60)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### getInput[​](#getinput "Direct link to getInput")

> **getInput**: `Function` = `defaultGetInput`

#### Type declaration[​](#type-declaration "Direct link to Type declaration")

> (`query`: `string`, `doc`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>): `Record`<`string`, `unknown`\>

##### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`query`

`string`

`doc`

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>

##### Returns[​](#returns-1 "Direct link to Returns")

`Record`<`string`, `unknown`\>

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/retrievers/document\_compressors/chain\_extract.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/document_compressors/chain_extract.ts#L57)

### llmChain[​](#llmchain "Direct link to llmChain")

> **llmChain**: [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/retrievers/document\_compressors/chain\_extract.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/document_compressors/chain_extract.ts#L55)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### compressDocuments()[​](#compressdocuments "Direct link to compressDocuments()")

> **compressDocuments**(`documents`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], `query`: `string`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`documents`

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

`query`

`string`

#### Returns[​](#returns-2 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[BaseDocumentCompressor](/docs/api/retrievers_document_compressors/classes/BaseDocumentCompressor).[compressDocuments](/docs/api/retrievers_document_compressors/classes/BaseDocumentCompressor#compressdocuments)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/retrievers/document\_compressors/chain\_extract.ts:66](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/document_compressors/chain_extract.ts#L66)

### fromLLM()[​](#fromllm "Direct link to fromLLM()")

> `Static` **fromLLM**(`llm`: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel), `prompt`?: [`PromptTemplate`](/docs/api/prompts/classes/PromptTemplate), `getInput`?: `Function`): [`LLMChainExtractor`](/docs/api/retrievers_document_compressors_chain_extract/classes/LLMChainExtractor)

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`llm`

[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)

`prompt?`

[`PromptTemplate`](/docs/api/prompts/classes/PromptTemplate)

`getInput?`

(`query`: `string`, `doc`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>) => `Record`<`string`, `unknown`\>

#### Returns[​](#returns-3 "Direct link to Returns")

[`LLMChainExtractor`](/docs/api/retrievers_document_compressors_chain_extract/classes/LLMChainExtractor)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/retrievers/document\_compressors/chain\_extract.ts:85](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/document_compressors/chain_extract.ts#L85)