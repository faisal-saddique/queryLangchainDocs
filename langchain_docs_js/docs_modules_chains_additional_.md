Additional
==========

[

🗃️ OpenAI functions chains
---------------------------

3 items

](/docs/modules/chains/additional/openai_functions/)

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