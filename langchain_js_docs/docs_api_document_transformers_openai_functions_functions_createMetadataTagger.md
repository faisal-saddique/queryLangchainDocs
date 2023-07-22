createMetadataTagger()
======================

> **createMetadataTagger**(`schema`: `JsonSchema7ObjectType`, `options`: {`prompt`?: [`PromptTemplate`](/docs/api/prompts/classes/PromptTemplate);} & `Omit`<[`LLMChainInput`](/docs/api/chains/interfaces/LLMChainInput)<`object`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>, "llm" | "prompt"\> & {`llm`?: [`ChatOpenAI`](/docs/api/chat_models_openai/classes/ChatOpenAI);}): [`MetadataTagger`](/docs/api/document_transformers_openai_functions/classes/MetadataTagger)

Parameters[​](#parameters "Direct link to Parameters")
------------------------------------------------------

Parameter

Type

`schema`

`JsonSchema7ObjectType`

`options`

{`prompt`?: [`PromptTemplate`](/docs/api/prompts/classes/PromptTemplate);} & `Omit`<[`LLMChainInput`](/docs/api/chains/interfaces/LLMChainInput)<`object`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>, "llm" | "prompt"\> & {`llm`?: [`ChatOpenAI`](/docs/api/chat_models_openai/classes/ChatOpenAI);}

Returns[​](#returns "Direct link to Returns")
---------------------------------------------

[`MetadataTagger`](/docs/api/document_transformers_openai_functions/classes/MetadataTagger)

Defined in[​](#defined-in "Direct link to Defined in")
------------------------------------------------------

[langchain/src/document\_transformers/openai\_functions.ts:50](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_transformers/openai_functions.ts#L50)