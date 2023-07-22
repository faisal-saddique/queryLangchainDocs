BaseSageMakerContentHandler<InputType, OutputType\>
===================================================

A handler class to transform input from LLM to a format that SageMaker endpoint expects. Similarily, the class also handles transforming output from the SageMaker endpoint to a format that LLM class expects.

Example:

    class ContentHandler implements ContentHandlerBase<string, string> {  contentType = "application/json"  accepts = "application/json"  transformInput(prompt: string, modelKwargs: Record<string, unknown>) {    const inputString = JSON.stringify({      prompt,     ...modelKwargs    })    return Buffer.from(inputString)  }  transformOutput(output: Uint8Array) {    const responseJson = JSON.parse(Buffer.from(output).toString("utf-8"))    return responseJson[0].generated_text  }}

Type parameters[​](#type-parameters "Direct link to Type parameters")
---------------------------------------------------------------------

*   `InputType`
*   `OutputType`

Constructors[​](#constructors "Direct link to Constructors")
------------------------------------------------------------

### constructor()[​](#constructor "Direct link to constructor()")

> **new BaseSageMakerContentHandler**<InputType, OutputType\>(): [`BaseSageMakerContentHandler`](/docs/api/llms_sagemaker_endpoint/classes/BaseSageMakerContentHandler)<`InputType`, `OutputType`\>

#### Type parameters[​](#type-parameters-1 "Direct link to Type parameters")

*   `InputType`
*   `OutputType`

#### Returns[​](#returns "Direct link to Returns")

[`BaseSageMakerContentHandler`](/docs/api/llms_sagemaker_endpoint/classes/BaseSageMakerContentHandler)<`InputType`, `OutputType`\>

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### accepts[​](#accepts "Direct link to accepts")

> **accepts**: `string` = `"text/plain"`

The MIME type of the response data returned from endpoint

#### Defined in[​](#defined-in "Direct link to Defined in")

[langchain/src/llms/sagemaker\_endpoint.ts:40](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/sagemaker_endpoint.ts#L40)

### contentType[​](#contenttype "Direct link to contentType")

> **contentType**: `string` = `"text/plain"`

The MIME type of the input data passed to endpoint

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[langchain/src/llms/sagemaker\_endpoint.ts:37](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/sagemaker_endpoint.ts#L37)

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### transformInput()[​](#transforminput "Direct link to transformInput()")

Transforms the input to a format that model can accept as the request Body. Should return bytes or seekable file like object in the format specified in the contentType request header.

> `Abstract` **transformInput**(`prompt`: `InputType`, `modelKwargs`: `Record`<`string`, `unknown`\>): `Promise`<`Uint8Array`\>

#### Parameters[​](#parameters "Direct link to Parameters")

Parameter

Type

`prompt`

`InputType`

`modelKwargs`

`Record`<`string`, `unknown`\>

#### Returns[​](#returns-1 "Direct link to Returns")

`Promise`<`Uint8Array`\>

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[langchain/src/llms/sagemaker\_endpoint.ts:47](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/sagemaker_endpoint.ts#L47)

### transformOutput()[​](#transformoutput "Direct link to transformOutput()")

Transforms the output from the model to string that the LLM class expects.

> `Abstract` **transformOutput**(`output`: `Uint8Array`): `Promise`<`OutputType`\>

#### Parameters[​](#parameters-1 "Direct link to Parameters")

Parameter

Type

`output`

`Uint8Array`

#### Returns[​](#returns-2 "Direct link to Returns")

`Promise`<`OutputType`\>

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[langchain/src/llms/sagemaker\_endpoint.ts:55](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/llms/sagemaker_endpoint.ts#L55)