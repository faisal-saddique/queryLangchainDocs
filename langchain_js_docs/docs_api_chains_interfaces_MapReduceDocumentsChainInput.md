MapReduceDocumentsChainInput
============================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`StuffDocumentsChainInput`](/docs/api/chains/interfaces/StuffDocumentsChainInput).**MapReduceDocumentsChainInput**

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### combineDocumentChain[​](#combinedocumentchain "Direct link to combineDocumentChain")

> **combineDocumentChain**: [`StuffDocumentsChain`](/docs/api/chains/classes/StuffDocumentsChain)

Chain to use to combine results of applying llm\_chain to documents.

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:113](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/combine_docs_chain.ts#L113)

### llmChain[​](#llmchain "Direct link to llmChain")

> **llmChain**: [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>

LLM Wrapper to use after formatting documents

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[StuffDocumentsChainInput](/docs/api/chains/interfaces/StuffDocumentsChainInput).[llmChain](/docs/api/chains/interfaces/StuffDocumentsChainInput#llmchain)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:18](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/combine_docs_chain.ts#L18)

### callbackManager?[​](#callbackmanager "Direct link to callbackManager?")

> **callbackManager**: [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Deprecated[​](#deprecated "Direct link to Deprecated")

Use `callbacks` instead

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[StuffDocumentsChainInput](/docs/api/chains/interfaces/StuffDocumentsChainInput).[callbackManager](/docs/api/chains/interfaces/StuffDocumentsChainInput#callbackmanager)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/chains/base.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L22)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[StuffDocumentsChainInput](/docs/api/chains/interfaces/StuffDocumentsChainInput).[callbacks](/docs/api/chains/interfaces/StuffDocumentsChainInput#callbacks)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L23)

### documentVariableName?[​](#documentvariablename "Direct link to documentVariableName?")

> **documentVariableName**: `string`

Variable name in the LLM chain to put the documents in

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[StuffDocumentsChainInput](/docs/api/chains/interfaces/StuffDocumentsChainInput).[documentVariableName](/docs/api/chains/interfaces/StuffDocumentsChainInput#documentvariablename)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:21](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/combine_docs_chain.ts#L21)

### ensureMapStep?[​](#ensuremapstep "Direct link to ensureMapStep?")

> **ensureMapStep**: `boolean`

Ensures that the map step is taken regardless of max tokens

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:111](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/combine_docs_chain.ts#L111)

### inputKey?[​](#inputkey "Direct link to inputKey?")

> **inputKey**: `string`

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[StuffDocumentsChainInput](/docs/api/chains/interfaces/StuffDocumentsChainInput).[inputKey](/docs/api/chains/interfaces/StuffDocumentsChainInput#inputkey)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:19](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/combine_docs_chain.ts#L19)

### maxIterations?[​](#maxiterations "Direct link to maxIterations?")

> **maxIterations**: `number`

The maximum number of iterations to run through the map

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:109](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/combine_docs_chain.ts#L109)

### maxTokens?[​](#maxtokens "Direct link to maxTokens?")

> **maxTokens**: `number`

The maximum number of tokens before requiring to do the reduction

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:107](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/combine_docs_chain.ts#L107)

### memory?[​](#memory "Direct link to memory?")

> **memory**: [`BaseMemory`](/docs/api/memory/classes/BaseMemory)

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[StuffDocumentsChainInput](/docs/api/chains/interfaces/StuffDocumentsChainInput).[memory](/docs/api/chains/interfaces/StuffDocumentsChainInput#memory)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/chains/base.ts:17](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L17)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[StuffDocumentsChainInput](/docs/api/chains/interfaces/StuffDocumentsChainInput).[metadata](/docs/api/chains/interfaces/StuffDocumentsChainInput#metadata)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:25](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L25)

### returnIntermediateSteps?[​](#returnintermediatesteps "Direct link to returnIntermediateSteps?")

> **returnIntermediateSteps**: `boolean`

Return the results of the map steps in the output.

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:115](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/combine_docs_chain.ts#L115)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

[StuffDocumentsChainInput](/docs/api/chains/interfaces/StuffDocumentsChainInput).[tags](/docs/api/chains/interfaces/StuffDocumentsChainInput#tags)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:24](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L24)

### verbose?[​](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[StuffDocumentsChainInput](/docs/api/chains/interfaces/StuffDocumentsChainInput).[verbose](/docs/api/chains/interfaces/StuffDocumentsChainInput#verbose)

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L22)