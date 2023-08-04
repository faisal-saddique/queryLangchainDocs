GoogleCloudStorageDocstore
==========================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`Docstore`](/docs/api/schema/classes/Docstore).**GoogleCloudStorageDocstore**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new GoogleCloudStorageDocstore**(`config`: [`GoogleCloudStorageDocstoreConfiguration`](/docs/api/stores_doc_gcs/interfaces/GoogleCloudStorageDocstoreConfiguration)): [`GoogleCloudStorageDocstore`](/docs/api/stores_doc_gcs/classes/GoogleCloudStorageDocstore)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`config`

[`GoogleCloudStorageDocstoreConfiguration`](/docs/api/stores_doc_gcs/interfaces/GoogleCloudStorageDocstoreConfiguration)

#### Returns[](#returns "Direct link to Returns")

[`GoogleCloudStorageDocstore`](/docs/api/stores_doc_gcs/classes/GoogleCloudStorageDocstore)

#### Overrides[](#overrides "Direct link to Overrides")

[Docstore](/docs/api/schema/classes/Docstore).[constructor](/docs/api/schema/classes/Docstore#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/stores/doc/gcs.ts:24](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/stores/doc/gcs.ts#L24)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### bucket[](#bucket "Direct link to bucket")

> **bucket**: `string`

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/stores/doc/gcs.ts:18](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/stores/doc/gcs.ts#L18)

### prefix[](#prefix "Direct link to prefix")

> **prefix**: `string` = `""`

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/stores/doc/gcs.ts:20](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/stores/doc/gcs.ts#L20)

### storage[](#storage "Direct link to storage")

> **storage**: `Storage`

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/stores/doc/gcs.ts:22](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/stores/doc/gcs.ts#L22)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### add()[](#add "Direct link to add()")

> **add**(`texts`: `Record`<`string`, [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\>): `Promise`<`void`\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`texts`

`Record`<`string`, [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\>

#### Returns[](#returns-1 "Direct link to Returns")

`Promise`<`void`\>

#### Overrides[](#overrides-1 "Direct link to Overrides")

[Docstore](/docs/api/schema/classes/Docstore).[add](/docs/api/schema/classes/Docstore#add)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/stores/doc/gcs.ts:50](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/stores/doc/gcs.ts#L50)

### addDocument()[](#adddocument "Direct link to addDocument()")

> **addDocument**(`name`: `string`, `document`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>): `Promise`<`void`\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`name`

`string`

`document`

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>

#### Returns[](#returns-2 "Direct link to Returns")

`Promise`<`void`\>

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/stores/doc/gcs.ts:56](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/stores/doc/gcs.ts#L56)

### search()[](#search "Direct link to search()")

> **search**(`search`: `string`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\>

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

`search`

`string`

#### Returns[](#returns-3 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\>

#### Overrides[](#overrides-2 "Direct link to Overrides")

[Docstore](/docs/api/schema/classes/Docstore).[search](/docs/api/schema/classes/Docstore#search)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/stores/doc/gcs.ts:33](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/stores/doc/gcs.ts#L33)