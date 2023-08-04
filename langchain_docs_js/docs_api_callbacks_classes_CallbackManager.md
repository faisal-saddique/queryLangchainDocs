CallbackManager
===============

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   `BaseCallbackManager`.**CallbackManager**

Implements[](#implements "Direct link to Implements")
------------------------------------------------------

*   `BaseCallbackManagerMethods`

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new CallbackManager**(`parentRunId`?: `string`): [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`parentRunId?`

`string`

#### Returns[](#returns "Direct link to Returns")

[`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Overrides[](#overrides "Direct link to Overrides")

BaseCallbackManager.constructor

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:455](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L455)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### handlers[](#handlers "Direct link to handlers")

> **handlers**: [`BaseCallbackHandler`](/docs/api/callbacks/classes/BaseCallbackHandler)\[\]

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:439](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L439)

### inheritableHandlers[](#inheritablehandlers "Direct link to inheritableHandlers")

> **inheritableHandlers**: [`BaseCallbackHandler`](/docs/api/callbacks/classes/BaseCallbackHandler)\[\]

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:441](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L441)

### inheritableMetadata[](#inheritablemetadata "Direct link to inheritableMetadata")

> **inheritableMetadata**: `Record`<`string`, `unknown`\> = `{}`

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:449](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L449)

### inheritableTags[](#inheritabletags "Direct link to inheritableTags")

> **inheritableTags**: `string`\[\] = `[]`

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:445](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L445)

### metadata[](#metadata "Direct link to metadata")

> **metadata**: `Record`<`string`, `unknown`\> = `{}`

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:447](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L447)

### name[](#name "Direct link to name")

> **name**: `string` = `"callback_manager"`

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:451](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L451)

### tags[](#tags "Direct link to tags")

> **tags**: `string`\[\] = `[]`

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:443](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L443)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### addHandler()[](#addhandler "Direct link to addHandler()")

> **addHandler**(`handler`: [`BaseCallbackHandler`](/docs/api/callbacks/classes/BaseCallbackHandler), `inherit`: `boolean` = `true`): `void`

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

Default value

`handler`

[`BaseCallbackHandler`](/docs/api/callbacks/classes/BaseCallbackHandler)

`undefined`

`inherit`

`boolean`

`true`

#### Returns[](#returns-1 "Direct link to Returns")

`void`

#### Overrides[](#overrides-1 "Direct link to Overrides")

BaseCallbackManager.addHandler

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:693](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L693)

### addMetadata()[](#addmetadata "Direct link to addMetadata()")

> **addMetadata**(`metadata`: `Record`<`string`, `unknown`\>, `inherit`: `boolean` = `true`): `void`

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

Default value

`metadata`

`Record`<`string`, `unknown`\>

`undefined`

`inherit`

`boolean`

`true`

#### Returns[](#returns-2 "Direct link to Returns")

`void`

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:730](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L730)

### addTags()[](#addtags "Direct link to addTags()")

> **addTags**(`tags`: `string`\[\], `inherit`: `boolean` = `true`): `void`

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

Default value

`tags`

`string`\[\]

`undefined`

`inherit`

`boolean`

`true`

#### Returns[](#returns-3 "Direct link to Returns")

`void`

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:715](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L715)

### copy()[](#copy "Direct link to copy()")

> **copy**(`additionalHandlers`: [`BaseCallbackHandler`](/docs/api/callbacks/classes/BaseCallbackHandler)\[\] = `[]`, `inherit`: `boolean` = `true`): [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

Default value

`additionalHandlers`

[`BaseCallbackHandler`](/docs/api/callbacks/classes/BaseCallbackHandler)\[\]

`[]`

`inherit`

`boolean`

`true`

#### Returns[](#returns-4 "Direct link to Returns")

[`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:744](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L744)

### handleChainStart()[](#handlechainstart "Direct link to handleChainStart()")

> **handleChainStart**(`chain`: [`Serialized`](/docs/api/load_serializable/types/Serialized), `inputs`: [`ChainValues`](/docs/api/schema/types/ChainValues), `runId`: `string` = `...`, `runType`: `undefined` | `string` = `undefined`): `Promise`<[`CallbackManagerForChainRun`](/docs/api/callbacks/classes/CallbackManagerForChainRun)\>

#### Parameters[](#parameters-5 "Direct link to Parameters")

Parameter

Type

Default value

`chain`

[`Serialized`](/docs/api/load_serializable/types/Serialized)

`undefined`

`inputs`

[`ChainValues`](/docs/api/schema/types/ChainValues)

`undefined`

`runId`

`string`

`undefined`

`runType`

`undefined` | `string`

`undefined`

#### Returns[](#returns-5 "Direct link to Returns")

`Promise`<[`CallbackManagerForChainRun`](/docs/api/callbacks/classes/CallbackManagerForChainRun)\>

#### Implementation of[](#implementation-of "Direct link to Implementation of")

BaseCallbackManagerMethods.handleChainStart

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:573](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L573)

### handleChatModelStart()[](#handlechatmodelstart "Direct link to handleChatModelStart()")

> **handleChatModelStart**(`llm`: [`Serialized`](/docs/api/load_serializable/types/Serialized), `messages`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]\[\], `_runId`: `undefined` | `string` = `undefined`, `_parentRunId`: `undefined` | `string` = `undefined`, `extraParams`: `undefined` | `Record`<`string`, `unknown`\> = `undefined`): `Promise`<[`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)\[\]\>

#### Parameters[](#parameters-6 "Direct link to Parameters")

Parameter

Type

Default value

`llm`

[`Serialized`](/docs/api/load_serializable/types/Serialized)

`undefined`

`messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]\[\]

`undefined`

`_runId`

`undefined` | `string`

`undefined`

`_parentRunId`

`undefined` | `string`

`undefined`

`extraParams`

`undefined` | `Record`<`string`, `unknown`\>

`undefined`

#### Returns[](#returns-6 "Direct link to Returns")

`Promise`<[`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)\[\]\>

#### Implementation of[](#implementation-of-1 "Direct link to Implementation of")

BaseCallbackManagerMethods.handleChatModelStart

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:511](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L511)

### handleLLMStart()[](#handlellmstart "Direct link to handleLLMStart()")

> **handleLLMStart**(`llm`: [`Serialized`](/docs/api/load_serializable/types/Serialized), `prompts`: `string`\[\], `_runId`: `undefined` | `string` = `undefined`, `_parentRunId`: `undefined` | `string` = `undefined`, `extraParams`: `undefined` | `Record`<`string`, `unknown`\> = `undefined`): `Promise`<[`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)\[\]\>

#### Parameters[](#parameters-7 "Direct link to Parameters")

Parameter

Type

Default value

`llm`

[`Serialized`](/docs/api/load_serializable/types/Serialized)

`undefined`

`prompts`

`string`\[\]

`undefined`

`_runId`

`undefined` | `string`

`undefined`

`_parentRunId`

`undefined` | `string`

`undefined`

`extraParams`

`undefined` | `Record`<`string`, `unknown`\>

`undefined`

#### Returns[](#returns-7 "Direct link to Returns")

`Promise`<[`CallbackManagerForLLMRun`](/docs/api/callbacks/classes/CallbackManagerForLLMRun)\[\]\>

#### Implementation of[](#implementation-of-2 "Direct link to Implementation of")

BaseCallbackManagerMethods.handleLLMStart

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:462](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L462)

### handleRetrieverStart()[](#handleretrieverstart "Direct link to handleRetrieverStart()")

> **handleRetrieverStart**(`retriever`: [`Serialized`](/docs/api/load_serializable/types/Serialized), `query`: `string`, `runId`: `string` = `...`, `_parentRunId`: `undefined` | `string` = `undefined`): `Promise`<`CallbackManagerForRetrieverRun`\>

#### Parameters[](#parameters-8 "Direct link to Parameters")

Parameter

Type

Default value

`retriever`

[`Serialized`](/docs/api/load_serializable/types/Serialized)

`undefined`

`query`

`string`

`undefined`

`runId`

`string`

`undefined`

`_parentRunId`

`undefined` | `string`

`undefined`

#### Returns[](#returns-8 "Direct link to Returns")

`Promise`<`CallbackManagerForRetrieverRun`\>

#### Implementation of[](#implementation-of-3 "Direct link to Implementation of")

BaseCallbackManagerMethods.handleRetrieverStart

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:653](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L653)

### handleToolStart()[](#handletoolstart "Direct link to handleToolStart()")

> **handleToolStart**(`tool`: [`Serialized`](/docs/api/load_serializable/types/Serialized), `input`: `string`, `runId`: `string` = `...`): `Promise`<[`CallbackManagerForToolRun`](/docs/api/callbacks/classes/CallbackManagerForToolRun)\>

#### Parameters[](#parameters-9 "Direct link to Parameters")

Parameter

Type

`tool`

[`Serialized`](/docs/api/load_serializable/types/Serialized)

`input`

`string`

`runId`

`string`

#### Returns[](#returns-9 "Direct link to Returns")

`Promise`<[`CallbackManagerForToolRun`](/docs/api/callbacks/classes/CallbackManagerForToolRun)\>

#### Implementation of[](#implementation-of-4 "Direct link to Implementation of")

BaseCallbackManagerMethods.handleToolStart

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:614](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L614)

### removeHandler()[](#removehandler "Direct link to removeHandler()")

> **removeHandler**(`handler`: [`BaseCallbackHandler`](/docs/api/callbacks/classes/BaseCallbackHandler)): `void`

#### Parameters[](#parameters-10 "Direct link to Parameters")

Parameter

Type

`handler`

[`BaseCallbackHandler`](/docs/api/callbacks/classes/BaseCallbackHandler)

#### Returns[](#returns-10 "Direct link to Returns")

`void`

#### Overrides[](#overrides-2 "Direct link to Overrides")

BaseCallbackManager.removeHandler

#### Defined in[](#defined-in-17 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:700](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L700)

### removeMetadata()[](#removemetadata "Direct link to removeMetadata()")

> **removeMetadata**(`metadata`: `Record`<`string`, `unknown`\>): `void`

#### Parameters[](#parameters-11 "Direct link to Parameters")

Parameter

Type

`metadata`

`Record`<`string`, `unknown`\>

#### Returns[](#returns-11 "Direct link to Returns")

`void`

#### Defined in[](#defined-in-18 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:737](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L737)

### removeTags()[](#removetags "Direct link to removeTags()")

> **removeTags**(`tags`: `string`\[\]): `void`

#### Parameters[](#parameters-12 "Direct link to Parameters")

Parameter

Type

`tags`

`string`\[\]

#### Returns[](#returns-12 "Direct link to Returns")

`void`

#### Defined in[](#defined-in-19 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:723](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L723)

### setHandler()[](#sethandler "Direct link to setHandler()")

> **setHandler**(`handler`: [`BaseCallbackHandler`](/docs/api/callbacks/classes/BaseCallbackHandler)): `void`

#### Parameters[](#parameters-13 "Direct link to Parameters")

Parameter

Type

`handler`

[`BaseCallbackHandler`](/docs/api/callbacks/classes/BaseCallbackHandler)

#### Returns[](#returns-13 "Direct link to Returns")

`void`

#### Inherited from[](#inherited-from "Direct link to Inherited from")

BaseCallbackManager.setHandler

#### Defined in[](#defined-in-20 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:83](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L83)

### setHandlers()[](#sethandlers "Direct link to setHandlers()")

> **setHandlers**(`handlers`: [`BaseCallbackHandler`](/docs/api/callbacks/classes/BaseCallbackHandler)\[\], `inherit`: `boolean` = `true`): `void`

#### Parameters[](#parameters-14 "Direct link to Parameters")

Parameter

Type

Default value

`handlers`

[`BaseCallbackHandler`](/docs/api/callbacks/classes/BaseCallbackHandler)\[\]

`undefined`

`inherit`

`boolean`

`true`

#### Returns[](#returns-14 "Direct link to Returns")

`void`

#### Overrides[](#overrides-3 "Direct link to Overrides")

BaseCallbackManager.setHandlers

#### Defined in[](#defined-in-21 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:707](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L707)

### configure()[](#configure "Direct link to configure()")

> `Static` **configure**(`inheritableHandlers`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks), `localHandlers`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks), `inheritableTags`?: `string`\[\], `localTags`?: `string`\[\], `inheritableMetadata`?: `Record`<`string`, `unknown`\>, `localMetadata`?: `Record`<`string`, `unknown`\>, `options`?: [`CallbackManagerOptions`](/docs/api/callbacks/interfaces/CallbackManagerOptions)): `Promise`<`undefined` | [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)\>

#### Parameters[](#parameters-15 "Direct link to Parameters")

Parameter

Type

`inheritableHandlers?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

`localHandlers?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

`inheritableTags?`

`string`\[\]

`localTags?`

`string`\[\]

`inheritableMetadata?`

`Record`<`string`, `unknown`\>

`localMetadata?`

`Record`<`string`, `unknown`\>

`options?`

[`CallbackManagerOptions`](/docs/api/callbacks/interfaces/CallbackManagerOptions)

#### Returns[](#returns-15 "Direct link to Returns")

`Promise`<`undefined` | [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)\>

#### Defined in[](#defined-in-22 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:790](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L790)

### fromHandlers()[](#fromhandlers "Direct link to fromHandlers()")

> `Static` **fromHandlers**(`handlers`: `BaseCallbackHandlerMethodsClass`): [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Parameters[](#parameters-16 "Direct link to Parameters")

Parameter

Type

`handlers`

`BaseCallbackHandlerMethodsClass`

#### Returns[](#returns-16 "Direct link to Returns")

[`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Defined in[](#defined-in-23 "Direct link to Defined in")

[langchain/src/callbacks/manager.ts:775](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/callbacks/manager.ts#L775)