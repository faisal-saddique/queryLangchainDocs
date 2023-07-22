College Confidential
====================

This example goes over how to load data from the college confidential website, using Cheerio. One document will be created for each page.

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

    import { CollegeConfidentialLoader } from "langchain/document_loaders/web/college_confidential";const loader = new CollegeConfidentialLoader(  "https://www.collegeconfidential.com/colleges/brown-university/");const docs = await loader.load();