HumanMessagePromptTemplate
==========================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   `BaseMessageStringPromptTemplate`.**HumanMessagePromptTemplate**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new HumanMessagePromptTemplate**(`prompt`: [`BaseStringPromptTemplate`](/docs/api/prompts/classes/BaseStringPromptTemplate)): [`HumanMessagePromptTemplate`](/docs/api/prompts/classes/HumanMessagePromptTemplate)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`prompt`

[`BaseStringPromptTemplate`](/docs/api/prompts/classes/BaseStringPromptTemplate)

#### Returns[](#returns "Direct link to Returns")

[`HumanMessagePromptTemplate`](/docs/api/prompts/classes/HumanMessagePromptTemplate)

#### Inherited from[](#inherited-from "Direct link to Inherited from")

BaseMessageStringPromptTemplate.constructor

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/prompts/chat.ts:99](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/chat.ts#L99)

> **new HumanMessagePromptTemplate**(`fields`: `MessageStringPromptTemplateFields`): [`HumanMessagePromptTemplate`](/docs/api/prompts/classes/HumanMessagePromptTemplate)

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`fields`

`MessageStringPromptTemplateFields`

#### Returns[](#returns-1 "Direct link to Returns")

[`HumanMessagePromptTemplate`](/docs/api/prompts/classes/HumanMessagePromptTemplate)

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

BaseMessageStringPromptTemplate.constructor

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/prompts/chat.ts:101](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/chat.ts#L101)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### lc\_kwargs[](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

BaseMessageStringPromptTemplate.lc\_kwargs

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L57)

### lc\_namespace[](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

BaseMessageStringPromptTemplate.lc\_namespace

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/prompts/chat.ts:20](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/chat.ts#L20)

### lc\_serializable[](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `true`

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

BaseMessageStringPromptTemplate.lc\_serializable

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/prompts/chat.ts:22](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/chat.ts#L22)

### prompt[](#prompt "Direct link to prompt")

> **prompt**: [`BaseStringPromptTemplate`](/docs/api/prompts/classes/BaseStringPromptTemplate)

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

BaseMessageStringPromptTemplate.prompt

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/prompts/chat.ts:97](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/chat.ts#L97)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### inputVariables[](#inputvariables "Direct link to inputVariables")

> **inputVariables**(): `string`\[\]

#### Returns[](#returns-2 "Direct link to Returns")

`string`\[\]

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

BaseMessageStringPromptTemplate.inputVariables

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/prompts/chat.ts:114](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/chat.ts#L114)

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

BaseMessageStringPromptTemplate.inputVariables

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/prompts/chat.ts:114](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/chat.ts#L114)

### lc\_aliases[](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

BaseMessageStringPromptTemplate.lc\_aliases

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

#### Inherited from[](#inherited-from-9 "Direct link to Inherited from")

BaseMessageStringPromptTemplate.lc\_aliases

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

### lc\_attributes[](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[](#returns-4 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[](#inherited-from-10 "Direct link to Inherited from")

BaseMessageStringPromptTemplate.lc\_attributes

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L80)

#### Inherited from[](#inherited-from-11 "Direct link to Inherited from")

BaseMessageStringPromptTemplate.lc\_attributes

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L80)

### lc\_secrets[](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[](#returns-5 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-12 "Direct link to Inherited from")

BaseMessageStringPromptTemplate.lc\_secrets

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

#### Inherited from[](#inherited-from-13 "Direct link to Inherited from")

BaseMessageStringPromptTemplate.lc\_secrets

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### format()[](#format "Direct link to format()")

> **format**(`values`: [`InputValues`](/docs/api/schema/types/InputValues)): `Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`values`

[`InputValues`](/docs/api/schema/types/InputValues)

#### Returns[](#returns-6 "Direct link to Returns")

`Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\>

#### Overrides[](#overrides "Direct link to Overrides")

BaseMessageStringPromptTemplate.format

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/prompts/chat.ts:176](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/chat.ts#L176)

### formatMessages()[](#formatmessages "Direct link to formatMessages()")

> **formatMessages**(`values`: [`InputValues`](/docs/api/schema/types/InputValues)): `Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]\>

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

`values`

[`InputValues`](/docs/api/schema/types/InputValues)

#### Returns[](#returns-7 "Direct link to Returns")

`Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]\>

#### Inherited from[](#inherited-from-14 "Direct link to Inherited from")

BaseMessageStringPromptTemplate.formatMessages

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/prompts/chat.ts:120](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/chat.ts#L120)

### toJSON()[](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[](#returns-8 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[](#inherited-from-15 "Direct link to Inherited from")

BaseMessageStringPromptTemplate.toJSON

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[](#returns-9 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[](#inherited-from-16 "Direct link to Inherited from")

BaseMessageStringPromptTemplate.toJSONNotImplemented

#### Defined in[](#defined-in-17 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L151)

### fromTemplate()[](#fromtemplate "Direct link to fromTemplate()")

> `Static` **fromTemplate**(`template`: `string`): [`HumanMessagePromptTemplate`](/docs/api/prompts/classes/HumanMessagePromptTemplate)

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

`template`

`string`

#### Returns[](#returns-10 "Direct link to Returns")

[`HumanMessagePromptTemplate`](/docs/api/prompts/classes/HumanMessagePromptTemplate)

#### Defined in[](#defined-in-18 "Direct link to Defined in")

[langchain/src/prompts/chat.ts:180](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/chat.ts#L180)