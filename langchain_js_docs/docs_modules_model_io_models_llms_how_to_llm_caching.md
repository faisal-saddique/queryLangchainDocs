Caching
=======

LangChain provides an optional caching layer for LLMs. This is useful for two reasons:

It can save you money by reducing the number of API calls you make to the LLM provider, if you're often requesting the same completion multiple times. It can speed up your application by reducing the number of API calls you make to the LLM provider.

    import { OpenAI } from "langchain/llms/openai";// To make the caching really obvious, lets use a slower model.const model = new OpenAI({  modelName: "text-davinci-002",  cache: true,  n: 2,  bestOf: 2});

In Memory Cache[​](#in-memory-cache "Direct link to In Memory Cache")
---------------------------------------------------------------------

The default cache is stored in-memory. This means that if you restart your application, the cache will be cleared.

    // The first time, it is not yet in cache, so it should take longerconst res = await model.predict("Tell me a joke");console.log(res);/*  CPU times: user 35.9 ms, sys: 28.6 ms, total: 64.6 ms  Wall time: 4.83 s  "\n\nWhy did the chicken cross the road?\n\nTo get to the other side."*/

    // The second time it is, so it goes fasterconst res2 = await model.predict("Tell me a joke");console.log(res2);/*  CPU times: user 238 µs, sys: 143 µs, total: 381 µs  Wall time: 1.76 ms  "\n\nWhy did the chicken cross the road?\n\nTo get to the other side."*/

Caching with Momento[​](#caching-with-momento "Direct link to Caching with Momento")
------------------------------------------------------------------------------------

LangChain also provides a Momento-based cache. [Momento](https://gomomento.com) is a distributed, serverless cache that requires zero setup or infrastructure maintenance. To use it, you'll need to install the `@gomomento/sdk` package:

    npm install @gomomento/sdk

Next you'll need to sign up and create an API key. Once you've done that, pass a `cache` option when you instantiate the LLM like this:

    import { OpenAI } from "langchain/llms/openai";import { MomentoCache } from "langchain/cache/momento";import {  CacheClient,  Configurations,  CredentialProvider,} from "@gomomento/sdk";// See https://github.com/momentohq/client-sdk-javascript for connection optionsconst client = new CacheClient({  configuration: Configurations.Laptop.v1(),  credentialProvider: CredentialProvider.fromEnvironmentVariable({    environmentVariableName: "MOMENTO_AUTH_TOKEN",  }),  defaultTtlSeconds: 60 * 60 * 24,});const cache = await MomentoCache.fromProps({  client,  cacheName: "langchain",});const model = new OpenAI({ cache });

#### API Reference:

*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [MomentoCache](/docs/api/cache_momento/classes/MomentoCache) from `langchain/cache/momento`

Caching with Redis[​](#caching-with-redis "Direct link to Caching with Redis")
------------------------------------------------------------------------------

LangChain also provides a Redis-based cache. This is useful if you want to share the cache across multiple processes or servers. To use it, you'll need to install the `redis` package:

    npm install redis

Then, you can pass a `cache` option when you instantiate the LLM. For example:

    import { OpenAI } from "langchain/llms/openai";import { RedisCache } from "langchain/cache/redis";import { createClient } from "redis";// See https://github.com/redis/node-redis for connection optionsconst client = createClient();const cache = new RedisCache(client);const model = new OpenAI({ cache });

Caching with Upstash Redis[​](#caching-with-upstash-redis "Direct link to Caching with Upstash Redis")
------------------------------------------------------------------------------------------------------

LangChain also provides an Upstash Redis-based cache. Like the Redis-based cache, this cache is useful if you want to share the cache across multiple processes or servers. The Upstash Redis client uses HTTP and supports edge environments. To use it, you'll need to install the `@upstash/redis` package:

    npm install @upstash/redis

You'll also need an [Upstash account](https://docs.upstash.com/redis#create-account) and a [Redis database](https://docs.upstash.com/redis#create-a-database) to connect to. Once you've done that, retrieve your REST URL and REST token.

Then, you can pass a `cache` option when you instantiate the LLM. For example:

    import { OpenAI } from "langchain/llms/openai";import { UpstashRedisCache } from "langchain/cache/upstash_redis";// See https://docs.upstash.com/redis/howto/connectwithupstashredis#quick-start for connection optionsconst cache = new UpstashRedisCache({  config: {    url: "UPSTASH_REDIS_REST_URL",    token: "UPSTASH_REDIS_REST_TOKEN",  },});const model = new OpenAI({ cache });

#### API Reference:

*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [UpstashRedisCache](/docs/api/cache_upstash_redis/classes/UpstashRedisCache) from `langchain/cache/upstash_redis`

You can also directly pass in a previously created [@upstash/redis](https://docs.upstash.com/redis/sdks/javascriptsdk/overview) client instance:

    import { Redis } from "@upstash/redis";import https from "https";import { OpenAI } from "langchain/llms/openai";import { UpstashRedisCache } from "langchain/cache/upstash_redis";// const client = new Redis({//   url: process.env.UPSTASH_REDIS_REST_URL!,//   token: process.env.UPSTASH_REDIS_REST_TOKEN!,//   agent: new https.Agent({ keepAlive: true }),// });// Or simply call Redis.fromEnv() to automatically load the UPSTASH_REDIS_REST_URL and UPSTASH_REDIS_REST_TOKEN environment variables.const client = Redis.fromEnv({  agent: new https.Agent({ keepAlive: true }),});const cache = new UpstashRedisCache({ client });const model = new OpenAI({ cache });

#### API Reference:

*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [UpstashRedisCache](/docs/api/cache_upstash_redis/classes/UpstashRedisCache) from `langchain/cache/upstash_redis`