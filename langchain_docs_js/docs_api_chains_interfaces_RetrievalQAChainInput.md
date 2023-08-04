RetrievalQAChainInput
=====================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   `Omit`<[`ChainInputs`](/docs/api/chains/interfaces/ChainInputs), "memory"\>.**RetrievalQAChainInput**

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### combineDocumentsChain[](#combinedocumentschain "Direct link to combineDocumentsChain")

> **combineDocumentsChain**: [`BaseChain`](/docs/api/chains/classes/BaseChain)<[`ChainValues`](/docs/api/schema/types/ChainValues), [`ChainValues`](/docs/api/schema/types/ChainValues)\>

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/chains/retrieval\_qa.ts:17](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/retrieval_qa.ts#L17)

### retriever[](#retriever "Direct link to retriever")

> **retriever**: [`BaseRetriever`](/docs/api/schema_retriever/classes/BaseRetriever)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/chains/retrieval\_qa.ts:16](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/retrieval_qa.ts#L16)

### callbackManager?[](#callbackmanager "Direct link to callbackManager?")

> **callbackManager**: [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Deprecated[](#deprecated "Direct link to Deprecated")

Use `callbacks` instead

#### Inherited from[](#inherited-from "Direct link to Inherited from")

Omit.callbackManager

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/chains/base.ts:22](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L22)

### callbacks?[](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

Omit.callbacks

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:25](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L25)

### inputKey?[](#inputkey "Direct link to inputKey?")

> **inputKey**: `string`

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/chains/retrieval\_qa.ts:18](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/retrieval_qa.ts#L18)

### metadata?[](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

Omit.metadata

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:27](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L27)

### returnSourceDocuments?[](#returnsourcedocuments "Direct link to returnSourceDocuments?")

> **returnSourceDocuments**: `boolean`

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/chains/retrieval\_qa.ts:19](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/retrieval_qa.ts#L19)

### tags?[](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

Omit.tags

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L26)

### verbose?[](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

Omit.verbose

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:24](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L24)