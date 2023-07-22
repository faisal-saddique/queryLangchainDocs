StructuredTool<T\>
==================

Base class for Tools that accept input of any shape defined by a Zod schema.

Type parameters[​](#type-parameters "Direct link to Type parameters")
---------------------------------------------------------------------

*   `T` _extends_ `z.ZodObject`<`any`, `any`, `any`, `any`\> = `z.ZodObject`<`any`, `any`, `any`, `any`\>

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseLangChain`](/docs/api/base_language/classes/BaseLangChain).**StructuredTool**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new StructuredTool**<T\>(`fields`?: [`ToolParams`](/docs/api/tools/interfaces/ToolParams)): [`StructuredTool`](/docs/api/tools/classes/StructuredTool)<`T`\>

#### Type parameters[​](#type-parameters-1 "Direct link to Type parameters")

*   `T` _extends_ `ZodObject`<`any`, `any`, `any`, `any`, {}, `T`\> = `ZodObject`<`any`, `any`, `any`, `any`, {}\>

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields?`

[`ToolParams`](/docs/api/tools/interfaces/ToolParams)

#### Returns[​](#returns "Direct link to Returns")

[`StructuredTool`](/docs/api/tools/classes/StructuredTool)<`T`\>

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[constructor](/docs/api/base_language/classes/BaseLangChain#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/tools/base.ts:26](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/base.ts#L26)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### description[​](#description "Direct link to description")

> `Abstract` **description**: `string`

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/tools/base.ts:69](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/base.ts#L69)

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[lc\_kwargs](/docs/api/base_language/classes/BaseLangChain#lc_kwargs)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[lc\_serializable](/docs/api/base_language/classes/BaseLangChain#lc_serializable)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L55)

### name[​](#name "Direct link to name")

> `Abstract` **name**: `string`

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/tools/base.ts:67](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/base.ts#L67)

### returnDirect[​](#returndirect "Direct link to returnDirect")

> **returnDirect**: `boolean` = `false`

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/tools/base.ts:71](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/base.ts#L71)

### schema[​](#schema "Direct link to schema")

> `Abstract` **schema**: `T` | `ZodEffects`<`T`, `output`<`T`\>, `input`<`T`\>\>

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/tools/base.ts:20](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/base.ts#L20)

### verbose[​](#verbose "Direct link to verbose")

> **verbose**: `boolean`

Whether to print out response text.

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[verbose](/docs/api/base_language/classes/BaseLangChain#verbose)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:38](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L38)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[callbacks](/docs/api/base_language/classes/BaseLangChain#callbacks)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L40)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[metadata](/docs/api/base_language/classes/BaseLangChain#metadata)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:44](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L44)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[tags](/docs/api/base_language/classes/BaseLangChain#tags)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L42)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-1 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

BaseLangChain.lc\_aliases

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[lc\_aliases](/docs/api/base_language/classes/BaseLangChain#lc_aliases)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

BaseLangChain.lc\_attributes

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[lc\_attributes](/docs/api/base_language/classes/BaseLangChain#lc_attributes)

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

> **lc\_namespace**(): `string`\[\]

#### Returns[​](#returns-3 "Direct link to Returns")

`string`\[\]

#### Overrides[​](#overrides-1 "Direct link to Overrides")

BaseLangChain.lc\_namespace

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/tools/base.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/base.ts#L22)

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[lc\_namespace](/docs/api/base_language/classes/BaseLangChain#lc_namespace)

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/tools/base.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/base.ts#L22)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-4 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

BaseLangChain.lc\_secrets

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[lc\_secrets](/docs/api/base_language/classes/BaseLangChain#lc_secrets)

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### call()[​](#call "Direct link to call()")

> **call**(`arg`: `input`<`T`\> | `output`<`T`\> _extends_ `string` ? `string` : `never`, `configArg`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`, `tags`?: `string`\[\]): `Promise`<`string`\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

Description

`arg`

`input`<`T`\> | `output`<`T`\> _extends_ `string` ? `string` : `never`

\-

`configArg?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`

\-

`tags?`

`string`\[\]

`Deprecated`  
  

#### Returns[​](#returns-5 "Direct link to Returns")

`Promise`<`string`\>

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/tools/base.ts:35](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/base.ts#L35)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-6 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[toJSON](/docs/api/base_language/classes/BaseLangChain#tojson)

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-7 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[toJSONNotImplemented](/docs/api/base_language/classes/BaseLangChain#tojsonnotimplemented)

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)

### \_call()[​](#_call "Direct link to _call")

> `Protected` `Abstract` **\_call**(`arg`: `output`<`T`\>, `runManager`?: [`CallbackManagerForToolRun`](/docs/api/callbacks/classes/CallbackManagerForToolRun)): `Promise`<`string`\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`arg`

`output`<`T`\>

`runManager?`

[`CallbackManagerForToolRun`](/docs/api/callbacks/classes/CallbackManagerForToolRun)

#### Returns[​](#returns-8 "Direct link to Returns")

`Promise`<`string`\>

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/tools/base.ts:30](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/base.ts#L30)