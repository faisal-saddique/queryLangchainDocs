Figma
=====

This example goes over how to load data from a Figma file. You will need a Figma access token in order to get started.

    import { FigmaFileLoader } from "langchain/document_loaders/web/figma";const loader = new FigmaFileLoader({  accessToken: "FIGMA_ACCESS_TOKEN", // or load it from process.env.FIGMA_ACCESS_TOKEN  nodeIds: ["id1", "id2", "id3"],  fileKey: "key",});const docs = await loader.load();console.log({ docs });

#### API Reference:

*   [FigmaFileLoader](/docs/api/document_loaders_web_figma/classes/FigmaFileLoader) from `langchain/document_loaders/web/figma`

You can find your Figma file's key and node ids by opening the file in your browser and extracting them from the URL:

    https://www.figma.com/file/<YOUR FILE KEY HERE>/LangChainJS-Test?type=whiteboard&node-id=<YOUR NODE ID HERE>&t=e6lqWkKecuYQRyRg-0