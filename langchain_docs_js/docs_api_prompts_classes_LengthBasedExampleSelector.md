LengthBasedExampleSelector
==========================

Base class for example selectors.

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseExampleSelector`](/docs/api/prompts/classes/BaseExampleSelector).**LengthBasedExampleSelector**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new LengthBasedExampleSelector**(`data`: [`LengthBasedExampleSelectorInput`](/docs/api/prompts/interfaces/LengthBasedExampleSelectorInput)): [`LengthBasedExampleSelector`](/docs/api/prompts/classes/LengthBasedExampleSelector)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`data`

[`LengthBasedExampleSelectorInput`](/docs/api/prompts/interfaces/LengthBasedExampleSelectorInput)

#### Returns[](#returns "Direct link to Returns")

[`LengthBasedExampleSelector`](/docs/api/prompts/classes/LengthBasedExampleSelector)

#### Overrides[](#overrides "Direct link to Overrides")

[BaseExampleSelector](/docs/api/prompts/classes/BaseExampleSelector).[constructor](/docs/api/prompts/classes/BaseExampleSelector#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/prompts/selectors/LengthBasedExampleSelector.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/selectors/LengthBasedExampleSelector.ts#L26)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### examplePrompt[](#exampleprompt "Direct link to examplePrompt")

> **examplePrompt**: [`PromptTemplate`](/docs/api/prompts/classes/PromptTemplate)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/prompts/selectors/LengthBasedExampleSelector.ts:18](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/selectors/LengthBasedExampleSelector.ts#L18)

### exampleTextLengths[](#exampletextlengths "Direct link to exampleTextLengths")

> **exampleTextLengths**: `number`\[\] = `[]`

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/prompts/selectors/LengthBasedExampleSelector.ts:24](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/selectors/LengthBasedExampleSelector.ts#L24)

### getTextLength[](#gettextlength "Direct link to getTextLength")

> **getTextLength**: `Function` = `getLengthBased`

#### Type declaration[](#type-declaration "Direct link to Type declaration")

> (`text`: `string`): `number`

##### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`text`

`string`

##### Returns[](#returns-1 "Direct link to Returns")

`number`

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/prompts/selectors/LengthBasedExampleSelector.ts:20](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/selectors/LengthBasedExampleSelector.ts#L20)

### lc\_kwargs[](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BaseExampleSelector](/docs/api/prompts/classes/BaseExampleSelector).[lc\_kwargs](/docs/api/prompts/classes/BaseExampleSelector#lc_kwargs)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L57)

### lc\_namespace[](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[BaseExampleSelector](/docs/api/prompts/classes/BaseExampleSelector).[lc\_namespace](/docs/api/prompts/classes/BaseExampleSelector#lc_namespace)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/prompts/base.ts:201](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/base.ts#L201)

### lc\_serializable[](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[BaseExampleSelector](/docs/api/prompts/classes/BaseExampleSelector).[lc\_serializable](/docs/api/prompts/classes/BaseExampleSelector#lc_serializable)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L55)

### maxLength[](#maxlength "Direct link to maxLength")

> **maxLength**: `number` = `2048`

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/prompts/selectors/LengthBasedExampleSelector.ts:22](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/selectors/LengthBasedExampleSelector.ts#L22)

### examples[](#examples "Direct link to examples")

> `Protected` **examples**: [`Example`](/docs/api/schema/types/Example)\[\] = `[]`

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/prompts/selectors/LengthBasedExampleSelector.ts:16](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/selectors/LengthBasedExampleSelector.ts#L16)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[](#returns-2 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

BaseExampleSelector.lc\_aliases

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[BaseExampleSelector](/docs/api/prompts/classes/BaseExampleSelector).[lc\_aliases](/docs/api/prompts/classes/BaseExampleSelector#lc_aliases)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

### lc\_attributes[](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[](#returns-3 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

BaseExampleSelector.lc\_attributes

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L80)

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[BaseExampleSelector](/docs/api/prompts/classes/BaseExampleSelector).[lc\_attributes](/docs/api/prompts/classes/BaseExampleSelector#lc_attributes)

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L80)

### lc\_secrets[](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[](#returns-4 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

BaseExampleSelector.lc\_secrets

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

[BaseExampleSelector](/docs/api/prompts/classes/BaseExampleSelector).[lc\_secrets](/docs/api/prompts/classes/BaseExampleSelector#lc_secrets)

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### addExample()[](#addexample "Direct link to addExample()")

> **addExample**(`example`: [`Example`](/docs/api/schema/types/Example)): `Promise`<`void`\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`example`

[`Example`](/docs/api/schema/types/Example)

#### Returns[](#returns-5 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[](#overrides-1 "Direct link to Overrides")

[BaseExampleSelector](/docs/api/prompts/classes/BaseExampleSelector).[addExample](/docs/api/prompts/classes/BaseExampleSelector#addexample)

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/prompts/selectors/LengthBasedExampleSelector.ts:33](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/selectors/LengthBasedExampleSelector.ts#L33)

### calculateExampleTextLengths()[](#calculateexampletextlengths "Direct link to calculateExampleTextLengths()")

> **calculateExampleTextLengths**(`v`: `number`\[\], `values`: [`LengthBasedExampleSelector`](/docs/api/prompts/classes/LengthBasedExampleSelector)): `Promise`<`number`\[\]\>

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

`v`

`number`\[\]

`values`

[`LengthBasedExampleSelector`](/docs/api/prompts/classes/LengthBasedExampleSelector)

#### Returns[](#returns-6 "Direct link to Returns")

`Promise`<`number`\[\]\>

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/prompts/selectors/LengthBasedExampleSelector.ts:39](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/selectors/LengthBasedExampleSelector.ts#L39)

### selectExamples()[](#selectexamples "Direct link to selectExamples()")

> **selectExamples**(`inputVariables`: [`Example`](/docs/api/schema/types/Example)): `Promise`<[`Example`](/docs/api/schema/types/Example)\[\]\>

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

`inputVariables`

[`Example`](/docs/api/schema/types/Example)

#### Returns[](#returns-7 "Direct link to Returns")

`Promise`<[`Example`](/docs/api/schema/types/Example)\[\]\>

#### Overrides[](#overrides-2 "Direct link to Overrides")

[BaseExampleSelector](/docs/api/prompts/classes/BaseExampleSelector).[selectExamples](/docs/api/prompts/classes/BaseExampleSelector#selectexamples)

#### Defined in[](#defined-in-17 "Direct link to Defined in")

[langchain/src/prompts/selectors/LengthBasedExampleSelector.ts:54](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/selectors/LengthBasedExampleSelector.ts#L54)

### toJSON()[](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[](#returns-8 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[](#inherited-from-9 "Direct link to Inherited from")

[BaseExampleSelector](/docs/api/prompts/classes/BaseExampleSelector).[toJSON](/docs/api/prompts/classes/BaseExampleSelector#tojson)

#### Defined in[](#defined-in-18 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[](#returns-9 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[](#inherited-from-10 "Direct link to Inherited from")

[BaseExampleSelector](/docs/api/prompts/classes/BaseExampleSelector).[toJSONNotImplemented](/docs/api/prompts/classes/BaseExampleSelector#tojsonnotimplemented)

#### Defined in[](#defined-in-19 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L151)

### fromExamples()[](#fromexamples "Direct link to fromExamples()")

> `Static` **fromExamples**(`examples`: [`Example`](/docs/api/schema/types/Example)\[\], `args`: [`LengthBasedExampleSelectorInput`](/docs/api/prompts/interfaces/LengthBasedExampleSelectorInput)): `Promise`<[`LengthBasedExampleSelector`](/docs/api/prompts/classes/LengthBasedExampleSelector)\>

#### Parameters[](#parameters-5 "Direct link to Parameters")

Parameter

Type

`examples`

[`Example`](/docs/api/schema/types/Example)\[\]

`args`

[`LengthBasedExampleSelectorInput`](/docs/api/prompts/interfaces/LengthBasedExampleSelectorInput)

#### Returns[](#returns-10 "Direct link to Returns")

`Promise`<[`LengthBasedExampleSelector`](/docs/api/prompts/classes/LengthBasedExampleSelector)\>

#### Defined in[](#defined-in-20 "Direct link to Defined in")

[langchain/src/prompts/selectors/LengthBasedExampleSelector.ts:74](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/prompts/selectors/LengthBasedExampleSelector.ts#L74)