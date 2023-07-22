TypesenseConfig
===============

Typesense vector store configuration.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   `AsyncCallerParams`.**TypesenseConfig**

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### schemaName[​](#schemaname "Direct link to schemaName")

> **schemaName**: `string`

Typesense schema name in which documents will be stored and searched.

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/vectorstores/typesense.ts:28](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/typesense.ts#L28)

### typesenseClient[​](#typesenseclient "Direct link to typesenseClient")

> **typesenseClient**: `default`

Typesense client.

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/vectorstores/typesense.ts:24](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/typesense.ts#L24)

### columnNames?[​](#columnnames "Direct link to columnNames?")

> **columnNames**: `object`

Column names.

#### Type declaration[​](#type-declaration "Direct link to Type declaration")

Member

Type

Description

`metadataColumnNames`?

`string`\[\]

Metadata column names.  
  
`Default`  
  
`ts<br />[]<br />`

`pageContent`?

`string`

Page content column name.  
  
`Default`  
  
`ts<br />'text'<br />`

`vector`?

`string`

Vector column name.  
  
`Default`  
  
`ts<br />'vec'<br />`

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/vectorstores/typesense.ts:37](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/typesense.ts#L37)

### maxConcurrency?[​](#maxconcurrency "Direct link to maxConcurrency?")

> **maxConcurrency**: `number`

The maximum number of concurrent calls that can be made. Defaults to `Infinity`, which means no limit.

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

AsyncCallerParams.maxConcurrency

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:21](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/util/async_caller.ts#L21)

### maxRetries?[​](#maxretries "Direct link to maxRetries?")

> **maxRetries**: `number`

The maximum number of retries that can be made for a single call, with an exponential backoff between each attempt. Defaults to 6.

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

AsyncCallerParams.maxRetries

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:26](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/util/async_caller.ts#L26)

### searchParams?[​](#searchparams "Direct link to searchParams?")

> **searchParams**: `MultiSearchRequestSchema`

Typesense search parameters.

#### Default[​](#default "Direct link to Default")

    { q: '*', per_page: 5, query_by: '' }

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/vectorstores/typesense.ts:33](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/typesense.ts#L33)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### import()?[​](#import "Direct link to import()?")

Replace default import function. Default import function will update documents if there is a document with the same id.

> `Optional` **import**<T\>(`data`: `T`\[\], `collectionName`: `string`): `Promise`<`void`\>

#### Type parameters[​](#type-parameters "Direct link to Type parameters")

*   `T` _extends_ `Record`<`string`, `unknown`\> = `Record`<`string`, `unknown`\>

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`data`

`T`\[\]

`collectionName`

`string`

#### Returns[​](#returns "Direct link to Returns")

`Promise`<`void`\>

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/vectorstores/typesense.ts:60](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/vectorstores/typesense.ts#L60)