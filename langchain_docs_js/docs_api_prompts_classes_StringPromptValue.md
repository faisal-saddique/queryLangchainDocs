StringPromptValue
=================

Base PromptValue class. All prompt values should extend this class.

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue).**StringPromptValue**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new StringPromptValue**(`value`: `string`): [`StringPromptValue`](/docs/api/prompts/classes/StringPromptValue)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`value`

`string`

#### Returns[](#returns "Direct link to Returns")

[`StringPromptValue`](/docs/api/prompts/classes/StringPromptValue)

#### Overrides[](#overrides "Direct link to Overrides")

[BasePromptValue](/docs/api/schema/classes/BasePromptValue).[constructor](/docs/api/schema/classes/BasePromptValue#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/prompts/base.ts:20](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/base.ts#L20)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### lc\_kwargs[](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BasePromptValue](/docs/api/schema/classes/BasePromptValue).[lc\_kwargs](/docs/api/schema/classes/BasePromptValue#lc_kwargs)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L57)

### lc\_namespace[](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Overrides[](#overrides-1 "Direct link to Overrides")

[BasePromptValue](/docs/api/schema/classes/BasePromptValue).[lc\_namespace](/docs/api/schema/classes/BasePromptValue#lc_namespace)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/prompts/base.ts:16](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/base.ts#L16)

### lc\_serializable[](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[BasePromptValue](/docs/api/schema/classes/BasePromptValue).[lc\_serializable](/docs/api/schema/classes/BasePromptValue#lc_serializable)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L55)

### value[](#value "Direct link to value")

> **value**: `string`

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/prompts/base.ts:18](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/base.ts#L18)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[](#returns-1 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

BasePromptValue.lc\_aliases

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[BasePromptValue](/docs/api/schema/classes/BasePromptValue).[lc\_aliases](/docs/api/schema/classes/BasePromptValue#lc_aliases)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

### lc\_attributes[](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[](#returns-2 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

BasePromptValue.lc\_attributes

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L80)

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[BasePromptValue](/docs/api/schema/classes/BasePromptValue).[lc\_attributes](/docs/api/schema/classes/BasePromptValue#lc_attributes)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L80)

### lc\_secrets[](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

BasePromptValue.lc\_secrets

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

[BasePromptValue](/docs/api/schema/classes/BasePromptValue).[lc\_secrets](/docs/api/schema/classes/BasePromptValue#lc_secrets)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### toChatMessages()[](#tochatmessages "Direct link to toChatMessages()")

> **toChatMessages**(): [`HumanMessage`](/docs/api/schema/classes/HumanMessage)\[\]

#### Returns[](#returns-4 "Direct link to Returns")

[`HumanMessage`](/docs/api/schema/classes/HumanMessage)\[\]

#### Overrides[](#overrides-2 "Direct link to Overrides")

[BasePromptValue](/docs/api/schema/classes/BasePromptValue).[toChatMessages](/docs/api/schema/classes/BasePromptValue#tochatmessages)

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/prompts/base.ts:29](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/base.ts#L29)

### toJSON()[](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[](#returns-5 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

[BasePromptValue](/docs/api/schema/classes/BasePromptValue).[toJSON](/docs/api/schema/classes/BasePromptValue#tojson)

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[](#returns-6 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[](#inherited-from-9 "Direct link to Inherited from")

[BasePromptValue](/docs/api/schema/classes/BasePromptValue).[toJSONNotImplemented](/docs/api/schema/classes/BasePromptValue#tojsonnotimplemented)

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L151)

### toString()[](#tostring "Direct link to toString()")

> **toString**(): `string`

#### Returns[](#returns-7 "Direct link to Returns")

`string`

#### Overrides[](#overrides-3 "Direct link to Overrides")

[BasePromptValue](/docs/api/schema/classes/BasePromptValue).[toString](/docs/api/schema/classes/BasePromptValue#tostring)

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/prompts/base.ts:25](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/base.ts#L25)