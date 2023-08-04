createOpenAPIChain()
====================

Create a chain for querying an API from a OpenAPI spec.

> **createOpenAPIChain**(`spec`: `string` | `Document`<{}\>, `options`: [`OpenAPIChainOptions`](/docs/api/chains/types/OpenAPIChainOptions) = `{}`): `Promise`<[`SequentialChain`](/docs/api/chains/classes/SequentialChain)\>

Parameters[](#parameters "Direct link to Parameters")
------------------------------------------------------

Parameter

Type

Description

`spec`

`string` | `Document`<{}\>

OpenAPISpec or url/file/text string corresponding to one.

`options`

[`OpenAPIChainOptions`](/docs/api/chains/types/OpenAPIChainOptions)

Custom options passed into the chain

Returns[](#returns "Direct link to Returns")
---------------------------------------------

`Promise`<[`SequentialChain`](/docs/api/chains/classes/SequentialChain)\>

OpenAPIChain

Defined in[](#defined-in "Direct link to Defined in")
------------------------------------------------------

[langchain/src/chains/openai\_functions/openapi.ts:408](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/openai_functions/openapi.ts#L408)