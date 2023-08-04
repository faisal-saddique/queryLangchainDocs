getInputValue()
===============

This function is used by memory classes to select the input value to use for the memory. If there is only one input value, it is used. If there are multiple input values, the inputKey must be specified.

> **getInputValue**(`inputValues`: `InputValues`, `inputKey`?: `string`): `any`

Parameters[](#parameters "Direct link to Parameters")
------------------------------------------------------

Parameter

Type

`inputValues`

`InputValues`

`inputKey?`

`string`

Returns[](#returns "Direct link to Returns")
---------------------------------------------

`any`

Defined in[](#defined-in "Direct link to Defined in")
------------------------------------------------------

[langchain/src/memory/base.ts:35](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/memory/base.ts#L35)