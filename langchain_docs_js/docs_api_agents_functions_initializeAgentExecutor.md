initializeAgentExecutor()
=========================

Deprecated[](#deprecated "Direct link to Deprecated")
------------------------------------------------------

use initializeAgentExecutorWithOptions instead

> **initializeAgentExecutor**(`tools`: [`Tool`](/docs/api/tools/classes/Tool)\[\], `llm`: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>, `_agentType`?: `AgentType`, `_verbose`?: `boolean`, `_callbackManager`?: [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)): `Promise`<[`AgentExecutor`](/docs/api/agents/classes/AgentExecutor)\>

Parameters[](#parameters "Direct link to Parameters")
------------------------------------------------------

Parameter

Type

`tools`

[`Tool`](/docs/api/tools/classes/Tool)\[\]

`llm`

[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>

`_agentType?`

`AgentType`

`_verbose?`

`boolean`

`_callbackManager?`

[`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

Returns[](#returns "Direct link to Returns")
---------------------------------------------

`Promise`<[`AgentExecutor`](/docs/api/agents/classes/AgentExecutor)\>

Defined in[](#defined-in "Direct link to Defined in")
------------------------------------------------------

[langchain/src/agents/initialize.ts:20](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/initialize.ts#L20)