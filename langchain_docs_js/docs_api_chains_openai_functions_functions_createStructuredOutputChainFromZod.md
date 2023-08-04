createStructuredOutputChainFromZod()
====================================

> **createStructuredOutputChainFromZod**<T\>(`zodSchema`: `T`, `input`: `Omit`<[`StructuredOutputChainInput`](/docs/api/chains_openai_functions/types/StructuredOutputChainInput), "outputSchema"\>): [`LLMChain`](/docs/api/chains/classes/LLMChain)<`any`, [`ChatOpenAI`](/docs/api/chat_models_openai/classes/ChatOpenAI)\>

Type parameters[](#type-parameters "Direct link to Type parameters")
---------------------------------------------------------------------

*   `T` _extends_ `ZodObject`<`any`, `any`, `any`, {}, {}, `T`\>

Parameters[](#parameters "Direct link to Parameters")
------------------------------------------------------

Parameter

Type

`zodSchema`

`T`

`input`

`Omit`<[`StructuredOutputChainInput`](/docs/api/chains_openai_functions/types/StructuredOutputChainInput), "outputSchema"\>

Returns[](#returns "Direct link to Returns")
---------------------------------------------

[`LLMChain`](/docs/api/chains/classes/LLMChain)<`any`, [`ChatOpenAI`](/docs/api/chat_models_openai/classes/ChatOpenAI)\>

Defined in[](#defined-in "Direct link to Defined in")
------------------------------------------------------

[langchain/src/chains/openai\_functions/structured\_output.ts:101](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/openai_functions/structured_output.ts#L101)