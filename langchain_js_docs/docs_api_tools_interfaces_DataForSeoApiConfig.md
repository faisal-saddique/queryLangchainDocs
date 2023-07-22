DataForSeoApiConfig
===================

DataForSeoApiConfig

Description[​](#description "Direct link to Description")
---------------------------------------------------------

Represents the configuration object used to set up a DataForSeoAPISearch instance.

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### apiLogin?[​](#apilogin "Direct link to apiLogin?")

> **apiLogin**: `string`

#### Description[​](#description-1 "Direct link to Description")

The API login credential for DataForSEO. If not provided, it will be fetched from environment variables.

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/tools/dataforseo\_api\_search.ts:14](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/dataforseo_api_search.ts#L14)

### apiPassword?[​](#apipassword "Direct link to apiPassword?")

> **apiPassword**: `string`

#### Description[​](#description-2 "Direct link to Description")

The API password credential for DataForSEO. If not provided, it will be fetched from environment variables.

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/tools/dataforseo\_api\_search.ts:21](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/dataforseo_api_search.ts#L21)

### jsonResultFields?[​](#jsonresultfields "Direct link to jsonResultFields?")

> **jsonResultFields**: `string`\[\]

#### Description[​](#description-3 "Direct link to Description")

Specifies the fields to include in each result object.

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/tools/dataforseo\_api\_search.ts:49](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/dataforseo_api_search.ts#L49)

### jsonResultTypes?[​](#jsonresulttypes "Direct link to jsonResultTypes?")

> **jsonResultTypes**: `string`\[\]

#### Description[​](#description-4 "Direct link to Description")

Specifies the types of results to include in the output.

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/tools/dataforseo\_api\_search.ts:42](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/dataforseo_api_search.ts#L42)

### params?[​](#params "Direct link to params?")

> **params**: `Record`<`string`, `string` | `number` | `boolean`\>

#### Description[​](#description-5 "Direct link to Description")

Additional parameters to customize the API request.

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[langchain/src/tools/dataforseo\_api\_search.ts:28](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/dataforseo_api_search.ts#L28)

### topCount?[​](#topcount "Direct link to topCount?")

> **topCount**: `number`

#### Description[​](#description-6 "Direct link to Description")

Specifies the maximum number of results to return.

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[langchain/src/tools/dataforseo\_api\_search.ts:56](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/dataforseo_api_search.ts#L56)

### useJsonOutput?[​](#usejsonoutput "Direct link to useJsonOutput?")

> **useJsonOutput**: `boolean`

#### Description[​](#description-7 "Direct link to Description")

Determines if the output should be in JSON format.

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[langchain/src/tools/dataforseo\_api\_search.ts:35](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/dataforseo_api_search.ts#L35)