Extraction
==========

info

[Python Guide](https://python.langchain.com/en/latest/use_cases/extraction.html)

Language models are actually great at extracting structured information from unstructured text. This is useful because a lot of information is stored as text, but in order to make it most usable downstream it is often convinient to convert it to a structured format.

The most useful concept to understand here is the idea of OutputParsers. OutputParsers are responsible for specifying the schema a language model should respond in, and then parsing their raw-text output into that structured format.

The way you would use these to do extraction is that you would define the schema of the information you want to extract in an OutputParser. You would then create a PromptTemplate that takes in a raw text blob, with instructions to extract information in the specified format.