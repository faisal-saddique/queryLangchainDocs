Mongodb Chat Message History
============================

This notebook goes over how to use Mongodb to store chat message history.

MongoDB is a source-available cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas.

MongoDB is developed by MongoDB Inc. and licensed under the Server Side Public License (SSPL). - [Wikipedia](https://en.wikipedia.org/wiki/MongoDB)

    # Provide the connection string to connect to the MongoDB databaseconnection_string = "mongodb://mongo_user:password123@mongo:27017"

    from langchain.memory import MongoDBChatMessageHistorymessage_history = MongoDBChatMessageHistory(    connection_string=connection_string, session_id="test-session")message_history.add_user_message("hi!")message_history.add_ai_message("whats up?")

    message_history.messages

        [HumanMessage(content='hi!', additional_kwargs={}, example=False),     AIMessage(content='whats up?', additional_kwargs={}, example=False)]