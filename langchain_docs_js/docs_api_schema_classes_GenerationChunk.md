GenerationChunk
===============

Chunk of a single generation. Used for streaming.

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`ChatGenerationChunk`](/docs/api/schema/classes/ChatGenerationChunk)

Implements[](#implements "Direct link to Implements")
------------------------------------------------------

*   [`Generation`](/docs/api/schema/interfaces/Generation)

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new GenerationChunk**(`fields`: [`GenerationChunkFields`](/docs/api/schema/types/GenerationChunkFields)): [`GenerationChunk`](/docs/api/schema/classes/GenerationChunk)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`fields`

[`GenerationChunkFields`](/docs/api/schema/types/GenerationChunkFields)

#### Returns[](#returns "Direct link to Returns")

[`GenerationChunk`](/docs/api/schema/classes/GenerationChunk)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/schema/index.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/index.ts#L48)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### text[](#text "Direct link to text")

> **text**: `string`

Generated text output

#### Implementation of[](#implementation-of "Direct link to Implementation of")

[Generation](/docs/api/schema/interfaces/Generation).[text](/docs/api/schema/interfaces/Generation#text)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/schema/index.ts:43](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/index.ts#L43)

### generationInfo?[](#generationinfo "Direct link to generationInfo?")

> **generationInfo**: `Record`<`string`, `any`\>

Raw generation info response from the provider. May include things like reason for finishing (e.g. in OpenAI)

#### Implementation of[](#implementation-of-1 "Direct link to Implementation of")

[Generation](/docs/api/schema/interfaces/Generation).[generationInfo](/docs/api/schema/interfaces/Generation#generationinfo)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/schema/index.ts:46](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/index.ts#L46)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### concat()[](#concat "Direct link to concat()")

> **concat**(`chunk`: [`GenerationChunk`](/docs/api/schema/classes/GenerationChunk)): [`GenerationChunk`](/docs/api/schema/classes/GenerationChunk)

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`chunk`

[`GenerationChunk`](/docs/api/schema/classes/GenerationChunk)

#### Returns[](#returns-1 "Direct link to Returns")

[`GenerationChunk`](/docs/api/schema/classes/GenerationChunk)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/schema/index.ts:53](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/index.ts#L53)