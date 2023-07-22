CallbackManagerForChainRun
==========================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   `BaseRunManager`.**CallbackManagerForChainRun**

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   `BaseCallbackManagerMethods`

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new CallbackManagerForChainRun**(`runId`: `string`, `handlers`: [`BaseCallbackHandler`](/docs/api/callbacks/classes/BaseCallbackHandler)\[\], `inheritableHandlers`: [`BaseCallbackHandler`](/docs/api/callbacks/classes/BaseCallbackHandler)\[\], `tags`: `string`\[\], `inheritableTags`: `string`\[\], `metadata`: `Record`<`string`, `unknown`\>, `inheritableMetadata`: `Record`<`string`, `unknown`\>, `_parentRunId`?: `string`): [`CallbackManagerForChainRun`](/docs/api/callbacks/classes/CallbackManagerForChainRun)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`runId`

`string`

`handlers`

[`BaseCallbackHandler`](/docs/api/callbacks/classes/BaseCallbackHandler)\[\]

`inheritableHandlers`

[`BaseCallbackHandler`](/docs/api/callbacks/classes/BaseCallbackHandler)\[\]

`tags`

`string`\[\]

`inheritableTags`

`string`\[\]

`metadata`

`Record`<`string`, `unknown`\>

`inheritableMetadata`

`Record`<`string`, `unknown`\>

`_parentRunId?`

`string`

#### Returns[​](#returns "Direct link to Returns")

[`CallbackManagerForChainRun`](/docs/api/callbacks/classes/CallbackManagerForChainRun)

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

BaseRunManager.constructor

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:89](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/manager.ts#L89)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### runId[​](#runid "Direct link to runId")

> `Readonly` **runId**: `string`

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

BaseRunManager.runId

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/manager.ts#L90)

### handlers[​](#handlers "Direct link to handlers")

> `Protected` `Readonly` **handlers**: [`BaseCallbackHandler`](/docs/api/callbacks/classes/BaseCallbackHandler)\[\]

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

BaseRunManager.handlers

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:91](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/manager.ts#L91)

### inheritableHandlers[​](#inheritablehandlers "Direct link to inheritableHandlers")

> `Protected` `Readonly` **inheritableHandlers**: [`BaseCallbackHandler`](/docs/api/callbacks/classes/BaseCallbackHandler)\[\]

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

BaseRunManager.inheritableHandlers

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:92](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/manager.ts#L92)

### inheritableMetadata[​](#inheritablemetadata "Direct link to inheritableMetadata")

> `Protected` `Readonly` **inheritableMetadata**: `Record`<`string`, `unknown`\>

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

BaseRunManager.inheritableMetadata

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:96](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/manager.ts#L96)

### inheritableTags[​](#inheritabletags "Direct link to inheritableTags")

> `Protected` `Readonly` **inheritableTags**: `string`\[\]

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

BaseRunManager.inheritableTags

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:94](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/manager.ts#L94)

### metadata[​](#metadata "Direct link to metadata")

> `Protected` `Readonly` **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

BaseRunManager.metadata

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:95](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/manager.ts#L95)

### tags[​](#tags "Direct link to tags")

> `Protected` `Readonly` **tags**: `string`\[\]

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

BaseRunManager.tags

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:93](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/manager.ts#L93)

### \_parentRunId?[​](#_parentrunid "Direct link to _parentrunid")

> **\_parentRunId**: `string`

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

BaseRunManager.\_parentRunId

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:97](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/manager.ts#L97)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### getChild()[​](#getchild "Direct link to getChild()")

> **getChild**(`tag`?: `string`): [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`tag?`

`string`

#### Returns[​](#returns-1 "Direct link to Returns")

[`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:267](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/manager.ts#L267)

### handleAgentAction()[​](#handleagentaction "Direct link to handleAgentAction()")

> **handleAgentAction**(`action`: [`AgentAction`](/docs/api/schema/types/AgentAction)): `Promise`<`void`\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`action`

[`AgentAction`](/docs/api/schema/types/AgentAction)

#### Returns[​](#returns-2 "Direct link to Returns")

`Promise`<`void`\>

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

BaseCallbackManagerMethods.handleAgentAction

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:325](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/manager.ts#L325)

### handleAgentEnd()[​](#handleagentend "Direct link to handleAgentEnd()")

> **handleAgentEnd**(`action`: [`AgentFinish`](/docs/api/schema/types/AgentFinish)): `Promise`<`void`\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`action`

[`AgentFinish`](/docs/api/schema/types/AgentFinish)

#### Returns[​](#returns-3 "Direct link to Returns")

`Promise`<`void`\>

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

BaseCallbackManagerMethods.handleAgentEnd

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:348](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/manager.ts#L348)

### handleChainEnd()[​](#handlechainend "Direct link to handleChainEnd()")

> **handleChainEnd**(`output`: [`ChainValues`](/docs/api/schema/types/ChainValues)): `Promise`<`void`\>

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`output`

[`ChainValues`](/docs/api/schema/types/ChainValues)

#### Returns[​](#returns-4 "Direct link to Returns")

`Promise`<`void`\>

#### Implementation of[​](#implementation-of-2 "Direct link to Implementation of")

BaseCallbackManagerMethods.handleChainEnd

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:302](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/manager.ts#L302)

### handleChainError()[​](#handlechainerror "Direct link to handleChainError()")

> **handleChainError**(`err`: `unknown`): `Promise`<`void`\>

#### Parameters[​](#parameters-5 "Direct link to Parameters")

Parameter

Type

`err`

`unknown`

#### Returns[​](#returns-5 "Direct link to Returns")

`Promise`<`void`\>

#### Implementation of[​](#implementation-of-3 "Direct link to Implementation of")

BaseCallbackManagerMethods.handleChainError

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:279](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/manager.ts#L279)

### handleText()[​](#handletext "Direct link to handleText()")

> **handleText**(`text`: `string`): `Promise`<`void`\>

#### Parameters[​](#parameters-6 "Direct link to Parameters")

Parameter

Type

`text`

`string`

#### Returns[​](#returns-6 "Direct link to Returns")

`Promise`<`void`\>

#### Implementation of[​](#implementation-of-4 "Direct link to Implementation of")

BaseCallbackManagerMethods.handleText

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

BaseRunManager.handleText

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:100](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/callbacks/manager.ts#L100)