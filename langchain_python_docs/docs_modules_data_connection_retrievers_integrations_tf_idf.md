TF-IDF
======

> [TF-IDF](https://scikit-learn.org/stable/modules/feature_extraction.html#tfidf-term-weighting) means term-frequency times inverse document-frequency.

This notebook goes over how to use a retriever that under the hood uses [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) using `scikit-learn` package.

For more information on the details of TF-IDF see [this blog post](https://medium.com/data-science-bootcamp/tf-idf-basics-of-information-retrieval-48de122b2a4c).

    # !pip install scikit-learn

    from langchain.retrievers import TFIDFRetriever

Create New Retriever with Texts[​](#create-new-retriever-with-texts "Direct link to Create New Retriever with Texts")
---------------------------------------------------------------------------------------------------------------------

    retriever = TFIDFRetriever.from_texts(["foo", "bar", "world", "hello", "foo bar"])

Create a New Retriever with Documents[​](#create-a-new-retriever-with-documents "Direct link to Create a New Retriever with Documents")
---------------------------------------------------------------------------------------------------------------------------------------

You can now create a new retriever with the documents you created.

    from langchain.schema import Documentretriever = TFIDFRetriever.from_documents(    [        Document(page_content="foo"),        Document(page_content="bar"),        Document(page_content="world"),        Document(page_content="hello"),        Document(page_content="foo bar"),    ])

Use Retriever[​](#use-retriever "Direct link to Use Retriever")
---------------------------------------------------------------

We can now use the retriever!

    result = retriever.get_relevant_documents("foo")

    result

        [Document(page_content='foo', metadata={}),     Document(page_content='foo bar', metadata={}),     Document(page_content='hello', metadata={}),     Document(page_content='world', metadata={})]