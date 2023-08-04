InitializeAgentExecutorOptions
==============================

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### agentType[](#agenttype "Direct link to agentType")

> **agentType**: "zero-shot-react-description" | "chat-zero-shot-react-description" | "chat-conversational-react-description"

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/agents/initialize.ts:64](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/initialize.ts#L64) [langchain/src/agents/initialize.ts:69](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/initialize.ts#L69) [langchain/src/agents/initialize.ts:74](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/initialize.ts#L74)

### agentArgs?[](#agentargs "Direct link to agentArgs?")

> **agentArgs**: [`ZeroShotCreatePromptArgs`](/docs/api/agents/interfaces/ZeroShotCreatePromptArgs) & [`AgentArgs`](/docs/api/agents/interfaces/AgentArgs) | [`ChatCreatePromptArgs`](/docs/api/agents/interfaces/ChatCreatePromptArgs) & [`AgentArgs`](/docs/api/agents/interfaces/AgentArgs) | [`ChatConversationalCreatePromptArgs`](/docs/api/agents/interfaces/ChatConversationalCreatePromptArgs) & [`AgentArgs`](/docs/api/agents/interfaces/AgentArgs)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/agents/initialize.ts:65](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/initialize.ts#L65) [langchain/src/agents/initialize.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/initialize.ts#L70) [langchain/src/agents/initialize.ts:75](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/initialize.ts#L75)

### callbackManager?[](#callbackmanager "Direct link to callbackManager?")

> **callbackManager**: [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Deprecated[](#deprecated "Direct link to Deprecated")

Use `callbacks` instead

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/chains/base.ts:22](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L22)

### callbacks?[](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

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

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/agents/initialize.ts:66](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/initialize.ts#L66) [langchain/src/chains/base.ts:17](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L17) [langchain/src/agents/initialize.ts:71](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/initialize.ts#L71) [langchain/src/chains/base.ts:17](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L17) [langchain/src/chains/base.ts:17](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L17)

### metadata?[](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:27](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L27)

### returnIntermediateSteps?[](#returnintermediatesteps "Direct link to returnIntermediateSteps?")

> **returnIntermediateSteps**: `boolean`

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/agents/executor.ts:16](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/executor.ts#L16)

### tags?[](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L26)

### verbose?[](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:24](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L24)