ChatGenerationChunk
===================

Output of a single generation.

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`GenerationChunk`](/docs/api/schema/classes/GenerationChunk).**ChatGenerationChunk**

Implements[](#implements "Direct link to Implements")
------------------------------------------------------

*   [`ChatGeneration`](/docs/api/schema/interfaces/ChatGeneration)

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new ChatGenerationChunk**(`fields`: [`ChatGenerationChunkFields`](/docs/api/schema/types/ChatGenerationChunkFields)): [`ChatGenerationChunk`](/docs/api/schema/classes/ChatGenerationChunk)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`fields`

[`ChatGenerationChunkFields`](/docs/api/schema/types/ChatGenerationChunkFields)

#### Returns[](#returns "Direct link to Returns")

[`ChatGenerationChunk`](/docs/api/schema/classes/ChatGenerationChunk)

#### Overrides[](#overrides "Direct link to Overrides")

[GenerationChunk](/docs/api/schema/classes/GenerationChunk).[constructor](/docs/api/schema/classes/GenerationChunk#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/schema/index.ts:403](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/index.ts#L403)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### message[](#message "Direct link to message")

> **message**: [`BaseMessageChunk`](/docs/api/schema/classes/BaseMessageChunk)

#### Implementation of[](#implementation-of "Direct link to Implementation of")

[ChatGeneration](/docs/api/schema/interfaces/ChatGeneration).[message](/docs/api/schema/interfaces/ChatGeneration#message)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/schema/index.ts:401](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/index.ts#L401)

### text[](#text "Direct link to text")

> **text**: `string`

Generated text output

#### Implementation of[](#implementation-of-1 "Direct link to Implementation of")

[ChatGeneration](/docs/api/schema/interfaces/ChatGeneration).[text](/docs/api/schema/interfaces/ChatGeneration#text)

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[GenerationChunk](/docs/api/schema/classes/GenerationChunk).[text](/docs/api/schema/classes/GenerationChunk#text)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/schema/index.ts:43](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/index.ts#L43)

### generationInfo?[](#generationinfo "Direct link to generationInfo?")

> **generationInfo**: `Record`<`string`, `any`\>

Raw generation info response from the provider. May include things like reason for finishing (e.g. in OpenAI)

#### Implementation of[](#implementation-of-2 "Direct link to Implementation of")

[ChatGeneration](/docs/api/schema/interfaces/ChatGeneration).[generationInfo](/docs/api/schema/interfaces/ChatGeneration#generationinfo)

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[GenerationChunk](/docs/api/schema/classes/GenerationChunk).[generationInfo](/docs/api/schema/classes/GenerationChunk#generationinfo)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/schema/index.ts:46](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/index.ts#L46)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### concat()[](#concat "Direct link to concat()")

> **concat**(`chunk`: [`ChatGenerationChunk`](/docs/api/schema/classes/ChatGenerationChunk)): [`ChatGenerationChunk`](/docs/api/schema/classes/ChatGenerationChunk)

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`chunk`

[`ChatGenerationChunk`](/docs/api/schema/classes/ChatGenerationChunk)

#### Returns[](#returns-1 "Direct link to Returns")

[`ChatGenerationChunk`](/docs/api/schema/classes/ChatGenerationChunk)

#### Overrides[](#overrides-1 "Direct link to Overrides")

[GenerationChunk](/docs/api/schema/classes/GenerationChunk).[concat](/docs/api/schema/classes/GenerationChunk#concat)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/schema/index.ts:408](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/index.ts#L408)