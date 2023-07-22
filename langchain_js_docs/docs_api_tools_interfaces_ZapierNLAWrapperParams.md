ZapierNLAWrapperParams
======================

Hierarchy[​](#hierarchy "Direct link to Hierarchy")
---------------------------------------------------

*   `AsyncCallerParams`.**ZapierNLAWrapperParams**

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### apiKey?[​](#apikey "Direct link to apiKey?")

> **apiKey**: `string`

NLA API Key. Found in the NLA documentation [https://nla.zapier.com/docs/authentication/#api-key](https://nla.zapier.com/docs/authentication/#api-key) Can also be set via the environment variable `ZAPIER_NLA_API_KEY`

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/tools/zapier.ts:29](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/zapier.ts#L29)

### maxConcurrency?[​](#maxconcurrency "Direct link to maxConcurrency?")

> **maxConcurrency**: `number`

The maximum number of concurrent calls that can be made. Defaults to `Infinity`, which means no limit.

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

AsyncCallerParams.maxConcurrency

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:21](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/util/async_caller.ts#L21)

### maxRetries?[​](#maxretries "Direct link to maxRetries?")

> **maxRetries**: `number`

The maximum number of retries that can be made for a single call, with an exponential backoff between each attempt. Defaults to 6.

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

AsyncCallerParams.maxRetries

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/util/async\_caller.ts:26](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/util/async_caller.ts#L26)

### oauthAccessToken?[​](#oauthaccesstoken "Direct link to oauthAccessToken?")

> **oauthAccessToken**: `string`

NLA OAuth Access Token. Found in the NLA documentation [https://nla.zapier.com/docs/authentication/#oauth-credentials](https://nla.zapier.com/docs/authentication/#oauth-credentials) Can also be set via the environment variable `ZAPIER_NLA_OAUTH_ACCESS_TOKEN`

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/tools/zapier.ts:34](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/tools/zapier.ts#L34)