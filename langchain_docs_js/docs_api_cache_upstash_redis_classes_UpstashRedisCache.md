UpstashRedisCache
=================

A cache that uses Upstash as the backing store. See [https://docs.upstash.com/redis](https://docs.upstash.com/redis).

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseCache`](/docs/api/schema/classes/BaseCache).**UpstashRedisCache**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new UpstashRedisCache**(`props`: [`UpstashRedisCacheProps`](/docs/api/cache_upstash_redis/types/UpstashRedisCacheProps)): [`UpstashRedisCache`](/docs/api/cache_upstash_redis/classes/UpstashRedisCache)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`props`

[`UpstashRedisCacheProps`](/docs/api/cache_upstash_redis/types/UpstashRedisCacheProps)

#### Returns[](#returns "Direct link to Returns")

[`UpstashRedisCache`](/docs/api/cache_upstash_redis/classes/UpstashRedisCache)

#### Overrides[](#overrides "Direct link to Overrides")

[BaseCache](/docs/api/schema/classes/BaseCache).[constructor](/docs/api/schema/classes/BaseCache#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/cache/upstash\_redis.ts:24](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/cache/upstash_redis.ts#L24)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### lookup()[](#lookup "Direct link to lookup()")

Lookup LLM generations in cache by prompt and associated LLM key.

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

[langchain/src/cache/upstash\_redis.ts:42](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/cache/upstash_redis.ts#L42)

### update()[](#update "Direct link to update()")

Update the cache with the given generations.

Note this overwrites any existing generations for the given prompt and LLM key.

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

[langchain/src/cache/upstash\_redis.ts:67](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/cache/upstash_redis.ts#L67)