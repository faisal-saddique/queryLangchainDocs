AIMessage
=========

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseMessage`](/docs/api/schema/classes/BaseMessage).**AIMessage**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new AIMessage**(`fields`: `string` | [`BaseMessageFields`](/docs/api/schema/interfaces/BaseMessageFields), `kwargs`?: `Record`<`string`, `unknown`\>): [`AIMessage`](/docs/api/schema/classes/AIMessage)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

Description

`fields`

`string` | [`BaseMessageFields`](/docs/api/schema/interfaces/BaseMessageFields)

\-

`kwargs?`

`Record`<`string`, `unknown`\>

`Deprecated`  
  

#### Returns[](#returns "Direct link to Returns")

[`AIMessage`](/docs/api/schema/classes/AIMessage)

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BaseMessage](/docs/api/schema/classes/BaseMessage).[constructor](/docs/api/schema/classes/BaseMessage#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/schema/index.ts:140](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/index.ts#L140)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### additional\_kwargs[](#additional_kwargs "Direct link to additional_kwargs")

> **additional\_kwargs**: `object`

Additional keyword arguments

#### Index signature[](#index-signature "Direct link to Index signature")

\[`key`: `string`\]: `unknown`

#### Type declaration[](#type-declaration "Direct link to Type declaration")

Member

Type

`function_call`?

`ChatCompletionRequestMessageFunctionCall`

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[BaseMessage](/docs/api/schema/classes/BaseMessage).[additional\_kwargs](/docs/api/schema/classes/BaseMessage#additional_kwargs)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/schema/index.ts:135](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/index.ts#L135)

### content[](#content "Direct link to content")

> **content**: `string`

The text of the message.

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[BaseMessage](/docs/api/schema/classes/BaseMessage).[content](/docs/api/schema/classes/BaseMessage#content)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/schema/index.ts:129](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/index.ts#L129)

### lc\_kwargs[](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[BaseMessage](/docs/api/schema/classes/BaseMessage).[lc\_kwargs](/docs/api/schema/classes/BaseMessage#lc_kwargs)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L57)

### lc\_namespace[](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[BaseMessage](/docs/api/schema/classes/BaseMessage).[lc\_namespace](/docs/api/schema/classes/BaseMessage#lc_namespace)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/schema/index.ts:116](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/index.ts#L116)

### lc\_serializable[](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `true`

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[BaseMessage](/docs/api/schema/classes/BaseMessage).[lc\_serializable](/docs/api/schema/classes/BaseMessage#lc_serializable)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/schema/index.ts:118](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/index.ts#L118)

### name?[](#name "Direct link to name?")

> **name**: `string`

The name of the message sender in a multi-user chat.

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[BaseMessage](/docs/api/schema/classes/BaseMessage).[name](/docs/api/schema/classes/BaseMessage#name)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/schema/index.ts:132](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/index.ts#L132)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[](#returns-1 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

BaseMessage.lc\_aliases

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

[BaseMessage](/docs/api/schema/classes/BaseMessage).[lc\_aliases](/docs/api/schema/classes/BaseMessage#lc_aliases)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

### lc\_attributes[](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[](#returns-2 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[](#inherited-from-9 "Direct link to Inherited from")

BaseMessage.lc\_attributes

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L80)

#### Inherited from[](#inherited-from-10 "Direct link to Inherited from")

[BaseMessage](/docs/api/schema/classes/BaseMessage).[lc\_attributes](/docs/api/schema/classes/BaseMessage#lc_attributes)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L80)

### lc\_secrets[](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-11 "Direct link to Inherited from")

BaseMessage.lc\_secrets

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

#### Inherited from[](#inherited-from-12 "Direct link to Inherited from")

[BaseMessage](/docs/api/schema/classes/BaseMessage).[lc\_secrets](/docs/api/schema/classes/BaseMessage#lc_secrets)

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

### text[](#text "Direct link to text")

#### Deprecated[](#deprecated "Direct link to Deprecated")

Use [content](/docs/api/schema/classes/BaseMessage#content) instead.

> **text**(): `string`

#### Returns[](#returns-4 "Direct link to Returns")

`string`

#### Inherited from[](#inherited-from-13 "Direct link to Inherited from")

BaseMessage.text

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/schema/index.ts:124](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/index.ts#L124)

#### Inherited from[](#inherited-from-14 "Direct link to Inherited from")

[BaseMessage](/docs/api/schema/classes/BaseMessage).[text](/docs/api/schema/classes/BaseMessage#text)

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/schema/index.ts:124](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/index.ts#L124)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### \_getType()[](#_gettype "Direct link to _gettype")

The type of the message.

> **\_getType**(): [`MessageType`](/docs/api/schema/types/MessageType)

#### Returns[](#returns-5 "Direct link to Returns")

[`MessageType`](/docs/api/schema/types/MessageType)

#### Overrides[](#overrides "Direct link to Overrides")

[BaseMessage](/docs/api/schema/classes/BaseMessage).[\_getType](/docs/api/schema/classes/BaseMessage#_gettype)

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/schema/index.ts:227](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/index.ts#L227)

### toDict()[](#todict "Direct link to toDict()")

> **toDict**(): [`StoredMessage`](/docs/api/schema/interfaces/StoredMessage)

#### Returns[](#returns-6 "Direct link to Returns")

[`StoredMessage`](/docs/api/schema/interfaces/StoredMessage)

#### Inherited from[](#inherited-from-15 "Direct link to Inherited from")

[BaseMessage](/docs/api/schema/classes/BaseMessage).[toDict](/docs/api/schema/classes/BaseMessage#todict)

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/schema/index.ts:160](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/index.ts#L160)

### toJSON()[](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[](#returns-7 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[](#inherited-from-16 "Direct link to Inherited from")

[BaseMessage](/docs/api/schema/classes/BaseMessage).[toJSON](/docs/api/schema/classes/BaseMessage#tojson)

#### Defined in[](#defined-in-17 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[](#returns-8 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[](#inherited-from-17 "Direct link to Inherited from")

[BaseMessage](/docs/api/schema/classes/BaseMessage).[toJSONNotImplemented](/docs/api/schema/classes/BaseMessage#tojsonnotimplemented)

#### Defined in[](#defined-in-18 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L151)