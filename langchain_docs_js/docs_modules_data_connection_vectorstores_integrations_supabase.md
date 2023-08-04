Supabase
========

Langchain supports using Supabase Postgres database as a vector store, using the `pgvector` postgres extension. Refer to the [Supabase blog post](https://supabase.com/blog/openai-embeddings-postgres-vector) for more information.

Setup[](#setup "Direct link to Setup")
---------------------------------------

### Install the library with[](#install-the-library-with "Direct link to Install the library with")

*   npm
*   Yarn
*   pnpm

    npm install -S @supabase/supabase-js

    yarn add @supabase/supabase-js

    pnpm add @supabase/supabase-js

### Create a table and search function in your database[](#create-a-table-and-search-function-in-your-database "Direct link to Create a table and search function in your database")

Run this in your database:

    -- Enable the pgvector extension to work with embedding vectorscreate extension vector;-- Create a table to store your documentscreate table documents (  id bigserial primary key,  content text, -- corresponds to Document.pageContent  metadata jsonb, -- corresponds to Document.metadata  embedding vector(1536) -- 1536 works for OpenAI embeddings, change if needed);-- Create a function to search for documentscreate function match_documents (  query_embedding vector(1536),  match_count int DEFAULT null,  filter jsonb DEFAULT '{}') returns table (  id bigint,  content text,  metadata jsonb,  similarity float)language plpgsqlas $$#variable_conflict use_columnbegin  return query  select    id,    content,    metadata,    1 - (documents.embedding <=> query_embedding) as similarity  from documents  where metadata @> filter  order by documents.embedding <=> query_embedding  limit match_count;end;$$;

Usage[](#usage "Direct link to Usage")
---------------------------------------

### Standard Usage[](#standard-usage "Direct link to Standard Usage")

The below example shows how to perform a basic similarity search with Supabase:

    import { SupabaseVectorStore } from "langchain/vectorstores/supabase";import { OpenAIEmbeddings } from "langchain/embeddings/openai";import { createClient } from "@supabase/supabase-js";// First, follow set-up instructions at// https://js.langchain.com/docs/modules/indexes/vector_stores/integrations/supabaseconst privateKey = process.env.SUPABASE_PRIVATE_KEY;if (!privateKey) throw new Error(`Expected env var SUPABASE_PRIVATE_KEY`);const url = process.env.SUPABASE_URL;if (!url) throw new Error(`Expected env var SUPABASE_URL`);export const run = async () => {  const client = createClient(url, privateKey);  const vectorStore = await SupabaseVectorStore.fromTexts(    ["Hello world", "Bye bye", "What's this?"],    [{ id: 2 }, { id: 1 }, { id: 3 }],    new OpenAIEmbeddings(),    {      client,      tableName: "documents",      queryName: "match_documents",    }  );  const resultOne = await vectorStore.similaritySearch("Hello world", 1);  console.log(resultOne);};

#### API Reference:

*   [SupabaseVectorStore](/docs/api/vectorstores_supabase/classes/SupabaseVectorStore) from `langchain/vectorstores/supabase`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`

### Metadata Filtering[](#metadata-filtering "Direct link to Metadata Filtering")

Given the above `match_documents` Postgres function, you can also pass a filter parameter to only documents with a specific metadata field value. This filter parameter is a JSON object, and the `match_documents` function will use the Postgres JSONB Containment operator `@>` to filter documents by the metadata field values you specify. See details on the [Postgres JSONB Containment operator](https://www.postgresql.org/docs/current/datatype-json.html#JSON-CONTAINMENT) for more information.

**Note:** If you've previously been using `SupabaseVectorStore`, you may need to drop and recreate the `match_documents` function per the updated SQL above to use this functionality.

    import { SupabaseVectorStore } from "langchain/vectorstores/supabase";import { OpenAIEmbeddings } from "langchain/embeddings/openai";import { createClient } from "@supabase/supabase-js";// First, follow set-up instructions at// https://js.langchain.com/docs/modules/indexes/vector_stores/integrations/supabaseconst privateKey = process.env.SUPABASE_PRIVATE_KEY;if (!privateKey) throw new Error(`Expected env var SUPABASE_PRIVATE_KEY`);const url = process.env.SUPABASE_URL;if (!url) throw new Error(`Expected env var SUPABASE_URL`);export const run = async () => {  const client = createClient(url, privateKey);  const vectorStore = await SupabaseVectorStore.fromTexts(    ["Hello world", "Hello world", "Hello world"],    [{ user_id: 2 }, { user_id: 1 }, { user_id: 3 }],    new OpenAIEmbeddings(),    {      client,      tableName: "documents",      queryName: "match_documents",    }  );  const result = await vectorStore.similaritySearch("Hello world", 1, {    user_id: 3,  });  console.log(result);};

#### API Reference:

*   [SupabaseVectorStore](/docs/api/vectorstores_supabase/classes/SupabaseVectorStore) from `langchain/vectorstores/supabase`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`

### Metadata Query Builder Filtering[](#metadata-query-builder-filtering "Direct link to Metadata Query Builder Filtering")

You can also use query builder-style filtering similar to how [the Supabase JavaScript library works](https://supabase.com/docs/reference/javascript/using-filters) instead of passing an object. Note that since most of the filter properties are in the metadata column, you need to use arrow operators (`->` for integer or `->>` for text) as defined in [Postgrest API documentation](https://postgrest.org/en/stable/references/api/tables_views.html?highlight=operators#json-columns) and specify the data type of the property (e.g. the column should look something like `metadata->some_int_value::int`).

    import {  SupabaseFilterRPCCall,  SupabaseVectorStore,} from "langchain/vectorstores/supabase";import { OpenAIEmbeddings } from "langchain/embeddings/openai";import { createClient } from "@supabase/supabase-js";// First, follow set-up instructions at// https://js.langchain.com/docs/modules/indexes/vector_stores/integrations/supabaseconst privateKey = process.env.SUPABASE_PRIVATE_KEY;if (!privateKey) throw new Error(`Expected env var SUPABASE_PRIVATE_KEY`);const url = process.env.SUPABASE_URL;if (!url) throw new Error(`Expected env var SUPABASE_URL`);export const run = async () => {  const client = createClient(url, privateKey);  const embeddings = new OpenAIEmbeddings();  const store = new SupabaseVectorStore(embeddings, {    client,    tableName: "documents",  });  const docs = [    {      pageContent:        "This is a long text, but it actually means something because vector database does not understand Lorem Ipsum. So I would need to expand upon the notion of quantum fluff, a theorectical concept where subatomic particles coalesce to form transient multidimensional spaces. Yet, this abstraction holds no real-world application or comprehensible meaning, reflecting a cosmic puzzle.",      metadata: { b: 1, c: 10, stuff: "right" },    },    {      pageContent:        "This is a long text, but it actually means something because vector database does not understand Lorem Ipsum. So I would need to proceed by discussing the echo of virtual tweets in the binary corridors of the digital universe. Each tweet, like a pixelated canary, hums in an unseen frequency, a fascinatingly perplexing phenomenon that, while conjuring vivid imagery, lacks any concrete implication or real-world relevance, portraying a paradox of multidimensional spaces in the age of cyber folklore.",      metadata: { b: 2, c: 9, stuff: "right" },    },    { pageContent: "hello", metadata: { b: 1, c: 9, stuff: "right" } },    { pageContent: "hello", metadata: { b: 1, c: 9, stuff: "wrong" } },    { pageContent: "hi", metadata: { b: 2, c: 8, stuff: "right" } },    { pageContent: "bye", metadata: { b: 3, c: 7, stuff: "right" } },    { pageContent: "what's this", metadata: { b: 4, c: 6, stuff: "right" } },  ];  // Also supports an additional {ids: []} parameter for upsertion  await store.addDocuments(docs);  const funcFilterA: SupabaseFilterRPCCall = (rpc) =>    rpc      .filter("metadata->b::int", "lt", 3)      .filter("metadata->c::int", "gt", 7)      .textSearch("content", `'multidimensional' & 'spaces'`, {        config: "english",      });  const resultA = await store.similaritySearch("quantum", 4, funcFilterA);  const funcFilterB: SupabaseFilterRPCCall = (rpc) =>    rpc      .filter("metadata->b::int", "lt", 3)      .filter("metadata->c::int", "gt", 7)      .filter("metadata->>stuff", "eq", "right");  const resultB = await store.similaritySearch("hello", 2, funcFilterB);  console.log(resultA, resultB);};

#### API Reference:

*   [SupabaseFilterRPCCall](/docs/api/vectorstores_supabase/types/SupabaseFilterRPCCall) from `langchain/vectorstores/supabase`
*   [SupabaseVectorStore](/docs/api/vectorstores_supabase/classes/SupabaseVectorStore) from `langchain/vectorstores/supabase`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`

### Document deletion[](#document-deletion "Direct link to Document deletion")

    import { SupabaseVectorStore } from "langchain/vectorstores/supabase";import { OpenAIEmbeddings } from "langchain/embeddings/openai";import { createClient } from "@supabase/supabase-js";// First, follow set-up instructions at// https://js.langchain.com/docs/modules/indexes/vector_stores/integrations/supabaseconst privateKey = process.env.SUPABASE_PRIVATE_KEY;if (!privateKey) throw new Error(`Expected env var SUPABASE_PRIVATE_KEY`);const url = process.env.SUPABASE_URL;if (!url) throw new Error(`Expected env var SUPABASE_URL`);export const run = async () => {  const client = createClient(url, privateKey);  const embeddings = new OpenAIEmbeddings();  const store = new SupabaseVectorStore(embeddings, {    client,    tableName: "documents",  });  const docs = [    { pageContent: "hello", metadata: { b: 1, c: 9, stuff: "right" } },    { pageContent: "hello", metadata: { b: 1, c: 9, stuff: "wrong" } },  ];  // Also takes an additional {ids: []} parameter for upsertion  const ids = await store.addDocuments(docs);  const resultA = await store.similaritySearch("hello", 2);  console.log(resultA);  /*    [      Document { pageContent: "hello", metadata: { b: 1, c: 9, stuff: "right" } },      Document { pageContent: "hello", metadata: { b: 1, c: 9, stuff: "wrong" } },    ]  */  await store.delete({ ids });  const resultB = await store.similaritySearch("hello", 2);  console.log(resultB);  /*    []  */};

#### API Reference:

*   [SupabaseVectorStore](/docs/api/vectorstores_supabase/classes/SupabaseVectorStore) from `langchain/vectorstores/supabase`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`