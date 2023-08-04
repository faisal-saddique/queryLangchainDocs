Webpages, with Cheerio
======================

This example goes over how to load data from webpages using Cheerio. One document will be created for each webpage.

Cheerio is a fast and lightweight library that allows you to parse and traverse HTML documents using a jQuery-like syntax. You can use Cheerio to extract data from web pages, without having to render them in a browser.

However, Cheerio does not simulate a web browser, so it cannot execute JavaScript code on the page. This means that it cannot extract data from dynamic web pages that require JavaScript to render. To do that, you can use the [PlaywrightWebBaseLoader](/docs/modules/data_connection/document_loaders/integrations/web_loaders/web_playwright) or [PuppeteerWebBaseLoader](/docs/modules/data_connection/document_loaders/integrations/web_loaders/web_puppeteer) instead.

Setup[](#setup "Direct link to Setup")
---------------------------------------

*   npm
*   Yarn
*   pnpm

    npm install cheerio

    yarn add cheerio

    pnpm add cheerio

Usage[](#usage "Direct link to Usage")
---------------------------------------

    import { CheerioWebBaseLoader } from "langchain/document_loaders/web/cheerio";const loader = new CheerioWebBaseLoader(  "https://news.ycombinator.com/item?id=34817881");const docs = await loader.load();

Usage, with a custom selector[](#usage-with-a-custom-selector "Direct link to Usage, with a custom selector")
--------------------------------------------------------------------------------------------------------------

    import { CheerioWebBaseLoader } from "langchain/document_loaders/web/cheerio";const loader = new CheerioWebBaseLoader(  "https://news.ycombinator.com/item?id=34817881",  {    selector: "p.athing",  });const docs = await loader.load();