BaseEntityStore
===============

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`Serializable`](/docs/api/load_serializable/classes/Serializable).**BaseEntityStore**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new BaseEntityStore**(`kwargs`?: `SerializedFields`, ...`_args`?: `never`\[\]): [`BaseEntityStore`](/docs/api/schema/classes/BaseEntityStore)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`kwargs?`

`SerializedFields`

`..._args?`

`never`\[\]

#### Returns[​](#returns "Direct link to Returns")

[`BaseEntityStore`](/docs/api/schema/classes/BaseEntityStore)

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[Serializable](/docs/api/load_serializable/classes/Serializable).[constructor](/docs/api/load_serializable/classes/Serializable#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/load/serializable.ts:94](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L94)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[Serializable](/docs/api/load_serializable/classes/Serializable).[lc\_kwargs](/docs/api/load_serializable/classes/Serializable#lc_kwargs)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

> `Abstract` **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[Serializable](/docs/api/load_serializable/classes/Serializable).[lc\_namespace](/docs/api/load_serializable/classes/Serializable#lc_namespace)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/load/serializable.ts:63](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L63)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[Serializable](/docs/api/load_serializable/classes/Serializable).[lc\_serializable](/docs/api/load_serializable/classes/Serializable#lc_serializable)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L55)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-1 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

Serializable.lc\_aliases

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[Serializable](/docs/api/load_serializable/classes/Serializable).[lc\_aliases](/docs/api/load_serializable/classes/Serializable#lc_aliases)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

Serializable.lc\_attributes

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

[Serializable](/docs/api/load_serializable/classes/Serializable).[lc\_attributes](/docs/api/load_serializable/classes/Serializable#lc_attributes)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

Serializable.lc\_secrets

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

[Serializable](/docs/api/load_serializable/classes/Serializable).[lc\_secrets](/docs/api/load_serializable/classes/Serializable#lc_secrets)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### clear()[​](#clear "Direct link to clear()")

> `Abstract` **clear**(): `Promise`<`void`\>

#### Returns[​](#returns-4 "Direct link to Returns")

`Promise`<`void`\>

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/schema/index.ts:305](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/index.ts#L305)

### delete()[​](#delete "Direct link to delete()")

> `Abstract` **delete**(`key`: `string`): `Promise`<`void`\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`key`

`string`

#### Returns[​](#returns-5 "Direct link to Returns")

`Promise`<`void`\>

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/schema/index.ts:301](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/index.ts#L301)

### exists()[​](#exists "Direct link to exists()")

> `Abstract` **exists**(`key`: `string`): `Promise`<`boolean`\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`key`

`string`

#### Returns[​](#returns-6 "Direct link to Returns")

`Promise`<`boolean`\>

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/schema/index.ts:303](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/index.ts#L303)

### get()[​](#get "Direct link to get()")

> `Abstract` **get**(`key`: `string`, `defaultValue`?: `string`): `Promise`<`undefined` | `string`\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`key`

`string`

`defaultValue?`

`string`

#### Returns[​](#returns-7 "Direct link to Returns")

`Promise`<`undefined` | `string`\>

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/schema/index.ts:297](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/index.ts#L297)

### set()[​](#set "Direct link to set()")

> `Abstract` **set**(`key`: `string`, `value`?: `string`): `Promise`<`void`\>

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`key`

`string`

`value?`

`string`

#### Returns[​](#returns-8 "Direct link to Returns")

`Promise`<`void`\>

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/schema/index.ts:299](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/index.ts#L299)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-9 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

[Serializable](/docs/api/load_serializable/classes/Serializable).[toJSON](/docs/api/load_serializable/classes/Serializable#tojson)

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-10 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

[Serializable](/docs/api/load_serializable/classes/Serializable).[toJSONNotImplemented](/docs/api/load_serializable/classes/Serializable#tojsonnotimplemented)

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)