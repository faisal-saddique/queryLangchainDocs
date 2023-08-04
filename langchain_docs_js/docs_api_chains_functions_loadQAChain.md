loadQAChain()
=============

> **loadQAChain**(`llm`: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>, `params`: [`QAChainParams`](/docs/api/chains/types/QAChainParams) = `...`): [`StuffDocumentsChain`](/docs/api/chains/classes/StuffDocumentsChain) | [`MapReduceDocumentsChain`](/docs/api/chains/classes/MapReduceDocumentsChain) | [`RefineDocumentsChain`](/docs/api/chains/classes/RefineDocumentsChain)

Parameters[](#parameters "Direct link to Parameters")
------------------------------------------------------

Parameter

Type

`llm`

[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>

`params`

[`QAChainParams`](/docs/api/chains/types/QAChainParams)

Returns[](#returns "Direct link to Returns")
---------------------------------------------

[`StuffDocumentsChain`](/docs/api/chains/classes/StuffDocumentsChain) | [`MapReduceDocumentsChain`](/docs/api/chains/classes/MapReduceDocumentsChain) | [`RefineDocumentsChain`](/docs/api/chains/classes/RefineDocumentsChain)

Defined in[](#defined-in "Direct link to Defined in")
------------------------------------------------------

[langchain/src/chains/question\_answering/load.ts:31](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/question_answering/load.ts#L31)