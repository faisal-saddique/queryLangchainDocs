AgentExecutorInput
==================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`ChainInputs`](/docs/api/chains/interfaces/ChainInputs).**AgentExecutorInput**

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### agent[](#agent "Direct link to agent")

> **agent**: [`BaseSingleActionAgent`](/docs/api/agents/classes/BaseSingleActionAgent) | `BaseMultiActionAgent`

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/agents/executor.ts:14](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/executor.ts#L14)

### tools[](#tools "Direct link to tools")

> **tools**: [`StructuredTool`](/docs/api/tools/classes/StructuredTool)<`ZodObject`<`any`, `any`, `any`, `any`, {}\>\>\[\]

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/agents/executor.ts:15](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/executor.ts#L15)

### callbackManager?[](#callbackmanager "Direct link to callbackManager?")

> **callbackManager**: [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Deprecated[](#deprecated "Direct link to Deprecated")

Use `callbacks` instead

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[callbackManager](/docs/api/chains/interfaces/ChainInputs#callbackmanager)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/chains/base.ts:22](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L22)

### callbacks?[](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[callbacks](/docs/api/chains/interfaces/ChainInputs#callbacks)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:25](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L25)

### earlyStoppingMethod?[](#earlystoppingmethod "Direct link to earlyStoppingMethod?")

> **earlyStoppingMethod**: [`StoppingMethod`](/docs/api/agents/types/StoppingMethod)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/agents/executor.ts:18](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/executor.ts#L18)

### maxIterations?[](#maxiterations "Direct link to maxIterations?")

> **maxIterations**: `number`

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/agents/executor.ts:17](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/executor.ts#L17)

### memory?[](#memory "Direct link to memory?")

> **memory**: [`BaseMemory`](/docs/api/memory/classes/BaseMemory)

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[memory](/docs/api/chains/interfaces/ChainInputs#memory)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/chains/base.ts:17](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L17)

### metadata?[](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[metadata](/docs/api/chains/interfaces/ChainInputs#metadata)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:27](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L27)

### returnIntermediateSteps?[](#returnintermediatesteps "Direct link to returnIntermediateSteps?")

> **returnIntermediateSteps**: `boolean`

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/agents/executor.ts:16](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/executor.ts#L16)

### tags?[](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[tags](/docs/api/chains/interfaces/ChainInputs#tags)

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L26)

### verbose?[](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[verbose](/docs/api/chains/interfaces/ChainInputs#verbose)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:24](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L24)