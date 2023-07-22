Google Cloud Enterprise Search
==============================

[Enterprise Search](https://cloud.google.com/enterprise-search) is a part of the Generative AI App Builder suite of tools offered by Google Cloud.

Gen AI App Builder lets developers, even those with limited machine learning skills, quickly and easily tap into the power of Google’s foundation models, search expertise, and conversational AI technologies to create enterprise-grade generative AI applications.

Enterprise Search lets organizations quickly build generative AI powered search engines for customers and employees.Enterprise Search is underpinned by a variety of Google Search technologies, including semantic search, which helps deliver more relevant results than traditional keyword-based search techniques by using natural language processing and machine learning techniques to infer relationships within the content and intent from the user’s query input. Enterprise Search also benefits from Google’s expertise in understanding how users search and factors in content relevance to order displayed results.

Google Cloud offers Enterprise Search via Gen App Builder in Google Cloud Console and via an API for enterprise workflow integration.

This notebook demonstrates how to configure Enterprise Search and use the Enterprise Search retriever. The Enterprise Search retriever encapsulates the [Generative AI App Builder Python client library](https://cloud.google.com/generative-ai-app-builder/docs/libraries#client-libraries-install-python) and uses it to access the Enterprise Search [Search Service API](https://cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.search_service).

Install pre-requisites[​](#install-pre-requisites "Direct link to Install pre-requisites")
------------------------------------------------------------------------------------------

You need to install the `google-cloud-discoverengine` package to use the Enterprise Search retriever.

    pip install google-cloud-discoveryengine

Configure access to Google Cloud and Google Cloud Enterprise Search[​](#configure-access-to-google-cloud-and-google-cloud-enterprise-search "Direct link to Configure access to Google Cloud and Google Cloud Enterprise Search")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Enterprise Search is generally available for the allowlist (which means customers need to be approved for access) as of June 6, 2023. Contact your Google Cloud sales team for access and pricing details. We are previewing additional features that are coming soon to the generally available offering as part of our [Trusted Tester](https://cloud.google.com/ai/earlyaccess/join?hl=en) program. Sign up for [Trusted Tester](https://cloud.google.com/ai/earlyaccess/join?hl=en) and contact your Google Cloud sales team for an expedited trial.

Before you can run this notebook you need to:

*   Set or create a Google Cloud project and turn on Gen App Builder
*   Create and populate an unstructured data store
*   Set credentials to access `Enterprise Search API`

### Set or create a Google Cloud poject and turn on Gen App Builder[​](#set-or-create-a-google-cloud-poject-and-turn-on-gen-app-builder "Direct link to Set or create a Google Cloud poject and turn on Gen App Builder")

Follow the instructions in the [Enterprise Search Getting Started guide](https://cloud.google.com/generative-ai-app-builder/docs/before-you-begin) to set/create a GCP project and enable Gen App Builder.

### Create and populate an unstructured data store[​](#create-and-populate-an-unstructured-data-store "Direct link to Create and populate an unstructured data store")

[Use Google Cloud Console to create an unstructured data store](https://cloud.google.com/generative-ai-app-builder/docs/create-engine-es#unstructured-data) and populate it with the example PDF documents from the `gs://cloud-samples-data/gen-app-builder/search/alphabet-investor-pdfs` Cloud Storage folder. Make sure to use the `Cloud Storage (without metadata)` option.

### Set credentials to access Enterprise Search API[​](#set-credentials-to-access-enterprise-search-api "Direct link to Set credentials to access Enterprise Search API")

The [Gen App Builder client libraries](https://cloud.google.com/generative-ai-app-builder/docs/libraries) used by the Enterprise Search retriever provide high-level language support for authenticating to Gen App Builder programmatically. Client libraries support [Application Default Credentials (ADC)](https://cloud.google.com/docs/authentication/application-default-credentials); the libraries look for credentials in a set of defined locations and use those credentials to authenticate requests to the API. With ADC, you can make credentials available to your application in a variety of environments, such as local development or production, without needing to modify your application code.

If running in [Google Colab](https://colab.google) authenticate with `google.colab.google.auth` otherwise follow one of the [supported methods](https://cloud.google.com/docs/authentication/application-default-credentials) to make sure that you Application Default Credentials are properly set.

    import sysif "google.colab" in sys.modules:    from google.colab import auth as google_auth    google_auth.authenticate_user()

Configure and use the Enterprise Search retriever[​](#configure-and-use-the-enterprise-search-retriever "Direct link to Configure and use the Enterprise Search retriever")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Enterprise Search retriever is implemented in the `langchain.retriever.GoogleCloudEntepriseSearchRetriever` class. The `get_relevan_documents` method returns a list of `langchain.schema.Document` documents where the `page_content` field of each document is populated with either an `extractive segment` or an `extractive answer` that matches a query. The `metadata` field is populated with metadata (if any) of a document from which the segments or answers were extracted.

An extractive answer is verbatim text that is returned with each search result. It is extracted directly from the original document. Extractive answers are typically displayed near the top of web pages to provide an end user with a brief answer that is contextually relevant to their query. Extractive answers are available for website and unstructured search.

An extractive segment is verbatim text that is returned with each search result. An extractive segment is usually more verbose than an extractive answer. Extractive segments can be displayed as an answer to a query, and can be used to perform post-processing tasks and as input for large language models to generate answers or new text. Extractive segments are available for unstructured search.

For more information about extractive segments and extractive answers refer to [product documentation](https://cloud.google.com/generative-ai-app-builder/docs/snippets).

When creating an instance of the retriever you can specify a number of parameters that control which Enterprise data store to access and how a natural language query is processed, including configurations for extractive answers and segments.

The mandatory parameters are:

*   `project_id` - Your Google Cloud PROJECT\_ID
*   `search_engine_id` - The ID of the data store you want to use.

The `project_id` and `search_engine_id` parameters can be provided explicitly in the retriever's constructor or through the environment variables - `PROJECT_ID` and `SEARCH_ENGINE_ID`.

You can also configure a number of optional parameters, including:

*   `max_documents` - The maximum number of documents used to provide extractive segments or extractive answers
*   `get_extractive_answers` - By default, the retriever is configured to return extractive segments. Set this field to `True` to return extractive answers
*   `max_extractive_answer_count` - The maximum number of extractive answers returned in each search result. At most 5 answers will be returned
*   `max_extractive_segment_count` - The maximum number of extractive segments returned in each search result. Currently one segment will be returned
*   `filter` - The filter expression that allows you filter the search results based on the metadata associated with the documents in the searched data store.
*   `query_expansion_condition` - Specification to determine under which conditions query expansion should occur. 0 - Unspecified query expansion condition. In this case, server behavior defaults to disabled. 1 - Disabled query expansion. Only the exact search query is used, even if SearchResponse.total\_size is zero. 2 - Automatic query expansion built by the Search API.

### Configure and use the retriever with extractve segments[​](#configure-and-use-the-retriever-with-extractve-segments "Direct link to Configure and use the retriever with extractve segments")

    from langchain.retrievers import GoogleCloudEnterpriseSearchRetrieverPROJECT_ID = "<YOUR PROJECT ID>"  # Set to your Project IDSEARCH_ENGINE_ID = "<YOUR SEARCH ENGINE ID>"  # Set to your data store ID

    retriever = GoogleCloudEnterpriseSearchRetriever(    project_id=PROJECT_ID,    search_engine_id=SEARCH_ENGINE_ID,    max_documents=3,)

    query = "What are Alphabet's Other Bets?"result = retriever.get_relevant_documents(query)for doc in result:    print(doc)

### Configure and use the retriever with extractve answers[​](#configure-and-use-the-retriever-with-extractve-answers "Direct link to Configure and use the retriever with extractve answers")

    retriever = GoogleCloudEnterpriseSearchRetriever(    project_id=PROJECT_ID,    search_engine_id=SEARCH_ENGINE_ID,    max_documents=3,    max_extractive_answer_count=3,    get_extractive_answers=True,)

    query = "What are Alphabet's Other Bets?"result = retriever.get_relevant_documents(query)for doc in result:    print(doc)