BM25
====

[BM25](https://en.wikipedia.org/wiki/Okapi_BM25) also known as the Okapi BM25, is a ranking function used in information retrieval systems to estimate the relevance of documents to a given search query.

This notebook goes over how to use a retriever that under the hood uses BM25 using [`rank_bm25`](https://github.com/dorianbrown/rank_bm25) package.

    # !pip install rank_bm25

    from langchain.retrievers import BM25Retriever

        /workspaces/langchain/.venv/lib/python3.10/site-packages/deeplake/util/check_latest_version.py:32: UserWarning: A newer version of deeplake (3.6.10) is available. It's recommended that you update to the latest version using `pip install -U deeplake`.      warnings.warn(

Create New Retriever with Texts[](#create-new-retriever-with-texts "Direct link to Create New Retriever with Texts")
---------------------------------------------------------------------------------------------------------------------

    retriever = BM25Retriever.from_texts(["foo", "bar", "world", "hello", "foo bar"])

Create a New Retriever with Documents[](#create-a-new-retriever-with-documents "Direct link to Create a New Retriever with Documents")
---------------------------------------------------------------------------------------------------------------------------------------

You can now create a new retriever with the documents you created.

    from langchain.schema import Documentretriever = BM25Retriever.from_documents(    [        Document(page_content="foo"),        Document(page_content="bar"),        Document(page_content="world"),        Document(page_content="hello"),        Document(page_content="foo bar"),    ])

Use Retriever[](#use-retriever "Direct link to Use Retriever")
---------------------------------------------------------------

We can now use the retriever!

    result = retriever.get_relevant_documents("foo")

    result

        [Document(page_content='foo', metadata={}),     Document(page_content='foo bar', metadata={}),     Document(page_content='hello', metadata={}),     Document(page_content='world', metadata={})]