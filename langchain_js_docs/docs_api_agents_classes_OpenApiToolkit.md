OpenApiToolkit
==============

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`RequestsToolkit`](/docs/api/agents/classes/RequestsToolkit).**OpenApiToolkit**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new OpenApiToolkit**(`jsonSpec`: [`JsonSpec`](/docs/api/tools/classes/JsonSpec), `llm`: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel), `headers`?: `Headers`): [`OpenApiToolkit`](/docs/api/agents/classes/OpenApiToolkit)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`jsonSpec`

[`JsonSpec`](/docs/api/tools/classes/JsonSpec)

`llm`

[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)

`headers?`

`Headers`

#### Returns[​](#returns "Direct link to Returns")

[`OpenApiToolkit`](/docs/api/agents/classes/OpenApiToolkit)

#### Overrides[​](#overrides "Direct link to Overrides")

[RequestsToolkit](/docs/api/agents/classes/RequestsToolkit).[constructor](/docs/api/agents/classes/RequestsToolkit#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/agents/toolkits/openapi/openapi.ts:31](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/agents/toolkits/openapi/openapi.ts#L31)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### tools[​](#tools "Direct link to tools")

> **tools**: [`Tool`](/docs/api/tools/classes/Tool)\[\]

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[RequestsToolkit](/docs/api/agents/classes/RequestsToolkit).[tools](/docs/api/agents/classes/RequestsToolkit#tools)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/agents/toolkits/openapi/openapi.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/agents/toolkits/openapi/openapi.ts#L22)