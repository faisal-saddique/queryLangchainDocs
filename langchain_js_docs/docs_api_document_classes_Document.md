Document<Metadata\>
===================

Interface for interacting with a document.

Type parameters[​](#type-parameters "Direct link to Type parameters")
---------------------------------------------------------------------

*   `Metadata` _extends_ `Record`<`string`, `any`\> = `Record`<`string`, `any`\>

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`TypeORMVectorStoreDocument`](/docs/api/vectorstores_typeorm/classes/TypeORMVectorStoreDocument)

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   [`DocumentInput`](/docs/api/document/interfaces/DocumentInput)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new Document**<Metadata\>(`fields`: [`DocumentInput`](/docs/api/document/interfaces/DocumentInput)<`Metadata`\>): [`Document`](/docs/api/document/classes/Document)<`Metadata`\>

#### Type parameters[​](#type-parameters-1 "Direct link to Type parameters")

*   `Metadata` _extends_ `Record`<`string`, `any`\> = `Record`<`string`, `any`\>

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields`

[`DocumentInput`](/docs/api/document/interfaces/DocumentInput)<`Metadata`\>

#### Returns[​](#returns "Direct link to Returns")

[`Document`](/docs/api/document/classes/Document)<`Metadata`\>

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/document.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document.ts#L22)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### metadata[​](#metadata "Direct link to metadata")

> **metadata**: `Metadata`

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

[DocumentInput](/docs/api/document/interfaces/DocumentInput).[metadata](/docs/api/document/interfaces/DocumentInput#metadata)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/document.ts:20](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document.ts#L20)

### pageContent[​](#pagecontent "Direct link to pageContent")

> **pageContent**: `string`

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

[DocumentInput](/docs/api/document/interfaces/DocumentInput).[pageContent](/docs/api/document/interfaces/DocumentInput#pagecontent)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/document.ts:18](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document.ts#L18)