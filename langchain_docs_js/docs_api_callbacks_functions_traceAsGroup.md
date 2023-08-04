traceAsGroup()
==============

> **traceAsGroup**<T, A\>(`groupOptions`: {`name`: `string`;} & `LangChainTracerFields`, `enclosedCode`: `Function`, ...`args`: `A`): `Promise`<`T`\>

Type parameters[](#type-parameters "Direct link to Type parameters")
---------------------------------------------------------------------

*   `T`
*   `A` _extends_ `any`\[\]

Parameters[](#parameters "Direct link to Parameters")
------------------------------------------------------

Parameter

Type

`groupOptions`

{`name`: `string`;} & `LangChainTracerFields`

`enclosedCode`

(`manager`: [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager), ...`args`: `A`) => `Promise`<`T`\>

`...args`

`A`

Returns[](#returns "Direct link to Returns")
---------------------------------------------

`Promise`<`T`\>

Defined in[](#defined-in "Direct link to Defined in")
------------------------------------------------------

[langchain/src/callbacks/manager.ts:933](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L933)