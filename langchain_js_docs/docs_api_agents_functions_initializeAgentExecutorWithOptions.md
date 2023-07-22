initializeAgentExecutorWithOptions()
====================================

Initialize an agent executor with options

> **initializeAgentExecutorWithOptions**(`tools`: [`StructuredTool`](/docs/api/tools/classes/StructuredTool)<`ZodObject`<`any`, `any`, `any`, `any`, {}\>\>\[\], `llm`: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel), `options`: `InitializeAgentExecutorOptionsStructured`): `Promise`<[`AgentExecutor`](/docs/api/agents/classes/AgentExecutor)\>

Parameters[​](#parameters "Direct link to Parameters")
------------------------------------------------------

Parameter

Type

Description

`tools`

[`StructuredTool`](/docs/api/tools/classes/StructuredTool)<`ZodObject`<`any`, `any`, `any`, `any`, {}\>\>\[\]

Array of tools to use in the agent

`llm`

[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)

LLM or ChatModel to use in the agent

`options`

`InitializeAgentExecutorOptionsStructured`

Options for the agent, including agentType, agentArgs, and other options for AgentExecutor.fromAgentAndTools

Returns[​](#returns "Direct link to Returns")
---------------------------------------------

`Promise`<[`AgentExecutor`](/docs/api/agents/classes/AgentExecutor)\>

AgentExecutor

Defined in[​](#defined-in "Direct link to Defined in")
------------------------------------------------------

[langchain/src/agents/initialize.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/agents/initialize.ts#L98)

> **initializeAgentExecutorWithOptions**(`tools`: [`Tool`](/docs/api/tools/classes/Tool)\[\], `llm`: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel), `options`?: [`InitializeAgentExecutorOptions`](/docs/api/agents/interfaces/InitializeAgentExecutorOptions)): `Promise`<[`AgentExecutor`](/docs/api/agents/classes/AgentExecutor)\>

Parameters[​](#parameters-1 "Direct link to Parameters")
--------------------------------------------------------

Parameter

Type

`tools`

[`Tool`](/docs/api/tools/classes/Tool)\[\]

`llm`

[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)

`options?`

[`InitializeAgentExecutorOptions`](/docs/api/agents/interfaces/InitializeAgentExecutorOptions)

Returns[​](#returns-1 "Direct link to Returns")
-----------------------------------------------

`Promise`<[`AgentExecutor`](/docs/api/agents/classes/AgentExecutor)\>

Defined in[​](#defined-in-1 "Direct link to Defined in")
--------------------------------------------------------

[langchain/src/agents/initialize.ts:103](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/agents/initialize.ts#L103)