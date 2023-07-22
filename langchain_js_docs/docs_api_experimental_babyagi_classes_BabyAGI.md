BabyAGI
=======

Base interface that all chains must implement.

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseChain`](/docs/api/chains/classes/BaseChain).**BabyAGI**

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   [`BabyAGIInputs`](/docs/api/experimental_babyagi/interfaces/BabyAGIInputs)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new BabyAGI**(«destructured»: [`BabyAGIInputs`](/docs/api/experimental_babyagi/interfaces/BabyAGIInputs)): [`BabyAGI`](/docs/api/experimental_babyagi/classes/BabyAGI)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`«destructured»`

[`BabyAGIInputs`](/docs/api/experimental_babyagi/interfaces/BabyAGIInputs)

#### Returns[​](#returns "Direct link to Returns")

[`BabyAGI`](/docs/api/experimental_babyagi/classes/BabyAGI)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseChain](/docs/api/chains/classes/BaseChain).[constructor](/docs/api/chains/classes/BaseChain#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/experimental/babyagi/agent.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/babyagi/agent.ts#L42)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### creationChain[​](#creationchain "Direct link to creationChain")

> **creationChain**: [`BaseChain`](/docs/api/chains/classes/BaseChain)

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

[BabyAGIInputs](/docs/api/experimental_babyagi/interfaces/BabyAGIInputs).[creationChain](/docs/api/experimental_babyagi/interfaces/BabyAGIInputs#creationchain)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/experimental/babyagi/agent.ts:30](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/babyagi/agent.ts#L30)

### executionChain[​](#executionchain "Direct link to executionChain")

> **executionChain**: [`BaseChain`](/docs/api/chains/classes/BaseChain)

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

[BabyAGIInputs](/docs/api/experimental_babyagi/interfaces/BabyAGIInputs).[executionChain](/docs/api/experimental_babyagi/interfaces/BabyAGIInputs#executionchain)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/experimental/babyagi/agent.ts:34](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/babyagi/agent.ts#L34)

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

### maxIterations[​](#maxiterations "Direct link to maxIterations")

> **maxIterations**: `number`

#### Implementation of[​](#implementation-of-2 "Direct link to Implementation of")

[BabyAGIInputs](/docs/api/experimental_babyagi/interfaces/BabyAGIInputs).[maxIterations](/docs/api/experimental_babyagi/interfaces/BabyAGIInputs#maxiterations)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/experimental/babyagi/agent.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/babyagi/agent.ts#L40)

### prioritizationChain[​](#prioritizationchain "Direct link to prioritizationChain")

> **prioritizationChain**: [`BaseChain`](/docs/api/chains/classes/BaseChain)

#### Implementation of[​](#implementation-of-3 "Direct link to Implementation of")

[BabyAGIInputs](/docs/api/experimental_babyagi/interfaces/BabyAGIInputs).[prioritizationChain](/docs/api/experimental_babyagi/interfaces/BabyAGIInputs#prioritizationchain)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/experimental/babyagi/agent.ts:32](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/babyagi/agent.ts#L32)

### taskIDCounter[​](#taskidcounter "Direct link to taskIDCounter")

> **taskIDCounter**: `number`

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/experimental/babyagi/agent.ts:36](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/babyagi/agent.ts#L36)

### taskList[​](#tasklist "Direct link to taskList")

> **taskList**: [`Task`](/docs/api/experimental_babyagi/interfaces/Task)\[\]

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/experimental/babyagi/agent.ts:28](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/babyagi/agent.ts#L28)

### vectorstore[​](#vectorstore "Direct link to vectorstore")

> **vectorstore**: [`VectorStore`](/docs/api/vectorstores_base/classes/VectorStore)

#### Implementation of[​](#implementation-of-4 "Direct link to Implementation of")

[BabyAGIInputs](/docs/api/experimental_babyagi/interfaces/BabyAGIInputs).[vectorstore](/docs/api/experimental_babyagi/interfaces/BabyAGIInputs#vectorstore)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/experimental/babyagi/agent.ts:38](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/babyagi/agent.ts#L38)

### verbose[​](#verbose "Direct link to verbose")

> **verbose**: `boolean`

Whether to print out response text.

#### Implementation of[​](#implementation-of-5 "Direct link to Implementation of")

[BabyAGIInputs](/docs/api/experimental_babyagi/interfaces/BabyAGIInputs).[verbose](/docs/api/experimental_babyagi/interfaces/BabyAGIInputs#verbose)

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[verbose](/docs/api/chains/classes/BaseChain#verbose)

#### Defined in[​](#defined-in-10 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:38](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L38)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Implementation of[​](#implementation-of-6 "Direct link to Implementation of")

[BabyAGIInputs](/docs/api/experimental_babyagi/interfaces/BabyAGIInputs).[callbacks](/docs/api/experimental_babyagi/interfaces/BabyAGIInputs#callbacks)

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[callbacks](/docs/api/chains/classes/BaseChain#callbacks)

#### Defined in[​](#defined-in-11 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L40)

### memory?[​](#memory "Direct link to memory?")

> **memory**: [`BaseMemory`](/docs/api/memory/classes/BaseMemory)

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[memory](/docs/api/chains/classes/BaseChain#memory)

#### Defined in[​](#defined-in-12 "Direct link to Defined in")

[langchain/src/chains/base.ts:29](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L29)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Implementation of[​](#implementation-of-7 "Direct link to Implementation of")

[BabyAGIInputs](/docs/api/experimental_babyagi/interfaces/BabyAGIInputs).[metadata](/docs/api/experimental_babyagi/interfaces/BabyAGIInputs#metadata)

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[metadata](/docs/api/chains/classes/BaseChain#metadata)

#### Defined in[​](#defined-in-13 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:44](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L44)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Implementation of[​](#implementation-of-8 "Direct link to Implementation of")

[BabyAGIInputs](/docs/api/experimental_babyagi/interfaces/BabyAGIInputs).[tags](/docs/api/experimental_babyagi/interfaces/BabyAGIInputs#tags)

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[tags](/docs/api/chains/classes/BaseChain#tags)

#### Defined in[​](#defined-in-14 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L42)

Accessors[​](#accessors "Direct link to Accessors")
---------------------------------------------------

### inputKeys[​](#inputkeys "Direct link to inputKeys")

> **inputKeys**(): `string`\[\]

#### Returns[​](#returns-1 "Direct link to Returns")

`string`\[\]

#### Overrides[​](#overrides-1 "Direct link to Overrides")

BaseChain.inputKeys

#### Defined in[​](#defined-in-15 "Direct link to Defined in")

[langchain/src/experimental/babyagi/agent.ts:65](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/babyagi/agent.ts#L65)

#### Overrides[​](#overrides-2 "Direct link to Overrides")

[BaseChain](/docs/api/chains/classes/BaseChain).[inputKeys](/docs/api/chains/classes/BaseChain#inputkeys)

#### Defined in[​](#defined-in-16 "Direct link to Defined in")

[langchain/src/experimental/babyagi/agent.ts:65](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/babyagi/agent.ts#L65)

### lc\_aliases[​](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[​](#returns-2 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-7 "Direct link to Inherited from")

BaseChain.lc\_aliases

#### Defined in[​](#defined-in-17 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

#### Inherited from[​](#inherited-from-8 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[lc\_aliases](/docs/api/chains/classes/BaseChain#lc_aliases)

#### Defined in[​](#defined-in-18 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L90)

### lc\_attributes[​](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | {}

#### Returns[​](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-9 "Direct link to Inherited from")

BaseChain.lc\_attributes

#### Defined in[​](#defined-in-19 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

#### Inherited from[​](#inherited-from-10 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[lc\_attributes](/docs/api/chains/classes/BaseChain#lc_attributes)

#### Defined in[​](#defined-in-20 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:46](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L46)

### lc\_namespace[​](#lc_namespace "Direct link to lc_namespace")

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

> **lc\_namespace**(): `string`\[\]

#### Returns[​](#returns-4 "Direct link to Returns")

`string`\[\]

#### Inherited from[​](#inherited-from-11 "Direct link to Inherited from")

BaseChain.lc\_namespace

#### Defined in[​](#defined-in-21 "Direct link to Defined in")

[langchain/src/chains/base.ts:31](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L31)

A path to the module that contains the class, eg. \["langchain", "llms"\] Usually should be the same as the entrypoint the class is exported from.

#### Inherited from[​](#inherited-from-12 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[lc\_namespace](/docs/api/chains/classes/BaseChain#lc_namespace)

#### Defined in[​](#defined-in-22 "Direct link to Defined in")

[langchain/src/chains/base.ts:31](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L31)

### lc\_secrets[​](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[​](#returns-5 "Direct link to Returns")

`undefined` | {}

#### Inherited from[​](#inherited-from-13 "Direct link to Inherited from")

BaseChain.lc\_secrets

#### Defined in[​](#defined-in-23 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

#### Inherited from[​](#inherited-from-14 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[lc\_secrets](/docs/api/chains/classes/BaseChain#lc_secrets)

#### Defined in[​](#defined-in-24 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L70)

### outputKeys[​](#outputkeys "Direct link to outputKeys")

> **outputKeys**(): `never`\[\]

#### Returns[​](#returns-6 "Direct link to Returns")

`never`\[\]

#### Overrides[​](#overrides-3 "Direct link to Overrides")

BaseChain.outputKeys

#### Defined in[​](#defined-in-25 "Direct link to Defined in")

[langchain/src/experimental/babyagi/agent.ts:69](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/babyagi/agent.ts#L69)

#### Overrides[​](#overrides-4 "Direct link to Overrides")

[BaseChain](/docs/api/chains/classes/BaseChain).[outputKeys](/docs/api/chains/classes/BaseChain#outputkeys)

#### Defined in[​](#defined-in-26 "Direct link to Defined in")

[langchain/src/experimental/babyagi/agent.ts:69](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/babyagi/agent.ts#L69)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### \_call()[​](#_call "Direct link to _call")

Run the core logic of this chain and return the output

> **\_call**(«destructured»: [`ChainValues`](/docs/api/schema/types/ChainValues), `runManager`?: [`CallbackManagerForChainRun`](/docs/api/callbacks/classes/CallbackManagerForChainRun)): `Promise`<{}\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`«destructured»`

[`ChainValues`](/docs/api/schema/types/ChainValues)

`runManager?`

[`CallbackManagerForChainRun`](/docs/api/callbacks/classes/CallbackManagerForChainRun)

#### Returns[​](#returns-7 "Direct link to Returns")

`Promise`<{}\>

#### Overrides[​](#overrides-5 "Direct link to Overrides")

[BaseChain](/docs/api/chains/classes/BaseChain).[\_call](/docs/api/chains/classes/BaseChain#_call)

#### Defined in[​](#defined-in-27 "Direct link to Defined in")

[langchain/src/experimental/babyagi/agent.ts:173](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/babyagi/agent.ts#L173)

### \_chainType()[​](#_chaintype "Direct link to _chaintype")

Return the string type key uniquely identifying this class of chain.

> **\_chainType**(): "BabyAGI"

#### Returns[​](#returns-8 "Direct link to Returns")

"BabyAGI"

#### Overrides[​](#overrides-6 "Direct link to Overrides")

[BaseChain](/docs/api/chains/classes/BaseChain).[\_chainType](/docs/api/chains/classes/BaseChain#_chaintype)

#### Defined in[​](#defined-in-28 "Direct link to Defined in")

[langchain/src/experimental/babyagi/agent.ts:61](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/babyagi/agent.ts#L61)

### addTask()[​](#addtask "Direct link to addTask()")

> **addTask**(`task`: [`Task`](/docs/api/experimental_babyagi/interfaces/Task)): `Promise`<`void`\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`task`

[`Task`](/docs/api/experimental_babyagi/interfaces/Task)

#### Returns[​](#returns-9 "Direct link to Returns")

`Promise`<`void`\>

#### Defined in[​](#defined-in-29 "Direct link to Defined in")

[langchain/src/experimental/babyagi/agent.ts:73](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/babyagi/agent.ts#L73)

### apply()[​](#apply "Direct link to apply()")

Call the chain on all inputs in the list

> **apply**(`inputs`: [`ChainValues`](/docs/api/schema/types/ChainValues)\[\], `config`?: ([`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`)\[\]): `Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\[\]\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

`inputs`

[`ChainValues`](/docs/api/schema/types/ChainValues)\[\]

`config?`

([`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`)\[\]

#### Returns[​](#returns-10 "Direct link to Returns")

`Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\[\]\>

#### Inherited from[​](#inherited-from-15 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[apply](/docs/api/chains/classes/BaseChain#apply)

#### Defined in[​](#defined-in-30 "Direct link to Defined in")

[langchain/src/chains/base.ts:192](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L192)

### call()[​](#call "Direct link to call()")

Run the core logic of this chain and add to output if desired.

Wraps \_call and handles memory.

> **call**(`values`: [`ChainValues`](/docs/api/schema/types/ChainValues) & {`signal`?: `AbortSignal`; `timeout`?: `number`;}, `config`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`, `tags`?: `string`\[\]): `Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\>

#### Parameters[​](#parameters-4 "Direct link to Parameters")

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
  

#### Returns[​](#returns-11 "Direct link to Returns")

`Promise`<[`ChainValues`](/docs/api/schema/types/ChainValues)\>

#### Inherited from[​](#inherited-from-16 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[call](/docs/api/chains/classes/BaseChain#call)

#### Defined in[​](#defined-in-31 "Direct link to Defined in")

[langchain/src/chains/base.ts:125](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L125)

### executeTask()[​](#executetask "Direct link to executeTask()")

> **executeTask**(`objective`: `string`, `task`: `string`, `runManager`?: [`CallbackManagerForChainRun`](/docs/api/callbacks/classes/CallbackManagerForChainRun)): `Promise`<`string`\>

#### Parameters[​](#parameters-5 "Direct link to Parameters")

Parameter

Type

`objective`

`string`

`task`

`string`

`runManager?`

[`CallbackManagerForChainRun`](/docs/api/callbacks/classes/CallbackManagerForChainRun)

#### Returns[​](#returns-12 "Direct link to Returns")

`Promise`<`string`\>

#### Defined in[​](#defined-in-32 "Direct link to Defined in")

[langchain/src/experimental/babyagi/agent.ts:155](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/babyagi/agent.ts#L155)

### getNextTasks()[​](#getnexttasks "Direct link to getNextTasks()")

> **getNextTasks**(`result`: `string`, `task_description`: `string`, `objective`: `string`, `runManager`?: [`CallbackManagerForChainRun`](/docs/api/callbacks/classes/CallbackManagerForChainRun)): `Promise`<`Optional`<[`Task`](/docs/api/experimental_babyagi/interfaces/Task), "taskID"\>\[\]\>

#### Parameters[​](#parameters-6 "Direct link to Parameters")

Parameter

Type

`result`

`string`

`task_description`

`string`

`objective`

`string`

`runManager?`

[`CallbackManagerForChainRun`](/docs/api/callbacks/classes/CallbackManagerForChainRun)

#### Returns[​](#returns-13 "Direct link to Returns")

`Promise`<`Optional`<[`Task`](/docs/api/experimental_babyagi/interfaces/Task), "taskID"\>\[\]\>

#### Defined in[​](#defined-in-33 "Direct link to Defined in")

[langchain/src/experimental/babyagi/agent.ts:94](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/babyagi/agent.ts#L94)

### getTopTasks()[​](#gettoptasks "Direct link to getTopTasks()")

> **getTopTasks**(`query`: `string`, `k`: `number` = `5`): `Promise`<`string`\[\]\>

#### Parameters[​](#parameters-7 "Direct link to Parameters")

Parameter

Type

Default value

`query`

`string`

`undefined`

`k`

`number`

`5`

#### Returns[​](#returns-14 "Direct link to Returns")

`Promise`<`string`\[\]\>

#### Defined in[​](#defined-in-34 "Direct link to Defined in")

[langchain/src/experimental/babyagi/agent.ts:147](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/babyagi/agent.ts#L147)

### printNextTask()[​](#printnexttask "Direct link to printNextTask()")

> **printNextTask**(`task`: [`Task`](/docs/api/experimental_babyagi/interfaces/Task)): `void`

#### Parameters[​](#parameters-8 "Direct link to Parameters")

Parameter

Type

`task`

[`Task`](/docs/api/experimental_babyagi/interfaces/Task)

#### Returns[​](#returns-15 "Direct link to Returns")

`void`

#### Defined in[​](#defined-in-35 "Direct link to Defined in")

[langchain/src/experimental/babyagi/agent.ts:84](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/babyagi/agent.ts#L84)

### printTaskList()[​](#printtasklist "Direct link to printTaskList()")

> **printTaskList**(): `void`

#### Returns[​](#returns-16 "Direct link to Returns")

`void`

#### Defined in[​](#defined-in-36 "Direct link to Defined in")

[langchain/src/experimental/babyagi/agent.ts:77](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/babyagi/agent.ts#L77)

### printTaskResult()[​](#printtaskresult "Direct link to printTaskResult()")

> **printTaskResult**(`result`: `string`): `void`

#### Parameters[​](#parameters-9 "Direct link to Parameters")

Parameter

Type

`result`

`string`

#### Returns[​](#returns-17 "Direct link to Returns")

`void`

#### Defined in[​](#defined-in-37 "Direct link to Defined in")

[langchain/src/experimental/babyagi/agent.ts:89](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/babyagi/agent.ts#L89)

### prioritizeTasks()[​](#prioritizetasks "Direct link to prioritizeTasks()")

> **prioritizeTasks**(`thisTaskID`: `number`, `objective`: `string`, `runManager`?: [`CallbackManagerForChainRun`](/docs/api/callbacks/classes/CallbackManagerForChainRun)): `Promise`<{`taskID`: `string`; `taskName`: `string`;}\[\]\>

#### Parameters[​](#parameters-10 "Direct link to Parameters")

Parameter

Type

`thisTaskID`

`number`

`objective`

`string`

`runManager?`

[`CallbackManagerForChainRun`](/docs/api/callbacks/classes/CallbackManagerForChainRun)

#### Returns[​](#returns-18 "Direct link to Returns")

`Promise`<{`taskID`: `string`; `taskName`: `string`;}\[\]\>

#### Defined in[​](#defined-in-38 "Direct link to Defined in")

[langchain/src/experimental/babyagi/agent.ts:118](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/babyagi/agent.ts#L118)

### run()[​](#run "Direct link to run()")

> **run**(`input`: `any`, `config`?: [`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`): `Promise`<`string`\>

#### Parameters[​](#parameters-11 "Direct link to Parameters")

Parameter

Type

`input`

`any`

`config?`

[`Callbacks`](/docs/api/callbacks/types/Callbacks) | `BaseCallbackConfig`

#### Returns[​](#returns-19 "Direct link to Returns")

`Promise`<`string`\>

#### Inherited from[​](#inherited-from-17 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[run](/docs/api/chains/classes/BaseChain#run)

#### Defined in[​](#defined-in-39 "Direct link to Defined in")

[langchain/src/chains/base.ts:94](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L94)

### serialize()[​](#serialize "Direct link to serialize()")

Return a json-like object representing this chain.

> **serialize**(): [`SerializedBaseChain`](/docs/api/chains/types/SerializedBaseChain)

#### Returns[​](#returns-20 "Direct link to Returns")

[`SerializedBaseChain`](/docs/api/chains/types/SerializedBaseChain)

#### Overrides[​](#overrides-7 "Direct link to Overrides")

[BaseChain](/docs/api/chains/classes/BaseChain).[serialize](/docs/api/chains/classes/BaseChain#serialize)

#### Defined in[​](#defined-in-40 "Direct link to Defined in")

[langchain/src/experimental/babyagi/agent.ts:226](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/babyagi/agent.ts#L226)

### toJSON()[​](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[​](#returns-21 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[​](#inherited-from-18 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[toJSON](/docs/api/chains/classes/BaseChain#tojson)

#### Defined in[​](#defined-in-41 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[​](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[​](#returns-22 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[​](#inherited-from-19 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[toJSONNotImplemented](/docs/api/chains/classes/BaseChain#tojsonnotimplemented)

#### Defined in[​](#defined-in-42 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/load/serializable.ts#L151)

### deserialize()[​](#deserialize "Direct link to deserialize()")

Load a chain from a json-like object describing it.

> `Static` **deserialize**(`data`: [`SerializedBaseChain`](/docs/api/chains/types/SerializedBaseChain), `values`: `LoadValues` = `{}`): `Promise`<[`BaseChain`](/docs/api/chains/classes/BaseChain)\>

#### Parameters[​](#parameters-12 "Direct link to Parameters")

Parameter

Type

`data`

[`SerializedBaseChain`](/docs/api/chains/types/SerializedBaseChain)

`values`

`LoadValues`

#### Returns[​](#returns-23 "Direct link to Returns")

`Promise`<[`BaseChain`](/docs/api/chains/classes/BaseChain)\>

#### Inherited from[​](#inherited-from-20 "Direct link to Inherited from")

[BaseChain](/docs/api/chains/classes/BaseChain).[deserialize](/docs/api/chains/classes/BaseChain#deserialize)

#### Defined in[​](#defined-in-43 "Direct link to Defined in")

[langchain/src/chains/base.ts:204](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/chains/base.ts#L204)

### fromLLM()[​](#fromllm "Direct link to fromLLM()")

> `Static` **fromLLM**(«destructured»: `Omit`<[`BabyAGIInputs`](/docs/api/experimental_babyagi/interfaces/BabyAGIInputs), "creationChain" | "prioritizationChain" | "executionChain"\> & `Partial`<`Pick`<[`BabyAGIInputs`](/docs/api/experimental_babyagi/interfaces/BabyAGIInputs), "creationChain" | "prioritizationChain" | "executionChain"\>\> & {`llm`: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel);}): [`BabyAGI`](/docs/api/experimental_babyagi/classes/BabyAGI)

#### Parameters[​](#parameters-13 "Direct link to Parameters")

Parameter

Type

`«destructured»`

`Omit`<[`BabyAGIInputs`](/docs/api/experimental_babyagi/interfaces/BabyAGIInputs), "creationChain" | "prioritizationChain" | "executionChain"\> & `Partial`<`Pick`<[`BabyAGIInputs`](/docs/api/experimental_babyagi/interfaces/BabyAGIInputs), "creationChain" | "prioritizationChain" | "executionChain"\>\> & {`llm`: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel);}

#### Returns[​](#returns-24 "Direct link to Returns")

[`BabyAGI`](/docs/api/experimental_babyagi/classes/BabyAGI)

#### Defined in[​](#defined-in-44 "Direct link to Defined in")

[langchain/src/experimental/babyagi/agent.ts:230](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/experimental/babyagi/agent.ts#L230)