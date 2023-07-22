Output Parser
=============

info

[Python Guide](https://python.langchain.com/en/latest/modules/prompts/output_parsers.html)

[JS Guide](https://js.langchain.com/docs/modules/prompts/output_parsers)

Output parsers are classes that help structure language model responses. There are two main methods an output parser must implement:

*   `get_format_instructions() -> str`: A method which returns a string containing instructions for how the output of a language model should be formatted.
*   `parse(str) -> Any`: A method which takes in a string (assumed to be the response from a language model) and parses it into some structure.

And then one optional one:

*   `parse_with_prompt(str) -> Any`: A method which takes in a string (assumed to be the response from a language model) and a prompt (assumed to the prompt that generated such a response) and parses it into some structure. The prompt is largely provided in the event the OutputParser wants to retry or fix the output in some way, and needs information from the prompt to do so.