createOpenApiAgent()
====================

> **createOpenApiAgent**(`llm`: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>, `openApiToolkit`: [`OpenApiToolkit`](/docs/api/agents/classes/OpenApiToolkit), `args`?: [`ZeroShotCreatePromptArgs`](/docs/api/agents/interfaces/ZeroShotCreatePromptArgs)): [`AgentExecutor`](/docs/api/agents/classes/AgentExecutor)

Parameters[](#parameters "Direct link to Parameters")
------------------------------------------------------

Parameter

Type

`llm`

[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>

`openApiToolkit`

[`OpenApiToolkit`](/docs/api/agents/classes/OpenApiToolkit)

`args?`

[`ZeroShotCreatePromptArgs`](/docs/api/agents/interfaces/ZeroShotCreatePromptArgs)

Returns[](#returns "Direct link to Returns")
---------------------------------------------

[`AgentExecutor`](/docs/api/agents/classes/AgentExecutor)

Defined in[](#defined-in "Direct link to Defined in")
------------------------------------------------------

[langchain/src/agents/toolkits/openapi/openapi.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/toolkits/openapi/openapi.ts#L48)