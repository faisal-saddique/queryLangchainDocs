CallbackManagerForToolRun
=========================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   `BaseRunManager`.**CallbackManagerForToolRun**

Implements[](#implements "Direct link to Implements")
------------------------------------------------------

*   `BaseCallbackManagerMethods`

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new CallbackManagerForToolRun**(`runId`: `string`, `handlers`: [`BaseCallbackHandler`](/docs/api/callbacks/classes/BaseCallbackHandler)\[\], `inheritableHandlers`: [`BaseCallbackHandler`](/docs/api/callbacks/classes/BaseCallbackHandler)\[\], `tags`: `string`\[\], `inheritableTags`: `string`\[\], `metadata`: `Record`<`string`, `unknown`\>, `inheritableMetadata`: `Record`<`string`, `unknown`\>, `_parentRunId`?: `string`): [`CallbackManagerForToolRun`](/docs/api/callbacks/classes/CallbackManagerForToolRun)

#### Parameters[](#parameters "Direct link to Parameters")

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

#### Returns[](#returns "Direct link to Returns")

[`CallbackManagerForToolRun`](/docs/api/callbacks/classes/CallbackManagerForToolRun)

#### Inherited from[](#inherited-from "Direct link to Inherited from")

BaseRunManager.constructor

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:89](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L89)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### runId[](#runid "Direct link to runId")

> `Readonly` **runId**: `string`

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

BaseRunManager.runId

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L90)

### handlers[](#handlers "Direct link to handlers")

> `Protected` `Readonly` **handlers**: [`BaseCallbackHandler`](/docs/api/callbacks/classes/BaseCallbackHandler)\[\]

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

BaseRunManager.handlers

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:91](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L91)

### inheritableHandlers[](#inheritablehandlers "Direct link to inheritableHandlers")

> `Protected` `Readonly` **inheritableHandlers**: [`BaseCallbackHandler`](/docs/api/callbacks/classes/BaseCallbackHandler)\[\]

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

BaseRunManager.inheritableHandlers

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:92](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L92)

### inheritableMetadata[](#inheritablemetadata "Direct link to inheritableMetadata")

> `Protected` `Readonly` **inheritableMetadata**: `Record`<`string`, `unknown`\>

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

BaseRunManager.inheritableMetadata

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:96](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L96)

### inheritableTags[](#inheritabletags "Direct link to inheritableTags")

> `Protected` `Readonly` **inheritableTags**: `string`\[\]

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

BaseRunManager.inheritableTags

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:94](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L94)

### metadata[](#metadata "Direct link to metadata")

> `Protected` `Readonly` **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

BaseRunManager.metadata

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:95](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L95)

### tags[](#tags "Direct link to tags")

> `Protected` `Readonly` **tags**: `string`\[\]

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

BaseRunManager.tags

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:93](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L93)

### \_parentRunId?[](#_parentrunid "Direct link to _parentrunid")

> **\_parentRunId**: `string`

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

BaseRunManager.\_parentRunId

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:97](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L97)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### getChild()[](#getchild "Direct link to getChild()")

> **getChild**(`tag`?: `string`): [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`tag?`

`string`

#### Returns[](#returns-1 "Direct link to Returns")

[`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:376](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L376)

### handleText()[](#handletext "Direct link to handleText()")

> **handleText**(`text`: `string`): `Promise`<`void`\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`text`

`string`

#### Returns[](#returns-2 "Direct link to Returns")

`Promise`<`void`\>

#### Implementation of[](#implementation-of "Direct link to Implementation of")

BaseCallbackManagerMethods.handleText

#### Inherited from[](#inherited-from-9 "Direct link to Inherited from")

BaseRunManager.handleText

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:100](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L100)

### handleToolEnd()[](#handletoolend "Direct link to handleToolEnd()")

> **handleToolEnd**(`output`: `string`): `Promise`<`void`\>

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

`output`

`string`

#### Returns[](#returns-3 "Direct link to Returns")

`Promise`<`void`\>

#### Implementation of[](#implementation-of-1 "Direct link to Implementation of")

BaseCallbackManagerMethods.handleToolEnd

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:411](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L411)

### handleToolError()[](#handletoolerror "Direct link to handleToolError()")

> **handleToolError**(`err`: `unknown`): `Promise`<`void`\>

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

`err`

`unknown`

#### Returns[](#returns-4 "Direct link to Returns")

`Promise`<`void`\>

#### Implementation of[](#implementation-of-2 "Direct link to Implementation of")

BaseCallbackManagerMethods.handleToolError

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:388](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L388)