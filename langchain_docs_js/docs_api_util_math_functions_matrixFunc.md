matrixFunc()
============

Apply a row-wise function between two matrices with the same number of columns.

Throws[](#throws "Direct link to Throws")
------------------------------------------

If the number of columns in X and Y are not the same.

> **matrixFunc**(`X`: `number`\[\]\[\], `Y`: `number`\[\]\[\], `func`: `VectorFunction`): `number`\[\]\[\]

Parameters[](#parameters "Direct link to Parameters")
------------------------------------------------------

Parameter

Type

Description

`X`

`number`\[\]\[\]

The first matrix.

`Y`

`number`\[\]\[\]

The second matrix.

`func`

`VectorFunction`

The function to apply.

Returns[](#returns "Direct link to Returns")
---------------------------------------------

`number`\[\]\[\]

A matrix where each row represents the result of applying the function between the corresponding rows of X and Y.

Defined in[](#defined-in "Direct link to Defined in")
------------------------------------------------------

[langchain/src/util/math.ts:20](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/util/math.ts#L20)