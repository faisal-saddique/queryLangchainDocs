Chains
======

info

[Python Guide](https://python.langchain.com/en/latest/modules/chains.html)

[JS Guide](https://js.langchain.com/docs/modules/chains/)

Chains is an incredibly generic concept which returns to a sequence of modular components (or other chains) combined in a particular way to accomplish a common use case.

The most commonly used type of chain is an LLMChain, which combines a PromptTemplate, a Model, and Guardrails to take user input, format it accordingly, pass it to the model and get a response, and then validate and fix (if necessary) the model output.

Go deeper[​](#go-deeper "Direct link to Go deeper")
---------------------------------------------------

[

📄️ Chain
---------

A chain is just an end-to-end wrapper around multiple individual components.

](/docs/components/chains/chain)

[

📄️ LLMChain
------------

A LLMChain is the most common type of chain. It consists of a PromptTemplate, a model (either an LLM or a ChatModel), and an optional output parser. This chain takes multiple input variables, uses the PromptTemplate to format them into a prompt. It then passes that to the model. Finally, it uses the OutputParser (if provided) to parse the output of the LLM into a final format.

](/docs/components/chains/llm-chain)

[

📄️ Index-related chains
------------------------

Python Guide

](/docs/components/chains/index_related_chains)

[

📄️ Prompt Selector
-------------------

One of the goals of chains in LangChain is to enable people to get started with a particular use case as quickly as possible. A big part of this is having good prompts.

](/docs/components/chains/prompt-selector)