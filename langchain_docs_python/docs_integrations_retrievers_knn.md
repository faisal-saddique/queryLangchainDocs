kNN
===

> In statistics, the [k-nearest neighbors algorithm (k-NN)](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) is a non-parametric supervised learning method first developed by Evelyn Fix and Joseph Hodges in 1951, and later expanded by Thomas Cover. It is used for classification and regression.

This notebook goes over how to use a retriever that under the hood uses an kNN.

Largely based on [https://github.com/karpathy/randomfun/blob/master/knn\_vs\_svm.html](https://github.com/karpathy/randomfun/blob/master/knn_vs_svm.html)

    from langchain.retrievers import KNNRetrieverfrom langchain.embeddings import OpenAIEmbeddings

Create New Retriever with Texts[](#create-new-retriever-with-texts "Direct link to Create New Retriever with Texts")
---------------------------------------------------------------------------------------------------------------------

    retriever = KNNRetriever.from_texts(    ["foo", "bar", "world", "hello", "foo bar"], OpenAIEmbeddings())

Use Retriever[](#use-retriever "Direct link to Use Retriever")
---------------------------------------------------------------

We can now use the retriever!

    result = retriever.get_relevant_documents("foo")

    result

        [Document(page_content='foo', metadata={}),     Document(page_content='foo bar', metadata={}),     Document(page_content='hello', metadata={}),     Document(page_content='bar', metadata={})]