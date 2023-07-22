RedisVectorStoreConfig
======================

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### indexName[​](#indexname "Direct link to indexName")

> **indexName**: `string`

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/vectorstores/redis.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/redis.ts#L40)

### redisClient[​](#redisclient "Direct link to redisClient")

> **redisClient**: `RedisClientType`<{} & `RedisModules`, `RedisFunctions`, `RedisScripts`\> | `RedisClusterType`<{} & `RedisModules`, `RedisFunctions`, `RedisScripts`\>

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/vectorstores/redis.ts:37](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/redis.ts#L37)

### contentKey?[​](#contentkey "Direct link to contentKey?")

> **contentKey**: `string`

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/vectorstores/redis.ts:43](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/redis.ts#L43)

### filter?[​](#filter "Direct link to filter?")

> **filter**: [`RedisVectorStoreFilterType`](/docs/api/vectorstores_redis/types/RedisVectorStoreFilterType)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/vectorstores/redis.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/redis.ts#L46)

### indexOptions?[​](#indexoptions "Direct link to indexOptions?")

> **indexOptions**: [`CreateSchemaFlatVectorField`](/docs/api/vectorstores_redis/types/CreateSchemaFlatVectorField) | [`CreateSchemaHNSWVectorField`](/docs/api/vectorstores_redis/types/CreateSchemaHNSWVectorField)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/vectorstores/redis.ts:41](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/redis.ts#L41)

### keyPrefix?[​](#keyprefix "Direct link to keyPrefix?")

> **keyPrefix**: `string`

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/vectorstores/redis.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/redis.ts#L42)

### metadataKey?[​](#metadatakey "Direct link to metadataKey?")

> **metadataKey**: `string`

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/vectorstores/redis.ts:44](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/redis.ts#L44)

### vectorKey?[​](#vectorkey "Direct link to vectorKey?")

> **vectorKey**: `string`

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/vectorstores/redis.ts:45](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/redis.ts#L45)