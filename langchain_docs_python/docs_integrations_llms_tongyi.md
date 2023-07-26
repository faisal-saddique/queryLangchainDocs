Tongyi Qwen
===========

Tongyi Qwen is a large-scale language model developed by Alibaba's Damo Academy. It is capable of understanding user intent through natural language understanding and semantic analysis, based on user input in natural language. It provides services and assistance to users in different domains and tasks. By providing clear and detailed instructions, you can obtain results that better align with your expectations.

    # Install the packagepip install dashscope

    # Get a new token: https://help.aliyun.com/document_detail/611472.html?spm=a2c4g.2399481.0.0from getpass import getpassDASHSCOPE_API_KEY = getpass()

        ········

    import osos.environ["DASHSCOPE_API_KEY"] = DASHSCOPE_API_KEY

    from langchain.llms import Tongyifrom langchain import PromptTemplate, LLMChain

    template = """Question: {question}Answer: Let's think step by step."""prompt = PromptTemplate(template=template, input_variables=["question"])

    llm = Tongyi()

    llm_chain = LLMChain(prompt=prompt, llm=llm)

    question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"llm_chain.run(question)

        "The year Justin Bieber was born was 1994. The Denver Broncos won the Super Bowl in 1997, which means they would have been the team that won the Super Bowl during Justin Bieber's birth year. So the answer is the Denver Broncos."