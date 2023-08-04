createConversationalRetrievalAgent()
====================================

> **createConversationalRetrievalAgent**(`llm`: [`ChatOpenAI`](/docs/api/chat_models_openai/classes/ChatOpenAI), `tools`: [`StructuredTool`](/docs/api/tools/classes/StructuredTool)<`ZodObject`<`any`, `any`, `any`, `any`, {}\>\>\[\], `options`?: [`ConversationalRetrievalAgentOptions`](/docs/api/agents_toolkits/types/ConversationalRetrievalAgentOptions)): `Promise`<[`AgentExecutor`](/docs/api/agents/classes/AgentExecutor)\>

Parameters[](#parameters "Direct link to Parameters")
------------------------------------------------------

Parameter

Type

`llm`

[`ChatOpenAI`](/docs/api/chat_models_openai/classes/ChatOpenAI)

`tools`

[`StructuredTool`](/docs/api/tools/classes/StructuredTool)<`ZodObject`<`any`, `any`, `any`, `any`, {}\>\>\[\]

`options?`

[`ConversationalRetrievalAgentOptions`](/docs/api/agents_toolkits/types/ConversationalRetrievalAgentOptions)

Returns[](#returns "Direct link to Returns")
---------------------------------------------

`Promise`<[`AgentExecutor`](/docs/api/agents/classes/AgentExecutor)\>

Defined in[](#defined-in "Direct link to Defined in")
------------------------------------------------------

[langchain/src/agents/toolkits/conversational\_retrieval/openai\_functions.ts:15](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/toolkits/conversational_retrieval/openai_functions.ts#L15)