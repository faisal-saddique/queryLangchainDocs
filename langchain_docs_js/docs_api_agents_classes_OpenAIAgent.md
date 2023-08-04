OpenAIAgent
===========

Class responsible for calling a language model and deciding an action.

Remarks[](#remarks "Direct link to Remarks")
---------------------------------------------

This is driven by an LLMChain. The prompt in the LLMChain _must_ include a variable called "agent\_scratchpad" where the agent can put its intermediary work.

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`Agent`](/docs/api/agents/classes/Agent).**OpenAIAgent**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new OpenAIAgent**(`input`: `Omit`<[`OpenAIAgentInput`](/docs/api/agents/interfaces/OpenAIAgentInput), "outputParser"\>): [`OpenAIAgent`](/docs/api/agents/classes/OpenAIAgent)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`input`

`Omit`<[`OpenAIAgentInput`](/docs/api/agents/interfaces/OpenAIAgentInput), "outputParser"\>

#### Returns[](#returns "Direct link to Returns")

[`OpenAIAgent`](/docs/api/agents/classes/OpenAIAgent)

#### Overrides[](#overrides "Direct link to Overrides")

[Agent](/docs/api/agents/classes/Agent).[constructor](/docs/api/agents/classes/Agent#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/agents/openai/index.ts:117](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/openai/index.ts#L117)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### ToolType[](#tooltype "Direct link to ToolType")

> **ToolType**: [`StructuredTool`](/docs/api/tools/classes/StructuredTool)<`ZodObject`<`any`, `any`, `any`, `any`, {}\>\>

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[Agent](/docs/api/agents/classes/Agent).[ToolType](/docs/api/agents/classes/Agent#tooltype)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/agents/agent.ts:34](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/agent.ts#L34)

### lc\_kwargs[](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[Agent](/docs/api/agents/classes/Agent).[lc\_kwargs](/docs/api/agents/classes/Agent#lc_kwargs)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L57)

### lc\_namespace[](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Overrides[](#overrides-1 "Direct link to Overrides")

[Agent](/docs/api/agents/classes/Agent).[lc\_namespace](/docs/api/agents/classes/Agent#lc_namespace)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/agents/openai/index.ts:97](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/openai/index.ts#L97)

### lc\_serializable[](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[Agent](/docs/api/agents/classes/Agent).[lc\_serializable](/docs/api/agents/classes/Agent#lc_serializable)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L55)

### llmChain[](#llmchain "Direct link to llmChain")

> **llmChain**: [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>\>

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[Agent](/docs/api/agents/classes/Agent).[llmChain](/docs/api/agents/classes/Agent#llmchain)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/agents/agent.ts:204](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/agent.ts#L204)

### outputParser[](#outputparser "Direct link to outputParser")

> **outputParser**: `undefined` | [`AgentActionOutputParser`](/docs/api/agents/classes/AgentActionOutputParser)

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[Agent](/docs/api/agents/classes/Agent).[outputParser](/docs/api/agents/classes/Agent#outputparser)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/agents/agent.ts:206](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/agent.ts#L206)

### tools[](#tools "Direct link to tools")

> **tools**: [`StructuredTool`](/docs/api/tools/classes/StructuredTool)<`ZodObject`<`any`, `any`, `any`, `any`, {}\>\>\[\]

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/agents/openai/index.ts:115](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/openai/index.ts#L115)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### allowedTools[](#allowedtools "Direct link to allowedTools")

> **allowedTools**(): `undefined` | `string`\[\]

#### Returns[](#returns-1 "Direct link to Returns")

`undefined` | `string`\[\]

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

Agent.allowedTools

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/agents/agent.ts:210](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/agent.ts#L210)

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[Agent](/docs/api/agents/classes/Agent).[allowedTools](/docs/api/agents/classes/Agent#allowedtools)

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/agents/agent.ts:210](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/agent.ts#L210)

### inputKeys[](#inputkeys "Direct link to inputKeys")

> **inputKeys**(): `string`\[\]

#### Returns[](#returns-2 "Direct link to Returns")

`string`\[\]

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

Agent.inputKeys

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/agents/agent.ts:214](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/agent.ts#L214)

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

[Agent](/docs/api/agents/classes/Agent).[inputKeys](/docs/api/agents/classes/Agent#inputkeys)

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/agents/agent.ts:214](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/agent.ts#L214)

### lc\_aliases[](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-9 "Direct link to Inherited from")

Agent.lc\_aliases

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

#### Inherited from[](#inherited-from-10 "Direct link to Inherited from")

[Agent](/docs/api/agents/classes/Agent).[lc\_aliases](/docs/api/agents/classes/Agent#lc_aliases)

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

### lc\_attributes[](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[](#returns-4 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[](#inherited-from-11 "Direct link to Inherited from")

Agent.lc\_attributes

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L80)

#### Inherited from[](#inherited-from-12 "Direct link to Inherited from")

[Agent](/docs/api/agents/classes/Agent).[lc\_attributes](/docs/api/agents/classes/Agent#lc_attributes)

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L80)

### lc\_secrets[](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[](#returns-5 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-13 "Direct link to Inherited from")

Agent.lc\_secrets

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

#### Inherited from[](#inherited-from-14 "Direct link to Inherited from")

[Agent](/docs/api/agents/classes/Agent).[lc\_secrets](/docs/api/agents/classes/Agent#lc_secrets)

#### Defined in[](#defined-in-17 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

### returnValues[](#returnvalues "Direct link to returnValues")

> **returnValues**(): `string`\[\]

#### Returns[](#returns-6 "Direct link to Returns")

`string`\[\]

#### Inherited from[](#inherited-from-15 "Direct link to Inherited from")

Agent.returnValues

#### Defined in[](#defined-in-18 "Direct link to Defined in")

[langchain/src/agents/agent.ts:38](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/agent.ts#L38)

#### Inherited from[](#inherited-from-16 "Direct link to Inherited from")

[Agent](/docs/api/agents/classes/Agent).[returnValues](/docs/api/agents/classes/Agent#returnvalues)

#### Defined in[](#defined-in-19 "Direct link to Defined in")

[langchain/src/agents/agent.ts:38](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/agent.ts#L38)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### \_agentActionType()[](#_agentactiontype "Direct link to _agentactiontype")

> **\_agentActionType**(): `string`

#### Returns[](#returns-7 "Direct link to Returns")

`string`

#### Inherited from[](#inherited-from-17 "Direct link to Inherited from")

[Agent](/docs/api/agents/classes/Agent).[\_agentActionType](/docs/api/agents/classes/Agent#_agentactiontype)

#### Defined in[](#defined-in-20 "Direct link to Defined in")

[langchain/src/agents/agent.ts:89](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/agent.ts#L89)

### \_agentType()[](#_agenttype "Direct link to _agenttype")

Return the string type key uniquely identifying this class of agent.

> **\_agentType**(): "openai-functions"

#### Returns[](#returns-8 "Direct link to Returns")

"openai-functions"

#### Overrides[](#overrides-2 "Direct link to Overrides")

[Agent](/docs/api/agents/classes/Agent).[\_agentType](/docs/api/agents/classes/Agent#_agenttype)

#### Defined in[](#defined-in-21 "Direct link to Defined in")

[langchain/src/agents/openai/index.ts:99](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/openai/index.ts#L99)

### \_stop()[](#_stop "Direct link to _stop")

> **\_stop**(): `string`\[\]

#### Returns[](#returns-9 "Direct link to Returns")

`string`\[\]

#### Overrides[](#overrides-3 "Direct link to Overrides")

[Agent](/docs/api/agents/classes/Agent).[\_stop](/docs/api/agents/classes/Agent#_stop)

#### Defined in[](#defined-in-22 "Direct link to Defined in")

[langchain/src/agents/openai/index.ts:111](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/openai/index.ts#L111)

### constructScratchPad()[](#constructscratchpad "Direct link to constructScratchPad()")

Construct a scratchpad to let the agent continue its thought process

> **constructScratchPad**(`steps`: [`AgentStep`](/docs/api/schema/types/AgentStep)\[\]): `Promise`<`string` | [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`steps`

[`AgentStep`](/docs/api/schema/types/AgentStep)\[\]

#### Returns[](#returns-10 "Direct link to Returns")

`Promise`<`string` | [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]\>

#### Overrides[](#overrides-4 "Direct link to Overrides")

[Agent](/docs/api/agents/classes/Agent).[constructScratchPad](/docs/api/agents/classes/Agent#constructscratchpad)

#### Defined in[](#defined-in-23 "Direct link to Defined in")

[langchain/src/agents/openai/index.ts:157](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/openai/index.ts#L157)

### finishToolName()[](#finishtoolname "Direct link to finishToolName()")

Name of tool to use to terminate the chain.

> **finishToolName**(): `string`

#### Returns[](#returns-11 "Direct link to Returns")

`string`

#### Inherited from[](#inherited-from-18 "Direct link to Inherited from")

[Agent](/docs/api/agents/classes/Agent).[finishToolName](/docs/api/agents/classes/Agent#finishtoolname)

#### Defined in[](#defined-in-24 "Direct link to Defined in")

[langchain/src/agents/agent.ts:287](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/agent.ts#L287)

### llmPrefix()[](#llmprefix "Direct link to llmPrefix()")

Prefix to append the LLM call with.

> **llmPrefix**(): `string`

#### Returns[](#returns-12 "Direct link to Returns")

`string`

#### Overrides[](#overrides-5 "Direct link to Overrides")

[Agent](/docs/api/agents/classes/Agent).[llmPrefix](/docs/api/agents/classes/Agent#llmprefix)

#### Defined in[](#defined-in-25 "Direct link to Defined in")

[langchain/src/agents/openai/index.ts:107](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/openai/index.ts#L107)

### observationPrefix()[](#observationprefix "Direct link to observationPrefix()")

Prefix to append the observation with.

> **observationPrefix**(): `string`

#### Returns[](#returns-13 "Direct link to Returns")

`string`

#### Overrides[](#overrides-6 "Direct link to Overrides")

[Agent](/docs/api/agents/classes/Agent).[observationPrefix](/docs/api/agents/classes/Agent#observationprefix)

#### Defined in[](#defined-in-26 "Direct link to Defined in")

[langchain/src/agents/openai/index.ts:103](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/openai/index.ts#L103)

### plan()[](#plan "Direct link to plan()")

Decide what to do given some input.

> **plan**(`steps`: [`AgentStep`](/docs/api/schema/types/AgentStep)\[\], `inputs`: [`ChainValues`](/docs/api/schema/types/ChainValues), `callbackManager`?: [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)): `Promise`<[`AgentAction`](/docs/api/schema/types/AgentAction) | [`AgentFinish`](/docs/api/schema/types/AgentFinish)\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

Description

`steps`

[`AgentStep`](/docs/api/schema/types/AgentStep)\[\]

Steps the LLM has taken so far, along with observations from each.

`inputs`

[`ChainValues`](/docs/api/schema/types/ChainValues)

User inputs.

`callbackManager?`

[`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

Callback manager to use for this call.

#### Returns[](#returns-14 "Direct link to Returns")

`Promise`<[`AgentAction`](/docs/api/schema/types/AgentAction) | [`AgentFinish`](/docs/api/schema/types/AgentFinish)\>

Action specifying what tool to use.

#### Overrides[](#overrides-7 "Direct link to Overrides")

[Agent](/docs/api/agents/classes/Agent).[plan](/docs/api/agents/classes/Agent#plan)

#### Defined in[](#defined-in-27 "Direct link to Defined in")

[langchain/src/agents/openai/index.ts:163](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/openai/index.ts#L163)

### prepareForOutput()[](#prepareforoutput "Direct link to prepareForOutput()")

Prepare the agent for output, if needed

> **prepareForOutput**(`_returnValues`: `Record`<`string`, `any`\>, `_steps`: [`AgentStep`](/docs/api/schema/types/AgentStep)\[\]): `Promise`<`Record`<`string`, `any`\>\>

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

`_returnValues`

`Record`<`string`, `any`\>

`_steps`

[`AgentStep`](/docs/api/schema/types/AgentStep)\[\]

#### Returns[](#returns-15 "Direct link to Returns")

`Promise`<`Record`<`string`, `any`\>\>

#### Inherited from[](#inherited-from-19 "Direct link to Inherited from")

[Agent](/docs/api/agents/classes/Agent).[prepareForOutput](/docs/api/agents/classes/Agent#prepareforoutput)

#### Defined in[](#defined-in-28 "Direct link to Defined in")

[langchain/src/agents/agent.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/agent.ts#L80)

### returnStoppedResponse()[](#returnstoppedresponse "Direct link to returnStoppedResponse()")

Return response when agent has been stopped due to max iterations

> **returnStoppedResponse**(`earlyStoppingMethod`: [`StoppingMethod`](/docs/api/agents/types/StoppingMethod), `steps`: [`AgentStep`](/docs/api/schema/types/AgentStep)\[\], `inputs`: [`ChainValues`](/docs/api/schema/types/ChainValues), `callbackManager`?: [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)): `Promise`<[`AgentFinish`](/docs/api/schema/types/AgentFinish)\>

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

`earlyStoppingMethod`

[`StoppingMethod`](/docs/api/agents/types/StoppingMethod)

`steps`

[`AgentStep`](/docs/api/schema/types/AgentStep)\[\]

`inputs`

[`ChainValues`](/docs/api/schema/types/ChainValues)

`callbackManager?`

[`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Returns[](#returns-16 "Direct link to Returns")

`Promise`<[`AgentFinish`](/docs/api/schema/types/AgentFinish)\>

#### Inherited from[](#inherited-from-20 "Direct link to Inherited from")

[Agent](/docs/api/agents/classes/Agent).[returnStoppedResponse](/docs/api/agents/classes/Agent#returnstoppedresponse)

#### Defined in[](#defined-in-29 "Direct link to Defined in")

[langchain/src/agents/agent.ts:352](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/agent.ts#L352)

### toJSON()[](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[](#returns-17 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[](#inherited-from-21 "Direct link to Inherited from")

[Agent](/docs/api/agents/classes/Agent).[toJSON](/docs/api/agents/classes/Agent#tojson)

#### Defined in[](#defined-in-30 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[](#returns-18 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[](#inherited-from-22 "Direct link to Inherited from")

[Agent](/docs/api/agents/classes/Agent).[toJSONNotImplemented](/docs/api/agents/classes/Agent#tojsonnotimplemented)

#### Defined in[](#defined-in-31 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L151)

### createPrompt()[](#createprompt "Direct link to createPrompt()")

Create a prompt for this class

> `Static` **createPrompt**(`_tools`: [`StructuredTool`](/docs/api/tools/classes/StructuredTool)<`ZodObject`<`any`, `any`, `any`, `any`, {}\>\>\[\], `fields`?: [`OpenAIAgentCreatePromptArgs`](/docs/api/agents/interfaces/OpenAIAgentCreatePromptArgs)): [`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)<[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\>

#### Parameters[](#parameters-5 "Direct link to Parameters")

Parameter

Type

Description

`_tools`

[`StructuredTool`](/docs/api/tools/classes/StructuredTool)<`ZodObject`<`any`, `any`, `any`, `any`, {}\>\>\[\]

List of tools the agent will have access to, used to format the prompt.

`fields?`

[`OpenAIAgentCreatePromptArgs`](/docs/api/agents/interfaces/OpenAIAgentCreatePromptArgs)

Additional fields used to format the prompt.

#### Returns[](#returns-19 "Direct link to Returns")

[`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)<[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\>

A PromptTemplate assembled from the given tools and fields.

#### Overrides[](#overrides-8 "Direct link to Overrides")

[Agent](/docs/api/agents/classes/Agent).[createPrompt](/docs/api/agents/classes/Agent#createprompt)

#### Defined in[](#defined-in-32 "Direct link to Defined in")

[langchain/src/agents/openai/index.ts:122](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/openai/index.ts#L122)

### deserialize()[](#deserialize "Direct link to deserialize()")

Load an agent from a json-like object describing it.

> `Static` **deserialize**(`data`: `Object`): `Promise`<[`Agent`](/docs/api/agents/classes/Agent)\>

#### Parameters[](#parameters-6 "Direct link to Parameters")

Parameter

Type

`data`

`Object`

#### Returns[](#returns-20 "Direct link to Returns")

`Promise`<[`Agent`](/docs/api/agents/classes/Agent)\>

#### Inherited from[](#inherited-from-23 "Direct link to Inherited from")

[Agent](/docs/api/agents/classes/Agent).[deserialize](/docs/api/agents/classes/Agent#deserialize)

#### Defined in[](#defined-in-33 "Direct link to Defined in")

[langchain/src/agents/agent.ts:394](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/agent.ts#L394)

### fromLLMAndTools()[](#fromllmandtools "Direct link to fromLLMAndTools()")

Construct an agent from an LLM and a list of tools

> `Static` **fromLLMAndTools**(`llm`: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>, `tools`: [`StructuredTool`](/docs/api/tools/classes/StructuredTool)<`ZodObject`<`any`, `any`, `any`, `any`, {}\>\>\[\], `args`?: [`OpenAIAgentCreatePromptArgs`](/docs/api/agents/interfaces/OpenAIAgentCreatePromptArgs) & `Pick`<[`AgentArgs`](/docs/api/agents/interfaces/AgentArgs), "callbacks"\>): [`OpenAIAgent`](/docs/api/agents/classes/OpenAIAgent)

#### Parameters[](#parameters-7 "Direct link to Parameters")

Parameter

Type

`llm`

[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>

`tools`

[`StructuredTool`](/docs/api/tools/classes/StructuredTool)<`ZodObject`<`any`, `any`, `any`, `any`, {}\>\>\[\]

`args?`

[`OpenAIAgentCreatePromptArgs`](/docs/api/agents/interfaces/OpenAIAgentCreatePromptArgs) & `Pick`<[`AgentArgs`](/docs/api/agents/interfaces/AgentArgs), "callbacks"\>

#### Returns[](#returns-21 "Direct link to Returns")

[`OpenAIAgent`](/docs/api/agents/classes/OpenAIAgent)

#### Overrides[](#overrides-9 "Direct link to Overrides")

[Agent](/docs/api/agents/classes/Agent).[fromLLMAndTools](/docs/api/agents/classes/Agent#fromllmandtools)

#### Defined in[](#defined-in-34 "Direct link to Defined in")

[langchain/src/agents/openai/index.ts:135](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/openai/index.ts#L135)

### getDefaultOutputParser()[](#getdefaultoutputparser "Direct link to getDefaultOutputParser()")

Get the default output parser for this agent.

> `Static` **getDefaultOutputParser**(`_fields`?: [`OutputParserArgs`](/docs/api/agents/types/OutputParserArgs)): [`AgentActionOutputParser`](/docs/api/agents/classes/AgentActionOutputParser)

#### Parameters[](#parameters-8 "Direct link to Parameters")

Parameter

Type

`_fields?`

[`OutputParserArgs`](/docs/api/agents/types/OutputParserArgs)

#### Returns[](#returns-22 "Direct link to Returns")

[`AgentActionOutputParser`](/docs/api/agents/classes/AgentActionOutputParser)

#### Inherited from[](#inherited-from-24 "Direct link to Inherited from")

[Agent](/docs/api/agents/classes/Agent).[getDefaultOutputParser](/docs/api/agents/classes/Agent#getdefaultoutputparser)

#### Defined in[](#defined-in-35 "Direct link to Defined in")

[langchain/src/agents/agent.ts:243](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/agent.ts#L243)

### validateTools()[](#validatetools "Direct link to validateTools()")

Validate that appropriate tools are passed in

> `Static` **validateTools**(`_tools`: [`StructuredTool`](/docs/api/tools/classes/StructuredTool)<`ZodObject`<`any`, `any`, `any`, `any`, {}\>\>\[\]): `void`

#### Parameters[](#parameters-9 "Direct link to Parameters")

Parameter

Type

`_tools`

[`StructuredTool`](/docs/api/tools/classes/StructuredTool)<`ZodObject`<`any`, `any`, `any`, `any`, {}\>\>\[\]

#### Returns[](#returns-23 "Direct link to Returns")

`void`

#### Inherited from[](#inherited-from-25 "Direct link to Inherited from")

[Agent](/docs/api/agents/classes/Agent).[validateTools](/docs/api/agents/classes/Agent#validatetools)

#### Defined in[](#defined-in-36 "Direct link to Defined in")

[langchain/src/agents/agent.ts:278](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/agents/agent.ts#L278)