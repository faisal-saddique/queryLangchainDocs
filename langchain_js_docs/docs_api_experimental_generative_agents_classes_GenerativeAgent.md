GenerativeAgent
===============

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new GenerativeAgent**(`llm`: [`BaseLLM`](/docs/api/llms_base/classes/BaseLLM), `memory`: [`GenerativeAgentMemory`](/docs/api/experimental_generative_agents/classes/GenerativeAgentMemory), `config`: `GenerativeAgentConfig`): [`GenerativeAgent`](/docs/api/experimental_generative_agents/classes/GenerativeAgent)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`llm`

[`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)

`memory`

[`GenerativeAgentMemory`](/docs/api/experimental_generative_agents/classes/GenerativeAgentMemory)

`config`

`GenerativeAgentConfig`

#### Returns[​](#returns "Direct link to Returns")

[`GenerativeAgent`](/docs/api/experimental_generative_agents/classes/GenerativeAgent)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent.ts#L42)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### llm[​](#llm "Direct link to llm")

> **llm**: [`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent.ts:29](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent.ts#L29)

### memory[​](#memory "Direct link to memory")

> **memory**: [`GenerativeAgentMemory`](/docs/api/experimental_generative_agents/classes/GenerativeAgentMemory)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent.ts:27](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent.ts#L27)

### name[​](#name "Direct link to name")

> **name**: `string`

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent.ts:19](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent.ts#L19)

### status[​](#status "Direct link to status")

> **status**: `string`

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent.ts:25](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent.ts#L25)

### traits[​](#traits "Direct link to traits")

> **traits**: `string`

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent.ts#L23)

### verbose[​](#verbose "Direct link to verbose")

> **verbose**: `boolean`

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent.ts:31](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent.ts#L31)

### age?[​](#age "Direct link to age?")

> **age**: `number`

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent.ts:21](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent.ts#L21)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### chain()[​](#chain "Direct link to chain()")

> **chain**(`prompt`: [`PromptTemplate`](/docs/api/prompts/classes/PromptTemplate)): [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`prompt`

[`PromptTemplate`](/docs/api/prompts/classes/PromptTemplate)

#### Returns[​](#returns-1 "Direct link to Returns")

[`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent.ts:71](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent.ts#L71)

### computeAgentSummary()[​](#computeagentsummary "Direct link to computeAgentSummary()")

> **computeAgentSummary**(): `Promise`<`string`\>

#### Returns[​](#returns-2 "Direct link to Returns")

`Promise`<`string`\>

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent.ts:309](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent.ts#L309)

### generateDialogueResponse()[​](#generatedialogueresponse "Direct link to generateDialogueResponse()")

> **generateDialogueResponse**(`observation`: `string`, `now`?: `Date`): `Promise`<\[`boolean`, `string`\]\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`observation`

`string`

`now?`

`Date`

#### Returns[​](#returns-3 "Direct link to Returns")

`Promise`<\[`boolean`, `string`\]\>

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent.ts:227](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent.ts#L227)

### generateReaction()[​](#generatereaction "Direct link to generateReaction()")

> **generateReaction**(`observation`: `string`, `now`?: `Date`): `Promise`<\[`boolean`, `string`\]\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`observation`

`string`

`now?`

`Date`

#### Returns[​](#returns-4 "Direct link to Returns")

`Promise`<\[`boolean`, `string`\]\>

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent.ts:190](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent.ts#L190)

### getEntityAction()[​](#getentityaction "Direct link to getEntityAction()")

> **getEntityAction**(`observation`: `string`, `entityName`: `string`): `Promise`<`string`\>

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`observation`

`string`

`entityName`

`string`

#### Returns[​](#returns-5 "Direct link to Returns")

`Promise`<`string`\>

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent.ts:95](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent.ts#L95)

### getEntityFromObservations()[​](#getentityfromobservations "Direct link to getEntityFromObservations()")

> **getEntityFromObservations**(`observation`: `string`): `Promise`<`string`\>

#### Parameters[​](#parameters-5 "Direct link to Parameters")

Parameter

Type

`observation`

`string`

#### Returns[​](#returns-6 "Direct link to Returns")

`Promise`<`string`\>

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent.ts:82](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent.ts#L82)

### getFullHeader()[​](#getfullheader "Direct link to getFullHeader()")

> **getFullHeader**(`config`: `object` = `{}`): `string`

#### Parameters[​](#parameters-6 "Direct link to Parameters")

Parameter

Type

`config`

`object`

`config.forceRefresh?`

`boolean`

`config.now?`

`Date`

#### Returns[​](#returns-7 "Direct link to Returns")

`string`

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent.ts:326](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent.ts#L326)

### getSummary()[​](#getsummary "Direct link to getSummary()")

> **getSummary**(`config`: `object` = `{}`): `Promise`<`string`\>

#### Parameters[​](#parameters-7 "Direct link to Parameters")

Parameter

Type

`config`

`object`

`config.forceRefresh?`

`boolean`

`config.now?`

`Date`

#### Returns[​](#returns-8 "Direct link to Returns")

`Promise`<`string`\>

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent.ts:276](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent.ts#L276)

### parseList()[​](#parselist "Direct link to parseList()")

> **parseList**(`text`: `string`): `string`\[\]

#### Parameters[​](#parameters-8 "Direct link to Parameters")

Parameter

Type

`text`

`string`

#### Returns[​](#returns-9 "Direct link to Returns")

`string`\[\]

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent.ts:62](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent.ts#L62)

### summarizeRelatedMemories()[​](#summarizerelatedmemories "Direct link to summarizeRelatedMemories()")

> **summarizeRelatedMemories**(`observation`: `string`): `Promise`<`string`\>

#### Parameters[​](#parameters-9 "Direct link to Parameters")

Parameter

Type

`observation`

`string`

#### Returns[​](#returns-10 "Direct link to Returns")

`Promise`<`string`\>

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent.ts:112](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent.ts#L112)