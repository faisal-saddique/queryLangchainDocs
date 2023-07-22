BaseCallbackHandler
===================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   `BaseCallbackHandlerMethodsClass`.**BaseCallbackHandler**

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   [`BaseCallbackHandlerInput`](/docs/api/callbacks/interfaces/BaseCallbackHandlerInput)
*   [`Serializable`](/docs/api/load_serializable/classes/Serializable)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new BaseCallbackHandler**(`input`?: [`BaseCallbackHandlerInput`](/docs/api/callbacks/interfaces/BaseCallbackHandlerInput)): [`BaseCallbackHandler`](/docs/api/callbacks/classes/BaseCallbackHandler)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`input?`

[`BaseCallbackHandlerInput`](/docs/api/callbacks/interfaces/BaseCallbackHandlerInput)

#### Returns[​](#returns "Direct link to Returns")

[`BaseCallbackHandler`](/docs/api/callbacks/classes/BaseCallbackHandler)

#### Overrides[​](#overrides "Direct link to Overrides")

BaseCallbackHandlerMethodsClass.constructor

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/callbacks/base.ts:268](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L268)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### awaitHandlers[​](#awaithandlers "Direct link to awaitHandlers")

> **awaitHandlers**: `boolean`

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:262](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L262)

### ignoreAgent[​](#ignoreagent "Direct link to ignoreAgent")

> **ignoreAgent**: `boolean` = `false`

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

[BaseCallbackHandlerInput](/docs/api/callbacks/interfaces/BaseCallbackHandlerInput).[ignoreAgent](/docs/api/callbacks/interfaces/BaseCallbackHandlerInput#ignoreagent)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:258](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L258)

### ignoreChain[​](#ignorechain "Direct link to ignoreChain")

> **ignoreChain**: `boolean` = `false`

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

[BaseCallbackHandlerInput](/docs/api/callbacks/interfaces/BaseCallbackHandlerInput).[ignoreChain](/docs/api/callbacks/interfaces/BaseCallbackHandlerInput#ignorechain)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:256](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L256)

### ignoreLLM[​](#ignorellm "Direct link to ignoreLLM")

> **ignoreLLM**: `boolean` = `false`

#### Implementation of[​](#implementation-of-2 "Direct link to Implementation of")

[BaseCallbackHandlerInput](/docs/api/callbacks/interfaces/BaseCallbackHandlerInput).[ignoreLLM](/docs/api/callbacks/interfaces/BaseCallbackHandlerInput#ignorellm)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:254](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L254)

### ignoreRetriever[​](#ignoreretriever "Direct link to ignoreRetriever")

> **ignoreRetriever**: `boolean` = `false`

#### Implementation of[​](#implementation-of-3 "Direct link to Implementation of")

[BaseCallbackHandlerInput](/docs/api/callbacks/interfaces/BaseCallbackHandlerInput).[ignoreRetriever](/docs/api/callbacks/interfaces/BaseCallbackHandlerInput#ignoreretriever)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:260](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L260)

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Implementation of[​](#implementation-of-4 "Direct link to Implementation of")

[Serializable](/docs/api/load_serializable/classes/Serializable).[lc\_kwargs](/docs/api/load_serializable/classes/Serializable#lc_kwargs)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:250](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L250)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Implementation of[​](#implementation-of-5 "Direct link to Implementation of")

[Serializable](/docs/api/load_serializable/classes/Serializable).[lc\_serializable](/docs/api/load_serializable/classes/Serializable#lc_serializable)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:232](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L232)

### name[​](#name "Direct link to name")

> `Abstract` **name**: `string`

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:252](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L252)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-1 "Direct link to Returns")

`undefined` | {}

#### Implementation of[​](#implementation-of-6 "Direct link to Implementation of")

Serializable.lc\_aliases

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:246](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L246)

#### Implementation of[​](#implementation-of-7 "Direct link to Implementation of")

[Serializable](/docs/api/load_serializable/classes/Serializable).[lc\_aliases](/docs/api/load_serializable/classes/Serializable#lc_aliases)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:246](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L246)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | {}

#### Implementation of[​](#implementation-of-8 "Direct link to Implementation of")

Serializable.lc\_attributes

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:242](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L242)

#### Implementation of[​](#implementation-of-9 "Direct link to Implementation of")

[Serializable](/docs/api/load_serializable/classes/Serializable).[lc\_attributes](/docs/api/load_serializable/classes/Serializable#lc_attributes)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:242](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L242)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

> **lc\_namespace**(): \["langchain", "callbacks", `string`\]

#### Returns[​](#returns-3 "Direct link to Returns")

\["langchain", "callbacks", `string`\]

#### Implementation of[​](#implementation-of-10 "Direct link to Implementation of")

[Serializable](/docs/api/load_serializable/classes/Serializable).[lc\_namespace](/docs/api/load_serializable/classes/Serializable#lc_namespace)

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:234](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L234)

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Implementation of[​](#implementation-of-11 "Direct link to Implementation of")

[Serializable](/docs/api/load_serializable/classes/Serializable).[lc\_namespace](/docs/api/load_serializable/classes/Serializable#lc_namespace)

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:234](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L234)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-4 "Direct link to Returns")

`undefined` | {}

#### Implementation of[​](#implementation-of-12 "Direct link to Implementation of")

Serializable.lc\_secrets

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:238](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L238)

#### Implementation of[​](#implementation-of-13 "Direct link to Implementation of")

[Serializable](/docs/api/load_serializable/classes/Serializable).[lc\_secrets](/docs/api/load_serializable/classes/Serializable#lc_secrets)

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:238](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L238)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### copy()[​](#copy "Direct link to copy()")

> **copy**(): [`BaseCallbackHandler`](/docs/api/callbacks/classes/BaseCallbackHandler)

#### Returns[​](#returns-5 "Direct link to Returns")

[`BaseCallbackHandler`](/docs/api/callbacks/classes/BaseCallbackHandler)

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:279](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L279)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-6 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Implementation of[​](#implementation-of-14 "Direct link to Implementation of")

[Serializable](/docs/api/load_serializable/classes/Serializable).[toJSON](/docs/api/load_serializable/classes/Serializable#tojson)

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:285](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L285)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-7 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Implementation of[​](#implementation-of-15 "Direct link to Implementation of")

[Serializable](/docs/api/load_serializable/classes/Serializable).[toJSONNotImplemented](/docs/api/load_serializable/classes/Serializable#tojsonnotimplemented)

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:289](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L289)

### handleAgentAction()?[​](#handleagentaction "Direct link to handleAgentAction()?")

Called when an agent is about to execute an action, with the action and the run ID.

> `Optional` **handleAgentAction**(`action`: [`AgentAction`](/docs/api/schema/types/AgentAction), `runId`: `string`, `parentRunId`?: `string`, `tags`?: `string`\[\]): `void` | `Promise`<`void`\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`action`

[`AgentAction`](/docs/api/schema/types/AgentAction)

`runId`

`string`

`parentRunId?`

`string`

`tags?`

`string`\[\]

#### Returns[​](#returns-8 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

BaseCallbackHandlerMethodsClass.handleAgentAction

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:175](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L175)

### handleAgentEnd()?[​](#handleagentend "Direct link to handleAgentEnd()?")

Called when an agent finishes execution, before it exits. with the final output and the run ID.

> `Optional` **handleAgentEnd**(`action`: [`AgentFinish`](/docs/api/schema/types/AgentFinish), `runId`: `string`, `parentRunId`?: `string`, `tags`?: `string`\[\]): `void` | `Promise`<`void`\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`action`

[`AgentFinish`](/docs/api/schema/types/AgentFinish)

`runId`

`string`

`parentRunId?`

`string`

`tags?`

`string`\[\]

#### Returns[​](#returns-9 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

BaseCallbackHandlerMethodsClass.handleAgentEnd

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:186](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L186)

### handleChainEnd()?[​](#handlechainend "Direct link to handleChainEnd()?")

Called at the end of a Chain run, with the outputs and the run ID.

> `Optional` **handleChainEnd**(`outputs`: [`ChainValues`](/docs/api/schema/types/ChainValues), `runId`: `string`, `parentRunId`?: `string`, `tags`?: `string`\[\]): `void` | `Promise`<`void`\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`outputs`

[`ChainValues`](/docs/api/schema/types/ChainValues)

`runId`

`string`

`parentRunId?`

`string`

`tags?`

`string`\[\]

#### Returns[​](#returns-10 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

BaseCallbackHandlerMethodsClass.handleChainEnd

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:124](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L124)

### handleChainError()?[​](#handlechainerror "Direct link to handleChainError()?")

Called if a Chain run encounters an error

> `Optional` **handleChainError**(`err`: `any`, `runId`: `string`, `parentRunId`?: `string`, `tags`?: `string`\[\]): `void` | `Promise`<`void`\>

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`err`

`any`

`runId`

`string`

`parentRunId?`

`string`

`tags?`

`string`\[\]

#### Returns[​](#returns-11 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

BaseCallbackHandlerMethodsClass.handleChainError

#### Defined in[​](#defined-in-23 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:114](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L114)

### handleChainStart()?[​](#handlechainstart "Direct link to handleChainStart()?")

Called at the start of a Chain run, with the chain name and inputs and the run ID.

> `Optional` **handleChainStart**(`chain`: [`Serialized`](/docs/api/load_serializable/types/Serialized), `inputs`: [`ChainValues`](/docs/api/schema/types/ChainValues), `runId`: `string`, `parentRunId`?: `string`, `tags`?: `string`\[\], `metadata`?: `Record`<`string`, `unknown`\>): `void` | `Promise`<`void`\>

#### Parameters[​](#parameters-5 "Direct link to Parameters")

Parameter

Type

`chain`

[`Serialized`](/docs/api/load_serializable/types/Serialized)

`inputs`

[`ChainValues`](/docs/api/schema/types/ChainValues)

`runId`

`string`

`parentRunId?`

`string`

`tags?`

`string`\[\]

`metadata?`

`Record`<`string`, `unknown`\>

#### Returns[​](#returns-12 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

BaseCallbackHandlerMethodsClass.handleChainStart

#### Defined in[​](#defined-in-24 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:102](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L102)

### handleChatModelStart()?[​](#handlechatmodelstart "Direct link to handleChatModelStart()?")

Called at the start of a Chat Model run, with the prompt(s) and the run ID.

> `Optional` **handleChatModelStart**(`llm`: [`Serialized`](/docs/api/load_serializable/types/Serialized), `messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]\[\], `runId`: `string`, `parentRunId`?: `string`, `extraParams`?: `Record`<`string`, `unknown`\>, `tags`?: `string`\[\], `metadata`?: `Record`<`string`, `unknown`\>): `void` | `Promise`<`void`\>

#### Parameters[​](#parameters-6 "Direct link to Parameters")

Parameter

Type

`llm`

[`Serialized`](/docs/api/load_serializable/types/Serialized)

`messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]\[\]

`runId`

`string`

`parentRunId?`

`string`

`extraParams?`

`Record`<`string`, `unknown`\>

`tags?`

`string`\[\]

`metadata?`

`Record`<`string`, `unknown`\>

#### Returns[​](#returns-13 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

BaseCallbackHandlerMethodsClass.handleChatModelStart

#### Defined in[​](#defined-in-25 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:88](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L88)

### handleLLMEnd()?[​](#handlellmend "Direct link to handleLLMEnd()?")

Called at the end of an LLM/ChatModel run, with the output and the run ID.

> `Optional` **handleLLMEnd**(`output`: [`LLMResult`](/docs/api/schema/types/LLMResult), `runId`: `string`, `parentRunId`?: `string`, `tags`?: `string`\[\]): `void` | `Promise`<`void`\>

#### Parameters[​](#parameters-7 "Direct link to Parameters")

Parameter

Type

`output`

[`LLMResult`](/docs/api/schema/types/LLMResult)

`runId`

`string`

`parentRunId?`

`string`

`tags?`

`string`\[\]

#### Returns[​](#returns-14 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

BaseCallbackHandlerMethodsClass.handleLLMEnd

#### Defined in[​](#defined-in-26 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:77](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L77)

### handleLLMError()?[​](#handlellmerror "Direct link to handleLLMError()?")

Called if an LLM/ChatModel run encounters an error

> `Optional` **handleLLMError**(`err`: `any`, `runId`: `string`, `parentRunId`?: `string`, `tags`?: `string`\[\]): `void` | `Promise`<`void`\>

#### Parameters[​](#parameters-8 "Direct link to Parameters")

Parameter

Type

`err`

`any`

`runId`

`string`

`parentRunId?`

`string`

`tags?`

`string`\[\]

#### Returns[​](#returns-15 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

BaseCallbackHandlerMethodsClass.handleLLMError

#### Defined in[​](#defined-in-27 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:67](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L67)

### handleLLMNewToken()?[​](#handlellmnewtoken "Direct link to handleLLMNewToken()?")

Called when an LLM/ChatModel in `streaming` mode produces a new token

> `Optional` **handleLLMNewToken**(`token`: `string`, `idx`: [`NewTokenIndices`](/docs/api/callbacks/interfaces/NewTokenIndices), `runId`: `string`, `parentRunId`?: `string`, `tags`?: `string`\[\]): `void` | `Promise`<`void`\>

#### Parameters[​](#parameters-9 "Direct link to Parameters")

Parameter

Type

Description

`token`

`string`

\-

`idx`

[`NewTokenIndices`](/docs/api/callbacks/interfaces/NewTokenIndices)

idx.prompt is the index of the prompt that produced the token  
(if there are multiple prompts)  
idx.completion is the index of the completion that produced the token  
(if multiple completions per prompt are requested)

`runId`

`string`

\-

`parentRunId?`

`string`

\-

`tags?`

`string`\[\]

\-

#### Returns[​](#returns-16 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

BaseCallbackHandlerMethodsClass.handleLLMNewToken

#### Defined in[​](#defined-in-28 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:50](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L50)

### handleLLMStart()?[​](#handlellmstart "Direct link to handleLLMStart()?")

Called at the start of an LLM or Chat Model run, with the prompt(s) and the run ID.

> `Optional` **handleLLMStart**(`llm`: [`Serialized`](/docs/api/load_serializable/types/Serialized), `prompts`: `string`\[\], `runId`: `string`, `parentRunId`?: `string`, `extraParams`?: `Record`<`string`, `unknown`\>, `tags`?: `string`\[\], `metadata`?: `Record`<`string`, `unknown`\>): `void` | `Promise`<`void`\>

#### Parameters[​](#parameters-10 "Direct link to Parameters")

Parameter

Type

`llm`

[`Serialized`](/docs/api/load_serializable/types/Serialized)

`prompts`

`string`\[\]

`runId`

`string`

`parentRunId?`

`string`

`extraParams?`

`Record`<`string`, `unknown`\>

`tags?`

`string`\[\]

`metadata?`

`Record`<`string`, `unknown`\>

#### Returns[​](#returns-17 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

BaseCallbackHandlerMethodsClass.handleLLMStart

#### Defined in[​](#defined-in-29 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:37](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L37)

### handleRetrieverEnd()?[​](#handleretrieverend "Direct link to handleRetrieverEnd()?")

> `Optional` **handleRetrieverEnd**(`documents`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], `runId`: `string`, `parentRunId`?: `string`, `tags`?: `string`\[\]): `void` | `Promise`<`void`\>

#### Parameters[​](#parameters-11 "Direct link to Parameters")

Parameter

Type

`documents`

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

`runId`

`string`

`parentRunId?`

`string`

`tags?`

`string`\[\]

#### Returns[​](#returns-18 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

BaseCallbackHandlerMethodsClass.handleRetrieverEnd

#### Defined in[​](#defined-in-30 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:202](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L202)

### handleRetrieverError()?[​](#handleretrievererror "Direct link to handleRetrieverError()?")

> `Optional` **handleRetrieverError**(`err`: `any`, `runId`: `string`, `parentRunId`?: `string`, `tags`?: `string`\[\]): `void` | `Promise`<`void`\>

#### Parameters[​](#parameters-12 "Direct link to Parameters")

Parameter

Type

`err`

`any`

`runId`

`string`

`parentRunId?`

`string`

`tags?`

`string`\[\]

#### Returns[​](#returns-19 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

BaseCallbackHandlerMethodsClass.handleRetrieverError

#### Defined in[​](#defined-in-31 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:209](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L209)

### handleRetrieverStart()?[​](#handleretrieverstart "Direct link to handleRetrieverStart()?")

> `Optional` **handleRetrieverStart**(`retriever`: [`Serialized`](/docs/api/load_serializable/types/Serialized), `query`: `string`, `runId`: `string`, `parentRunId`?: `string`, `tags`?: `string`\[\], `metadata`?: `Record`<`string`, `unknown`\>): `void` | `Promise`<`void`\>

#### Parameters[​](#parameters-13 "Direct link to Parameters")

Parameter

Type

`retriever`

[`Serialized`](/docs/api/load_serializable/types/Serialized)

`query`

`string`

`runId`

`string`

`parentRunId?`

`string`

`tags?`

`string`\[\]

`metadata?`

`Record`<`string`, `unknown`\>

#### Returns[​](#returns-20 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

BaseCallbackHandlerMethodsClass.handleRetrieverStart

#### Defined in[​](#defined-in-32 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:193](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L193)

### handleText()?[​](#handletext "Direct link to handleText()?")

> `Optional` **handleText**(`text`: `string`, `runId`: `string`, `parentRunId`?: `string`, `tags`?: `string`\[\]): `void` | `Promise`<`void`\>

#### Parameters[​](#parameters-14 "Direct link to Parameters")

Parameter

Type

`text`

`string`

`runId`

`string`

`parentRunId?`

`string`

`tags?`

`string`\[\]

#### Returns[​](#returns-21 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

BaseCallbackHandlerMethodsClass.handleText

#### Defined in[​](#defined-in-33 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:164](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L164)

### handleToolEnd()?[​](#handletoolend "Direct link to handleToolEnd()?")

Called at the end of a Tool run, with the tool output and the run ID.

> `Optional` **handleToolEnd**(`output`: `string`, `runId`: `string`, `parentRunId`?: `string`, `tags`?: `string`\[\]): `void` | `Promise`<`void`\>

#### Parameters[​](#parameters-15 "Direct link to Parameters")

Parameter

Type

`output`

`string`

`runId`

`string`

`parentRunId?`

`string`

`tags?`

`string`\[\]

#### Returns[​](#returns-22 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

BaseCallbackHandlerMethodsClass.handleToolEnd

#### Defined in[​](#defined-in-34 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:157](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L157)

### handleToolError()?[​](#handletoolerror "Direct link to handleToolError()?")

Called if a Tool run encounters an error

> `Optional` **handleToolError**(`err`: `any`, `runId`: `string`, `parentRunId`?: `string`, `tags`?: `string`\[\]): `void` | `Promise`<`void`\>

#### Parameters[​](#parameters-16 "Direct link to Parameters")

Parameter

Type

`err`

`any`

`runId`

`string`

`parentRunId?`

`string`

`tags?`

`string`\[\]

#### Returns[​](#returns-23 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Inherited from[​](#inherited-from-15 "Direct link to Inherited from")

BaseCallbackHandlerMethodsClass.handleToolError

#### Defined in[​](#defined-in-35 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:147](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L147)

### handleToolStart()?[​](#handletoolstart "Direct link to handleToolStart()?")

Called at the start of a Tool run, with the tool name and input and the run ID.

> `Optional` **handleToolStart**(`tool`: [`Serialized`](/docs/api/load_serializable/types/Serialized), `input`: `string`, `runId`: `string`, `parentRunId`?: `string`, `tags`?: `string`\[\], `metadata`?: `Record`<`string`, `unknown`\>): `void` | `Promise`<`void`\>

#### Parameters[​](#parameters-17 "Direct link to Parameters")

Parameter

Type

`tool`

[`Serialized`](/docs/api/load_serializable/types/Serialized)

`input`

`string`

`runId`

`string`

`parentRunId?`

`string`

`tags?`

`string`\[\]

`metadata?`

`Record`<`string`, `unknown`\>

#### Returns[​](#returns-24 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Inherited from[​](#inherited-from-16 "Direct link to Inherited from")

BaseCallbackHandlerMethodsClass.handleToolStart

#### Defined in[​](#defined-in-36 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:135](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L135)

### fromMethods()[​](#frommethods "Direct link to fromMethods()")

> `Static` **fromMethods**(`methods`: `BaseCallbackHandlerMethodsClass`): `Handler`

#### Parameters[​](#parameters-18 "Direct link to Parameters")

Parameter

Type

`methods`

`BaseCallbackHandlerMethodsClass`

#### Returns[​](#returns-25 "Direct link to Returns")

`Handler`

#### Defined in[​](#defined-in-37 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:293](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/base.ts#L293)