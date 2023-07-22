TypeORM
=======

To enable vector search in a generic PostgreSQL database, LangChainJS supports using [TypeORM](https://typeorm.io/) with the [`pgvector`](https://github.com/pgvector/pgvector) Postgres extension.

Setup[​](#setup "Direct link to Setup")
---------------------------------------

To work with TypeORM, you need to install the `typeorm` and `pg` packages:

*   npm
*   Yarn
*   pnpm

    npm install typeorm

    yarn add typeorm

    pnpm add typeorm

*   npm
*   Yarn
*   pnpm

    npm install pg

    yarn add pg

    pnpm add pg

### Setup a `pgvector` self hosted instance with `docker-compose`[​](#setup-a-pgvector-self-hosted-instance-with-docker-compose "Direct link to setup-a-pgvector-self-hosted-instance-with-docker-compose")

`pgvector` provides a prebuilt Docker image that can be used to quickly setup a self-hosted Postgres instance. Create a file below named `docker-compose.yml`:

    services:  db:    image: ankane/pgvector    ports:      - 5432:5432    volumes:      - ./data:/var/lib/postgresql/data    environment:      - POSTGRES_PASSWORD=ChangeMe      - POSTGRES_USER=myuser      - POSTGRES_DB=api

#### API Reference:

And then in the same directory, run `docker compose up` to start the container.

You can find more information on how to setup `pgvector` in the [official repository](https://github.com/pgvector/pgvector).

Usage[​](#usage "Direct link to Usage")
---------------------------------------

One complete example of using `TypeORMVectorStore` is the following:

    import { DataSourceOptions } from "typeorm";import { OpenAIEmbeddings } from "langchain/embeddings/openai";import { TypeORMVectorStore } from "langchain/vectorstores/typeorm";// First, follow set-up instructions at// https://js.langchain.com/docs/modules/indexes/vector_stores/integrations/typeormexport const run = async () => {  const args = {    postgresConnectionOptions: {      type: "postgres",      host: "localhost",      port: 5432,      username: "myuser",      password: "ChangeMe",      database: "api",    } as DataSourceOptions,  };  const typeormVectorStore = await TypeORMVectorStore.fromDataSource(    new OpenAIEmbeddings(),    args  );  await typeormVectorStore.ensureTableInDatabase();  await typeormVectorStore.addDocuments([    { pageContent: "what's this", metadata: { a: 2 } },    { pageContent: "Cat drinks milk", metadata: { a: 1 } },  ]);  const results = await typeormVectorStore.similaritySearch("hello", 2);  console.log(results);};

#### API Reference:

*   [OpenAIEmbeddings](/docs/api/embeddings_openai/classes/OpenAIEmbeddings) from `langchain/embeddings/openai`
*   [TypeORMVectorStore](/docs/api/vectorstores_typeorm/classes/TypeORMVectorStore) from `langchain/vectorstores/typeorm`