FigmaFileLoader
===============

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`BaseDocumentLoader`](/docs/api/document_loaders_base/classes/BaseDocumentLoader).**FigmaFileLoader**

Implements[](#implements "Direct link to Implements")
------------------------------------------------------

*   [`FigmaLoaderParams`](/docs/api/document_loaders_web_figma/interfaces/FigmaLoaderParams)

Constructors[](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[](#constructor "Direct link to constructor()")

> **new FigmaFileLoader**(«destructured»: [`FigmaLoaderParams`](/docs/api/document_loaders_web_figma/interfaces/FigmaLoaderParams)): [`FigmaFileLoader`](/docs/api/document_loaders_web_figma/classes/FigmaFileLoader)

#### Parameters[](#parameters "Direct link to Parameters")

Parameter

Type

`«destructured»`

[`FigmaLoaderParams`](/docs/api/document_loaders_web_figma/interfaces/FigmaLoaderParams)

#### Returns[](#returns "Direct link to Returns")

[`FigmaFileLoader`](/docs/api/document_loaders_web_figma/classes/FigmaFileLoader)

#### Overrides[](#overrides "Direct link to Overrides")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[constructor](/docs/api/document_loaders_base/classes/BaseDocumentLoader#constructor)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/document\_loaders/web/figma.ts:42](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/figma.ts#L42)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### fileKey[](#filekey "Direct link to fileKey")

> **fileKey**: `string`

#### Implementation of[](#implementation-of "Direct link to Implementation of")

[FigmaLoaderParams](/docs/api/document_loaders_web_figma/interfaces/FigmaLoaderParams).[fileKey](/docs/api/document_loaders_web_figma/interfaces/FigmaLoaderParams#filekey)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/document\_loaders/web/figma.ts:38](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/figma.ts#L38)

### nodeIds[](#nodeids "Direct link to nodeIds")

> **nodeIds**: `string`\[\]

#### Implementation of[](#implementation-of-1 "Direct link to Implementation of")

[FigmaLoaderParams](/docs/api/document_loaders_web_figma/interfaces/FigmaLoaderParams).[nodeIds](/docs/api/document_loaders_web_figma/interfaces/FigmaLoaderParams#nodeids)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/document\_loaders/web/figma.ts:36](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/figma.ts#L36)

### accessToken?[](#accesstoken "Direct link to accessToken?")

> **accessToken**: `string`

#### Implementation of[](#implementation-of-2 "Direct link to Implementation of")

[FigmaLoaderParams](/docs/api/document_loaders_web_figma/interfaces/FigmaLoaderParams).[accessToken](/docs/api/document_loaders_web_figma/interfaces/FigmaLoaderParams#accesstoken)

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/document\_loaders/web/figma.ts:34](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/figma.ts#L34)

Methods[](#methods "Direct link to Methods")
---------------------------------------------

### load()[](#load "Direct link to load()")

> **load**(): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Returns[](#returns-1 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Overrides[](#overrides-1 "Direct link to Overrides")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[load](/docs/api/document_loaders_base/classes/BaseDocumentLoader#load)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/document\_loaders/web/figma.ts:84](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/web/figma.ts#L84)

### loadAndSplit()[](#loadandsplit "Direct link to loadAndSplit()")

> **loadAndSplit**(`splitter`: [`TextSplitter`](/docs/api/text_splitter/classes/TextSplitter) = `...`): `Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Parameters[](#parameters-1 "Direct link to Parameters")

Parameter

Type

`splitter`

[`TextSplitter`](/docs/api/text_splitter/classes/TextSplitter)

#### Returns[](#returns-2 "Direct link to Returns")

`Promise`<[`Document`](/docs/api/document/classes/Document)<`Record`<`string`, `any`\>\>\[\]\>

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[BaseDocumentLoader](/docs/api/document_loaders_base/classes/BaseDocumentLoader).[loadAndSplit](/docs/api/document_loaders_base/classes/BaseDocumentLoader#loadandsplit)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/document\_loaders/base.ts:15](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/document_loaders/base.ts#L15)