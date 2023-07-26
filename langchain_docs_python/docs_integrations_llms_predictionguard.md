Prediction Guard
================

    pip install predictionguard langchain

    import osimport predictionguard as pgfrom langchain.llms import PredictionGuardfrom langchain import PromptTemplate, LLMChain

Basic LLM usage[](#basic-llm-usage "Direct link to Basic LLM usage")
---------------------------------------------------------------------

    # Optional, add your OpenAI API Key. This is optional, as Prediction Guard allows# you to access all the latest open access models (see https://docs.predictionguard.com)os.environ["OPENAI_API_KEY"] = "<your OpenAI api key>"# Your Prediction Guard API key. Get one at predictionguard.comos.environ["PREDICTIONGUARD_TOKEN"] = "<your Prediction Guard access token>"

    pgllm = PredictionGuard(model="OpenAI-text-davinci-003")

    pgllm("Tell me a joke")

Control the output structure/ type of LLMs[](#control-the-output-structure-type-of-llms "Direct link to Control the output structure/ type of LLMs")
-----------------------------------------------------------------------------------------------------------------------------------------------------

    template = """Respond to the following query based on the context.Context: EVERY comment, DM + email suggestion has led us to this EXCITING announcement! 🎉 We have officially added TWO new candle subscription box options! 📦Exclusive Candle Box - $80 Monthly Candle Box - $45 (NEW!)Scent of The Month Box - $28 (NEW!)Head to stories to get ALLL the deets on each box! 👆 BONUS: Save 50% on your first box with code 50OFF! 🎉Query: {query}Result: """prompt = PromptTemplate(template=template, input_variables=["query"])

    # Without "guarding" or controlling the output of the LLM.pgllm(prompt.format(query="What kind of post is this?"))

    # With "guarding" or controlling the output of the LLM. See the# Prediction Guard docs (https://docs.predictionguard.com) to learn how to# control the output with integer, float, boolean, JSON, and other types and# structures.pgllm = PredictionGuard(    model="OpenAI-text-davinci-003",    output={        "type": "categorical",        "categories": ["product announcement", "apology", "relational"],    },)pgllm(prompt.format(query="What kind of post is this?"))

Chaining[](#chaining "Direct link to Chaining")
------------------------------------------------

    pgllm = PredictionGuard(model="OpenAI-text-davinci-003")

    template = """Question: {question}Answer: Let's think step by step."""prompt = PromptTemplate(template=template, input_variables=["question"])llm_chain = LLMChain(prompt=prompt, llm=pgllm, verbose=True)question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"llm_chain.predict(question=question)

    template = """Write a {adjective} poem about {subject}."""prompt = PromptTemplate(template=template, input_variables=["adjective", "subject"])llm_chain = LLMChain(prompt=prompt, llm=pgllm, verbose=True)llm_chain.predict(adjective="sad", subject="ducks")