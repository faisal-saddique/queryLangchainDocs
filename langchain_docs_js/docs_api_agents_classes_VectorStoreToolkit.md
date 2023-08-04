VectorStoreToolkit
==================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`Toolkit`](/docs/api/agents/classes/Toolkit).**VectorStoreToolkit**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new VectorStoreToolkit**(`vectorStoreInfo`: [`VectorStoreInfo`](/docs/api/agents/interfaces/VectorStoreInfo), `llm`: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>): [`VectorStoreToolkit`](/docs/api/agents/classes/VectorStoreToolkit)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`vectorStoreInfo`

[`VectorStoreInfo`](/docs/api/agents/interfaces/VectorStoreInfo)

`llm`

[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>

#### Returns[](#returns "Direct link to Returns")

[`VectorStoreToolkit`](/docs/api/agents/classes/VectorStoreToolkit)

#### Overrides[](#overrides "Direct link to Overrides")

[Toolkit](/docs/api/agents/classes/Toolkit).[constructor](/docs/api/agents/classes/Toolkit#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/agents/toolkits/vectorstore/vectorstore.ts:23](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/toolkits/vectorstore/vectorstore.ts#L23)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### llm[](#llm "Direct link to llm")

> **llm**: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/agents/toolkits/vectorstore/vectorstore.ts:21](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/toolkits/vectorstore/vectorstore.ts#L21)

### tools[](#tools "Direct link to tools")

> **tools**: [`Tool`](/docs/api/tools/classes/Tool)\[\]

#### Overrides[](#overrides-1 "Direct link to Overrides")

[Toolkit](/docs/api/agents/classes/Toolkit).[tools](/docs/api/agents/classes/Toolkit#tools)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/agents/toolkits/vectorstore/vectorstore.ts:19](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/toolkits/vectorstore/vectorstore.ts#L19)