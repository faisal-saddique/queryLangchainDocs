loadPrompt()
============

Load a prompt from [LangchainHub](https://github.com/hwchase17/langchain-hub) or local filesystem.

Example[](#example "Direct link to Example")
---------------------------------------------

Loading from LangchainHub:

    import { loadPrompt } from "langchain/prompts/load";const prompt = await loadPrompt("lc://prompts/hello-world/prompt.yaml");

Example[](#example-1 "Direct link to Example")
-----------------------------------------------

Loading from local filesystem:

    import { loadPrompt } from "langchain/prompts/load";const prompt = await loadPrompt("/path/to/prompt.json");

> **loadPrompt**(`uri`: `string`): `Promise`<[`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)<[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\>\>

Parameters[](#parameters "Direct link to Parameters")
------------------------------------------------------

Parameter

Type

`uri`

`string`

Returns[](#returns "Direct link to Returns")
---------------------------------------------

`Promise`<[`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)<[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\>\>

Defined in[](#defined-in "Direct link to Defined in")
------------------------------------------------------

[langchain/src/prompts/load.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/load.ts#L26)