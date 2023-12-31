Tools
=====

Tools are interfaces that an agent can use to interact with the world.

Get started[](#get-started "Direct link to Get started")
---------------------------------------------------------

Tools are functions that agents can use to interact with the world. These tools can be generic utilities (e.g. search), other chains, or even other agents.

Specifically, the interface of a tool has a single text input and a single text output. It includes a name and description that communicate to the model what the tool does and when to use it.

    interface Tool {  call(arg: string): Promise<string>;  name: string;  description: string;}

Advanced[](#advanced "Direct link to Advanced")
------------------------------------------------

To implement your own tool you can subclass the `Tool` class and implement the `_call` method. The `_call` method is called with the input text and should return the output text. The Tool superclass implements the `call` method, which takes care of calling the right CallbackManager methods before and after calling your `_call` method. When an error occurs, the `_call` method should when possible return a string representing an error, rather than throwing an error. This allows the error to be passed to the LLM and the LLM can decide how to handle it. If an error is thrown then execution of the agent will stop.

    abstract class Tool {  abstract _call(arg: string): Promise<string>;  abstract name: string;  abstract description: string;}