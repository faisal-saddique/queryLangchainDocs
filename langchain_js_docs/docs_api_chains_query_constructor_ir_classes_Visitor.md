Visitor
=======

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseTranslator`](/docs/api/retrievers_self_query/classes/BaseTranslator)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new Visitor**(): [`Visitor`](/docs/api/chains_query_constructor_ir/classes/Visitor)

#### Returns[​](#returns "Direct link to Returns")

[`Visitor`](/docs/api/chains_query_constructor_ir/classes/Visitor)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### VisitComparisonOutput[​](#visitcomparisonoutput "Direct link to VisitComparisonOutput")

> **VisitComparisonOutput**: `object`

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/chains/query\_constructor/ir.ts:56](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/query_constructor/ir.ts#L56)

### VisitOperationOutput[​](#visitoperationoutput "Direct link to VisitOperationOutput")

> **VisitOperationOutput**: `object`

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/chains/query\_constructor/ir.ts:54](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/query_constructor/ir.ts#L54)

### VisitStructuredQueryOutput[​](#visitstructuredqueryoutput "Direct link to VisitStructuredQueryOutput")

> **VisitStructuredQueryOutput**: `object`

#### Type declaration[​](#type-declaration "Direct link to Type declaration")

Member

Type

`filter`?

`object`

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/chains/query\_constructor/ir.ts:58](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/query_constructor/ir.ts#L58)

### allowedComparators[​](#allowedcomparators "Direct link to allowedComparators")

> `Abstract` **allowedComparators**: [`Comparator`](/docs/api/chains_query_constructor_ir/types/Comparator)\[\]

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/chains/query\_constructor/ir.ts:62](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/query_constructor/ir.ts#L62)

### allowedOperators[​](#allowedoperators "Direct link to allowedOperators")

> `Abstract` **allowedOperators**: [`Operator`](/docs/api/chains_query_constructor_ir/types/Operator)\[\]

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/chains/query\_constructor/ir.ts:60](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/query_constructor/ir.ts#L60)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### visitComparison()[​](#visitcomparison "Direct link to visitComparison()")

> `Abstract` **visitComparison**(`comparison`: [`Comparison`](/docs/api/chains_query_constructor_ir/classes/Comparison)): `object`

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`comparison`

[`Comparison`](/docs/api/chains_query_constructor_ir/classes/Comparison)

#### Returns[​](#returns-1 "Direct link to Returns")

`object`

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/chains/query\_constructor/ir.ts:66](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/query_constructor/ir.ts#L66)

### visitOperation()[​](#visitoperation "Direct link to visitOperation()")

> `Abstract` **visitOperation**(`operation`: [`Operation`](/docs/api/chains_query_constructor_ir/classes/Operation)): `object`

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`operation`

[`Operation`](/docs/api/chains_query_constructor_ir/classes/Operation)

#### Returns[​](#returns-2 "Direct link to Returns")

`object`

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/chains/query\_constructor/ir.ts:64](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/query_constructor/ir.ts#L64)

### visitStructuredQuery()[​](#visitstructuredquery "Direct link to visitStructuredQuery()")

> `Abstract` **visitStructuredQuery**(`structuredQuery`: [`StructuredQuery`](/docs/api/chains_query_constructor_ir/classes/StructuredQuery)): `object`

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`structuredQuery`

[`StructuredQuery`](/docs/api/chains_query_constructor_ir/classes/StructuredQuery)

#### Returns[​](#returns-3 "Direct link to Returns")

`object`

Member

Type

`filter`?

`object`

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/chains/query\_constructor/ir.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/query_constructor/ir.ts#L70)