AutoGPT
=======

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new AutoGPT**(«destructured»: `Omit`<`Required`<[`AutoGPTInput`](/docs/api/experimental_autogpt/interfaces/AutoGPTInput)\>, "aiRole" | "humanInTheLoop"\> & {`chain`: [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>\>; `tools`: `ObjectTool`\[\]; `feedbackTool`?: [`Tool`](/docs/api/tools/classes/Tool);}): [`AutoGPT`](/docs/api/experimental_autogpt/classes/AutoGPT)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`«destructured»`

`Omit`<`Required`<[`AutoGPTInput`](/docs/api/experimental_autogpt/interfaces/AutoGPTInput)\>, "aiRole" | "humanInTheLoop"\> & {`chain`: [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>\>;  
`tools`: `ObjectTool`\[\];  
`feedbackTool`?: [`Tool`](/docs/api/tools/classes/Tool);}

#### Returns[](#returns "Direct link to Returns")

[`AutoGPT`](/docs/api/experimental_autogpt/classes/AutoGPT)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/experimental/autogpt/agent.ts:53](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/autogpt/agent.ts#L53)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### aiName[](#ainame "Direct link to aiName")

> **aiName**: `string`

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/experimental/autogpt/agent.ts:32](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/autogpt/agent.ts#L32)

### chain[](#chain "Direct link to chain")

> **chain**: [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>\>

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/experimental/autogpt/agent.ts:40](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/autogpt/agent.ts#L40)

### fullMessageHistory[](#fullmessagehistory "Direct link to fullMessageHistory")

> **fullMessageHistory**: [`BaseMessage`](/docs/api/schema/classes/BaseMessage)\[\]

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/experimental/autogpt/agent.ts:36](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/autogpt/agent.ts#L36)

### maxIterations[](#maxiterations "Direct link to maxIterations")

> **maxIterations**: `number`

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/experimental/autogpt/agent.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/autogpt/agent.ts#L48)

### memory[](#memory "Direct link to memory")

> **memory**: [`VectorStoreRetriever`](/docs/api/vectorstores_base/classes/VectorStoreRetriever)<[`VectorStore`](/docs/api/vectorstores_base/classes/VectorStore)\>

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/experimental/autogpt/agent.ts:34](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/autogpt/agent.ts#L34)

### nextActionCount[](#nextactioncount "Direct link to nextActionCount")

> **nextActionCount**: `number`

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/experimental/autogpt/agent.ts:38](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/autogpt/agent.ts#L38)

### outputParser[](#outputparser "Direct link to outputParser")

> **outputParser**: [`AutoGPTOutputParser`](/docs/api/experimental_autogpt/classes/AutoGPTOutputParser)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/experimental/autogpt/agent.ts:42](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/autogpt/agent.ts#L42)

### textSplitter[](#textsplitter "Direct link to textSplitter")

> **textSplitter**: [`TokenTextSplitter`](/docs/api/text_splitter/classes/TokenTextSplitter)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/experimental/autogpt/agent.ts:51](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/autogpt/agent.ts#L51)

### tools[](#tools "Direct link to tools")

> **tools**: `ObjectTool`\[\]

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/experimental/autogpt/agent.ts:44](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/autogpt/agent.ts#L44)

### feedbackTool?[](#feedbacktool "Direct link to feedbackTool?")

> **feedbackTool**: [`Tool`](/docs/api/tools/classes/Tool)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/experimental/autogpt/agent.ts:46](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/autogpt/agent.ts#L46)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### run()[](#run "Direct link to run()")

> **run**(`goals`: `string`\[\]): `Promise`<`undefined` | `string`\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`goals`

`string`\[\]

#### Returns[](#returns-1 "Direct link to Returns")

`Promise`<`undefined` | `string`\>

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/experimental/autogpt/agent.ts:120](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/autogpt/agent.ts#L120)

### fromLLMAndTools()[](#fromllmandtools "Direct link to fromLLMAndTools()")

> `Static` **fromLLMAndTools**(`llm`: [`BaseChatModel`](/docs/api/chat_models_base/classes/BaseChatModel)<[`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>, `tools`: `ObjectTool`\[\], «destructured»: [`AutoGPTInput`](/docs/api/experimental_autogpt/interfaces/AutoGPTInput)): [`AutoGPT`](/docs/api/experimental_autogpt/classes/AutoGPT)

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`llm`

[`BaseChatModel`](/docs/api/chat_models_base/classes/BaseChatModel)<[`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>

`tools`

`ObjectTool`\[\]

`«destructured»`

[`AutoGPTInput`](/docs/api/experimental_autogpt/interfaces/AutoGPTInput)

#### Returns[](#returns-2 "Direct link to Returns")

[`AutoGPT`](/docs/api/experimental_autogpt/classes/AutoGPT)

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/experimental/autogpt/agent.ts:86](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/experimental/autogpt/agent.ts#L86)