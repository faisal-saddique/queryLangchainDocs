Operation
=========

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`FilterDirective`](/docs/api/chains_query_constructor_ir/classes/FilterDirective).**Operation**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new Operation**(`operator`: [`Operator`](/docs/api/chains_query_constructor_ir/types/Operator), `args`?: [`FilterDirective`](/docs/api/chains_query_constructor_ir/classes/FilterDirective)\[\]): [`Operation`](/docs/api/chains_query_constructor_ir/classes/Operation)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`operator`

[`Operator`](/docs/api/chains_query_constructor_ir/types/Operator)

`args?`

[`FilterDirective`](/docs/api/chains_query_constructor_ir/classes/FilterDirective)\[\]

#### Returns[​](#returns "Direct link to Returns")

[`Operation`](/docs/api/chains_query_constructor_ir/classes/Operation)

#### Overrides[​](#overrides "Direct link to Overrides")

[FilterDirective](/docs/api/chains_query_constructor_ir/classes/FilterDirective).[constructor](/docs/api/chains_query_constructor_ir/classes/FilterDirective#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/chains/query\_constructor/ir.ts:108](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/query_constructor/ir.ts#L108)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### exprName[​](#exprname "Direct link to exprName")

> **exprName**: "Operation"

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[FilterDirective](/docs/api/chains_query_constructor_ir/classes/FilterDirective).[exprName](/docs/api/chains_query_constructor_ir/classes/FilterDirective#exprname)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/chains/query\_constructor/ir.ts:106](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/query_constructor/ir.ts#L106)

### operator[​](#operator "Direct link to operator")

> **operator**: [`Operator`](/docs/api/chains_query_constructor_ir/types/Operator)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/chains/query\_constructor/ir.ts:108](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/query_constructor/ir.ts#L108)

### args?[​](#args "Direct link to args?")

> **args**: [`FilterDirective`](/docs/api/chains_query_constructor_ir/classes/FilterDirective)\[\]

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/chains/query\_constructor/ir.ts:108](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/query_constructor/ir.ts#L108)

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

[FilterDirective](/docs/api/chains_query_constructor_ir/classes/FilterDirective).[accept](/docs/api/chains_query_constructor_ir/classes/FilterDirective#accept)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/chains/query\_constructor/ir.ts:78](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/query_constructor/ir.ts#L78)