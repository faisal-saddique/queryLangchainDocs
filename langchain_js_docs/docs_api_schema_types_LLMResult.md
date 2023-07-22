LLMResult
=========

> **LLMResult**: `object`

Contains all relevant information returned by an LLM.

Type declaration[​](#type-declaration "Direct link to Type declaration")
------------------------------------------------------------------------

Member

Type

Description

`generations`

[`Generation`](/docs/api/schema/interfaces/Generation)\[\]\[\]

List of the things generated. Each input could have multiple [generations](/docs/api/schema/interfaces/Generation), hence this is a list of lists.

`__run`?

`Record`<`string`, `any`\>

Dictionary of run metadata

`llmOutput`?

`Record`<`string`, `any`\>

Dictionary of arbitrary LLM-provider specific output.

Defined in[​](#defined-in "Direct link to Defined in")
------------------------------------------------------

[langchain/src/schema/index.ts:36](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/index.ts#L36)