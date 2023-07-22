SerializedFewShotTemplate
=========================

> **SerializedFewShotTemplate**: `object`

Type declaration[​](#type-declaration "Direct link to Type declaration")
------------------------------------------------------------------------

Member

Type

`_type`

"few\_shot"

`example_separator`

`string`

`examples`

`string` | [`Example`](/docs/api/schema/types/Example)\[\]

`input_variables`

`string`\[\]

`template_format`

[`TemplateFormat`](/docs/api/prompts/types/TemplateFormat)

`example_prompt`?

[`SerializedPromptTemplate`](/docs/api/prompts/types/SerializedPromptTemplate)

`prefix`?

`string`

`suffix`?

`string`

Defined in[​](#defined-in "Direct link to Defined in")
------------------------------------------------------

[langchain/src/prompts/serde.ts:11](https://github.com/hwchase17/langchainjs/blob/46e1734/langchain/src/prompts/serde.ts#L11)