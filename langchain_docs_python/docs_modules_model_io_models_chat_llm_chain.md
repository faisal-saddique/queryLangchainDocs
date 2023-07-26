LLMChain
========

You can use the existing LLMChain in a very similar way to before - provide a prompt and a model.

    chain = LLMChain(llm=chat, prompt=chat_prompt)

    chain.run(input_language="English", output_language="French", text="I love programming.")

        "J'adore la programmation."