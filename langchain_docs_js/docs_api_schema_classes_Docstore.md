Docstore
========

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`InMemoryDocstore`](/docs/api/stores_doc_in_memory/classes/InMemoryDocstore)
*   [`GoogleCloudStorageDocstore`](/docs/api/stores_doc_gcs/classes/GoogleCloudStorageDocstore)

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new Docstore**(): [`Docstore`](/docs/api/schema/classes/Docstore)

#### Returns[](#returns "Direct link to Returns")

[`Docstore`](/docs/api/schema/classes/Docstore)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### add()[](#add "Direct link to add()")

> `Abstract` **add**(`texts`: `Record`<`string`, [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\>): `Promise`<`void`\>

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`texts`

`Record`<`string`, [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\>

#### Returns[](#returns-1 "Direct link to Returns")

`Promise`<`void`\>

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/schema/index.ts:507](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/index.ts#L507)

### search()[](#search "Direct link to search()")

> `Abstract` **search**(`search`: `string`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`search`

`string`

#### Returns[](#returns-2 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\>

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/schema/index.ts:505](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/index.ts#L505)