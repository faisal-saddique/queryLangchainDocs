consumeCallback()
=================

Consume a promise, either adding it to the queue or waiting for it to resolve

> **consumeCallback**<T\>(`promiseFn`: `Function`, `wait`: `boolean`): `Promise`<`void`\>

Type parameters[​](#type-parameters "Direct link to Type parameters")
---------------------------------------------------------------------

*   `T`

Parameters[​](#parameters "Direct link to Parameters")
------------------------------------------------------

Parameter

Type

Description

`promiseFn`

() => `void` | `T` | `Promise`<`T`\>

\-

`wait`

`boolean`

Whether to wait for the promise to resolve or resolve immediately

Returns[​](#returns "Direct link to Returns")
---------------------------------------------

`Promise`<`void`\>

Defined in[​](#defined-in "Direct link to Defined in")
------------------------------------------------------

[langchain/src/callbacks/promises.ts:18](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/promises.ts#L18)