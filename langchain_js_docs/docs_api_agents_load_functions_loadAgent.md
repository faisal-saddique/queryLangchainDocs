loadAgent()
===========

> **loadAgent**(`uri`: `string`, `llmAndTools`?: `object`): `Promise`<[`Agent`](/docs/api/agents/classes/Agent)\>

Parameters[​](#parameters "Direct link to Parameters")
------------------------------------------------------

Parameter

Type

`uri`

`string`

`llmAndTools?`

`object`

`llmAndTools.llm?`

[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)

`llmAndTools.tools?`

[`Tool`](/docs/api/tools/classes/Tool)\[\]

Returns[​](#returns "Direct link to Returns")
---------------------------------------------

`Promise`<[`Agent`](/docs/api/agents/classes/Agent)\>

Defined in[​](#defined-in "Direct link to Defined in")
------------------------------------------------------

[langchain/src/agents/load.ts:17](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/agents/load.ts#L17)