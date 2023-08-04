LLMRouterChain
==============

Base interface that all chains must implement.

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`RouterChain`](/docs/api/chains/classes/RouterChain).**LLMRouterChain**

Implements[](#implements "Direct link to Implements")
------------------------------------------------------

*   [`LLMRouterChainInput`](/docs/api/chains/interfaces/LLMRouterChainInput)

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new LLMRouterChain**(`fields`: [`LLMRouterChainInput`](/docs/api/chains/interfaces/LLMRouterChainInput)): [`LLMRouterChain`](/docs/api/chains/classes/LLMRouterChain)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`fields`

[`LLMRouterChainInput`](/docs/api/chains/interfaces/LLMRouterChainInput)

#### Returns[](#returns "Direct link to Returns")

[`LLMRouterChain`](/docs/api/chains/classes/LLMRouterChain)

#### Overrides[](#overrides "Direct link to Overrides")

[RouterChain](/docs/api/chains/classes/RouterChain).[constructor](/docs/api/chains/classes/RouterChain#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/chains/router/llm\_router.ts:21](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/router/llm_router.ts#L21)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### lc\_kwargs[](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[lc\_kwargs](/docs/api/chains/classes/RouterChain#lc_kwargs)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L57)

### lc\_serializable[](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[lc\_serializable](/docs/api/chains/classes/RouterChain#lc_serializable)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L55)

### llmChain[](#llmchain "Direct link to llmChain")

> **llmChain**: [`LLMChain`](/docs/api/chains/classes/LLMChain)<[`RouterOutputSchema`](/docs/api/chains/types/RouterOutputSchema), [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>\>

#### Implementation of[](#implementation-of "Direct link to Implementation of")

[LLMRouterChainInput](/docs/api/chains/interfaces/LLMRouterChainInput).[llmChain](/docs/api/chains/interfaces/LLMRouterChainInput#llmchain)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/chains/router/llm\_router.ts:19](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/router/llm_router.ts#L19)

### verbose[](#verbose "Direct link to verbose")

> **verbose**: `boolean`

Whether to print out response text.

#### Implementation of[](#implementation-of-1 "Direct link to Implementation of")

[LLMRouterChainInput](/docs/api/chains/interfaces/LLMRouterChainInput).[verbose](/docs/api/chains/interfaces/LLMRouterChainInput#verbose)

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[verbose](/docs/api/chains/classes/RouterChain#verbose)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:44](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L44)

### callbacks?[](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Implementation of[](#implementation-of-2 "Direct link to Implementation of")

[LLMRouterChainInput](/docs/api/chains/interfaces/LLMRouterChainInput).[callbacks](/docs/api/chains/interfaces/LLMRouterChainInput#callbacks)

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[callbacks](/docs/api/chains/classes/RouterChain#callbacks)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L46)

### memory?[](#memory "Direct link to memory?")

> **memory**: [`BaseMemory`](/docs/api/memory/classes/BaseMemory)

#### Implementation of[](#implementation-of-3 "Direct link to Implementation of")

[LLMRouterChainInput](/docs/api/chains/interfaces/LLMRouterChainInput).[memory](/docs/api/chains/interfaces/LLMRouterChainInput#memory)

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[memory](/docs/api/chains/classes/RouterChain#memory)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/chains/base.ts:35](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L35)

### metadata?[](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Implementation of[](#implementation-of-4 "Direct link to Implementation of")

[LLMRouterChainInput](/docs/api/chains/interfaces/LLMRouterChainInput).[metadata](/docs/api/chains/interfaces/LLMRouterChainInput#metadata)

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[metadata](/docs/api/chains/classes/RouterChain#metadata)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:50](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L50)

### tags?[](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Implementation of[](#implementation-of-5 "Direct link to Implementation of")

[LLMRouterChainInput](/docs/api/chains/interfaces/LLMRouterChainInput).[tags](/docs/api/chains/interfaces/LLMRouterChainInput#tags)

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[tags](/docs/api/chains/classes/RouterChain#tags)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L48)

### lc\_runnable[](#lc_runnable "Direct link to lc_runnable")

> `Protected` **lc\_runnable**: `boolean` = `true`

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[lc\_runnable](/docs/api/chains/classes/RouterChain#lc_runnable)

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:34](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L34)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### inputKeys[](#inputkeys "Direct link to inputKeys")

> **inputKeys**(): `string`\[\]

#### Returns[](#returns-1 "Direct link to Returns")

`string`\[\]

#### Overrides[](#overrides-1 "Direct link to Overrides")

RouterChain.inputKeys

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/chains/router/llm\_router.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/router/llm_router.ts#L26)

#### Overrides[](#overrides-2 "Direct link to Overrides")

[RouterChain](/docs/api/chains/classes/RouterChain).[inputKeys](/docs/api/chains/classes/RouterChain#inputkeys)

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/chains/router/llm\_router.ts:26](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/router/llm_router.ts#L26)

### lc\_aliases[](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[](#returns-2 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

RouterChain.lc\_aliases

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

#### Inherited from[](#inherited-from-9 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[lc\_aliases](/docs/api/chains/classes/RouterChain#lc_aliases)

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

### lc\_attributes[](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-10 "Direct link to Inherited from")

RouterChain.lc\_attributes

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:52](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L52)

#### Inherited from[](#inherited-from-11 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[lc\_attributes](/docs/api/chains/classes/RouterChain#lc_attributes)

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:52](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L52)

### lc\_namespace[](#lc_namespace "Direct link to lc_namespace")

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

> **lc\_namespace**(): `string`\[\]

#### Returns[](#returns-4 "Direct link to Returns")

`string`\[\]

#### Inherited from[](#inherited-from-12 "Direct link to Inherited from")

RouterChain.lc\_namespace

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/chains/base.ts:37](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L37)

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[](#inherited-from-13 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[lc\_namespace](/docs/api/chains/classes/RouterChain#lc_namespace)

#### Defined in[](#defined-in-17 "Direct link to Defined in")

[langchain/src/chains/base.ts:37](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L37)

### lc\_secrets[](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[](#returns-5 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-14 "Direct link to Inherited from")

RouterChain.lc\_secrets

#### Defined in[](#defined-in-18 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

#### Inherited from[](#inherited-from-15 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[lc\_secrets](/docs/api/chains/classes/RouterChain#lc_secrets)

#### Defined in[](#defined-in-19 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

### outputKeys[](#outputkeys "Direct link to outputKeys")

> **outputKeys**(): `string`\[\]

#### Returns[](#returns-6 "Direct link to Returns")

`string`\[\]

#### Inherited from[](#inherited-from-16 "Direct link to Inherited from")

RouterChain.outputKeys

#### Defined in[](#defined-in-20 "Direct link to Defined in")

[langchain/src/chains/router/multi\_route.ts:25](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/router/multi_route.ts#L25)

#### Inherited from[](#inherited-from-17 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[outputKeys](/docs/api/chains/classes/RouterChain#outputkeys)

#### Defined in[](#defined-in-21 "Direct link to Defined in")

[langchain/src/chains/router/multi\_route.ts:25](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/router/multi_route.ts#L25)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### \_call()[](#_call "Direct link to _call")

Run the core logic of this chain and return the output

> **\_call**(`values`: [`ChainValues`](/docs/api/schema/types/ChainValues), `runManager`?: [`CallbackManagerForChainRun`](/docs/api/callbacks/classes/CallbackManagerForChainRun)): `Promise`<[`RouterOutputSchema`](/docs/api/chains/types/RouterOutputSchema)\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`values`

[`ChainValues`](/docs/api/schema/types/ChainValues)

`runManager?`

[`CallbackManagerForChainRun`](/docs/api/callbacks/classes/CallbackManagerForChainRun)

#### Returns[](#returns-7 "Direct link to Returns")

`Promise`<[`RouterOutputSchema`](/docs/api/chains/types/RouterOutputSchema)\>

#### Overrides[](#overrides-3 "Direct link to Overrides")

[RouterChain](/docs/api/chains/classes/RouterChain).[\_call](/docs/api/chains/classes/RouterChain#_call)

#### Defined in[](#defined-in-22 "Direct link to Defined in")

[langchain/src/chains/router/llm\_router.ts:30](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/router/llm_router.ts#L30)

### \_chainType()[](#_chaintype "Direct link to _chaintype")

Return the string type key uniquely identifying this class of chain.

> **\_chainType**(): `string`

#### Returns[](#returns-8 "Direct link to Returns")

`string`

#### Overrides[](#overrides-4 "Direct link to Overrides")

[RouterChain](/docs/api/chains/classes/RouterChain).[\_chainType](/docs/api/chains/classes/RouterChain#_chaintype)

#### Defined in[](#defined-in-23 "Direct link to Defined in")

[langchain/src/chains/router/llm\_router.ts:37](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/router/llm_router.ts#L37)

### \_patchConfig()[](#_patchconfig "Direct link to _patchconfig")

> **\_patchConfig**(`config`: `Partial`<`BaseCallbackConfig`\> = `{}`, `callbackManager`: `undefined` | [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager) = `undefined`): `Partial`<`BaseCallbackConfig`\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

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

#### Inherited from[](#inherited-from-18 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[\_patchConfig](/docs/api/chains/classes/RouterChain#_patchconfig)

#### Defined in[](#defined-in-24 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:146](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L146)

### \_streamIterator()[](#_streamiterator "Direct link to _streamiterator")

> **\_streamIterator**(`input`: [`ChainValues`](/docs/api/schema/types/ChainValues), `options`?: `Partial`<`BaseCallbackConfig`\>): `AsyncGenerator`<[`ChainValues`](/docs/api/schema/types/ChainValues), `any`, `unknown`\>

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

`input`

[`ChainValues`](/docs/api/schema/types/ChainValues)

`options?`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-10 "Direct link to Returns")

`AsyncGenerator`<[`ChainValues`](/docs/api/schema/types/ChainValues), `any`, `unknown`\>

#### Inherited from[](#inherited-from-19 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[\_streamIterator](/docs/api/chains/classes/RouterChain#_streamiterator)

#### Defined in[](#defined-in-25 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:86](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L86)

### apply()[](#apply "Direct link to apply()")

Call the chain on all inputs in the list

> **apply**(`inputs`: [`ChainValues`](/docs/api/schema/types/ChainValues)\[\], `config`?: ([`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`)\[\]): `Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\[\]\>

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

`inputs`

[`ChainValues`](/docs/api/schema/types/ChainValues)\[\]

`config?`

([`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`)\[\]

#### Returns[](#returns-11 "Direct link to Returns")

`Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\[\]\>

#### Inherited from[](#inherited-from-20 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[apply](/docs/api/chains/classes/RouterChain#apply)

#### Defined in[](#defined-in-26 "Direct link to Defined in")

[langchain/src/chains/base.ts:210](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L210)

### batch()[](#batch "Direct link to batch()")

> **batch**(`inputs`: [`ChainValues`](/docs/api/schema/types/ChainValues)\[\], `options`?: `Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\], `batchOptions`?: `object`): `Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\[\]\>

#### Parameters[](#parameters-5 "Direct link to Parameters")

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

#### Inherited from[](#inherited-from-21 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[batch](/docs/api/chains/classes/RouterChain#batch)

#### Defined in[](#defined-in-27 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:63](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L63)

### bind()[](#bind "Direct link to bind()")

> **bind**(`kwargs`: `Partial`<`BaseCallbackConfig`\>): [`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<[`ChainValues`](/docs/api/schema/types/ChainValues), [`ChainValues`](/docs/api/schema/types/ChainValues), `BaseCallbackConfig`\>

#### Parameters[](#parameters-6 "Direct link to Parameters")

Parameter

Type

`kwargs`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-13 "Direct link to Returns")

[`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<[`ChainValues`](/docs/api/schema/types/ChainValues), [`ChainValues`](/docs/api/schema/types/ChainValues), `BaseCallbackConfig`\>

#### Inherited from[](#inherited-from-22 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[bind](/docs/api/chains/classes/RouterChain#bind)

#### Defined in[](#defined-in-28 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:41](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L41)

### call()[](#call "Direct link to call()")

Run the core logic of this chain and add to output if desired.

Wraps \_call and handles memory.

> **call**(`values`: [`ChainValues`](/docs/api/schema/types/ChainValues) & {`signal`?: `AbortSignal`; `timeout`?: `number`;}, `config`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`, `tags`?: `string`\[\]): `Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\>

#### Parameters[](#parameters-7 "Direct link to Parameters")

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

#### Inherited from[](#inherited-from-23 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[call](/docs/api/chains/classes/RouterChain#call)

#### Defined in[](#defined-in-29 "Direct link to Defined in")

[langchain/src/chains/base.ts:155](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L155)

### invoke()[](#invoke "Direct link to invoke()")

> **invoke**(`input`: [`ChainValues`](/docs/api/schema/types/ChainValues), `config`?: `BaseCallbackConfig`): `Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\>

#### Parameters[](#parameters-8 "Direct link to Parameters")

Parameter

Type

`input`

[`ChainValues`](/docs/api/schema/types/ChainValues)

`config?`

`BaseCallbackConfig`

#### Returns[](#returns-15 "Direct link to Returns")

`Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\>

#### Inherited from[](#inherited-from-24 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[invoke](/docs/api/chains/classes/RouterChain#invoke)

#### Defined in[](#defined-in-30 "Direct link to Defined in")

[langchain/src/chains/base.ts:76](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L76)

### pipe()[](#pipe "Direct link to pipe()")

> **pipe**<NewRunOutput\>(`coerceable`: [`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<[`ChainValues`](/docs/api/schema/types/ChainValues), `NewRunOutput`\>): [`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<[`ChainValues`](/docs/api/schema/types/ChainValues), `NewRunOutput`\>

#### Type parameters[](#type-parameters "Direct link to Type parameters")

*   `NewRunOutput`

#### Parameters[](#parameters-9 "Direct link to Parameters")

Parameter

Type

`coerceable`

[`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<[`ChainValues`](/docs/api/schema/types/ChainValues), `NewRunOutput`\>

#### Returns[](#returns-16 "Direct link to Returns")

[`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<[`ChainValues`](/docs/api/schema/types/ChainValues), `NewRunOutput`\>

#### Inherited from[](#inherited-from-25 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[pipe](/docs/api/chains/classes/RouterChain#pipe)

#### Defined in[](#defined-in-31 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:153](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L153)

### route()[](#route "Direct link to route()")

> **route**(`inputs`: [`ChainValues`](/docs/api/schema/types/ChainValues), `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): `Promise`<`Route`\>

#### Parameters[](#parameters-10 "Direct link to Parameters")

Parameter

Type

`inputs`

[`ChainValues`](/docs/api/schema/types/ChainValues)

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Returns[](#returns-17 "Direct link to Returns")

`Promise`<`Route`\>

#### Inherited from[](#inherited-from-26 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[route](/docs/api/chains/classes/RouterChain#route)

#### Defined in[](#defined-in-32 "Direct link to Defined in")

[langchain/src/chains/router/multi\_route.ts:29](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/router/multi_route.ts#L29)

### run()[](#run "Direct link to run()")

> **run**(`input`: `any`, `config`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`): `Promise`<`string`\>

#### Parameters[](#parameters-11 "Direct link to Parameters")

Parameter

Type

`input`

`any`

`config?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`

#### Returns[](#returns-18 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[](#inherited-from-27 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[run](/docs/api/chains/classes/RouterChain#run)

#### Defined in[](#defined-in-33 "Direct link to Defined in")

[langchain/src/chains/base.ts:104](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L104)

### serialize()[](#serialize "Direct link to serialize()")

Return a json-like object representing this chain.

> **serialize**(): [`SerializedBaseChain`](/docs/api/chains/types/SerializedBaseChain)

#### Returns[](#returns-19 "Direct link to Returns")

[`SerializedBaseChain`](/docs/api/chains/types/SerializedBaseChain)

#### Inherited from[](#inherited-from-28 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[serialize](/docs/api/chains/classes/RouterChain#serialize)

#### Defined in[](#defined-in-34 "Direct link to Defined in")

[langchain/src/chains/base.ts:96](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L96)

### stream()[](#stream "Direct link to stream()")

> **stream**(`input`: [`ChainValues`](/docs/api/schema/types/ChainValues), `options`?: `Partial`<`BaseCallbackConfig`\>): `Promise`<`IterableReadableStream`<[`ChainValues`](/docs/api/schema/types/ChainValues)\>\>

#### Parameters[](#parameters-12 "Direct link to Parameters")

Parameter

Type

`input`

[`ChainValues`](/docs/api/schema/types/ChainValues)

`options?`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-20 "Direct link to Returns")

`Promise`<`IterableReadableStream`<[`ChainValues`](/docs/api/schema/types/ChainValues)\>\>

#### Inherited from[](#inherited-from-29 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[stream](/docs/api/chains/classes/RouterChain#stream)

#### Defined in[](#defined-in-35 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:93](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L93)

### toJSON()[](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[](#returns-21 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[](#inherited-from-30 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[toJSON](/docs/api/chains/classes/RouterChain#tojson)

#### Defined in[](#defined-in-36 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[](#returns-22 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[](#inherited-from-31 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[toJSONNotImplemented](/docs/api/chains/classes/RouterChain#tojsonnotimplemented)

#### Defined in[](#defined-in-37 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L151)

### deserialize()[](#deserialize "Direct link to deserialize()")

Load a chain from a json-like object describing it.

> `Static` **deserialize**(`data`: [`SerializedBaseChain`](/docs/api/chains/types/SerializedBaseChain), `values`: `LoadValues` = `{}`): `Promise`<[`BaseChain`](/docs/api/chains/classes/BaseChain)<[`ChainValues`](/docs/api/schema/types/ChainValues), [`ChainValues`](/docs/api/schema/types/ChainValues)\>\>

#### Parameters[](#parameters-13 "Direct link to Parameters")

Parameter

Type

`data`

[`SerializedBaseChain`](/docs/api/chains/types/SerializedBaseChain)

`values`

`LoadValues`

#### Returns[](#returns-23 "Direct link to Returns")

`Promise`<[`BaseChain`](/docs/api/chains/classes/BaseChain)<[`ChainValues`](/docs/api/schema/types/ChainValues), [`ChainValues`](/docs/api/schema/types/ChainValues)\>\>

#### Inherited from[](#inherited-from-32 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[deserialize](/docs/api/chains/classes/RouterChain#deserialize)

#### Defined in[](#defined-in-38 "Direct link to Defined in")

[langchain/src/chains/base.ts:222](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L222)

### fromLLM()[](#fromllm "Direct link to fromLLM()")

> `Static` **fromLLM**(`llm`: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>, `prompt`: [`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)<[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\>, `options`?: `Omit`<[`LLMRouterChainInput`](/docs/api/chains/interfaces/LLMRouterChainInput), "llmChain"\>): [`LLMRouterChain`](/docs/api/chains/classes/LLMRouterChain)

#### Parameters[](#parameters-14 "Direct link to Parameters")

Parameter

Type

`llm`

[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)<`any`, [`BaseLanguageModelCallOptions`](/docs/api/base_language/interfaces/BaseLanguageModelCallOptions)\>

`prompt`

[`BasePromptTemplate`](/docs/api/prompts/classes/BasePromptTemplate)<[`BasePromptValue`](/docs/api/schema/classes/BasePromptValue)\>

`options?`

`Omit`<[`LLMRouterChainInput`](/docs/api/chains/interfaces/LLMRouterChainInput), "llmChain"\>

#### Returns[](#returns-24 "Direct link to Returns")

[`LLMRouterChain`](/docs/api/chains/classes/LLMRouterChain)

#### Defined in[](#defined-in-39 "Direct link to Defined in")

[langchain/src/chains/router/llm\_router.ts:41](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/router/llm_router.ts#L41)

### isRunnable()[](#isrunnable "Direct link to isRunnable()")

> `Static` **isRunnable**(`thing`: `any`): thing is Runnable<any, any, BaseCallbackConfig\>

#### Parameters[](#parameters-15 "Direct link to Parameters")

Parameter

Type

`thing`

`any`

#### Returns[](#returns-25 "Direct link to Returns")

thing is Runnable<any, any, BaseCallbackConfig\>

#### Inherited from[](#inherited-from-33 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[isRunnable](/docs/api/chains/classes/RouterChain#isrunnable)

#### Defined in[](#defined-in-40 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:164](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L164)

### \_callWithConfig()[](#_callwithconfig "Direct link to _callwithconfig")

> `Protected` **\_callWithConfig**<T\>(`func`: `Function`, `input`: `T`, `options`?: `BaseCallbackConfig` & {`runType`?: `string`;}): `Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\>

#### Type parameters[](#type-parameters-1 "Direct link to Type parameters")

*   `T` _extends_ [`ChainValues`](/docs/api/schema/types/ChainValues)

#### Parameters[](#parameters-16 "Direct link to Parameters")

Parameter

Type

`func`

(`input`: `T`) => `Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\>

`input`

`T`

`options?`

`BaseCallbackConfig` & {`runType`?: `string`;}

#### Returns[](#returns-26 "Direct link to Returns")

`Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\>

#### Inherited from[](#inherited-from-34 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[\_callWithConfig](/docs/api/chains/classes/RouterChain#_callwithconfig)

#### Defined in[](#defined-in-41 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:117](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L117)

### \_formatValues()[](#_formatvalues "Direct link to _formatvalues")

> `Protected` **\_formatValues**(`values`: [`ChainValues`](/docs/api/schema/types/ChainValues) & {`signal`?: `AbortSignal`; `timeout`?: `number`;}): `Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues) & {`signal`?: `AbortSignal`; `timeout`?: `number`;}\>

#### Parameters[](#parameters-17 "Direct link to Parameters")

Parameter

Type

`values`

[`ChainValues`](/docs/api/schema/types/ChainValues) & {`signal`?: `AbortSignal`;  
`timeout`?: `number`;}

#### Returns[](#returns-27 "Direct link to Returns")

`Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues) & {`signal`?: `AbortSignal`; `timeout`?: `number`;}\>

#### Inherited from[](#inherited-from-35 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[\_formatValues](/docs/api/chains/classes/RouterChain#_formatvalues)

#### Defined in[](#defined-in-42 "Direct link to Defined in")

[langchain/src/chains/base.ts:131](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L131)

### \_getOptionsList()[](#_getoptionslist "Direct link to _getoptionslist")

> `Protected` **\_getOptionsList**(`options`: `Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\], `length`: `number` = `0`): `Partial`<`BaseCallbackConfig`\>\[\]

#### Parameters[](#parameters-18 "Direct link to Parameters")

Parameter

Type

Default value

`options`

`Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\]

`undefined`

`length`

`number`

`0`

#### Returns[](#returns-28 "Direct link to Returns")

`Partial`<`BaseCallbackConfig`\>\[\]

#### Inherited from[](#inherited-from-36 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[\_getOptionsList](/docs/api/chains/classes/RouterChain#_getoptionslist)

#### Defined in[](#defined-in-43 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L48)

### \_separateRunnableConfigFromCallOptions()[](#_separaterunnableconfigfromcalloptions "Direct link to _separaterunnableconfigfromcalloptions")

> `Protected` **\_separateRunnableConfigFromCallOptions**(`options`: `Partial`<`BaseCallbackConfig`\> = `{}`): \[`BaseCallbackConfig`, `Omit`<`Partial`<`BaseCallbackConfig`\>, _keyof_ `BaseCallbackConfig`\>\]

#### Parameters[](#parameters-19 "Direct link to Parameters")

Parameter

Type

`options`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-29 "Direct link to Returns")

\[`BaseCallbackConfig`, `Omit`<`Partial`<`BaseCallbackConfig`\>, _keyof_ `BaseCallbackConfig`\>\]

#### Inherited from[](#inherited-from-37 "Direct link to Inherited from")

[RouterChain](/docs/api/chains/classes/RouterChain).[\_separateRunnableConfigFromCallOptions](/docs/api/chains/classes/RouterChain#_separaterunnableconfigfromcalloptions)

#### Defined in[](#defined-in-44 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:102](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L102)