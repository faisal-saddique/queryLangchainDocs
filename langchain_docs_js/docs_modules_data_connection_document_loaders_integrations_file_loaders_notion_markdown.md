Notion markdown export
======================

This example goes over how to load data from your Notion pages exported from the notion dashboard.

First, export your notion pages as **Markdown & CSV** as per the offical explanation [here](https://www.notion.so/help/export-your-content). Make sure to select `include subpages` and `Create folders for subpages.`

Then, unzip the downloaded file and move the unzipped folder into your repository. It should contain the markdown files of your pages.

Once the folder is in your repository, simply run the example below:

    import { NotionLoader } from "langchain/document_loaders/fs/notion";export const run = async () => {  /** Provide the directory path of your notion folder */  const directoryPath = "Notion_DB";  const loader = new NotionLoader(directoryPath);  const docs = await loader.load();  console.log({ docs });};

#### API Reference:

*   [NotionLoader](/docs/api/document_loaders_fs_notion/classes/NotionLoader) from `langchain/document_loaders/fs/notion`