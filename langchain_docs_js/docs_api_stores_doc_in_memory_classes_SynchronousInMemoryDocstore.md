SynchronousInMemoryDocstore
===========================

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new SynchronousInMemoryDocstore**(`docs`?: `Map`<`string`, [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\>): [`SynchronousInMemoryDocstore`](/docs/api/stores_doc_in_memory/classes/SynchronousInMemoryDocstore)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`docs?`

`Map`<`string`, [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\>

#### Returns[](#returns "Direct link to Returns")

[`SynchronousInMemoryDocstore`](/docs/api/stores_doc_in_memory/classes/SynchronousInMemoryDocstore)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/stores/doc/in\_memory.ts:38](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/stores/doc/in_memory.ts#L38)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### \_docs[](#_docs "Direct link to _docs")

> **\_docs**: `Map`<`string`, [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\>

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/stores/doc/in\_memory.ts:36](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/stores/doc/in_memory.ts#L36)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### add()[](#add "Direct link to add()")

> **add**(`texts`: `Record`<`string`, [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\>): `void`

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`texts`

`Record`<`string`, [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\>

#### Returns[](#returns-1 "Direct link to Returns")

`void`

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/stores/doc/in\_memory.ts:51](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/stores/doc/in_memory.ts#L51)

### search()[](#search "Direct link to search()")

> **search**(`search`: `string`): [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`search`

`string`

#### Returns[](#returns-2 "Direct link to Returns")

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/stores/doc/in\_memory.ts:42](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/stores/doc/in_memory.ts#L42)