WebBrowserArgs
==============

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   [`ToolParams`](/docs/api/tools/interfaces/ToolParams).**WebBrowserArgs**

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### embeddings[​](#embeddings "Direct link to embeddings")

> **embeddings**: [`Embeddings`](/docs/api/embeddings_base/classes/Embeddings)

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/tools/webbrowser.ts:150](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/webbrowser.ts#L150)

### model[​](#model "Direct link to model")

> **model**: [`BaseLanguageModel`](/docs/api/base_language/classes/BaseLanguageModel)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/tools/webbrowser.ts:148](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/webbrowser.ts#L148)

### axiosConfig?[​](#axiosconfig "Direct link to axiosConfig?")

> **axiosConfig**: `Omit`<`AxiosRequestConfig`<`any`\>, "url"\>

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/tools/webbrowser.ts:154](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/webbrowser.ts#L154)

### callbackManager?[​](#callbackmanager "Direct link to callbackManager?")

> **callbackManager**: [`CallbackManager`](/docs/api/callbacks/classes/CallbackManager)

#### Deprecated[​](#deprecated "Direct link to Deprecated")

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/tools/webbrowser.ts:157](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/webbrowser.ts#L157)

### callbacks?[​](#callbacks "Direct link to callbacks?")

> **callbacks**: [`Callbacks`](/docs/api/callbacks/types/Callbacks)

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[ToolParams](/docs/api/tools/interfaces/ToolParams).[callbacks](/docs/api/tools/interfaces/ToolParams#callbacks)

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:23](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L23)

### headers?[​](#headers "Direct link to headers?")

> **headers**: `Headers`

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/tools/webbrowser.ts:152](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/webbrowser.ts#L152)

### metadata?[​](#metadata "Direct link to metadata?")

> **metadata**: `Record`<`string`, `unknown`\>

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[ToolParams](/docs/api/tools/interfaces/ToolParams).[metadata](/docs/api/tools/interfaces/ToolParams#metadata)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:25](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L25)

### tags?[​](#tags "Direct link to tags?")

> **tags**: `string`\[\]

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[ToolParams](/docs/api/tools/interfaces/ToolParams).[tags](/docs/api/tools/interfaces/ToolParams#tags)

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:24](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L24)

### textSplitter?[​](#textsplitter "Direct link to textSplitter?")

> **textSplitter**: [`TextSplitter`](/docs/api/text_splitter/classes/TextSplitter)

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[langchain/src/tools/webbrowser.ts:159](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/webbrowser.ts#L159)

### verbose?[​](#verbose "Direct link to verbose?")

> **verbose**: `boolean`

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[ToolParams](/docs/api/tools/interfaces/ToolParams).[verbose](/docs/api/tools/interfaces/ToolParams#verbose)

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[langchain/src/base\_language/index.ts:22](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/base_language/index.ts#L22)