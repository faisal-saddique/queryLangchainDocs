Redis Chat Message History
==========================

This notebook goes over how to use Redis to store chat message history.

    from langchain.memory import RedisChatMessageHistoryhistory = RedisChatMessageHistory("foo")history.add_user_message("hi!")history.add_ai_message("whats up?")

    history.messages

        [AIMessage(content='whats up?', additional_kwargs={}),     HumanMessage(content='hi!', additional_kwargs={})]