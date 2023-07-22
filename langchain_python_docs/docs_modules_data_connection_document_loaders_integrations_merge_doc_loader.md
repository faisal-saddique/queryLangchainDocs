MergeDocLoader
==============

Merge the documents returned from a set of specified data loaders.

    from langchain.document_loaders import WebBaseLoaderloader_web = WebBaseLoader(    "https://github.com/basecamp/handbook/blob/master/37signals-is-you.md")

    from langchain.document_loaders import PyPDFLoaderloader_pdf = PyPDFLoader("../MachineLearning-Lecture01.pdf")

    from langchain.document_loaders.merge import MergedDataLoaderloader_all = MergedDataLoader(loaders=[loader_web, loader_pdf])

    docs_all = loader_all.load()

    len(docs_all)

        23