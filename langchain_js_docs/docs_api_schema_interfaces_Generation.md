Generation
==========

Output of a single generation.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`ChatGeneration`](/docs/api/schema/interfaces/ChatGeneration)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### text[​](#text "Direct link to text")

> **text**: `string`

Generated text output

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/schema/index.ts:24](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/index.ts#L24)

### generationInfo?[​](#generationinfo "Direct link to generationInfo?")

> **generationInfo**: `Record`<`string`, `any`\>

Raw generation info response from the provider. May include things like reason for finishing (e.g. in OpenAI)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/schema/index.ts:30](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/index.ts#L30)