AutoGPTPrompt
=============

Base class for prompt templates. Exposes a format method that returns a string prompt given a set of input values.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseChatPromptTemplate`](/docs/api/prompts/classes/BaseChatPromptTemplate).**AutoGPTPrompt**

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   [`AutoGPTPromptInput`](/docs/api/experimental_autogpt/interfaces/AutoGPTPromptInput)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new AutoGPTPrompt**(`fields`: [`AutoGPTPromptInput`](/docs/api/experimental_autogpt/interfaces/AutoGPTPromptInput)): [`AutoGPTPrompt`](/docs/api/experimental_autogpt/classes/AutoGPTPrompt)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields`

[`AutoGPTPromptInput`](/docs/api/experimental_autogpt/interfaces/AutoGPTPromptInput)

#### Returns[​](#returns "Direct link to Returns")

[`AutoGPTPrompt`](/docs/api/experimental_autogpt/classes/AutoGPTPrompt)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseChatPromptTemplate](/docs/api/prompts/classes/BaseChatPromptTemplate).[constructor](/docs/api/prompts/classes/BaseChatPromptTemplate#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/experimental/autogpt/prompt.ts:36](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/autogpt/prompt.ts#L36)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### PromptValueReturnType[​](#promptvaluereturntype "Direct link to PromptValueReturnType")

> **PromptValueReturnType**: `ChatPromptValue`

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BaseChatPromptTemplate](/docs/api/prompts/classes/BaseChatPromptTemplate).[PromptValueReturnType](/docs/api/prompts/classes/BaseChatPromptTemplate#promptvaluereturntype)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/prompts/chat.ts:126](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/chat.ts#L126)

### aiName[​](#ainame "Direct link to aiName")

> **aiName**: `string`

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

[AutoGPTPromptInput](/docs/api/experimental_autogpt/interfaces/AutoGPTPromptInput).[aiName](/docs/api/experimental_autogpt/interfaces/AutoGPTPromptInput#ainame)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/experimental/autogpt/prompt.ts:26](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/autogpt/prompt.ts#L26)

### aiRole[​](#airole "Direct link to aiRole")

> **aiRole**: `string`

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

[AutoGPTPromptInput](/docs/api/experimental_autogpt/interfaces/AutoGPTPromptInput).[aiRole](/docs/api/experimental_autogpt/interfaces/AutoGPTPromptInput#airole)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/experimental/autogpt/prompt.ts:28](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/autogpt/prompt.ts#L28)

### inputVariables[​](#inputvariables "Direct link to inputVariables")

> **inputVariables**: `string`\[\]

A list of variable names the prompt template expects

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[BaseChatPromptTemplate](/docs/api/prompts/classes/BaseChatPromptTemplate).[inputVariables](/docs/api/prompts/classes/BaseChatPromptTemplate#inputvariables)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/prompts/base.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L70)

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[BaseChatPromptTemplate](/docs/api/prompts/classes/BaseChatPromptTemplate).[lc\_kwargs](/docs/api/prompts/classes/BaseChatPromptTemplate#lc_kwargs)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[BaseChatPromptTemplate](/docs/api/prompts/classes/BaseChatPromptTemplate).[lc\_namespace](/docs/api/prompts/classes/BaseChatPromptTemplate#lc_namespace)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/prompts/base.ts:62](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L62)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `true`

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[BaseChatPromptTemplate](/docs/api/prompts/classes/BaseChatPromptTemplate).[lc\_serializable](/docs/api/prompts/classes/BaseChatPromptTemplate#lc_serializable)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/prompts/base.ts:60](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L60)

### partialVariables[​](#partialvariables "Direct link to partialVariables")

> **partialVariables**: [`InputValues`](/docs/api/schema/types/InputValues) = `{}`

Partial variables

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[BaseChatPromptTemplate](/docs/api/prompts/classes/BaseChatPromptTemplate).[partialVariables](/docs/api/prompts/classes/BaseChatPromptTemplate#partialvariables)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/prompts/base.ts:74](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L74)

### sendTokenLimit[​](#sendtokenlimit "Direct link to sendTokenLimit")

> **sendTokenLimit**: `number`

#### Implementation of[​](#implementation-of-2 "Direct link to Implementation of")

[AutoGPTPromptInput](/docs/api/experimental_autogpt/interfaces/AutoGPTPromptInput).[sendTokenLimit](/docs/api/experimental_autogpt/interfaces/AutoGPTPromptInput#sendtokenlimit)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/experimental/autogpt/prompt.ts:34](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/autogpt/prompt.ts#L34)

### tokenCounter[​](#tokencounter "Direct link to tokenCounter")

> **tokenCounter**: `Function`

#### Type declaration[​](#type-declaration "Direct link to Type declaration")

> (`text`: `string`): `Promise`<`number`\>

##### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`text`

`string`

##### Returns[​](#returns-1 "Direct link to Returns")

`Promise`<`number`\>

#### Implementation of[​](#implementation-of-3 "Direct link to Implementation of")

[AutoGPTPromptInput](/docs/api/experimental_autogpt/interfaces/AutoGPTPromptInput).[tokenCounter](/docs/api/experimental_autogpt/interfaces/AutoGPTPromptInput#tokencounter)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/experimental/autogpt/prompt.ts:32](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/autogpt/prompt.ts#L32)

### tools[​](#tools "Direct link to tools")

> **tools**: `ObjectTool`\[\]

#### Implementation of[​](#implementation-of-4 "Direct link to Implementation of")

[AutoGPTPromptInput](/docs/api/experimental_autogpt/interfaces/AutoGPTPromptInput).[tools](/docs/api/experimental_autogpt/interfaces/AutoGPTPromptInput#tools)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/experimental/autogpt/prompt.ts:30](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/autogpt/prompt.ts#L30)

### outputParser?[​](#outputparser "Direct link to outputParser?")

> **outputParser**: [`BaseOutputParser`](/docs/api/schema_output_parser/classes/BaseOutputParser)<`unknown`\>

How to parse the output of calling an LLM on this formatted prompt

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[BaseChatPromptTemplate](/docs/api/prompts/classes/BaseChatPromptTemplate).[outputParser](/docs/api/prompts/classes/BaseChatPromptTemplate#outputparser)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/prompts/base.ts:72](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L72)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

BaseChatPromptTemplate.lc\_aliases

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[BaseChatPromptTemplate](/docs/api/prompts/classes/BaseChatPromptTemplate).[lc\_aliases](/docs/api/prompts/classes/BaseChatPromptTemplate#lc_aliases)

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

BaseChatPromptTemplate.lc\_attributes

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/prompts/base.ts:64](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L64)

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

[BaseChatPromptTemplate](/docs/api/prompts/classes/BaseChatPromptTemplate).[lc\_attributes](/docs/api/prompts/classes/BaseChatPromptTemplate#lc_attributes)

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/prompts/base.ts:64](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L64)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-4 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

BaseChatPromptTemplate.lc\_secrets

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

[BaseChatPromptTemplate](/docs/api/prompts/classes/BaseChatPromptTemplate).[lc\_secrets](/docs/api/prompts/classes/BaseChatPromptTemplate#lc_secrets)

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### \_getPromptType()[​](#_getprompttype "Direct link to _getprompttype")

Return the string type key uniquely identifying this class of prompt template.

> **\_getPromptType**(): "autogpt"

#### Returns[​](#returns-5 "Direct link to Returns")

"autogpt"

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[BaseChatPromptTemplate](/docs/api/prompts/classes/BaseChatPromptTemplate).[\_getPromptType](/docs/api/prompts/classes/BaseChatPromptTemplate#_getprompttype)

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/experimental/autogpt/prompt.ts:45](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/autogpt/prompt.ts#L45)

### constructFullPrompt()[​](#constructfullprompt "Direct link to constructFullPrompt()")

> **constructFullPrompt**(`goals`: `string`\[\]): `string`

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`goals`

`string`\[\]

#### Returns[​](#returns-6 "Direct link to Returns")

`string`

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/experimental/autogpt/prompt.ts:49](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/autogpt/prompt.ts#L49)

### format()[​](#format "Direct link to format()")

Format the prompt given the input values.

#### Example[​](#example "Direct link to Example")

    prompt.format({ foo: "bar" });

> **format**(`values`: [`InputValues`](/docs/api/schema/types/InputValues)): `Promise`<`string`\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

Description

`values`

[`InputValues`](/docs/api/schema/types/InputValues)

A dictionary of arguments to be passed to the prompt template.

#### Returns[​](#returns-7 "Direct link to Returns")

`Promise`<`string`\>

A formatted prompt string.

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

[BaseChatPromptTemplate](/docs/api/prompts/classes/BaseChatPromptTemplate).[format](/docs/api/prompts/classes/BaseChatPromptTemplate#format)

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/prompts/chat.ts:134](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/chat.ts#L134)

### formatMessages()[​](#formatmessages "Direct link to formatMessages()")

> **formatMessages**(«destructured»: `object`): `Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]\>

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`«destructured»`

`object`

› `goals`

`string`\[\]

› `memory`

[`VectorStoreRetriever`](/docs/api/vectorstores_base/classes/VectorStoreRetriever)<[`VectorStore`](/docs/api/vectorstores_base/classes/VectorStore)\>

› `messages`

[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]

› `user_input`

`string`

#### Returns[​](#returns-8 "Direct link to Returns")

`Promise`<[`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]\>

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[BaseChatPromptTemplate](/docs/api/prompts/classes/BaseChatPromptTemplate).[formatMessages](/docs/api/prompts/classes/BaseChatPromptTemplate#formatmessages)

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/experimental/autogpt/prompt.ts:65](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/autogpt/prompt.ts#L65)

### formatPromptValue()[​](#formatpromptvalue "Direct link to formatPromptValue()")

Format the prompt given the input values and return a formatted prompt value.

> **formatPromptValue**(`values`: [`InputValues`](/docs/api/schema/types/InputValues)): `Promise`<`ChatPromptValue`\>

#### Parameters[​](#parameters-5 "Direct link to Parameters")

Parameter

Type

`values`

[`InputValues`](/docs/api/schema/types/InputValues)

#### Returns[​](#returns-9 "Direct link to Returns")

`Promise`<`ChatPromptValue`\>

A formatted PromptValue.

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

[BaseChatPromptTemplate](/docs/api/prompts/classes/BaseChatPromptTemplate).[formatPromptValue](/docs/api/prompts/classes/BaseChatPromptTemplate#formatpromptvalue)

#### Defined in[​](#defined-in-23 "Direct link to Defined in")

[langchain/src/prompts/chat.ts:138](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/chat.ts#L138)

### mergePartialAndUserVariables()[​](#mergepartialanduservariables "Direct link to mergePartialAndUserVariables()")

> **mergePartialAndUserVariables**(`userVariables`: [`InputValues`](/docs/api/schema/types/InputValues)): `Promise`<[`InputValues`](/docs/api/schema/types/InputValues)\>

#### Parameters[​](#parameters-6 "Direct link to Parameters")

Parameter

Type

`userVariables`

[`InputValues`](/docs/api/schema/types/InputValues)

#### Returns[​](#returns-10 "Direct link to Returns")

`Promise`<[`InputValues`](/docs/api/schema/types/InputValues)\>

#### Inherited from[​](#inherited-from-15 "Direct link to Inherited from")

[BaseChatPromptTemplate](/docs/api/prompts/classes/BaseChatPromptTemplate).[mergePartialAndUserVariables](/docs/api/prompts/classes/BaseChatPromptTemplate#mergepartialanduservariables)

#### Defined in[​](#defined-in-24 "Direct link to Defined in")

[langchain/src/prompts/base.ts:89](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L89)

### partial()[​](#partial "Direct link to partial()")

> **partial**(`_values`: [`PartialValues`](/docs/api/schema/types/PartialValues)): `Promise`<[`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)\>

#### Parameters[​](#parameters-7 "Direct link to Parameters")

Parameter

Type

`_values`

[`PartialValues`](/docs/api/schema/types/PartialValues)

#### Returns[​](#returns-11 "Direct link to Returns")

`Promise`<[`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)\>

#### Overrides[​](#overrides-3 "Direct link to Overrides")

[BaseChatPromptTemplate](/docs/api/prompts/classes/BaseChatPromptTemplate).[partial](/docs/api/prompts/classes/BaseChatPromptTemplate#partial)

#### Defined in[​](#defined-in-25 "Direct link to Defined in")

[langchain/src/experimental/autogpt/prompt.ts:127](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/autogpt/prompt.ts#L127)

### serialize()[​](#serialize "Direct link to serialize()")

Return a json-like object representing this prompt template.

#### Deprecated[​](#deprecated "Direct link to Deprecated")

> **serialize**(): [`SerializedBasePromptTemplate`](/docs/api/prompts/types/SerializedBasePromptTemplate)

#### Returns[​](#returns-12 "Direct link to Returns")

[`SerializedBasePromptTemplate`](/docs/api/prompts/types/SerializedBasePromptTemplate)

#### Overrides[​](#overrides-4 "Direct link to Overrides")

[BaseChatPromptTemplate](/docs/api/prompts/classes/BaseChatPromptTemplate).[serialize](/docs/api/prompts/classes/BaseChatPromptTemplate#serialize)

#### Defined in[​](#defined-in-26 "Direct link to Defined in")

[langchain/src/experimental/autogpt/prompt.ts:131](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/autogpt/prompt.ts#L131)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-13 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-16 "Direct link to Inherited from")

[BaseChatPromptTemplate](/docs/api/prompts/classes/BaseChatPromptTemplate).[toJSON](/docs/api/prompts/classes/BaseChatPromptTemplate#tojson)

#### Defined in[​](#defined-in-27 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-14 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-17 "Direct link to Inherited from")

[BaseChatPromptTemplate](/docs/api/prompts/classes/BaseChatPromptTemplate).[toJSONNotImplemented](/docs/api/prompts/classes/BaseChatPromptTemplate#tojsonnotimplemented)

#### Defined in[​](#defined-in-28 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)

### deserialize()[​](#deserialize "Direct link to deserialize()")

#### Deprecated[​](#deprecated-1 "Direct link to Deprecated")

Load a prompt template from a json-like object describing it.

#### Remarks[​](#remarks "Direct link to Remarks")

Deserializing needs to be async because templates (e.g. FewShotPromptTemplate) can reference remote resources that we read asynchronously with a web request.

> `Static` **deserialize**(`data`: [`SerializedBasePromptTemplate`](/docs/api/prompts/types/SerializedBasePromptTemplate)): `Promise`<[`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)\>

#### Parameters[​](#parameters-8 "Direct link to Parameters")

Parameter

Type

`data`

[`SerializedBasePromptTemplate`](/docs/api/prompts/types/SerializedBasePromptTemplate)

#### Returns[​](#returns-15 "Direct link to Returns")

`Promise`<[`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)\>

#### Inherited from[​](#inherited-from-18 "Direct link to Inherited from")

[BaseChatPromptTemplate](/docs/api/prompts/classes/BaseChatPromptTemplate).[deserialize](/docs/api/prompts/classes/BaseChatPromptTemplate#deserialize)

#### Defined in[​](#defined-in-29 "Direct link to Defined in")

[langchain/src/prompts/base.ts:149](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/base.ts#L149)