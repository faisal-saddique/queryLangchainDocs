Prompts
=======

info

[Python Guide](https://python.langchain.com/en/latest/modules/prompts.html)

[JS Guide](https://js.langchain.com/docs/modules/prompts/)

The new way of programming models is through prompts. A "prompt" refers to the input to the model. This input is rarely hard coded, but rather is often constructed from multiple components. A PromptTemplate is responsible for the construction of this input. LangChain provides several classes and functions to make constructing and working with prompts easy.

This section of documentation is split into four sections:

**PromptValue**

The class representing an input to a model.

**Prompt Templates**

The class in charge of constructing a PromptValue.

**Example Selectors**

Often times it is useful to include examples in prompts. These examples can be hardcoded, but it is often more powerful if they are dynamically selected.

**Output Parsers**

Language models (and Chat Models) output text. But many times you may want to get more structured information than just text back. This is where output parsers come in. Output Parsers are responsible for (1) instructing the model how output should be formatted, (2) parsing output into the desired formatting (including retrying if necessary).

Go deeper[​](#go-deeper "Direct link to Go deeper")
---------------------------------------------------

[

📄️ Prompt Value
----------------

A “prompt” refers to what is passed to the underlying model. The main abstractions have for prompt in LangChain so for all deal with text data. For other data types (images, audio) we are working on adding abstractions but do not yet have them.

](/docs/components/prompts/prompt-value)

[

📄️ Prompt Template
-------------------

Python Guide

](/docs/components/prompts/prompt-template)

[

📄️ Example Selectors
---------------------

Python Guide

](/docs/components/prompts/example-selectors)

[

📄️ Output Parser
-----------------

Python Guide

](/docs/components/prompts/output-parser)