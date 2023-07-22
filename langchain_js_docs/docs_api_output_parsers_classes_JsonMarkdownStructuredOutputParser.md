JsonMarkdownStructuredOutputParser<T\>
======================================

Class to parse the output of an LLM call.

Type parameters[​](#type-parameters "Direct link to Type parameters")
---------------------------------------------------------------------

*   `T` _extends_ `z.ZodTypeAny`

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`StructuredOutputParser`](/docs/api/output_parsers/classes/StructuredOutputParser)<`T`\>.**JsonMarkdownStructuredOutputParser**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new JsonMarkdownStructuredOutputParser**<T\>(`schema`: `T`): [`JsonMarkdownStructuredOutputParser`](/docs/api/output_parsers/classes/JsonMarkdownStructuredOutputParser)<`T`\>

#### Type parameters[​](#type-parameters-1 "Direct link to Type parameters")

*   `T` _extends_ `ZodType`<`any`, `any`, `any`, `T`\>

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`schema`

`T`

#### Returns[​](#returns "Direct link to Returns")

[`JsonMarkdownStructuredOutputParser`](/docs/api/output_parsers/classes/JsonMarkdownStructuredOutputParser)<`T`\>

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[StructuredOutputParser](/docs/api/output_parsers/classes/StructuredOutputParser).[constructor](/docs/api/output_parsers/classes/StructuredOutputParser#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/output\_parsers/structured.ts:33](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/output_parsers/structured.ts#L33)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[StructuredOutputParser](/docs/api/output_parsers/classes/StructuredOutputParser).[lc\_kwargs](/docs/api/output_parsers/classes/StructuredOutputParser#lc_kwargs)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[StructuredOutputParser](/docs/api/output_parsers/classes/StructuredOutputParser).[lc\_namespace](/docs/api/output_parsers/classes/StructuredOutputParser#lc_namespace)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/output\_parsers/structured.ts:27](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/output_parsers/structured.ts#L27)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[StructuredOutputParser](/docs/api/output_parsers/classes/StructuredOutputParser).[lc\_serializable](/docs/api/output_parsers/classes/StructuredOutputParser#lc_serializable)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L55)

### schema[​](#schema "Direct link to schema")

> **schema**: `T`

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[StructuredOutputParser](/docs/api/output_parsers/classes/StructuredOutputParser).[schema](/docs/api/output_parsers/classes/StructuredOutputParser#schema)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/output\_parsers/structured.ts:33](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/output_parsers/structured.ts#L33)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-1 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

StructuredOutputParser.lc\_aliases

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[StructuredOutputParser](/docs/api/output_parsers/classes/StructuredOutputParser).[lc\_aliases](/docs/api/output_parsers/classes/StructuredOutputParser#lc_aliases)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

StructuredOutputParser.lc\_attributes

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[StructuredOutputParser](/docs/api/output_parsers/classes/StructuredOutputParser).[lc\_attributes](/docs/api/output_parsers/classes/StructuredOutputParser#lc_attributes)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

StructuredOutputParser.lc\_secrets

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

[StructuredOutputParser](/docs/api/output_parsers/classes/StructuredOutputParser).[lc\_secrets](/docs/api/output_parsers/classes/StructuredOutputParser#lc_secrets)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### \_type()[​](#_type "Direct link to _type")

Return the string type key uniquely identifying this class of parser

> **\_type**(): `string`

#### Returns[​](#returns-4 "Direct link to Returns")

`string`

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

[StructuredOutputParser](/docs/api/output_parsers/classes/StructuredOutputParser).[\_type](/docs/api/output_parsers/classes/StructuredOutputParser#_type)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/schema/output\_parser.ts:69](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/output_parser.ts#L69)

### getFormatInstructions()[​](#getformatinstructions "Direct link to getFormatInstructions()")

Return a string describing the format of the output.

#### Example[​](#example "Direct link to Example")

    {  "foo": "bar"}

> **getFormatInstructions**(`options`?: [`JsonMarkdownFormatInstructionsOptions`](/docs/api/output_parsers/interfaces/JsonMarkdownFormatInstructionsOptions)): `string`

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`options?`

[`JsonMarkdownFormatInstructionsOptions`](/docs/api/output_parsers/interfaces/JsonMarkdownFormatInstructionsOptions)

#### Returns[​](#returns-5 "Direct link to Returns")

`string`

Format instructions.

#### Overrides[​](#overrides "Direct link to Overrides")

[StructuredOutputParser](/docs/api/output_parsers/classes/StructuredOutputParser).[getFormatInstructions](/docs/api/output_parsers/classes/StructuredOutputParser#getformatinstructions)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/output\_parsers/structured.ts:92](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/output_parsers/structured.ts#L92)

### parse()[​](#parse "Direct link to parse()")

Parse the output of an LLM call.

> **parse**(`text`: `string`): `Promise`<`TypeOf`<`T`\>\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

Description

`text`

`string`

LLM output to parse.

#### Returns[​](#returns-6 "Direct link to Returns")

`Promise`<`TypeOf`<`T`\>\>

Parsed output.

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

[StructuredOutputParser](/docs/api/output_parsers/classes/StructuredOutputParser).[parse](/docs/api/output_parsers/classes/StructuredOutputParser#parse)

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/output\_parsers/structured.ts:74](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/output_parsers/structured.ts#L74)

### parseResult()[​](#parseresult "Direct link to parseResult()")

> **parseResult**(`generations`: [`Generation`](/docs/api/schema/interfaces/Generation)\[\] | [`ChatGeneration`](/docs/api/schema/interfaces/ChatGeneration)\[\], `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`TypeOf`<`T`\>\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`generations`

[`Generation`](/docs/api/schema/interfaces/Generation)\[\] | [`ChatGeneration`](/docs/api/schema/interfaces/ChatGeneration)\[\]

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-7 "Direct link to Returns")

`Promise`<`TypeOf`<`T`\>\>

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

[StructuredOutputParser](/docs/api/output_parsers/classes/StructuredOutputParser).[parseResult](/docs/api/output_parsers/classes/StructuredOutputParser#parseresult)

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/schema/output\_parser.ts:30](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/output_parser.ts#L30)

### parseResultWithPrompt()[​](#parseresultwithprompt "Direct link to parseResultWithPrompt()")

> **parseResultWithPrompt**(`generations`: [`Generation`](/docs/api/schema/interfaces/Generation)\[\] | [`ChatGeneration`](/docs/api/schema/interfaces/ChatGeneration)\[\], `_prompt`: [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`TypeOf`<`T`\>\>

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`generations`

[`Generation`](/docs/api/schema/interfaces/Generation)\[\] | [`ChatGeneration`](/docs/api/schema/interfaces/ChatGeneration)\[\]

`_prompt`

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-8 "Direct link to Returns")

`Promise`<`TypeOf`<`T`\>\>

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

[StructuredOutputParser](/docs/api/output_parsers/classes/StructuredOutputParser).[parseResultWithPrompt](/docs/api/output_parsers/classes/StructuredOutputParser#parseresultwithprompt)

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/schema/output\_parser.ts:16](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/output_parser.ts#L16)

### parseWithPrompt()[​](#parsewithprompt "Direct link to parseWithPrompt()")

> **parseWithPrompt**(`text`: `string`, `_prompt`: [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`TypeOf`<`T`\>\>

#### Parameters[​](#parameters-5 "Direct link to Parameters")

Parameter

Type

`text`

`string`

`_prompt`

[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[​](#returns-9 "Direct link to Returns")

`Promise`<`TypeOf`<`T`\>\>

#### Inherited from[​](#inherited-from-15 "Direct link to Inherited from")

[StructuredOutputParser](/docs/api/output_parsers/classes/StructuredOutputParser).[parseWithPrompt](/docs/api/output_parsers/classes/StructuredOutputParser#parsewithprompt)

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/schema/output\_parser.ts:45](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/output_parser.ts#L45)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-10 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-16 "Direct link to Inherited from")

[StructuredOutputParser](/docs/api/output_parsers/classes/StructuredOutputParser).[toJSON](/docs/api/output_parsers/classes/StructuredOutputParser#tojson)

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/output\_parsers/structured.ts:29](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/output_parsers/structured.ts#L29)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-11 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-17 "Direct link to Inherited from")

[StructuredOutputParser](/docs/api/output_parsers/classes/StructuredOutputParser).[toJSONNotImplemented](/docs/api/output_parsers/classes/StructuredOutputParser#tojsonnotimplemented)

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)

### fromNamesAndDescriptions()[​](#fromnamesanddescriptions "Direct link to fromNamesAndDescriptions()")

> `Static` **fromNamesAndDescriptions**<S\>(`schemas`: `S`): [`JsonMarkdownStructuredOutputParser`](/docs/api/output_parsers/classes/JsonMarkdownStructuredOutputParser)<`ZodObject`<{}, "strip", `ZodTypeAny`, {}, {}\>\>

#### Type parameters[​](#type-parameters-2 "Direct link to Type parameters")

*   `S` _extends_ {}

#### Parameters[​](#parameters-6 "Direct link to Parameters")

Parameter

Type

`schemas`

`S`

#### Returns[​](#returns-12 "Direct link to Returns")

[`JsonMarkdownStructuredOutputParser`](/docs/api/output_parsers/classes/JsonMarkdownStructuredOutputParser)<`ZodObject`<{}, "strip", `ZodTypeAny`, {}, {}\>\>

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[StructuredOutputParser](/docs/api/output_parsers/classes/StructuredOutputParser).[fromNamesAndDescriptions](/docs/api/output_parsers/classes/StructuredOutputParser#fromnamesanddescriptions)

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/output\_parsers/structured.ts:178](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/output_parsers/structured.ts#L178)

### fromZodSchema()[​](#fromzodschema "Direct link to fromZodSchema()")

> `Static` **fromZodSchema**<T\>(`schema`: `T`): [`JsonMarkdownStructuredOutputParser`](/docs/api/output_parsers/classes/JsonMarkdownStructuredOutputParser)<`T`\>

#### Type parameters[​](#type-parameters-3 "Direct link to Type parameters")

*   `T` _extends_ `ZodType`<`any`, `any`, `any`, `T`\>

#### Parameters[​](#parameters-7 "Direct link to Parameters")

Parameter

Type

`schema`

`T`

#### Returns[​](#returns-13 "Direct link to Returns")

[`JsonMarkdownStructuredOutputParser`](/docs/api/output_parsers/classes/JsonMarkdownStructuredOutputParser)<`T`\>

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[StructuredOutputParser](/docs/api/output_parsers/classes/StructuredOutputParser).[fromZodSchema](/docs/api/output_parsers/classes/StructuredOutputParser#fromzodschema)

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/output\_parsers/structured.ts:174](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/output_parsers/structured.ts#L174)