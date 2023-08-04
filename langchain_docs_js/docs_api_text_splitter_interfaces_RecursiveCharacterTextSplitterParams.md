RecursiveCharacterTextSplitterParams
====================================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`TextSplitterParams`](/docs/api/text_splitter/interfaces/TextSplitterParams).**RecursiveCharacterTextSplitterParams**

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### chunkOverlap[](#chunkoverlap "Direct link to chunkOverlap")

> **chunkOverlap**: `number`

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[TextSplitterParams](/docs/api/text_splitter/interfaces/TextSplitterParams).[chunkOverlap](/docs/api/text_splitter/interfaces/TextSplitterParams#chunkoverlap)

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/text\_splitter.ts:8](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L8)

### chunkSize[](#chunksize "Direct link to chunkSize")

> **chunkSize**: `number`

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[TextSplitterParams](/docs/api/text_splitter/interfaces/TextSplitterParams).[chunkSize](/docs/api/text_splitter/interfaces/TextSplitterParams#chunksize)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:7](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L7)

### keepSeparator[](#keepseparator "Direct link to keepSeparator")

> **keepSeparator**: `boolean`

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[TextSplitterParams](/docs/api/text_splitter/interfaces/TextSplitterParams).[keepSeparator](/docs/api/text_splitter/interfaces/TextSplitterParams#keepseparator)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:9](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L9)

### separators[](#separators "Direct link to separators")

> **separators**: `string`\[\]

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:230](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L230)

### lengthFunction?[](#lengthfunction "Direct link to lengthFunction?")

> **lengthFunction**: (`text`: `string`) => `number` | (`text`: `string`) => `Promise`<`number`\>

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[TextSplitterParams](/docs/api/text_splitter/interfaces/TextSplitterParams).[lengthFunction](/docs/api/text_splitter/interfaces/TextSplitterParams#lengthfunction)

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:10](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L10)