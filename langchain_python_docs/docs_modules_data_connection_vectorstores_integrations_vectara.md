Vectara
=======

> [Vectara](https://vectara.com/) is a API platform for building LLM-powered applications. It provides a simple to use API for document indexing and query that is managed by Vectara and is optimized for performance and accuracy.

This notebook shows how to use functionality related to the `Vectara` vector database or the `Vectara` retriever.

See the [Vectara API documentation](https://docs.vectara.com/docs/) for more information on how to use the API.

    import osfrom langchain.embeddings import FakeEmbeddingsfrom langchain.text_splitter import CharacterTextSplitterfrom langchain.vectorstores import Vectarafrom langchain.document_loaders import TextLoader

Connecting to Vectara from LangChain[​](#connecting-to-vectara-from-langchain "Direct link to Connecting to Vectara from LangChain")
------------------------------------------------------------------------------------------------------------------------------------

The Vectara API provides simple API endpoints for indexing and querying, which is encapsulated in the Vectara integration. First let's ingest the documents using the from\_documents() method:

    loader = TextLoader("../../../state_of_the_union.txt")documents = loader.load()text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)docs = text_splitter.split_documents(documents)

    vectara = Vectara.from_documents(    docs,    embedding=FakeEmbeddings(size=768),    doc_metadata={"speech": "state-of-the-union"},)

Vectara's indexing API provides a file upload API where the file is handled directly by Vectara - pre-processed, chunked optimally and added to the Vectara vector store. To use this, we added the add\_files() method (and from\_files()).

Let's see this in action. We pick two PDF documents to upload:

1.  The "I have a dream" speech by Dr. King
2.  Churchill's "We Shall Fight on the Beaches" speech

    import tempfileimport urllib.requesturls = [    [        "https://www.gilderlehrman.org/sites/default/files/inline-pdfs/king.dreamspeech.excerpts.pdf",        "I-have-a-dream",    ],    [        "https://www.parkwayschools.net/cms/lib/MO01931486/Centricity/Domain/1578/Churchill_Beaches_Speech.pdf",        "we shall fight on the beaches",    ],]files_list = []for url, _ in urls:    name = tempfile.NamedTemporaryFile().name    urllib.request.urlretrieve(url, name)    files_list.append(name)docsearch: Vectara = Vectara.from_files(    files=files_list,    embedding=FakeEmbeddings(size=768),    metadatas=[{"url": url, "speech": title} for url, title in urls],)

Similarity search[​](#similarity-search "Direct link to Similarity search")
---------------------------------------------------------------------------

The simplest scenario for using Vectara is to perform a similarity search.

    query = "What did the president say about Ketanji Brown Jackson"found_docs = vectara.similarity_search(    query, n_sentence_context=0, filter="doc.speech = 'state-of-the-union'")

    print(found_docs[0].page_content)

        Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections.         Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service.         One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court.         And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.

Similarity search with score[​](#similarity-search-with-score "Direct link to Similarity search with score")
------------------------------------------------------------------------------------------------------------

Sometimes we might want to perform the search, but also obtain a relevancy score to know how good is a particular result.

    query = "What did the president say about Ketanji Brown Jackson"found_docs = vectara.similarity_search_with_score(    query, filter="doc.speech = 'state-of-the-union'")

    document, score = found_docs[0]print(document.page_content)print(f"\nScore: {score}")

        Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections.         Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service.         One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court.         And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.        Score: 0.4917977

Now let's do similar search for content in the files we uploaded

    query = "We must forever conduct our struggle"found_docs = vectara.similarity_search_with_score(    query, filter="doc.speech = 'I-have-a-dream'")print(found_docs[0])print(found_docs[1])

        (Document(page_content='We must forever conduct our struggle on the high plane of dignity and discipline.', metadata={'section': '1'}), 0.7962591)    (Document(page_content='We must not allow our\ncreative protests to degenerate into physical violence. . . .', metadata={'section': '1'}), 0.25983918)

Vectara as a Retriever[​](#vectara-as-a-retriever "Direct link to Vectara as a Retriever")
------------------------------------------------------------------------------------------

Vectara, as all the other vector stores, can be used also as a LangChain Retriever:

    retriever = vectara.as_retriever()retriever

        VectaraRetriever(vectorstore=<langchain.vectorstores.vectara.Vectara object at 0x12772caf0>, search_type='similarity', search_kwargs={'lambda_val': 0.025, 'k': 5, 'filter': '', 'n_sentence_context': '0'})

    query = "What did the president say about Ketanji Brown Jackson"retriever.get_relevant_documents(query)[0]

        Document(page_content='Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections. \n\nTonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service. \n\nOne of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court. \n\nAnd I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.', metadata={'source': '../../../state_of_the_union.txt'})