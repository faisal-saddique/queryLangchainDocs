ChatVectorDBQAChain
===================

Deprecated[​](#deprecated "Direct link to Deprecated")
------------------------------------------------------

use `ConversationalRetrievalQAChain` instead.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseChain`](/docs/api/chains/classes/BaseChain).**ChatVectorDBQAChain**

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   [`ChatVectorDBQAChainInput`](/docs/api/chains/interfaces/ChatVectorDBQAChainInput)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new ChatVectorDBQAChain**(`fields`: [`ChatVectorDBQAChainInput`](/docs/api/chains/interfaces/ChatVectorDBQAChainInput)): [`ChatVectorDBQAChain`](/docs/api/chains/classes/ChatVectorDBQAChain)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`fields`

[`ChatVectorDBQAChainInput`](/docs/api/chains/interfaces/ChatVectorDBQAChainInput)

#### Returns[​](#returns "Direct link to Returns")

[`ChatVectorDBQAChain`](/docs/api/chains/classes/ChatVectorDBQAChain)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseChain](/docs/api/chains/classes/BaseChain).[constructor](/docs/api/chains/classes/BaseChain#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/chains/chat\_vector\_db\_chain.ts:67](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/chat_vector_db_chain.ts#L67)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### chatHistoryKey[​](#chathistorykey "Direct link to chatHistoryKey")

> **chatHistoryKey**: `string` = `"chat_history"`

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/chains/chat\_vector\_db\_chain.ts:47](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/chat_vector_db_chain.ts#L47)

### combineDocumentsChain[​](#combinedocumentschain "Direct link to combineDocumentsChain")

> **combineDocumentsChain**: [`BaseChain`](/docs/api/chains/classes/BaseChain)

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

[ChatVectorDBQAChainInput](/docs/api/chains/interfaces/ChatVectorDBQAChainInput).[combineDocumentsChain](/docs/api/chains/interfaces/ChatVectorDBQAChainInput#combinedocumentschain)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/chains/chat\_vector\_db\_chain.ts:61](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/chat_vector_db_chain.ts#L61)

### inputKey[​](#inputkey "Direct link to inputKey")

> **inputKey**: `string` = `"question"`

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

[ChatVectorDBQAChainInput](/docs/api/chains/interfaces/ChatVectorDBQAChainInput).[inputKey](/docs/api/chains/interfaces/ChatVectorDBQAChainInput#inputkey)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/chains/chat\_vector\_db\_chain.ts:45](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/chat_vector_db_chain.ts#L45)

### k[​](#k "Direct link to k")

> **k**: `number` = `4`

#### Implementation of[​](#implementation-of-2 "Direct link to Implementation of")

[ChatVectorDBQAChainInput](/docs/api/chains/interfaces/ChatVectorDBQAChainInput).[k](/docs/api/chains/interfaces/ChatVectorDBQAChainInput#k)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/chains/chat\_vector\_db\_chain.ts:43](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/chat_vector_db_chain.ts#L43)

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[lc\_kwargs](/docs/api/chains/classes/BaseChain#lc_kwargs)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[lc\_serializable](/docs/api/chains/classes/BaseChain#lc_serializable)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L55)

### outputKey[​](#outputkey "Direct link to outputKey")

> **outputKey**: `string` = `"result"`

#### Implementation of[​](#implementation-of-3 "Direct link to Implementation of")

[ChatVectorDBQAChainInput](/docs/api/chains/interfaces/ChatVectorDBQAChainInput).[outputKey](/docs/api/chains/interfaces/ChatVectorDBQAChainInput#outputkey)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/chains/chat\_vector\_db\_chain.ts:53](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/chat_vector_db_chain.ts#L53)

### questionGeneratorChain[​](#questiongeneratorchain "Direct link to questionGeneratorChain")

> **questionGeneratorChain**: [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>

#### Implementation of[​](#implementation-of-4 "Direct link to Implementation of")

[ChatVectorDBQAChainInput](/docs/api/chains/interfaces/ChatVectorDBQAChainInput).[questionGeneratorChain](/docs/api/chains/interfaces/ChatVectorDBQAChainInput#questiongeneratorchain)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/chains/chat\_vector\_db\_chain.ts:63](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/chat_vector_db_chain.ts#L63)

### returnSourceDocuments[​](#returnsourcedocuments "Direct link to returnSourceDocuments")

> **returnSourceDocuments**: `boolean` = `false`

#### Implementation of[​](#implementation-of-5 "Direct link to Implementation of")

[ChatVectorDBQAChainInput](/docs/api/chains/interfaces/ChatVectorDBQAChainInput).[returnSourceDocuments](/docs/api/chains/interfaces/ChatVectorDBQAChainInput#returnsourcedocuments)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/chains/chat\_vector\_db\_chain.ts:65](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/chat_vector_db_chain.ts#L65)

### vectorstore[​](#vectorstore "Direct link to vectorstore")

> **vectorstore**: [`VectorStore`](/docs/api/vectorstores_base/classes/VectorStore)

#### Implementation of[​](#implementation-of-6 "Direct link to Implementation of")

[ChatVectorDBQAChainInput](/docs/api/chains/interfaces/ChatVectorDBQAChainInput).[vectorstore](/docs/api/chains/interfaces/ChatVectorDBQAChainInput#vectorstore)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/chains/chat\_vector\_db\_chain.ts:59](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/chat_vector_db_chain.ts#L59)

### verbose[​](#verbose "Direct link to verbose")

> **verbose**: `boolean`

Whether to print out response text.

#### Implementation of[​](#implementation-of-7 "Direct link to Implementation of")

[ChatVectorDBQAChainInput](/docs/api/chains/interfaces/ChatVectorDBQAChainInput).[verbose](/docs/api/chains/interfaces/ChatVectorDBQAChainInput#verbose)

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[verbose](/docs/api/chains/classes/BaseChain#verbose)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:38](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L38)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Implementation of[​](#implementation-of-8 "Direct link to Implementation of")

[ChatVectorDBQAChainInput](/docs/api/chains/interfaces/ChatVectorDBQAChainInput).[callbacks](/docs/api/chains/interfaces/ChatVectorDBQAChainInput#callbacks)

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[callbacks](/docs/api/chains/classes/BaseChain#callbacks)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L40)

### memory?[​](#memory "Direct link to memory?")

> **memory**: [`BaseMemory`](/docs/api/memory/classes/BaseMemory)

#### Implementation of[​](#implementation-of-9 "Direct link to Implementation of")

[ChatVectorDBQAChainInput](/docs/api/chains/interfaces/ChatVectorDBQAChainInput).[memory](/docs/api/chains/interfaces/ChatVectorDBQAChainInput#memory)

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[memory](/docs/api/chains/classes/BaseChain#memory)

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/chains/base.ts:29](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L29)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Implementation of[​](#implementation-of-10 "Direct link to Implementation of")

[ChatVectorDBQAChainInput](/docs/api/chains/interfaces/ChatVectorDBQAChainInput).[metadata](/docs/api/chains/interfaces/ChatVectorDBQAChainInput#metadata)

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[metadata](/docs/api/chains/classes/BaseChain#metadata)

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:44](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L44)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Implementation of[​](#implementation-of-11 "Direct link to Implementation of")

[ChatVectorDBQAChainInput](/docs/api/chains/interfaces/ChatVectorDBQAChainInput).[tags](/docs/api/chains/interfaces/ChatVectorDBQAChainInput#tags)

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[tags](/docs/api/chains/classes/BaseChain#tags)

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L42)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### inputKeys[​](#inputkeys "Direct link to inputKeys")

> **inputKeys**(): `string`\[\]

#### Returns[​](#returns-1 "Direct link to Returns")

`string`\[\]

#### Overrides[​](#overrides-1 "Direct link to Overrides")

BaseChain.inputKeys

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/chains/chat\_vector\_db\_chain.ts:49](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/chat_vector_db_chain.ts#L49)

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[BaseChain](/docs/api/chains/classes/BaseChain).[inputKeys](/docs/api/chains/classes/BaseChain#inputkeys)

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/chains/chat\_vector\_db\_chain.ts:49](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/chat_vector_db_chain.ts#L49)

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

BaseChain.lc\_aliases

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[lc\_aliases](/docs/api/chains/classes/BaseChain#lc_aliases)

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

BaseChain.lc\_attributes

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[lc\_attributes](/docs/api/chains/classes/BaseChain#lc_attributes)

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

> **lc\_namespace**(): `string`\[\]

#### Returns[​](#returns-4 "Direct link to Returns")

`string`\[\]

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

BaseChain.lc\_namespace

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/chains/base.ts:31](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L31)

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[lc\_namespace](/docs/api/chains/classes/BaseChain#lc_namespace)

#### Defined in[​](#defined-in-23 "Direct link to Defined in")

[langchain/src/chains/base.ts:31](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L31)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-5 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

BaseChain.lc\_secrets

#### Defined in[​](#defined-in-24 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[lc\_secrets](/docs/api/chains/classes/BaseChain#lc_secrets)

#### Defined in[​](#defined-in-25 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

### outputKeys[​](#outputkeys "Direct link to outputKeys")

> **outputKeys**(): `string`\[\]

#### Returns[​](#returns-6 "Direct link to Returns")

`string`\[\]

#### Overrides[​](#overrides-3 "Direct link to Overrides")

BaseChain.outputKeys

#### Defined in[​](#defined-in-26 "Direct link to Defined in")

[langchain/src/chains/chat\_vector\_db\_chain.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/chat_vector_db_chain.ts#L55)

#### Overrides[​](#overrides-4 "Direct link to Overrides")

[BaseChain](/docs/api/chains/classes/BaseChain).[outputKeys](/docs/api/chains/classes/BaseChain#outputkeys)

#### Defined in[​](#defined-in-27 "Direct link to Defined in")

[langchain/src/chains/chat\_vector\_db\_chain.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/chat_vector_db_chain.ts#L55)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### \_chainType()[​](#_chaintype "Direct link to _chaintype")

Return the string type key uniquely identifying this class of chain.

> **\_chainType**(): "chat-vector-db"

#### Returns[​](#returns-7 "Direct link to Returns")

"chat-vector-db"

#### Overrides[​](#overrides-5 "Direct link to Overrides")

[BaseChain](/docs/api/chains/classes/BaseChain).[\_chainType](/docs/api/chains/classes/BaseChain#_chaintype)

#### Defined in[​](#defined-in-28 "Direct link to Defined in")

[langchain/src/chains/chat\_vector\_db\_chain.ts:135](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/chat_vector_db_chain.ts#L135)

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

#### Defined in[​](#defined-in-29 "Direct link to Defined in")

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

#### Defined in[​](#defined-in-30 "Direct link to Defined in")

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

#### Defined in[​](#defined-in-31 "Direct link to Defined in")

[langchain/src/chains/base.ts:94](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L94)

### serialize()[​](#serialize "Direct link to serialize()")

Return a json-like object representing this chain.

> **serialize**(): [`SerializedChatVectorDBQAChain`](/docs/api/chains/types/SerializedChatVectorDBQAChain)

#### Returns[​](#returns-11 "Direct link to Returns")

[`SerializedChatVectorDBQAChain`](/docs/api/chains/types/SerializedChatVectorDBQAChain)

#### Overrides[​](#overrides-6 "Direct link to Overrides")

[BaseChain](/docs/api/chains/classes/BaseChain).[serialize](/docs/api/chains/classes/BaseChain#serialize)

#### Defined in[​](#defined-in-32 "Direct link to Defined in")

[langchain/src/chains/chat\_vector\_db\_chain.ts:162](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/chat_vector_db_chain.ts#L162)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-12 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-18 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[toJSON](/docs/api/chains/classes/BaseChain#tojson)

#### Defined in[​](#defined-in-33 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-13 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-19 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[toJSONNotImplemented](/docs/api/chains/classes/BaseChain#tojsonnotimplemented)

#### Defined in[​](#defined-in-34 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)

### deserialize()[​](#deserialize "Direct link to deserialize()")

Load a chain from a json-like object describing it.

> `Static` **deserialize**(`data`: [`SerializedChatVectorDBQAChain`](/docs/api/chains/types/SerializedChatVectorDBQAChain), `values`: `LoadValues`): `Promise`<[`ChatVectorDBQAChain`](/docs/api/chains/classes/ChatVectorDBQAChain)\>

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

`data`

[`SerializedChatVectorDBQAChain`](/docs/api/chains/types/SerializedChatVectorDBQAChain)

`values`

`LoadValues`

#### Returns[​](#returns-14 "Direct link to Returns")

`Promise`<[`ChatVectorDBQAChain`](/docs/api/chains/classes/ChatVectorDBQAChain)\>

#### Overrides[​](#overrides-7 "Direct link to Overrides")

[BaseChain](/docs/api/chains/classes/BaseChain).[deserialize](/docs/api/chains/classes/BaseChain#deserialize)

#### Defined in[​](#defined-in-35 "Direct link to Defined in")

[langchain/src/chains/chat\_vector\_db\_chain.ts:139](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/chat_vector_db_chain.ts#L139)

### fromLLM()[​](#fromllm "Direct link to fromLLM()")

> `Static` **fromLLM**(`llm`: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel), `vectorstore`: [`VectorStore`](/docs/api/vectorstores_base/classes/VectorStore), `options`: `object` = `{}`): [`ChatVectorDBQAChain`](/docs/api/chains/classes/ChatVectorDBQAChain)

#### Parameters[​](#parameters-5 "Direct link to Parameters")

Parameter

Type

`llm`

[`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)

`vectorstore`

[`VectorStore`](/docs/api/vectorstores_base/classes/VectorStore)

`options`

`object`

`options.inputKey?`

`string`

`options.k?`

`number`

`options.outputKey?`

`string`

`options.qaTemplate?`

`string`

`options.questionGeneratorTemplate?`

`string`

`options.returnSourceDocuments?`

`boolean`

`options.verbose?`

`boolean`

#### Returns[​](#returns-15 "Direct link to Returns")

[`ChatVectorDBQAChain`](/docs/api/chains/classes/ChatVectorDBQAChain)

#### Defined in[​](#defined-in-36 "Direct link to Defined in")

[langchain/src/chains/chat\_vector\_db\_chain.ts:171](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/chat_vector_db_chain.ts#L171)