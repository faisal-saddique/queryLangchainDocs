FilterDirective
===============

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`Expression`](/docs/api/chains_query_constructor_ir/classes/Expression).**FilterDirective**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new FilterDirective**(): [`FilterDirective`](/docs/api/chains_query_constructor_ir/classes/FilterDirective)

#### Returns[](#returns "Direct link to Returns")

[`FilterDirective`](/docs/api/chains_query_constructor_ir/classes/FilterDirective)

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[Expression](/docs/api/chains_query_constructor_ir/classes/Expression).[constructor](/docs/api/chains_query_constructor_ir/classes/Expression#constructor)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### exprName[](#exprname "Direct link to exprName")

> `Abstract` **exprName**: "Operation" | "Comparison" | "StructuredQuery"

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[Expression](/docs/api/chains_query_constructor_ir/classes/Expression).[exprName](/docs/api/chains_query_constructor_ir/classes/Expression#exprname)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/chains/query\_constructor/ir.ts:76](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/query_constructor/ir.ts#L76)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### accept()[](#accept "Direct link to accept()")

> **accept**(`visitor`: [`Visitor`](/docs/api/chains_query_constructor_ir/classes/Visitor)): `object`

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`visitor`

[`Visitor`](/docs/api/chains_query_constructor_ir/classes/Visitor)

#### Returns[](#returns-1 "Direct link to Returns")

`object`

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[Expression](/docs/api/chains_query_constructor_ir/classes/Expression).[accept](/docs/api/chains_query_constructor_ir/classes/Expression#accept)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/chains/query\_constructor/ir.ts:78](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/query_constructor/ir.ts#L78)