APIChainInput
=============

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   `Omit`<[`ChainInputs`](/docs/api/chains/interfaces/ChainInputs), "memory"\>.**APIChainInput**

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### apiAnswerChain[​](#apianswerchain "Direct link to apiAnswerChain")

> **apiAnswerChain**: [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/chains/api/api\_chain.ts:14](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/api/api_chain.ts#L14)

### apiDocs[​](#apidocs "Direct link to apiDocs")

> **apiDocs**: `string`

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/chains/api/api\_chain.ts:16](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/api/api_chain.ts#L16)

### apiRequestChain[​](#apirequestchain "Direct link to apiRequestChain")

> **apiRequestChain**: [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/chains/api/api\_chain.ts:15](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/api/api_chain.ts#L15)

### callbackManager?[​](#callbackmanager "Direct link to callbackManager?")

> **callbackManager**: [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Deprecated[​](#deprecated "Direct link to Deprecated")

Use `callbacks` instead

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

Omit.callbackManager

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/chains/base.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L22)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

Omit.callbacks

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L23)

### headers?[​](#headers "Direct link to headers?")

> **headers**: `Record`<`string`, `string`\>

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/chains/api/api\_chain.ts:18](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/api/api_chain.ts#L18)

### inputKey?[​](#inputkey "Direct link to inputKey?")

> **inputKey**: `string`

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/chains/api/api\_chain.ts:17](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/api/api_chain.ts#L17)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

Omit.metadata

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:25](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L25)

### outputKey?[​](#outputkey "Direct link to outputKey?")

> **outputKey**: `string`

Key to use for output, defaults to `output`

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/chains/api/api\_chain.ts:20](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/api/api_chain.ts#L20)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

Omit.tags

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:24](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L24)

### verbose?[​](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

Omit.verbose

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L22)