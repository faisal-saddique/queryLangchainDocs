Context aware text splitting and QA / Chat
==========================================

Text splitting for vector storage often uses sentences or other delimiters [to keep related text together](https://www.pinecone.io/learn/chunking-strategies/).

But many documents (such as `Markdown` files) have structure (headers) that can be explicitly used in splitting.

The `MarkdownHeaderTextSplitter` lets a user split `Markdown` files files based on specified headers.

This results in chunks that retain the header(s) that it came from in the metadata.

This works nicely w/ `SelfQueryRetriever`.

First, tell the retriever about our splits.

Then, query based on the doc structure (e.g., "summarize the doc introduction").

Chunks only from that section of the Document will be filtered and used in chat / Q+A.

Let's test this out on an [example Notion page](https://rlancemartin.notion.site/Auto-Evaluation-of-Metadata-Filtering-18502448c85240828f33716740f9574b?pvs=4)!

First, I download the page to Markdown as explained [here](https://python.langchain.com/docs/ecosystem/integrations/notion).

    # Load Notion page as a markdownfile filefrom langchain.document_loaders import NotionDirectoryLoaderpath = "../Notion_DB/"loader = NotionDirectoryLoader(path)docs = loader.load()md_file = docs[0].page_content

    # Let's create groups based on the section headers in our pagefrom langchain.text_splitter import MarkdownHeaderTextSplitterheaders_to_split_on = [    ("###", "Section"),]markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)md_header_splits = markdown_splitter.split_text(md_file)

Now, perform text splitting on the header grouped documents.

    # Define our text splitterfrom langchain.text_splitter import RecursiveCharacterTextSplitterchunk_size = 500chunk_overlap = 0text_splitter = RecursiveCharacterTextSplitter(    chunk_size=chunk_size, chunk_overlap=chunk_overlap)all_splits = text_splitter.split_documents(md_header_splits)

This sets us up well do perform metadata filtering based on the document structure.

Let's bring this all togther by building a vectorstore first.

    pip install chromadb

    # Build vectorstore and keep the metadatafrom langchain.embeddings import OpenAIEmbeddingsfrom langchain.vectorstores import Chromavectorstore = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbeddings())

Let's create a `SelfQueryRetriever` that can filter based upon metadata we defined.

    # Create retrieverfrom langchain.llms import OpenAIfrom langchain.retrievers.self_query.base import SelfQueryRetrieverfrom langchain.chains.query_constructor.base import AttributeInfo# Define our metadatametadata_field_info = [    AttributeInfo(        name="Section",        description="Part of the document that the text comes from",        type="string or list[string]",    ),]document_content_description = "Major sections of the document"# Define self query retriverllm = OpenAI(temperature=0)retriever = SelfQueryRetriever.from_llm(    llm, vectorstore, document_content_description, metadata_field_info, verbose=True)

We can see that we can query _only for texts_ in the `Introduction` of the document!

    # Testretriever.get_relevant_documents("Summarize the Introduction section of the document")

        query='Introduction' filter=Comparison(comparator=<Comparator.EQ: 'eq'>, attribute='Section', value='Introduction') limit=None    [Document(page_content='![Untitled](Auto-Evaluation%20of%20Metadata%20Filtering%2018502448c85240828f33716740f9574b/Untitled.png)', metadata={'Section': 'Introduction'}),     Document(page_content='Q+A systems often use a two-step approach: retrieve relevant text chunks and then synthesize them into an answer. There many ways to approach this. For example, we recently [discussed](https://blog.langchain.dev/auto-evaluation-of-anthropic-100k-context-window/) the Retriever-Less option (at bottom in the below diagram), highlighting the Anthropic 100k context window model. Metadata filtering is an alternative approach that pre-filters chunks based on a user-defined criteria in a VectorDB using', metadata={'Section': 'Introduction'}),     Document(page_content='metadata tags prior to semantic search.', metadata={'Section': 'Introduction'})]

    # Testretriever.get_relevant_documents("Summarize the Introduction section of the document")

        query='Introduction' filter=Comparison(comparator=<Comparator.EQ: 'eq'>, attribute='Section', value='Introduction') limit=None    [Document(page_content='![Untitled](Auto-Evaluation%20of%20Metadata%20Filtering%2018502448c85240828f33716740f9574b/Untitled.png)', metadata={'Section': 'Introduction'}),     Document(page_content='Q+A systems often use a two-step approach: retrieve relevant text chunks and then synthesize them into an answer. There many ways to approach this. For example, we recently [discussed](https://blog.langchain.dev/auto-evaluation-of-anthropic-100k-context-window/) the Retriever-Less option (at bottom in the below diagram), highlighting the Anthropic 100k context window model. Metadata filtering is an alternative approach that pre-filters chunks based on a user-defined criteria in a VectorDB using', metadata={'Section': 'Introduction'}),     Document(page_content='metadata tags prior to semantic search.', metadata={'Section': 'Introduction'})]

We can also look at other parts of the document.

    retriever.get_relevant_documents("Summarize the Testing section of the document")

        query='Testing' filter=Comparison(comparator=<Comparator.EQ: 'eq'>, attribute='Section', value='Testing') limit=None    [Document(page_content='![Untitled](Auto-Evaluation%20of%20Metadata%20Filtering%2018502448c85240828f33716740f9574b/Untitled%202.png)', metadata={'Section': 'Testing'}),     Document(page_content='`SelfQueryRetriever` works well in [many cases](https://twitter.com/hwchase17/status/1656791488569954304/photo/1). For example, given [this test case](https://twitter.com/hwchase17/status/1656791488569954304?s=20):  \n![Untitled](Auto-Evaluation%20of%20Metadata%20Filtering%2018502448c85240828f33716740f9574b/Untitled%201.png)  \nThe query can be nicely broken up into semantic query and metadata filter:  \n```python\nsemantic query: "prompt injection"', metadata={'Section': 'Testing'}),     Document(page_content='Below, we can see detailed results from the app:  \n- Kor extraction is above to perform the transformation between query and metadata format ✅\n- Self-querying attempts to filter using the episode ID (`252`) in the query and fails 🚫\n- Baseline returns docs from 3 different episodes (one from `252`), confusing the answer 🚫', metadata={'Section': 'Testing'}),     Document(page_content='will use in retrieval [here](https://github.com/langchain-ai/auto-evaluator/blob/main/streamlit/kor_retriever_lex.py).', metadata={'Section': 'Testing'})]

Now, we can create chat or Q+A apps that are aware of the explict document structure.

The ability to retain document structure for metadata filtering can be helpful for complicated or longer documents.

    from langchain.chains import RetrievalQAfrom langchain.chat_models import ChatOpenAIllm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)qa_chain = RetrievalQA.from_chain_type(llm, retriever=retriever)qa_chain.run("Summarize the Testing section of the document")

        query='Testing' filter=Comparison(comparator=<Comparator.EQ: 'eq'>, attribute='Section', value='Testing') limit=None    'The Testing section of the document describes the evaluation of the `SelfQueryRetriever` component in comparison to a baseline model. The evaluation was performed on a test case where the query was broken down into a semantic query and a metadata filter. The results showed that the `SelfQueryRetriever` component was able to perform the transformation between query and metadata format, but failed to filter using the episode ID in the query. The baseline model returned documents from three different episodes, which confused the answer. The `SelfQueryRetriever` component was deemed to work well in many cases and will be used in retrieval.'