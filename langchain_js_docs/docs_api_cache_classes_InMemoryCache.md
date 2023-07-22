InMemoryCache<T\>
=================

Type parameters[​](#type-parameters "Direct link to Type parameters")
---------------------------------------------------------------------

*   `T` = [`Generation`](/docs/api/schema/interfaces/Generation)\[\]

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseCache`](/docs/api/schema/classes/BaseCache)<`T`\>.**InMemoryCache**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new InMemoryCache**<T\>(`map`?: `Map`<`string`, `T`\>): [`InMemoryCache`](/docs/api/cache/classes/InMemoryCache)<`T`\>

#### Type parameters[​](#type-parameters-1 "Direct link to Type parameters")

*   `T` = [`Generation`](/docs/api/schema/interfaces/Generation)\[\]

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`map?`

`Map`<`string`, `T`\>

#### Returns[​](#returns "Direct link to Returns")

[`InMemoryCache`](/docs/api/cache/classes/InMemoryCache)<`T`\>

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseCache](/docs/api/schema/classes/BaseCache).[constructor](/docs/api/schema/classes/BaseCache#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/cache/index.ts:9](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/cache/index.ts#L9)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### lookup()[​](#lookup "Direct link to lookup()")

> **lookup**(`prompt`: `string`, `llmKey`: `string`): `Promise`<null | `T`\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`prompt`

`string`

`llmKey`

`string`

#### Returns[​](#returns-1 "Direct link to Returns")

`Promise`<null | `T`\>

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[BaseCache](/docs/api/schema/classes/BaseCache).[lookup](/docs/api/schema/classes/BaseCache#lookup)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/cache/index.ts:14](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/cache/index.ts#L14)

### update()[​](#update "Direct link to update()")

> **update**(`prompt`: `string`, `llmKey`: `string`, `value`: `T`): `Promise`<`void`\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`prompt`

`string`

`llmKey`

`string`

`value`

`T`

#### Returns[​](#returns-2 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[BaseCache](/docs/api/schema/classes/BaseCache).[update](/docs/api/schema/classes/BaseCache#update)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/cache/index.ts:18](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/cache/index.ts#L18)

### global()[​](#global "Direct link to global()")

> `Static` **global**(): [`InMemoryCache`](/docs/api/cache/classes/InMemoryCache)<[`Generation`](/docs/api/schema/interfaces/Generation)\[\]\>

#### Returns[​](#returns-3 "Direct link to Returns")

[`InMemoryCache`](/docs/api/cache/classes/InMemoryCache)<[`Generation`](/docs/api/schema/interfaces/Generation)\[\]\>

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/cache/index.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/cache/index.ts#L22)