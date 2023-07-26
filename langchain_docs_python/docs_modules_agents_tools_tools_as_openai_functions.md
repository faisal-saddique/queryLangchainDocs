Tools as OpenAI Functions
=========================

This notebook goes over how to use LangChain tools as OpenAI functions.

    from langchain.chat_models import ChatOpenAIfrom langchain.schema import HumanMessage

    model = ChatOpenAI(model="gpt-3.5-turbo-0613")

    from langchain.tools import MoveFileTool, format_tool_to_openai_function

    tools = [MoveFileTool()]functions = [format_tool_to_openai_function(t) for t in tools]

    message = model.predict_messages(    [HumanMessage(content="move file foo to bar")], functions=functions)

    message

        AIMessage(content='', additional_kwargs={'function_call': {'name': 'move_file', 'arguments': '{\n  "source_path": "foo",\n  "destination_path": "bar"\n}'}}, example=False)

    message.additional_kwargs["function_call"]

        {'name': 'move_file',     'arguments': '{\n  "source_path": "foo",\n  "destination_path": "bar"\n}'}