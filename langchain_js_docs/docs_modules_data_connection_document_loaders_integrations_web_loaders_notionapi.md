Notion API
==========

This guide will take you through the steps required to load documents from Notion pages and databases using the Notion API.

Overview[​](#overview "Direct link to Overview")
------------------------------------------------

Notion is a versatile productivity platform that consolidates note-taking, task management, and data organization tools into one interface.

This document loader is able to take full Notion pages and databases and turn them into a LangChain Documents ready to be integrated into your projects.

Setup[​](#setup "Direct link to Setup")
---------------------------------------

1.  You will first need to install the official Notion client and the [notion-to-md](https://www.npmjs.com/package/notion-to-md) package as peer dependencies:

*   npm
*   Yarn
*   pnpm

    npm install @notionhq/client notion-to-md

    yarn add @notionhq/client notion-to-md

    pnpm add @notionhq/client notion-to-md

2.  Create a [Notion integration](https://www.notion.so/my-integrations) and securely record the Internal Integration Secret (also known as `NOTION_INTEGRATION_TOKEN`).
3.  Add a connection to your new integration on your page or database. To do this open your Notion page, go to the settings pips in the top right and scroll down to `Add connections` and select your new integration.
4.  Get the `PAGE_ID` or `DATABASE_ID` for the page or database you want to load.

> The 32 char hex in the url path represents the `ID`. For example:

> PAGE\_ID: [https://www.notion.so/skarard/LangChain-Notion-API-`b34ca03f219c4420a6046fc4bdfdf7b4`](https://www.notion.so/skarard/LangChain-Notion-API-b34ca03f219c4420a6046fc4bdfdf7b4)

> DATABASE\_ID: [https://www.notion.so/skarard/`c393f19c3903440da0d34bf9c6c12ff2`?v=9c70a0f4e174498aa0f9021e0a9d52de](https://www.notion.so/skarard/c393f19c3903440da0d34bf9c6c12ff2?v=9c70a0f4e174498aa0f9021e0a9d52de)

> REGEX: `/(?<!=)[0-9a-f]{32}/`

Example Usage[​](#example-usage "Direct link to Example Usage")
---------------------------------------------------------------

    import { NotionAPILoader } from "langchain/document_loaders/web/notionapi";// Loading a page (including child pages all as separate documents)const pageLoader = new NotionAPILoader({  clientOptions: {    auth: "<NOTION_INTEGRATION_TOKEN>",  },  id: "<PAGE_ID>",  type: "page",});// A page contents is likely to be more than 1000 characters so it's split into multiple documents (important for vectorization)const pageDocs = await pageLoader.loadAndSplit();console.log({ pageDocs });// Loading a database (each row is a separate document with all properties as metadata)const dbLoader = new NotionAPILoader({  clientOptions: {    auth: "<NOTION_INTEGRATION_TOKEN>",  },  id: "<DATABASE_ID>",  type: "database",});// A database row contents is likely to be less than 1000 characters so it's not split into multiple documentsconst dbDocs = await dbLoader.load();console.log({ dbDocs });

#### API Reference:

*   [NotionAPILoader](/docs/api/document_loaders_web_notionapi/classes/NotionAPILoader) from `langchain/document_loaders/web/notionapi`