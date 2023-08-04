TokenTextSplitterParams
=======================

Hierarchy[](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`TextSplitterParams`](/docs/api/text_splitter/interfaces/TextSplitterParams).**TokenTextSplitterParams**

Properties[](#properties "Direct link to Properties")
------------------------------------------------------

### allowedSpecial[](#allowedspecial "Direct link to allowedSpecial")

> **allowedSpecial**: `string`\[\] | "all"

#### Defined in[](#defined-in "Direct link to Defined in")

[langchain/src/text\_splitter.ts:683](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L683)

### chunkOverlap[](#chunkoverlap "Direct link to chunkOverlap")

> **chunkOverlap**: `number`

#### Inherited from[](#inherited-from "Direct link to Inherited from")

[TextSplitterParams](/docs/api/text_splitter/interfaces/TextSplitterParams).[chunkOverlap](/docs/api/text_splitter/interfaces/TextSplitterParams#chunkoverlap)

#### Defined in[](#defined-in-1 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:8](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L8)

### chunkSize[](#chunksize "Direct link to chunkSize")

> **chunkSize**: `number`

#### Inherited from[](#inherited-from-1 "Direct link to Inherited from")

[TextSplitterParams](/docs/api/text_splitter/interfaces/TextSplitterParams).[chunkSize](/docs/api/text_splitter/interfaces/TextSplitterParams#chunksize)

#### Defined in[](#defined-in-2 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:7](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L7)

### disallowedSpecial[](#disallowedspecial "Direct link to disallowedSpecial")

> **disallowedSpecial**: `string`\[\] | "all"

#### Defined in[](#defined-in-3 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:684](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L684)

### encodingName[](#encodingname "Direct link to encodingName")

> **encodingName**: `TiktokenEncoding`

#### Defined in[](#defined-in-4 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:682](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L682)

### keepSeparator[](#keepseparator "Direct link to keepSeparator")

> **keepSeparator**: `boolean`

#### Inherited from[](#inherited-from-2 "Direct link to Inherited from")

[TextSplitterParams](/docs/api/text_splitter/interfaces/TextSplitterParams).[keepSeparator](/docs/api/text_splitter/interfaces/TextSplitterParams#keepseparator)

#### Defined in[](#defined-in-5 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:9](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L9)

### lengthFunction?[](#lengthfunction "Direct link to lengthFunction?")

> **lengthFunction**: (`text`: `string`) => `number` | (`text`: `string`) => `Promise`<`number`\>

#### Inherited from[](#inherited-from-3 "Direct link to Inherited from")

[TextSplitterParams](/docs/api/text_splitter/interfaces/TextSplitterParams).[lengthFunction](/docs/api/text_splitter/interfaces/TextSplitterParams#lengthfunction)

#### Defined in[](#defined-in-6 "Direct link to Defined in")

[langchain/src/text\_splitter.ts:10](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/text_splitter.ts#L10)