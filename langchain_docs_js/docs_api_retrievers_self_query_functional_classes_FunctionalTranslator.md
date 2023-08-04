FunctionalTranslator
====================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseTranslator`](/docs/api/retrievers_self_query/classes/BaseTranslator).**FunctionalTranslator**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new FunctionalTranslator**(): [`FunctionalTranslator`](/docs/api/retrievers_self_query_functional/classes/FunctionalTranslator)

#### Returns[](#returns "Direct link to Returns")

[`FunctionalTranslator`](/docs/api/retrievers_self_query_functional/classes/FunctionalTranslator)

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[constructor](/docs/api/retrievers_self_query/classes/BaseTranslator#constructor)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### VisitComparisonOutput[](#visitcomparisonoutput "Direct link to VisitComparisonOutput")

> **VisitComparisonOutput**: [`FunctionFilter`](/docs/api/retrievers_self_query_functional/types/FunctionFilter)

#### Overrides[](#overrides "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[VisitComparisonOutput](/docs/api/retrievers_self_query/classes/BaseTranslator#visitcomparisonoutput)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/retrievers/self\_query/functional.ts:27](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/functional.ts#L27)

### VisitOperationOutput[](#visitoperationoutput "Direct link to VisitOperationOutput")

> **VisitOperationOutput**: [`FunctionFilter`](/docs/api/retrievers_self_query_functional/types/FunctionFilter)

#### Overrides[](#overrides-1 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[VisitOperationOutput](/docs/api/retrievers_self_query/classes/BaseTranslator#visitoperationoutput)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/functional.ts:25](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/functional.ts#L25)

### VisitStructuredQueryOutput[](#visitstructuredqueryoutput "Direct link to VisitStructuredQueryOutput")

> **VisitStructuredQueryOutput**: `object`

#### Type declaration[](#type-declaration "Direct link to Type declaration")

Member

Type

`filter`

[`FunctionFilter`](/docs/api/retrievers_self_query_functional/types/FunctionFilter)

#### Overrides[](#overrides-2 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[VisitStructuredQueryOutput](/docs/api/retrievers_self_query/classes/BaseTranslator#visitstructuredqueryoutput)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/functional.ts:29](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/functional.ts#L29)

### allowedComparators[](#allowedcomparators "Direct link to allowedComparators")

> **allowedComparators**: [`Comparator`](/docs/api/chains_query_constructor_ir/types/Comparator)\[\]

#### Overrides[](#overrides-3 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[allowedComparators](/docs/api/retrievers_self_query/classes/BaseTranslator#allowedcomparators)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/functional.ts:33](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/functional.ts#L33)

### allowedOperators[](#allowedoperators "Direct link to allowedOperators")

> **allowedOperators**: [`Operator`](/docs/api/chains_query_constructor_ir/types/Operator)\[\]

#### Overrides[](#overrides-4 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[allowedOperators](/docs/api/retrievers_self_query/classes/BaseTranslator#allowedoperators)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/functional.ts:31](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/functional.ts#L31)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### formatFunction()[](#formatfunction "Direct link to formatFunction()")

> **formatFunction**(): `string`

#### Returns[](#returns-1 "Direct link to Returns")

`string`

#### Overrides[](#overrides-5 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[formatFunction](/docs/api/retrievers_self_query/classes/BaseTranslator#formatfunction)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/functional.ts:42](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/functional.ts#L42)

### getComparatorFunction()[](#getcomparatorfunction "Direct link to getComparatorFunction()")

> **getComparatorFunction**<C\>(`comparator`: [`Comparator`](/docs/api/chains_query_constructor_ir/types/Comparator)): `Function`

#### Type parameters[](#type-parameters "Direct link to Type parameters")

*   `C` _extends_ [`Comparator`](/docs/api/chains_query_constructor_ir/types/Comparator)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`comparator`

[`Comparator`](/docs/api/chains_query_constructor_ir/types/Comparator)

#### Returns[](#returns-2 "Direct link to Returns")

`Function`

> (`a`: `string` | `number`, `b`: `ValueType`\[`C`\]): `boolean`

##### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`a`

`string` | `number`

`b`

`ValueType`\[`C`\]

##### Returns[](#returns-3 "Direct link to Returns")

`boolean`

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/functional.ts:46](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/functional.ts#L46)

### getOperatorFunction()[](#getoperatorfunction "Direct link to getOperatorFunction()")

> **getOperatorFunction**(`operator`: [`Operator`](/docs/api/chains_query_constructor_ir/types/Operator)): `Function`

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`operator`

[`Operator`](/docs/api/chains_query_constructor_ir/types/Operator)

#### Returns[](#returns-4 "Direct link to Returns")

`Function`

> (`a`: `boolean`, `b`: `boolean`): `boolean`

##### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

`a`

`boolean`

`b`

`boolean`

##### Returns[](#returns-5 "Direct link to Returns")

`boolean`

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/functional.ts:74](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/functional.ts#L74)

### visitComparison()[](#visitcomparison "Direct link to visitComparison()")

> **visitComparison**(`comparison`: [`Comparison`](/docs/api/chains_query_constructor_ir/classes/Comparison)): [`FunctionFilter`](/docs/api/retrievers_self_query_functional/types/FunctionFilter)

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

`comparison`

[`Comparison`](/docs/api/chains_query_constructor_ir/classes/Comparison)

#### Returns[](#returns-6 "Direct link to Returns")

[`FunctionFilter`](/docs/api/retrievers_self_query_functional/types/FunctionFilter)

#### Overrides[](#overrides-6 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[visitComparison](/docs/api/retrievers_self_query/classes/BaseTranslator#visitcomparison)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/functional.ts:111](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/functional.ts#L111)

### visitOperation()[](#visitoperation "Direct link to visitOperation()")

> **visitOperation**(`operation`: [`Operation`](/docs/api/chains_query_constructor_ir/classes/Operation)): [`FunctionFilter`](/docs/api/retrievers_self_query_functional/types/FunctionFilter)

#### Parameters[](#parameters-5 "Direct link to Parameters")

Parameter

Type

`operation`

[`Operation`](/docs/api/chains_query_constructor_ir/classes/Operation)

#### Returns[](#returns-7 "Direct link to Returns")

[`FunctionFilter`](/docs/api/retrievers_self_query_functional/types/FunctionFilter)

#### Overrides[](#overrides-7 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[visitOperation](/docs/api/retrievers_self_query/classes/BaseTranslator#visitoperation)

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/functional.ts:88](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/functional.ts#L88)

### visitStructuredQuery()[](#visitstructuredquery "Direct link to visitStructuredQuery()")

> **visitStructuredQuery**(`query`: [`StructuredQuery`](/docs/api/chains_query_constructor_ir/classes/StructuredQuery)): `object`

#### Parameters[](#parameters-6 "Direct link to Parameters")

Parameter

Type

`query`

[`StructuredQuery`](/docs/api/chains_query_constructor_ir/classes/StructuredQuery)

#### Returns[](#returns-8 "Direct link to Returns")

`object`

Member

Type

`filter`

[`FunctionFilter`](/docs/api/retrievers_self_query_functional/types/FunctionFilter)

#### Overrides[](#overrides-8 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[visitStructuredQuery](/docs/api/retrievers_self_query/classes/BaseTranslator#visitstructuredquery)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/functional.ts:131](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/functional.ts#L131)