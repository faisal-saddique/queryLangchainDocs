RedisCache
==========

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseCache`](/docs/api/schema/classes/BaseCache).**RedisCache**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new RedisCache**(`redisClient`: `RedisClientType`): [`RedisCache`](/docs/api/cache_redis/classes/RedisCache)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`redisClient`

`RedisClientType`

#### Returns[](#returns "Direct link to Returns")

[`RedisCache`](/docs/api/cache_redis/classes/RedisCache)

#### Overrides[](#overrides "Direct link to Overrides")

[BaseCache](/docs/api/schema/classes/BaseCache).[constructor](/docs/api/schema/classes/BaseCache#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/cache/redis.ts:13](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/cache/redis.ts#L13)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### lookup()[](#lookup "Direct link to lookup()")

> **lookup**(`prompt`: `string`, `llmKey`: `string`): `Promise`<null | [`Generation`](/docs/api/schema/interfaces/Generation)\[\]\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`prompt`

`string`

`llmKey`

`string`

#### Returns[](#returns-1 "Direct link to Returns")

`Promise`<null | [`Generation`](/docs/api/schema/interfaces/Generation)\[\]\>

#### Overrides[](#overrides-1 "Direct link to Overrides")

[BaseCache](/docs/api/schema/classes/BaseCache).[lookup](/docs/api/schema/classes/BaseCache#lookup)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/cache/redis.ts:18](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/cache/redis.ts#L18)

### update()[](#update "Direct link to update()")

> **update**(`prompt`: `string`, `llmKey`: `string`, `value`: [`Generation`](/docs/api/schema/interfaces/Generation)\[\]): `Promise`<`void`\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`prompt`

`string`

`llmKey`

`string`

`value`

[`Generation`](/docs/api/schema/interfaces/Generation)\[\]

#### Returns[](#returns-2 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[](#overrides-2 "Direct link to Overrides")

[BaseCache](/docs/api/schema/classes/BaseCache).[update](/docs/api/schema/classes/BaseCache#update)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/cache/redis.ts:38](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/cache/redis.ts#L38)