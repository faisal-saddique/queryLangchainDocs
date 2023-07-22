BasePromptSelector
==================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`ConditionalPromptSelector`](/docs/api/prompts/classes/ConditionalPromptSelector)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new BasePromptSelector**(): [`BasePromptSelector`](/docs/api/prompts/classes/BasePromptSelector)

#### Returns[​](#returns "Direct link to Returns")

[`BasePromptSelector`](/docs/api/prompts/classes/BasePromptSelector)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### getPrompt()[​](#getprompt "Direct link to getPrompt()")

> `Abstract` **getPrompt**(`llm`: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)): [`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`llm`

[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)

#### Returns[​](#returns-1 "Direct link to Returns")

[`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/prompts/selectors/conditional.ts:12](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/selectors/conditional.ts#L12)

### getPromptAsync()[​](#getpromptasync "Direct link to getPromptAsync()")

> **getPromptAsync**(`llm`: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel), `options`?: `BaseGetPromptAsyncOptions`): `Promise`<[`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`llm`

[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)

`options?`

`BaseGetPromptAsyncOptions`

#### Returns[​](#returns-2 "Direct link to Returns")

`Promise`<[`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)\>

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/prompts/selectors/conditional.ts:14](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/selectors/conditional.ts#L14)