SqlDatabaseChainInput
=====================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`ChainInputs`](/docs/api/chains/interfaces/ChainInputs).**SqlDatabaseChainInput**

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### database[​](#database "Direct link to database")

> **database**: [`SqlDatabase`](/docs/api/sql_db/classes/SqlDatabase)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/chains/sql\_db/sql\_db\_chain.ts:19](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/sql_db/sql_db_chain.ts#L19)

### llm[​](#llm "Direct link to llm")

> **llm**: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/chains/sql\_db/sql\_db\_chain.ts:18](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/sql_db/sql_db_chain.ts#L18)

### callbackManager?[​](#callbackmanager "Direct link to callbackManager?")

> **callbackManager**: [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Deprecated[​](#deprecated "Direct link to Deprecated")

Use `callbacks` instead

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[callbackManager](/docs/api/chains/interfaces/ChainInputs#callbackmanager)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/chains/base.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L22)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[callbacks](/docs/api/chains/interfaces/ChainInputs#callbacks)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L23)

### inputKey?[​](#inputkey "Direct link to inputKey?")

> **inputKey**: `string`

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/chains/sql\_db/sql\_db\_chain.ts:21](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/sql_db/sql_db_chain.ts#L21)

### memory?[​](#memory "Direct link to memory?")

> **memory**: [`BaseMemory`](/docs/api/memory/classes/BaseMemory)

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[memory](/docs/api/chains/interfaces/ChainInputs#memory)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/chains/base.ts:17](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L17)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[metadata](/docs/api/chains/interfaces/ChainInputs#metadata)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:25](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L25)

### outputKey?[​](#outputkey "Direct link to outputKey?")

> **outputKey**: `string`

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/chains/sql\_db/sql\_db\_chain.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/sql_db/sql_db_chain.ts#L22)

### prompt?[​](#prompt "Direct link to prompt?")

> **prompt**: [`PromptTemplate`](/docs/api/prompts/classes/PromptTemplate)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/chains/sql\_db/sql\_db\_chain.ts:24](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/sql_db/sql_db_chain.ts#L24)

### sqlOutputKey?[​](#sqloutputkey "Direct link to sqlOutputKey?")

> **sqlOutputKey**: `string`

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/chains/sql\_db/sql\_db\_chain.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/sql_db/sql_db_chain.ts#L23)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[tags](/docs/api/chains/interfaces/ChainInputs#tags)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:24](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L24)

### topK?[​](#topk "Direct link to topK?")

> **topK**: `number`

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/chains/sql\_db/sql\_db\_chain.ts:20](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/sql_db/sql_db_chain.ts#L20)

### verbose?[​](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[verbose](/docs/api/chains/interfaces/ChainInputs#verbose)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L22)