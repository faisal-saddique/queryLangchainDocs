BaseCache<T\>
=============

Type parameters[​](#type-parameters "Direct link to Type parameters")
---------------------------------------------------------------------

*   `T` = [`Generation`](/docs/api/schema/interfaces/Generation)\[\]

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`InMemoryCache`](/docs/api/cache/classes/InMemoryCache)
*   [`MomentoCache`](/docs/api/cache_momento/classes/MomentoCache)
*   [`RedisCache`](/docs/api/cache_redis/classes/RedisCache)
*   [`UpstashRedisCache`](/docs/api/cache_upstash_redis/classes/UpstashRedisCache)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new BaseCache**<T\>(): [`BaseCache`](/docs/api/schema/classes/BaseCache)<`T`\>

#### Type parameters[​](#type-parameters-1 "Direct link to Type parameters")

*   `T` = [`Generation`](/docs/api/schema/interfaces/Generation)\[\]

#### Returns[​](#returns "Direct link to Returns")

[`BaseCache`](/docs/api/schema/classes/BaseCache)<`T`\>

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### lookup()[​](#lookup "Direct link to lookup()")

> `Abstract` **lookup**(`prompt`: `string`, `llmKey`: `string`): `Promise`<null | `T`\>

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`prompt`

`string`

`llmKey`

`string`

#### Returns[​](#returns-1 "Direct link to Returns")

`Promise`<null | `T`\>

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/schema/index.ts:285](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/index.ts#L285)

### update()[​](#update "Direct link to update()")

> `Abstract` **update**(`prompt`: `string`, `llmKey`: `string`, `value`: `T`): `Promise`<`void`\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

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

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/schema/index.ts:287](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/index.ts#L287)