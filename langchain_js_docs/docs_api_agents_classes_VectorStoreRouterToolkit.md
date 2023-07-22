VectorStoreRouterToolkit
========================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`Toolkit`](/docs/api/agents/classes/Toolkit).**VectorStoreRouterToolkit**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new VectorStoreRouterToolkit**(`vectorStoreInfos`: [`VectorStoreInfo`](/docs/api/agents/interfaces/VectorStoreInfo)\[\], `llm`: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)): [`VectorStoreRouterToolkit`](/docs/api/agents/classes/VectorStoreRouterToolkit)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`vectorStoreInfos`

[`VectorStoreInfo`](/docs/api/agents/interfaces/VectorStoreInfo)\[\]

`llm`

[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)

#### Returns[​](#returns "Direct link to Returns")

[`VectorStoreRouterToolkit`](/docs/api/agents/classes/VectorStoreRouterToolkit)

#### Overrides[​](#overrides "Direct link to Overrides")

[Toolkit](/docs/api/agents/classes/Toolkit).[constructor](/docs/api/agents/classes/Toolkit#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/agents/toolkits/vectorstore/vectorstore.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/agents/toolkits/vectorstore/vectorstore.ts#L46)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### llm[​](#llm "Direct link to llm")

> **llm**: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/agents/toolkits/vectorstore/vectorstore.ts:44](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/agents/toolkits/vectorstore/vectorstore.ts#L44)

### tools[​](#tools "Direct link to tools")

> **tools**: [`Tool`](/docs/api/tools/classes/Tool)\[\]

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[Toolkit](/docs/api/agents/classes/Toolkit).[tools](/docs/api/agents/classes/Toolkit#tools)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/agents/toolkits/vectorstore/vectorstore.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/agents/toolkits/vectorstore/vectorstore.ts#L40)

### vectorStoreInfos[​](#vectorstoreinfos "Direct link to vectorStoreInfos")

> **vectorStoreInfos**: [`VectorStoreInfo`](/docs/api/agents/interfaces/VectorStoreInfo)\[\]

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/agents/toolkits/vectorstore/vectorstore.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/agents/toolkits/vectorstore/vectorstore.ts#L42)