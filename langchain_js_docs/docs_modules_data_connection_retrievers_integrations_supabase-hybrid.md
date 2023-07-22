Supabase Hybrid Search
======================

Langchain supports hybrid search with a Supabase Postgres database. The hybrid search combines the postgres `pgvector` extension (similarity search) and Full-Text Search (keyword search) to retrieve documents. You can add documents via SupabaseVectorStore `addDocuments` function. SupabaseHybridKeyWordSearch accepts embedding, supabase client, number of results for similarity search, and number of results for keyword search as parameters. The `getRelevantDocuments` function produces a list of documents that has duplicates removed and is sorted by relevance score.

Setup[​](#setup "Direct link to Setup")
---------------------------------------

### Install the library with[​](#install-the-library-with "Direct link to Install the library with")

*   npm
*   Yarn
*   pnpm

    npm install -S @supabase/supabase-js

    yarn add @supabase/supabase-js

    pnpm add @supabase/supabase-js

### Create a table and search functions in your database[​](#create-a-table-and-search-functions-in-your-database "Direct link to Create a table and search functions in your database")

Run this in your database:

    -- Enable the pgvector extension to work with embedding vectorscreate extension vector;-- Create a table to store your documentscreate table documents (  id bigserial primary key,  content text, -- corresponds to Document.pageContent  metadata jsonb, -- corresponds to Document.metadata  embedding vector(1536) -- 1536 works for OpenAI embeddings, change if needed);-- Create a function to similarity search for documentscreate function match_documents (  query_embedding vector(1536),  match_count int DEFAULT null,  filter jsonb DEFAULT '{}') returns table (  id bigint,  content text,  metadata jsonb,  similarity float)language plpgsqlas $$#variable_conflict use_columnbegin  return query  select    id,    content,    metadata,    1 - (documents.embedding <=> query_embedding) as similarity  from documents  where metadata @> filter  order by documents.embedding <=> query_embedding  limit match_count;end;$$;-- Create a function to keyword search for documentscreate function kw_match_documents(query_text text, match_count int)returns table (id bigint, content text, metadata jsonb, similarity real)as $$beginreturn query executeformat('select id, content, metadata, ts_rank(to_tsvector(content), plainto_tsquery($1)) as similarityfrom documentswhere to_tsvector(content) @@ plainto_tsquery($1)order by similarity desclimit $2')using query_text, match_count;end;$$ language plpgsql;

Usage[​](#usage "Direct link to Usage")
---------------------------------------

    import { OpenAIEmbeddings } from "langchain/embeddings/openai";import { createClient } from "@supabase/supabase-js";import { SupabaseHybridSearch } from "langchain/retrievers/supabase";export const run = async () => {  const client = createClient(    process.env.SUPABASE_URL || "",    process.env.SUPABASE_PRIVATE_KEY || ""  );  const embeddings = new OpenAIEmbeddings();  const retriever = new SupabaseHybridSearch(embeddings, {    client,    //  Below are the defaults, expecting that you set up your supabase table and functions according to the guide above. Please change if necessary.    similarityK: 2,    keywordK: 2,    tableName: "documents",    similarityQueryName: "match_documents",    keywordQueryName: "kw_match_documents",  });  const results = await retriever.getRelevantDocuments("hello bye");  console.log(results);};

#### API Reference:

*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`
*   [SupabaseHybridSearch](/docs/api/retrievers_supabase/classes/SupabaseHybridSearch) from `langchain/retrievers/supabase`