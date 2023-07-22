loadChain()
===========

Load a chain from [LangchainHub](https://github.com/hwchase17/langchain-hub) or local filesystem.

Example[​](#example "Direct link to Example")
---------------------------------------------

Loading from LangchainHub:

    import { loadChain } from "langchain/chains/load";const chain = await loadChain("lc://chains/hello-world/chain.json");const res = await chain.call({ topic: "my favorite color" });

Example[​](#example-1 "Direct link to Example")
-----------------------------------------------

Loading from local filesystem:

    import { loadChain } from "langchain/chains/load";const chain = await loadChain("/path/to/chain.json");

> **loadChain**(`uri`: `string`, `values`: `LoadValues` = `{}`): `Promise`<[`BaseChain`](/docs/api/chains/classes/BaseChain)\>

Parameters[​](#parameters "Direct link to Parameters")
------------------------------------------------------

Parameter

Type

`uri`

`string`

`values`

`LoadValues`

Returns[​](#returns "Direct link to Returns")
---------------------------------------------

`Promise`<[`BaseChain`](/docs/api/chains/classes/BaseChain)\>

Defined in[​](#defined-in "Direct link to Defined in")
------------------------------------------------------

[langchain/src/chains/load.ts:33](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/load.ts#L33)