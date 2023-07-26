Datetime parser
===============

This OutputParser shows out to parse LLM output into datetime format.

    from langchain.prompts import PromptTemplatefrom langchain.output_parsers import DatetimeOutputParserfrom langchain.chains import LLMChainfrom langchain.llms import OpenAI

    output_parser = DatetimeOutputParser()template = """Answer the users question:{question}{format_instructions}"""prompt = PromptTemplate.from_template(    template,    partial_variables={"format_instructions": output_parser.get_format_instructions()},)

    chain = LLMChain(prompt=prompt, llm=OpenAI())

    output = chain.run("around when was bitcoin founded?")

    output

        '\n\n2008-01-03T18:15:05.000000Z'

    output_parser.parse(output)

        datetime.datetime(2008, 1, 3, 18, 15, 5)