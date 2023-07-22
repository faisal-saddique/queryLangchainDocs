MasterHandler
=============

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   `NodeHandler`.**MasterHandler**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new MasterHandler**(`parentHandler`?: `NodeHandler`): [`MasterHandler`](/docs/api/output_parsers_expression/classes/MasterHandler)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`parentHandler?`

`NodeHandler`

#### Returns[​](#returns "Direct link to Returns")

[`MasterHandler`](/docs/api/output_parsers_expression/classes/MasterHandler)

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

NodeHandler.constructor

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/output\_parsers/expression\_type\_handlers/base.ts:4](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/output_parsers/expression_type_handlers/base.ts#L4)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### nodeHandlers[​](#nodehandlers "Direct link to nodeHandlers")

> **nodeHandlers**: `NodeHandler`\[\] = `[]`

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/output\_parsers/expression\_type\_handlers/factory.ts:26](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/output_parsers/expression_type_handlers/factory.ts#L26)

### parentHandler?[​](#parenthandler "Direct link to parentHandler?")

> **parentHandler**: `NodeHandler`

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

NodeHandler.parentHandler

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/output\_parsers/expression\_type\_handlers/base.ts:4](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/output_parsers/expression_type_handlers/base.ts#L4)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### accepts()[​](#accepts "Direct link to accepts()")

> **accepts**(`node`: `ExpressionNode`): `Promise`<`boolean` | `ExpressionNode`\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`node`

`ExpressionNode`

#### Returns[​](#returns-1 "Direct link to Returns")

`Promise`<`boolean` | `ExpressionNode`\>

#### Overrides[​](#overrides "Direct link to Overrides")

NodeHandler.accepts

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/output\_parsers/expression\_type\_handlers/factory.ts:28](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/output_parsers/expression_type_handlers/factory.ts#L28)

### handle()[​](#handle "Direct link to handle()")

> **handle**(`node`: `CallExpression`): `Promise`<[`ParsedType`](/docs/api/output_parsers_expression/types/ParsedType)\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`node`

`CallExpression`

#### Returns[​](#returns-2 "Direct link to Returns")

`Promise`<[`ParsedType`](/docs/api/output_parsers_expression/types/ParsedType)\>

#### Overrides[​](#overrides-1 "Direct link to Overrides")

NodeHandler.handle

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/output\_parsers/expression\_type\_handlers/factory.ts:32](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/output_parsers/expression_type_handlers/factory.ts#L32)

### createMasterHandler()[​](#createmasterhandler "Direct link to createMasterHandler()")

> `Static` **createMasterHandler**(): [`MasterHandler`](/docs/api/output_parsers_expression/classes/MasterHandler)

#### Returns[​](#returns-3 "Direct link to Returns")

[`MasterHandler`](/docs/api/output_parsers_expression/classes/MasterHandler)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/output\_parsers/expression\_type\_handlers/factory.ts:43](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/output_parsers/expression_type_handlers/factory.ts#L43)