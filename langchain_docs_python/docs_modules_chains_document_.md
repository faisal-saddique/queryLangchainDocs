Documents
=========

These are the core chains for working with Documents. They are useful for summarizing documents, answering questions over documents, extracting information from documents, and more.

These chains all implement a common interface:

    class BaseCombineDocumentsChain(Chain, ABC):    """Base interface for chains combining documents."""    @abstractmethod    def combine_docs(self, docs: List[Document], **kwargs: Any) -> Tuple[str, dict]:        """Combine documents into a single string."""

[

📄️ Stuff
---------

The stuff documents chain ("stuff" as in "to stuff" or "to fill") is the most straightforward of the document chains. It takes a list of documents, inserts them all into a prompt and passes that prompt to an LLM.

](/docs/modules/chains/document/stuff)

[

📄️ Refine
----------

The refine documents chain constructs a response by looping over the input documents and iteratively updating its answer. For each document, it passes all non-document inputs, the current document, and the latest intermediate answer to an LLM chain to get a new answer.

](/docs/modules/chains/document/refine)

[

📄️ Map reduce
--------------

The map reduce documents chain first applies an LLM chain to each document individually (the Map step), treating the chain output as a new document. It then passes all the new documents to a separate combine documents chain to get a single output (the Reduce step). It can optionally first compress, or collapse, the mapped documents to make sure that they fit in the combine documents chain (which will often pass them to an LLM). This compression step is performed recursively if necessary.

](/docs/modules/chains/document/map_reduce)

[

📄️ Map re-rank
---------------

The map re-rank documents chain runs an initial prompt on each document, that not only tries to complete a task but also gives a score for how certain it is in its answer. The highest scoring response is returned.

](/docs/modules/chains/document/map_rerank)