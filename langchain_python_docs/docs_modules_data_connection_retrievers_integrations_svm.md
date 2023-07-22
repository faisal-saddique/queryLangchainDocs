SVM
===

> [Support vector machines (SVMs)](https://scikit-learn.org/stable/modules/svm.html#support-vector-machines) are a set of supervised learning methods used for classification, regression and outliers detection.

This notebook goes over how to use a retriever that under the hood uses an `SVM` using `scikit-learn` package.

Largely based on [https://github.com/karpathy/randomfun/blob/master/knn\_vs\_svm.html](https://github.com/karpathy/randomfun/blob/master/knn_vs_svm.html)

    #!pip install scikit-learn

    #!pip install lark

We want to use `OpenAIEmbeddings` so we have to get the OpenAI API Key.

    import osimport getpassos.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")

        OpenAI API Key: ········

    from langchain.retrievers import SVMRetrieverfrom langchain.embeddings import OpenAIEmbeddings

Create New Retriever with Texts[​](#create-new-retriever-with-texts "Direct link to Create New Retriever with Texts")
---------------------------------------------------------------------------------------------------------------------

    retriever = SVMRetriever.from_texts(    ["foo", "bar", "world", "hello", "foo bar"], OpenAIEmbeddings())

Use Retriever[​](#use-retriever "Direct link to Use Retriever")
---------------------------------------------------------------

We can now use the retriever!

    result = retriever.get_relevant_documents("foo")

    result

        [Document(page_content='foo', metadata={}),     Document(page_content='foo bar', metadata={}),     Document(page_content='hello', metadata={}),     Document(page_content='world', metadata={})]