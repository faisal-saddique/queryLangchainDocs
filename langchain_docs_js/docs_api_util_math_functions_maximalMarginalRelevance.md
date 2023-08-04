maximalMarginalRelevance()
==========================

This function implements the Maximal Marginal Relevance algorithm to select a set of embeddings that maximizes the diversity and relevance to a query embedding.

> **maximalMarginalRelevance**(`queryEmbedding`: `number`\[\] | `number`\[\]\[\], `embeddingList`: `number`\[\]\[\], `lambda`?: `number` = `0.5`, `k`?: `number` = `4`): `number`\[\]

Parameters[](#parameters "Direct link to Parameters")
------------------------------------------------------

Parameter

Type

Default value

Description

`queryEmbedding`

`number`\[\] | `number`\[\]\[\]

`undefined`

The query embedding.

`embeddingList`

`number`\[\]\[\]

`undefined`

The list of embeddings to select from.

`lambda?`

`number`

`0.5`

The trade-off parameter between relevance and diversity.

`k?`

`number`

`4`

The maximum number of embeddings to select.

Returns[](#returns "Direct link to Returns")
---------------------------------------------

`number`\[\]

The indexes of the selected embeddings in the embeddingList.

Defined in[](#defined-in "Direct link to Defined in")
------------------------------------------------------

[langchain/src/util/math.ts:90](https://github.com/hwchase17/langchainjs/blob/1c1274d/langchain/src/util/math.ts#L90)