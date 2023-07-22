ConstitutionalChain
===================

Base interface that all chains must implement.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseChain`](/docs/api/chains/classes/BaseChain).**ConstitutionalChain**

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   [`ConstitutionalChainInput`](/docs/api/chains/interfaces/ConstitutionalChainInput)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new ConstitutionalChain**(`fields`: [`ConstitutionalChainInput`](/docs/api/chains/interfaces/ConstitutionalChainInput)): [`ConstitutionalChain`](/docs/api/chains/classes/ConstitutionalChain)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields`

[`ConstitutionalChainInput`](/docs/api/chains/interfaces/ConstitutionalChainInput)

#### Returns[​](#returns "Direct link to Returns")

[`ConstitutionalChain`](/docs/api/chains/classes/ConstitutionalChain)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseChain](/docs/api/chains/classes/BaseChain).[constructor](/docs/api/chains/classes/BaseChain#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/chains/constitutional\_ai/constitutional\_chain.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/constitutional_ai/constitutional_chain.ts#L40)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### chain[​](#chain "Direct link to chain")

> **chain**: [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

[ConstitutionalChainInput](/docs/api/chains/interfaces/ConstitutionalChainInput).[chain](/docs/api/chains/interfaces/ConstitutionalChainInput#chain)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/chains/constitutional\_ai/constitutional\_chain.ts:24](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/constitutional_ai/constitutional_chain.ts#L24)

### constitutionalPrinciples[​](#constitutionalprinciples "Direct link to constitutionalPrinciples")

> **constitutionalPrinciples**: [`ConstitutionalPrinciple`](/docs/api/chains/classes/ConstitutionalPrinciple)\[\]

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

[ConstitutionalChainInput](/docs/api/chains/interfaces/ConstitutionalChainInput).[constitutionalPrinciples](/docs/api/chains/interfaces/ConstitutionalChainInput#constitutionalprinciples)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/chains/constitutional\_ai/constitutional\_chain.ts:26](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/constitutional_ai/constitutional_chain.ts#L26)

### critiqueChain[​](#critiquechain "Direct link to critiqueChain")

> **critiqueChain**: [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>

#### Implementation of[​](#implementation-of-2 "Direct link to Implementation of")

[ConstitutionalChainInput](/docs/api/chains/interfaces/ConstitutionalChainInput).[critiqueChain](/docs/api/chains/interfaces/ConstitutionalChainInput#critiquechain)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/chains/constitutional\_ai/constitutional\_chain.ts:28](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/constitutional_ai/constitutional_chain.ts#L28)

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[lc\_kwargs](/docs/api/chains/classes/BaseChain#lc_kwargs)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[lc\_serializable](/docs/api/chains/classes/BaseChain#lc_serializable)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L55)

### revisionChain[​](#revisionchain "Direct link to revisionChain")

> **revisionChain**: [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>

#### Implementation of[​](#implementation-of-3 "Direct link to Implementation of")

[ConstitutionalChainInput](/docs/api/chains/interfaces/ConstitutionalChainInput).[revisionChain](/docs/api/chains/interfaces/ConstitutionalChainInput#revisionchain)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/chains/constitutional\_ai/constitutional\_chain.ts:30](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/constitutional_ai/constitutional_chain.ts#L30)

### verbose[​](#verbose "Direct link to verbose")

> **verbose**: `boolean`

Whether to print out response text.

#### Implementation of[​](#implementation-of-4 "Direct link to Implementation of")

[ConstitutionalChainInput](/docs/api/chains/interfaces/ConstitutionalChainInput).[verbose](/docs/api/chains/interfaces/ConstitutionalChainInput#verbose)

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[verbose](/docs/api/chains/classes/BaseChain#verbose)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:38](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L38)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Implementation of[​](#implementation-of-5 "Direct link to Implementation of")

[ConstitutionalChainInput](/docs/api/chains/interfaces/ConstitutionalChainInput).[callbacks](/docs/api/chains/interfaces/ConstitutionalChainInput#callbacks)

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[callbacks](/docs/api/chains/classes/BaseChain#callbacks)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L40)

### memory?[​](#memory "Direct link to memory?")

> **memory**: [`BaseMemory`](/docs/api/memory/classes/BaseMemory)

#### Implementation of[​](#implementation-of-6 "Direct link to Implementation of")

[ConstitutionalChainInput](/docs/api/chains/interfaces/ConstitutionalChainInput).[memory](/docs/api/chains/interfaces/ConstitutionalChainInput#memory)

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[memory](/docs/api/chains/classes/BaseChain#memory)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/chains/base.ts:29](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L29)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Implementation of[​](#implementation-of-7 "Direct link to Implementation of")

[ConstitutionalChainInput](/docs/api/chains/interfaces/ConstitutionalChainInput).[metadata](/docs/api/chains/interfaces/ConstitutionalChainInput#metadata)

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[metadata](/docs/api/chains/classes/BaseChain#metadata)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:44](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L44)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Implementation of[​](#implementation-of-8 "Direct link to Implementation of")

[ConstitutionalChainInput](/docs/api/chains/interfaces/ConstitutionalChainInput).[tags](/docs/api/chains/interfaces/ConstitutionalChainInput#tags)

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[tags](/docs/api/chains/classes/BaseChain#tags)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L42)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### inputKeys[​](#inputkeys "Direct link to inputKeys")

> **inputKeys**(): `string`\[\]

#### Returns[​](#returns-1 "Direct link to Returns")

`string`\[\]

#### Overrides[​](#overrides-1 "Direct link to Overrides")

BaseChain.inputKeys

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/chains/constitutional\_ai/constitutional\_chain.ts:32](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/constitutional_ai/constitutional_chain.ts#L32)

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[BaseChain](/docs/api/chains/classes/BaseChain).[inputKeys](/docs/api/chains/classes/BaseChain#inputkeys)

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/chains/constitutional\_ai/constitutional\_chain.ts:32](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/constitutional_ai/constitutional_chain.ts#L32)

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

BaseChain.lc\_aliases

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[lc\_aliases](/docs/api/chains/classes/BaseChain#lc_aliases)

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

BaseChain.lc\_attributes

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[lc\_attributes](/docs/api/chains/classes/BaseChain#lc_attributes)

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

> **lc\_namespace**(): `string`\[\]

#### Returns[​](#returns-4 "Direct link to Returns")

`string`\[\]

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

BaseChain.lc\_namespace

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/chains/base.ts:31](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L31)

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[lc\_namespace](/docs/api/chains/classes/BaseChain#lc_namespace)

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/chains/base.ts:31](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L31)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-5 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

BaseChain.lc\_secrets

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[lc\_secrets](/docs/api/chains/classes/BaseChain#lc_secrets)

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

### outputKeys[​](#outputkeys "Direct link to outputKeys")

> **outputKeys**(): `string`\[\]

#### Returns[​](#returns-6 "Direct link to Returns")

`string`\[\]

#### Overrides[​](#overrides-3 "Direct link to Overrides")

BaseChain.outputKeys

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/chains/constitutional\_ai/constitutional\_chain.ts:36](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/constitutional_ai/constitutional_chain.ts#L36)

#### Overrides[​](#overrides-4 "Direct link to Overrides")

[BaseChain](/docs/api/chains/classes/BaseChain).[outputKeys](/docs/api/chains/classes/BaseChain#outputkeys)

#### Defined in[​](#defined-in-23 "Direct link to Defined in")

[langchain/src/chains/constitutional\_ai/constitutional\_chain.ts:36](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/constitutional_ai/constitutional_chain.ts#L36)

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

#### Overrides[​](#overrides-5 "Direct link to Overrides")

[BaseChain](/docs/api/chains/classes/BaseChain).[\_call](/docs/api/chains/classes/BaseChain#_call)

#### Defined in[​](#defined-in-24 "Direct link to Defined in")

[langchain/src/chains/constitutional\_ai/constitutional\_chain.ts:48](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/constitutional_ai/constitutional_chain.ts#L48)

### \_chainType()[​](#_chaintype "Direct link to _chaintype")

Return the string type key uniquely identifying this class of chain.

> **\_chainType**(): "constitutional\_chain"

#### Returns[​](#returns-8 "Direct link to Returns")

"constitutional\_chain"

#### Overrides[​](#overrides-6 "Direct link to Overrides")

[BaseChain](/docs/api/chains/classes/BaseChain).[\_chainType](/docs/api/chains/classes/BaseChain#_chaintype)

#### Defined in[​](#defined-in-25 "Direct link to Defined in")

[langchain/src/chains/constitutional\_ai/constitutional\_chain.ts:143](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/constitutional_ai/constitutional_chain.ts#L143)

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

#### Inherited from[​](#inherited-from-15 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[apply](/docs/api/chains/classes/BaseChain#apply)

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

#### Inherited from[​](#inherited-from-16 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[call](/docs/api/chains/classes/BaseChain#call)

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

#### Inherited from[​](#inherited-from-17 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[run](/docs/api/chains/classes/BaseChain#run)

#### Defined in[​](#defined-in-28 "Direct link to Defined in")

[langchain/src/chains/base.ts:94](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L94)

### serialize()[​](#serialize "Direct link to serialize()")

Return a json-like object representing this chain.

> **serialize**(): [`SerializedBaseChain`](/docs/api/chains/types/SerializedBaseChain)

#### Returns[​](#returns-12 "Direct link to Returns")

[`SerializedBaseChain`](/docs/api/chains/types/SerializedBaseChain)

#### Overrides[​](#overrides-7 "Direct link to Overrides")

[BaseChain](/docs/api/chains/classes/BaseChain).[serialize](/docs/api/chains/classes/BaseChain#serialize)

#### Defined in[​](#defined-in-29 "Direct link to Defined in")

[langchain/src/chains/constitutional\_ai/constitutional\_chain.ts:147](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/constitutional_ai/constitutional_chain.ts#L147)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-13 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-18 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[toJSON](/docs/api/chains/classes/BaseChain#tojson)

#### Defined in[​](#defined-in-30 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-14 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-19 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[toJSONNotImplemented](/docs/api/chains/classes/BaseChain#tojsonnotimplemented)

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

#### Inherited from[​](#inherited-from-20 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[deserialize](/docs/api/chains/classes/BaseChain#deserialize)

#### Defined in[​](#defined-in-32 "Direct link to Defined in")

[langchain/src/chains/base.ts:204](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L204)

### fromLLM()[​](#fromllm "Direct link to fromLLM()")

> `Static` **fromLLM**(`llm`: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel), `options`: `Omit`<[`ConstitutionalChainInput`](/docs/api/chains/interfaces/ConstitutionalChainInput), "critiqueChain" | "revisionChain"\> & {`critiqueChain`?: [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>; `revisionChain`?: [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>;}): [`ConstitutionalChain`](/docs/api/chains/classes/ConstitutionalChain)

#### Parameters[​](#parameters-6 "Direct link to Parameters")

Parameter

Type

`llm`

[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)

`options`

`Omit`<[`ConstitutionalChainInput`](/docs/api/chains/interfaces/ConstitutionalChainInput), "critiqueChain" | "revisionChain"\> & {`critiqueChain`?: [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>;  
`revisionChain`?: [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>;}

#### Returns[​](#returns-16 "Direct link to Returns")

[`ConstitutionalChain`](/docs/api/chains/classes/ConstitutionalChain)

#### Defined in[​](#defined-in-33 "Direct link to Defined in")

[langchain/src/chains/constitutional\_ai/constitutional\_chain.ts:97](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/constitutional_ai/constitutional_chain.ts#L97)

### getPrinciples()[​](#getprinciples "Direct link to getPrinciples()")

> `Static` **getPrinciples**(`names`?: `string`\[\]): [`ConstitutionalPrinciple`](/docs/api/chains/classes/ConstitutionalPrinciple)\[\]

#### Parameters[​](#parameters-7 "Direct link to Parameters")

Parameter

Type

`names?`

`string`\[\]

#### Returns[​](#returns-17 "Direct link to Returns")

[`ConstitutionalPrinciple`](/docs/api/chains/classes/ConstitutionalPrinciple)\[\]

#### Defined in[​](#defined-in-34 "Direct link to Defined in")

[langchain/src/chains/constitutional\_ai/constitutional\_chain.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/constitutional_ai/constitutional_chain.ts#L90)