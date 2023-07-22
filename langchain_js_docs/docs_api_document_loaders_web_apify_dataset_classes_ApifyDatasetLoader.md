ApifyDatasetLoader
==================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseDocumentLoader`](/docs/api/document_loaders_base/classes/BaseDocumentLoader).**ApifyDatasetLoader**

Implements[​](#implements "Direct link to Implements")
------------------------------------------------------

*   [`DocumentLoader`](/docs/api/document_loaders_base/interfaces/DocumentLoader)

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new ApifyDatasetLoader**(`datasetId`: `string`, `config`: `object`): [`ApifyDatasetLoader`](/docs/api/document_loaders_web_apify_dataset/classes/ApifyDatasetLoader)

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`datasetId`

`string`

`config`

`object`

`config.datasetMappingFunction`

[`ApifyDatasetMappingFunction`](/docs/api/document_loaders_web_apify_dataset/types/ApifyDatasetMappingFunction)

`config.clientOptions?`

`ApifyClientOptions`

#### Returns[​](#returns "Direct link to Returns")

[`ApifyDatasetLoader`](/docs/api/document_loaders_web_apify_dataset/classes/ApifyDatasetLoader)

#### Overrides[​](#overrides "Direct link to Overrides")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[constructor](/docs/api/document_loaders_base/classes/BaseDocumentLoader#constructor)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/document\_loaders/web/apify\_dataset.ts:28](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/apify_dataset.ts#L28)

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### apifyClient[​](#apifyclient "Direct link to apifyClient")

> `Protected` **apifyClient**: `ApifyClient`

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/document\_loaders/web/apify\_dataset.ts:20](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/apify_dataset.ts#L20)

### datasetId[​](#datasetid "Direct link to datasetId")

> `Protected` **datasetId**: `string`

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/document\_loaders/web/apify\_dataset.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/apify_dataset.ts#L22)

### datasetMappingFunction[​](#datasetmappingfunction "Direct link to datasetMappingFunction")

> `Protected` **datasetMappingFunction**: `Function`

#### Type declaration[​](#type-declaration "Direct link to Type declaration")

> (`item`: `Record`<`string` | `number`, `unknown`\>): [`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>

##### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`item`

`Record`<`string` | `number`, `unknown`\>

##### Returns[​](#returns-1 "Direct link to Returns")

[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/document\_loaders/web/apify\_dataset.ts:24](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/apify_dataset.ts#L24)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### load()[​](#load "Direct link to load()")

> **load**(): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Returns[​](#returns-2 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Implementation of[​](#implementation-of "Direct link to Implementation of")

[DocumentLoader](/docs/api/document_loaders_base/interfaces/DocumentLoader).[load](/docs/api/document_loaders_base/interfaces/DocumentLoader#load)

#### Overrides[​](#overrides-1 "Direct link to Overrides")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[load](/docs/api/document_loaders_base/classes/BaseDocumentLoader#load)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/document\_loaders/web/apify\_dataset.ts:51](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/apify_dataset.ts#L51)

### loadAndSplit()[​](#loadandsplit "Direct link to loadAndSplit()")

> **loadAndSplit**(`splitter`: [`TextSplitter`](/docs/api/text_splitter/classes/TextSplitter) = `...`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[​](#parameters-2 "Direct link to Parameters")

Parameter

Type

`splitter`

[`TextSplitter`](/docs/api/text_splitter/classes/TextSplitter)

#### Returns[​](#returns-3 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Implementation of[​](#implementation-of-1 "Direct link to Implementation of")

[DocumentLoader](/docs/api/document_loaders_base/interfaces/DocumentLoader).[loadAndSplit](/docs/api/document_loaders_base/interfaces/DocumentLoader#loadandsplit)

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[loadAndSplit](/docs/api/document_loaders_base/classes/BaseDocumentLoader#loadandsplit)

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/document\_loaders/base.ts:15](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/base.ts#L15)

### fromActorCall()[​](#fromactorcall "Direct link to fromActorCall()")

Create an ApifyDatasetLoader by calling an Actor on the Apify platform and waiting for its results to be ready.

> `Static` **fromActorCall**(`actorId`: `string`, `input`: `Record`<`string` | `number`, `unknown`\>, `config`: `object`): `Promise`<[`ApifyDatasetLoader`](/docs/api/document_loaders_web_apify_dataset/classes/ApifyDatasetLoader)\>

#### Parameters[​](#parameters-3 "Direct link to Parameters")

Parameter

Type

Description

`actorId`

`string`

The ID or name of the Actor on the Apify platform.

`input`

`Record`<`string` | `number`, `unknown`\>

The input object of the Actor that you're trying to run.

`config`

`object`

\-

`config.datasetMappingFunction`

[`ApifyDatasetMappingFunction`](/docs/api/document_loaders_web_apify_dataset/types/ApifyDatasetMappingFunction)

\-

`config.callOptions?`

`ActorCallOptions`

\-

`config.clientOptions?`

`ApifyClientOptions`

\-

#### Returns[​](#returns-4 "Direct link to Returns")

`Promise`<[`ApifyDatasetLoader`](/docs/api/document_loaders_web_apify_dataset/classes/ApifyDatasetLoader)\>

An instance of `ApifyDatasetLoader` with the results from the Actor run.

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/document\_loaders/web/apify\_dataset.ts:66](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/apify_dataset.ts#L66)

### fromActorTaskCall()[​](#fromactortaskcall "Direct link to fromActorTaskCall()")

Create an ApifyDatasetLoader by calling a saved Actor task on the Apify platform and waiting for its results to be ready.

> `Static` **fromActorTaskCall**(`taskId`: `string`, `input`: `Record`<`string` | `number`, `unknown`\>, `config`: `object`): `Promise`<[`ApifyDatasetLoader`](/docs/api/document_loaders_web_apify_dataset/classes/ApifyDatasetLoader)\>

#### Parameters[​](#parameters-4 "Direct link to Parameters")

Parameter

Type

Description

`taskId`

`string`

The ID or name of the task on the Apify platform.

`input`

`Record`<`string` | `number`, `unknown`\>

The input object of the task that you're trying to run. Overrides the task's saved input.

`config`

`object`

\-

`config.datasetMappingFunction`

[`ApifyDatasetMappingFunction`](/docs/api/document_loaders_web_apify_dataset/types/ApifyDatasetMappingFunction)

\-

`config.callOptions?`

`TaskCallOptions`

\-

`config.clientOptions?`

`ApifyClientOptions`

\-

#### Returns[​](#returns-5 "Direct link to Returns")

`Promise`<[`ApifyDatasetLoader`](/docs/api/document_loaders_web_apify_dataset/classes/ApifyDatasetLoader)\>

An instance of `ApifyDatasetLoader` with the results from the task's run.

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/document\_loaders/web/apify\_dataset.ts:98](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/document_loaders/web/apify_dataset.ts#L98)