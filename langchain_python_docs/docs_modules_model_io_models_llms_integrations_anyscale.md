Anyscale
========

[Anyscale](https://www.anyscale.com/) is a fully-managed [Ray](https://www.ray.io/) platform, on which you can build, deploy, and manage scalable AI and Python applications

This example goes over how to use LangChain to interact with `Anyscale` [service](https://docs.anyscale.com/productionize/services-v2/get-started).

It will send the requests to Anyscale Service endpoint, which is concatenate `ANYSCALE_SERVICE_URL` and `ANYSCALE_SERVICE_ROUTE`, with a token defined in `ANYSCALE_SERVICE_TOKEN`

    import osos.environ["ANYSCALE_SERVICE_URL"] = ANYSCALE_SERVICE_URLos.environ["ANYSCALE_SERVICE_ROUTE"] = ANYSCALE_SERVICE_ROUTEos.environ["ANYSCALE_SERVICE_TOKEN"] = ANYSCALE_SERVICE_TOKEN

    from langchain.llms import Anyscalefrom langchain import PromptTemplate, LLMChain

    template = """Question: {question}Answer: Let's think step by step."""prompt = PromptTemplate(template=template, input_variables=["question"])

    llm = Anyscale()

    llm_chain = LLMChain(prompt=prompt, llm=llm)

    question = "When was George Washington president?"llm_chain.run(question)

With Ray, we can distribute the queries without asyncrhonized implementation. This not only applies to Anyscale LLM model, but to any other Langchain LLM models which do not have `_acall` or `_agenerate` implemented

    prompt_list = [    "When was George Washington president?",    "Explain to me the difference between nuclear fission and fusion.",    "Give me a list of 5 science fiction books I should read next.",    "Explain the difference between Spark and Ray.",    "Suggest some fun holiday ideas.",    "Tell a joke.",    "What is 2+2?",    "Explain what is machine learning like I am five years old.",    "Explain what is artifical intelligence.",]

    import ray@ray.remotedef send_query(llm, prompt):    resp = llm(prompt)    return respfutures = [send_query.remote(llm, prompt) for prompt in prompt_list]results = ray.get(futures)