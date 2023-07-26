Introduction
============

**LangChain** is a framework for developing applications powered by language models. It enables applications that are:

*   **Data-aware**: connect a language model to other sources of data
*   **Agentic**: allow a language model to interact with its environment

The main value props of LangChain are:

1.  **Components**: abstractions for working with language models, along with a collection of implementations for each abstraction. Components are modular and easy-to-use, whether you are using the rest of the LangChain framework or not
2.  **Off-the-shelf chains**: a structured assembly of components for accomplishing specific higher-level tasks

Off-the-shelf chains make it easy to get started. For more complex applications and nuanced use-cases, components make it easy to customize existing chains or build new ones.

Get started[](#get-started "Direct link to Get started")
---------------------------------------------------------

[Here’s](/docs/get_started/installation.html) how to install LangChain, set up your environment, and start building.

We recommend following our [Quickstart](/docs/get_started/quickstart.html) guide to familiarize yourself with the framework by building your first LangChain application.

_**Note**: These docs are for the LangChain [Python package](https://github.com/hwchase17/langchain). For documentation on [LangChain.js](https://github.com/hwchase17/langchainjs), the JS/TS version, [head here](https://js.langchain.com/docs)._

Modules[](#modules "Direct link to Modules")
---------------------------------------------

LangChain provides standard, extendable interfaces and external integrations for the following modules, listed from least to most complex:

#### [Model I/O](/docs/modules/model_io/)[](#model-io "Direct link to model-io")

Interface with language models

#### [Data connection](/docs/modules/data_connection/)[](#data-connection "Direct link to data-connection")

Interface with application-specific data

#### [Chains](/docs/modules/chains/)[](#chains "Direct link to chains")

Construct sequences of calls

#### [Agents](/docs/modules/agents/)[](#agents "Direct link to agents")

Let chains choose which tools to use given high-level directives

#### [Memory](/docs/modules/memory/)[](#memory "Direct link to memory")

Persist application state between runs of a chain

#### [Callbacks](/docs/modules/callbacks/)[](#callbacks "Direct link to callbacks")

Log and stream intermediate steps of any chain

Examples, ecosystem, and resources[](#examples-ecosystem-and-resources "Direct link to Examples, ecosystem, and resources")
----------------------------------------------------------------------------------------------------------------------------

### [Use cases](/docs/use_cases/)[](#use-cases "Direct link to use-cases")

Walkthroughs and best-practices for common end-to-end use cases, like:

*   [Chatbots](/docs/use_cases/chatbots/)
*   [Answering questions using sources](/docs/use_cases/question_answering/)
*   [Analyzing structured data](/docs/use_cases/tabular.html)
*   and much more...

### [Guides](/docs/guides/)[](#guides "Direct link to guides")

Learn best practices for developing with LangChain.

### [Ecosystem](/docs/ecosystem/)[](#ecosystem "Direct link to ecosystem")

LangChain is part of a rich ecosystem of tools that integrate with our framework and build on top of it. Check out our growing list of [integrations](/docs/integrations/) and [dependent repos](/docs/ecosystem/dependents).

### [Additional resources](/docs/additional_resources/)[](#additional-resources "Direct link to additional-resources")

Our community is full of prolific developers, creative builders, and fantastic teachers. Check out [YouTube tutorials](/docs/additional_resources/youtube.html) for great tutorials from folks in the community, and [Gallery](https://github.com/kyrolabs/awesome-langchain) for a list of awesome LangChain projects, compiled by the folks at [KyroLabs](https://kyrolabs.com).

### Support

Join us on [GitHub](https://github.com/hwchase17/langchain) or [Discord](https://discord.gg/6adMQxSpJS) to ask questions, share feedback, meet other developers building with LangChain, and dream about the future of LLM’s.

API reference[](#api-reference "Direct link to API reference")
---------------------------------------------------------------

Head to the [reference](https://api.python.langchain.com) section for full documentation of all classes and methods in the LangChain Python package.