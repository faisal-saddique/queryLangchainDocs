SimpleSequentialChainInput
==========================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`ChainInputs`](/docs/api/chains/interfaces/ChainInputs).**SimpleSequentialChainInput**

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### chains[](#chains "Direct link to chains")

> **chains**: [`BaseChain`](/docs/api/chains/classes/BaseChain)<[`ChainValues`](/docs/api/schema/types/ChainValues), [`ChainValues`](/docs/api/schema/types/ChainValues)\>\[\]

Array of chains to run as a sequence. The chains are run in order they appear in the array.

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/chains/sequential\_chain.ts:190](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/sequential_chain.ts#L190)

### callbackManager?[](#callbackmanager "Direct link to callbackManager?")

> **callbackManager**: [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Deprecated[](#deprecated "Direct link to Deprecated")

Use `callbacks` instead

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[callbackManager](/docs/api/chains/interfaces/ChainInputs#callbackmanager)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/chains/base.ts:22](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L22)

### callbacks?[](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[callbacks](/docs/api/chains/interfaces/ChainInputs#callbacks)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:25](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L25)

### memory?[](#memory "Direct link to memory?")

> **memory**: [`BaseMemory`](/docs/api/memory/classes/BaseMemory)

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[memory](/docs/api/chains/interfaces/ChainInputs#memory)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/chains/base.ts:17](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L17)

### metadata?[](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[metadata](/docs/api/chains/interfaces/ChainInputs#metadata)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:27](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L27)

### tags?[](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[tags](/docs/api/chains/interfaces/ChainInputs#tags)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L26)

### trimOutputs?[](#trimoutputs "Direct link to trimOutputs?")

> **trimOutputs**: `boolean`

Whether or not to trim the intermediate outputs.

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/chains/sequential\_chain.ts:192](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/sequential_chain.ts#L192)

### verbose?[](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[verbose](/docs/api/chains/interfaces/ChainInputs#verbose)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:24](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L24)