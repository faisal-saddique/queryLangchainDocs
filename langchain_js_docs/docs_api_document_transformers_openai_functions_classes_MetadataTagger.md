MetadataTagger
==============

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   `BaseDocumentTransformer`.**MetadataTagger**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new MetadataTagger**(`fields`: `object`): [`MetadataTagger`](/docs/api/document_transformers_openai_functions/classes/MetadataTagger)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields`

`object`

`fields.taggingChain`

[`BaseChain`](/docs/api/chains/classes/BaseChain)

#### Returns[​](#returns "Direct link to Returns")

[`MetadataTagger`](/docs/api/document_transformers_openai_functions/classes/MetadataTagger)

#### Overrides[​](#overrides "Direct link to Overrides")

BaseDocumentTransformer.constructor

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/document\_transformers/openai\_functions.ts:17](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_transformers/openai_functions.ts#L17)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

BaseDocumentTransformer.lc\_kwargs

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

BaseDocumentTransformer.lc\_namespace

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/schema/document.ts:15](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/document.ts#L15)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

BaseDocumentTransformer.lc\_serializable

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L55)

### taggingChain[​](#taggingchain "Direct link to taggingChain")

> `Protected` **taggingChain**: [`BaseChain`](/docs/api/chains/classes/BaseChain)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/document\_transformers/openai\_functions.ts:15](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_transformers/openai_functions.ts#L15)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-1 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

BaseDocumentTransformer.lc\_aliases

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

BaseDocumentTransformer.lc\_aliases

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

BaseDocumentTransformer.lc\_attributes

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

BaseDocumentTransformer.lc\_attributes

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

BaseDocumentTransformer.lc\_secrets

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

BaseDocumentTransformer.lc\_secrets

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-4 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

BaseDocumentTransformer.toJSON

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-5 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

BaseDocumentTransformer.toJSONNotImplemented

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)

### transformDocuments()[​](#transformdocuments "Direct link to transformDocuments()")

> **transformDocuments**(`documents`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`documents`

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

#### Returns[​](#returns-6 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Overrides[​](#overrides-1 "Direct link to Overrides")

BaseDocumentTransformer.transformDocuments

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/document\_transformers/openai\_functions.ts:32](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_transformers/openai_functions.ts#L32)