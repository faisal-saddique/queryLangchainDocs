List parser
===========

This output parser can be used when you want to return a list of comma-separated items.

    from langchain.output_parsers import CommaSeparatedListOutputParserfrom langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplatefrom langchain.llms import OpenAIfrom langchain.chat_models import ChatOpenAIoutput_parser = CommaSeparatedListOutputParser()

    format_instructions = output_parser.get_format_instructions()prompt = PromptTemplate(    template="List five {subject}.\n{format_instructions}",    input_variables=["subject"],    partial_variables={"format_instructions": format_instructions})

    model = OpenAI(temperature=0)

    _input = prompt.format(subject="ice cream flavors")output = model(_input)

    output_parser.parse(output)

        ['Vanilla',     'Chocolate',     'Strawberry',     'Mint Chocolate Chip',     'Cookies and Cream']