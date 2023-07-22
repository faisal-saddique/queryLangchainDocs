QueryTransformer
================

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new QueryTransformer**(`allowedComparators`: [`Comparator`](/docs/api/chains_query_constructor_ir/types/Comparator)\[\] = `[]`, `allowedOperators`: [`Operator`](/docs/api/chains_query_constructor_ir/types/Operator)\[\] = `[]`): [`QueryTransformer`](/docs/api/chains_query_constructor/classes/QueryTransformer)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

Default value

`allowedComparators`

[`Comparator`](/docs/api/chains_query_constructor_ir/types/Comparator)\[\]

`[]`

`allowedOperators`

[`Operator`](/docs/api/chains_query_constructor_ir/types/Operator)\[\]

`[]`

#### Returns[​](#returns "Direct link to Returns")

[`QueryTransformer`](/docs/api/chains_query_constructor/classes/QueryTransformer)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/chains/query\_constructor/parser.ts:26](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/query_constructor/parser.ts#L26)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### allowedComparators[​](#allowedcomparators "Direct link to allowedComparators")

> **allowedComparators**: [`Comparator`](/docs/api/chains_query_constructor_ir/types/Comparator)\[\] = `[]`

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/chains/query\_constructor/parser.ts:27](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/query_constructor/parser.ts#L27)

### allowedOperators[​](#allowedoperators "Direct link to allowedOperators")

> **allowedOperators**: [`Operator`](/docs/api/chains_query_constructor_ir/types/Operator)\[\] = `[]`

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/chains/query\_constructor/parser.ts:28](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/query_constructor/parser.ts#L28)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### parse()[​](#parse "Direct link to parse()")

> **parse**(`expression`: `string`): `Promise`<[`Operation`](/docs/api/chains_query_constructor_ir/classes/Operation) | [`Comparison`](/docs/api/chains_query_constructor_ir/classes/Comparison)\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`expression`

`string`

#### Returns[​](#returns-1 "Direct link to Returns")

`Promise`<[`Operation`](/docs/api/chains_query_constructor_ir/classes/Operation) | [`Comparison`](/docs/api/chains_query_constructor_ir/classes/Comparison)\>

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/chains/query\_constructor/parser.ts:111](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/query_constructor/parser.ts#L111)