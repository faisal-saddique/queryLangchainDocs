BaseChain<RunInput, RunOutput\>
===============================

Base interface that all chains must implement.

Type parameters[](#type-parameters "Direct link to Type parameters")
---------------------------------------------------------------------

*   `RunInput` _extends_ [`ChainValues`](/docs/api/schema/types/ChainValues) = [`ChainValues`](/docs/api/schema/types/ChainValues)
*   `RunOutput` _extends_ [`ChainValues`](/docs/api/schema/types/ChainValues) = [`ChainValues`](/docs/api/schema/types/ChainValues)

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseLangChain`](/docs/api/base_language/classes/BaseLangChain)<`RunInput`, `RunOutput`\>.**BaseChain**

Implements[](#implements "Direct link to Implements")
------------------------------------------------------

*   [`ChainInputs`](/docs/api/chains/interfaces/ChainInputs)

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new BaseChain**<RunInput, RunOutput\>(`fields`?: [`BaseMemory`](/docs/api/memory/classes/BaseMemory) | [`ChainInputs`](/docs/api/chains/interfaces/ChainInputs), `verbose`?: `boolean`, `callbacks`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks)): [`BaseChain`](/docs/api/chains/classes/BaseChain)<`RunInput`, `RunOutput`\>

#### Type parameters[](#type-parameters-1 "Direct link to Type parameters")

*   `RunInput` _extends_ [`ChainValues`](/docs/api/schema/types/ChainValues) = [`ChainValues`](/docs/api/schema/types/ChainValues)
*   `RunOutput` _extends_ [`ChainValues`](/docs/api/schema/types/ChainValues) = [`ChainValues`](/docs/api/schema/types/ChainValues)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

Description

`fields?`

[`BaseMemory`](/docs/api/memory/classes/BaseMemory) | [`ChainInputs`](/docs/api/chains/interfaces/ChainInputs)

\-

`verbose?`

`boolean`

`Deprecated`  
  

`callbacks?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks)

`Deprecated`  
  

#### Returns[](#returns "Direct link to Returns")

[`BaseChain`](/docs/api/chains/classes/BaseChain)<`RunInput`, `RunOutput`\>

#### Overrides[](#overrides "Direct link to Overrides")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[constructor](/docs/api/base_language/classes/BaseLangChain#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/chains/base.ts:41](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L41)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### lc\_kwargs[](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[lc\_kwargs](/docs/api/base_language/classes/BaseLangChain#lc_kwargs)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L57)

### lc\_serializable[](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[lc\_serializable](/docs/api/base_language/classes/BaseLangChain#lc_serializable)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L55)

### verbose[](#verbose "Direct link to verbose")

> **verbose**: `boolean`

Whether to print out response text.

#### Implementation of[](#implementation-of "Direct link to Implementation of")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[verbose](/docs/api/chains/interfaces/ChainInputs#verbose)

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[verbose](/docs/api/base_language/classes/BaseLangChain#verbose)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:44](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L44)

### callbacks?[](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Implementation of[](#implementation-of-1 "Direct link to Implementation of")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[callbacks](/docs/api/chains/interfaces/ChainInputs#callbacks)

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[callbacks](/docs/api/base_language/classes/BaseLangChain#callbacks)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L46)

### memory?[](#memory "Direct link to memory?")

> **memory**: [`BaseMemory`](/docs/api/memory/classes/BaseMemory)

#### Implementation of[](#implementation-of-2 "Direct link to Implementation of")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[memory](/docs/api/chains/interfaces/ChainInputs#memory)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/chains/base.ts:35](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L35)

### metadata?[](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Implementation of[](#implementation-of-3 "Direct link to Implementation of")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[metadata](/docs/api/chains/interfaces/ChainInputs#metadata)

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[metadata](/docs/api/base_language/classes/BaseLangChain#metadata)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:50](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L50)

### tags?[](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Implementation of[](#implementation-of-4 "Direct link to Implementation of")

[ChainInputs](/docs/api/chains/interfaces/ChainInputs).[tags](/docs/api/chains/interfaces/ChainInputs#tags)

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[tags](/docs/api/base_language/classes/BaseLangChain#tags)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L48)

### lc\_runnable[](#lc_runnable "Direct link to lc_runnable")

> `Protected` **lc\_runnable**: `boolean` = `true`

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[lc\_runnable](/docs/api/base_language/classes/BaseLangChain#lc_runnable)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:34](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L34)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### inputKeys[](#inputkeys "Direct link to inputKeys")

> `Abstract` **inputKeys**(): `string`\[\]

#### Returns[](#returns-1 "Direct link to Returns")

`string`\[\]

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/chains/base.ts:100](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L100)

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/chains/base.ts:100](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L100)

### lc\_aliases[](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[](#returns-2 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

BaseLangChain.lc\_aliases

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[lc\_aliases](/docs/api/base_language/classes/BaseLangChain#lc_aliases)

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

### lc\_attributes[](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-9 "Direct link to Inherited from")

BaseLangChain.lc\_attributes

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:52](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L52)

#### Inherited from[](#inherited-from-10 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[lc\_attributes](/docs/api/base_language/classes/BaseLangChain#lc_attributes)

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:52](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/base_language/index.ts#L52)

### lc\_namespace[](#lc_namespace "Direct link to lc_namespace")

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

> **lc\_namespace**(): `string`\[\]

#### Returns[](#returns-4 "Direct link to Returns")

`string`\[\]

#### Overrides[](#overrides-1 "Direct link to Overrides")

BaseLangChain.lc\_namespace

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/chains/base.ts:37](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L37)

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Overrides[](#overrides-2 "Direct link to Overrides")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[lc\_namespace](/docs/api/base_language/classes/BaseLangChain#lc_namespace)

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/chains/base.ts:37](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L37)

### lc\_secrets[](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[](#returns-5 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-11 "Direct link to Inherited from")

BaseLangChain.lc\_secrets

#### Defined in[](#defined-in-17 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

#### Inherited from[](#inherited-from-12 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[lc\_secrets](/docs/api/base_language/classes/BaseLangChain#lc_secrets)

#### Defined in[](#defined-in-18 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

### outputKeys[](#outputkeys "Direct link to outputKeys")

> `Abstract` **outputKeys**(): `string`\[\]

#### Returns[](#returns-6 "Direct link to Returns")

`string`\[\]

#### Defined in[](#defined-in-19 "Direct link to Defined in")

[langchain/src/chains/base.ts:102](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L102)

#### Defined in[](#defined-in-20 "Direct link to Defined in")

[langchain/src/chains/base.ts:102](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L102)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### \_call()[](#_call "Direct link to _call")

Run the core logic of this chain and return the output

> `Abstract` **\_call**(`values`: `RunInput`, `runManager`?: [`CallbackManagerForChainRun`](/docs/api/callbacks/classes/CallbackManagerForChainRun)): `Promise`<`RunOutput`\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`values`

`RunInput`

`runManager?`

[`CallbackManagerForChainRun`](/docs/api/callbacks/classes/CallbackManagerForChainRun)

#### Returns[](#returns-7 "Direct link to Returns")

`Promise`<`RunOutput`\>

#### Defined in[](#defined-in-21 "Direct link to Defined in")

[langchain/src/chains/base.ts:83](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L83)

### \_chainType()[](#_chaintype "Direct link to _chaintype")

Return the string type key uniquely identifying this class of chain.

> `Abstract` **\_chainType**(): `string`

#### Returns[](#returns-8 "Direct link to Returns")

`string`

#### Defined in[](#defined-in-22 "Direct link to Defined in")

[langchain/src/chains/base.ts:91](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L91)

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

#### Inherited from[](#inherited-from-13 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[\_patchConfig](/docs/api/base_language/classes/BaseLangChain#_patchconfig)

#### Defined in[](#defined-in-23 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:146](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L146)

### \_streamIterator()[](#_streamiterator "Direct link to _streamiterator")

> **\_streamIterator**(`input`: `RunInput`, `options`?: `Partial`<`BaseCallbackConfig`\>): `AsyncGenerator`<`RunOutput`, `any`, `unknown`\>

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

`input`

`RunInput`

`options?`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-10 "Direct link to Returns")

`AsyncGenerator`<`RunOutput`, `any`, `unknown`\>

#### Inherited from[](#inherited-from-14 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[\_streamIterator](/docs/api/base_language/classes/BaseLangChain#_streamiterator)

#### Defined in[](#defined-in-24 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:86](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L86)

### apply()[](#apply "Direct link to apply()")

Call the chain on all inputs in the list

> **apply**(`inputs`: `RunInput`\[\], `config`?: ([`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`)\[\]): `Promise`<`RunOutput`\[\]\>

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

`inputs`

`RunInput`\[\]

`config?`

([`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`)\[\]

#### Returns[](#returns-11 "Direct link to Returns")

`Promise`<`RunOutput`\[\]\>

#### Defined in[](#defined-in-25 "Direct link to Defined in")

[langchain/src/chains/base.ts:210](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L210)

### batch()[](#batch "Direct link to batch()")

> **batch**(`inputs`: `RunInput`\[\], `options`?: `Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\], `batchOptions`?: `object`): `Promise`<`RunOutput`\[\]\>

#### Parameters[](#parameters-5 "Direct link to Parameters")

Parameter

Type

`inputs`

`RunInput`\[\]

`options?`

`Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\]

`batchOptions?`

`object`

`batchOptions.maxConcurrency?`

`number`

#### Returns[](#returns-12 "Direct link to Returns")

`Promise`<`RunOutput`\[\]\>

#### Inherited from[](#inherited-from-15 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[batch](/docs/api/base_language/classes/BaseLangChain#batch)

#### Defined in[](#defined-in-26 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:63](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L63)

### bind()[](#bind "Direct link to bind()")

> **bind**(`kwargs`: `Partial`<`BaseCallbackConfig`\>): [`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<`RunInput`, `RunOutput`, `BaseCallbackConfig`\>

#### Parameters[](#parameters-6 "Direct link to Parameters")

Parameter

Type

`kwargs`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-13 "Direct link to Returns")

[`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<`RunInput`, `RunOutput`, `BaseCallbackConfig`\>

#### Inherited from[](#inherited-from-16 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[bind](/docs/api/base_language/classes/BaseLangChain#bind)

#### Defined in[](#defined-in-27 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:41](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L41)

### call()[](#call "Direct link to call()")

Run the core logic of this chain and add to output if desired.

Wraps \_call and handles memory.

> **call**(`values`: [`ChainValues`](/docs/api/schema/types/ChainValues) & {`signal`?: `AbortSignal`; `timeout`?: `number`;}, `config`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`, `tags`?: `string`\[\]): `Promise`<`RunOutput`\>

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

`Promise`<`RunOutput`\>

#### Defined in[](#defined-in-28 "Direct link to Defined in")

[langchain/src/chains/base.ts:155](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L155)

### invoke()[](#invoke "Direct link to invoke()")

> **invoke**(`input`: `RunInput`, `config`?: `BaseCallbackConfig`): `Promise`<`RunOutput`\>

#### Parameters[](#parameters-8 "Direct link to Parameters")

Parameter

Type

`input`

`RunInput`

`config?`

`BaseCallbackConfig`

#### Returns[](#returns-15 "Direct link to Returns")

`Promise`<`RunOutput`\>

#### Overrides[](#overrides-3 "Direct link to Overrides")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[invoke](/docs/api/base_language/classes/BaseLangChain#invoke)

#### Defined in[](#defined-in-29 "Direct link to Defined in")

[langchain/src/chains/base.ts:76](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L76)

### pipe()[](#pipe "Direct link to pipe()")

> **pipe**<NewRunOutput\>(`coerceable`: [`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<`RunOutput`, `NewRunOutput`\>): [`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<`RunInput`, `NewRunOutput`\>

#### Type parameters[](#type-parameters-2 "Direct link to Type parameters")

*   `NewRunOutput`

#### Parameters[](#parameters-9 "Direct link to Parameters")

Parameter

Type

`coerceable`

[`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<`RunOutput`, `NewRunOutput`\>

#### Returns[](#returns-16 "Direct link to Returns")

[`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<`RunInput`, `NewRunOutput`\>

#### Inherited from[](#inherited-from-17 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[pipe](/docs/api/base_language/classes/BaseLangChain#pipe)

#### Defined in[](#defined-in-30 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:153](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L153)

### run()[](#run "Direct link to run()")

> **run**(`input`: `any`, `config`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`): `Promise`<`string`\>

#### Parameters[](#parameters-10 "Direct link to Parameters")

Parameter

Type

`input`

`any`

`config?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`

#### Returns[](#returns-17 "Direct link to Returns")

`Promise`<`string`\>

#### Defined in[](#defined-in-31 "Direct link to Defined in")

[langchain/src/chains/base.ts:104](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L104)

### serialize()[](#serialize "Direct link to serialize()")

Return a json-like object representing this chain.

> **serialize**(): [`SerializedBaseChain`](/docs/api/chains/types/SerializedBaseChain)

#### Returns[](#returns-18 "Direct link to Returns")

[`SerializedBaseChain`](/docs/api/chains/types/SerializedBaseChain)

#### Defined in[](#defined-in-32 "Direct link to Defined in")

[langchain/src/chains/base.ts:96](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L96)

### stream()[](#stream "Direct link to stream()")

> **stream**(`input`: `RunInput`, `options`?: `Partial`<`BaseCallbackConfig`\>): `Promise`<`IterableReadableStream`<`RunOutput`\>\>

#### Parameters[](#parameters-11 "Direct link to Parameters")

Parameter

Type

`input`

`RunInput`

`options?`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-19 "Direct link to Returns")

`Promise`<`IterableReadableStream`<`RunOutput`\>\>

#### Inherited from[](#inherited-from-18 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[stream](/docs/api/base_language/classes/BaseLangChain#stream)

#### Defined in[](#defined-in-33 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:93](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L93)

### toJSON()[](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[](#returns-20 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[](#inherited-from-19 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[toJSON](/docs/api/base_language/classes/BaseLangChain#tojson)

#### Defined in[](#defined-in-34 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[](#returns-21 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[](#inherited-from-20 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[toJSONNotImplemented](/docs/api/base_language/classes/BaseLangChain#tojsonnotimplemented)

#### Defined in[](#defined-in-35 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L151)

### deserialize()[](#deserialize "Direct link to deserialize()")

Load a chain from a json-like object describing it.

> `Static` **deserialize**(`data`: [`SerializedBaseChain`](/docs/api/chains/types/SerializedBaseChain), `values`: `LoadValues` = `{}`): `Promise`<[`BaseChain`](/docs/api/chains/classes/BaseChain)<[`ChainValues`](/docs/api/schema/types/ChainValues), [`ChainValues`](/docs/api/schema/types/ChainValues)\>\>

#### Parameters[](#parameters-12 "Direct link to Parameters")

Parameter

Type

`data`

[`SerializedBaseChain`](/docs/api/chains/types/SerializedBaseChain)

`values`

`LoadValues`

#### Returns[](#returns-22 "Direct link to Returns")

`Promise`<[`BaseChain`](/docs/api/chains/classes/BaseChain)<[`ChainValues`](/docs/api/schema/types/ChainValues), [`ChainValues`](/docs/api/schema/types/ChainValues)\>\>

#### Defined in[](#defined-in-36 "Direct link to Defined in")

[langchain/src/chains/base.ts:222](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L222)

### isRunnable()[](#isrunnable "Direct link to isRunnable()")

> `Static` **isRunnable**(`thing`: `any`): thing is Runnable<any, any, BaseCallbackConfig\>

#### Parameters[](#parameters-13 "Direct link to Parameters")

Parameter

Type

`thing`

`any`

#### Returns[](#returns-23 "Direct link to Returns")

thing is Runnable<any, any, BaseCallbackConfig\>

#### Inherited from[](#inherited-from-21 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[isRunnable](/docs/api/base_language/classes/BaseLangChain#isrunnable)

#### Defined in[](#defined-in-37 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:164](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L164)

### \_callWithConfig()[](#_callwithconfig "Direct link to _callwithconfig")

> `Protected` **\_callWithConfig**<T\>(`func`: `Function`, `input`: `T`, `options`?: `BaseCallbackConfig` & {`runType`?: `string`;}): `Promise`<`RunOutput`\>

#### Type parameters[](#type-parameters-3 "Direct link to Type parameters")

*   `T` _extends_ [`ChainValues`](/docs/api/schema/types/ChainValues)

#### Parameters[](#parameters-14 "Direct link to Parameters")

Parameter

Type

`func`

(`input`: `T`) => `Promise`<`RunOutput`\>

`input`

`T`

`options?`

`BaseCallbackConfig` & {`runType`?: `string`;}

#### Returns[](#returns-24 "Direct link to Returns")

`Promise`<`RunOutput`\>

#### Inherited from[](#inherited-from-22 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[\_callWithConfig](/docs/api/base_language/classes/BaseLangChain#_callwithconfig)

#### Defined in[](#defined-in-38 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:117](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L117)

### \_formatValues()[](#_formatvalues "Direct link to _formatvalues")

> `Protected` **\_formatValues**(`values`: [`ChainValues`](/docs/api/schema/types/ChainValues) & {`signal`?: `AbortSignal`; `timeout`?: `number`;}): `Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues) & {`signal`?: `AbortSignal`; `timeout`?: `number`;}\>

#### Parameters[](#parameters-15 "Direct link to Parameters")

Parameter

Type

`values`

[`ChainValues`](/docs/api/schema/types/ChainValues) & {`signal`?: `AbortSignal`;  
`timeout`?: `number`;}

#### Returns[](#returns-25 "Direct link to Returns")

`Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues) & {`signal`?: `AbortSignal`; `timeout`?: `number`;}\>

#### Defined in[](#defined-in-39 "Direct link to Defined in")

[langchain/src/chains/base.ts:131](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/chains/base.ts#L131)

### \_getOptionsList()[](#_getoptionslist "Direct link to _getoptionslist")

> `Protected` **\_getOptionsList**(`options`: `Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\], `length`: `number` = `0`): `Partial`<`BaseCallbackConfig`\>\[\]

#### Parameters[](#parameters-16 "Direct link to Parameters")

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

#### Inherited from[](#inherited-from-23 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[\_getOptionsList](/docs/api/base_language/classes/BaseLangChain#_getoptionslist)

#### Defined in[](#defined-in-40 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L48)

### \_separateRunnableConfigFromCallOptions()[](#_separaterunnableconfigfromcalloptions "Direct link to _separaterunnableconfigfromcalloptions")

> `Protected` **\_separateRunnableConfigFromCallOptions**(`options`: `Partial`<`BaseCallbackConfig`\> = `{}`): \[`BaseCallbackConfig`, `Omit`<`Partial`<`BaseCallbackConfig`\>, _keyof_ `BaseCallbackConfig`\>\]

#### Parameters[](#parameters-17 "Direct link to Parameters")

Parameter

Type

`options`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-27 "Direct link to Returns")

\[`BaseCallbackConfig`, `Omit`<`Partial`<`BaseCallbackConfig`\>, _keyof_ `BaseCallbackConfig`\>\]

#### Inherited from[](#inherited-from-24 "Direct link to Inherited from")

[BaseLangChain](/docs/api/base_language/classes/BaseLangChain).[\_separateRunnableConfigFromCallOptions](/docs/api/base_language/classes/BaseLangChain#_separaterunnableconfigfromcalloptions)

#### Defined in[](#defined-in-41 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:102](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L102)