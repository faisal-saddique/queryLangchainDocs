TextSplitterParams
==================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`CharacterTextSplitterParams`](/docs/api/text_splitter/interfaces/CharacterTextSplitterParams)
*   [`RecursiveCharacterTextSplitterParams`](/docs/api/text_splitter/interfaces/RecursiveCharacterTextSplitterParams)
*   [`TokenTextSplitterParams`](/docs/api/text_splitter/interfaces/TokenTextSplitterParams)

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### chunkOverlap[](#chunkoverlap "Direct link to chunkOverlap")

> **chunkOverlap**: `number`

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/text\_splitter.ts:8](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L8)

### chunkSize[](#chunksize "Direct link to chunkSize")

> **chunkSize**: `number`

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:7](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L7)

### keepSeparator[](#keepseparator "Direct link to keepSeparator")

> **keepSeparator**: `boolean`

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:9](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L9)

### lengthFunction?[](#lengthfunction "Direct link to lengthFunction?")

> **lengthFunction**: (`text`: `string`) => `number` | (`text`: `string`) => `Promise`<`number`\>

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:10](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L10)