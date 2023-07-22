Prompt Template
===============

info

[Python Guide](https://python.langchain.com/en/latest/modules/prompts/prompt_templates.html)

[JS Guide](https://js.langchain.com/docs/modules/prompts/prompt_templates)

A PromptValue is what is eventually passed to the model. Most of the time, this value is not hardcoded but is rather dynamically created based on a combination of user input, other non-static information (often coming from multiple sources), and a fixed template string. We call the object responsible for creating the PromptValue a PromptTemplate. This object exposes a method for taking in input variables and returning a PromptValue.