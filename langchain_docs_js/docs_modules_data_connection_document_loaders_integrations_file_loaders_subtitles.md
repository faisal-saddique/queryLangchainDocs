Subtitles
=========

This example goes over how to load data from subtitle files. One document will be created for each subtitles file.

Setup[](#setup "Direct link to Setup")
---------------------------------------

*   npm
*   Yarn
*   pnpm

    npm install srt-parser-2

    yarn add srt-parser-2

    pnpm add srt-parser-2

Usage[](#usage "Direct link to Usage")
---------------------------------------

    import { SRTLoader } from "langchain/document_loaders/fs/srt";const loader = new SRTLoader(  "src/document_loaders/example_data/Star_Wars_The_Clone_Wars_S06E07_Crisis_at_the_Heart.srt");const docs = await loader.load();