Recursive URL Loader
====================

We may want to process load all URLs under a root directory.

For example, let's look at the [LangChain JS documentation](https://js.langchain.com/docs/).

This has many interesting child pages that we may want to read in bulk.

Of course, the `WebBaseLoader` can load a list of pages.

But, the challenge is traversing the tree of child pages and actually assembling that list!

We do this using the `RecursiveUrlLoader`.

This also gives us the flexibility to exclude some children (e.g., the `api` directory with > 800 child pages).

    from langchain.document_loaders.recursive_url_loader import RecursiveUrlLoader

Let's try a simple example.

    url = "https://js.langchain.com/docs/modules/memory/examples/"loader = RecursiveUrlLoader(url=url)docs = loader.load()

    len(docs)

        12

    docs[0].page_content[:50]

        '\n\n\n\n\nBuffer Window Memory | 🦜️🔗 Langchain\n\n\n\n\n\nSki'

    docs[0].metadata

        {'source': 'https://js.langchain.com/docs/modules/memory/examples/buffer_window_memory',     'title': 'Buffer Window Memory | 🦜️🔗 Langchain',     'description': 'BufferWindowMemory keeps track of the back-and-forths in conversation, and then uses a window of size k to surface the last k back-and-forths to use as memory.',     'language': 'en'}

Now, let's try a more extensive example, the `docs` root dir.

We will skip everything under `api`.

For this, we can `lazy_load` each page as we crawl the tree, using `WebBaseLoader` to load each as we go.

    url = "https://js.langchain.com/docs/"exclude_dirs = ["https://js.langchain.com/docs/api/"]loader = RecursiveUrlLoader(url=url, exclude_dirs=exclude_dirs)# Lazy load eachdocs = [print(doc) or doc for doc in loader.lazy_load()]

    # Load all pagesdocs = loader.load()

    len(docs)

        188

    docs[0].page_content[:50]

        '\n\n\n\n\nAgent Simulations | 🦜️🔗 Langchain\n\n\n\n\n\nSkip t'

    docs[0].metadata

        {'source': 'https://js.langchain.com/docs/use_cases/agent_simulations/',     'title': 'Agent Simulations | 🦜️🔗 Langchain',     'description': 'Agent simulations involve taking multiple agents and having them interact with each other.',     'language': 'en'}