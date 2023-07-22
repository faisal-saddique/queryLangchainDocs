loadSummarizationChain()
========================

> **loadSummarizationChain**(`llm`: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel), `params`: [`SummarizationChainParams`](/docs/api/chains/interfaces/SummarizationChainParams) = `...`): [`StuffDocumentsChain`](/docs/api/chains/classes/StuffDocumentsChain) | [`MapReduceDocumentsChain`](/docs/api/chains/classes/MapReduceDocumentsChain) | [`RefineDocumentsChain`](/docs/api/chains/classes/RefineDocumentsChain)

Parameters[​](#parameters "Direct link to Parameters")
------------------------------------------------------

Parameter

Type

`llm`

[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)

`params`

[`SummarizationChainParams`](/docs/api/chains/interfaces/SummarizationChainParams)

Returns[​](#returns "Direct link to Returns")
---------------------------------------------

[`StuffDocumentsChain`](/docs/api/chains/classes/StuffDocumentsChain) | [`MapReduceDocumentsChain`](/docs/api/chains/classes/MapReduceDocumentsChain) | [`RefineDocumentsChain`](/docs/api/chains/classes/RefineDocumentsChain)

Defined in[​](#defined-in "Direct link to Defined in")
------------------------------------------------------

[langchain/src/chains/summarization/load.ts:36](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/summarization/load.ts#L36)