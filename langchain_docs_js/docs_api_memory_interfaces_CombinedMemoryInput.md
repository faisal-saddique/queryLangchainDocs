CombinedMemoryInput
===================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseChatMemoryInput`](/docs/api/memory/interfaces/BaseChatMemoryInput).**CombinedMemoryInput**

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### memories[](#memories "Direct link to memories")

> **memories**: [`BaseMemory`](/docs/api/memory/classes/BaseMemory)\[\]

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/memory/combined\_memory.ts:10](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/combined_memory.ts#L10)

### aiPrefix?[](#aiprefix "Direct link to aiPrefix?")

> **aiPrefix**: `string`

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/memory/combined\_memory.ts:12](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/combined_memory.ts#L12)

### chatHistory?[](#chathistory "Direct link to chatHistory?")

> **chatHistory**: [`BaseChatMessageHistory`](/docs/api/schema/classes/BaseChatMessageHistory)

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BaseChatMemoryInput](/docs/api/memory/interfaces/BaseChatMemoryInput).[chatHistory](/docs/api/memory/interfaces/BaseChatMemoryInput#chathistory)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:12](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L12)

### humanPrefix?[](#humanprefix "Direct link to humanPrefix?")

> **humanPrefix**: `string`

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/memory/combined\_memory.ts:11](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/combined_memory.ts#L11)

### inputKey?[](#inputkey "Direct link to inputKey?")

> **inputKey**: `string`

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[BaseChatMemoryInput](/docs/api/memory/interfaces/BaseChatMemoryInput).[inputKey](/docs/api/memory/interfaces/BaseChatMemoryInput#inputkey)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:14](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L14)

### memoryKey?[](#memorykey "Direct link to memoryKey?")

> **memoryKey**: `string`

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/memory/combined\_memory.ts:13](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/combined_memory.ts#L13)

### outputKey?[](#outputkey "Direct link to outputKey?")

> **outputKey**: `string`

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[BaseChatMemoryInput](/docs/api/memory/interfaces/BaseChatMemoryInput).[outputKey](/docs/api/memory/interfaces/BaseChatMemoryInput#outputkey)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:15](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L15)

### returnMessages?[](#returnmessages "Direct link to returnMessages?")

> **returnMessages**: `boolean`

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[BaseChatMemoryInput](/docs/api/memory/interfaces/BaseChatMemoryInput).[returnMessages](/docs/api/memory/interfaces/BaseChatMemoryInput#returnmessages)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/memory/chat\_memory.ts:13](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/chat_memory.ts#L13)