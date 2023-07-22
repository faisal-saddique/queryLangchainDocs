Hacker News
===========

This example goes over how to load data from the hacker news website, using Cheerio. One document will be created for each page.

Setup[​](#setup "Direct link to Setup")
---------------------------------------

*   npm
*   Yarn
*   pnpm

    npm install cheerio

    yarn add cheerio

    pnpm add cheerio

Usage[​](#usage "Direct link to Usage")
---------------------------------------

    import { HNLoader } from "langchain/document_loaders/web/hn";const loader = new HNLoader("https://news.ycombinator.com/item?id=34817881");const docs = await loader.load();