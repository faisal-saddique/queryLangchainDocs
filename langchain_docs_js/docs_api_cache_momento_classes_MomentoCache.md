MomentoCache
============

A cache that uses Momento as the backing store. See [https://gomomento.com](https://gomomento.com).

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseCache`](/docs/api/schema/classes/BaseCache).**MomentoCache**

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### lookup()[](#lookup "Direct link to lookup()")

Lookup LLM generations in cache by prompt and associated LLM key.

> **lookup**(`prompt`: `string`, `llmKey`: `string`): `Promise`<null | [`Generation`](/docs/api/schema/interfaces/Generation)\[\]\>

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

Description

`prompt`

`string`

The prompt to lookup.

`llmKey`

`string`

The LLM key to lookup.

#### Returns[](#returns "Direct link to Returns")

`Promise`<null | [`Generation`](/docs/api/schema/interfaces/Generation)\[\]\>

The generations associated with the prompt and LLM key, or null if not found.

#### Overrides[](#overrides "Direct link to Overrides")

[BaseCache](/docs/api/schema/classes/BaseCache).[lookup](/docs/api/schema/classes/BaseCache#lookup)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/cache/momento.ts:97](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/cache/momento.ts#L97)

### update()[](#update "Direct link to update()")

Update the cache with the given generations.

Note this overwrites any existing generations for the given prompt and LLM key.

> **update**(`prompt`: `string`, `llmKey`: `string`, `value`: [`Generation`](/docs/api/schema/interfaces/Generation)\[\]): `Promise`<`void`\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

Description

`prompt`

`string`

The prompt to update.

`llmKey`

`string`

The LLM key to update.

`value`

[`Generation`](/docs/api/schema/interfaces/Generation)\[\]

The generations to store.

#### Returns[](#returns-1 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[](#overrides-1 "Direct link to Overrides")

[BaseCache](/docs/api/schema/classes/BaseCache).[update](/docs/api/schema/classes/BaseCache#update)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/cache/momento.ts:125](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/cache/momento.ts#L125)

### fromProps()[](#fromprops "Direct link to fromProps()")

Create a new standard cache backed by Momento.

#### Throws[](#throws "Direct link to Throws")

InvalidArgumentError if props.ttlSeconds is not strictly positive.

> `Static` **fromProps**(`props`: [`MomentoCacheProps`](/docs/api/cache_momento/interfaces/MomentoCacheProps)): `Promise`<[`MomentoCache`](/docs/api/cache_momento/classes/MomentoCache)\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

Description

`props`

[`MomentoCacheProps`](/docs/api/cache_momento/interfaces/MomentoCacheProps)

The settings to instantiate the cache.

#### Returns[](#returns-2 "Direct link to Returns")

`Promise`<[`MomentoCache`](/docs/api/cache_momento/classes/MomentoCache)\>

The Momento-backed cache.

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/cache/momento.ts:71](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/cache/momento.ts#L71)