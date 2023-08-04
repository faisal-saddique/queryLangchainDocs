Creating custom callback handlers
=================================

You can also create your own handler by implementing the `BaseCallbackHandler` interface. This is useful if you want to do something more complex than just logging to the console, eg. send the events to a logging service. As an example here is a simple implementation of a handler that logs to the console:

    import { BaseCallbackHandler } from "langchain/callbacks";import { Serialized } from "langchain/load/serializable";import { AgentAction, AgentFinish, ChainValues } from "langchain/schema";export class MyCallbackHandler extends BaseCallbackHandler {  name = "MyCallbackHandler";  async handleChainStart(chain: Serialized) {    console.log(`Entering new ${chain.id} chain...`);  }  async handleChainEnd(_output: ChainValues) {    console.log("Finished chain.");  }  async handleAgentAction(action: AgentAction) {    console.log(action.log);  }  async handleToolEnd(output: string) {    console.log(output);  }  async handleText(text: string) {    console.log(text);  }  async handleAgentEnd(action: AgentFinish) {    console.log(action.log);  }}

#### API Reference:

*   [BaseCallbackHandler](/docs/api/callbacks/classes/BaseCallbackHandler) from `langchain/callbacks`
*   [Serialized](/docs/api/load_serializable/types/Serialized) from `langchain/load/serializable`
*   [AgentAction](/docs/api/schema/types/AgentAction) from `langchain/schema`
*   [AgentFinish](/docs/api/schema/types/AgentFinish) from `langchain/schema`
*   [ChainValues](/docs/api/schema/types/ChainValues) from `langchain/schema`

You could then use it as described in the [section](#built-in-handlers) above.