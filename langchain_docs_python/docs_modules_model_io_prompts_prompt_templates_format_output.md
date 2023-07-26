Format template output
======================

The output of the format method is available as string, list of messages and `ChatPromptValue`

As string:

    output = chat_prompt.format(input_language="English", output_language="French", text="I love programming.")output

        'System: You are a helpful assistant that translates English to French.\nHuman: I love programming.'

    # or alternativelyoutput_2 = chat_prompt.format_prompt(input_language="English", output_language="French", text="I love programming.").to_string()assert output == output_2

As `ChatPromptValue`

    chat_prompt.format_prompt(input_language="English", output_language="French", text="I love programming.")

        ChatPromptValue(messages=[SystemMessage(content='You are a helpful assistant that translates English to French.', additional_kwargs={}), HumanMessage(content='I love programming.', additional_kwargs={})])

As list of Message objects

    chat_prompt.format_prompt(input_language="English", output_language="French", text="I love programming.").to_messages()

        [SystemMessage(content='You are a helpful assistant that translates English to French.', additional_kwargs={}),     HumanMessage(content='I love programming.', additional_kwargs={})]