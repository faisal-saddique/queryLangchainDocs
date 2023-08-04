ChromaTranslator
================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BasicTranslator`](/docs/api/retrievers_self_query/classes/BasicTranslator).**ChromaTranslator**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new ChromaTranslator**(): [`ChromaTranslator`](/docs/api/retrievers_self_query_chroma/classes/ChromaTranslator)

#### Returns[](#returns "Direct link to Returns")

[`ChromaTranslator`](/docs/api/retrievers_self_query_chroma/classes/ChromaTranslator)

#### Overrides[](#overrides "Direct link to Overrides")

[BasicTranslator](/docs/api/retrievers_self_query/classes/BasicTranslator).[constructor](/docs/api/retrievers_self_query/classes/BasicTranslator#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/retrievers/self\_query/chroma.ts:5](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/chroma.ts#L5)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### VisitComparisonOutput[](#visitcomparisonoutput "Direct link to VisitComparisonOutput")

> **VisitComparisonOutput**: [`VisitorComparisonResult`](/docs/api/chains_query_constructor_ir/types/VisitorComparisonResult)

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BasicTranslator](/docs/api/retrievers_self_query/classes/BasicTranslator).[VisitComparisonOutput](/docs/api/retrievers_self_query/classes/BasicTranslator#visitcomparisonoutput)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/base.ts:28](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/base.ts#L28)

### VisitOperationOutput[](#visitoperationoutput "Direct link to VisitOperationOutput")

> **VisitOperationOutput**: [`VisitorOperationResult`](/docs/api/chains_query_constructor_ir/types/VisitorOperationResult)

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[BasicTranslator](/docs/api/retrievers_self_query/classes/BasicTranslator).[VisitOperationOutput](/docs/api/retrievers_self_query/classes/BasicTranslator#visitoperationoutput)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/base.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/base.ts#L26)

### VisitStructuredQueryOutput[](#visitstructuredqueryoutput "Direct link to VisitStructuredQueryOutput")

> **VisitStructuredQueryOutput**: [`VisitorStructuredQueryResult`](/docs/api/chains_query_constructor_ir/types/VisitorStructuredQueryResult)

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[BasicTranslator](/docs/api/retrievers_self_query/classes/BasicTranslator).[VisitStructuredQueryOutput](/docs/api/retrievers_self_query/classes/BasicTranslator#visitstructuredqueryoutput)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/base.ts:30](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/base.ts#L30)

### allowedComparators[](#allowedcomparators "Direct link to allowedComparators")

> **allowedComparators**: [`Comparator`](/docs/api/chains_query_constructor_ir/types/Comparator)\[\]

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[BasicTranslator](/docs/api/retrievers_self_query/classes/BasicTranslator).[allowedComparators](/docs/api/retrievers_self_query/classes/BasicTranslator#allowedcomparators)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/base.ts:34](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/base.ts#L34)

### allowedOperators[](#allowedoperators "Direct link to allowedOperators")

> **allowedOperators**: [`Operator`](/docs/api/chains_query_constructor_ir/types/Operator)\[\]

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[BasicTranslator](/docs/api/retrievers_self_query/classes/BasicTranslator).[allowedOperators](/docs/api/retrievers_self_query/classes/BasicTranslator#allowedoperators)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/base.ts:32](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/base.ts#L32)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### formatFunction()[](#formatfunction "Direct link to formatFunction()")

> **formatFunction**(`func`: [`Operator`](/docs/api/chains_query_constructor_ir/types/Operator) | [`Comparator`](/docs/api/chains_query_constructor_ir/types/Comparator)): `string`

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`func`

[`Operator`](/docs/api/chains_query_constructor_ir/types/Operator) | [`Comparator`](/docs/api/chains_query_constructor_ir/types/Comparator)

#### Returns[](#returns-1 "Direct link to Returns")

`string`

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[BasicTranslator](/docs/api/retrievers_self_query/classes/BasicTranslator).[formatFunction](/docs/api/retrievers_self_query/classes/BasicTranslator#formatfunction)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/base.ts:52](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/base.ts#L52)

### visitComparison()[](#visitcomparison "Direct link to visitComparison()")

> **visitComparison**(`comparison`: [`Comparison`](/docs/api/chains_query_constructor_ir/classes/Comparison)): [`VisitorComparisonResult`](/docs/api/chains_query_constructor_ir/types/VisitorComparisonResult)

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`comparison`

[`Comparison`](/docs/api/chains_query_constructor_ir/classes/Comparison)

#### Returns[](#returns-2 "Direct link to Returns")

[`VisitorComparisonResult`](/docs/api/chains_query_constructor_ir/types/VisitorComparisonResult)

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[BasicTranslator](/docs/api/retrievers_self_query/classes/BasicTranslator).[visitComparison](/docs/api/retrievers_self_query/classes/BasicTranslator#visitcomparison)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/base.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/base.ts#L90)

### visitOperation()[](#visitoperation "Direct link to visitOperation()")

> **visitOperation**(`operation`: [`Operation`](/docs/api/chains_query_constructor_ir/classes/Operation)): [`VisitorOperationResult`](/docs/api/chains_query_constructor_ir/types/VisitorOperationResult)

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`operation`

[`Operation`](/docs/api/chains_query_constructor_ir/classes/Operation)

#### Returns[](#returns-3 "Direct link to Returns")

[`VisitorOperationResult`](/docs/api/chains_query_constructor_ir/types/VisitorOperationResult)

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

[BasicTranslator](/docs/api/retrievers_self_query/classes/BasicTranslator).[visitOperation](/docs/api/retrievers_self_query/classes/BasicTranslator#visitoperation)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/base.ts:81](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/base.ts#L81)

### visitStructuredQuery()[](#visitstructuredquery "Direct link to visitStructuredQuery()")

> **visitStructuredQuery**(`query`: [`StructuredQuery`](/docs/api/chains_query_constructor_ir/classes/StructuredQuery)): [`VisitorStructuredQueryResult`](/docs/api/chains_query_constructor_ir/types/VisitorStructuredQueryResult)

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

`query`

[`StructuredQuery`](/docs/api/chains_query_constructor_ir/classes/StructuredQuery)

#### Returns[](#returns-4 "Direct link to Returns")

[`VisitorStructuredQueryResult`](/docs/api/chains_query_constructor_ir/types/VisitorStructuredQueryResult)

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

[BasicTranslator](/docs/api/retrievers_self_query/classes/BasicTranslator).[visitStructuredQuery](/docs/api/retrievers_self_query/classes/BasicTranslator#visitstructuredquery)

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/base.ts:98](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/base.ts#L98)