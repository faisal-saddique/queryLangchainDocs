OpenAIAgentInput
================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`AgentInput`](/docs/api/agents/interfaces/AgentInput).**OpenAIAgentInput**

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### llmChain[](#llmchain "Direct link to llmChain")

> **llmChain**: [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>\>

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[AgentInput](/docs/api/agents/interfaces/AgentInput).[llmChain](/docs/api/agents/interfaces/AgentInput#llmchain)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/agents/types.ts:7](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/types.ts#L7)

### outputParser[](#outputparser "Direct link to outputParser")

> **outputParser**: `undefined` | [`AgentActionOutputParser`](/docs/api/agents/classes/AgentActionOutputParser)

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[AgentInput](/docs/api/agents/interfaces/AgentInput).[outputParser](/docs/api/agents/interfaces/AgentInput#outputparser)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/agents/types.ts:8](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/types.ts#L8)

### tools[](#tools "Direct link to tools")

> **tools**: [`StructuredTool`](/docs/api/tools/classes/StructuredTool)<`ZodObject`<`any`, `any`, `any`, `any`, {}\>\>\[\]

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/agents/openai/index.ts:88](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/openai/index.ts#L88)

### allowedTools?[](#allowedtools "Direct link to allowedTools?")

> **allowedTools**: `string`\[\]

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[AgentInput](/docs/api/agents/interfaces/AgentInput).[allowedTools](/docs/api/agents/interfaces/AgentInput#allowedtools)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/agents/types.ts:9](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/types.ts#L9)