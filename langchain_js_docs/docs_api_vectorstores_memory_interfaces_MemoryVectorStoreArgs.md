MemoryVectorStoreArgs
=====================

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### similarity?[​](#similarity "Direct link to similarity?")

> **similarity**: `Function`

#### Type declaration[​](#type-declaration "Direct link to Type declaration")

Returns the average of cosine distances between vectors a and b

> (`a`: `NumberArray`, `b`: `NumberArray`): `number`

##### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

Description

`a`

`NumberArray`

first vector

`b`

`NumberArray`

second vector

##### Returns[​](#returns "Direct link to Returns")

`number`

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/vectorstores/memory.ts:14](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/memory.ts#L14)