GenerativeAgentMemory
=====================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseMemory`](/docs/api/memory/classes/BaseMemory).**GenerativeAgentMemory**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new GenerativeAgentMemory**(`llm`: [`BaseLLM`](/docs/api/llms_base/classes/BaseLLM), `memoryRetriever`: [`TimeWeightedVectorStoreRetriever`](/docs/api/retrievers_time_weighted/classes/TimeWeightedVectorStoreRetriever), `config`?: `GenerativeAgentMemoryConfig`): [`GenerativeAgentMemory`](/docs/api/experimental_generative_agents/classes/GenerativeAgentMemory)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`llm`

[`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)

`memoryRetriever`

[`TimeWeightedVectorStoreRetriever`](/docs/api/retrievers_time_weighted/classes/TimeWeightedVectorStoreRetriever)

`config?`

`GenerativeAgentMemoryConfig`

#### Returns[​](#returns "Direct link to Returns")

[`GenerativeAgentMemory`](/docs/api/experimental_generative_agents/classes/GenerativeAgentMemory)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseMemory](/docs/api/memory/classes/BaseMemory).[constructor](/docs/api/memory/classes/BaseMemory#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:48](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L48)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### addMemoryKey[​](#addmemorykey "Direct link to addMemoryKey")

> **addMemoryKey**: `string` = `"addMemory"`

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:36](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L36)

### currentPlan[​](#currentplan "Direct link to currentPlan")

> **currentPlan**: `string`\[\] = `[]`

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:24](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L24)

### importanceWeight[​](#importanceweight "Direct link to importanceWeight")

> **importanceWeight**: `number` = `0.15`

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:26](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L26)

### llm[​](#llm "Direct link to llm")

> **llm**: [`BaseLLM`](/docs/api/llms_base/classes/BaseLLM)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:16](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L16)

### memoryRetriever[​](#memoryretriever "Direct link to memoryRetriever")

> **memoryRetriever**: [`TimeWeightedVectorStoreRetriever`](/docs/api/retrievers_time_weighted/classes/TimeWeightedVectorStoreRetriever)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:18](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L18)

### mostRecentMemoriesKey[​](#mostrecentmemorieskey "Direct link to mostRecentMemoriesKey")

> **mostRecentMemoriesKey**: `string` = `"most_recent_memories"`

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L42)

### mostRecentMemoriesTokenKey[​](#mostrecentmemoriestokenkey "Direct link to mostRecentMemoriesTokenKey")

> **mostRecentMemoriesTokenKey**: `string` = `"recent_memories_token"`

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:34](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L34)

### nowKey[​](#nowkey "Direct link to nowKey")

> **nowKey**: `string` = `"now"`

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:44](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L44)

### queriesKey[​](#querieskey "Direct link to queriesKey")

> **queriesKey**: `string` = `"queries"`

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:32](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L32)

### reflecting[​](#reflecting "Direct link to reflecting")

> **reflecting**: `boolean` = `false`

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L46)

### relevantMemoriesKey[​](#relevantmemorieskey "Direct link to relevantMemoriesKey")

> **relevantMemoriesKey**: `string` = `"relevant_memories"`

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:38](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L38)

### relevantMemoriesSimpleKey[​](#relevantmemoriessimplekey "Direct link to relevantMemoriesSimpleKey")

> **relevantMemoriesSimpleKey**: `string` = `"relevant_memories_simple"`

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L40)

### verbose[​](#verbose "Direct link to verbose")

> **verbose**: `boolean`

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:20](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L20)

### reflectionThreshold?[​](#reflectionthreshold "Direct link to reflectionThreshold?")

> **reflectionThreshold**: `number`

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L22)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### memoryKeys[​](#memorykeys "Direct link to memoryKeys")

> **memoryKeys**(): `string`\[\]

#### Returns[​](#returns-1 "Direct link to Returns")

`string`\[\]

#### Overrides[​](#overrides-1 "Direct link to Overrides")

BaseMemory.memoryKeys

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:79](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L79)

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[BaseMemory](/docs/api/memory/classes/BaseMemory).[memoryKeys](/docs/api/memory/classes/BaseMemory#memorykeys)

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:79](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L79)

### memoryVariables[​](#memoryvariables "Direct link to memoryVariables")

> **memoryVariables**(): `string`\[\]

#### Returns[​](#returns-2 "Direct link to Returns")

`string`\[\]

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:267](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L267)

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:267](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L267)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### addMemory()[​](#addmemory "Direct link to addMemory()")

> **addMemory**(`memoryContent`: `string`, `now`?: `Date`): `Promise`<`void`\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`memoryContent`

`string`

`now?`

`Date`

#### Returns[​](#returns-3 "Direct link to Returns")

`Promise`<`void`\>

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:182](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L182)

### chain()[​](#chain "Direct link to chain()")

> **chain**(`prompt`: [`PromptTemplate`](/docs/api/prompts/classes/PromptTemplate)): [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`prompt`

[`PromptTemplate`](/docs/api/prompts/classes/PromptTemplate)

#### Returns[​](#returns-4 "Direct link to Returns")

[`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:84](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L84)

### clear()[​](#clear "Direct link to clear()")

> **clear**(): `void`

#### Returns[​](#returns-5 "Direct link to Returns")

`void`

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:312](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L312)

### fetchMemories()[​](#fetchmemories "Direct link to fetchMemories()")

> **fetchMemories**(`observation`: `string`, `_now`?: `Date`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`observation`

`string`

`_now?`

`Date`

#### Returns[​](#returns-6 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:209](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L209)

### formatMemoriesDetail()[​](#formatmemoriesdetail "Direct link to formatMemoriesDetail()")

> **formatMemoriesDetail**(`relevantMemories`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]): `string`

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`relevantMemories`

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

#### Returns[​](#returns-7 "Direct link to Returns")

`string`

#### Defined in[​](#defined-in-23 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:213](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L213)

### formatMemoriesSimple()[​](#formatmemoriessimple "Direct link to formatMemoriesSimple()")

> **formatMemoriesSimple**(`relevantMemories`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]): `string`

#### Parameters[​](#parameters-5 "Direct link to Parameters")

Parameter

Type

`relevantMemories`

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

#### Returns[​](#returns-8 "Direct link to Returns")

`string`

#### Defined in[​](#defined-in-24 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:238](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L238)

### getAddMemoryKey()[​](#getaddmemorykey "Direct link to getAddMemoryKey()")

> **getAddMemoryKey**(): `string`

#### Returns[​](#returns-9 "Direct link to Returns")

`string`

#### Defined in[​](#defined-in-25 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:71](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L71)

### getCurrentTimeKey()[​](#getcurrenttimekey "Direct link to getCurrentTimeKey()")

> **getCurrentTimeKey**(): `string`

#### Returns[​](#returns-10 "Direct link to Returns")

`string`

#### Defined in[​](#defined-in-26 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:75](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L75)

### getInsightsOnTopic()[​](#getinsightsontopic "Direct link to getInsightsOnTopic()")

> **getInsightsOnTopic**(`topic`: `string`, `now`?: `Date`): `Promise`<`string`\[\]\>

#### Parameters[​](#parameters-6 "Direct link to Parameters")

Parameter

Type

`topic`

`string`

`now?`

`Date`

#### Returns[​](#returns-11 "Direct link to Returns")

`Promise`<`string`\[\]\>

#### Defined in[​](#defined-in-27 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:115](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L115)

### getMemoriesUntilLimit()[​](#getmemoriesuntillimit "Direct link to getMemoriesUntilLimit()")

> **getMemoriesUntilLimit**(`consumedTokens`: `number`): `Promise`<`string`\>

#### Parameters[​](#parameters-7 "Direct link to Parameters")

Parameter

Type

`consumedTokens`

`number`

#### Returns[​](#returns-12 "Direct link to Returns")

`Promise`<`string`\>

#### Defined in[​](#defined-in-28 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:245](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L245)

### getMostRecentMemoriesTokenKey()[​](#getmostrecentmemoriestokenkey "Direct link to getMostRecentMemoriesTokenKey()")

> **getMostRecentMemoriesTokenKey**(): `string`

#### Returns[​](#returns-13 "Direct link to Returns")

`string`

#### Defined in[​](#defined-in-29 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:67](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L67)

### getRelevantMemoriesKey()[​](#getrelevantmemorieskey "Direct link to getRelevantMemoriesKey()")

> **getRelevantMemoriesKey**(): `string`

#### Returns[​](#returns-14 "Direct link to Returns")

`string`

#### Defined in[​](#defined-in-30 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:63](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L63)

### getTopicsOfReflection()[​](#gettopicsofreflection "Direct link to getTopicsOfReflection()")

> **getTopicsOfReflection**(`lastK`: `number` = `50`): `Promise`<`string`\[\]\>

#### Parameters[​](#parameters-8 "Direct link to Parameters")

Parameter

Type

Default value

`lastK`

`number`

`50`

#### Returns[​](#returns-15 "Direct link to Returns")

`Promise`<`string`\[\]\>

#### Defined in[​](#defined-in-31 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:99](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L99)

### loadMemoryVariables()[​](#loadmemoryvariables "Direct link to loadMemoryVariables()")

> **loadMemoryVariables**(`inputs`: `InputValues`): `Promise`<`Record`<`string`, `string`\>\>

#### Parameters[​](#parameters-9 "Direct link to Parameters")

Parameter

Type

`inputs`

`InputValues`

#### Returns[​](#returns-16 "Direct link to Returns")

`Promise`<`Record`<`string`, `string`\>\>

#### Overrides[​](#overrides-3 "Direct link to Overrides")

[BaseMemory](/docs/api/memory/classes/BaseMemory).[loadMemoryVariables](/docs/api/memory/classes/BaseMemory#loadmemoryvariables)

#### Defined in[​](#defined-in-32 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:272](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L272)

### pauseToReflect()[​](#pausetoreflect "Direct link to pauseToReflect()")

> **pauseToReflect**(`now`?: `Date`): `Promise`<`string`\[\]\>

#### Parameters[​](#parameters-10 "Direct link to Parameters")

Parameter

Type

`now?`

`Date`

#### Returns[​](#returns-17 "Direct link to Returns")

`Promise`<`string`\[\]\>

#### Defined in[​](#defined-in-33 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:135](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L135)

### saveContext()[​](#savecontext "Direct link to saveContext()")

> **saveContext**(`_inputs`: `InputValues`, `outputs`: `OutputValues`): `Promise`<`void`\>

#### Parameters[​](#parameters-11 "Direct link to Parameters")

Parameter

Type

`_inputs`

`InputValues`

`outputs`

`OutputValues`

#### Returns[​](#returns-18 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[​](#overrides-4 "Direct link to Overrides")

[BaseMemory](/docs/api/memory/classes/BaseMemory).[saveContext](/docs/api/memory/classes/BaseMemory#savecontext)

#### Defined in[​](#defined-in-34 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:300](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L300)

### scoreMemoryImportance()[​](#scorememoryimportance "Direct link to scoreMemoryImportance()")

> **scoreMemoryImportance**(`memoryContent`: `string`): `Promise`<`number`\>

#### Parameters[​](#parameters-12 "Direct link to Parameters")

Parameter

Type

`memoryContent`

`string`

#### Returns[​](#returns-19 "Direct link to Returns")

`Promise`<`number`\>

#### Defined in[​](#defined-in-35 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:152](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L152)

### parseList()[​](#parselist "Direct link to parseList()")

> `Static` **parseList**(`text`: `string`): `string`\[\]

#### Parameters[​](#parameters-13 "Direct link to Parameters")

Parameter

Type

`text`

`string`

#### Returns[​](#returns-20 "Direct link to Returns")

`string`\[\]

#### Defined in[​](#defined-in-36 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:94](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L94)