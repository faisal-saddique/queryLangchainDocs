RefineDocumentsChainInput
=========================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`StuffDocumentsChainInput`](/docs/api/chains/interfaces/StuffDocumentsChainInput).**RefineDocumentsChainInput**

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### llmChain[](#llmchain "Direct link to llmChain")

> **llmChain**: [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>\>

LLM Wrapper to use after formatting documents

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[StuffDocumentsChainInput](/docs/api/chains/interfaces/StuffDocumentsChainInput).[llmChain](/docs/api/chains/interfaces/StuffDocumentsChainInput#llmchain)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:18](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/combine_docs_chain.ts#L18)

### refineLLMChain[](#refinellmchain "Direct link to refineLLMChain")

> **refineLLMChain**: [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>\>

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:279](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/combine_docs_chain.ts#L279)

### callbackManager?[](#callbackmanager "Direct link to callbackManager?")

> **callbackManager**: [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Deprecated[](#deprecated "Direct link to Deprecated")

Use `callbacks` instead

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[StuffDocumentsChainInput](/docs/api/chains/interfaces/StuffDocumentsChainInput).[callbackManager](/docs/api/chains/interfaces/StuffDocumentsChainInput#callbackmanager)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/chains/base.ts:22](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L22)

### callbacks?[](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[StuffDocumentsChainInput](/docs/api/chains/interfaces/StuffDocumentsChainInput).[callbacks](/docs/api/chains/interfaces/StuffDocumentsChainInput#callbacks)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:25](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L25)

### documentPrompt?[](#documentprompt "Direct link to documentPrompt?")

> **documentPrompt**: [`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)<[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\>

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:280](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/combine_docs_chain.ts#L280)

### documentVariableName?[](#documentvariablename "Direct link to documentVariableName?")

> **documentVariableName**: `string`

Variable name in the LLM chain to put the documents in

#### Overrides[](#overrides "Direct link to Overrides")

[StuffDocumentsChainInput](/docs/api/chains/interfaces/StuffDocumentsChainInput).[documentVariableName](/docs/api/chains/interfaces/StuffDocumentsChainInput#documentvariablename)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:282](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/combine_docs_chain.ts#L282)

### initialResponseName?[](#initialresponsename "Direct link to initialResponseName?")

> **initialResponseName**: `string`

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:281](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/combine_docs_chain.ts#L281)

### inputKey?[](#inputkey "Direct link to inputKey?")

> **inputKey**: `string`

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[StuffDocumentsChainInput](/docs/api/chains/interfaces/StuffDocumentsChainInput).[inputKey](/docs/api/chains/interfaces/StuffDocumentsChainInput#inputkey)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:19](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/combine_docs_chain.ts#L19)

### memory?[](#memory "Direct link to memory?")

> **memory**: [`BaseMemory`](/docs/api/memory/classes/BaseMemory)

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[StuffDocumentsChainInput](/docs/api/chains/interfaces/StuffDocumentsChainInput).[memory](/docs/api/chains/interfaces/StuffDocumentsChainInput#memory)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/chains/base.ts:17](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L17)

### metadata?[](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[StuffDocumentsChainInput](/docs/api/chains/interfaces/StuffDocumentsChainInput).[metadata](/docs/api/chains/interfaces/StuffDocumentsChainInput#metadata)

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:27](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L27)

### outputKey?[](#outputkey "Direct link to outputKey?")

> **outputKey**: `string`

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:283](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/combine_docs_chain.ts#L283)

### tags?[](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[StuffDocumentsChainInput](/docs/api/chains/interfaces/StuffDocumentsChainInput).[tags](/docs/api/chains/interfaces/StuffDocumentsChainInput#tags)

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L26)

### verbose?[](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

[StuffDocumentsChainInput](/docs/api/chains/interfaces/StuffDocumentsChainInput).[verbose](/docs/api/chains/interfaces/StuffDocumentsChainInput#verbose)

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:24](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L24)