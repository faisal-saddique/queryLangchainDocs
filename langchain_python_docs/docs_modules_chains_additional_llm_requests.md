HTTP request chain
==================

Using the request library to get HTML results from a URL and then an LLM to parse results

    from langchain.llms import OpenAIfrom langchain.chains import LLMRequestsChain, LLMChain

    from langchain.prompts import PromptTemplatetemplate = """Between >>> and <<< are the raw search result text from google.Extract the answer to the question '{query}' or say "not found" if the information is not contained.Use the formatExtracted:<answer or "not found">>>> {requests_result} <<<Extracted:"""PROMPT = PromptTemplate(    input_variables=["query", "requests_result"],    template=template,)

    chain = LLMRequestsChain(llm_chain=LLMChain(llm=OpenAI(temperature=0), prompt=PROMPT))

    question = "What are the Three (3) biggest countries, and their respective sizes?"inputs = {    "query": question,    "url": "https://www.google.com/search?q=" + question.replace(" ", "+"),}

    chain(inputs)

        {'query': 'What are the Three (3) biggest countries, and their respective sizes?',     'url': 'https://www.google.com/search?q=What+are+the+Three+(3)+biggest+countries,+and+their+respective+sizes?',     'output': ' Russia (17,098,242 km²), Canada (9,984,670 km²), United States (9,826,675 km²)'}