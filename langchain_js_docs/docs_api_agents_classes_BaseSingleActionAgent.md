BaseSingleActionAgent
=====================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   `BaseAgent`.**BaseSingleActionAgent**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new BaseSingleActionAgent**(`kwargs`?: `SerializedFields`, ...`_args`?: `never`\[\]): [`BaseSingleActionAgent`](/docs/api/agents/classes/BaseSingleActionAgent)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`kwargs?`

`SerializedFields`

`..._args?`

`never`\[\]

#### Returns[​](#returns "Direct link to Returns")

[`BaseSingleActionAgent`](/docs/api/agents/classes/BaseSingleActionAgent)

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

BaseAgent.constructor

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/load/serializable.ts:94](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L94)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### ToolType[​](#tooltype "Direct link to ToolType")

> **ToolType**: [`StructuredTool`](/docs/api/tools/classes/StructuredTool)<`ZodObject`<`any`, `any`, `any`, `any`, {}\>\>

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

BaseAgent.ToolType

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/agents/agent.ts:34](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/agents/agent.ts#L34)

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

BaseAgent.lc\_kwargs

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

> `Abstract` **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

BaseAgent.lc\_namespace

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/load/serializable.ts:63](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L63)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

BaseAgent.lc\_serializable

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L55)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### allowedTools[​](#allowedtools "Direct link to allowedTools")

> **allowedTools**(): `undefined` | `string`\[\]

#### Returns[​](#returns-1 "Direct link to Returns")

`undefined` | `string`\[\]

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

BaseAgent.allowedTools

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/agents/agent.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/agents/agent.ts#L42)

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

BaseAgent.allowedTools

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/agents/agent.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/agents/agent.ts#L42)

### inputKeys[​](#inputkeys "Direct link to inputKeys")

> `Abstract` **inputKeys**(): `string`\[\]

#### Returns[​](#returns-2 "Direct link to Returns")

`string`\[\]

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

BaseAgent.inputKeys

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/agents/agent.ts:36](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/agents/agent.ts#L36)

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

BaseAgent.inputKeys

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/agents/agent.ts:36](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/agents/agent.ts#L36)

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

BaseAgent.lc\_aliases

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

BaseAgent.lc\_aliases

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[​](#returns-4 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

BaseAgent.lc\_attributes

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

BaseAgent.lc\_attributes

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-5 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

BaseAgent.lc\_secrets

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

BaseAgent.lc\_secrets

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

### returnValues[​](#returnvalues "Direct link to returnValues")

> **returnValues**(): `string`\[\]

#### Returns[​](#returns-6 "Direct link to Returns")

`string`\[\]

#### Inherited from[​](#inherited-from-15 "Direct link to Inherited from")

BaseAgent.returnValues

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/agents/agent.ts:38](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/agents/agent.ts#L38)

#### Inherited from[​](#inherited-from-16 "Direct link to Inherited from")

BaseAgent.returnValues

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/agents/agent.ts:38](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/agents/agent.ts#L38)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### \_agentActionType()[​](#_agentactiontype "Direct link to _agentactiontype")

> **\_agentActionType**(): `string`

#### Returns[​](#returns-7 "Direct link to Returns")

`string`

#### Overrides[​](#overrides "Direct link to Overrides")

BaseAgent.\_agentActionType

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/agents/agent.ts:89](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/agents/agent.ts#L89)

### \_agentType()[​](#_agenttype "Direct link to _agenttype")

Return the string type key uniquely identifying this class of agent.

> **\_agentType**(): `string`

#### Returns[​](#returns-8 "Direct link to Returns")

`string`

#### Inherited from[​](#inherited-from-17 "Direct link to Inherited from")

BaseAgent.\_agentType

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/agents/agent.ts:49](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/agents/agent.ts#L49)

### plan()[​](#plan "Direct link to plan()")

Decide what to do, given some input.

> `Abstract` **plan**(`steps`: [`AgentStep`](/docs/api/schema/types/AgentStep)\[\], `inputs`: [`ChainValues`](/docs/api/schema/types/ChainValues), `callbackManager`?: [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)): `Promise`<[`AgentAction`](/docs/api/schema/types/AgentAction) | [`AgentFinish`](/docs/api/schema/types/AgentFinish)\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

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

Callback manager.

#### Returns[​](#returns-9 "Direct link to Returns")

`Promise`<[`AgentAction`](/docs/api/schema/types/AgentAction) | [`AgentFinish`](/docs/api/schema/types/AgentFinish)\>

Action specifying what tool to use.

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/agents/agent.ts:102](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/agents/agent.ts#L102)

### prepareForOutput()[​](#prepareforoutput "Direct link to prepareForOutput()")

Prepare the agent for output, if needed

> **prepareForOutput**(`_returnValues`: `Record`<`string`, `any`\>, `_steps`: [`AgentStep`](/docs/api/schema/types/AgentStep)\[\]): `Promise`<`Record`<`string`, `any`\>\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`_returnValues`

`Record`<`string`, `any`\>

`_steps`

[`AgentStep`](/docs/api/schema/types/AgentStep)\[\]

#### Returns[​](#returns-10 "Direct link to Returns")

`Promise`<`Record`<`string`, `any`\>\>

#### Inherited from[​](#inherited-from-18 "Direct link to Inherited from")

BaseAgent.prepareForOutput

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/agents/agent.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/agents/agent.ts#L80)

### returnStoppedResponse()[​](#returnstoppedresponse "Direct link to returnStoppedResponse()")

Return response when agent has been stopped due to max iterations

> **returnStoppedResponse**(`earlyStoppingMethod`: [`StoppingMethod`](/docs/api/agents/types/StoppingMethod), `_steps`: [`AgentStep`](/docs/api/schema/types/AgentStep)\[\], `_inputs`: [`ChainValues`](/docs/api/schema/types/ChainValues), `_callbackManager`?: [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)): `Promise`<[`AgentFinish`](/docs/api/schema/types/AgentFinish)\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`earlyStoppingMethod`

[`StoppingMethod`](/docs/api/agents/types/StoppingMethod)

`_steps`

[`AgentStep`](/docs/api/schema/types/AgentStep)\[\]

`_inputs`

[`ChainValues`](/docs/api/schema/types/ChainValues)

`_callbackManager?`

[`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Returns[​](#returns-11 "Direct link to Returns")

`Promise`<[`AgentFinish`](/docs/api/schema/types/AgentFinish)\>

#### Inherited from[​](#inherited-from-19 "Direct link to Inherited from")

BaseAgent.returnStoppedResponse

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/agents/agent.ts:61](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/agents/agent.ts#L61)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-12 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-20 "Direct link to Inherited from")

BaseAgent.toJSON

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-13 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-21 "Direct link to Inherited from")

BaseAgent.toJSONNotImplemented

#### Defined in[​](#defined-in-23 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)