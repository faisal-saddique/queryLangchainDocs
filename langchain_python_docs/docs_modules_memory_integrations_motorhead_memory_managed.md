Motörhead Memory (Managed)
==========================

[Motörhead](https://github.com/getmetal/motorhead) is a memory server implemented in Rust. It automatically handles incremental summarization in the background and allows for stateless applications.

Setup[​](#setup "Direct link to Setup")
---------------------------------------

See instructions at [Motörhead](https://docs.getmetal.io/motorhead/introduction) for running the managed version of Motorhead. You can retrieve your `api_key` and `client_id` by creating an account on [Metal](https://getmetal.io).

    from langchain.memory.motorhead_memory import MotorheadMemoryfrom langchain import OpenAI, LLMChain, PromptTemplatetemplate = """You are a chatbot having a conversation with a human.{chat_history}Human: {human_input}AI:"""prompt = PromptTemplate(    input_variables=["chat_history", "human_input"],     template=template)memory = MotorheadMemory(    api_key="YOUR_API_KEY",    client_id="YOUR_CLIENT_ID"    session_id="testing-1",    memory_key="chat_history")await memory.init();  # loads previous state from Motörhead 🤘llm_chain = LLMChain(    llm=OpenAI(),     prompt=prompt,     verbose=True,     memory=memory,)

    llm_chain.run("hi im bob")

                > Entering new LLMChain chain...    Prompt after formatting:    You are a chatbot having a conversation with a human.            Human: hi im bob    AI:        > Finished chain.    ' Hi Bob, nice to meet you! How are you doing today?'

    llm_chain.run("whats my name?")

                > Entering new LLMChain chain...    Prompt after formatting:    You are a chatbot having a conversation with a human.        Human: hi im bob    AI:  Hi Bob, nice to meet you! How are you doing today?    Human: whats my name?    AI:        > Finished chain.    ' You said your name is Bob. Is that correct?'

    llm_chain.run("whats for dinner?")

                > Entering new LLMChain chain...    Prompt after formatting:    You are a chatbot having a conversation with a human.        Human: hi im bob    AI:  Hi Bob, nice to meet you! How are you doing today?    Human: whats my name?    AI:  You said your name is Bob. Is that correct?    Human: whats for dinner?    AI:        > Finished chain.    "  I'm sorry, I'm not sure what you're asking. Could you please rephrase your question?"