createAWSSfnAgent()
===================

> **createAWSSfnAgent**(`llm`: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>, `toolkit`: [`AWSSfnToolkit`](/docs/api/agents_toolkits_aws_sfn/classes/AWSSfnToolkit), `args`?: [`AWSSfnCreatePromptArgs`](/docs/api/agents_toolkits_aws_sfn/interfaces/AWSSfnCreatePromptArgs)): [`AgentExecutor`](/docs/api/agents/classes/AgentExecutor)

Parameters[](#parameters "Direct link to Parameters")
------------------------------------------------------

Parameter

Type

`llm`

[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>

`toolkit`

[`AWSSfnToolkit`](/docs/api/agents_toolkits_aws_sfn/classes/AWSSfnToolkit)

`args?`

[`AWSSfnCreatePromptArgs`](/docs/api/agents_toolkits_aws_sfn/interfaces/AWSSfnCreatePromptArgs)

Returns[](#returns "Direct link to Returns")
---------------------------------------------

[`AgentExecutor`](/docs/api/agents/classes/AgentExecutor)

Defined in[](#defined-in "Direct link to Defined in")
------------------------------------------------------

[langchain/src/agents/toolkits/aws\_sfn.ts:87](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/toolkits/aws_sfn.ts#L87)