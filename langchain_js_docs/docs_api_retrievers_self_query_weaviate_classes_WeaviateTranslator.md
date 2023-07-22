WeaviateTranslator
==================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseTranslator`](/docs/api/retrievers_self_query/classes/BaseTranslator).**WeaviateTranslator**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new WeaviateTranslator**(): [`WeaviateTranslator`](/docs/api/retrievers_self_query_weaviate/classes/WeaviateTranslator)

#### Returns[​](#returns "Direct link to Returns")

[`WeaviateTranslator`](/docs/api/retrievers_self_query_weaviate/classes/WeaviateTranslator)

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[constructor](/docs/api/retrievers_self_query/classes/BaseTranslator#constructor)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### VisitComparisonOutput[​](#visitcomparisonoutput "Direct link to VisitComparisonOutput")

> **VisitComparisonOutput**: [`WeaviateComparisonResult`](/docs/api/retrievers_self_query_weaviate/types/WeaviateComparisonResult)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[VisitComparisonOutput](/docs/api/retrievers_self_query/classes/BaseTranslator#visitcomparisonoutput)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/retrievers/self\_query/weaviate.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/self_query/weaviate.ts#L55)

### VisitOperationOutput[​](#visitoperationoutput "Direct link to VisitOperationOutput")

> **VisitOperationOutput**: [`WeaviateOperationResult`](/docs/api/retrievers_self_query_weaviate/types/WeaviateOperationResult)

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[VisitOperationOutput](/docs/api/retrievers_self_query/classes/BaseTranslator#visitoperationoutput)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/weaviate.ts:53](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/self_query/weaviate.ts#L53)

### VisitStructuredQueryOutput[​](#visitstructuredqueryoutput "Direct link to VisitStructuredQueryOutput")

> **VisitStructuredQueryOutput**: [`WeaviateStructuredQueryResult`](/docs/api/retrievers_self_query_weaviate/types/WeaviateStructuredQueryResult)

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[VisitStructuredQueryOutput](/docs/api/retrievers_self_query/classes/BaseTranslator#visitstructuredqueryoutput)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/weaviate.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/self_query/weaviate.ts#L57)

### allowedComparators[​](#allowedcomparators "Direct link to allowedComparators")

> **allowedComparators**: [`Comparator`](/docs/api/chains_query_constructor_ir/types/Comparator)\[\]

#### Overrides[​](#overrides-3 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[allowedComparators](/docs/api/retrievers_self_query/classes/BaseTranslator#allowedcomparators)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/weaviate.ts:61](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/self_query/weaviate.ts#L61)

### allowedOperators[​](#allowedoperators "Direct link to allowedOperators")

> **allowedOperators**: [`Operator`](/docs/api/chains_query_constructor_ir/types/Operator)\[\]

#### Overrides[​](#overrides-4 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[allowedOperators](/docs/api/retrievers_self_query/classes/BaseTranslator#allowedoperators)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/weaviate.ts:59](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/self_query/weaviate.ts#L59)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### formatFunction()[​](#formatfunction "Direct link to formatFunction()")

> **formatFunction**(`func`: [`Operator`](/docs/api/chains_query_constructor_ir/types/Operator) | [`Comparator`](/docs/api/chains_query_constructor_ir/types/Comparator)): `string`

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`func`

[`Operator`](/docs/api/chains_query_constructor_ir/types/Operator) | [`Comparator`](/docs/api/chains_query_constructor_ir/types/Comparator)

#### Returns[​](#returns-1 "Direct link to Returns")

`string`

#### Overrides[​](#overrides-5 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[formatFunction](/docs/api/retrievers_self_query/classes/BaseTranslator#formatfunction)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/weaviate.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/self_query/weaviate.ts#L70)

### visitComparison()[​](#visitcomparison "Direct link to visitComparison()")

> **visitComparison**(`comparison`: [`Comparison`](/docs/api/chains_query_constructor_ir/classes/Comparison)): [`WeaviateComparisonResult`](/docs/api/retrievers_self_query_weaviate/types/WeaviateComparisonResult)

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`comparison`

[`Comparison`](/docs/api/chains_query_constructor_ir/classes/Comparison)

#### Returns[​](#returns-2 "Direct link to Returns")

[`WeaviateComparisonResult`](/docs/api/retrievers_self_query_weaviate/types/WeaviateComparisonResult)

#### Overrides[​](#overrides-6 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[visitComparison](/docs/api/retrievers_self_query/classes/BaseTranslator#visitcomparison)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/weaviate.ts:119](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/self_query/weaviate.ts#L119)

### visitOperation()[​](#visitoperation "Direct link to visitOperation()")

> **visitOperation**(`operation`: [`Operation`](/docs/api/chains_query_constructor_ir/classes/Operation)): [`WeaviateOperationResult`](/docs/api/retrievers_self_query_weaviate/types/WeaviateOperationResult)

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`operation`

[`Operation`](/docs/api/chains_query_constructor_ir/classes/Operation)

#### Returns[​](#returns-3 "Direct link to Returns")

[`WeaviateOperationResult`](/docs/api/retrievers_self_query_weaviate/types/WeaviateOperationResult)

#### Overrides[​](#overrides-7 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[visitOperation](/docs/api/retrievers_self_query/classes/BaseTranslator#visitoperation)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/weaviate.ts:109](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/self_query/weaviate.ts#L109)

### visitStructuredQuery()[​](#visitstructuredquery "Direct link to visitStructuredQuery()")

> **visitStructuredQuery**(`query`: [`StructuredQuery`](/docs/api/chains_query_constructor_ir/classes/StructuredQuery)): [`WeaviateStructuredQueryResult`](/docs/api/retrievers_self_query_weaviate/types/WeaviateStructuredQueryResult)

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`query`

[`StructuredQuery`](/docs/api/chains_query_constructor_ir/classes/StructuredQuery)

#### Returns[​](#returns-4 "Direct link to Returns")

[`WeaviateStructuredQueryResult`](/docs/api/retrievers_self_query_weaviate/types/WeaviateStructuredQueryResult)

#### Overrides[​](#overrides-8 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[visitStructuredQuery](/docs/api/retrievers_self_query/classes/BaseTranslator#visitstructuredquery)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/weaviate.ts:145](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/self_query/weaviate.ts#L145)