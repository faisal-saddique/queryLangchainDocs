LarkSuite (FeiShu)
==================

> [LarkSuite](https://www.larksuite.com/) is an enterprise collaboration platform developed by ByteDance.

This notebook covers how to load data from the `LarkSuite` REST API into a format that can be ingested into LangChain, along with example usage for text summarization.

The LarkSuite API requires an access token (tenant\_access\_token or user\_access\_token), checkout [LarkSuite open platform document](https://open.larksuite.com/document) for API details.

    from getpass import getpassfrom langchain.document_loaders.larksuite import LarkSuiteDocLoaderDOMAIN = input("larksuite domain")ACCESS_TOKEN = getpass("larksuite tenant_access_token or user_access_token")DOCUMENT_ID = input("larksuite document id")

    from pprint import pprintlarksuite_loader = LarkSuiteDocLoader(DOMAIN, ACCESS_TOKEN, DOCUMENT_ID)docs = larksuite_loader.load()pprint(docs)

        [Document(page_content='Test Doc\nThis is a Test Doc\n\n1\n2\n3\n\n', metadata={'document_id': 'V76kdbd2HoBbYJxdiNNccajunPf', 'revision_id': 11, 'title': 'Test Doc'})]

    # see https://python.langchain.com/docs/use_cases/summarization for more detailsfrom langchain.chains.summarize import load_summarize_chainchain = load_summarize_chain(llm, chain_type="map_reduce")chain.run(docs)