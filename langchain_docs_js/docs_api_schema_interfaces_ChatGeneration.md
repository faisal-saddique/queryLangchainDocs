ChatGeneration
==============

Output of a single generation.

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`Generation`](/docs/api/schema/interfaces/Generation).**ChatGeneration**

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### message[](#message "Direct link to message")

> **message**: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/schema/index.ts:390](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/index.ts#L390)

### text[](#text "Direct link to text")

> **text**: `string`

Generated text output

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[Generation](/docs/api/schema/interfaces/Generation).[text](/docs/api/schema/interfaces/Generation#text)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/schema/index.ts:24](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/index.ts#L24)

### generationInfo?[](#generationinfo "Direct link to generationInfo?")

> **generationInfo**: `Record`<`string`, `any`\>

Raw generation info response from the provider. May include things like reason for finishing (e.g. in OpenAI)

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[Generation](/docs/api/schema/interfaces/Generation).[generationInfo](/docs/api/schema/interfaces/Generation#generationinfo)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/schema/index.ts:30](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/index.ts#L30)