SqlToolkit
==========

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`Toolkit`](/docs/api/agents/classes/Toolkit).**SqlToolkit**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new SqlToolkit**(`db`: [`SqlDatabase`](/docs/api/sql_db/classes/SqlDatabase), `llm`?: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>): [`SqlToolkit`](/docs/api/agents_toolkits_sql/classes/SqlToolkit)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`db`

[`SqlDatabase`](/docs/api/sql_db/classes/SqlDatabase)

`llm?`

[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>

#### Returns[](#returns "Direct link to Returns")

[`SqlToolkit`](/docs/api/agents_toolkits_sql/classes/SqlToolkit)

#### Overrides[](#overrides "Direct link to Overrides")

[Toolkit](/docs/api/agents/classes/Toolkit).[constructor](/docs/api/agents/classes/Toolkit#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/agents/toolkits/sql/sql.ts:29](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/toolkits/sql/sql.ts#L29)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### db[](#db "Direct link to db")

> **db**: [`SqlDatabase`](/docs/api/sql_db/classes/SqlDatabase)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/agents/toolkits/sql/sql.ts:25](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/toolkits/sql/sql.ts#L25)

### dialect[](#dialect "Direct link to dialect")

> **dialect**: `string` = `"sqlite"`

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/agents/toolkits/sql/sql.ts:27](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/toolkits/sql/sql.ts#L27)

### tools[](#tools "Direct link to tools")

> **tools**: [`Tool`](/docs/api/tools/classes/Tool)\[\]

#### Overrides[](#overrides-1 "Direct link to Overrides")

[Toolkit](/docs/api/agents/classes/Toolkit).[tools](/docs/api/agents/classes/Toolkit#tools)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/agents/toolkits/sql/sql.ts:23](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/toolkits/sql/sql.ts#L23)