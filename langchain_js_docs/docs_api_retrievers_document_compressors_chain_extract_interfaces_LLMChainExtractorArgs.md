LLMChainExtractorArgs
=====================

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### getInput[​](#getinput "Direct link to getInput")

> **getInput**: `Function`

#### Type declaration[​](#type-declaration "Direct link to Type declaration")

> (`query`: `string`, `doc`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>): `Record`<`string`, `unknown`\>

##### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`query`

`string`

`doc`

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>

##### Returns[​](#returns "Direct link to Returns")

`Record`<`string`, `unknown`\>

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/retrievers/document\_compressors/chain\_extract.ts:51](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/document_compressors/chain_extract.ts#L51)

### llmChain[​](#llmchain "Direct link to llmChain")

> **llmChain**: [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/retrievers/document\_compressors/chain\_extract.ts:50](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/document_compressors/chain_extract.ts#L50)