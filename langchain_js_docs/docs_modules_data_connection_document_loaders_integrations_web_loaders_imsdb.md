IMSDB
=====

This example goes over how to load data from the internet movie script database website, using Cheerio. One document will be created for each page.

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

    import { IMSDBLoader } from "langchain/document_loaders/web/imsdb";const loader = new IMSDBLoader("https://imsdb.com/scripts/BlacKkKlansman.html");const docs = await loader.load();