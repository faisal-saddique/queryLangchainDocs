DynamicStructuredToolInput<T\>
==============================

Type parameters[](#type-parameters "Direct link to Type parameters")
---------------------------------------------------------------------

*   `T` _extends_ `z.ZodObject`<`any`, `any`, `any`, `any`\> = `z.ZodObject`<`any`, `any`, `any`, `any`\>

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   `BaseDynamicToolInput`.**DynamicStructuredToolInput**

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### description[](#description "Direct link to description")

> **description**: `string`

#### Inherited from[](#inherited-from "Direct link to Inherited from")

BaseDynamicToolInput.description

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/tools/dynamic.ts:7](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/dynamic.ts#L7)

### func[](#func "Direct link to func")

> **func**: `Function`

#### Type declaration[](#type-declaration "Direct link to Type declaration")

> (`input`: `TypeOf`<`T`\>, `runManager`?: [`CallbackManagerForToolRun`](/docs/api/callbacks/classes/CallbackManagerForToolRun)): `Promise`<`string`\>

##### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`input`

`TypeOf`<`T`\>

`runManager?`

[`CallbackManagerForToolRun`](/docs/api/callbacks/classes/CallbackManagerForToolRun)

##### Returns[](#returns "Direct link to Returns")

`Promise`<`string`\>

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/tools/dynamic.ts:22](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/dynamic.ts#L22)

### name[](#name "Direct link to name")

> **name**: `string`

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

BaseDynamicToolInput.name

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/tools/dynamic.ts:6](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/dynamic.ts#L6)

### schema[](#schema "Direct link to schema")

> **schema**: `T`

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/tools/dynamic.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/dynamic.ts#L26)

### callbacks?[](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

BaseDynamicToolInput.callbacks

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:25](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L25)

### metadata?[](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

BaseDynamicToolInput.metadata

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:27](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L27)

### returnDirect?[](#returndirect "Direct link to returnDirect?")

> **returnDirect**: `boolean`

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

BaseDynamicToolInput.returnDirect

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/tools/dynamic.ts:8](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/tools/dynamic.ts#L8)

### tags?[](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

BaseDynamicToolInput.tags

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L26)

### verbose?[](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

BaseDynamicToolInput.verbose

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:24](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L24)