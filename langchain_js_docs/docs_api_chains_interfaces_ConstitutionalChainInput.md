ConstitutionalChainInput
========================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`ChainInputs`](/docs/api/chains/interfaces/ChainInputs).**ConstitutionalChainInput**

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### chain[​](#chain "Direct link to chain")

> **chain**: [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/chains/constitutional\_ai/constitutional\_chain.ts:14](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/constitutional_ai/constitutional_chain.ts#L14)

### constitutionalPrinciples[​](#constitutionalprinciples "Direct link to constitutionalPrinciples")

> **constitutionalPrinciples**: [`ConstitutionalPrinciple`](/docs/api/chains/classes/ConstitutionalPrinciple)\[\]

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/chains/constitutional\_ai/constitutional\_chain.ts:15](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/constitutional_ai/constitutional_chain.ts#L15)

### critiqueChain[​](#critiquechain "Direct link to critiqueChain")

> **critiqueChain**: [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/chains/constitutional\_ai/constitutional\_chain.ts:16](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/constitutional_ai/constitutional_chain.ts#L16)

### revisionChain[​](#revisionchain "Direct link to revisionChain")

> **revisionChain**: [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/chains/constitutional\_ai/constitutional\_chain.ts:17](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/constitutional_ai/constitutional_chain.ts#L17)

### callbackManager?[​](#callbackmanager "Direct link to callbackManager?")

> **callbackManager**: [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Deprecated[​](#deprecated "Direct link to Deprecated")

Use `callbacks` instead

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[callbackManager](/docs/api/chains/interfaces/ChainInputs#callbackmanager)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/chains/base.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L22)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[callbacks](/docs/api/chains/interfaces/ChainInputs#callbacks)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L23)

### memory?[​](#memory "Direct link to memory?")

> **memory**: [`BaseMemory`](/docs/api/memory/classes/BaseMemory)

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[memory](/docs/api/chains/interfaces/ChainInputs#memory)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/chains/base.ts:17](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L17)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[metadata](/docs/api/chains/interfaces/ChainInputs#metadata)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:25](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L25)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[tags](/docs/api/chains/interfaces/ChainInputs#tags)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:24](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L24)

### verbose?[​](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[verbose](/docs/api/chains/interfaces/ChainInputs#verbose)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L22)