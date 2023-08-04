OpenAIAgentTokenBufferMemory
============================

Memory used to save agent output and intermediate steps.

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseChatMemory`](/docs/api/memory/classes/BaseChatMemory).**OpenAIAgentTokenBufferMemory**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new OpenAIAgentTokenBufferMemory**(`fields`: `OpenAIAgentTokenBufferMemoryFields`): [`OpenAIAgentTokenBufferMemory`](/docs/api/agents_toolkits/classes/OpenAIAgentTokenBufferMemory)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`fields`

`OpenAIAgentTokenBufferMemoryFields`

#### Returns[](#returns "Direct link to Returns")

[`OpenAIAgentTokenBufferMemory`](/docs/api/agents_toolkits/classes/OpenAIAgentTokenBufferMemory)

#### Overrides[](#overrides "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[constructor](/docs/api/memory/classes/BaseChatMemory#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/agents/toolkits/conversational\_retrieval/token\_buffer\_memory.ts:47](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/toolkits/conversational_retrieval/token_buffer_memory.ts#L47)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### aiPrefix[](#aiprefix "Direct link to aiPrefix")

> **aiPrefix**: `string` = `"AI"`

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/agents/toolkits/conversational\_retrieval/token\_buffer\_memory.ts:33](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/toolkits/conversational_retrieval/token_buffer_memory.ts#L33)

### chatHistory[](#chathistory "Direct link to chatHistory")

> **chatHistory**: [`BaseChatMessageHistory`](/docs/api/schema/classes/BaseChatMessageHistory)

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[chatHistory](/docs/api/memory/classes/BaseChatMemory#chathistory)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:19](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L19)

### humanPrefix[](#humanprefix "Direct link to humanPrefix")

> **humanPrefix**: `string` = `"Human"`

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/agents/toolkits/conversational\_retrieval/token\_buffer\_memory.ts:31](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/toolkits/conversational_retrieval/token_buffer_memory.ts#L31)

### intermediateStepsKey[](#intermediatestepskey "Direct link to intermediateStepsKey")

> **intermediateStepsKey**: `string` = `"intermediateSteps"`

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/agents/toolkits/conversational\_retrieval/token\_buffer\_memory.ts:45](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/toolkits/conversational_retrieval/token_buffer_memory.ts#L45)

### llm[](#llm "Direct link to llm")

> **llm**: [`ChatOpenAI`](/docs/api/chat_models_openai/classes/ChatOpenAI)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/agents/toolkits/conversational\_retrieval/token\_buffer\_memory.ts:35](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/toolkits/conversational_retrieval/token_buffer_memory.ts#L35)

### maxTokenLimit[](#maxtokenlimit "Direct link to maxTokenLimit")

> **maxTokenLimit**: `number` = `12000`

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/agents/toolkits/conversational\_retrieval/token\_buffer\_memory.ts:39](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/toolkits/conversational_retrieval/token_buffer_memory.ts#L39)

### memoryKey[](#memorykey "Direct link to memoryKey")

> **memoryKey**: `string` = `"history"`

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/agents/toolkits/conversational\_retrieval/token\_buffer\_memory.ts:37](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/toolkits/conversational_retrieval/token_buffer_memory.ts#L37)

### outputKey[](#outputkey "Direct link to outputKey")

> **outputKey**: `string` = `"output"`

#### Overrides[](#overrides-1 "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[outputKey](/docs/api/memory/classes/BaseChatMemory#outputkey)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/agents/toolkits/conversational\_retrieval/token\_buffer\_memory.ts:43](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/toolkits/conversational_retrieval/token_buffer_memory.ts#L43)

### returnMessages[](#returnmessages "Direct link to returnMessages")

> **returnMessages**: `boolean` = `true`

#### Overrides[](#overrides-2 "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[returnMessages](/docs/api/memory/classes/BaseChatMemory#returnmessages)

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/agents/toolkits/conversational\_retrieval/token\_buffer\_memory.ts:41](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/toolkits/conversational_retrieval/token_buffer_memory.ts#L41)

### inputKey?[](#inputkey "Direct link to inputKey?")

> **inputKey**: `string`

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[inputKey](/docs/api/memory/classes/BaseChatMemory#inputkey)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:23](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L23)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### memoryKeys[](#memorykeys "Direct link to memoryKeys")

> **memoryKeys**(): `string`\[\]

#### Returns[](#returns-1 "Direct link to Returns")

`string`\[\]

#### Overrides[](#overrides-3 "Direct link to Overrides")

BaseChatMemory.memoryKeys

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/agents/toolkits/conversational\_retrieval/token\_buffer\_memory.ts:60](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/toolkits/conversational_retrieval/token_buffer_memory.ts#L60)

#### Overrides[](#overrides-4 "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[memoryKeys](/docs/api/memory/classes/BaseChatMemory#memorykeys)

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/agents/toolkits/conversational\_retrieval/token\_buffer\_memory.ts:60](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/toolkits/conversational_retrieval/token_buffer_memory.ts#L60)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### clear()[](#clear "Direct link to clear()")

> **clear**(): `Promise`<`void`\>

#### Returns[](#returns-2 "Direct link to Returns")

`Promise`<`void`\>

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[clear](/docs/api/memory/classes/BaseChatMemory#clear)

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L48)

### getMessages()[](#getmessages "Direct link to getMessages()")

> **getMessages**(): `Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]\>

#### Returns[](#returns-3 "Direct link to Returns")

`Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]\>

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/agents/toolkits/conversational\_retrieval/token\_buffer\_memory.ts:64](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/toolkits/conversational_retrieval/token_buffer_memory.ts#L64)

### loadMemoryVariables()[](#loadmemoryvariables "Direct link to loadMemoryVariables()")

> **loadMemoryVariables**(`_values`: `InputValues`): `Promise`<`MemoryVariables`\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`_values`

`InputValues`

#### Returns[](#returns-4 "Direct link to Returns")

`Promise`<`MemoryVariables`\>

#### Overrides[](#overrides-5 "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[loadMemoryVariables](/docs/api/memory/classes/BaseChatMemory#loadmemoryvariables)

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/agents/toolkits/conversational\_retrieval/token\_buffer\_memory.ts:68](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/toolkits/conversational_retrieval/token_buffer_memory.ts#L68)

### saveContext()[](#savecontext "Direct link to saveContext()")

> **saveContext**(`inputValues`: `InputValues`, `outputValues`: `OutputValues`): `Promise`<`void`\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`inputValues`

`InputValues`

`outputValues`

`OutputValues`

#### Returns[](#returns-5 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[](#overrides-6 "Direct link to Overrides")

[BaseChatMemory](/docs/api/memory/classes/BaseChatMemory).[saveContext](/docs/api/memory/classes/BaseChatMemory#savecontext)

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/agents/toolkits/conversational\_retrieval/token\_buffer\_memory.ts:82](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/toolkits/conversational_retrieval/token_buffer_memory.ts#L82)