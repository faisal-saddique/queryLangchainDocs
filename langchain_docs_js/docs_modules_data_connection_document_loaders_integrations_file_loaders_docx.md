Docx files
==========

This example goes over how to load data from docx files.

Setup
=====

*   npm
*   Yarn
*   pnpm

    npm install mammoth

    yarn add mammoth

    pnpm add mammoth

Usage
=====

    import { DocxLoader } from "langchain/document_loaders/fs/docx";const loader = new DocxLoader(  "src/document_loaders/tests/example_data/attention.docx");const docs = await loader.load();