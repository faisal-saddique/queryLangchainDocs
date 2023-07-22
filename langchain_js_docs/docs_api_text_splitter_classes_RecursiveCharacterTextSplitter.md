RecursiveCharacterTextSplitter
==============================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`TextSplitter`](/docs/api/text_splitter/classes/TextSplitter).**RecursiveCharacterTextSplitter**

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   [`RecursiveCharacterTextSplitterParams`](/docs/api/text_splitter/interfaces/RecursiveCharacterTextSplitterParams)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new RecursiveCharacterTextSplitter**(`fields`?: `Partial`<[`RecursiveCharacterTextSplitterParams`](/docs/api/text_splitter/interfaces/RecursiveCharacterTextSplitterParams)\>): [`RecursiveCharacterTextSplitter`](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields?`

`Partial`<[`RecursiveCharacterTextSplitterParams`](/docs/api/text_splitter/interfaces/RecursiveCharacterTextSplitterParams)\>

#### Returns[​](#returns "Direct link to Returns")

[`RecursiveCharacterTextSplitter`](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter)

#### Overrides[​](#overrides "Direct link to Overrides")

[TextSplitter](/docs/api/text_splitter/classes/TextSplitter).[constructor](/docs/api/text_splitter/classes/TextSplitter#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/text\_splitter.ts:261](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/text_splitter.ts#L261)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### chunkOverlap[​](#chunkoverlap "Direct link to chunkOverlap")

> **chunkOverlap**: `number` = `200`

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

[RecursiveCharacterTextSplitterParams](/docs/api/text_splitter/interfaces/RecursiveCharacterTextSplitterParams).[chunkOverlap](/docs/api/text_splitter/interfaces/RecursiveCharacterTextSplitterParams#chunkoverlap)

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[TextSplitter](/docs/api/text_splitter/classes/TextSplitter).[chunkOverlap](/docs/api/text_splitter/classes/TextSplitter#chunkoverlap)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:29](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/text_splitter.ts#L29)

### chunkSize[​](#chunksize "Direct link to chunkSize")

> **chunkSize**: `number` = `1000`

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

[RecursiveCharacterTextSplitterParams](/docs/api/text_splitter/interfaces/RecursiveCharacterTextSplitterParams).[chunkSize](/docs/api/text_splitter/interfaces/RecursiveCharacterTextSplitterParams#chunksize)

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[TextSplitter](/docs/api/text_splitter/classes/TextSplitter).[chunkSize](/docs/api/text_splitter/classes/TextSplitter#chunksize)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:27](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/text_splitter.ts#L27)

### keepSeparator[​](#keepseparator "Direct link to keepSeparator")

> **keepSeparator**: `boolean` = `false`

#### Implementation of[​](#implementation-of-2 "Direct link to Implementation of")

[RecursiveCharacterTextSplitterParams](/docs/api/text_splitter/interfaces/RecursiveCharacterTextSplitterParams).[keepSeparator](/docs/api/text_splitter/interfaces/RecursiveCharacterTextSplitterParams#keepseparator)

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[TextSplitter](/docs/api/text_splitter/classes/TextSplitter).[keepSeparator](/docs/api/text_splitter/classes/TextSplitter#keepseparator)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:31](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/text_splitter.ts#L31)

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[TextSplitter](/docs/api/text_splitter/classes/TextSplitter).[lc\_kwargs](/docs/api/text_splitter/classes/TextSplitter#lc_kwargs)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[TextSplitter](/docs/api/text_splitter/classes/TextSplitter).[lc\_namespace](/docs/api/text_splitter/classes/TextSplitter#lc_namespace)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:25](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/text_splitter.ts#L25)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[TextSplitter](/docs/api/text_splitter/classes/TextSplitter).[lc\_serializable](/docs/api/text_splitter/classes/TextSplitter#lc_serializable)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L55)

### lengthFunction[​](#lengthfunction "Direct link to lengthFunction")

> **lengthFunction**: (`text`: `string`) => `number` | (`text`: `string`) => `Promise`<`number`\>

#### Implementation of[​](#implementation-of-3 "Direct link to Implementation of")

[RecursiveCharacterTextSplitterParams](/docs/api/text_splitter/interfaces/RecursiveCharacterTextSplitterParams).[lengthFunction](/docs/api/text_splitter/interfaces/RecursiveCharacterTextSplitterParams#lengthfunction)

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[TextSplitter](/docs/api/text_splitter/classes/TextSplitter).[lengthFunction](/docs/api/text_splitter/classes/TextSplitter#lengthfunction)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:33](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/text_splitter.ts#L33)

### separators[​](#separators "Direct link to separators")

> **separators**: `string`\[\]

#### Implementation of[​](#implementation-of-4 "Direct link to Implementation of")

[RecursiveCharacterTextSplitterParams](/docs/api/text_splitter/interfaces/RecursiveCharacterTextSplitterParams).[separators](/docs/api/text_splitter/interfaces/RecursiveCharacterTextSplitterParams#separators)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:259](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/text_splitter.ts#L259)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-1 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

TextSplitter.lc\_aliases

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[TextSplitter](/docs/api/text_splitter/classes/TextSplitter).[lc\_aliases](/docs/api/text_splitter/classes/TextSplitter#lc_aliases)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

TextSplitter.lc\_attributes

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

[TextSplitter](/docs/api/text_splitter/classes/TextSplitter).[lc\_attributes](/docs/api/text_splitter/classes/TextSplitter#lc_attributes)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

TextSplitter.lc\_secrets

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

[TextSplitter](/docs/api/text_splitter/classes/TextSplitter).[lc\_secrets](/docs/api/text_splitter/classes/TextSplitter#lc_secrets)

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### createDocuments()[​](#createdocuments "Direct link to createDocuments()")

> **createDocuments**(`texts`: `string`\[\], `metadatas`: `Record`<`string`, `any`\>\[\] = `[]`, `chunkHeaderOptions`: [`TextSplitterChunkHeaderOptions`](/docs/api/text_splitter/types/TextSplitterChunkHeaderOptions) = `{}`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

Default value

`texts`

`string`\[\]

`undefined`

`metadatas`

`Record`<`string`, `any`\>\[\]

`[]`

`chunkHeaderOptions`

[`TextSplitterChunkHeaderOptions`](/docs/api/text_splitter/types/TextSplitterChunkHeaderOptions)

`{}`

#### Returns[​](#returns-4 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

[TextSplitter](/docs/api/text_splitter/classes/TextSplitter).[createDocuments](/docs/api/text_splitter/classes/TextSplitter#createdocuments)

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:76](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/text_splitter.ts#L76)

### mergeSplits()[​](#mergesplits "Direct link to mergeSplits()")

> **mergeSplits**(`splits`: `string`\[\], `separator`: `string`): `Promise`<`string`\[\]\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`splits`

`string`\[\]

`separator`

`string`

#### Returns[​](#returns-5 "Direct link to Returns")

`Promise`<`string`\[\]\>

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

[TextSplitter](/docs/api/text_splitter/classes/TextSplitter).[mergeSplits](/docs/api/text_splitter/classes/TextSplitter#mergesplits)

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:162](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/text_splitter.ts#L162)

### splitDocuments()[​](#splitdocuments "Direct link to splitDocuments()")

> **splitDocuments**(`documents`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], `chunkHeaderOptions`: [`TextSplitterChunkHeaderOptions`](/docs/api/text_splitter/types/TextSplitterChunkHeaderOptions) = `{}`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`documents`

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

`chunkHeaderOptions`

[`TextSplitterChunkHeaderOptions`](/docs/api/text_splitter/types/TextSplitterChunkHeaderOptions)

#### Returns[​](#returns-6 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Inherited from[​](#inherited-from-15 "Direct link to Inherited from")

[TextSplitter](/docs/api/text_splitter/classes/TextSplitter).[splitDocuments](/docs/api/text_splitter/classes/TextSplitter#splitdocuments)

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:145](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/text_splitter.ts#L145)

### splitText()[​](#splittext "Direct link to splitText()")

> **splitText**(`text`: `string`): `Promise`<`string`\[\]\>

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`text`

`string`

#### Returns[​](#returns-7 "Direct link to Returns")

`Promise`<`string`\[\]\>

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[TextSplitter](/docs/api/text_splitter/classes/TextSplitter).[splitText](/docs/api/text_splitter/classes/TextSplitter#splittext)

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:316](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/text_splitter.ts#L316)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-8 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-16 "Direct link to Inherited from")

[TextSplitter](/docs/api/text_splitter/classes/TextSplitter).[toJSON](/docs/api/text_splitter/classes/TextSplitter#tojson)

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-9 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-17 "Direct link to Inherited from")

[TextSplitter](/docs/api/text_splitter/classes/TextSplitter).[toJSONNotImplemented](/docs/api/text_splitter/classes/TextSplitter#tojsonnotimplemented)

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)

### transformDocuments()[​](#transformdocuments "Direct link to transformDocuments()")

> **transformDocuments**(`documents`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], `chunkHeaderOptions`: [`TextSplitterChunkHeaderOptions`](/docs/api/text_splitter/types/TextSplitterChunkHeaderOptions) = `{}`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[​](#parameters-5 "Direct link to Parameters")

Parameter

Type

`documents`

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

`chunkHeaderOptions`

[`TextSplitterChunkHeaderOptions`](/docs/api/text_splitter/types/TextSplitterChunkHeaderOptions)

#### Returns[​](#returns-10 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Inherited from[​](#inherited-from-18 "Direct link to Inherited from")

[TextSplitter](/docs/api/text_splitter/classes/TextSplitter).[transformDocuments](/docs/api/text_splitter/classes/TextSplitter#transformdocuments)

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:49](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/text_splitter.ts#L49)

### fromLanguage()[​](#fromlanguage "Direct link to fromLanguage()")

> `Static` **fromLanguage**(`language`: "cpp" | "go" | "java" | "js" | "php" | "proto" | "python" | "rst" | "ruby" | "rust" | "scala" | "swift" | "markdown" | "latex" | "html" | "sol", `options`: `Partial`<[`RecursiveCharacterTextSplitterParams`](/docs/api/text_splitter/interfaces/RecursiveCharacterTextSplitterParams)\>): [`RecursiveCharacterTextSplitter`](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter)

#### Parameters[​](#parameters-6 "Direct link to Parameters")

Parameter

Type

`language`

"cpp" | "go" | "java" | "js" | "php" | "proto" | "python" | "rst" | "ruby" | "rust" | "scala" | "swift" | "markdown" | "latex" | "html" | "sol"

`options`

`Partial`<[`RecursiveCharacterTextSplitterParams`](/docs/api/text_splitter/interfaces/RecursiveCharacterTextSplitterParams)\>

#### Returns[​](#returns-11 "Direct link to Returns")

[`RecursiveCharacterTextSplitter`](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter)

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:320](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/text_splitter.ts#L320)

### getSeparatorsForLanguage()[​](#getseparatorsforlanguage "Direct link to getSeparatorsForLanguage()")

> `Static` **getSeparatorsForLanguage**(`language`: "cpp" | "go" | "java" | "js" | "php" | "proto" | "python" | "rst" | "ruby" | "rust" | "scala" | "swift" | "markdown" | "latex" | "html" | "sol"): `string`\[\]

#### Parameters[​](#parameters-7 "Direct link to Parameters")

Parameter

Type

`language`

"cpp" | "go" | "java" | "js" | "php" | "proto" | "python" | "rst" | "ruby" | "rust" | "scala" | "swift" | "markdown" | "latex" | "html" | "sol"

#### Returns[​](#returns-12 "Direct link to Returns")

`string`\[\]

#### Defined in[​](#defined-in-23 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:331](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/text_splitter.ts#L331)

### splitOnSeparator()[​](#splitonseparator "Direct link to splitOnSeparator()")

> `Protected` **splitOnSeparator**(`text`: `string`, `separator`: `string`): `string`\[\]

#### Parameters[​](#parameters-8 "Direct link to Parameters")

Parameter

Type

`text`

`string`

`separator`

`string`

#### Returns[​](#returns-13 "Direct link to Returns")

`string`\[\]

#### Inherited from[​](#inherited-from-19 "Direct link to Inherited from")

[TextSplitter](/docs/api/text_splitter/classes/TextSplitter).[splitOnSeparator](/docs/api/text_splitter/classes/TextSplitter#splitonseparator)

#### Defined in[​](#defined-in-24 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:58](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/text_splitter.ts#L58)