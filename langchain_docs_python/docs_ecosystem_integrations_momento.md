Momento
=======

> [Momento Cache](https://docs.momentohq.com/) is the world's first truly serverless caching service. It provides instant elasticity, scale-to-zero capability, and blazing-fast performance.  
> With Momento Cache, you grab the SDK, you get an end point, input a few lines into your code, and you're off and running.

This page covers how to use the [Momento](https://gomomento.com) ecosystem within LangChain.

Installation and Setup[](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

*   Sign up for a free account [here](https://docs.momentohq.com/getting-started) and get an auth token
*   Install the Momento Python SDK with `pip install momento`

Cache[](#cache "Direct link to Cache")
---------------------------------------

The Cache wrapper allows for [Momento](https://gomomento.com) to be used as a serverless, distributed, low-latency cache for LLM prompts and responses.

The standard cache is the go-to use case for [Momento](https://gomomento.com) users in any environment.

Import the cache as follows:

    from langchain.cache import MomentoCache

And set up like so:

    from datetime import timedeltafrom momento import CacheClient, Configurations, CredentialProviderimport langchain# Instantiate the Momento clientcache_client = CacheClient(    Configurations.Laptop.v1(),    CredentialProvider.from_environment_variable("MOMENTO_AUTH_TOKEN"),    default_ttl=timedelta(days=1))# Choose a Momento cache name of your choicecache_name = "langchain"# Instantiate the LLM cachelangchain.llm_cache = MomentoCache(cache_client, cache_name)

Memory[](#memory "Direct link to Memory")
------------------------------------------

Momento can be used as a distributed memory store for LLMs.

### Chat Message History Memory[](#chat-message-history-memory "Direct link to Chat Message History Memory")

See [this notebook](/docs/modules/memory/integrations/momento_chat_message_history.html) for a walkthrough of how to use Momento as a memory store for chat message history.