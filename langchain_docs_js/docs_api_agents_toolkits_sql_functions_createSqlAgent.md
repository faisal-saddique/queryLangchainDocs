createSqlAgent()
================

> **createSqlAgent**(`llm`: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>, `toolkit`: [`SqlToolkit`](/docs/api/agents_toolkits_sql/classes/SqlToolkit), `args`?: [`SqlCreatePromptArgs`](/docs/api/agents_toolkits_sql/interfaces/SqlCreatePromptArgs)): [`AgentExecutor`](/docs/api/agents/classes/AgentExecutor)

Parameters[](#parameters "Direct link to Parameters")
------------------------------------------------------

Parameter

Type

`llm`

[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>

`toolkit`

[`SqlToolkit`](/docs/api/agents_toolkits_sql/classes/SqlToolkit)

`args?`

[`SqlCreatePromptArgs`](/docs/api/agents_toolkits_sql/interfaces/SqlCreatePromptArgs)

Returns[](#returns "Direct link to Returns")
---------------------------------------------

[`AgentExecutor`](/docs/api/agents/classes/AgentExecutor)

Defined in[](#defined-in "Direct link to Defined in")
------------------------------------------------------

[langchain/src/agents/toolkits/sql/sql.ts:41](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/toolkits/sql/sql.ts#L41)