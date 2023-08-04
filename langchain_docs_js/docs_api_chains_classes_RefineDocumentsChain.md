RefineDocumentsChain
====================

Combine documents by doing a first pass and then refining on more documents.

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseChain`](/docs/api/chains/classes/BaseChain).**RefineDocumentsChain**

Implements[](#implements "Direct link to Implements")
------------------------------------------------------

*   [`RefineDocumentsChainInput`](/docs/api/chains/interfaces/RefineDocumentsChainInput)

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new RefineDocumentsChain**(`fields`: [`RefineDocumentsChainInput`](/docs/api/chains/interfaces/RefineDocumentsChainInput)): [`RefineDocumentsChain`](/docs/api/chains/classes/RefineDocumentsChain)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`fields`

[`RefineDocumentsChainInput`](/docs/api/chains/interfaces/RefineDocumentsChainInput)

#### Returns[](#returns "Direct link to Returns")

[`RefineDocumentsChain`](/docs/api/chains/classes/RefineDocumentsChain)

#### Overrides[](#overrides "Direct link to Overrides")

[BaseChain](/docs/api/chains/classes/BaseChain).[constructor](/docs/api/chains/classes/BaseChain#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:333](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/combine_docs_chain.ts#L333)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### documentPrompt[](#documentprompt "Direct link to documentPrompt")

> **documentPrompt**: [`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)<[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\>

#### Implementation of[](#implementation-of "Direct link to Implementation of")

[RefineDocumentsChainInput](/docs/api/chains/interfaces/RefineDocumentsChainInput).[documentPrompt](/docs/api/chains/interfaces/RefineDocumentsChainInput#documentprompt)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:314](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/combine_docs_chain.ts#L314)

### documentVariableName[](#documentvariablename "Direct link to documentVariableName")

> **documentVariableName**: `string` = `"context"`

Variable name in the LLM chain to put the documents in

#### Implementation of[](#implementation-of-1 "Direct link to Implementation of")

[RefineDocumentsChainInput](/docs/api/chains/interfaces/RefineDocumentsChainInput).[documentVariableName](/docs/api/chains/interfaces/RefineDocumentsChainInput#documentvariablename)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:301](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/combine_docs_chain.ts#L301)

### initialResponseName[](#initialresponsename "Direct link to initialResponseName")

> **initialResponseName**: `string` = `"existing_answer"`

#### Implementation of[](#implementation-of-2 "Direct link to Implementation of")

[RefineDocumentsChainInput](/docs/api/chains/interfaces/RefineDocumentsChainInput).[initialResponseName](/docs/api/chains/interfaces/RefineDocumentsChainInput#initialresponsename)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:303](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/combine_docs_chain.ts#L303)

### inputKey[](#inputkey "Direct link to inputKey")

> **inputKey**: `string` = `"input_documents"`

#### Implementation of[](#implementation-of-3 "Direct link to Implementation of")

[RefineDocumentsChainInput](/docs/api/chains/interfaces/RefineDocumentsChainInput).[inputKey](/docs/api/chains/interfaces/RefineDocumentsChainInput#inputkey)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:297](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/combine_docs_chain.ts#L297)

### lc\_kwargs[](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[lc\_kwargs](/docs/api/chains/classes/BaseChain#lc_kwargs)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L57)

### lc\_serializable[](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[lc\_serializable](/docs/api/chains/classes/BaseChain#lc_serializable)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L55)

### llmChain[](#llmchain "Direct link to llmChain")

> **llmChain**: [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>\>

LLM Wrapper to use after formatting documents

#### Implementation of[](#implementation-of-4 "Direct link to Implementation of")

[RefineDocumentsChainInput](/docs/api/chains/interfaces/RefineDocumentsChainInput).[llmChain](/docs/api/chains/interfaces/RefineDocumentsChainInput#llmchain)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:295](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/combine_docs_chain.ts#L295)

### outputKey[](#outputkey "Direct link to outputKey")

> **outputKey**: `string` = `"output_text"`

#### Implementation of[](#implementation-of-5 "Direct link to Implementation of")

[RefineDocumentsChainInput](/docs/api/chains/interfaces/RefineDocumentsChainInput).[outputKey](/docs/api/chains/interfaces/RefineDocumentsChainInput#outputkey)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:299](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/combine_docs_chain.ts#L299)

### refineLLMChain[](#refinellmchain "Direct link to refineLLMChain")

> **refineLLMChain**: [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>\>

#### Implementation of[](#implementation-of-6 "Direct link to Implementation of")

[RefineDocumentsChainInput](/docs/api/chains/interfaces/RefineDocumentsChainInput).[refineLLMChain](/docs/api/chains/interfaces/RefineDocumentsChainInput#refinellmchain)

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:305](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/combine_docs_chain.ts#L305)

### verbose[](#verbose "Direct link to verbose")

> **verbose**: `boolean`

Whether to print out response text.

#### Implementation of[](#implementation-of-7 "Direct link to Implementation of")

[RefineDocumentsChainInput](/docs/api/chains/interfaces/RefineDocumentsChainInput).[verbose](/docs/api/chains/interfaces/RefineDocumentsChainInput#verbose)

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[verbose](/docs/api/chains/classes/BaseChain#verbose)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:44](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L44)

### callbacks?[](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Implementation of[](#implementation-of-8 "Direct link to Implementation of")

[RefineDocumentsChainInput](/docs/api/chains/interfaces/RefineDocumentsChainInput).[callbacks](/docs/api/chains/interfaces/RefineDocumentsChainInput#callbacks)

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[callbacks](/docs/api/chains/classes/BaseChain#callbacks)

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L46)

### memory?[](#memory "Direct link to memory?")

> **memory**: [`BaseMemory`](/docs/api/memory/classes/BaseMemory)

#### Implementation of[](#implementation-of-9 "Direct link to Implementation of")

[RefineDocumentsChainInput](/docs/api/chains/interfaces/RefineDocumentsChainInput).[memory](/docs/api/chains/interfaces/RefineDocumentsChainInput#memory)

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[memory](/docs/api/chains/classes/BaseChain#memory)

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/chains/base.ts:35](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L35)

### metadata?[](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Implementation of[](#implementation-of-10 "Direct link to Implementation of")

[RefineDocumentsChainInput](/docs/api/chains/interfaces/RefineDocumentsChainInput).[metadata](/docs/api/chains/interfaces/RefineDocumentsChainInput#metadata)

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[metadata](/docs/api/chains/classes/BaseChain#metadata)

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:50](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L50)

### tags?[](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Implementation of[](#implementation-of-11 "Direct link to Implementation of")

[RefineDocumentsChainInput](/docs/api/chains/interfaces/RefineDocumentsChainInput).[tags](/docs/api/chains/interfaces/RefineDocumentsChainInput#tags)

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[tags](/docs/api/chains/classes/BaseChain#tags)

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L48)

### lc\_runnable[](#lc_runnable "Direct link to lc_runnable")

> `Protected` **lc\_runnable**: `boolean` = `true`

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[lc\_runnable](/docs/api/chains/classes/BaseChain#lc_runnable)

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:34](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L34)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### defaultDocumentPrompt[](#defaultdocumentprompt "Direct link to defaultDocumentPrompt")

> **defaultDocumentPrompt**(): [`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)<[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\>

#### Returns[](#returns-1 "Direct link to Returns")

[`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)<[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\>

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:307](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/combine_docs_chain.ts#L307)

#### Defined in[](#defined-in-17 "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:307](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/combine_docs_chain.ts#L307)

### inputKeys[](#inputkeys "Direct link to inputKeys")

> **inputKeys**(): `string`\[\]

#### Returns[](#returns-2 "Direct link to Returns")

`string`\[\]

#### Overrides[](#overrides-1 "Direct link to Overrides")

BaseChain.inputKeys

#### Defined in[](#defined-in-18 "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:316](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/combine_docs_chain.ts#L316)

#### Overrides[](#overrides-2 "Direct link to Overrides")

[BaseChain](/docs/api/chains/classes/BaseChain).[inputKeys](/docs/api/chains/classes/BaseChain#inputkeys)

#### Defined in[](#defined-in-19 "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:316](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/combine_docs_chain.ts#L316)

### lc\_aliases[](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

BaseChain.lc\_aliases

#### Defined in[](#defined-in-20 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

#### Inherited from[](#inherited-from-9 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[lc\_aliases](/docs/api/chains/classes/BaseChain#lc_aliases)

#### Defined in[](#defined-in-21 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

### lc\_attributes[](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[](#returns-4 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-10 "Direct link to Inherited from")

BaseChain.lc\_attributes

#### Defined in[](#defined-in-22 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:52](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L52)

#### Inherited from[](#inherited-from-11 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[lc\_attributes](/docs/api/chains/classes/BaseChain#lc_attributes)

#### Defined in[](#defined-in-23 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:52](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L52)

### lc\_namespace[](#lc_namespace "Direct link to lc_namespace")

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

> **lc\_namespace**(): `string`\[\]

#### Returns[](#returns-5 "Direct link to Returns")

`string`\[\]

#### Inherited from[](#inherited-from-12 "Direct link to Inherited from")

BaseChain.lc\_namespace

#### Defined in[](#defined-in-24 "Direct link to Defined in")

[langchain/src/chains/base.ts:37](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L37)

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[](#inherited-from-13 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[lc\_namespace](/docs/api/chains/classes/BaseChain#lc_namespace)

#### Defined in[](#defined-in-25 "Direct link to Defined in")

[langchain/src/chains/base.ts:37](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L37)

### lc\_secrets[](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[](#returns-6 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-14 "Direct link to Inherited from")

BaseChain.lc\_secrets

#### Defined in[](#defined-in-26 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

#### Inherited from[](#inherited-from-15 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[lc\_secrets](/docs/api/chains/classes/BaseChain#lc_secrets)

#### Defined in[](#defined-in-27 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

### outputKeys[](#outputkeys "Direct link to outputKeys")

> **outputKeys**(): `string`\[\]

#### Returns[](#returns-7 "Direct link to Returns")

`string`\[\]

#### Overrides[](#overrides-3 "Direct link to Overrides")

BaseChain.outputKeys

#### Defined in[](#defined-in-28 "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:329](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/combine_docs_chain.ts#L329)

#### Overrides[](#overrides-4 "Direct link to Overrides")

[BaseChain](/docs/api/chains/classes/BaseChain).[outputKeys](/docs/api/chains/classes/BaseChain#outputkeys)

#### Defined in[](#defined-in-29 "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:329](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/combine_docs_chain.ts#L329)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### \_chainType()[](#_chaintype "Direct link to _chaintype")

Return the string type key uniquely identifying this class of chain.

> **\_chainType**(): "refine\_documents\_chain"

#### Returns[](#returns-8 "Direct link to Returns")

"refine\_documents\_chain"

#### Overrides[](#overrides-5 "Direct link to Overrides")

[BaseChain](/docs/api/chains/classes/BaseChain).[\_chainType](/docs/api/chains/classes/BaseChain#_chaintype)

#### Defined in[](#defined-in-30 "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:424](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/combine_docs_chain.ts#L424)

### \_patchConfig()[](#_patchconfig "Direct link to _patchconfig")

> **\_patchConfig**(`config`: `Partial`<`BaseCallbackConfig`\> = `{}`, `callbackManager`: `undefined` | [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager) = `undefined`): `Partial`<`BaseCallbackConfig`\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

Default value

`config`

`Partial`<`BaseCallbackConfig`\>

`{}`

`callbackManager`

`undefined` | [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

`undefined`

#### Returns[](#returns-9 "Direct link to Returns")

`Partial`<`BaseCallbackConfig`\>

#### Inherited from[](#inherited-from-16 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[\_patchConfig](/docs/api/chains/classes/BaseChain#_patchconfig)

#### Defined in[](#defined-in-31 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:146](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L146)

### \_streamIterator()[](#_streamiterator "Direct link to _streamiterator")

> **\_streamIterator**(`input`: [`ChainValues`](/docs/api/schema/types/ChainValues), `options`?: `Partial`<`BaseCallbackConfig`\>): `AsyncGenerator`<[`ChainValues`](/docs/api/schema/types/ChainValues), `any`, `unknown`\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`input`

[`ChainValues`](/docs/api/schema/types/ChainValues)

`options?`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-10 "Direct link to Returns")

`AsyncGenerator`<[`ChainValues`](/docs/api/schema/types/ChainValues), `any`, `unknown`\>

#### Inherited from[](#inherited-from-17 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[\_streamIterator](/docs/api/chains/classes/BaseChain#_streamiterator)

#### Defined in[](#defined-in-32 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:86](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L86)

### apply()[](#apply "Direct link to apply()")

Call the chain on all inputs in the list

> **apply**(`inputs`: [`ChainValues`](/docs/api/schema/types/ChainValues)\[\], `config`?: ([`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`)\[\]): `Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\[\]\>

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

`inputs`

[`ChainValues`](/docs/api/schema/types/ChainValues)\[\]

`config?`

([`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`)\[\]

#### Returns[](#returns-11 "Direct link to Returns")

`Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\[\]\>

#### Inherited from[](#inherited-from-18 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[apply](/docs/api/chains/classes/BaseChain#apply)

#### Defined in[](#defined-in-33 "Direct link to Defined in")

[langchain/src/chains/base.ts:210](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L210)

### batch()[](#batch "Direct link to batch()")

> **batch**(`inputs`: [`ChainValues`](/docs/api/schema/types/ChainValues)\[\], `options`?: `Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\], `batchOptions`?: `object`): `Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\[\]\>

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

`inputs`

[`ChainValues`](/docs/api/schema/types/ChainValues)\[\]

`options?`

`Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\]

`batchOptions?`

`object`

`batchOptions.maxConcurrency?`

`number`

#### Returns[](#returns-12 "Direct link to Returns")

`Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\[\]\>

#### Inherited from[](#inherited-from-19 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[batch](/docs/api/chains/classes/BaseChain#batch)

#### Defined in[](#defined-in-34 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:63](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L63)

### bind()[](#bind "Direct link to bind()")

> **bind**(`kwargs`: `Partial`<`BaseCallbackConfig`\>): [`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<[`ChainValues`](/docs/api/schema/types/ChainValues), [`ChainValues`](/docs/api/schema/types/ChainValues), `BaseCallbackConfig`\>

#### Parameters[](#parameters-5 "Direct link to Parameters")

Parameter

Type

`kwargs`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-13 "Direct link to Returns")

[`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<[`ChainValues`](/docs/api/schema/types/ChainValues), [`ChainValues`](/docs/api/schema/types/ChainValues), `BaseCallbackConfig`\>

#### Inherited from[](#inherited-from-20 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[bind](/docs/api/chains/classes/BaseChain#bind)

#### Defined in[](#defined-in-35 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:41](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L41)

### call()[](#call "Direct link to call()")

Run the core logic of this chain and add to output if desired.

Wraps \_call and handles memory.

> **call**(`values`: [`ChainValues`](/docs/api/schema/types/ChainValues) & {`signal`?: `AbortSignal`; `timeout`?: `number`;}, `config`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`, `tags`?: `string`\[\]): `Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\>

#### Parameters[](#parameters-6 "Direct link to Parameters")

Parameter

Type

Description

`values`

[`ChainValues`](/docs/api/schema/types/ChainValues) & {`signal`?: `AbortSignal`;  
`timeout`?: `number`;}

\-

`config?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`

\-

`tags?`

`string`\[\]

`Deprecated`  
  

#### Returns[](#returns-14 "Direct link to Returns")

`Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\>

#### Inherited from[](#inherited-from-21 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[call](/docs/api/chains/classes/BaseChain#call)

#### Defined in[](#defined-in-36 "Direct link to Defined in")

[langchain/src/chains/base.ts:155](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L155)

### invoke()[](#invoke "Direct link to invoke()")

> **invoke**(`input`: [`ChainValues`](/docs/api/schema/types/ChainValues), `config`?: `BaseCallbackConfig`): `Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\>

#### Parameters[](#parameters-7 "Direct link to Parameters")

Parameter

Type

`input`

[`ChainValues`](/docs/api/schema/types/ChainValues)

`config?`

`BaseCallbackConfig`

#### Returns[](#returns-15 "Direct link to Returns")

`Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\>

#### Inherited from[](#inherited-from-22 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[invoke](/docs/api/chains/classes/BaseChain#invoke)

#### Defined in[](#defined-in-37 "Direct link to Defined in")

[langchain/src/chains/base.ts:76](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L76)

### pipe()[](#pipe "Direct link to pipe()")

> **pipe**<NewRunOutput\>(`coerceable`: [`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<[`ChainValues`](/docs/api/schema/types/ChainValues), `NewRunOutput`\>): [`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<[`ChainValues`](/docs/api/schema/types/ChainValues), `NewRunOutput`\>

#### Type parameters[](#type-parameters "Direct link to Type parameters")

*   `NewRunOutput`

#### Parameters[](#parameters-8 "Direct link to Parameters")

Parameter

Type

`coerceable`

[`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<[`ChainValues`](/docs/api/schema/types/ChainValues), `NewRunOutput`\>

#### Returns[](#returns-16 "Direct link to Returns")

[`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<[`ChainValues`](/docs/api/schema/types/ChainValues), `NewRunOutput`\>

#### Inherited from[](#inherited-from-23 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[pipe](/docs/api/chains/classes/BaseChain#pipe)

#### Defined in[](#defined-in-38 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:153](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L153)

### run()[](#run "Direct link to run()")

> **run**(`input`: `any`, `config`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`): `Promise`<`string`\>

#### Parameters[](#parameters-9 "Direct link to Parameters")

Parameter

Type

`input`

`any`

`config?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`

#### Returns[](#returns-17 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[](#inherited-from-24 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[run](/docs/api/chains/classes/BaseChain#run)

#### Defined in[](#defined-in-39 "Direct link to Defined in")

[langchain/src/chains/base.ts:104](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L104)

### serialize()[](#serialize "Direct link to serialize()")

Return a json-like object representing this chain.

> **serialize**(): [`SerializedRefineDocumentsChain`](/docs/api/chains/types/SerializedRefineDocumentsChain)

#### Returns[](#returns-18 "Direct link to Returns")

[`SerializedRefineDocumentsChain`](/docs/api/chains/types/SerializedRefineDocumentsChain)

#### Overrides[](#overrides-6 "Direct link to Overrides")

[BaseChain](/docs/api/chains/classes/BaseChain).[serialize](/docs/api/chains/classes/BaseChain#serialize)

#### Defined in[](#defined-in-40 "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:447](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/combine_docs_chain.ts#L447)

### stream()[](#stream "Direct link to stream()")

> **stream**(`input`: [`ChainValues`](/docs/api/schema/types/ChainValues), `options`?: `Partial`<`BaseCallbackConfig`\>): `Promise`<`IterableReadableStream`<[`ChainValues`](/docs/api/schema/types/ChainValues)\>\>

#### Parameters[](#parameters-10 "Direct link to Parameters")

Parameter

Type

`input`

[`ChainValues`](/docs/api/schema/types/ChainValues)

`options?`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-19 "Direct link to Returns")

`Promise`<`IterableReadableStream`<[`ChainValues`](/docs/api/schema/types/ChainValues)\>\>

#### Inherited from[](#inherited-from-25 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[stream](/docs/api/chains/classes/BaseChain#stream)

#### Defined in[](#defined-in-41 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:93](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L93)

### toJSON()[](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[](#returns-20 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[](#inherited-from-26 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[toJSON](/docs/api/chains/classes/BaseChain#tojson)

#### Defined in[](#defined-in-42 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[](#returns-21 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[](#inherited-from-27 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[toJSONNotImplemented](/docs/api/chains/classes/BaseChain#tojsonnotimplemented)

#### Defined in[](#defined-in-43 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L151)

### deserialize()[](#deserialize "Direct link to deserialize()")

Load a chain from a json-like object describing it.

> `Static` **deserialize**(`data`: [`SerializedRefineDocumentsChain`](/docs/api/chains/types/SerializedRefineDocumentsChain)): `Promise`<[`RefineDocumentsChain`](/docs/api/chains/classes/RefineDocumentsChain)\>

#### Parameters[](#parameters-11 "Direct link to Parameters")

Parameter

Type

`data`

[`SerializedRefineDocumentsChain`](/docs/api/chains/types/SerializedRefineDocumentsChain)

#### Returns[](#returns-22 "Direct link to Returns")

`Promise`<[`RefineDocumentsChain`](/docs/api/chains/classes/RefineDocumentsChain)\>

#### Overrides[](#overrides-7 "Direct link to Overrides")

[BaseChain](/docs/api/chains/classes/BaseChain).[deserialize](/docs/api/chains/classes/BaseChain#deserialize)

#### Defined in[](#defined-in-44 "Direct link to Defined in")

[langchain/src/chains/combine\_docs\_chain.ts:428](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/combine_docs_chain.ts#L428)

### isRunnable()[](#isrunnable "Direct link to isRunnable()")

> `Static` **isRunnable**(`thing`: `any`): thing is Runnable<any, any, BaseCallbackConfig\>

#### Parameters[](#parameters-12 "Direct link to Parameters")

Parameter

Type

`thing`

`any`

#### Returns[](#returns-23 "Direct link to Returns")

thing is Runnable<any, any, BaseCallbackConfig\>

#### Inherited from[](#inherited-from-28 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[isRunnable](/docs/api/chains/classes/BaseChain#isrunnable)

#### Defined in[](#defined-in-45 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:164](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L164)

### \_callWithConfig()[](#_callwithconfig "Direct link to _callwithconfig")

> `Protected` **\_callWithConfig**<T\>(`func`: `Function`, `input`: `T`, `options`?: `BaseCallbackConfig` & {`runType`?: `string`;}): `Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\>

#### Type parameters[](#type-parameters-1 "Direct link to Type parameters")

*   `T` _extends_ [`ChainValues`](/docs/api/schema/types/ChainValues)

#### Parameters[](#parameters-13 "Direct link to Parameters")

Parameter

Type

`func`

(`input`: `T`) => `Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\>

`input`

`T`

`options?`

`BaseCallbackConfig` & {`runType`?: `string`;}

#### Returns[](#returns-24 "Direct link to Returns")

`Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\>

#### Inherited from[](#inherited-from-29 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[\_callWithConfig](/docs/api/chains/classes/BaseChain#_callwithconfig)

#### Defined in[](#defined-in-46 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:117](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L117)

### \_formatValues()[](#_formatvalues "Direct link to _formatvalues")

> `Protected` **\_formatValues**(`values`: [`ChainValues`](/docs/api/schema/types/ChainValues) & {`signal`?: `AbortSignal`; `timeout`?: `number`;}): `Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues) & {`signal`?: `AbortSignal`; `timeout`?: `number`;}\>

#### Parameters[](#parameters-14 "Direct link to Parameters")

Parameter

Type

`values`

[`ChainValues`](/docs/api/schema/types/ChainValues) & {`signal`?: `AbortSignal`;  
`timeout`?: `number`;}

#### Returns[](#returns-25 "Direct link to Returns")

`Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues) & {`signal`?: `AbortSignal`; `timeout`?: `number`;}\>

#### Inherited from[](#inherited-from-30 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[\_formatValues](/docs/api/chains/classes/BaseChain#_formatvalues)

#### Defined in[](#defined-in-47 "Direct link to Defined in")

[langchain/src/chains/base.ts:131](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L131)

### \_getOptionsList()[](#_getoptionslist "Direct link to _getoptionslist")

> `Protected` **\_getOptionsList**(`options`: `Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\], `length`: `number` = `0`): `Partial`<`BaseCallbackConfig`\>\[\]

#### Parameters[](#parameters-15 "Direct link to Parameters")

Parameter

Type

Default value

`options`

`Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\]

`undefined`

`length`

`number`

`0`

#### Returns[](#returns-26 "Direct link to Returns")

`Partial`<`BaseCallbackConfig`\>\[\]

#### Inherited from[](#inherited-from-31 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[\_getOptionsList](/docs/api/chains/classes/BaseChain#_getoptionslist)

#### Defined in[](#defined-in-48 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L48)

### \_separateRunnableConfigFromCallOptions()[](#_separaterunnableconfigfromcalloptions "Direct link to _separaterunnableconfigfromcalloptions")

> `Protected` **\_separateRunnableConfigFromCallOptions**(`options`: `Partial`<`BaseCallbackConfig`\> = `{}`): \[`BaseCallbackConfig`, `Omit`<`Partial`<`BaseCallbackConfig`\>, _keyof_ `BaseCallbackConfig`\>\]

#### Parameters[](#parameters-16 "Direct link to Parameters")

Parameter

Type

`options`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-27 "Direct link to Returns")

\[`BaseCallbackConfig`, `Omit`<`Partial`<`BaseCallbackConfig`\>, _keyof_ `BaseCallbackConfig`\>\]

#### Inherited from[](#inherited-from-32 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[\_separateRunnableConfigFromCallOptions](/docs/api/chains/classes/BaseChain#_separaterunnableconfigfromcalloptions)

#### Defined in[](#defined-in-49 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:102](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L102)