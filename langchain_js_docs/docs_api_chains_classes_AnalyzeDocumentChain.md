AnalyzeDocumentChain
====================

Chain that combines documents by stuffing into context.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseChain`](/docs/api/chains/classes/BaseChain).**AnalyzeDocumentChain**

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   [`AnalyzeDocumentChainInput`](/docs/api/chains/interfaces/AnalyzeDocumentChainInput)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new AnalyzeDocumentChain**(`fields`: [`AnalyzeDocumentChainInput`](/docs/api/chains/interfaces/AnalyzeDocumentChainInput)): [`AnalyzeDocumentChain`](/docs/api/chains/classes/AnalyzeDocumentChain)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields`

[`AnalyzeDocumentChainInput`](/docs/api/chains/interfaces/AnalyzeDocumentChainInput)

#### Returns[​](#returns "Direct link to Returns")

[`AnalyzeDocumentChain`](/docs/api/chains/classes/AnalyzeDocumentChain)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseChain](/docs/api/chains/classes/BaseChain).[constructor](/docs/api/chains/classes/BaseChain#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/chains/analyze\_documents\_chain.ts:34](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/analyze_documents_chain.ts#L34)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### combineDocumentsChain[​](#combinedocumentschain "Direct link to combineDocumentsChain")

> **combineDocumentsChain**: [`BaseChain`](/docs/api/chains/classes/BaseChain)

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

[AnalyzeDocumentChainInput](/docs/api/chains/interfaces/AnalyzeDocumentChainInput).[combineDocumentsChain](/docs/api/chains/interfaces/AnalyzeDocumentChainInput#combinedocumentschain)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/chains/analyze\_documents\_chain.ts:30](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/analyze_documents_chain.ts#L30)

### inputKey[​](#inputkey "Direct link to inputKey")

> **inputKey**: `string` = `"input_document"`

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

[AnalyzeDocumentChainInput](/docs/api/chains/interfaces/AnalyzeDocumentChainInput).[inputKey](/docs/api/chains/interfaces/AnalyzeDocumentChainInput#inputkey)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/chains/analyze\_documents\_chain.ts:28](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/analyze_documents_chain.ts#L28)

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[lc\_kwargs](/docs/api/chains/classes/BaseChain#lc_kwargs)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[lc\_serializable](/docs/api/chains/classes/BaseChain#lc_serializable)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L55)

### textSplitter[​](#textsplitter "Direct link to textSplitter")

> **textSplitter**: [`TextSplitter`](/docs/api/text_splitter/classes/TextSplitter)

#### Implementation of[​](#implementation-of-2 "Direct link to Implementation of")

[AnalyzeDocumentChainInput](/docs/api/chains/interfaces/AnalyzeDocumentChainInput).[textSplitter](/docs/api/chains/interfaces/AnalyzeDocumentChainInput#textsplitter)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/chains/analyze\_documents\_chain.ts:32](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/analyze_documents_chain.ts#L32)

### verbose[​](#verbose "Direct link to verbose")

> **verbose**: `boolean`

Whether to print out response text.

#### Implementation of[​](#implementation-of-3 "Direct link to Implementation of")

[AnalyzeDocumentChainInput](/docs/api/chains/interfaces/AnalyzeDocumentChainInput).[verbose](/docs/api/chains/interfaces/AnalyzeDocumentChainInput#verbose)

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[verbose](/docs/api/chains/classes/BaseChain#verbose)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:38](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L38)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Implementation of[​](#implementation-of-4 "Direct link to Implementation of")

[AnalyzeDocumentChainInput](/docs/api/chains/interfaces/AnalyzeDocumentChainInput).[callbacks](/docs/api/chains/interfaces/AnalyzeDocumentChainInput#callbacks)

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[callbacks](/docs/api/chains/classes/BaseChain#callbacks)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L40)

### memory?[​](#memory "Direct link to memory?")

> **memory**: [`BaseMemory`](/docs/api/memory/classes/BaseMemory)

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[memory](/docs/api/chains/classes/BaseChain#memory)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/chains/base.ts:29](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L29)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Implementation of[​](#implementation-of-5 "Direct link to Implementation of")

[AnalyzeDocumentChainInput](/docs/api/chains/interfaces/AnalyzeDocumentChainInput).[metadata](/docs/api/chains/interfaces/AnalyzeDocumentChainInput#metadata)

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[metadata](/docs/api/chains/classes/BaseChain#metadata)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:44](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L44)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Implementation of[​](#implementation-of-6 "Direct link to Implementation of")

[AnalyzeDocumentChainInput](/docs/api/chains/interfaces/AnalyzeDocumentChainInput).[tags](/docs/api/chains/interfaces/AnalyzeDocumentChainInput#tags)

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[tags](/docs/api/chains/classes/BaseChain#tags)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L42)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### inputKeys[​](#inputkeys "Direct link to inputKeys")

> **inputKeys**(): `string`\[\]

#### Returns[​](#returns-1 "Direct link to Returns")

`string`\[\]

#### Overrides[​](#overrides-1 "Direct link to Overrides")

BaseChain.inputKeys

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/chains/analyze\_documents\_chain.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/analyze_documents_chain.ts#L42)

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[BaseChain](/docs/api/chains/classes/BaseChain).[inputKeys](/docs/api/chains/classes/BaseChain#inputkeys)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/chains/analyze\_documents\_chain.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/analyze_documents_chain.ts#L42)

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

BaseChain.lc\_aliases

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[lc\_aliases](/docs/api/chains/classes/BaseChain#lc_aliases)

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

BaseChain.lc\_attributes

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[lc\_attributes](/docs/api/chains/classes/BaseChain#lc_attributes)

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

> **lc\_namespace**(): `string`\[\]

#### Returns[​](#returns-4 "Direct link to Returns")

`string`\[\]

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

BaseChain.lc\_namespace

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/chains/base.ts:31](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L31)

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[lc\_namespace](/docs/api/chains/classes/BaseChain#lc_namespace)

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/chains/base.ts:31](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L31)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-5 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

BaseChain.lc\_secrets

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[lc\_secrets](/docs/api/chains/classes/BaseChain#lc_secrets)

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

### outputKeys[​](#outputkeys "Direct link to outputKeys")

> **outputKeys**(): `string`\[\]

#### Returns[​](#returns-6 "Direct link to Returns")

`string`\[\]

#### Overrides[​](#overrides-3 "Direct link to Overrides")

BaseChain.outputKeys

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/chains/analyze\_documents\_chain.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/analyze_documents_chain.ts#L46)

#### Overrides[​](#overrides-4 "Direct link to Overrides")

[BaseChain](/docs/api/chains/classes/BaseChain).[outputKeys](/docs/api/chains/classes/BaseChain#outputkeys)

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/chains/analyze\_documents\_chain.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/analyze_documents_chain.ts#L46)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### \_chainType()[​](#_chaintype "Direct link to _chaintype")

Return the string type key uniquely identifying this class of chain.

> **\_chainType**(): "analyze\_document\_chain"

#### Returns[​](#returns-7 "Direct link to Returns")

"analyze\_document\_chain"

#### Overrides[​](#overrides-5 "Direct link to Overrides")

[BaseChain](/docs/api/chains/classes/BaseChain).[\_chainType](/docs/api/chains/classes/BaseChain#_chaintype)

#### Defined in[​](#defined-in-23 "Direct link to Defined in")

[langchain/src/chains/analyze\_documents\_chain.ts:71](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/analyze_documents_chain.ts#L71)

### apply()[​](#apply "Direct link to apply()")

Call the chain on all inputs in the list

> **apply**(`inputs`: [`ChainValues`](/docs/api/schema/types/ChainValues)\[\], `config`?: ([`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`)\[\]): `Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\[\]\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`inputs`

[`ChainValues`](/docs/api/schema/types/ChainValues)\[\]

`config?`

([`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`)\[\]

#### Returns[​](#returns-8 "Direct link to Returns")

`Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\[\]\>

#### Inherited from[​](#inherited-from-15 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[apply](/docs/api/chains/classes/BaseChain#apply)

#### Defined in[​](#defined-in-24 "Direct link to Defined in")

[langchain/src/chains/base.ts:192](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L192)

### call()[​](#call "Direct link to call()")

Run the core logic of this chain and add to output if desired.

Wraps \_call and handles memory.

> **call**(`values`: [`ChainValues`](/docs/api/schema/types/ChainValues) & {`signal`?: `AbortSignal`; `timeout`?: `number`;}, `config`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`, `tags`?: `string`\[\]): `Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

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
  

#### Returns[​](#returns-9 "Direct link to Returns")

`Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\>

#### Inherited from[​](#inherited-from-16 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[call](/docs/api/chains/classes/BaseChain#call)

#### Defined in[​](#defined-in-25 "Direct link to Defined in")

[langchain/src/chains/base.ts:125](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L125)

### run()[​](#run "Direct link to run()")

> **run**(`input`: `any`, `config`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`): `Promise`<`string`\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`input`

`any`

`config?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`

#### Returns[​](#returns-10 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[​](#inherited-from-17 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[run](/docs/api/chains/classes/BaseChain#run)

#### Defined in[​](#defined-in-26 "Direct link to Defined in")

[langchain/src/chains/base.ts:94](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L94)

### serialize()[​](#serialize "Direct link to serialize()")

Return a json-like object representing this chain.

> **serialize**(): [`SerializedAnalyzeDocumentChain`](/docs/api/chains/types/SerializedAnalyzeDocumentChain)

#### Returns[​](#returns-11 "Direct link to Returns")

[`SerializedAnalyzeDocumentChain`](/docs/api/chains/types/SerializedAnalyzeDocumentChain)

#### Overrides[​](#overrides-6 "Direct link to Overrides")

[BaseChain](/docs/api/chains/classes/BaseChain).[serialize](/docs/api/chains/classes/BaseChain#serialize)

#### Defined in[​](#defined-in-27 "Direct link to Defined in")

[langchain/src/chains/analyze\_documents\_chain.ts:100](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/analyze_documents_chain.ts#L100)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-12 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-18 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[toJSON](/docs/api/chains/classes/BaseChain#tojson)

#### Defined in[​](#defined-in-28 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-13 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-19 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[toJSONNotImplemented](/docs/api/chains/classes/BaseChain#tojsonnotimplemented)

#### Defined in[​](#defined-in-29 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)

### deserialize()[​](#deserialize "Direct link to deserialize()")

Load a chain from a json-like object describing it.

> `Static` **deserialize**(`data`: [`SerializedAnalyzeDocumentChain`](/docs/api/chains/types/SerializedAnalyzeDocumentChain), `values`: `LoadValues`): `Promise`<[`AnalyzeDocumentChain`](/docs/api/chains/classes/AnalyzeDocumentChain)\>

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`data`

[`SerializedAnalyzeDocumentChain`](/docs/api/chains/types/SerializedAnalyzeDocumentChain)

`values`

`LoadValues`

#### Returns[​](#returns-14 "Direct link to Returns")

`Promise`<[`AnalyzeDocumentChain`](/docs/api/chains/classes/AnalyzeDocumentChain)\>

#### Overrides[​](#overrides-7 "Direct link to Overrides")

[BaseChain](/docs/api/chains/classes/BaseChain).[deserialize](/docs/api/chains/classes/BaseChain#deserialize)

#### Defined in[​](#defined-in-30 "Direct link to Defined in")

[langchain/src/chains/analyze\_documents\_chain.ts:75](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/analyze_documents_chain.ts#L75)