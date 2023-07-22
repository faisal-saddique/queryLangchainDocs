MomentoChatMessageHistoryProps
==============================

The settings to instantiate the Momento chat message history.

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### cacheName[​](#cachename "Direct link to cacheName")

> **cacheName**: `string`

The name of the cache to use to store the data.

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/stores/message/momento.ts:36](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/stores/message/momento.ts#L36)

### client[​](#client "Direct link to client")

> **client**: `ICacheClient`

The Momento cache client.

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/stores/message/momento.ts:32](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/stores/message/momento.ts#L32)

### sessionId[​](#sessionid "Direct link to sessionId")

> **sessionId**: `string`

The session ID to use to store the data.

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/stores/message/momento.ts:28](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/stores/message/momento.ts#L28)

### ensureCacheExists?[​](#ensurecacheexists "Direct link to ensureCacheExists?")

> **ensureCacheExists**: true

If true, ensure that the cache exists before returning. If false, the cache is not checked for existence. Defaults to true.

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/stores/message/momento.ts:47](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/stores/message/momento.ts#L47)

### sessionTtl?[​](#sessionttl "Direct link to sessionTtl?")

> **sessionTtl**: `number`

The time to live for the cache items in seconds. If not specified, the cache client default is used.

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/stores/message/momento.ts:41](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/stores/message/momento.ts#L41)