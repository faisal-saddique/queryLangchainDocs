loadSummarizationChain()
========================

> **loadSummarizationChain**(`llm`: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>, `params`: [`SummarizationChainParams`](/docs/api/chains/interfaces/SummarizationChainParams) = `...`): [`StuffDocumentsChain`](/docs/api/chains/classes/StuffDocumentsChain) | [`MapReduceDocumentsChain`](/docs/api/chains/classes/MapReduceDocumentsChain) | [`RefineDocumentsChain`](/docs/api/chains/classes/RefineDocumentsChain)

Parameters[](#parameters "Direct link to Parameters")
------------------------------------------------------

Parameter

Type

`llm`

[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>

`params`

[`SummarizationChainParams`](/docs/api/chains/interfaces/SummarizationChainParams)

Returns[](#returns "Direct link to Returns")
---------------------------------------------

[`StuffDocumentsChain`](/docs/api/chains/classes/StuffDocumentsChain) | [`MapReduceDocumentsChain`](/docs/api/chains/classes/MapReduceDocumentsChain) | [`RefineDocumentsChain`](/docs/api/chains/classes/RefineDocumentsChain)

Defined in[](#defined-in "Direct link to Defined in")
------------------------------------------------------

[langchain/src/chains/summarization/load.ts:36](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/summarization/load.ts#L36)