Additional
==========

[

📄️ Analyze Document
--------------------

The AnalyzeDocumentChain can be used as an end-to-end to chain. This chain takes in a single document, splits it up, and then runs it through a CombineDocumentsChain.

](/docs/modules/chains/additional/analyze_document)

[

📄️ Self-critique chain with constitutional AI
----------------------------------------------

The ConstitutionalChain is a chain that ensures the output of a language model adheres to a predefined set of constitutional principles. By incorporating specific rules and guidelines, the ConstitutionalChain filters and modifies the generated content to align with these principles, thus providing more controlled, ethical, and contextually appropriate responses. This mechanism helps maintain the integrity of the output while minimizing the risk of generating content that may violate guidelines, be offensive, or deviate from the desired context.

](/docs/modules/chains/additional/constitutional_chain)

[

📄️ Causal program-aided language (CPAL) chain
----------------------------------------------

The CPAL chain builds on the recent PAL to stop LLM hallucination. The problem with the PAL approach is that it hallucinates on a math problem with a nested chain of dependence. The innovation here is that this new CPAL approach includes causal structure to fix hallucination.

](/docs/modules/chains/additional/cpal)

[

📄️ Elasticsearch database
--------------------------

Interact with Elasticsearch analytics database via Langchain. This chain builds search queries via the Elasticsearch DSL API (filters and aggregations).

](/docs/modules/chains/additional/elasticsearch_database)

[

📄️ Extraction
--------------

The extraction chain uses the OpenAI functions parameter to specify a schema to extract entities from a document. This helps us make sure that the model outputs exactly the schema of entities and properties that we want, with their appropriate types.

](/docs/modules/chains/additional/extraction)

[

📄️ FLARE
---------

This notebook is an implementation of Forward-Looking Active REtrieval augmented generation (FLARE).

](/docs/modules/chains/additional/flare)

[

📄️ Graph DB QA chain
---------------------

This notebook shows how to use LLMs to provide a natural language interface to a graph database you can query with the Cypher query language.

](/docs/modules/chains/additional/graph_cypher_qa)

[

📄️ HugeGraph QA Chain
----------------------

This notebook shows how to use LLMs to provide a natural language interface to HugeGraph database.

](/docs/modules/chains/additional/graph_hugegraph_qa)

[

📄️ KuzuQAChain
---------------

This notebook shows how to use LLMs to provide a natural language interface to Kùzu database.

](/docs/modules/chains/additional/graph_kuzu_qa)

[

📄️ NebulaGraphQAChain
----------------------

This notebook shows how to use LLMs to provide a natural language interface to NebulaGraph database.

](/docs/modules/chains/additional/graph_nebula_qa)

[

📄️ Graph QA
------------

This notebook goes over how to do question answering over a graph data structure.

](/docs/modules/chains/additional/graph_qa)

[

📄️ GraphSparqlQAChain
----------------------

Graph databases are an excellent choice for applications based on network-like models. To standardize the syntax and semantics of such graphs, the W3C recommends Semantic Web Technologies, cp. Semantic Web. SPARQL serves as a query language analogously to SQL or Cypher for these graphs. This notebook demonstrates the application of LLMs as a natural language interface to a graph database by generating SPARQL.\\

](/docs/modules/chains/additional/graph_sparql_qa)

[

📄️ Hypothetical Document Embeddings
------------------------------------

This notebook goes over how to use Hypothetical Document Embeddings (HyDE), as described in this paper.

](/docs/modules/chains/additional/hyde)

[

📄️ Bash chain
--------------

This notebook showcases using LLMs and a bash process to perform simple filesystem commands.

](/docs/modules/chains/additional/llm_bash)

[

📄️ Self-checking chain
-----------------------

This notebook showcases how to use LLMCheckerChain.

](/docs/modules/chains/additional/llm_checker)

[

📄️ Math chain
--------------

This notebook showcases using LLMs and Python REPLs to do complex word math problems.

](/docs/modules/chains/additional/llm_math)

[

📄️ HTTP request chain
----------------------

Using the request library to get HTML results from a URL and then an LLM to parse results

](/docs/modules/chains/additional/llm_requests)

[

📄️ Summarization checker chain
-------------------------------

This notebook shows some examples of LLMSummarizationCheckerChain in use with different types of texts. It has a few distinct differences from the LLMCheckerChain, in that it doesn't have any assumptions to the format of the input text (or summary).

](/docs/modules/chains/additional/llm_summarization_checker)

[

📄️ LLM Symbolic Math
---------------------

This notebook showcases using LLMs and Python to Solve Algebraic Equations. Under the hood is makes use of SymPy.

](/docs/modules/chains/additional/llm_symbolic_math)

[

📄️ Moderation
--------------

This notebook walks through examples of how to use a moderation chain, and several common ways for doing so. Moderation chains are useful for detecting text that could be hateful, violent, etc. This can be useful to apply on both user input, but also on the output of a Language Model. Some API providers, like OpenAI, specifically prohibit you, or your end users, from generating some types of harmful content. To comply with this (and to just generally prevent your application from being harmful) you may often want to append a moderation chain to any LLMChains, in order to make sure any output the LLM generates is not harmful.

](/docs/modules/chains/additional/moderation)

[

📄️ Dynamically selecting from multiple prompts
-----------------------------------------------

This notebook demonstrates how to use the RouterChain paradigm to create a chain that dynamically selects the prompt to use for a given input. Specifically we show how to use the MultiPromptChain to create a question-answering chain that selects the prompt which is most relevant for a given question, and then answers the question using that prompt.

](/docs/modules/chains/additional/multi_prompt_router)

[

📄️ Dynamically selecting from multiple retrievers
--------------------------------------------------

This notebook demonstrates how to use the RouterChain paradigm to create a chain that dynamically selects which Retrieval system to use. Specifically we show how to use the MultiRetrievalQAChain to create a question-answering chain that selects the retrieval QA chain which is most relevant for a given question, and then answers the question using it.

](/docs/modules/chains/additional/multi_retrieval_qa_router)

[

📄️ Neptune Open Cypher QA Chain
--------------------------------

This QA chain queries Neptune graph database using openCypher and returns human readable response

](/docs/modules/chains/additional/neptune_cypher_qa)

[

📄️ Retrieval QA using OpenAI functions
---------------------------------------

OpenAI functions allows for structuring of response output. This is often useful in question answering when you want to not only get the final answer but also supporting evidence, citations, etc.

](/docs/modules/chains/additional/openai_functions_retrieval_qa)

[

📄️ OpenAPI chain
-----------------

This notebook shows an example of using an OpenAPI chain to call an endpoint in natural language, and get back a response in natural language.

](/docs/modules/chains/additional/openapi)

[

📄️ OpenAPI calls with OpenAI functions
---------------------------------------

In this notebook we'll show how to create a chain that automatically makes calls to an API based only on an OpenAPI spec. Under the hood, we're parsing the OpenAPI spec into a JSON schema that the OpenAI functions API can handle. This allows ChatGPT to automatically select and populate the relevant API call to make for any user input. Using the output of ChatGPT we then make the actual API call, and return the result.

](/docs/modules/chains/additional/openapi_openai)

[

📄️ Program-aided language model (PAL) chain
--------------------------------------------

Implements Program-Aided Language Models, as in https://arxiv.org/pdf/2211.10435.pdf.

](/docs/modules/chains/additional/pal)

[

📄️ Question-Answering Citations
--------------------------------

This notebook shows how to use OpenAI functions ability to extract citations from text.

](/docs/modules/chains/additional/qa_citations)

[

📄️ Document QA
---------------

Here we walk through how to use LangChain for question answering over a list of documents. Under the hood we'll be using our Document chains.

](/docs/modules/chains/additional/question_answering)

[

📄️ Tagging
-----------

The tagging chain uses the OpenAI functions parameter to specify a schema to tag a document with. This helps us make sure that the model outputs exactly tags that we want, with their appropriate types.

](/docs/modules/chains/additional/tagging)

[

📄️ Vector store-augmented text generation
------------------------------------------

This notebook walks through how to use LangChain for text generation over a vector index. This is useful if we want to generate text that is able to draw from a large body of custom text, for example, generating blog posts that have an understanding of previous blog posts written, or product tutorials that can refer to product documentation.

](/docs/modules/chains/additional/vector_db_text_generation)