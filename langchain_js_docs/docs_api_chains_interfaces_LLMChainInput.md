LLMChainInput<T, L\>
====================

Type parameters[​](#type-parameters "Direct link to Type parameters")
---------------------------------------------------------------------

*   `T` _extends_ `string` | `object` = `string`
*   `L` _extends_ [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel) = [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`ChainInputs`](/docs/api/chains/interfaces/ChainInputs).**LLMChainInput**

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### llm[​](#llm "Direct link to llm")

> **llm**: `L`

LLM Wrapper to use

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/chains/llm\_chain.ts:21](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/llm_chain.ts#L21)

### prompt[​](#prompt "Direct link to prompt")

> **prompt**: [`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)

Prompt object to use

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/chains/llm\_chain.ts:19](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/llm_chain.ts#L19)

### callbackManager?[​](#callbackmanager "Direct link to callbackManager?")

> **callbackManager**: [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Deprecated[​](#deprecated "Direct link to Deprecated")

Use `callbacks` instead

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[callbackManager](/docs/api/chains/interfaces/ChainInputs#callbackmanager)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/chains/base.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L22)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[callbacks](/docs/api/chains/interfaces/ChainInputs#callbacks)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L23)

### llmKwargs?[​](#llmkwargs "Direct link to llmKwargs?")

> **llmKwargs**: `L`\["CallOptions"\]

Kwargs to pass to LLM

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/chains/llm\_chain.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/llm_chain.ts#L23)

### memory?[​](#memory "Direct link to memory?")

> **memory**: [`BaseMemory`](/docs/api/memory/classes/BaseMemory)

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[memory](/docs/api/chains/interfaces/ChainInputs#memory)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/chains/base.ts:17](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L17)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[metadata](/docs/api/chains/interfaces/ChainInputs#metadata)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:25](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L25)

### outputKey?[​](#outputkey "Direct link to outputKey?")

> **outputKey**: `string`

Key to use for output, defaults to `text`

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/chains/llm\_chain.ts:27](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/llm_chain.ts#L27)

### outputParser?[​](#outputparser "Direct link to outputParser?")

> **outputParser**: [`BaseLLMOutputParser`](/docs/api/schema_output_parser/classes/BaseLLMOutputParser)<`T`\>

OutputParser to use

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/chains/llm\_chain.ts:25](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/llm_chain.ts#L25)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[tags](/docs/api/chains/interfaces/ChainInputs#tags)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:24](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L24)

### verbose?[​](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[verbose](/docs/api/chains/interfaces/ChainInputs#verbose)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L22)