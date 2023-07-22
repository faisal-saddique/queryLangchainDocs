SelfQueryRetriever
==================

Base Index class. All indexes should extend this class.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseRetriever`](/docs/api/schema_retriever/classes/BaseRetriever).**SelfQueryRetriever**

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   [`SelfQueryRetrieverArgs`](/docs/api/retrievers_self_query/interfaces/SelfQueryRetrieverArgs)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new SelfQueryRetriever**(`options`: [`SelfQueryRetrieverArgs`](/docs/api/retrievers_self_query/interfaces/SelfQueryRetrieverArgs)): [`SelfQueryRetriever`](/docs/api/retrievers_self_query/classes/SelfQueryRetriever)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`options`

[`SelfQueryRetrieverArgs`](/docs/api/retrievers_self_query/interfaces/SelfQueryRetrieverArgs)

#### Returns[​](#returns "Direct link to Returns")

[`SelfQueryRetriever`](/docs/api/retrievers_self_query/classes/SelfQueryRetriever)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[constructor](/docs/api/schema_retriever/classes/BaseRetriever#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/retrievers/self\_query/index.ts:47](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/self_query/index.ts#L47)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### lc\_kwargs[​](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[lc\_kwargs](/docs/api/schema_retriever/classes/BaseRetriever#lc_kwargs)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L57)

### lc\_serializable[​](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[lc\_serializable](/docs/api/schema_retriever/classes/BaseRetriever#lc_serializable)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L55)

### llmChain[​](#llmchain "Direct link to llmChain")

> **llmChain**: [`LLMChain`](/docs/api/chains/classes/LLMChain)<`string`, [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)\>

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

[SelfQueryRetrieverArgs](/docs/api/retrievers_self_query/interfaces/SelfQueryRetrieverArgs).[llmChain](/docs/api/retrievers_self_query/interfaces/SelfQueryRetrieverArgs#llmchain)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/index.ts:36](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/self_query/index.ts#L36)

### structuredQueryTranslator[​](#structuredquerytranslator "Direct link to structuredQueryTranslator")

> **structuredQueryTranslator**: [`BaseTranslator`](/docs/api/retrievers_self_query/classes/BaseTranslator)

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

[SelfQueryRetrieverArgs](/docs/api/retrievers_self_query/interfaces/SelfQueryRetrieverArgs).[structuredQueryTranslator](/docs/api/retrievers_self_query/interfaces/SelfQueryRetrieverArgs#structuredquerytranslator)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/index.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/self_query/index.ts#L40)

### vectorStore[​](#vectorstore "Direct link to vectorStore")

> **vectorStore**: [`VectorStore`](/docs/api/vectorstores_base/classes/VectorStore)

#### Implementation of[​](#implementation-of-2 "Direct link to Implementation of")

[SelfQueryRetrieverArgs](/docs/api/retrievers_self_query/interfaces/SelfQueryRetrieverArgs).[vectorStore](/docs/api/retrievers_self_query/interfaces/SelfQueryRetrieverArgs#vectorstore)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/index.ts:34](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/self_query/index.ts#L34)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Implementation of[​](#implementation-of-3 "Direct link to Implementation of")

[SelfQueryRetrieverArgs](/docs/api/retrievers_self_query/interfaces/SelfQueryRetrieverArgs).[callbacks](/docs/api/retrievers_self_query/interfaces/SelfQueryRetrieverArgs#callbacks)

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[callbacks](/docs/api/schema_retriever/classes/BaseRetriever#callbacks)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L23)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Implementation of[​](#implementation-of-4 "Direct link to Implementation of")

[SelfQueryRetrieverArgs](/docs/api/retrievers_self_query/interfaces/SelfQueryRetrieverArgs).[metadata](/docs/api/retrievers_self_query/interfaces/SelfQueryRetrieverArgs#metadata)

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[metadata](/docs/api/schema_retriever/classes/BaseRetriever#metadata)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:27](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L27)

### searchParams?[​](#searchparams "Direct link to searchParams?")

> **searchParams**: `object`

#### Type declaration[​](#type-declaration "Direct link to Type declaration")

Member

Type

`filter`?

`object`

`k`?

`number`

#### Implementation of[​](#implementation-of-5 "Direct link to Implementation of")

[SelfQueryRetrieverArgs](/docs/api/retrievers_self_query/interfaces/SelfQueryRetrieverArgs).[searchParams](/docs/api/retrievers_self_query/interfaces/SelfQueryRetrieverArgs#searchparams)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/index.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/self_query/index.ts#L42)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Implementation of[​](#implementation-of-6 "Direct link to Implementation of")

[SelfQueryRetrieverArgs](/docs/api/retrievers_self_query/interfaces/SelfQueryRetrieverArgs).[tags](/docs/api/retrievers_self_query/interfaces/SelfQueryRetrieverArgs#tags)

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[tags](/docs/api/schema_retriever/classes/BaseRetriever#tags)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:25](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L25)

### verbose?[​](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Implementation of[​](#implementation-of-7 "Direct link to Implementation of")

[SelfQueryRetrieverArgs](/docs/api/retrievers_self_query/interfaces/SelfQueryRetrieverArgs).[verbose](/docs/api/retrievers_self_query/interfaces/SelfQueryRetrieverArgs#verbose)

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[verbose](/docs/api/schema_retriever/classes/BaseRetriever#verbose)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/index.ts:38](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/self_query/index.ts#L38)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-1 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

BaseRetriever.lc\_aliases

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[lc\_aliases](/docs/api/schema_retriever/classes/BaseRetriever#lc_aliases)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

BaseRetriever.lc\_attributes

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[lc\_attributes](/docs/api/schema_retriever/classes/BaseRetriever#lc_attributes)

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L80)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

> **lc\_namespace**(): `string`\[\]

#### Returns[​](#returns-3 "Direct link to Returns")

`string`\[\]

#### Overrides[​](#overrides-2 "Direct link to Overrides")

BaseRetriever.lc\_namespace

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/index.ts:30](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/self_query/index.ts#L30)

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Overrides[​](#overrides-3 "Direct link to Overrides")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[lc\_namespace](/docs/api/schema_retriever/classes/BaseRetriever#lc_namespace)

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/index.ts:30](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/self_query/index.ts#L30)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-4 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

BaseRetriever.lc\_secrets

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[lc\_secrets](/docs/api/schema_retriever/classes/BaseRetriever#lc_secrets)

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### \_getRelevantDocuments()[​](#_getrelevantdocuments "Direct link to _getrelevantdocuments")

TODO: This should be an abstract method, but we'd like to avoid breaking changes to people currently using subclassed custom retrievers. Change it on next major release.

> **\_getRelevantDocuments**(`query`: `string`, `runManager`?: `CallbackManagerForRetrieverRun`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `unknown`\>\>\[\]\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`query`

`string`

`runManager?`

`CallbackManagerForRetrieverRun`

#### Returns[​](#returns-5 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `unknown`\>\>\[\]\>

#### Overrides[​](#overrides-4 "Direct link to Overrides")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[\_getRelevantDocuments](/docs/api/schema_retriever/classes/BaseRetriever#_getrelevantdocuments)

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/index.ts:57](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/self_query/index.ts#L57)

### getRelevantDocuments()[​](#getrelevantdocuments "Direct link to getRelevantDocuments()")

> **getRelevantDocuments**(`query`: `string`, `config`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`query`

`string`

`config?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`

#### Returns[​](#returns-6 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[getRelevantDocuments](/docs/api/schema_retriever/classes/BaseRetriever#getrelevantdocuments)

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/schema/retriever.ts:51](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/schema/retriever.ts#L51)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-7 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[toJSON](/docs/api/schema_retriever/classes/BaseRetriever#tojson)

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-8 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

[BaseRetriever](/docs/api/schema_retriever/classes/BaseRetriever).[toJSONNotImplemented](/docs/api/schema_retriever/classes/BaseRetriever#tojsonnotimplemented)

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)

### fromLLM()[​](#fromllm "Direct link to fromLLM()")

> `Static` **fromLLM**(`options`: [`QueryConstructorChainOptions`](/docs/api/chains_query_constructor/types/QueryConstructorChainOptions) & `Omit`<[`SelfQueryRetrieverArgs`](/docs/api/retrievers_self_query/interfaces/SelfQueryRetrieverArgs), "llmChain"\>): [`SelfQueryRetriever`](/docs/api/retrievers_self_query/classes/SelfQueryRetriever)

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`options`

[`QueryConstructorChainOptions`](/docs/api/chains_query_constructor/types/QueryConstructorChainOptions) & `Omit`<[`SelfQueryRetrieverArgs`](/docs/api/retrievers_self_query/interfaces/SelfQueryRetrieverArgs), "llmChain"\>

#### Returns[​](#returns-9 "Direct link to Returns")

[`SelfQueryRetriever`](/docs/api/retrievers_self_query/classes/SelfQueryRetriever)

#### Defined in[​](#defined-in-23 "Direct link to Defined in")

[langchain/src/retrievers/self\_query/index.ts:89](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/retrievers/self_query/index.ts#L89)