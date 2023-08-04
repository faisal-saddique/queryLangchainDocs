TypeORMVectorStoreDocument
==========================

Interface for interacting with a document.

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`Document`](/docs/api/document/classes/Document).**TypeORMVectorStoreDocument**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new TypeORMVectorStoreDocument**(`fields`: [`DocumentInput`](/docs/api/document/interfaces/DocumentInput)<`Record`<`string`, `any`\>\>): [`TypeORMVectorStoreDocument`](/docs/api/vectorstores_typeorm/classes/TypeORMVectorStoreDocument)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`fields`

[`DocumentInput`](/docs/api/document/interfaces/DocumentInput)<`Record`<`string`, `any`\>\>

#### Returns[](#returns "Direct link to Returns")

[`TypeORMVectorStoreDocument`](/docs/api/vectorstores_typeorm/classes/TypeORMVectorStoreDocument)

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[Document](/docs/api/document/classes/Document).[constructor](/docs/api/document/classes/Document#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/document.ts:22](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document.ts#L22)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### embedding[](#embedding "Direct link to embedding")

> **embedding**: `string`

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/vectorstores/typeorm.ts:16](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/typeorm.ts#L16)

### metadata[](#metadata "Direct link to metadata")

> **metadata**: `Record`<`string`, `any`\>

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[Document](/docs/api/document/classes/Document).[metadata](/docs/api/document/classes/Document#metadata)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/document.ts:20](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document.ts#L20)

### pageContent[](#pagecontent "Direct link to pageContent")

> **pageContent**: `string`

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[Document](/docs/api/document/classes/Document).[pageContent](/docs/api/document/classes/Document#pagecontent)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/document.ts:18](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document.ts#L18)

### id?[](#id "Direct link to id?")

> **id**: `string`

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/vectorstores/typeorm.ts:18](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/vectorstores/typeorm.ts#L18)