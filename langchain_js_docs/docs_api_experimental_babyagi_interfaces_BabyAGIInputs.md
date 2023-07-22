BabyAGIInputs
=============

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   `Omit`<[`ChainInputs`](/docs/api/chains/interfaces/ChainInputs), "memory" | "callbackManager"\>.**BabyAGIInputs**

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### creationChain[​](#creationchain "Direct link to creationChain")

> **creationChain**: [`BaseChain`](/docs/api/chains/classes/BaseChain)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/experimental/babyagi/agent.ts:20](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/babyagi/agent.ts#L20)

### executionChain[​](#executionchain "Direct link to executionChain")

> **executionChain**: [`BaseChain`](/docs/api/chains/classes/BaseChain)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/experimental/babyagi/agent.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/babyagi/agent.ts#L22)

### prioritizationChain[​](#prioritizationchain "Direct link to prioritizationChain")

> **prioritizationChain**: [`BaseChain`](/docs/api/chains/classes/BaseChain)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/experimental/babyagi/agent.ts:21](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/babyagi/agent.ts#L21)

### vectorstore[​](#vectorstore "Direct link to vectorstore")

> **vectorstore**: [`VectorStore`](/docs/api/vectorstores_base/classes/VectorStore)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/experimental/babyagi/agent.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/babyagi/agent.ts#L23)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

Omit.callbacks

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L23)

### maxIterations?[​](#maxiterations "Direct link to maxIterations?")

> **maxIterations**: `number`

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/experimental/babyagi/agent.ts:24](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/babyagi/agent.ts#L24)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

Omit.metadata

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:25](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L25)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

Omit.tags

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:24](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L24)

### verbose?[​](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

Omit.verbose

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L22)