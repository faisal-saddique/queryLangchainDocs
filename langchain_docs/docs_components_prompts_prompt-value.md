Prompt Value
============

A “prompt” refers to what is passed to the underlying model. The main abstractions have for prompt in LangChain so for all deal with text data. For other data types (images, audio) we are working on adding abstractions but do not yet have them.

Different models may expect different data formats. Where possible, we want to allow for the same prompt to be used in different model types. For that reason, we have a concept of a PromptValue. This is a class which exposes methods to be converted to the exact input types that each model type expects (text or ChatMessages for now)