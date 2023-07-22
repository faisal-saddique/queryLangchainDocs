ChatMessageHistory
==================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseListChatMessageHistory`](/docs/api/schema/classes/BaseListChatMessageHistory).**ChatMessageHistory**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new ChatMessageHistory**(`messages`?: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]): [`ChatMessageHistory`](/docs/api/stores_message_in_memory/classes/ChatMessageHistory)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`messages?`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]

#### Returns[​](#returns "Direct link to Returns")

[`ChatMessageHistory`](/docs/api/stores_message_in_memory/classes/ChatMessageHistory)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseListChatMessageHistory](/docs/api/schema/classes/BaseListChatMessageHistory).[constructor](/docs/api/schema/classes/BaseListChatMessageHistory#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/stores/message/in\_memory.ts:8](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/stores/message/in_memory.ts#L8)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BaseListChatMessageHistory](/docs/api/schema/classes/BaseListChatMessageHistory).[lc\_kwargs](/docs/api/schema/classes/BaseListChatMessageHistory#lc_kwargs)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[BaseListChatMessageHistory](/docs/api/schema/classes/BaseListChatMessageHistory).[lc\_namespace](/docs/api/schema/classes/BaseListChatMessageHistory#lc_namespace)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/stores/message/in\_memory.ts:4](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/stores/message/in_memory.ts#L4)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[BaseListChatMessageHistory](/docs/api/schema/classes/BaseListChatMessageHistory).[lc\_serializable](/docs/api/schema/classes/BaseListChatMessageHistory#lc_serializable)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L55)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-1 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

BaseListChatMessageHistory.lc\_aliases

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[BaseListChatMessageHistory](/docs/api/schema/classes/BaseListChatMessageHistory).[lc\_aliases](/docs/api/schema/classes/BaseListChatMessageHistory#lc_aliases)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

BaseListChatMessageHistory.lc\_attributes

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[BaseListChatMessageHistory](/docs/api/schema/classes/BaseListChatMessageHistory).[lc\_attributes](/docs/api/schema/classes/BaseListChatMessageHistory#lc_attributes)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

BaseListChatMessageHistory.lc\_secrets

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

[BaseListChatMessageHistory](/docs/api/schema/classes/BaseListChatMessageHistory).[lc\_secrets](/docs/api/schema/classes/BaseListChatMessageHistory#lc_secrets)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### addAIChatMessage()[​](#addaichatmessage "Direct link to addAIChatMessage()")

> **addAIChatMessage**(`message`: `string`): `Promise`<`void`\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`message`

`string`

#### Returns[​](#returns-4 "Direct link to Returns")

`Promise`<`void`\>

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[BaseListChatMessageHistory](/docs/api/schema/classes/BaseListChatMessageHistory).[addAIChatMessage](/docs/api/schema/classes/BaseListChatMessageHistory#addaichatmessage)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/schema/index.ts:279](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/index.ts#L279)

### addMessage()[​](#addmessage "Direct link to addMessage()")

> **addMessage**(`message`: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)): `Promise`<`void`\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`message`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)

#### Returns[​](#returns-5 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[BaseListChatMessageHistory](/docs/api/schema/classes/BaseListChatMessageHistory).[addMessage](/docs/api/schema/classes/BaseListChatMessageHistory#addmessage)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/stores/message/in\_memory.ts:17](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/stores/message/in_memory.ts#L17)

### addUserMessage()[​](#addusermessage "Direct link to addUserMessage()")

> **addUserMessage**(`message`: `string`): `Promise`<`void`\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`message`

`string`

#### Returns[​](#returns-6 "Direct link to Returns")

`Promise`<`void`\>

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

[BaseListChatMessageHistory](/docs/api/schema/classes/BaseListChatMessageHistory).[addUserMessage](/docs/api/schema/classes/BaseListChatMessageHistory#addusermessage)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/schema/index.ts:275](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/index.ts#L275)

### clear()[​](#clear "Direct link to clear()")

> **clear**(): `Promise`<`void`\>

#### Returns[​](#returns-7 "Direct link to Returns")

`Promise`<`void`\>

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/stores/message/in\_memory.ts:21](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/stores/message/in_memory.ts#L21)

### getMessages()[​](#getmessages "Direct link to getMessages()")

> **getMessages**(): `Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]\>

#### Returns[​](#returns-8 "Direct link to Returns")

`Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]\>

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/stores/message/in\_memory.ts:13](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/stores/message/in_memory.ts#L13)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-9 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

[BaseListChatMessageHistory](/docs/api/schema/classes/BaseListChatMessageHistory).[toJSON](/docs/api/schema/classes/BaseListChatMessageHistory#tojson)

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-10 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

[BaseListChatMessageHistory](/docs/api/schema/classes/BaseListChatMessageHistory).[toJSONNotImplemented](/docs/api/schema/classes/BaseListChatMessageHistory#tojsonnotimplemented)

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)