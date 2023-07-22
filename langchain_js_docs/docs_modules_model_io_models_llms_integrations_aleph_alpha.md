AlephAlpha
==========

LangChain.js supports AlephAlpha's Luminous family of models. You'll need to sign up for an API key [on their website](https://www.aleph-alpha.com/).

Here's an example:

    import { AlephAlpha } from "langchain/llms/aleph_alpha";const model = new AlephAlpha({  aleph_alpha_api_key: "YOUR_ALEPH_ALPHA_API_KEY", // Or set as process.env.ALEPH_ALPHA_API_KEY});const res = await model.call(`Is cereal soup?`);console.log({ res });/*  {    res: "\nIs soup a cereal? I don’t think so, but it is delicious."  } */

#### API Reference:

*   [AlephAlpha](/docs/api/llms_aleph_alpha/classes/AlephAlpha) from `langchain/llms/aleph_alpha`