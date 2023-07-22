SupabaseLibArgs
===============

Base Index class. All indexes should extend this class.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseRetrieverInput`](/docs/api/schema_retriever/interfaces/BaseRetrieverInput).**SupabaseLibArgs**

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### client[​](#client "Direct link to client")

> **client**: `default`<`any`, "public", `any`\>

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/retrievers/supabase.ts:30](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/supabase.ts#L30)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BaseRetrieverInput](/docs/api/schema_retriever/interfaces/BaseRetrieverInput).[callbacks](/docs/api/schema_retriever/interfaces/BaseRetrieverInput#callbacks)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:16](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L16)

### keywordK?[​](#keywordk "Direct link to keywordK?")

> **keywordK**: `number`

The number of documents to return from the keyword search. Defaults to 2.

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/retrievers/supabase.ts:50](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/supabase.ts#L50)

### keywordQueryName?[​](#keywordqueryname "Direct link to keywordQueryName?")

> **keywordQueryName**: `string`

The name of the Keyword search function on Supabase. Defaults to "kw\_match\_documents".

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/retrievers/supabase.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/supabase.ts#L42)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[BaseRetrieverInput](/docs/api/schema_retriever/interfaces/BaseRetrieverInput).[metadata](/docs/api/schema_retriever/interfaces/BaseRetrieverInput#metadata)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:18](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L18)

### similarityK?[​](#similarityk "Direct link to similarityK?")

> **similarityK**: `number`

The number of documents to return from the similarity search. Defaults to 2.

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/retrievers/supabase.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/supabase.ts#L46)

### similarityQueryName?[​](#similarityqueryname "Direct link to similarityQueryName?")

> **similarityQueryName**: `string`

The name of the Similarity search function on Supabase. Defaults to "match\_documents".

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/retrievers/supabase.ts:38](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/supabase.ts#L38)

### tableName?[​](#tablename "Direct link to tableName?")

> **tableName**: `string`

The table name on Supabase. Defaults to "documents".

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/retrievers/supabase.ts:34](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/supabase.ts#L34)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[BaseRetrieverInput](/docs/api/schema_retriever/interfaces/BaseRetrieverInput).[tags](/docs/api/schema_retriever/interfaces/BaseRetrieverInput#tags)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:17](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L17)

### verbose?[​](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[BaseRetrieverInput](/docs/api/schema_retriever/interfaces/BaseRetrieverInput).[verbose](/docs/api/schema_retriever/interfaces/BaseRetrieverInput#verbose)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:19](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L19)