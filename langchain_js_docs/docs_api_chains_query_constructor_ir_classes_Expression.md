Expression
==========

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`FilterDirective`](/docs/api/chains_query_constructor_ir/classes/FilterDirective)
*   [`StructuredQuery`](/docs/api/chains_query_constructor_ir/classes/StructuredQuery)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new Expression**(): [`Expression`](/docs/api/chains_query_constructor_ir/classes/Expression)

#### Returns[​](#returns "Direct link to Returns")

[`Expression`](/docs/api/chains_query_constructor_ir/classes/Expression)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### exprName[​](#exprname "Direct link to exprName")

> `Abstract` **exprName**: "Operation" | "Comparison" | "StructuredQuery"

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/chains/query\_constructor/ir.ts:76](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/query_constructor/ir.ts#L76)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### accept()[​](#accept "Direct link to accept()")

> **accept**(`visitor`: [`Visitor`](/docs/api/chains_query_constructor_ir/classes/Visitor)): `object`

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`visitor`

[`Visitor`](/docs/api/chains_query_constructor_ir/classes/Visitor)

#### Returns[​](#returns-1 "Direct link to Returns")

`object`

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/chains/query\_constructor/ir.ts:78](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/query_constructor/ir.ts#L78)