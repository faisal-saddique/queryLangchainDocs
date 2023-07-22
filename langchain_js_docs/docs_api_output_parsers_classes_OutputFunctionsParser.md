OutputFunctionsParser
=====================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseLLMOutputParser`](/docs/api/schema_output_parser/classes/BaseLLMOutputParser)<`string`\>.**OutputFunctionsParser**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new OutputFunctionsParser**(`config`?: `object`): [`OutputFunctionsParser`](/docs/api/output_parsers/classes/OutputFunctionsParser)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`config?`

`object`

`config.argsOnly?`

`boolean`

#### Returns[​](#returns "Direct link to Returns")

[`OutputFunctionsParser`](/docs/api/output_parsers/classes/OutputFunctionsParser)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[constructor](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/output\_parsers/openai\_functions.ts:18](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/output_parsers/openai_functions.ts#L18)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### argsOnly[​](#argsonly "Direct link to argsOnly")

> **argsOnly**: `boolean` = `true`

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/output\_parsers/openai\_functions.ts:16](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/output_parsers/openai_functions.ts#L16)

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[lc\_kwargs](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#lc_kwargs)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[lc\_namespace](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#lc_namespace)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/output\_parsers/openai\_functions.ts:12](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/output_parsers/openai_functions.ts#L12)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `true`

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[lc\_serializable](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#lc_serializable)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/output\_parsers/openai\_functions.ts:14](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/output_parsers/openai_functions.ts#L14)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-1 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

BaseLLMOutputParser.lc\_aliases

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[lc\_aliases](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#lc_aliases)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

BaseLLMOutputParser.lc\_attributes

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[lc\_attributes](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#lc_attributes)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

BaseLLMOutputParser.lc\_secrets

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[lc\_secrets](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#lc_secrets)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### parseResult()[​](#parseresult "Direct link to parseResult()")

> **parseResult**(`generations`: [`Generation`](/docs/api/schema/interfaces/Generation)\[\] | [`ChatGeneration`](/docs/api/schema/interfaces/ChatGeneration)\[\]): `Promise`<`string`\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`generations`

[`Generation`](/docs/api/schema/interfaces/Generation)\[\] | [`ChatGeneration`](/docs/api/schema/interfaces/ChatGeneration)\[\]

#### Returns[​](#returns-4 "Direct link to Returns")

`Promise`<`string`\>

#### Overrides[​](#overrides-3 "Direct link to Overrides")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[parseResult](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#parseresult)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/output\_parsers/openai\_functions.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/output_parsers/openai_functions.ts#L23)

### parseResultWithPrompt()[​](#parseresultwithprompt "Direct link to parseResultWithPrompt()")

> **parseResultWithPrompt**(`generations`: [`Generation`](/docs/api/schema/interfaces/Generation)\[\] | [`ChatGeneration`](/docs/api/schema/interfaces/ChatGeneration)\[\], `_prompt`: [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`string`\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`generations`

[`Generation`](/docs/api/schema/interfaces/Generation)\[\] | [`ChatGeneration`](/docs/api/schema/interfaces/ChatGeneration)\[\]

`_prompt`

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-5 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[parseResultWithPrompt](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#parseresultwithprompt)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/schema/output\_parser.ts:16](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/output_parser.ts#L16)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-6 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[toJSON](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#tojson)

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-7 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

[BaseLLMOutputParser](/docs/api/schema_output_parser/classes/BaseLLMOutputParser).[toJSONNotImplemented](/docs/api/schema_output_parser/classes/BaseLLMOutputParser#tojsonnotimplemented)

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)