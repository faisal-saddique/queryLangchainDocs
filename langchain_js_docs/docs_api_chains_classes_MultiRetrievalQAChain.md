MultiRetrievalQAChain
=====================

Base interface that all chains must implement.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`MultiRouteChain`](/docs/api/chains/classes/MultiRouteChain).**MultiRetrievalQAChain**

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new MultiRetrievalQAChain**(`fields`: [`MultiRouteChainInput`](/docs/api/chains/interfaces/MultiRouteChainInput)): [`MultiRetrievalQAChain`](/docs/api/chains/classes/MultiRetrievalQAChain)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields`

[`MultiRouteChainInput`](/docs/api/chains/interfaces/MultiRouteChainInput)

#### Returns[​](#returns "Direct link to Returns")

[`MultiRetrievalQAChain`](/docs/api/chains/classes/MultiRetrievalQAChain)

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[MultiRouteChain](/docs/api/chains/classes/MultiRouteChain).[constructor](/docs/api/chains/classes/MultiRouteChain#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/chains/router/multi\_route.ts:47](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/router/multi_route.ts#L47)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### defaultChain[​](#defaultchain "Direct link to defaultChain")

> **defaultChain**: [`BaseChain`](/docs/api/chains/classes/BaseChain)

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[MultiRouteChain](/docs/api/chains/classes/MultiRouteChain).[defaultChain](/docs/api/chains/classes/MultiRouteChain#defaultchain)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/chains/router/multi\_route.ts:43](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/router/multi_route.ts#L43)

### destinationChains[​](#destinationchains "Direct link to destinationChains")

> **destinationChains**: `object`

#### Index signature[​](#index-signature "Direct link to Index signature")

\[`name`: `string`\]: [`BaseChain`](/docs/api/chains/classes/BaseChain)

#### Type declaration[​](#type-declaration "Direct link to Type declaration")

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[MultiRouteChain](/docs/api/chains/classes/MultiRouteChain).[destinationChains](/docs/api/chains/classes/MultiRouteChain#destinationchains)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/chains/router/multi\_route.ts:41](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/router/multi_route.ts#L41)

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[MultiRouteChain](/docs/api/chains/classes/MultiRouteChain).[lc\_kwargs](/docs/api/chains/classes/MultiRouteChain#lc_kwargs)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[MultiRouteChain](/docs/api/chains/classes/MultiRouteChain).[lc\_serializable](/docs/api/chains/classes/MultiRouteChain#lc_serializable)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L55)

### routerChain[​](#routerchain "Direct link to routerChain")

> **routerChain**: [`RouterChain`](/docs/api/chains/classes/RouterChain)

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[MultiRouteChain](/docs/api/chains/classes/MultiRouteChain).[routerChain](/docs/api/chains/classes/MultiRouteChain#routerchain)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/chains/router/multi\_route.ts:39](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/router/multi_route.ts#L39)

### silentErrors[​](#silenterrors "Direct link to silentErrors")

> **silentErrors**: `boolean` = `false`

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[MultiRouteChain](/docs/api/chains/classes/MultiRouteChain).[silentErrors](/docs/api/chains/classes/MultiRouteChain#silenterrors)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/chains/router/multi\_route.ts:45](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/router/multi_route.ts#L45)

### verbose[​](#verbose "Direct link to verbose")

> **verbose**: `boolean`

Whether to print out response text.

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

[MultiRouteChain](/docs/api/chains/classes/MultiRouteChain).[verbose](/docs/api/chains/classes/MultiRouteChain#verbose)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:38](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L38)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[MultiRouteChain](/docs/api/chains/classes/MultiRouteChain).[callbacks](/docs/api/chains/classes/MultiRouteChain#callbacks)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L40)

### memory?[​](#memory "Direct link to memory?")

> **memory**: [`BaseMemory`](/docs/api/memory/classes/BaseMemory)

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

[MultiRouteChain](/docs/api/chains/classes/MultiRouteChain).[memory](/docs/api/chains/classes/MultiRouteChain#memory)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/chains/base.ts:29](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L29)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

[MultiRouteChain](/docs/api/chains/classes/MultiRouteChain).[metadata](/docs/api/chains/classes/MultiRouteChain#metadata)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:44](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L44)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

[MultiRouteChain](/docs/api/chains/classes/MultiRouteChain).[tags](/docs/api/chains/classes/MultiRouteChain#tags)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L42)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### inputKeys[​](#inputkeys "Direct link to inputKeys")

> **inputKeys**(): `string`\[\]

#### Returns[​](#returns-1 "Direct link to Returns")

`string`\[\]

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

MultiRouteChain.inputKeys

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/chains/router/multi\_route.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/router/multi_route.ts#L55)

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

[MultiRouteChain](/docs/api/chains/classes/MultiRouteChain).[inputKeys](/docs/api/chains/classes/MultiRouteChain#inputkeys)

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/chains/router/multi\_route.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/router/multi_route.ts#L55)

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

MultiRouteChain.lc\_aliases

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-15 "Direct link to Inherited from")

[MultiRouteChain](/docs/api/chains/classes/MultiRouteChain).[lc\_aliases](/docs/api/chains/classes/MultiRouteChain#lc_aliases)

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-16 "Direct link to Inherited from")

MultiRouteChain.lc\_attributes

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

#### Inherited from[​](#inherited-from-17 "Direct link to Inherited from")

[MultiRouteChain](/docs/api/chains/classes/MultiRouteChain).[lc\_attributes](/docs/api/chains/classes/MultiRouteChain#lc_attributes)

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

> **lc\_namespace**(): `string`\[\]

#### Returns[​](#returns-4 "Direct link to Returns")

`string`\[\]

#### Inherited from[​](#inherited-from-18 "Direct link to Inherited from")

MultiRouteChain.lc\_namespace

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/chains/base.ts:31](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L31)

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[​](#inherited-from-19 "Direct link to Inherited from")

[MultiRouteChain](/docs/api/chains/classes/MultiRouteChain).[lc\_namespace](/docs/api/chains/classes/MultiRouteChain#lc_namespace)

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/chains/base.ts:31](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L31)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-5 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-20 "Direct link to Inherited from")

MultiRouteChain.lc\_secrets

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-21 "Direct link to Inherited from")

[MultiRouteChain](/docs/api/chains/classes/MultiRouteChain).[lc\_secrets](/docs/api/chains/classes/MultiRouteChain#lc_secrets)

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

### outputKeys[​](#outputkeys "Direct link to outputKeys")

> **outputKeys**(): `string`\[\]

#### Returns[​](#returns-6 "Direct link to Returns")

`string`\[\]

#### Overrides[​](#overrides "Direct link to Overrides")

MultiRouteChain.outputKeys

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/chains/router/multi\_retrieval\_qa.ts:28](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/router/multi_retrieval_qa.ts#L28)

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[MultiRouteChain](/docs/api/chains/classes/MultiRouteChain).[outputKeys](/docs/api/chains/classes/MultiRouteChain#outputkeys)

#### Defined in[​](#defined-in-23 "Direct link to Defined in")

[langchain/src/chains/router/multi\_retrieval\_qa.ts:28](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/router/multi_retrieval_qa.ts#L28)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### \_call()[​](#_call "Direct link to _call")

Run the core logic of this chain and return the output

> **\_call**(`values`: [`ChainValues`](/docs/api/schema/types/ChainValues), `runManager`?: [`CallbackManagerForChainRun`](/docs/api/callbacks/classes/CallbackManagerForChainRun)): `Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`values`

[`ChainValues`](/docs/api/schema/types/ChainValues)

`runManager?`

[`CallbackManagerForChainRun`](/docs/api/callbacks/classes/CallbackManagerForChainRun)

#### Returns[​](#returns-7 "Direct link to Returns")

`Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\>

#### Inherited from[​](#inherited-from-22 "Direct link to Inherited from")

[MultiRouteChain](/docs/api/chains/classes/MultiRouteChain).[\_call](/docs/api/chains/classes/MultiRouteChain#_call)

#### Defined in[​](#defined-in-24 "Direct link to Defined in")

[langchain/src/chains/router/multi\_route.ts:63](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/router/multi_route.ts#L63)

### \_chainType()[​](#_chaintype "Direct link to _chaintype")

Return the string type key uniquely identifying this class of chain.

> **\_chainType**(): `string`

#### Returns[​](#returns-8 "Direct link to Returns")

`string`

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[MultiRouteChain](/docs/api/chains/classes/MultiRouteChain).[\_chainType](/docs/api/chains/classes/MultiRouteChain#_chaintype)

#### Defined in[​](#defined-in-25 "Direct link to Defined in")

[langchain/src/chains/router/multi\_retrieval\_qa.ts:169](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/router/multi_retrieval_qa.ts#L169)

### apply()[​](#apply "Direct link to apply()")

Call the chain on all inputs in the list

> **apply**(`inputs`: [`ChainValues`](/docs/api/schema/types/ChainValues)\[\], `config`?: ([`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`)\[\]): `Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\[\]\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`inputs`

[`ChainValues`](/docs/api/schema/types/ChainValues)\[\]

`config?`

([`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`)\[\]

#### Returns[​](#returns-9 "Direct link to Returns")

`Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\[\]\>

#### Inherited from[​](#inherited-from-23 "Direct link to Inherited from")

[MultiRouteChain](/docs/api/chains/classes/MultiRouteChain).[apply](/docs/api/chains/classes/MultiRouteChain#apply)

#### Defined in[​](#defined-in-26 "Direct link to Defined in")

[langchain/src/chains/base.ts:192](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L192)

### call()[​](#call "Direct link to call()")

Run the core logic of this chain and add to output if desired.

Wraps \_call and handles memory.

> **call**(`values`: [`ChainValues`](/docs/api/schema/types/ChainValues) & {`signal`?: `AbortSignal`; `timeout`?: `number`;}, `config`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`, `tags`?: `string`\[\]): `Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

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
  

#### Returns[​](#returns-10 "Direct link to Returns")

`Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\>

#### Inherited from[​](#inherited-from-24 "Direct link to Inherited from")

[MultiRouteChain](/docs/api/chains/classes/MultiRouteChain).[call](/docs/api/chains/classes/MultiRouteChain#call)

#### Defined in[​](#defined-in-27 "Direct link to Defined in")

[langchain/src/chains/base.ts:125](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L125)

### run()[​](#run "Direct link to run()")

> **run**(`input`: `any`, `config`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`): `Promise`<`string`\>

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`input`

`any`

`config?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`

#### Returns[​](#returns-11 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[​](#inherited-from-25 "Direct link to Inherited from")

[MultiRouteChain](/docs/api/chains/classes/MultiRouteChain).[run](/docs/api/chains/classes/MultiRouteChain#run)

#### Defined in[​](#defined-in-28 "Direct link to Defined in")

[langchain/src/chains/base.ts:94](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L94)

### serialize()[​](#serialize "Direct link to serialize()")

Return a json-like object representing this chain.

> **serialize**(): [`SerializedBaseChain`](/docs/api/chains/types/SerializedBaseChain)

#### Returns[​](#returns-12 "Direct link to Returns")

[`SerializedBaseChain`](/docs/api/chains/types/SerializedBaseChain)

#### Inherited from[​](#inherited-from-26 "Direct link to Inherited from")

[MultiRouteChain](/docs/api/chains/classes/MultiRouteChain).[serialize](/docs/api/chains/classes/MultiRouteChain#serialize)

#### Defined in[​](#defined-in-29 "Direct link to Defined in")

[langchain/src/chains/base.ts:86](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L86)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-13 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-27 "Direct link to Inherited from")

[MultiRouteChain](/docs/api/chains/classes/MultiRouteChain).[toJSON](/docs/api/chains/classes/MultiRouteChain#tojson)

#### Defined in[​](#defined-in-30 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-14 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-28 "Direct link to Inherited from")

[MultiRouteChain](/docs/api/chains/classes/MultiRouteChain).[toJSONNotImplemented](/docs/api/chains/classes/MultiRouteChain#tojsonnotimplemented)

#### Defined in[​](#defined-in-31 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)

### deserialize()[​](#deserialize "Direct link to deserialize()")

Load a chain from a json-like object describing it.

> `Static` **deserialize**(`data`: [`SerializedBaseChain`](/docs/api/chains/types/SerializedBaseChain), `values`: `LoadValues` = `{}`): `Promise`<[`BaseChain`](/docs/api/chains/classes/BaseChain)\>

#### Parameters[​](#parameters-5 "Direct link to Parameters")

Parameter

Type

`data`

[`SerializedBaseChain`](/docs/api/chains/types/SerializedBaseChain)

`values`

`LoadValues`

#### Returns[​](#returns-15 "Direct link to Returns")

`Promise`<[`BaseChain`](/docs/api/chains/classes/BaseChain)\>

#### Inherited from[​](#inherited-from-29 "Direct link to Inherited from")

[MultiRouteChain](/docs/api/chains/classes/MultiRouteChain).[deserialize](/docs/api/chains/classes/MultiRouteChain#deserialize)

#### Defined in[​](#defined-in-32 "Direct link to Defined in")

[langchain/src/chains/base.ts:204](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L204)

### fromLLMAndRetrievers()[​](#fromllmandretrievers "Direct link to fromLLMAndRetrievers()")

> `Static` **fromLLMAndRetrievers**(`llm`: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel), «destructured»: `object`): [`MultiRetrievalQAChain`](/docs/api/chains/classes/MultiRetrievalQAChain)

#### Parameters[​](#parameters-6 "Direct link to Parameters")

Parameter

Type

`llm`

[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)

`«destructured»`

`object`

› `retrieverDescriptions`

`string`\[\]

› `retrieverNames`

`string`\[\]

› `retrievers`

[`BaseRetriever`](/docs/api/schema_retriever/classes/BaseRetriever)\[\]

› `defaults?`

`MultiRetrievalDefaults`

› `multiRetrievalChainOpts?`

`Omit`<[`MultiRouteChainInput`](/docs/api/chains/interfaces/MultiRouteChainInput), "defaultChain"\>

› `retrievalQAChainOpts?`

`Partial`<`Omit`<[`RetrievalQAChainInput`](/docs/api/chains/interfaces/RetrievalQAChainInput), "retriever" | "combineDocumentsChain"\>\> & {`prompt`?: [`PromptTemplate`](/docs/api/prompts/classes/PromptTemplate);}

› `retrieverPrompts?`

[`PromptTemplate`](/docs/api/prompts/classes/PromptTemplate)\[\]

#### Returns[​](#returns-16 "Direct link to Returns")

[`MultiRetrievalQAChain`](/docs/api/chains/classes/MultiRetrievalQAChain)

#### Defined in[​](#defined-in-33 "Direct link to Defined in")

[langchain/src/chains/router/multi\_retrieval\_qa.ts:54](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/router/multi_retrieval_qa.ts#L54)

### fromRetrievers()[​](#fromretrievers "Direct link to fromRetrievers()")

#### Deprecated[​](#deprecated "Direct link to Deprecated")

Use `fromRetrieversAndPrompts` instead

> `Static` **fromRetrievers**(`llm`: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel), `retrieverNames`: `string`\[\], `retrieverDescriptions`: `string`\[\], `retrievers`: [`BaseRetriever`](/docs/api/schema_retriever/classes/BaseRetriever)\[\], `retrieverPrompts`?: [`PromptTemplate`](/docs/api/prompts/classes/PromptTemplate)\[\], `defaults`?: `MultiRetrievalDefaults`, `options`?: `Omit`<[`MultiRouteChainInput`](/docs/api/chains/interfaces/MultiRouteChainInput), "defaultChain"\>): [`MultiRetrievalQAChain`](/docs/api/chains/classes/MultiRetrievalQAChain)

#### Parameters[​](#parameters-7 "Direct link to Parameters")

Parameter

Type

`llm`

[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)

`retrieverNames`

`string`\[\]

`retrieverDescriptions`

`string`\[\]

`retrievers`

[`BaseRetriever`](/docs/api/schema_retriever/classes/BaseRetriever)\[\]

`retrieverPrompts?`

[`PromptTemplate`](/docs/api/prompts/classes/PromptTemplate)\[\]

`defaults?`

`MultiRetrievalDefaults`

`options?`

`Omit`<[`MultiRouteChainInput`](/docs/api/chains/interfaces/MultiRouteChainInput), "defaultChain"\>

#### Returns[​](#returns-17 "Direct link to Returns")

[`MultiRetrievalQAChain`](/docs/api/chains/classes/MultiRetrievalQAChain)

#### Defined in[​](#defined-in-34 "Direct link to Defined in")

[langchain/src/chains/router/multi\_retrieval\_qa.ts:35](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/router/multi_retrieval_qa.ts#L35)