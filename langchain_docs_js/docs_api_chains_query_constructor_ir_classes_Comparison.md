Comparison
==========

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`FilterDirective`](/docs/api/chains_query_constructor_ir/classes/FilterDirective).**Comparison**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new Comparison**(`comparator`: [`Comparator`](/docs/api/chains_query_constructor_ir/types/Comparator), `attribute`: `string`, `value`: `string` | `number`): [`Comparison`](/docs/api/chains_query_constructor_ir/classes/Comparison)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`comparator`

[`Comparator`](/docs/api/chains_query_constructor_ir/types/Comparator)

`attribute`

`string`

`value`

`string` | `number`

#### Returns[](#returns "Direct link to Returns")

[`Comparison`](/docs/api/chains_query_constructor_ir/classes/Comparison)

#### Overrides[](#overrides "Direct link to Overrides")

[FilterDirective](/docs/api/chains_query_constructor_ir/classes/FilterDirective).[constructor](/docs/api/chains_query_constructor_ir/classes/FilterDirective#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/chains/query\_constructor/ir.ts:96](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/query_constructor/ir.ts#L96)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### attribute[](#attribute "Direct link to attribute")

> **attribute**: `string`

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/chains/query\_constructor/ir.ts:98](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/query_constructor/ir.ts#L98)

### comparator[](#comparator "Direct link to comparator")

> **comparator**: [`Comparator`](/docs/api/chains_query_constructor_ir/types/Comparator)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/chains/query\_constructor/ir.ts:97](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/query_constructor/ir.ts#L97)

### exprName[](#exprname "Direct link to exprName")

> **exprName**: "Comparison"

#### Overrides[](#overrides-1 "Direct link to Overrides")

[FilterDirective](/docs/api/chains_query_constructor_ir/classes/FilterDirective).[exprName](/docs/api/chains_query_constructor_ir/classes/FilterDirective#exprname)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/chains/query\_constructor/ir.ts:94](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/query_constructor/ir.ts#L94)

### value[](#value "Direct link to value")

> **value**: `string` | `number`

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/chains/query\_constructor/ir.ts:99](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/query_constructor/ir.ts#L99)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### accept()[](#accept "Direct link to accept()")

> **accept**(`visitor`: [`Visitor`](/docs/api/chains_query_constructor_ir/classes/Visitor)): `object`

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`visitor`

[`Visitor`](/docs/api/chains_query_constructor_ir/classes/Visitor)

#### Returns[](#returns-1 "Direct link to Returns")

`object`

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[FilterDirective](/docs/api/chains_query_constructor_ir/classes/FilterDirective).[accept](/docs/api/chains_query_constructor_ir/classes/FilterDirective#accept)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/chains/query\_constructor/ir.ts:78](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/query_constructor/ir.ts#L78)