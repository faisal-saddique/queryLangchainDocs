MarkdownTextSplitter
====================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`RecursiveCharacterTextSplitter`](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).**MarkdownTextSplitter**

Implements[](#implements "Direct link to Implements")
------------------------------------------------------

*   [`MarkdownTextSplitterParams`](/docs/api/text_splitter/types/MarkdownTextSplitterParams)

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new MarkdownTextSplitter**(`fields`?: `Partial`<[`TextSplitterParams`](/docs/api/text_splitter/interfaces/TextSplitterParams)\>): [`MarkdownTextSplitter`](/docs/api/text_splitter/classes/MarkdownTextSplitter)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`fields?`

`Partial`<[`TextSplitterParams`](/docs/api/text_splitter/interfaces/TextSplitterParams)\>

#### Returns[](#returns "Direct link to Returns")

[`MarkdownTextSplitter`](/docs/api/text_splitter/classes/MarkdownTextSplitter)

#### Overrides[](#overrides "Direct link to Overrides")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[constructor](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/text\_splitter.ts:745](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L745)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### chunkOverlap[](#chunkoverlap "Direct link to chunkOverlap")

> **chunkOverlap**: `number` = `200`

#### Implementation of[](#implementation-of "Direct link to Implementation of")

MarkdownTextSplitterParams.chunkOverlap

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[chunkOverlap](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#chunkoverlap)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:29](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L29)

### chunkSize[](#chunksize "Direct link to chunkSize")

> **chunkSize**: `number` = `1000`

#### Implementation of[](#implementation-of-1 "Direct link to Implementation of")

MarkdownTextSplitterParams.chunkSize

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[chunkSize](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#chunksize)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:27](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L27)

### keepSeparator[](#keepseparator "Direct link to keepSeparator")

> **keepSeparator**: `boolean` = `false`

#### Implementation of[](#implementation-of-2 "Direct link to Implementation of")

MarkdownTextSplitterParams.keepSeparator

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[keepSeparator](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#keepseparator)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:31](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L31)

### lc\_kwargs[](#lc_kwargs "Direct link to lc_kwargs")

> **lc\_kwargs**: `SerializedFields`

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[lc\_kwargs](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#lc_kwargs)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/load/serializable.ts:57](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L57)

### lc\_namespace[](#lc_namespace "Direct link to lc_namespace")

> **lc\_namespace**: `string`\[\]

#### Inherited from[](#inherited-from-4 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[lc\_namespace](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#lc_namespace)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:25](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L25)

### lc\_serializable[](#lc_serializable "Direct link to lc_serializable")

> **lc\_serializable**: `boolean` = `false`

#### Inherited from[](#inherited-from-5 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[lc\_serializable](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#lc_serializable)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/load/serializable.ts:55](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L55)

### lengthFunction[](#lengthfunction "Direct link to lengthFunction")

> **lengthFunction**: (`text`: `string`) => `number` | (`text`: `string`) => `Promise`<`number`\>

#### Implementation of[](#implementation-of-3 "Direct link to Implementation of")

MarkdownTextSplitterParams.lengthFunction

#### Inherited from[](#inherited-from-6 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[lengthFunction](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#lengthfunction)

#### Defined in[](#defined-in-7 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:33](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L33)

### separators[](#separators "Direct link to separators")

> **separators**: `string`\[\]

#### Inherited from[](#inherited-from-7 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[separators](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#separators)

#### Defined in[](#defined-in-8 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:259](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L259)

### lc\_runnable[](#lc_runnable "Direct link to lc_runnable")

> `Protected` **lc\_runnable**: `boolean` = `true`

#### Inherited from[](#inherited-from-8 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[lc\_runnable](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#lc_runnable)

#### Defined in[](#defined-in-9 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:34](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L34)

Accessors[](#accessors "Direct link to Accessors")
---------------------------------------------------

### lc\_aliases[](#lc_aliases "Direct link to lc_aliases")

A map of aliases for constructor args. Keys are the attribute names, e.g. "foo". Values are the alias that will replace the key in serialization. This is used to eg. make argument names match Python.

> **lc\_aliases**(): `undefined` | {}

#### Returns[](#returns-1 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-9 "Direct link to Inherited from")

RecursiveCharacterTextSplitter.lc\_aliases

#### Defined in[](#defined-in-10 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

#### Inherited from[](#inherited-from-10 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[lc\_aliases](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#lc_aliases)

#### Defined in[](#defined-in-11 "Direct link to Defined in")

[langchain/src/load/serializable.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L90)

### lc\_attributes[](#lc_attributes "Direct link to lc_attributes")

A map of additional attributes to merge with constructor args. Keys are the attribute names, e.g. "foo". Values are the attribute values, which will be serialized. These attributes need to be accepted by the constructor as arguments.

> **lc\_attributes**(): `undefined` | `SerializedFields`

#### Returns[](#returns-2 "Direct link to Returns")

`undefined` | `SerializedFields`

#### Inherited from[](#inherited-from-11 "Direct link to Inherited from")

RecursiveCharacterTextSplitter.lc\_attributes

#### Defined in[](#defined-in-12 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L80)

#### Inherited from[](#inherited-from-12 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[lc\_attributes](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#lc_attributes)

#### Defined in[](#defined-in-13 "Direct link to Defined in")

[langchain/src/load/serializable.ts:80](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L80)

### lc\_secrets[](#lc_secrets "Direct link to lc_secrets")

A map of secrets, which will be omitted from serialization. Keys are paths to the secret in constructor args, e.g. "foo.bar.baz". Values are the secret ids, which will be used when deserializing.

> **lc\_secrets**(): `undefined` | {}

#### Returns[](#returns-3 "Direct link to Returns")

`undefined` | {}

#### Inherited from[](#inherited-from-13 "Direct link to Inherited from")

RecursiveCharacterTextSplitter.lc\_secrets

#### Defined in[](#defined-in-14 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

#### Inherited from[](#inherited-from-14 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[lc\_secrets](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#lc_secrets)

#### Defined in[](#defined-in-15 "Direct link to Defined in")

[langchain/src/load/serializable.ts:70](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L70)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

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

#### Returns[](#returns-4 "Direct link to Returns")

`Partial`<`BaseCallbackConfig`\>

#### Inherited from[](#inherited-from-15 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[\_patchConfig](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#_patchconfig)

#### Defined in[](#defined-in-16 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:146](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L146)

### \_streamIterator()[](#_streamiterator "Direct link to _streamiterator")

> **\_streamIterator**(`input`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], `options`?: `Partial`<`BaseCallbackConfig`\>): `AsyncGenerator`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], `any`, `unknown`\>

#### Parameters[](#parameters-2 "Direct link to Parameters")

Parameter

Type

`input`

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

`options?`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-5 "Direct link to Returns")

`AsyncGenerator`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], `any`, `unknown`\>

#### Inherited from[](#inherited-from-16 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[\_streamIterator](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#_streamiterator)

#### Defined in[](#defined-in-17 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:86](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L86)

### batch()[](#batch "Direct link to batch()")

> **batch**(`inputs`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\[\], `options`?: `Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\], `batchOptions`?: `object`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\[\]\>

#### Parameters[](#parameters-3 "Direct link to Parameters")

Parameter

Type

`inputs`

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\[\]

`options?`

`Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\]

`batchOptions?`

`object`

`batchOptions.maxConcurrency?`

`number`

#### Returns[](#returns-6 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\[\]\>

#### Inherited from[](#inherited-from-17 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[batch](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#batch)

#### Defined in[](#defined-in-18 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:63](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L63)

### bind()[](#bind "Direct link to bind()")

> **bind**(`kwargs`: `Partial`<`BaseCallbackConfig`\>): [`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], `BaseCallbackConfig`\>

#### Parameters[](#parameters-4 "Direct link to Parameters")

Parameter

Type

`kwargs`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-7 "Direct link to Returns")

[`RunnableBinding`](/docs/api/schema_runnable/classes/RunnableBinding)<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], `BaseCallbackConfig`\>

#### Inherited from[](#inherited-from-18 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[bind](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#bind)

#### Defined in[](#defined-in-19 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:41](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L41)

### createDocuments()[](#createdocuments "Direct link to createDocuments()")

> **createDocuments**(`texts`: `string`\[\], `metadatas`: `Record`<`string`, `any`\>\[\] = `[]`, `chunkHeaderOptions`: [`TextSplitterChunkHeaderOptions`](/docs/api/text_splitter/types/TextSplitterChunkHeaderOptions) = `{}`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[](#parameters-5 "Direct link to Parameters")

Parameter

Type

Default value

`texts`

`string`\[\]

`undefined`

`metadatas`

`Record`<`string`, `any`\>\[\]

`[]`

`chunkHeaderOptions`

[`TextSplitterChunkHeaderOptions`](/docs/api/text_splitter/types/TextSplitterChunkHeaderOptions)

`{}`

#### Returns[](#returns-8 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Inherited from[](#inherited-from-19 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[createDocuments](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#createdocuments)

#### Defined in[](#defined-in-20 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:76](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L76)

### invoke()[](#invoke "Direct link to invoke()")

> **invoke**(`input`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], `_options`?: `Partial`<`BaseCallbackConfig`\>): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[](#parameters-6 "Direct link to Parameters")

Parameter

Type

`input`

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

`_options?`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-9 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Inherited from[](#inherited-from-20 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[invoke](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#invoke)

#### Defined in[](#defined-in-21 "Direct link to Defined in")

[langchain/src/schema/document.ts:28](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/document.ts#L28)

### mergeSplits()[](#mergesplits "Direct link to mergeSplits()")

> **mergeSplits**(`splits`: `string`\[\], `separator`: `string`): `Promise`<`string`\[\]\>

#### Parameters[](#parameters-7 "Direct link to Parameters")

Parameter

Type

`splits`

`string`\[\]

`separator`

`string`

#### Returns[](#returns-10 "Direct link to Returns")

`Promise`<`string`\[\]\>

#### Inherited from[](#inherited-from-21 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[mergeSplits](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#mergesplits)

#### Defined in[](#defined-in-22 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:162](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L162)

### pipe()[](#pipe "Direct link to pipe()")

> **pipe**<NewRunOutput\>(`coerceable`: [`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], `NewRunOutput`\>): [`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], `NewRunOutput`\>

#### Type parameters[](#type-parameters "Direct link to Type parameters")

*   `NewRunOutput`

#### Parameters[](#parameters-8 "Direct link to Parameters")

Parameter

Type

`coerceable`

[`RunnableLike`](/docs/api/schema_runnable/types/RunnableLike)<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], `NewRunOutput`\>

#### Returns[](#returns-11 "Direct link to Returns")

[`RunnableSequence`](/docs/api/schema_runnable/classes/RunnableSequence)<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], `NewRunOutput`\>

#### Inherited from[](#inherited-from-22 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[pipe](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#pipe)

#### Defined in[](#defined-in-23 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:153](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L153)

### splitDocuments()[](#splitdocuments "Direct link to splitDocuments()")

> **splitDocuments**(`documents`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], `chunkHeaderOptions`: [`TextSplitterChunkHeaderOptions`](/docs/api/text_splitter/types/TextSplitterChunkHeaderOptions) = `{}`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[](#parameters-9 "Direct link to Parameters")

Parameter

Type

`documents`

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

`chunkHeaderOptions`

[`TextSplitterChunkHeaderOptions`](/docs/api/text_splitter/types/TextSplitterChunkHeaderOptions)

#### Returns[](#returns-12 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Inherited from[](#inherited-from-23 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[splitDocuments](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#splitdocuments)

#### Defined in[](#defined-in-24 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:145](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L145)

### splitText()[](#splittext "Direct link to splitText()")

> **splitText**(`text`: `string`): `Promise`<`string`\[\]\>

#### Parameters[](#parameters-10 "Direct link to Parameters")

Parameter

Type

`text`

`string`

#### Returns[](#returns-13 "Direct link to Returns")

`Promise`<`string`\[\]\>

#### Inherited from[](#inherited-from-24 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[splitText](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#splittext)

#### Defined in[](#defined-in-25 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:316](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L316)

### stream()[](#stream "Direct link to stream()")

> **stream**(`input`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], `options`?: `Partial`<`BaseCallbackConfig`\>): `Promise`<`IterableReadableStream`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>\>

#### Parameters[](#parameters-11 "Direct link to Parameters")

Parameter

Type

`input`

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

`options?`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-14 "Direct link to Returns")

`Promise`<`IterableReadableStream`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>\>

#### Inherited from[](#inherited-from-25 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[stream](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#stream)

#### Defined in[](#defined-in-26 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:93](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L93)

### toJSON()[](#tojson "Direct link to toJSON()")

> **toJSON**(): [`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Returns[](#returns-15 "Direct link to Returns")

[`Serialized`](/docs/api/load_serializable/types/Serialized)

#### Inherited from[](#inherited-from-26 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[toJSON](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#tojson)

#### Defined in[](#defined-in-27 "Direct link to Defined in")

[langchain/src/load/serializable.ts:98](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L98)

### toJSONNotImplemented()[](#tojsonnotimplemented "Direct link to toJSONNotImplemented()")

> **toJSONNotImplemented**(): [`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Returns[](#returns-16 "Direct link to Returns")

[`SerializedNotImplemented`](/docs/api/load_serializable/interfaces/SerializedNotImplemented)

#### Inherited from[](#inherited-from-27 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[toJSONNotImplemented](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#tojsonnotimplemented)

#### Defined in[](#defined-in-28 "Direct link to Defined in")

[langchain/src/load/serializable.ts:151](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/load/serializable.ts#L151)

### transformDocuments()[](#transformdocuments "Direct link to transformDocuments()")

> **transformDocuments**(`documents`: [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\], `chunkHeaderOptions`: [`TextSplitterChunkHeaderOptions`](/docs/api/text_splitter/types/TextSplitterChunkHeaderOptions) = `{}`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[](#parameters-12 "Direct link to Parameters")

Parameter

Type

`documents`

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

`chunkHeaderOptions`

[`TextSplitterChunkHeaderOptions`](/docs/api/text_splitter/types/TextSplitterChunkHeaderOptions)

#### Returns[](#returns-17 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Inherited from[](#inherited-from-28 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[transformDocuments](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#transformdocuments)

#### Defined in[](#defined-in-29 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:49](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L49)

### fromLanguage()[](#fromlanguage "Direct link to fromLanguage()")

> `Static` **fromLanguage**(`language`: "cpp" | "go" | "java" | "js" | "php" | "proto" | "python" | "rst" | "ruby" | "rust" | "scala" | "swift" | "markdown" | "latex" | "html" | "sol", `options`?: `Partial`<[`RecursiveCharacterTextSplitterParams`](/docs/api/text_splitter/interfaces/RecursiveCharacterTextSplitterParams)\>): [`RecursiveCharacterTextSplitter`](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter)

#### Parameters[](#parameters-13 "Direct link to Parameters")

Parameter

Type

`language`

"cpp" | "go" | "java" | "js" | "php" | "proto" | "python" | "rst" | "ruby" | "rust" | "scala" | "swift" | "markdown" | "latex" | "html" | "sol"

`options?`

`Partial`<[`RecursiveCharacterTextSplitterParams`](/docs/api/text_splitter/interfaces/RecursiveCharacterTextSplitterParams)\>

#### Returns[](#returns-18 "Direct link to Returns")

[`RecursiveCharacterTextSplitter`](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter)

#### Inherited from[](#inherited-from-29 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[fromLanguage](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#fromlanguage)

#### Defined in[](#defined-in-30 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:320](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L320)

### getSeparatorsForLanguage()[](#getseparatorsforlanguage "Direct link to getSeparatorsForLanguage()")

> `Static` **getSeparatorsForLanguage**(`language`: "cpp" | "go" | "java" | "js" | "php" | "proto" | "python" | "rst" | "ruby" | "rust" | "scala" | "swift" | "markdown" | "latex" | "html" | "sol"): `string`\[\]

#### Parameters[](#parameters-14 "Direct link to Parameters")

Parameter

Type

`language`

"cpp" | "go" | "java" | "js" | "php" | "proto" | "python" | "rst" | "ruby" | "rust" | "scala" | "swift" | "markdown" | "latex" | "html" | "sol"

#### Returns[](#returns-19 "Direct link to Returns")

`string`\[\]

#### Inherited from[](#inherited-from-30 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[getSeparatorsForLanguage](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#getseparatorsforlanguage)

#### Defined in[](#defined-in-31 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:331](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L331)

### isRunnable()[](#isrunnable "Direct link to isRunnable()")

> `Static` **isRunnable**(`thing`: `any`): thing is Runnable<any, any, BaseCallbackConfig\>

#### Parameters[](#parameters-15 "Direct link to Parameters")

Parameter

Type

`thing`

`any`

#### Returns[](#returns-20 "Direct link to Returns")

thing is Runnable<any, any, BaseCallbackConfig\>

#### Inherited from[](#inherited-from-31 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[isRunnable](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#isrunnable)

#### Defined in[](#defined-in-32 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:164](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L164)

### \_callWithConfig()[](#_callwithconfig "Direct link to _callwithconfig")

> `Protected` **\_callWithConfig**<T\>(`func`: `Function`, `input`: `T`, `options`?: `BaseCallbackConfig` & {`runType`?: `string`;}): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Type parameters[](#type-parameters-1 "Direct link to Type parameters")

*   `T` _extends_ [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]

#### Parameters[](#parameters-16 "Direct link to Parameters")

Parameter

Type

`func`

(`input`: `T`) => `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

`input`

`T`

`options?`

`BaseCallbackConfig` & {`runType`?: `string`;}

#### Returns[](#returns-21 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Inherited from[](#inherited-from-32 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[\_callWithConfig](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#_callwithconfig)

#### Defined in[](#defined-in-33 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:117](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L117)

### \_getOptionsList()[](#_getoptionslist "Direct link to _getoptionslist")

> `Protected` **\_getOptionsList**(`options`: `Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\], `length`: `number` = `0`): `Partial`<`BaseCallbackConfig`\>\[\]

#### Parameters[](#parameters-17 "Direct link to Parameters")

Parameter

Type

Default value

`options`

`Partial`<`BaseCallbackConfig`\> | `Partial`<`BaseCallbackConfig`\>\[\]

`undefined`

`length`

`number`

`0`

#### Returns[](#returns-22 "Direct link to Returns")

`Partial`<`BaseCallbackConfig`\>\[\]

#### Inherited from[](#inherited-from-33 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[\_getOptionsList](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#_getoptionslist)

#### Defined in[](#defined-in-34 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:48](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L48)

### \_separateRunnableConfigFromCallOptions()[](#_separaterunnableconfigfromcalloptions "Direct link to _separaterunnableconfigfromcalloptions")

> `Protected` **\_separateRunnableConfigFromCallOptions**(`options`: `Partial`<`BaseCallbackConfig`\> = `{}`): \[`BaseCallbackConfig`, `Omit`<`Partial`<`BaseCallbackConfig`\>, _keyof_ `BaseCallbackConfig`\>\]

#### Parameters[](#parameters-18 "Direct link to Parameters")

Parameter

Type

`options`

`Partial`<`BaseCallbackConfig`\>

#### Returns[](#returns-23 "Direct link to Returns")

\[`BaseCallbackConfig`, `Omit`<`Partial`<`BaseCallbackConfig`\>, _keyof_ `BaseCallbackConfig`\>\]

#### Inherited from[](#inherited-from-34 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[\_separateRunnableConfigFromCallOptions](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#_separaterunnableconfigfromcalloptions)

#### Defined in[](#defined-in-35 "Direct link to Defined in")

[langchain/src/schema/runnable.ts:102](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/schema/runnable.ts#L102)

### splitOnSeparator()[](#splitonseparator "Direct link to splitOnSeparator()")

> `Protected` **splitOnSeparator**(`text`: `string`, `separator`: `string`): `string`\[\]

#### Parameters[](#parameters-19 "Direct link to Parameters")

Parameter

Type

`text`

`string`

`separator`

`string`

#### Returns[](#returns-24 "Direct link to Returns")

`string`\[\]

#### Inherited from[](#inherited-from-35 "Direct link to Inherited from")

[RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter).[splitOnSeparator](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter#splitonseparator)

#### Defined in[](#defined-in-36 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:58](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L58)