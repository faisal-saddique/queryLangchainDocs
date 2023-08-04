createStructuredOutputChain()
=============================

Create a chain that returns output matching a JSON Schema.

> **createStructuredOutputChain**<T\>(`input`: [`StructuredOutputChainInput`](/docs/api/chains_openai_functions/types/StructuredOutputChainInput)): [`LLMChain`](/docs/api/chains/classes/LLMChain)<`any`, [`ChatOpenAI`](/docs/api/chat_models_openai/classes/ChatOpenAI)\>

Type parameters[](#type-parameters "Direct link to Type parameters")
---------------------------------------------------------------------

*   `T` _extends_ `ZodObject`<`any`, `any`, `any`, {}, {}, `T`\> = `AnyZodObject`

Parameters[](#parameters "Direct link to Parameters")
------------------------------------------------------

Parameter

Type

Description

`input`

[`StructuredOutputChainInput`](/docs/api/chains_openai_functions/types/StructuredOutputChainInput)

Object that includes all LLMChainInput fields except "outputParser"  
as well as an additional required "outputSchema" JSON Schema object.

Returns[](#returns "Direct link to Returns")
---------------------------------------------

[`LLMChain`](/docs/api/chains/classes/LLMChain)<`any`, [`ChatOpenAI`](/docs/api/chat_models_openai/classes/ChatOpenAI)\>

OpenAPIChain

Defined in[](#defined-in "Direct link to Defined in")
------------------------------------------------------

[langchain/src/chains/openai\_functions/structured\_output.ts:69](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/openai_functions/structured_output.ts#L69)