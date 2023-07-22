ChatConversationalAgentOutputParserArgs
=======================================

> **ChatConversationalAgentOutputParserArgs**: `object`

Type declaration[​](#type-declaration "Direct link to Type declaration")
------------------------------------------------------------------------

Member

Type

`baseParser`?

[`ChatConversationalAgentOutputParser`](/docs/api/agents/classes/ChatConversationalAgentOutputParser)

`outputFixingParser`?

[`OutputFixingParser`](/docs/api/output_parsers/classes/OutputFixingParser)<[`AgentAction`](/docs/api/schema/types/AgentAction) | [`AgentFinish`](/docs/api/schema/types/AgentFinish)\>

`toolNames`?

`string`\[\]

Defined in[​](#defined-in "Direct link to Defined in")
------------------------------------------------------

[langchain/src/agents/chat\_convo/outputParser.ts:64](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/agents/chat_convo/outputParser.ts#L64)