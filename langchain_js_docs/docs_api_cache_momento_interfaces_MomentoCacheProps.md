MomentoCacheProps
=================

The settings to instantiate the Momento standard cache.

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### cacheName[​](#cachename "Direct link to cacheName")

> **cacheName**: `string`

The name of the cache to use to store the data.

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/cache/momento.ts:24](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/cache/momento.ts#L24)

### client[​](#client "Direct link to client")

> **client**: `ICacheClient`

The Momento cache client.

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/cache/momento.ts:20](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/cache/momento.ts#L20)

### ensureCacheExists?[​](#ensurecacheexists "Direct link to ensureCacheExists?")

> **ensureCacheExists**: true

If true, ensure that the cache exists before returning. If false, the cache is not checked for existence. Defaults to true.

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/cache/momento.ts:35](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/cache/momento.ts#L35)

### ttlSeconds?[​](#ttlseconds "Direct link to ttlSeconds?")

> **ttlSeconds**: `number`

The time to live for the cache items. If not specified, the cache client default is used.

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/cache/momento.ts:29](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/cache/momento.ts#L29)