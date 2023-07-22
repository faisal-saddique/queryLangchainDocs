GitBook
=======

This example goes over how to load data from any GitBook, using Cheerio. One document will be created for each page.

Setup[​](#setup "Direct link to Setup")
---------------------------------------

*   npm
*   Yarn
*   pnpm

    npm install cheerio

    yarn add cheerio

    pnpm add cheerio

Load from single GitBook page[​](#load-from-single-gitbook-page "Direct link to Load from single GitBook page")
---------------------------------------------------------------------------------------------------------------

    import { GitbookLoader } from "langchain/document_loaders/web/gitbook";const loader = new GitbookLoader(  "https://docs.gitbook.com/product-tour/navigation");const docs = await loader.load();

Load from all paths in a given GitBook[​](#load-from-all-paths-in-a-given-gitbook "Direct link to Load from all paths in a given GitBook")
------------------------------------------------------------------------------------------------------------------------------------------

For this to work, the GitbookLoader needs to be initialized with the root path ([https://docs.gitbook.com](https://docs.gitbook.com) in this example) and have `shouldLoadAllPaths` set to `true`.

    import { GitbookLoader } from "langchain/document_loaders/web/gitbook";const loader = new GitbookLoader("https://docs.gitbook.com", {  shouldLoadAllPaths: true,});const docs = await loader.load();