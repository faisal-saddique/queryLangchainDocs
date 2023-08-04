ConditionalPromptSelector
=========================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BasePromptSelector`](/docs/api/prompts/classes/BasePromptSelector).**ConditionalPromptSelector**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new ConditionalPromptSelector**(`default_prompt`: [`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)<[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\>, `conditionals`: \[condition: Function, prompt: BasePromptTemplate<BasePromptValue\>\]\[\] = `[]`): [`ConditionalPromptSelector`](/docs/api/prompts/classes/ConditionalPromptSelector)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

Default value

`default_prompt`

[`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)<[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\>

`undefined`

`conditionals`

\[condition: Function, prompt: BasePromptTemplate<BasePromptValue\>\]\[\]

`[]`

#### Returns[](#returns "Direct link to Returns")

[`ConditionalPromptSelector`](/docs/api/prompts/classes/ConditionalPromptSelector)

#### Overrides[](#overrides "Direct link to Overrides")

[BasePromptSelector](/docs/api/prompts/classes/BasePromptSelector).[constructor](/docs/api/prompts/classes/BasePromptSelector#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/prompts/selectors/conditional.ts:30](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/selectors/conditional.ts#L30)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### conditionals[](#conditionals "Direct link to conditionals")

> **conditionals**: \[condition: Function, prompt: BasePromptTemplate<BasePromptValue\>\]\[\]

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/prompts/selectors/conditional.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/selectors/conditional.ts#L26)

### defaultPrompt[](#defaultprompt "Direct link to defaultPrompt")

> **defaultPrompt**: [`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)<[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\>

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/prompts/selectors/conditional.ts:24](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/selectors/conditional.ts#L24)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### getPrompt()[](#getprompt "Direct link to getPrompt()")

> **getPrompt**(`llm`: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>): [`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)<[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`llm`

[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>

#### Returns[](#returns-1 "Direct link to Returns")

[`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)<[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\>

#### Overrides[](#overrides-1 "Direct link to Overrides")

[BasePromptSelector](/docs/api/prompts/classes/BasePromptSelector).[getPrompt](/docs/api/prompts/classes/BasePromptSelector#getprompt)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/prompts/selectors/conditional.ts:44](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/selectors/conditional.ts#L44)

### getPromptAsync()[](#getpromptasync "Direct link to getPromptAsync()")

> **getPromptAsync**(`llm`: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>, `options`?: `BaseGetPromptAsyncOptions`): `Promise`<[`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)<[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\>\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`llm`

[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>

`options?`

`BaseGetPromptAsyncOptions`

#### Returns[](#returns-2 "Direct link to Returns")

`Promise`<[`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)<[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\>\>

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BasePromptSelector](/docs/api/prompts/classes/BasePromptSelector).[getPromptAsync](/docs/api/prompts/classes/BasePromptSelector#getpromptasync)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/prompts/selectors/conditional.ts:14](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/selectors/conditional.ts#L14)