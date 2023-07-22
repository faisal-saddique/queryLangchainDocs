BaseStringPromptTemplate
========================

Base class for prompt templates. Exposes a format method that returns a string prompt given a set of input values.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate).**BaseStringPromptTemplate**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new BaseStringPromptTemplate**(`input`: [`BasePromptTemplateInput`](/docs/api/prompts/interfaces/BasePromptTemplateInput)): [`BaseStringPromptTemplate`](/docs/api/prompts/classes/BaseStringPromptTemplate)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`input`

[`BasePromptTemplateInput`](/docs/api/prompts/interfaces/BasePromptTemplateInput)

#### Returns[​](#returns "Direct link to Returns")

[`BaseStringPromptTemplate`](/docs/api/prompts/classes/BaseStringPromptTemplate)

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BasePromptTemplate](/docs/api/prompts/classes/BasePromptTemplate).[constructor](/docs/api/prompts/classes/BasePromptTemplate#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/prompts/base.ts:76](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L76)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### PromptValueReturnType[​](#promptvaluereturntype "Direct link to PromptValueReturnType")

> **PromptValueReturnType**: [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[BasePromptTemplate](/docs/api/prompts/classes/BasePromptTemplate).[PromptValueReturnType](/docs/api/prompts/classes/BasePromptTemplate#promptvaluereturntype)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/prompts/base.ts:58](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L58)

### inputVariables[​](#inputvariables "Direct link to inputVariables")

> **inputVariables**: `string`\[\]

A list of variable names the prompt template expects

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[BasePromptTemplate](/docs/api/prompts/classes/BasePromptTemplate).[inputVariables](/docs/api/prompts/classes/BasePromptTemplate#inputvariables)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/prompts/base.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L70)

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[BasePromptTemplate](/docs/api/prompts/classes/BasePromptTemplate).[lc\_kwargs](/docs/api/prompts/classes/BasePromptTemplate#lc_kwargs)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[BasePromptTemplate](/docs/api/prompts/classes/BasePromptTemplate).[lc\_namespace](/docs/api/prompts/classes/BasePromptTemplate#lc_namespace)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/prompts/base.ts:62](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L62)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `true`

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[BasePromptTemplate](/docs/api/prompts/classes/BasePromptTemplate).[lc\_serializable](/docs/api/prompts/classes/BasePromptTemplate#lc_serializable)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/prompts/base.ts:60](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L60)

### partialVariables[​](#partialvariables "Direct link to partialVariables")

> **partialVariables**: [`InputValues`](/docs/api/schema/types/InputValues) = `{}`

Partial variables

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[BasePromptTemplate](/docs/api/prompts/classes/BasePromptTemplate).[partialVariables](/docs/api/prompts/classes/BasePromptTemplate#partialvariables)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/prompts/base.ts:74](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L74)

### outputParser?[​](#outputparser "Direct link to outputParser?")

> **outputParser**: [`BaseOutputParser`](/docs/api/schema_output_parser/classes/BaseOutputParser)<`unknown`\>

How to parse the output of calling an LLM on this formatted prompt

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

[BasePromptTemplate](/docs/api/prompts/classes/BasePromptTemplate).[outputParser](/docs/api/prompts/classes/BasePromptTemplate#outputparser)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/prompts/base.ts:72](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L72)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-1 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

BasePromptTemplate.lc\_aliases

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

[BasePromptTemplate](/docs/api/prompts/classes/BasePromptTemplate).[lc\_aliases](/docs/api/prompts/classes/BasePromptTemplate#lc_aliases)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

BasePromptTemplate.lc\_attributes

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/prompts/base.ts:64](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L64)

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

[BasePromptTemplate](/docs/api/prompts/classes/BasePromptTemplate).[lc\_attributes](/docs/api/prompts/classes/BasePromptTemplate#lc_attributes)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/prompts/base.ts:64](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L64)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

BasePromptTemplate.lc\_secrets

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

[BasePromptTemplate](/docs/api/prompts/classes/BasePromptTemplate).[lc\_secrets](/docs/api/prompts/classes/BasePromptTemplate#lc_secrets)

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### \_getPromptType()[​](#_getprompttype "Direct link to _getprompttype")

Return the string type key uniquely identifying this class of prompt template.

> `Abstract` **\_getPromptType**(): `string`

#### Returns[​](#returns-4 "Direct link to Returns")

`string`

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

[BasePromptTemplate](/docs/api/prompts/classes/BasePromptTemplate).[\_getPromptType](/docs/api/prompts/classes/BasePromptTemplate#_getprompttype)

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/prompts/base.ts:130](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L130)

### format()[​](#format "Direct link to format()")

Format the prompt given the input values.

#### Example[​](#example "Direct link to Example")

    prompt.format({ foo: "bar" });

> `Abstract` **format**(`values`: [`InputValues`](/docs/api/schema/types/InputValues)): `Promise`<`string`\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

Description

`values`

[`InputValues`](/docs/api/schema/types/InputValues)

A dictionary of arguments to be passed to the prompt template.

#### Returns[​](#returns-5 "Direct link to Returns")

`Promise`<`string`\>

A formatted prompt string.

#### Inherited from[​](#inherited-from-15 "Direct link to Inherited from")

[BasePromptTemplate](/docs/api/prompts/classes/BasePromptTemplate).[format](/docs/api/prompts/classes/BasePromptTemplate#format)

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/prompts/base.ts:118](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L118)

### formatPromptValue()[​](#formatpromptvalue "Direct link to formatPromptValue()")

Format the prompt given the input values and return a formatted prompt value.

> **formatPromptValue**(`values`: [`InputValues`](/docs/api/schema/types/InputValues)): `Promise`<[`StringPromptValue`](/docs/api/prompts/classes/StringPromptValue)\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`values`

[`InputValues`](/docs/api/schema/types/InputValues)

#### Returns[​](#returns-6 "Direct link to Returns")

`Promise`<[`StringPromptValue`](/docs/api/prompts/classes/StringPromptValue)\>

A formatted PromptValue.

#### Overrides[​](#overrides "Direct link to Overrides")

[BasePromptTemplate](/docs/api/prompts/classes/BasePromptTemplate).[formatPromptValue](/docs/api/prompts/classes/BasePromptTemplate#formatpromptvalue)

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/prompts/base.ts:176](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L176)

### mergePartialAndUserVariables()[​](#mergepartialanduservariables "Direct link to mergePartialAndUserVariables()")

> **mergePartialAndUserVariables**(`userVariables`: [`InputValues`](/docs/api/schema/types/InputValues)): `Promise`<[`InputValues`](/docs/api/schema/types/InputValues)\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`userVariables`

[`InputValues`](/docs/api/schema/types/InputValues)

#### Returns[​](#returns-7 "Direct link to Returns")

`Promise`<[`InputValues`](/docs/api/schema/types/InputValues)\>

#### Inherited from[​](#inherited-from-16 "Direct link to Inherited from")

[BasePromptTemplate](/docs/api/prompts/classes/BasePromptTemplate).[mergePartialAndUserVariables](/docs/api/prompts/classes/BasePromptTemplate#mergepartialanduservariables)

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/prompts/base.ts:89](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L89)

### partial()[​](#partial "Direct link to partial()")

> `Abstract` **partial**(`values`: [`PartialValues`](/docs/api/schema/types/PartialValues)): `Promise`<[`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)\>

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`values`

[`PartialValues`](/docs/api/schema/types/PartialValues)

#### Returns[​](#returns-8 "Direct link to Returns")

`Promise`<[`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)\>

#### Inherited from[​](#inherited-from-17 "Direct link to Inherited from")

[BasePromptTemplate](/docs/api/prompts/classes/BasePromptTemplate).[partial](/docs/api/prompts/classes/BasePromptTemplate#partial)

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/prompts/base.ts:87](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L87)

### serialize()[​](#serialize "Direct link to serialize()")

Return a json-like object representing this prompt template.

#### Deprecated[​](#deprecated "Direct link to Deprecated")

> **serialize**(): [`SerializedBasePromptTemplate`](/docs/api/prompts/types/SerializedBasePromptTemplate)

#### Returns[​](#returns-9 "Direct link to Returns")

[`SerializedBasePromptTemplate`](/docs/api/prompts/types/SerializedBasePromptTemplate)

#### Inherited from[​](#inherited-from-18 "Direct link to Inherited from")

[BasePromptTemplate](/docs/api/prompts/classes/BasePromptTemplate).[serialize](/docs/api/prompts/classes/BasePromptTemplate#serialize)

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/prompts/base.ts:136](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L136)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-10 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-19 "Direct link to Inherited from")

[BasePromptTemplate](/docs/api/prompts/classes/BasePromptTemplate).[toJSON](/docs/api/prompts/classes/BasePromptTemplate#tojson)

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-11 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-20 "Direct link to Inherited from")

[BasePromptTemplate](/docs/api/prompts/classes/BasePromptTemplate).[toJSONNotImplemented](/docs/api/prompts/classes/BasePromptTemplate#tojsonnotimplemented)

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)

### deserialize()[​](#deserialize "Direct link to deserialize()")

#### Deprecated[​](#deprecated-1 "Direct link to Deprecated")

Load a prompt template from a json-like object describing it.

#### Remarks[​](#remarks "Direct link to Remarks")

Deserializing needs to be async because templates (e.g. [FewShotPromptTemplate](/docs/api/prompts/classes/FewShotPromptTemplate)) can reference remote resources that we read asynchronously with a web request.

> `Static` **deserialize**(`data`: [`SerializedBasePromptTemplate`](/docs/api/prompts/types/SerializedBasePromptTemplate)): `Promise`<[`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)\>

#### Parameters[​](#parameters-5 "Direct link to Parameters")

Parameter

Type

`data`

[`SerializedBasePromptTemplate`](/docs/api/prompts/types/SerializedBasePromptTemplate)

#### Returns[​](#returns-12 "Direct link to Returns")

`Promise`<[`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)\>

#### Inherited from[​](#inherited-from-21 "Direct link to Inherited from")

[BasePromptTemplate](/docs/api/prompts/classes/BasePromptTemplate).[deserialize](/docs/api/prompts/classes/BasePromptTemplate#deserialize)

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/prompts/base.ts:149](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L149)