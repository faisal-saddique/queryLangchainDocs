SerializedAgentT<TType, FromLLMInput, ConstructorInput\>
========================================================

> **SerializedAgentT**: <`TType`, `FromLLMInput`, `ConstructorInput`\> {`_type`: `TType`; `llm_chain`?: [`SerializedLLMChain`](/docs/api/chains/types/SerializedLLMChain);} & {`load_from_llm_and_tools`: true;} & `FromLLMInput` | {`load_from_llm_and_tools`?: false;} & `ConstructorInput`

Type parameters[​](#type-parameters "Direct link to Type parameters")
---------------------------------------------------------------------

*   `TType` _extends_ `string` = `string`
*   `FromLLMInput` _extends_ `Record`<`string`, `unknown`\> = `Record`<`string`, `unknown`\>
*   `ConstructorInput` _extends_ [`AgentInput`](/docs/api/agents/interfaces/AgentInput) = [`AgentInput`](/docs/api/agents/interfaces/AgentInput)

Defined in[​](#defined-in "Direct link to Defined in")
------------------------------------------------------

[langchain/src/agents/types.ts:18](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/agents/types.ts#L18)