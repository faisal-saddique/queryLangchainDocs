StarRocks
=========

> [StarRocks](https://www.starrocks.io/) is a High-Performance Analytical Database. `StarRocks` is a next-gen sub-second MPP database for full analytics scenarios, including multi-dimensional analytics, real-time analytics and ad-hoc query.

> Usually `StarRocks` is categorized into OLAP, and it has showed excellent performance in [ClickBench — a Benchmark For Analytical DBMS](https://benchmark.clickhouse.com/). Since it has a super-fast vectorized execution engine, it could also be used as a fast vectordb.

Here we'll show how to use the StarRocks Vector Store.

Setup[](#setup "Direct link to Setup")
---------------------------------------

    #!pip install pymysql

Set `update_vectordb = False` at the beginning. If there is no docs updated, then we don't need to rebuild the embeddings of docs

    from langchain.embeddings.openai import OpenAIEmbeddingsfrom langchain.vectorstores import StarRocksfrom langchain.vectorstores.starrocks import StarRocksSettingsfrom langchain.vectorstores import Chromafrom langchain.text_splitter import CharacterTextSplitter, TokenTextSplitterfrom langchain import OpenAI, VectorDBQAfrom langchain.document_loaders import DirectoryLoaderfrom langchain.chains import RetrievalQAfrom langchain.document_loaders import TextLoader, UnstructuredMarkdownLoaderupdate_vectordb = False

        /Users/dirlt/utils/py3env/lib/python3.9/site-packages/requests/__init__.py:102: RequestsDependencyWarning: urllib3 (1.26.7) or chardet (5.1.0)/charset_normalizer (2.0.9) doesn't match a supported version!      warnings.warn("urllib3 ({}) or chardet ({})/charset_normalizer ({}) doesn't match a supported "

Load docs and split them into tokens[](#load-docs-and-split-them-into-tokens "Direct link to Load docs and split them into tokens")
------------------------------------------------------------------------------------------------------------------------------------

Load all markdown files under the `docs` directory

for starrocks documents, you can clone repo from [https://github.com/StarRocks/starrocks](https://github.com/StarRocks/starrocks), and there is `docs` directory in it.

    loader = DirectoryLoader(    "./docs", glob="**/*.md", loader_cls=UnstructuredMarkdownLoader)documents = loader.load()

Split docs into tokens, and set `update_vectordb = True` because there are new docs/tokens.

    # load text splitter and split docs into snippets of texttext_splitter = TokenTextSplitter(chunk_size=400, chunk_overlap=50)split_docs = text_splitter.split_documents(documents)# tell vectordb to update text embeddingsupdate_vectordb = True

    split_docs[-20]

        Document(page_content='Compile StarRocks with Docker\n\nThis topic describes how to compile StarRocks using Docker.\n\nOverview\n\nStarRocks provides development environment images for both Ubuntu 22.04 and CentOS 7.9. With the image, you can launch a Docker container and compile StarRocks in the container.\n\nStarRocks version and DEV ENV image\n\nDifferent branches of StarRocks correspond to different development environment images provided on StarRocks Docker Hub.\n\nFor Ubuntu 22.04:\n\n| Branch name | Image name              |\n  | --------------- | ----------------------------------- |\n  | main            | starrocks/dev-env-ubuntu:latest     |\n  | branch-3.0      | starrocks/dev-env-ubuntu:3.0-latest |\n  | branch-2.5      | starrocks/dev-env-ubuntu:2.5-latest |\n\nFor CentOS 7.9:\n\n| Branch name | Image name                       |\n  | --------------- | ------------------------------------ |\n  | main            | starrocks/dev-env-centos7:latest     |\n  | branch-3.0      | starrocks/dev-env-centos7:3.0-latest |\n  | branch-2.5      | starrocks/dev-env-centos7:2.5-latest |\n\nPrerequisites\n\nBefore compiling StarRocks, make sure the following requirements are satisfied:\n\nHardware\n\n', metadata={'source': 'docs/developers/build-starrocks/Build_in_docker.md'})

    print("# docs  = %d, # splits = %d" % (len(documents), len(split_docs)))

        # docs  = 657, # splits = 2802

Create vectordb instance[](#create-vectordb-instance "Direct link to Create vectordb instance")
------------------------------------------------------------------------------------------------

### Use StarRocks as vectordb[](#use-starrocks-as-vectordb "Direct link to Use StarRocks as vectordb")

    def gen_starrocks(update_vectordb, embeddings, settings):    if update_vectordb:        docsearch = StarRocks.from_documents(split_docs, embeddings, config=settings)    else:        docsearch = StarRocks(embeddings, settings)    return docsearch

Convert tokens into embeddings and put them into vectordb[](#convert-tokens-into-embeddings-and-put-them-into-vectordb "Direct link to Convert tokens into embeddings and put them into vectordb")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Here we use StarRocks as vectordb, you can configure StarRocks instance via `StarRocksSettings`.

Configuring StarRocks instance is pretty much like configuring mysql instance. You need to specify:

1.  host/port
2.  username(default: 'root')
3.  password(default: '')
4.  database(default: 'default')
5.  table(default: 'langchain')

    embeddings = OpenAIEmbeddings()# configure starrocks settings(host/port/user/pw/db)settings = StarRocksSettings()settings.port = 41003settings.host = "127.0.0.1"settings.username = "root"settings.password = ""settings.database = "zya"docsearch = gen_starrocks(update_vectordb, embeddings, settings)print(docsearch)update_vectordb = False

        Inserting data...: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2802/2802 [02:26<00:00, 19.11it/s]    zya.langchain @ 127.0.0.1:41003        username: root        Table Schema:    ----------------------------------------------------------------------------    |name                    |type                    |key                     |    ----------------------------------------------------------------------------    |id                      |varchar(65533)          |true                    |    |document                |varchar(65533)          |false                   |    |embedding               |array<float>            |false                   |    |metadata                |varchar(65533)          |false                   |    ----------------------------------------------------------------------------    

Build QA and ask question to it[](#build-qa-and-ask-question-to-it "Direct link to Build QA and ask question to it")
---------------------------------------------------------------------------------------------------------------------

    llm = OpenAI()qa = RetrievalQA.from_chain_type(    llm=llm, chain_type="stuff", retriever=docsearch.as_retriever())query = "is profile enabled by default? if not, how to enable profile?"resp = qa.run(query)print(resp)

         No, profile is not enabled by default. To enable profile, set the variable `enable_profile` to `true` using the command `set enable_profile = true;`