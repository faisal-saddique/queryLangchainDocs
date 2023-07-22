PlanOutputParser
================

Class to parse the output of an LLM call.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseOutputParser`](/docs/api/schema_output_parser/classes/BaseOutputParser)<[`Plan`](/docs/api/experimental_plan_and_execute/types/Plan)\>.**PlanOutputParser**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new PlanOutputParser**(`kwargs`?: `SerializedFields`, ...`_args`?: `never`\[\]): [`PlanOutputParser`](/docs/api/experimental_plan_and_execute/classes/PlanOutputParser)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`kwargs?`

`SerializedFields`

`..._args?`

`never`\[\]

#### Returns[​](#returns "Direct link to Returns")

[`PlanOutputParser`](/docs/api/experimental_plan_and_execute/classes/PlanOutputParser)

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BaseOutputParser](/docs/api/schema_output_parser/classes/BaseOutputParser).[constructor](/docs/api/schema_output_parser/classes/BaseOutputParser#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/load/serializable.ts:94](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L94)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[BaseOutputParser](/docs/api/schema_output_parser/classes/BaseOutputParser).[lc\_kwargs](/docs/api/schema_output_parser/classes/BaseOutputParser#lc_kwargs)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseOutputParser](/docs/api/schema_output_parser/classes/BaseOutputParser).[lc\_namespace](/docs/api/schema_output_parser/classes/BaseOutputParser#lc_namespace)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/experimental/plan\_and\_execute/outputParser.ts:7](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/plan_and_execute/outputParser.ts#L7)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[BaseOutputParser](/docs/api/schema_output_parser/classes/BaseOutputParser).[lc\_serializable](/docs/api/schema_output_parser/classes/BaseOutputParser#lc_serializable)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L55)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-1 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

BaseOutputParser.lc\_aliases

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[BaseOutputParser](/docs/api/schema_output_parser/classes/BaseOutputParser).[lc\_aliases](/docs/api/schema_output_parser/classes/BaseOutputParser#lc_aliases)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

BaseOutputParser.lc\_attributes

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[BaseOutputParser](/docs/api/schema_output_parser/classes/BaseOutputParser).[lc\_attributes](/docs/api/schema_output_parser/classes/BaseOutputParser#lc_attributes)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

BaseOutputParser.lc\_secrets

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[BaseOutputParser](/docs/api/schema_output_parser/classes/BaseOutputParser).[lc\_secrets](/docs/api/schema_output_parser/classes/BaseOutputParser#lc_secrets)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### \_type()[​](#_type "Direct link to _type")

Return the string type key uniquely identifying this class of parser

> **\_type**(): `string`

#### Returns[​](#returns-4 "Direct link to Returns")

`string`

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

[BaseOutputParser](/docs/api/schema_output_parser/classes/BaseOutputParser).[\_type](/docs/api/schema_output_parser/classes/BaseOutputParser#_type)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/schema/output\_parser.ts:69](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/output_parser.ts#L69)

### getFormatInstructions()[​](#getformatinstructions "Direct link to getFormatInstructions()")

Return a string describing the format of the output.

#### Example[​](#example "Direct link to Example")

    {  "foo": "bar"}

> **getFormatInstructions**(): `string`

#### Returns[​](#returns-5 "Direct link to Returns")

`string`

Format instructions.

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[BaseOutputParser](/docs/api/schema_output_parser/classes/BaseOutputParser).[getFormatInstructions](/docs/api/schema_output_parser/classes/BaseOutputParser#getformatinstructions)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/experimental/plan\_and\_execute/outputParser.ts:18](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/plan_and_execute/outputParser.ts#L18)

### parse()[​](#parse "Direct link to parse()")

Parse the output of an LLM call.

> **parse**(`text`: `string`): `Promise`<[`Plan`](/docs/api/experimental_plan_and_execute/types/Plan)\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

Description

`text`

`string`

LLM output to parse.

#### Returns[​](#returns-6 "Direct link to Returns")

`Promise`<[`Plan`](/docs/api/experimental_plan_and_execute/types/Plan)\>

Parsed output.

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[BaseOutputParser](/docs/api/schema_output_parser/classes/BaseOutputParser).[parse](/docs/api/schema_output_parser/classes/BaseOutputParser#parse)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/experimental/plan\_and\_execute/outputParser.ts:9](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/plan_and_execute/outputParser.ts#L9)

### parseResult()[​](#parseresult "Direct link to parseResult()")

> **parseResult**(`generations`: [`Generation`](/docs/api/schema/interfaces/Generation)\[\] | [`ChatGeneration`](/docs/api/schema/interfaces/ChatGeneration)\[\], `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`Plan`](/docs/api/experimental_plan_and_execute/types/Plan)\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`generations`

[`Generation`](/docs/api/schema/interfaces/Generation)\[\] | [`ChatGeneration`](/docs/api/schema/interfaces/ChatGeneration)\[\]

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-7 "Direct link to Returns")

`Promise`<[`Plan`](/docs/api/experimental_plan_and_execute/types/Plan)\>

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

[BaseOutputParser](/docs/api/schema_output_parser/classes/BaseOutputParser).[parseResult](/docs/api/schema_output_parser/classes/BaseOutputParser#parseresult)

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/schema/output\_parser.ts:30](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/output_parser.ts#L30)

### parseResultWithPrompt()[​](#parseresultwithprompt "Direct link to parseResultWithPrompt()")

> **parseResultWithPrompt**(`generations`: [`Generation`](/docs/api/schema/interfaces/Generation)\[\] | [`ChatGeneration`](/docs/api/schema/interfaces/ChatGeneration)\[\], `_prompt`: [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`Plan`](/docs/api/experimental_plan_and_execute/types/Plan)\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`generations`

[`Generation`](/docs/api/schema/interfaces/Generation)\[\] | [`ChatGeneration`](/docs/api/schema/interfaces/ChatGeneration)\[\]

`_prompt`

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-8 "Direct link to Returns")

`Promise`<[`Plan`](/docs/api/experimental_plan_and_execute/types/Plan)\>

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

[BaseOutputParser](/docs/api/schema_output_parser/classes/BaseOutputParser).[parseResultWithPrompt](/docs/api/schema_output_parser/classes/BaseOutputParser#parseresultwithprompt)

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/schema/output\_parser.ts:16](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/output_parser.ts#L16)

### parseWithPrompt()[​](#parsewithprompt "Direct link to parseWithPrompt()")

> **parseWithPrompt**(`text`: `string`, `_prompt`: [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<[`Plan`](/docs/api/experimental_plan_and_execute/types/Plan)\>

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`text`

`string`

`_prompt`

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-9 "Direct link to Returns")

`Promise`<[`Plan`](/docs/api/experimental_plan_and_execute/types/Plan)\>

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

[BaseOutputParser](/docs/api/schema_output_parser/classes/BaseOutputParser).[parseWithPrompt](/docs/api/schema_output_parser/classes/BaseOutputParser#parsewithprompt)

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/schema/output\_parser.ts:45](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/output_parser.ts#L45)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-10 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

[BaseOutputParser](/docs/api/schema_output_parser/classes/BaseOutputParser).[toJSON](/docs/api/schema_output_parser/classes/BaseOutputParser#tojson)

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-11 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

[BaseOutputParser](/docs/api/schema_output_parser/classes/BaseOutputParser).[toJSONNotImplemented](/docs/api/schema_output_parser/classes/BaseOutputParser#tojsonnotimplemented)

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)