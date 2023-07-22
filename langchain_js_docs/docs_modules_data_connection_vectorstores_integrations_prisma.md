Prisma
======

For augmenting existing models in PostgreSQL database with vector search, Langchain supports using [Prisma](https://www.prisma.io/) together with PostgreSQL and [`pgvector`](https://github.com/pgvector/pgvector) Postgres extension.

Setup[​](#setup "Direct link to Setup")
---------------------------------------

### Setup database instance with Supabase[​](#setup-database-instance-with-supabase "Direct link to Setup database instance with Supabase")

Refer to the [Prisma and Supabase integration guide](https://supabase.com/docs/guides/integrations/prisma) to setup a new database instance with Supabase and Prisma.

### Install Prisma[​](#install-prisma "Direct link to Install Prisma")

*   npm
*   Yarn
*   pnpm

    npm install prisma

    yarn add prisma

    pnpm add prisma

### Setup `pgvector` self hosted instance with `docker-compose`[​](#setup-pgvector-self-hosted-instance-with-docker-compose "Direct link to setup-pgvector-self-hosted-instance-with-docker-compose")

`pgvector` provides a prebuilt Docker image that can be used to quickly setup a self-hosted Postgres instance.

    services:  db:    image: ankane/pgvector    ports:      - 5432:5432    volumes:      - db:/var/lib/postgresql/data    environment:      - POSTGRES_PASSWORD=      - POSTGRES_USER=      - POSTGRES_DB=volumes:  db:

### Create a new schema[​](#create-a-new-schema "Direct link to Create a new schema")

Assuming you haven't created a schema yet, create a new model with a `vector` field of type `Unsupported("vector")`:

    model Document {  id      String                 @id @default(cuid())  content String  vector  Unsupported("vector")?}

Afterwards, create a new migration with `--create-only` to avoid running the migration directly.

*   npm
*   Yarn
*   pnpm

    npx prisma migrate dev --create-only

    npx prisma migrate dev --create-only

    npx prisma migrate dev --create-only

Add the following line to the newly created migration to enable `pgvector` extension if it hasn't been enabled yet:

    CREATE EXTENSION IF NOT EXISTS vector;

Run the migration afterwards:

*   npm
*   Yarn
*   pnpm

    npx prisma migrate dev

    npx prisma migrate dev

    npx prisma migrate dev

Usage[​](#usage "Direct link to Usage")
---------------------------------------

danger

Table names and column names (in fields such as `tableName`, `vectorColumnName`, `columns` and `filter`) are passed into SQL queries directly without parametrisation. These fields must be sanitized beforehand to avoid SQL injection.

    import { PrismaVectorStore } from "langchain/vectorstores/prisma";import { OpenAIEmbeddings } from "langchain/embeddings/openai";import { PrismaClient, Prisma, Document } from "@prisma/client";export const run = async () => {  const db = new PrismaClient();  // Use the `withModel` method to get proper type hints for `metadata` field:  const vectorStore = PrismaVectorStore.withModel<Document>(db).create(    new OpenAIEmbeddings(),    {      prisma: Prisma,      tableName: "Document",      vectorColumnName: "vector",      columns: {        id: PrismaVectorStore.IdColumn,        content: PrismaVectorStore.ContentColumn,      },    }  );  const texts = ["Hello world", "Bye bye", "What's this?"];  await vectorStore.addModels(    await db.$transaction(      texts.map((content) => db.document.create({ data: { content } }))    )  );  const resultOne = await vectorStore.similaritySearch("Hello world", 1);  console.log(resultOne);  // create an instance with default filter  const vectorStore2 = PrismaVectorStore.withModel<Document>(db).create(    new OpenAIEmbeddings(),    {      prisma: Prisma,      tableName: "Document",      vectorColumnName: "vector",      columns: {        id: PrismaVectorStore.IdColumn,        content: PrismaVectorStore.ContentColumn,      },      filter: {        content: {          equals: "default",        },      },    }  );  await vectorStore2.addModels(    await db.$transaction(      texts.map((content) => db.document.create({ data: { content } }))    )  );  // Use the default filter a.k.a {"content": "default"}  const resultTwo = await vectorStore.similaritySearch("Hello world", 1);  console.log(resultTwo);  // Override the local filter  const resultThree = await vectorStore.similaritySearchWithScore(    "Hello world",    1,    { content: { equals: "different_content" } }  );  console.log(resultThree);};

#### API Reference:

*   [PrismaVectorStore](/docs/api/vectorstores_prisma/classes/PrismaVectorStore) from `langchain/vectorstores/prisma`
*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`

The samples above uses the following schema:

    // This is your Prisma schema file,// learn more about it in the docs: https://pris.ly/d/prisma-schemagenerator client {  provider = "prisma-client-js"}datasource db {  provider = "postgresql"  url      = env("DATABASE_URL")}model Document {  id        String                 @id @default(cuid())  content   String  namespace String?                @default("default")  vector    Unsupported("vector")?}

#### API Reference:

You can remove `namespace` if you don't need it.