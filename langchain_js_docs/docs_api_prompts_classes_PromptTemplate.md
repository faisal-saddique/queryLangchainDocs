PromptTemplate
==============

Schema to represent a basic prompt for an LLM.

Example[​](#example "Direct link to Example")
---------------------------------------------

    import { PromptTemplate } from "langchain/prompts";const prompt = new PromptTemplate({  inputVariables: ["foo"],  template: "Say {foo}",});

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseStringPromptTemplate`](/docs/api/prompts/classes/BaseStringPromptTemplate).**PromptTemplate**

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   [`PromptTemplateInput`](/docs/api/prompts/interfaces/PromptTemplateInput)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new PromptTemplate**(`input`: [`PromptTemplateInput`](/docs/api/prompts/interfaces/PromptTemplateInput)): [`PromptTemplate`](/docs/api/prompts/classes/PromptTemplate)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`input`

[`PromptTemplateInput`](/docs/api/prompts/interfaces/PromptTemplateInput)

#### Returns[​](#returns "Direct link to Returns")

[`PromptTemplate`](/docs/api/prompts/classes/PromptTemplate)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseStringPromptTemplate](/docs/api/prompts/classes/BaseStringPromptTemplate).[constructor](/docs/api/prompts/classes/BaseStringPromptTemplate#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/prompts/prompt.ts:61](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/prompt.ts#L61)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### PromptValueReturnType[​](#promptvaluereturntype "Direct link to PromptValueReturnType")

> **PromptValueReturnType**: [`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BaseStringPromptTemplate](/docs/api/prompts/classes/BaseStringPromptTemplate).[PromptValueReturnType](/docs/api/prompts/classes/BaseStringPromptTemplate#promptvaluereturntype)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/prompts/base.ts:58](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L58)

### inputVariables[​](#inputvariables "Direct link to inputVariables")

> **inputVariables**: `string`\[\]

A list of variable names the prompt template expects

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

[PromptTemplateInput](/docs/api/prompts/interfaces/PromptTemplateInput).[inputVariables](/docs/api/prompts/interfaces/PromptTemplateInput#inputvariables)

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[BaseStringPromptTemplate](/docs/api/prompts/classes/BaseStringPromptTemplate).[inputVariables](/docs/api/prompts/classes/BaseStringPromptTemplate#inputvariables)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/prompts/base.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L70)

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[BaseStringPromptTemplate](/docs/api/prompts/classes/BaseStringPromptTemplate).[lc\_kwargs](/docs/api/prompts/classes/BaseStringPromptTemplate#lc_kwargs)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[BaseStringPromptTemplate](/docs/api/prompts/classes/BaseStringPromptTemplate).[lc\_namespace](/docs/api/prompts/classes/BaseStringPromptTemplate#lc_namespace)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/prompts/base.ts:62](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L62)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `true`

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[BaseStringPromptTemplate](/docs/api/prompts/classes/BaseStringPromptTemplate).[lc\_serializable](/docs/api/prompts/classes/BaseStringPromptTemplate#lc_serializable)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/prompts/base.ts:60](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L60)

### partialVariables[​](#partialvariables "Direct link to partialVariables")

> **partialVariables**: [`InputValues`](/docs/api/schema/types/InputValues) = `{}`

Partial variables

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

[PromptTemplateInput](/docs/api/prompts/interfaces/PromptTemplateInput).[partialVariables](/docs/api/prompts/interfaces/PromptTemplateInput#partialvariables)

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[BaseStringPromptTemplate](/docs/api/prompts/classes/BaseStringPromptTemplate).[partialVariables](/docs/api/prompts/classes/BaseStringPromptTemplate#partialvariables)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/prompts/base.ts:74](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L74)

### template[​](#template "Direct link to template")

> **template**: `string`

The prompt template

#### Implementation of[​](#implementation-of-2 "Direct link to Implementation of")

[PromptTemplateInput](/docs/api/prompts/interfaces/PromptTemplateInput).[template](/docs/api/prompts/interfaces/PromptTemplateInput#template)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/prompts/prompt.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/prompt.ts#L55)

### templateFormat[​](#templateformat "Direct link to templateFormat")

> **templateFormat**: [`TemplateFormat`](/docs/api/prompts/types/TemplateFormat) = `"f-string"`

The format of the prompt template. Options are 'f-string', 'jinja-2'

#### Default Value[​](#default-value "Direct link to Default Value")

'f-string'

#### Implementation of[​](#implementation-of-3 "Direct link to Implementation of")

[PromptTemplateInput](/docs/api/prompts/interfaces/PromptTemplateInput).[templateFormat](/docs/api/prompts/interfaces/PromptTemplateInput#templateformat)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/prompts/prompt.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/prompt.ts#L57)

### validateTemplate[​](#validatetemplate "Direct link to validateTemplate")

> **validateTemplate**: `boolean` = `true`

Whether or not to try validating the template on initialization

#### Default Value[​](#default-value-1 "Direct link to Default Value")

`true`

#### Implementation of[​](#implementation-of-4 "Direct link to Implementation of")

[PromptTemplateInput](/docs/api/prompts/interfaces/PromptTemplateInput).[validateTemplate](/docs/api/prompts/interfaces/PromptTemplateInput#validatetemplate)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/prompts/prompt.ts:59](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/prompt.ts#L59)

### outputParser?[​](#outputparser "Direct link to outputParser?")

> **outputParser**: [`BaseOutputParser`](/docs/api/schema_output_parser/classes/BaseOutputParser)<`unknown`\>

How to parse the output of calling an LLM on this formatted prompt

#### Implementation of[​](#implementation-of-5 "Direct link to Implementation of")

[PromptTemplateInput](/docs/api/prompts/interfaces/PromptTemplateInput).[outputParser](/docs/api/prompts/interfaces/PromptTemplateInput#outputparser)

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[BaseStringPromptTemplate](/docs/api/prompts/classes/BaseStringPromptTemplate).[outputParser](/docs/api/prompts/classes/BaseStringPromptTemplate#outputparser)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/prompts/base.ts:72](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L72)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-1 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

BaseStringPromptTemplate.lc\_aliases

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[BaseStringPromptTemplate](/docs/api/prompts/classes/BaseStringPromptTemplate).[lc\_aliases](/docs/api/prompts/classes/BaseStringPromptTemplate#lc_aliases)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

BaseStringPromptTemplate.lc\_attributes

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/prompts/base.ts:64](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L64)

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

[BaseStringPromptTemplate](/docs/api/prompts/classes/BaseStringPromptTemplate).[lc\_attributes](/docs/api/prompts/classes/BaseStringPromptTemplate#lc_attributes)

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/prompts/base.ts:64](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L64)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

BaseStringPromptTemplate.lc\_secrets

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

[BaseStringPromptTemplate](/docs/api/prompts/classes/BaseStringPromptTemplate).[lc\_secrets](/docs/api/prompts/classes/BaseStringPromptTemplate#lc_secrets)

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### \_getPromptType()[​](#_getprompttype "Direct link to _getprompttype")

Return the string type key uniquely identifying this class of prompt template.

> **\_getPromptType**(): "prompt"

#### Returns[​](#returns-4 "Direct link to Returns")

"prompt"

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[BaseStringPromptTemplate](/docs/api/prompts/classes/BaseStringPromptTemplate).[\_getPromptType](/docs/api/prompts/classes/BaseStringPromptTemplate#_getprompttype)

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/prompts/prompt.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/prompt.ts#L80)

### format()[​](#format "Direct link to format()")

Format the prompt given the input values.

#### Example[​](#example-1 "Direct link to Example")

    prompt.format({ foo: "bar" });

> **format**(`values`: [`InputValues`](/docs/api/schema/types/InputValues)): `Promise`<`string`\>

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

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[BaseStringPromptTemplate](/docs/api/prompts/classes/BaseStringPromptTemplate).[format](/docs/api/prompts/classes/BaseStringPromptTemplate#format)

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/prompts/prompt.ts:84](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/prompt.ts#L84)

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

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

[BaseStringPromptTemplate](/docs/api/prompts/classes/BaseStringPromptTemplate).[formatPromptValue](/docs/api/prompts/classes/BaseStringPromptTemplate#formatpromptvalue)

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

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

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

[BaseStringPromptTemplate](/docs/api/prompts/classes/BaseStringPromptTemplate).[mergePartialAndUserVariables](/docs/api/prompts/classes/BaseStringPromptTemplate#mergepartialanduservariables)

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/prompts/base.ts:89](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L89)

### partial()[​](#partial "Direct link to partial()")

> **partial**(`values`: [`PartialValues`](/docs/api/schema/types/PartialValues)): `Promise`<[`PromptTemplate`](/docs/api/prompts/classes/PromptTemplate)\>

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`values`

[`PartialValues`](/docs/api/schema/types/PartialValues)

#### Returns[​](#returns-8 "Direct link to Returns")

`Promise`<[`PromptTemplate`](/docs/api/prompts/classes/PromptTemplate)\>

#### Overrides[​](#overrides-3 "Direct link to Overrides")

[BaseStringPromptTemplate](/docs/api/prompts/classes/BaseStringPromptTemplate).[partial](/docs/api/prompts/classes/BaseStringPromptTemplate#partial)

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/prompts/prompt.ts:141](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/prompt.ts#L141)

### serialize()[​](#serialize "Direct link to serialize()")

Return a json-like object representing this prompt template.

#### Deprecated[​](#deprecated "Direct link to Deprecated")

> **serialize**(): [`SerializedPromptTemplate`](/docs/api/prompts/types/SerializedPromptTemplate)

#### Returns[​](#returns-9 "Direct link to Returns")

[`SerializedPromptTemplate`](/docs/api/prompts/types/SerializedPromptTemplate)

#### Overrides[​](#overrides-4 "Direct link to Overrides")

[BaseStringPromptTemplate](/docs/api/prompts/classes/BaseStringPromptTemplate).[serialize](/docs/api/prompts/classes/BaseStringPromptTemplate#serialize)

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/prompts/prompt.ts:153](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/prompt.ts#L153)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-10 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-15 "Direct link to Inherited from")

[BaseStringPromptTemplate](/docs/api/prompts/classes/BaseStringPromptTemplate).[toJSON](/docs/api/prompts/classes/BaseStringPromptTemplate#tojson)

#### Defined in[​](#defined-in-23 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-11 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-16 "Direct link to Inherited from")

[BaseStringPromptTemplate](/docs/api/prompts/classes/BaseStringPromptTemplate).[toJSONNotImplemented](/docs/api/prompts/classes/BaseStringPromptTemplate#tojsonnotimplemented)

#### Defined in[​](#defined-in-24 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)

### deserialize()[​](#deserialize "Direct link to deserialize()")

#### Deprecated[​](#deprecated-1 "Direct link to Deprecated")

Load a prompt template from a json-like object describing it.

#### Remarks[​](#remarks "Direct link to Remarks")

Deserializing needs to be async because templates (e.g. [FewShotPromptTemplate](/docs/api/prompts/classes/FewShotPromptTemplate)) can reference remote resources that we read asynchronously with a web request.

> `Static` **deserialize**(`data`: [`SerializedPromptTemplate`](/docs/api/prompts/types/SerializedPromptTemplate)): `Promise`<[`PromptTemplate`](/docs/api/prompts/classes/PromptTemplate)\>

#### Parameters[​](#parameters-5 "Direct link to Parameters")

Parameter

Type

`data`

[`SerializedPromptTemplate`](/docs/api/prompts/types/SerializedPromptTemplate)

#### Returns[​](#returns-12 "Direct link to Returns")

`Promise`<[`PromptTemplate`](/docs/api/prompts/classes/PromptTemplate)\>

#### Overrides[​](#overrides-5 "Direct link to Overrides")

[BaseStringPromptTemplate](/docs/api/prompts/classes/BaseStringPromptTemplate).[deserialize](/docs/api/prompts/classes/BaseStringPromptTemplate#deserialize)

#### Defined in[​](#defined-in-25 "Direct link to Defined in")

[langchain/src/prompts/prompt.ts:167](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/prompt.ts#L167)

### fromExamples()[​](#fromexamples "Direct link to fromExamples()")

Take examples in list format with prefix and suffix to create a prompt.

Intendend to be used a a way to dynamically create a prompt from examples.

> `Static` **fromExamples**(`examples`: `string`\[\], `suffix`: `string`, `inputVariables`: `string`\[\], `exampleSeparator`: `string` = `"\n\n"`, `prefix`: `string` = `""`): [`PromptTemplate`](/docs/api/prompts/classes/PromptTemplate)

#### Parameters[​](#parameters-6 "Direct link to Parameters")

Parameter

Type

Default value

Description

`examples`

`string`\[\]

`undefined`

List of examples to use in the prompt.

`suffix`

`string`

`undefined`

String to go after the list of examples. Should generally set up the user's input.

`inputVariables`

`string`\[\]

`undefined`

A list of variable names the final prompt template will expect

`exampleSeparator`

`string`

`"\n\n"`

The separator to use in between examples

`prefix`

`string`

`""`

String that should go before any examples. Generally includes examples.

#### Returns[​](#returns-13 "Direct link to Returns")

[`PromptTemplate`](/docs/api/prompts/classes/PromptTemplate)

The final prompt template generated.

#### Defined in[​](#defined-in-26 "Direct link to Defined in")

[langchain/src/prompts/prompt.ts:102](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/prompt.ts#L102)

### fromTemplate()[​](#fromtemplate "Direct link to fromTemplate()")

Load prompt template from a template f-string

> `Static` **fromTemplate**(`template`: `string`, «destructured»: `Omit`<[`PromptTemplateInput`](/docs/api/prompts/interfaces/PromptTemplateInput), "template" | "inputVariables"\> = `{}`): [`PromptTemplate`](/docs/api/prompts/classes/PromptTemplate)

#### Parameters[​](#parameters-7 "Direct link to Parameters")

Parameter

Type

`template`

`string`

`«destructured»`

`Omit`<[`PromptTemplateInput`](/docs/api/prompts/interfaces/PromptTemplateInput), "template" | "inputVariables"\>

#### Returns[​](#returns-14 "Direct link to Returns")

[`PromptTemplate`](/docs/api/prompts/classes/PromptTemplate)

#### Defined in[​](#defined-in-27 "Direct link to Defined in")

[langchain/src/prompts/prompt.ts:119](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/prompt.ts#L119)