BasicTranslator
===============

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseTranslator`](/docs/api/retrievers_self_query/classes/BaseTranslator).**BasicTranslator**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new BasicTranslator**(`opts`?: `TranslatorOpts`): [`BasicTranslator`](/docs/api/retrievers_self_query/classes/BasicTranslator)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`opts?`

`TranslatorOpts`

#### Returns[​](#returns "Direct link to Returns")

[`BasicTranslator`](/docs/api/retrievers_self_query/classes/BasicTranslator)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[constructor](/docs/api/retrievers_self_query/classes/BaseTranslator#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/retrievers/self\_query/base.ts:36](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/self_query/base.ts#L36)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### VisitComparisonOutput[​](#visitcomparisonoutput "Direct link to VisitComparisonOutput")

> **VisitComparisonOutput**: [`VisitorComparisonResult`](/docs/api/chains_query_constructor_ir/types/VisitorComparisonResult)

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[VisitComparisonOutput](/docs/api/retrievers_self_query/classes/BaseTranslator#visitcomparisonoutput)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/base.ts:28](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/self_query/base.ts#L28)

### VisitOperationOutput[​](#visitoperationoutput "Direct link to VisitOperationOutput")

> **VisitOperationOutput**: [`VisitorOperationResult`](/docs/api/chains_query_constructor_ir/types/VisitorOperationResult)

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[VisitOperationOutput](/docs/api/retrievers_self_query/classes/BaseTranslator#visitoperationoutput)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/base.ts:26](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/self_query/base.ts#L26)

### VisitStructuredQueryOutput[​](#visitstructuredqueryoutput "Direct link to VisitStructuredQueryOutput")

> **VisitStructuredQueryOutput**: [`VisitorStructuredQueryResult`](/docs/api/chains_query_constructor_ir/types/VisitorStructuredQueryResult)

#### Overrides[​](#overrides-3 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[VisitStructuredQueryOutput](/docs/api/retrievers_self_query/classes/BaseTranslator#visitstructuredqueryoutput)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/base.ts:30](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/self_query/base.ts#L30)

### allowedComparators[​](#allowedcomparators "Direct link to allowedComparators")

> **allowedComparators**: [`Comparator`](/docs/api/chains_query_constructor_ir/types/Comparator)\[\]

#### Overrides[​](#overrides-4 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[allowedComparators](/docs/api/retrievers_self_query/classes/BaseTranslator#allowedcomparators)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/base.ts:34](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/self_query/base.ts#L34)

### allowedOperators[​](#allowedoperators "Direct link to allowedOperators")

> **allowedOperators**: [`Operator`](/docs/api/chains_query_constructor_ir/types/Operator)\[\]

#### Overrides[​](#overrides-5 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[allowedOperators](/docs/api/retrievers_self_query/classes/BaseTranslator#allowedoperators)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/base.ts:32](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/self_query/base.ts#L32)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### formatFunction()[​](#formatfunction "Direct link to formatFunction()")

> **formatFunction**(`func`: [`Operator`](/docs/api/chains_query_constructor_ir/types/Operator) | [`Comparator`](/docs/api/chains_query_constructor_ir/types/Comparator)): `string`

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`func`

[`Operator`](/docs/api/chains_query_constructor_ir/types/Operator) | [`Comparator`](/docs/api/chains_query_constructor_ir/types/Comparator)

#### Returns[​](#returns-1 "Direct link to Returns")

`string`

#### Overrides[​](#overrides-6 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[formatFunction](/docs/api/retrievers_self_query/classes/BaseTranslator#formatfunction)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/base.ts:52](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/self_query/base.ts#L52)

### visitComparison()[​](#visitcomparison "Direct link to visitComparison()")

> **visitComparison**(`comparison`: [`Comparison`](/docs/api/chains_query_constructor_ir/classes/Comparison)): [`VisitorComparisonResult`](/docs/api/chains_query_constructor_ir/types/VisitorComparisonResult)

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`comparison`

[`Comparison`](/docs/api/chains_query_constructor_ir/classes/Comparison)

#### Returns[​](#returns-2 "Direct link to Returns")

[`VisitorComparisonResult`](/docs/api/chains_query_constructor_ir/types/VisitorComparisonResult)

#### Overrides[​](#overrides-7 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[visitComparison](/docs/api/retrievers_self_query/classes/BaseTranslator#visitcomparison)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/base.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/self_query/base.ts#L90)

### visitOperation()[​](#visitoperation "Direct link to visitOperation()")

> **visitOperation**(`operation`: [`Operation`](/docs/api/chains_query_constructor_ir/classes/Operation)): [`VisitorOperationResult`](/docs/api/chains_query_constructor_ir/types/VisitorOperationResult)

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`operation`

[`Operation`](/docs/api/chains_query_constructor_ir/classes/Operation)

#### Returns[​](#returns-3 "Direct link to Returns")

[`VisitorOperationResult`](/docs/api/chains_query_constructor_ir/types/VisitorOperationResult)

#### Overrides[​](#overrides-8 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[visitOperation](/docs/api/retrievers_self_query/classes/BaseTranslator#visitoperation)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/base.ts:81](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/self_query/base.ts#L81)

### visitStructuredQuery()[​](#visitstructuredquery "Direct link to visitStructuredQuery()")

> **visitStructuredQuery**(`query`: [`StructuredQuery`](/docs/api/chains_query_constructor_ir/classes/StructuredQuery)): [`VisitorStructuredQueryResult`](/docs/api/chains_query_constructor_ir/types/VisitorStructuredQueryResult)

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`query`

[`StructuredQuery`](/docs/api/chains_query_constructor_ir/classes/StructuredQuery)

#### Returns[​](#returns-4 "Direct link to Returns")

[`VisitorStructuredQueryResult`](/docs/api/chains_query_constructor_ir/types/VisitorStructuredQueryResult)

#### Overrides[​](#overrides-9 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[visitStructuredQuery](/docs/api/retrievers_self_query/classes/BaseTranslator#visitstructuredquery)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/base.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/self_query/base.ts#L98)