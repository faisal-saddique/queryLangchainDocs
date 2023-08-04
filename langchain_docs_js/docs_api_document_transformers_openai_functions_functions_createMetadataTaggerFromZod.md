createMetadataTaggerFromZod()
=============================

> **createMetadataTaggerFromZod**(`schema`: `AnyZodObject`, `options`: {`prompt`?: [`PromptTemplate`](/docs/api/prompts/classes/PromptTemplate);} & `Omit`<[`LLMChainInput`](/docs/api/chains/interfaces/LLMChainInput)<`object`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>\>, "llm" | "prompt"\> & {`llm`?: [`ChatOpenAI`](/docs/api/chat_models_openai/classes/ChatOpenAI);}): [`MetadataTagger`](/docs/api/document_transformers_openai_functions/classes/MetadataTagger)

Parameters[](#parameters "Direct link to Parameters")
------------------------------------------------------

Parameter

Type

`schema`

`AnyZodObject`

`options`

{`prompt`?: [`PromptTemplate`](/docs/api/prompts/classes/PromptTemplate);} & `Omit`<[`LLMChainInput`](/docs/api/chains/interfaces/LLMChainInput)<`object`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>\>, "llm" | "prompt"\> & {`llm`?: [`ChatOpenAI`](/docs/api/chat_models_openai/classes/ChatOpenAI);}

Returns[](#returns "Direct link to Returns")
---------------------------------------------

[`MetadataTagger`](/docs/api/document_transformers_openai_functions/classes/MetadataTagger)

Defined in[](#defined-in "Direct link to Defined in")
------------------------------------------------------

[langchain/src/document\_transformers/openai\_functions.ts:55](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_transformers/openai_functions.ts#L55)