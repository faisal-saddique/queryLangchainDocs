getBufferString()
=================

This function is used by memory classes to get a string representation of the chat message history, based on the message content and role.

> **getBufferString**(`messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\], `humanPrefix`: `string` = `"Human"`, `aiPrefix`: `string` = `"AI"`): `string`

Parameters[​](#parameters "Direct link to Parameters")
------------------------------------------------------

Parameter

Type

Default value

`messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]

`undefined`

`humanPrefix`

`string`

`"Human"`

`aiPrefix`

`string`

`"AI"`

Returns[​](#returns "Direct link to Returns")
---------------------------------------------

`string`

Defined in[​](#defined-in "Direct link to Defined in")
------------------------------------------------------

[langchain/src/memory/base.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/memory/base.ts#L70)