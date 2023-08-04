SupabaseTranslator
==================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseTranslator`](/docs/api/retrievers_self_query/classes/BaseTranslator).**SupabaseTranslator**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new SupabaseTranslator**(): [`SupabaseTranslator`](/docs/api/retrievers_self_query_supabase/classes/SupabaseTranslator)

#### Returns[](#returns "Direct link to Returns")

[`SupabaseTranslator`](/docs/api/retrievers_self_query_supabase/classes/SupabaseTranslator)

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[constructor](/docs/api/retrievers_self_query/classes/BaseTranslator#constructor)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### VisitComparisonOutput[](#visitcomparisonoutput "Direct link to VisitComparisonOutput")

> **VisitComparisonOutput**: [`SupabaseFilterRPCCall`](/docs/api/vectorstores_supabase/types/SupabaseFilterRPCCall)

#### Overrides[](#overrides "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[VisitComparisonOutput](/docs/api/retrievers_self_query/classes/BaseTranslator#visitcomparisonoutput)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/retrievers/self\_query/supabase.ts:25](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/supabase.ts#L25)

### VisitOperationOutput[](#visitoperationoutput "Direct link to VisitOperationOutput")

> **VisitOperationOutput**: [`SupabaseFilterRPCCall`](/docs/api/vectorstores_supabase/types/SupabaseFilterRPCCall)

#### Overrides[](#overrides-1 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[VisitOperationOutput](/docs/api/retrievers_self_query/classes/BaseTranslator#visitoperationoutput)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/supabase.ts:23](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/supabase.ts#L23)

### VisitStructuredQueryOutput[](#visitstructuredqueryoutput "Direct link to VisitStructuredQueryOutput")

> **VisitStructuredQueryOutput**: `object`

#### Type declaration[](#type-declaration "Direct link to Type declaration")

Member

Type

`filter`

[`SupabaseFilterRPCCall`](/docs/api/vectorstores_supabase/types/SupabaseFilterRPCCall)

#### Overrides[](#overrides-2 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[VisitStructuredQueryOutput](/docs/api/retrievers_self_query/classes/BaseTranslator#visitstructuredqueryoutput)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/supabase.ts:27](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/supabase.ts#L27)

### allowedComparators[](#allowedcomparators "Direct link to allowedComparators")

> **allowedComparators**: [`Comparator`](/docs/api/chains_query_constructor_ir/types/Comparator)\[\]

#### Overrides[](#overrides-3 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[allowedComparators](/docs/api/retrievers_self_query/classes/BaseTranslator#allowedcomparators)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/supabase.ts:31](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/supabase.ts#L31)

### allowedOperators[](#allowedoperators "Direct link to allowedOperators")

> **allowedOperators**: [`Operator`](/docs/api/chains_query_constructor_ir/types/Operator)\[\]

#### Overrides[](#overrides-4 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[allowedOperators](/docs/api/retrievers_self_query/classes/BaseTranslator#allowedoperators)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/supabase.ts:29](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/supabase.ts#L29)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### buildColumnName()[](#buildcolumnname "Direct link to buildColumnName()")

> **buildColumnName**(`attr`: `string`, `value`: `string` | `number`, `includeType`: `boolean` = `true`): `string`

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

Default value

`attr`

`string`

`undefined`

`value`

`string` | `number`

`undefined`

`includeType`

`boolean`

`true`

#### Returns[](#returns-1 "Direct link to Returns")

`string`

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/supabase.ts:78](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/supabase.ts#L78)

### formatFunction()[](#formatfunction "Direct link to formatFunction()")

> **formatFunction**(): `string`

#### Returns[](#returns-2 "Direct link to Returns")

`string`

#### Overrides[](#overrides-5 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[formatFunction](/docs/api/retrievers_self_query/classes/BaseTranslator#formatfunction)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/supabase.ts:40](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/supabase.ts#L40)

### getComparatorFunction()[](#getcomparatorfunction "Direct link to getComparatorFunction()")

> **getComparatorFunction**<C\>(`comparator`: [`Comparator`](/docs/api/chains_query_constructor_ir/types/Comparator)): `Function`

#### Type parameters[](#type-parameters "Direct link to Type parameters")

*   `C` _extends_ [`Comparator`](/docs/api/chains_query_constructor_ir/types/Comparator)

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`comparator`

[`Comparator`](/docs/api/chains_query_constructor_ir/types/Comparator)

#### Returns[](#returns-3 "Direct link to Returns")

`Function`

> (`attr`: `string`, `value`: `ValueType`\[`C`\]): [`SupabaseFilterRPCCall`](/docs/api/vectorstores_supabase/types/SupabaseFilterRPCCall)

##### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`attr`

`string`

`value`

`ValueType`\[`C`\]

##### Returns[](#returns-4 "Direct link to Returns")

[`SupabaseFilterRPCCall`](/docs/api/vectorstores_supabase/types/SupabaseFilterRPCCall)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/supabase.ts:44](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/supabase.ts#L44)

### visitComparison()[](#visitcomparison "Direct link to visitComparison()")

> **visitComparison**(`comparison`: [`Comparison`](/docs/api/chains_query_constructor_ir/classes/Comparison)): [`SupabaseFilterRPCCall`](/docs/api/vectorstores_supabase/types/SupabaseFilterRPCCall)

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

`comparison`

[`Comparison`](/docs/api/chains_query_constructor_ir/classes/Comparison)

#### Returns[](#returns-5 "Direct link to Returns")

[`SupabaseFilterRPCCall`](/docs/api/vectorstores_supabase/types/SupabaseFilterRPCCall)

#### Overrides[](#overrides-6 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[visitComparison](/docs/api/retrievers_self_query/classes/BaseTranslator#visitcomparison)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/supabase.ts:156](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/supabase.ts#L156)

### visitComparisonAsString()[](#visitcomparisonasstring "Direct link to visitComparisonAsString()")

> **visitComparisonAsString**(`comparison`: [`Comparison`](/docs/api/chains_query_constructor_ir/classes/Comparison)): `string`

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

`comparison`

[`Comparison`](/docs/api/chains_query_constructor_ir/classes/Comparison)

#### Returns[](#returns-6 "Direct link to Returns")

`string`

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/supabase.ts:134](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/supabase.ts#L134)

### visitOperation()[](#visitoperation "Direct link to visitOperation()")

> **visitOperation**(`operation`: [`Operation`](/docs/api/chains_query_constructor_ir/classes/Operation)): [`SupabaseFilterRPCCall`](/docs/api/vectorstores_supabase/types/SupabaseFilterRPCCall)

#### Parameters[](#parameters-5 "Direct link to Parameters")

Parameter

Type

`operation`

[`Operation`](/docs/api/chains_query_constructor_ir/classes/Operation)

#### Returns[](#returns-7 "Direct link to Returns")

[`SupabaseFilterRPCCall`](/docs/api/vectorstores_supabase/types/SupabaseFilterRPCCall)

#### Overrides[](#overrides-7 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[visitOperation](/docs/api/retrievers_self_query/classes/BaseTranslator#visitoperation)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/supabase.ts:111](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/supabase.ts#L111)

### visitOperationAsString()[](#visitoperationasstring "Direct link to visitOperationAsString()")

> **visitOperationAsString**(`operation`: [`Operation`](/docs/api/chains_query_constructor_ir/classes/Operation)): `string`

#### Parameters[](#parameters-6 "Direct link to Parameters")

Parameter

Type

`operation`

[`Operation`](/docs/api/chains_query_constructor_ir/classes/Operation)

#### Returns[](#returns-8 "Direct link to Returns")

`string`

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/supabase.ts:91](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/supabase.ts#L91)

### visitStructuredQuery()[](#visitstructuredquery "Direct link to visitStructuredQuery()")

> **visitStructuredQuery**(`query`: [`StructuredQuery`](/docs/api/chains_query_constructor_ir/classes/StructuredQuery)): `object`

#### Parameters[](#parameters-7 "Direct link to Parameters")

Parameter

Type

`query`

[`StructuredQuery`](/docs/api/chains_query_constructor_ir/classes/StructuredQuery)

#### Returns[](#returns-9 "Direct link to Returns")

`object`

Member

Type

`filter`

[`SupabaseFilterRPCCall`](/docs/api/vectorstores_supabase/types/SupabaseFilterRPCCall)

#### Overrides[](#overrides-8 "Direct link to Overrides")

[BaseTranslator](/docs/api/retrievers_self_query/classes/BaseTranslator).[visitStructuredQuery](/docs/api/retrievers_self_query/classes/BaseTranslator#visitstructuredquery)

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/supabase.ts:168](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/retrievers/self_query/supabase.ts#L168)