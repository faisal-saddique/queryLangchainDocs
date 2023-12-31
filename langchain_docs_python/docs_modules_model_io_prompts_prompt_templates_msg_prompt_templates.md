Types of `MessagePromptTemplate`
================================

LangChain provides different types of `MessagePromptTemplate`. The most commonly used are `AIMessagePromptTemplate`, `SystemMessagePromptTemplate` and `HumanMessagePromptTemplate`, which create an AI message, system message and human message respectively.

However, in cases where the chat model supports taking chat message with arbitrary role, you can use `ChatMessagePromptTemplate`, which allows user to specify the role name.

    from langchain.prompts import ChatMessagePromptTemplateprompt = "May the {subject} be with you"chat_message_prompt = ChatMessagePromptTemplate.from_template(role="Jedi", template=prompt)chat_message_prompt.format(subject="force")

        ChatMessage(content='May the force be with you', additional_kwargs={}, role='Jedi')

LangChain also provides `MessagesPlaceholder`, which gives you full control of what messages to be rendered during formatting. This can be useful when you are uncertain of what role you should be using for your message prompt templates or when you wish to insert a list of messages during formatting.

    from langchain.prompts import MessagesPlaceholderhuman_prompt = "Summarize our conversation so far in {word_count} words."human_message_template = HumanMessagePromptTemplate.from_template(human_prompt)chat_prompt = ChatPromptTemplate.from_messages([MessagesPlaceholder(variable_name="conversation"), human_message_template])

    human_message = HumanMessage(content="What is the best way to learn programming?")ai_message = AIMessage(content="""\1. Choose a programming language: Decide on a programming language that you want to learn.2. Start with the basics: Familiarize yourself with the basic programming concepts such as variables, data types and control structures.3. Practice, practice, practice: The best way to learn programming is through hands-on experience\""")chat_prompt.format_prompt(conversation=[human_message, ai_message], word_count="10").to_messages()

        [HumanMessage(content='What is the best way to learn programming?', additional_kwargs={}),     AIMessage(content='1. Choose a programming language: Decide on a programming language that you want to learn. \n\n2. Start with the basics: Familiarize yourself with the basic programming concepts such as variables, data types and control structures.\n\n3. Practice, practice, practice: The best way to learn programming is through hands-on experience', additional_kwargs={}),     HumanMessage(content='Summarize our conversation so far in 10 words.', additional_kwargs={})]