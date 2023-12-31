Composition
===========

This notebook goes over how to compose multiple prompts together. This can be useful when you want to reuse parts of prompts. This can be done with a PipelinePrompt. A PipelinePrompt consists of two main parts:

*   Final prompt: This is the final prompt that is returned
*   Pipeline prompts: This is a list of tuples, consisting of a string name and a prompt template. Each prompt template will be formatted and then passed to future prompt templates as a variable with the same name.

    from langchain.prompts.pipeline import PipelinePromptTemplatefrom langchain.prompts.prompt import PromptTemplate

    full_template = """{introduction}{example}{start}"""full_prompt = PromptTemplate.from_template(full_template)

    introduction_template = """You are impersonating {person}."""introduction_prompt = PromptTemplate.from_template(introduction_template)

    example_template = """Here's an example of an interaction: Q: {example_q}A: {example_a}"""example_prompt = PromptTemplate.from_template(example_template)

    start_template = """Now, do this for real!Q: {input}A:"""start_prompt = PromptTemplate.from_template(start_template)

    input_prompts = [    ("introduction", introduction_prompt),    ("example", example_prompt),    ("start", start_prompt)]pipeline_prompt = PipelinePromptTemplate(final_prompt=full_prompt, pipeline_prompts=input_prompts)

    pipeline_prompt.input_variables

        ['example_a', 'person', 'example_q', 'input']

    print(pipeline_prompt.format(    person="Elon Musk",    example_q="What's your favorite car?",    example_a="Tesla",    input="What's your favorite social media site?"))

        You are impersonating Elon Musk.    Here's an example of an interaction:         Q: What's your favorite car?    A: Tesla    Now, do this for real!        Q: What's your favorite social media site?    A: