EPUB files
==========

This example goes over how to load data from EPUB files. By default, one document will be created for each chapter in the EPUB file, you can change this behavior by setting the `splitChapters` option to `false`.

Setup
=====

*   npm
*   Yarn
*   pnpm

    npm install epub2 html-to-text

    yarn add epub2 html-to-text

    pnpm add epub2 html-to-text

Usage, one document per chapter
===============================

    import { EPubLoader } from "langchain/document_loaders/fs/epub";const loader = new EPubLoader("src/document_loaders/example_data/example.epub");const docs = await loader.load();

Usage, one document per file
============================

    import { EPubLoader } from "langchain/document_loaders/fs/epub";const loader = new EPubLoader(  "src/document_loaders/example_data/example.epub",  {    splitChapters: false,  });const docs = await loader.load();