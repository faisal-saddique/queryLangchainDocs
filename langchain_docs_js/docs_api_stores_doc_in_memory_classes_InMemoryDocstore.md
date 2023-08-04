InMemoryDocstore
================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`Docstore`](/docs/api/schema/classes/Docstore).**InMemoryDocstore**

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new InMemoryDocstore**(`docs`?: `Map`<`string`, [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\>): [`InMemoryDocstore`](/docs/api/stores_doc_in_memory/classes/InMemoryDocstore)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`docs?`

`Map`<`string`, [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\>

#### Returns[](#returns "Direct link to Returns")

[`InMemoryDocstore`](/docs/api/stores_doc_in_memory/classes/InMemoryDocstore)

#### Overrides[](#overrides "Direct link to Overrides")

[Docstore](/docs/api/schema/classes/Docstore).[constructor](/docs/api/schema/classes/Docstore#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/stores/doc/in\_memory.ts:7](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/stores/doc/in_memory.ts#L7)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### \_docs[](#_docs "Direct link to _docs")

> **\_docs**: `Map`<`string`, [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\>

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/stores/doc/in\_memory.ts:5](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/stores/doc/in_memory.ts#L5)

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

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/stores/doc/in\_memory.ts:21](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/stores/doc/in_memory.ts#L21)

### search()[](#search "Direct link to search()")

> **search**(`search`: `string`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`search`

`string`

#### Returns[](#returns-2 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\>

#### Overrides[](#overrides-2 "Direct link to Overrides")

[Docstore](/docs/api/schema/classes/Docstore).[search](/docs/api/schema/classes/Docstore#search)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/stores/doc/in\_memory.ts:12](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/stores/doc/in_memory.ts#L12)