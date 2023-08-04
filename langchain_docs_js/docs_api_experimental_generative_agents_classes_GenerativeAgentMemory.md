GenerativeAgentMemory
=====================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseMemory`](/docs/api/memory/classes/BaseMemory).**GenerativeAgentMemory**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new GenerativeAgentMemory**(`llm`: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>, `memoryRetriever`: [`TimeWeightedVectorStoreRetriever`](/docs/api/retrievers_time_weighted/classes/TimeWeightedVectorStoreRetriever), `config`?: `GenerativeAgentMemoryConfig`): [`GenerativeAgentMemory`](/docs/api/experimental_generative_agents/classes/GenerativeAgentMemory)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`llm`

[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>

`memoryRetriever`

[`TimeWeightedVectorStoreRetriever`](/docs/api/retrievers_time_weighted/classes/TimeWeightedVectorStoreRetriever)

`config?`

`GenerativeAgentMemoryConfig`

#### Returns[](#returns "Direct link to Returns")

[`GenerativeAgentMemory`](/docs/api/experimental_generative_agents/classes/GenerativeAgentMemory)

#### Overrides[](#overrides "Direct link to Overrides")

[BaseMemory](/docs/api/memory/classes/BaseMemory).[constructor](/docs/api/memory/classes/BaseMemory#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:261](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L261)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### addMemoryKey[](#addmemorykey "Direct link to addMemoryKey")

> **addMemoryKey**: `string` = `"addMemory"`

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:249](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L249)

### llm[](#llm "Direct link to llm")

> **llm**: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:235](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L235)

### memoryChain[](#memorychain "Direct link to memoryChain")

> **memoryChain**: `GenerativeAgentMemoryChain`

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:259](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L259)

### memoryRetriever[](#memoryretriever "Direct link to memoryRetriever")

> **memoryRetriever**: [`TimeWeightedVectorStoreRetriever`](/docs/api/retrievers_time_weighted/classes/TimeWeightedVectorStoreRetriever)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:237](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L237)

### mostRecentMemoriesKey[](#mostrecentmemorieskey "Direct link to mostRecentMemoriesKey")

> **mostRecentMemoriesKey**: `string` = `"most_recent_memories"`

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:255](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L255)

### mostRecentMemoriesTokenKey[](#mostrecentmemoriestokenkey "Direct link to mostRecentMemoriesTokenKey")

> **mostRecentMemoriesTokenKey**: `string` = `"recent_memories_token"`

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:247](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L247)

### nowKey[](#nowkey "Direct link to nowKey")

> **nowKey**: `string` = `"now"`

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:257](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L257)

### queriesKey[](#querieskey "Direct link to queriesKey")

> **queriesKey**: `string` = `"queries"`

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:245](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L245)

### relevantMemoriesKey[](#relevantmemorieskey "Direct link to relevantMemoriesKey")

> **relevantMemoriesKey**: `string` = `"relevant_memories"`

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:251](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L251)

### relevantMemoriesSimpleKey[](#relevantmemoriessimplekey "Direct link to relevantMemoriesSimpleKey")

> **relevantMemoriesSimpleKey**: `string` = `"relevant_memories_simple"`

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:253](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L253)

### verbose[](#verbose "Direct link to verbose")

> **verbose**: `boolean`

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:239](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L239)

### reflectionThreshold?[](#reflectionthreshold "Direct link to reflectionThreshold?")

> **reflectionThreshold**: `number`

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:241](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L241)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### memoryKeys[](#memorykeys "Direct link to memoryKeys")

> **memoryKeys**(): `string`\[\]

#### Returns[](#returns-1 "Direct link to Returns")

`string`\[\]

#### Overrides[](#overrides-1 "Direct link to Overrides")

BaseMemory.memoryKeys

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:295](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L295)

#### Overrides[](#overrides-2 "Direct link to Overrides")

[BaseMemory](/docs/api/memory/classes/BaseMemory).[memoryKeys](/docs/api/memory/classes/BaseMemory#memorykeys)

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:295](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L295)

### memoryVariables[](#memoryvariables "Direct link to memoryVariables")

> **memoryVariables**(): `string`\[\]

#### Returns[](#returns-2 "Direct link to Returns")

`string`\[\]

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:366](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L366)

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:366](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L366)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### addMemory()[](#addmemory "Direct link to addMemory()")

> **addMemory**(`memoryContent`: `string`, `now`?: `Date`, `metadata`?: `Record`<`string`, `unknown`\>, `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`memoryContent`

`string`

`now?`

`Date`

`metadata?`

`Record`<`string`, `unknown`\>

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-3 "Direct link to Returns")

`Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\>

#### Defined in[](#defined-in-17 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:300](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L300)

### clear()[](#clear "Direct link to clear()")

> **clear**(): `void`

#### Returns[](#returns-4 "Direct link to Returns")

`void`

#### Defined in[](#defined-in-18 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:413](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L413)

### formatMemoriesDetail()[](#formatmemoriesdetail "Direct link to formatMemoriesDetail()")

> **formatMemoriesDetail**(`relevantMemories`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]): `string`

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`relevantMemories`

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

#### Returns[](#returns-5 "Direct link to Returns")

`string`

#### Defined in[](#defined-in-19 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:312](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L312)

### formatMemoriesSimple()[](#formatmemoriessimple "Direct link to formatMemoriesSimple()")

> **formatMemoriesSimple**(`relevantMemories`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]): `string`

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

`relevantMemories`

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

#### Returns[](#returns-6 "Direct link to Returns")

`string`

#### Defined in[](#defined-in-20 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:337](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L337)

### getAddMemoryKey()[](#getaddmemorykey "Direct link to getAddMemoryKey()")

> **getAddMemoryKey**(): `string`

#### Returns[](#returns-7 "Direct link to Returns")

`string`

#### Defined in[](#defined-in-21 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:287](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L287)

### getCurrentTimeKey()[](#getcurrenttimekey "Direct link to getCurrentTimeKey()")

> **getCurrentTimeKey**(): `string`

#### Returns[](#returns-8 "Direct link to Returns")

`string`

#### Defined in[](#defined-in-22 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:291](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L291)

### getMemoriesUntilLimit()[](#getmemoriesuntillimit "Direct link to getMemoriesUntilLimit()")

> **getMemoriesUntilLimit**(`consumedTokens`: `number`): `Promise`<`string`\>

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

`consumedTokens`

`number`

#### Returns[](#returns-9 "Direct link to Returns")

`Promise`<`string`\>

#### Defined in[](#defined-in-23 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:344](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L344)

### getMostRecentMemoriesTokenKey()[](#getmostrecentmemoriestokenkey "Direct link to getMostRecentMemoriesTokenKey()")

> **getMostRecentMemoriesTokenKey**(): `string`

#### Returns[](#returns-10 "Direct link to Returns")

`string`

#### Defined in[](#defined-in-24 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:283](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L283)

### getRelevantMemoriesKey()[](#getrelevantmemorieskey "Direct link to getRelevantMemoriesKey()")

> **getRelevantMemoriesKey**(): `string`

#### Returns[](#returns-11 "Direct link to Returns")

`string`

#### Defined in[](#defined-in-25 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:279](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L279)

### loadMemoryVariables()[](#loadmemoryvariables "Direct link to loadMemoryVariables()")

> **loadMemoryVariables**(`inputs`: `InputValues`): `Promise`<`Record`<`string`, `string`\>\>

#### Parameters[](#parameters-5 "Direct link to Parameters")

Parameter

Type

`inputs`

`InputValues`

#### Returns[](#returns-12 "Direct link to Returns")

`Promise`<`Record`<`string`, `string`\>\>

#### Overrides[](#overrides-3 "Direct link to Overrides")

[BaseMemory](/docs/api/memory/classes/BaseMemory).[loadMemoryVariables](/docs/api/memory/classes/BaseMemory#loadmemoryvariables)

#### Defined in[](#defined-in-26 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:371](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L371)

### saveContext()[](#savecontext "Direct link to saveContext()")

> **saveContext**(`_inputs`: `InputValues`, `outputs`: `OutputValues`): `Promise`<`void`\>

#### Parameters[](#parameters-6 "Direct link to Parameters")

Parameter

Type

`_inputs`

`InputValues`

`outputs`

`OutputValues`

#### Returns[](#returns-13 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[](#overrides-4 "Direct link to Overrides")

[BaseMemory](/docs/api/memory/classes/BaseMemory).[saveContext](/docs/api/memory/classes/BaseMemory#savecontext)

#### Defined in[](#defined-in-27 "Direct link to Defined in")

[langchain/src/experimental/generative\_agents/generative\_agent\_memory.ts:401](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/generative_agents/generative_agent_memory.ts#L401)