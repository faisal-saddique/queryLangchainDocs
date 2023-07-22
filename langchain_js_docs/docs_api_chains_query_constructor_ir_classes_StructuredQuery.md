StructuredQuery
===============

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`Expression`](/docs/api/chains_query_constructor_ir/classes/Expression).**StructuredQuery**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new StructuredQuery**(`query`: `string`, `filter`?: [`FilterDirective`](/docs/api/chains_query_constructor_ir/classes/FilterDirective)): [`StructuredQuery`](/docs/api/chains_query_constructor_ir/classes/StructuredQuery)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`query`

`string`

`filter?`

[`FilterDirective`](/docs/api/chains_query_constructor_ir/classes/FilterDirective)

#### Returns[​](#returns "Direct link to Returns")

[`StructuredQuery`](/docs/api/chains_query_constructor_ir/classes/StructuredQuery)

#### Overrides[​](#overrides "Direct link to Overrides")

[Expression](/docs/api/chains_query_constructor_ir/classes/Expression).[constructor](/docs/api/chains_query_constructor_ir/classes/Expression#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/chains/query\_constructor/ir.ts:116](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/query_constructor/ir.ts#L116)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### exprName[​](#exprname "Direct link to exprName")

> **exprName**: "StructuredQuery"

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[Expression](/docs/api/chains_query_constructor_ir/classes/Expression).[exprName](/docs/api/chains_query_constructor_ir/classes/Expression#exprname)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/chains/query\_constructor/ir.ts:114](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/query_constructor/ir.ts#L114)

### query[​](#query "Direct link to query")

> **query**: `string`

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/chains/query\_constructor/ir.ts:116](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/query_constructor/ir.ts#L116)

### filter?[​](#filter "Direct link to filter?")

> **filter**: [`FilterDirective`](/docs/api/chains_query_constructor_ir/classes/FilterDirective)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/chains/query\_constructor/ir.ts:116](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/query_constructor/ir.ts#L116)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### accept()[​](#accept "Direct link to accept()")

> **accept**(`visitor`: [`Visitor`](/docs/api/chains_query_constructor_ir/classes/Visitor)): `object`

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`visitor`

[`Visitor`](/docs/api/chains_query_constructor_ir/classes/Visitor)

#### Returns[​](#returns-1 "Direct link to Returns")

`object`

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[Expression](/docs/api/chains_query_constructor_ir/classes/Expression).[accept](/docs/api/chains_query_constructor_ir/classes/Expression#accept)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/chains/query\_constructor/ir.ts:78](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/query_constructor/ir.ts#L78)