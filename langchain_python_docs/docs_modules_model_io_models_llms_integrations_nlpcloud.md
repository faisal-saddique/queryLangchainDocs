NLP Cloud
=========

The [NLP Cloud](https://nlpcloud.io) serves high performance pre-trained or custom models for NER, sentiment-analysis, classification, summarization, paraphrasing, grammar and spelling correction, keywords and keyphrases extraction, chatbot, product description and ad generation, intent classification, text generation, image generation, blog post generation, code generation, question answering, automatic speech recognition, machine translation, language detection, semantic search, semantic similarity, tokenization, POS tagging, embeddings, and dependency parsing. It is ready for production, served through a REST API.

This example goes over how to use LangChain to interact with `NLP Cloud` [models](https://docs.nlpcloud.com/#models).

    pip install nlpcloud

    # get a token: https://docs.nlpcloud.com/#authenticationfrom getpass import getpassNLPCLOUD_API_KEY = getpass()

         ········

    import osos.environ["NLPCLOUD_API_KEY"] = NLPCLOUD_API_KEY

    from langchain.llms import NLPCloudfrom langchain import PromptTemplate, LLMChain

    template = """Question: {question}Answer: Let's think step by step."""prompt = PromptTemplate(template=template, input_variables=["question"])

    llm = NLPCloud()

    llm_chain = LLMChain(prompt=prompt, llm=llm)

    question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"llm_chain.run(question)

        ' Justin Bieber was born in 1994, so the team that won the Super Bowl that year was the San Francisco 49ers.'