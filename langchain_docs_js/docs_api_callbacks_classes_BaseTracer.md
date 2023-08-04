BaseTracer
==========

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseCallbackHandler`](/docs/api/callbacks/classes/BaseCallbackHandler).**BaseTracer**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new BaseTracer**(`_fields`?: [`BaseCallbackHandlerInput`](/docs/api/callbacks/interfaces/BaseCallbackHandlerInput)): [`BaseTracer`](/docs/api/callbacks/classes/BaseTracer)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`_fields?`

[`BaseCallbackHandlerInput`](/docs/api/callbacks/interfaces/BaseCallbackHandlerInput)

#### Returns[](#returns "Direct link to Returns")

[`BaseTracer`](/docs/api/callbacks/classes/BaseTracer)

#### Overrides[](#overrides "Direct link to Overrides")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[constructor](/docs/api/callbacks/classes/BaseCallbackHandler#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:42](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L42)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### awaitHandlers[](#awaithandlers "Direct link to awaitHandlers")

> **awaitHandlers**: `boolean`

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[awaitHandlers](/docs/api/callbacks/classes/BaseCallbackHandler#awaithandlers)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:263](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/base.ts#L263)

### ignoreAgent[](#ignoreagent "Direct link to ignoreAgent")

> **ignoreAgent**: `boolean` = `false`

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[ignoreAgent](/docs/api/callbacks/classes/BaseCallbackHandler#ignoreagent)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:259](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/base.ts#L259)

### ignoreChain[](#ignorechain "Direct link to ignoreChain")

> **ignoreChain**: `boolean` = `false`

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[ignoreChain](/docs/api/callbacks/classes/BaseCallbackHandler#ignorechain)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:257](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/base.ts#L257)

### ignoreLLM[](#ignorellm "Direct link to ignoreLLM")

> **ignoreLLM**: `boolean` = `false`

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[ignoreLLM](/docs/api/callbacks/classes/BaseCallbackHandler#ignorellm)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:255](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/base.ts#L255)

### ignoreRetriever[](#ignoreretriever "Direct link to ignoreRetriever")

> **ignoreRetriever**: `boolean` = `false`

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[ignoreRetriever](/docs/api/callbacks/classes/BaseCallbackHandler#ignoreretriever)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:261](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/base.ts#L261)

### lc\_kwargs[](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[lc\_kwargs](/docs/api/callbacks/classes/BaseCallbackHandler#lc_kwargs)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:251](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/base.ts#L251)

### lc\_serializable[](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[lc\_serializable](/docs/api/callbacks/classes/BaseCallbackHandler#lc_serializable)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:233](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/base.ts#L233)

### name[](#name "Direct link to name")

> `Abstract` **name**: `string`

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[name](/docs/api/callbacks/classes/BaseCallbackHandler#name)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:253](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/base.ts#L253)

### runMap[](#runmap "Direct link to runMap")

> `Protected` **runMap**: `Map`<`string`, [`Run`](/docs/api/callbacks/interfaces/Run)\>

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:40](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L40)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[](#returns-1 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

BaseCallbackHandler.lc\_aliases

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:247](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/base.ts#L247)

#### Inherited from[](#inherited-from-9 "Direct link to Inherited from")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[lc\_aliases](/docs/api/callbacks/classes/BaseCallbackHandler#lc_aliases)

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:247](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/base.ts#L247)

### lc\_attributes[](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[](#returns-2 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-10 "Direct link to Inherited from")

BaseCallbackHandler.lc\_attributes

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:243](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/base.ts#L243)

#### Inherited from[](#inherited-from-11 "Direct link to Inherited from")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[lc\_attributes](/docs/api/callbacks/classes/BaseCallbackHandler#lc_attributes)

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:243](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/base.ts#L243)

### lc\_namespace[](#lc_namespace "Direct link to lc_namespace")

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

> **lc\_namespace**(): \["langchain", "callbacks", `string`\]

#### Returns[](#returns-3 "Direct link to Returns")

\["langchain", "callbacks", `string`\]

#### Inherited from[](#inherited-from-12 "Direct link to Inherited from")

BaseCallbackHandler.lc\_namespace

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:235](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/base.ts#L235)

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[](#inherited-from-13 "Direct link to Inherited from")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[lc\_namespace](/docs/api/callbacks/classes/BaseCallbackHandler#lc_namespace)

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:235](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/base.ts#L235)

### lc\_secrets[](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[](#returns-4 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-14 "Direct link to Inherited from")

BaseCallbackHandler.lc\_secrets

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:239](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/base.ts#L239)

#### Inherited from[](#inherited-from-15 "Direct link to Inherited from")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[lc\_secrets](/docs/api/callbacks/classes/BaseCallbackHandler#lc_secrets)

#### Defined in[](#defined-in-17 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:239](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/base.ts#L239)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### copy()[](#copy "Direct link to copy()")

> **copy**(): [`BaseTracer`](/docs/api/callbacks/classes/BaseTracer)

#### Returns[](#returns-5 "Direct link to Returns")

[`BaseTracer`](/docs/api/callbacks/classes/BaseTracer)

#### Overrides[](#overrides-1 "Direct link to Overrides")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[copy](/docs/api/callbacks/classes/BaseCallbackHandler#copy)

#### Defined in[](#defined-in-18 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:46](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L46)

### handleAgentAction()[](#handleagentaction "Direct link to handleAgentAction()")

Called when an agent is about to execute an action, with the action and the run ID.

> **handleAgentAction**(`action`: [`AgentAction`](/docs/api/schema/types/AgentAction), `runId`: `string`): `Promise`<`void`\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`action`

[`AgentAction`](/docs/api/schema/types/AgentAction)

`runId`

`string`

#### Returns[](#returns-6 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[](#overrides-2 "Direct link to Overrides")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[handleAgentAction](/docs/api/callbacks/classes/BaseCallbackHandler#handleagentaction)

#### Defined in[](#defined-in-19 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:329](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L329)

### handleAgentEnd()[](#handleagentend "Direct link to handleAgentEnd()")

Called when an agent finishes execution, before it exits. with the final output and the run ID.

> **handleAgentEnd**(`action`: [`AgentFinish`](/docs/api/schema/types/AgentFinish), `runId`: `string`): `Promise`<`void`\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`action`

[`AgentFinish`](/docs/api/schema/types/AgentFinish)

`runId`

`string`

#### Returns[](#returns-7 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[](#overrides-3 "Direct link to Overrides")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[handleAgentEnd](/docs/api/callbacks/classes/BaseCallbackHandler#handleagentend)

#### Defined in[](#defined-in-20 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:345](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L345)

### handleChainEnd()[](#handlechainend "Direct link to handleChainEnd()")

Called at the end of a Chain run, with the outputs and the run ID.

> **handleChainEnd**(`outputs`: [`ChainValues`](/docs/api/schema/types/ChainValues), `runId`: `string`): `Promise`<`void`\>

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

`outputs`

[`ChainValues`](/docs/api/schema/types/ChainValues)

`runId`

`string`

#### Returns[](#returns-8 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[](#overrides-4 "Direct link to Overrides")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[handleChainEnd](/docs/api/callbacks/classes/BaseCallbackHandler#handlechainend)

#### Defined in[](#defined-in-21 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:234](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L234)

### handleChainError()[](#handlechainerror "Direct link to handleChainError()")

Called if a Chain run encounters an error

> **handleChainError**(`error`: `Error`, `runId`: `string`): `Promise`<`void`\>

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

`error`

`Error`

`runId`

`string`

#### Returns[](#returns-9 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[](#overrides-5 "Direct link to Overrides")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[handleChainError](/docs/api/callbacks/classes/BaseCallbackHandler#handlechainerror)

#### Defined in[](#defined-in-22 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:249](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L249)

### handleChainStart()[](#handlechainstart "Direct link to handleChainStart()")

Called at the start of a Chain run, with the chain name and inputs and the run ID.

> **handleChainStart**(`chain`: [`Serialized`](/docs/api/load_serializable/types/Serialized), `inputs`: [`ChainValues`](/docs/api/schema/types/ChainValues), `runId`: `string`, `parentRunId`?: `string`, `tags`?: `string`\[\], `metadata`?: `KVMap`, `runType`?: `string`): `Promise`<`void`\>

#### Parameters[](#parameters-5 "Direct link to Parameters")

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

`KVMap`

`runType?`

`string`

#### Returns[](#returns-10 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[](#overrides-6 "Direct link to Overrides")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[handleChainStart](/docs/api/callbacks/classes/BaseCallbackHandler#handlechainstart)

#### Defined in[](#defined-in-23 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:198](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L198)

### handleChatModelStart()[](#handlechatmodelstart "Direct link to handleChatModelStart()")

Called at the start of a Chat Model run, with the prompt(s) and the run ID.

> **handleChatModelStart**(`llm`: [`Serialized`](/docs/api/load_serializable/types/Serialized), `messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]\[\], `runId`: `string`, `parentRunId`?: `string`, `extraParams`?: `KVMap`, `tags`?: `string`\[\], `metadata`?: `KVMap`): `Promise`<`void`\>

#### Parameters[](#parameters-6 "Direct link to Parameters")

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

`KVMap`

`tags?`

`string`\[\]

`metadata?`

`KVMap`

#### Returns[](#returns-11 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[](#overrides-7 "Direct link to Overrides")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[handleChatModelStart](/docs/api/callbacks/classes/BaseCallbackHandler#handlechatmodelstart)

#### Defined in[](#defined-in-24 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:129](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L129)

### handleLLMEnd()[](#handlellmend "Direct link to handleLLMEnd()")

Called at the end of an LLM/ChatModel run, with the output and the run ID.

> **handleLLMEnd**(`output`: [`LLMResult`](/docs/api/schema/types/LLMResult), `runId`: `string`): `Promise`<`void`\>

#### Parameters[](#parameters-7 "Direct link to Parameters")

Parameter

Type

`output`

[`LLMResult`](/docs/api/schema/types/LLMResult)

`runId`

`string`

#### Returns[](#returns-12 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[](#overrides-8 "Direct link to Overrides")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[handleLLMEnd](/docs/api/callbacks/classes/BaseCallbackHandler#handlellmend)

#### Defined in[](#defined-in-25 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:168](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L168)

### handleLLMError()[](#handlellmerror "Direct link to handleLLMError()")

Called if an LLM/ChatModel run encounters an error

> **handleLLMError**(`error`: `Error`, `runId`: `string`): `Promise`<`void`\>

#### Parameters[](#parameters-8 "Direct link to Parameters")

Parameter

Type

`error`

`Error`

`runId`

`string`

#### Returns[](#returns-13 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[](#overrides-9 "Direct link to Overrides")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[handleLLMError](/docs/api/callbacks/classes/BaseCallbackHandler#handlellmerror)

#### Defined in[](#defined-in-26 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:183](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L183)

### handleLLMNewToken()[](#handlellmnewtoken "Direct link to handleLLMNewToken()")

Called when an LLM/ChatModel in `streaming` mode produces a new token

> **handleLLMNewToken**(`token`: `string`, `idx`: [`NewTokenIndices`](/docs/api/callbacks/interfaces/NewTokenIndices), `runId`: `string`): `Promise`<`void`\>

#### Parameters[](#parameters-9 "Direct link to Parameters")

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

#### Returns[](#returns-14 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[](#overrides-10 "Direct link to Overrides")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[handleLLMNewToken](/docs/api/callbacks/classes/BaseCallbackHandler#handlellmnewtoken)

#### Defined in[](#defined-in-27 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:439](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L439)

### handleLLMStart()[](#handlellmstart "Direct link to handleLLMStart()")

Called at the start of an LLM or Chat Model run, with the prompt(s) and the run ID.

> **handleLLMStart**(`llm`: [`Serialized`](/docs/api/load_serializable/types/Serialized), `prompts`: `string`\[\], `runId`: `string`, `parentRunId`?: `string`, `extraParams`?: `KVMap`, `tags`?: `string`\[\], `metadata`?: `KVMap`): `Promise`<`void`\>

#### Parameters[](#parameters-10 "Direct link to Parameters")

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

`KVMap`

`tags?`

`string`\[\]

`metadata?`

`KVMap`

#### Returns[](#returns-15 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[](#overrides-11 "Direct link to Overrides")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[handleLLMStart](/docs/api/callbacks/classes/BaseCallbackHandler#handlellmstart)

#### Defined in[](#defined-in-28 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L90)

### handleRetrieverEnd()[](#handleretrieverend "Direct link to handleRetrieverEnd()")

> **handleRetrieverEnd**(`documents`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `unknown`\>\>\[\], `runId`: `string`): `Promise`<`void`\>

#### Parameters[](#parameters-11 "Direct link to Parameters")

Parameter

Type

`documents`

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `unknown`\>\>\[\]

`runId`

`string`

#### Returns[](#returns-16 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[](#overrides-12 "Direct link to Overrides")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[handleRetrieverEnd](/docs/api/callbacks/classes/BaseCallbackHandler#handleretrieverend)

#### Defined in[](#defined-in-29 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:393](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L393)

### handleRetrieverError()[](#handleretrievererror "Direct link to handleRetrieverError()")

> **handleRetrieverError**(`error`: `Error`, `runId`: `string`): `Promise`<`void`\>

#### Parameters[](#parameters-12 "Direct link to Parameters")

Parameter

Type

`error`

`Error`

`runId`

`string`

#### Returns[](#returns-17 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[](#overrides-13 "Direct link to Overrides")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[handleRetrieverError](/docs/api/callbacks/classes/BaseCallbackHandler#handleretrievererror)

#### Defined in[](#defined-in-30 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:411](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L411)

### handleRetrieverStart()[](#handleretrieverstart "Direct link to handleRetrieverStart()")

> **handleRetrieverStart**(`retriever`: [`Serialized`](/docs/api/load_serializable/types/Serialized), `query`: `string`, `runId`: `string`, `parentRunId`?: `string`, `tags`?: `string`\[\], `metadata`?: `KVMap`): `Promise`<`void`\>

#### Parameters[](#parameters-13 "Direct link to Parameters")

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

`KVMap`

#### Returns[](#returns-18 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[](#overrides-14 "Direct link to Overrides")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[handleRetrieverStart](/docs/api/callbacks/classes/BaseCallbackHandler#handleretrieverstart)

#### Defined in[](#defined-in-31 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:358](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L358)

### handleText()[](#handletext "Direct link to handleText()")

> **handleText**(`text`: `string`, `runId`: `string`): `Promise`<`void`\>

#### Parameters[](#parameters-14 "Direct link to Parameters")

Parameter

Type

`text`

`string`

`runId`

`string`

#### Returns[](#returns-19 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[](#overrides-15 "Direct link to Overrides")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[handleText](/docs/api/callbacks/classes/BaseCallbackHandler#handletext)

#### Defined in[](#defined-in-32 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:426](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L426)

### handleToolEnd()[](#handletoolend "Direct link to handleToolEnd()")

Called at the end of a Tool run, with the tool output and the run ID.

> **handleToolEnd**(`output`: `string`, `runId`: `string`): `Promise`<`void`\>

#### Parameters[](#parameters-15 "Direct link to Parameters")

Parameter

Type

`output`

`string`

`runId`

`string`

#### Returns[](#returns-20 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[](#overrides-16 "Direct link to Overrides")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[handleToolEnd](/docs/api/callbacks/classes/BaseCallbackHandler#handletoolend)

#### Defined in[](#defined-in-33 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:299](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L299)

### handleToolError()[](#handletoolerror "Direct link to handleToolError()")

Called if a Tool run encounters an error

> **handleToolError**(`error`: `Error`, `runId`: `string`): `Promise`<`void`\>

#### Parameters[](#parameters-16 "Direct link to Parameters")

Parameter

Type

`error`

`Error`

`runId`

`string`

#### Returns[](#returns-21 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[](#overrides-17 "Direct link to Overrides")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[handleToolError](/docs/api/callbacks/classes/BaseCallbackHandler#handletoolerror)

#### Defined in[](#defined-in-34 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:314](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L314)

### handleToolStart()[](#handletoolstart "Direct link to handleToolStart()")

Called at the start of a Tool run, with the tool name and input and the run ID.

> **handleToolStart**(`tool`: [`Serialized`](/docs/api/load_serializable/types/Serialized), `input`: `string`, `runId`: `string`, `parentRunId`?: `string`, `tags`?: `string`\[\], `metadata`?: `KVMap`): `Promise`<`void`\>

#### Parameters[](#parameters-17 "Direct link to Parameters")

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

`KVMap`

#### Returns[](#returns-22 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[](#overrides-18 "Direct link to Overrides")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[handleToolStart](/docs/api/callbacks/classes/BaseCallbackHandler#handletoolstart)

#### Defined in[](#defined-in-35 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:264](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L264)

### toJSON()[](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[](#returns-23 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[](#inherited-from-16 "Direct link to Inherited from")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[toJSON](/docs/api/callbacks/classes/BaseCallbackHandler#tojson)

#### Defined in[](#defined-in-36 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:286](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/base.ts#L286)

### toJSONNotImplemented()[](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[](#returns-24 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[](#inherited-from-17 "Direct link to Inherited from")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[toJSONNotImplemented](/docs/api/callbacks/classes/BaseCallbackHandler#tojsonnotimplemented)

#### Defined in[](#defined-in-37 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:290](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/base.ts#L290)

### onAgentAction()?[](#onagentaction "Direct link to onAgentAction()?")

> `Optional` **onAgentAction**(`run`: [`Run`](/docs/api/callbacks/interfaces/Run)): `void` | `Promise`<`void`\>

#### Parameters[](#parameters-18 "Direct link to Parameters")

Parameter

Type

`run`

[`Run`](/docs/api/callbacks/interfaces/Run)

#### Returns[](#returns-25 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Defined in[](#defined-in-38 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:476](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L476)

### onAgentEnd()?[](#onagentend "Direct link to onAgentEnd()?")

> `Optional` **onAgentEnd**(`run`: [`Run`](/docs/api/callbacks/interfaces/Run)): `void` | `Promise`<`void`\>

#### Parameters[](#parameters-19 "Direct link to Parameters")

Parameter

Type

`run`

[`Run`](/docs/api/callbacks/interfaces/Run)

#### Returns[](#returns-26 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Defined in[](#defined-in-39 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:478](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L478)

### onChainEnd()?[](#onchainend "Direct link to onChainEnd()?")

> `Optional` **onChainEnd**(`run`: [`Run`](/docs/api/callbacks/interfaces/Run)): `void` | `Promise`<`void`\>

#### Parameters[](#parameters-20 "Direct link to Parameters")

Parameter

Type

`run`

[`Run`](/docs/api/callbacks/interfaces/Run)

#### Returns[](#returns-27 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Defined in[](#defined-in-40 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:466](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L466)

### onChainError()?[](#onchainerror "Direct link to onChainError()?")

> `Optional` **onChainError**(`run`: [`Run`](/docs/api/callbacks/interfaces/Run)): `void` | `Promise`<`void`\>

#### Parameters[](#parameters-21 "Direct link to Parameters")

Parameter

Type

`run`

[`Run`](/docs/api/callbacks/interfaces/Run)

#### Returns[](#returns-28 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Defined in[](#defined-in-41 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:468](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L468)

### onChainStart()?[](#onchainstart "Direct link to onChainStart()?")

> `Optional` **onChainStart**(`run`: [`Run`](/docs/api/callbacks/interfaces/Run)): `void` | `Promise`<`void`\>

#### Parameters[](#parameters-22 "Direct link to Parameters")

Parameter

Type

`run`

[`Run`](/docs/api/callbacks/interfaces/Run)

#### Returns[](#returns-29 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Defined in[](#defined-in-42 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:464](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L464)

### onLLMEnd()?[](#onllmend "Direct link to onLLMEnd()?")

> `Optional` **onLLMEnd**(`run`: [`Run`](/docs/api/callbacks/interfaces/Run)): `void` | `Promise`<`void`\>

#### Parameters[](#parameters-23 "Direct link to Parameters")

Parameter

Type

`run`

[`Run`](/docs/api/callbacks/interfaces/Run)

#### Returns[](#returns-30 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Defined in[](#defined-in-43 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:460](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L460)

### onLLMError()?[](#onllmerror "Direct link to onLLMError()?")

> `Optional` **onLLMError**(`run`: [`Run`](/docs/api/callbacks/interfaces/Run)): `void` | `Promise`<`void`\>

#### Parameters[](#parameters-24 "Direct link to Parameters")

Parameter

Type

`run`

[`Run`](/docs/api/callbacks/interfaces/Run)

#### Returns[](#returns-31 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Defined in[](#defined-in-44 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:462](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L462)

### onLLMNewToken()?[](#onllmnewtoken "Direct link to onLLMNewToken()?")

> `Optional` **onLLMNewToken**(`run`: [`Run`](/docs/api/callbacks/interfaces/Run)): `void` | `Promise`<`void`\>

#### Parameters[](#parameters-25 "Direct link to Parameters")

Parameter

Type

`run`

[`Run`](/docs/api/callbacks/interfaces/Run)

#### Returns[](#returns-32 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Defined in[](#defined-in-45 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:488](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L488)

### onLLMStart()?[](#onllmstart "Direct link to onLLMStart()?")

> `Optional` **onLLMStart**(`run`: [`Run`](/docs/api/callbacks/interfaces/Run)): `void` | `Promise`<`void`\>

#### Parameters[](#parameters-26 "Direct link to Parameters")

Parameter

Type

`run`

[`Run`](/docs/api/callbacks/interfaces/Run)

#### Returns[](#returns-33 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Defined in[](#defined-in-46 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:458](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L458)

### onRetrieverEnd()?[](#onretrieverend "Direct link to onRetrieverEnd()?")

> `Optional` **onRetrieverEnd**(`run`: [`Run`](/docs/api/callbacks/interfaces/Run)): `void` | `Promise`<`void`\>

#### Parameters[](#parameters-27 "Direct link to Parameters")

Parameter

Type

`run`

[`Run`](/docs/api/callbacks/interfaces/Run)

#### Returns[](#returns-34 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Defined in[](#defined-in-47 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:482](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L482)

### onRetrieverError()?[](#onretrievererror "Direct link to onRetrieverError()?")

> `Optional` **onRetrieverError**(`run`: [`Run`](/docs/api/callbacks/interfaces/Run)): `void` | `Promise`<`void`\>

#### Parameters[](#parameters-28 "Direct link to Parameters")

Parameter

Type

`run`

[`Run`](/docs/api/callbacks/interfaces/Run)

#### Returns[](#returns-35 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Defined in[](#defined-in-48 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:484](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L484)

### onRetrieverStart()?[](#onretrieverstart "Direct link to onRetrieverStart()?")

> `Optional` **onRetrieverStart**(`run`: [`Run`](/docs/api/callbacks/interfaces/Run)): `void` | `Promise`<`void`\>

#### Parameters[](#parameters-29 "Direct link to Parameters")

Parameter

Type

`run`

[`Run`](/docs/api/callbacks/interfaces/Run)

#### Returns[](#returns-36 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Defined in[](#defined-in-49 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:480](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L480)

### onText()?[](#ontext "Direct link to onText()?")

> `Optional` **onText**(`run`: [`Run`](/docs/api/callbacks/interfaces/Run)): `void` | `Promise`<`void`\>

#### Parameters[](#parameters-30 "Direct link to Parameters")

Parameter

Type

`run`

[`Run`](/docs/api/callbacks/interfaces/Run)

#### Returns[](#returns-37 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Defined in[](#defined-in-50 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:486](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L486)

### onToolEnd()?[](#ontoolend "Direct link to onToolEnd()?")

> `Optional` **onToolEnd**(`run`: [`Run`](/docs/api/callbacks/interfaces/Run)): `void` | `Promise`<`void`\>

#### Parameters[](#parameters-31 "Direct link to Parameters")

Parameter

Type

`run`

[`Run`](/docs/api/callbacks/interfaces/Run)

#### Returns[](#returns-38 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Defined in[](#defined-in-51 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:472](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L472)

### onToolError()?[](#ontoolerror "Direct link to onToolError()?")

> `Optional` **onToolError**(`run`: [`Run`](/docs/api/callbacks/interfaces/Run)): `void` | `Promise`<`void`\>

#### Parameters[](#parameters-32 "Direct link to Parameters")

Parameter

Type

`run`

[`Run`](/docs/api/callbacks/interfaces/Run)

#### Returns[](#returns-39 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Defined in[](#defined-in-52 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:474](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L474)

### onToolStart()?[](#ontoolstart "Direct link to onToolStart()?")

> `Optional` **onToolStart**(`run`: [`Run`](/docs/api/callbacks/interfaces/Run)): `void` | `Promise`<`void`\>

#### Parameters[](#parameters-33 "Direct link to Parameters")

Parameter

Type

`run`

[`Run`](/docs/api/callbacks/interfaces/Run)

#### Returns[](#returns-40 "Direct link to Returns")

`void` | `Promise`<`void`\>

#### Defined in[](#defined-in-53 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:470](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L470)

### fromMethods()[](#frommethods "Direct link to fromMethods()")

> `Static` **fromMethods**(`methods`: `BaseCallbackHandlerMethodsClass`): `Handler`

#### Parameters[](#parameters-34 "Direct link to Parameters")

Parameter

Type

`methods`

`BaseCallbackHandlerMethodsClass`

#### Returns[](#returns-41 "Direct link to Returns")

`Handler`

#### Inherited from[](#inherited-from-18 "Direct link to Inherited from")

[BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler).[fromMethods](/docs/api/callbacks/classes/BaseCallbackHandler#frommethods)

#### Defined in[](#defined-in-54 "Direct link to Defined in")

[langchain/src/callbacks/base.ts:294](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/base.ts#L294)

### \_addChildRun()[](#_addchildrun "Direct link to _addchildrun")

> `Protected` **\_addChildRun**(`parentRun`: [`Run`](/docs/api/callbacks/interfaces/Run), `childRun`: [`Run`](/docs/api/callbacks/interfaces/Run)): `void`

#### Parameters[](#parameters-35 "Direct link to Parameters")

Parameter

Type

`parentRun`

[`Run`](/docs/api/callbacks/interfaces/Run)

`childRun`

[`Run`](/docs/api/callbacks/interfaces/Run)

#### Returns[](#returns-42 "Direct link to Returns")

`void`

#### Defined in[](#defined-in-55 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:52](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L52)

### \_endTrace()[](#_endtrace "Direct link to _endtrace")

> `Protected` **\_endTrace**(`run`: [`Run`](/docs/api/callbacks/interfaces/Run)): `Promise`<`void`\>

#### Parameters[](#parameters-36 "Direct link to Parameters")

Parameter

Type

`run`

[`Run`](/docs/api/callbacks/interfaces/Run)

#### Returns[](#returns-43 "Direct link to Returns")

`Promise`<`void`\>

#### Defined in[](#defined-in-56 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:66](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L66)

### \_getExecutionOrder()[](#_getexecutionorder "Direct link to _getexecutionorder")

> `Protected` **\_getExecutionOrder**(`parentRunId`: `undefined` | `string`): `number`

#### Parameters[](#parameters-37 "Direct link to Parameters")

Parameter

Type

`parentRunId`

`undefined` | `string`

#### Returns[](#returns-44 "Direct link to Returns")

`number`

#### Defined in[](#defined-in-57 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L80)

### \_startTrace()[](#_starttrace "Direct link to _starttrace")

> `Protected` **\_startTrace**(`run`: [`Run`](/docs/api/callbacks/interfaces/Run)): `void`

#### Parameters[](#parameters-38 "Direct link to Parameters")

Parameter

Type

`run`

[`Run`](/docs/api/callbacks/interfaces/Run)

#### Returns[](#returns-45 "Direct link to Returns")

`void`

#### Defined in[](#defined-in-58 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:56](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L56)

### persistRun()[](#persistrun "Direct link to persistRun()")

> `Protected` `Abstract` **persistRun**(`run`: [`Run`](/docs/api/callbacks/interfaces/Run)): `Promise`<`void`\>

#### Parameters[](#parameters-39 "Direct link to Parameters")

Parameter

Type

`run`

[`Run`](/docs/api/callbacks/interfaces/Run)

#### Returns[](#returns-46 "Direct link to Returns")

`Promise`<`void`\>

#### Defined in[](#defined-in-59 "Direct link to Defined in")

[langchain/src/callbacks/handlers/tracer.ts:50](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/handlers/tracer.ts#L50)