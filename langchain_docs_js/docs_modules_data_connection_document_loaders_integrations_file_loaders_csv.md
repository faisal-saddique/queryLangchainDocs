CSV files
=========

This example goes over how to load data from CSV files. The second argument is the `column` name to extract from the CSV file. One document will be created for each row in the CSV file. When `column` is not specified, each row is converted into a key/value pair with each key/value pair outputted to a new line in the document's `pageContent`. When `column` is specified, one document is created for each row, and the value of the specified column is used as the document's pageContent.

Setup[](#setup "Direct link to Setup")
---------------------------------------

*   npm
*   Yarn
*   pnpm

    npm install d3-dsv@2

    yarn add d3-dsv@2

    pnpm add d3-dsv@2

Usage, extracting all columns[](#usage-extracting-all-columns "Direct link to Usage, extracting all columns")
--------------------------------------------------------------------------------------------------------------

Example CSV file:

    id,text1,This is a sentence.2,This is another sentence.

Example code:

    import { CSVLoader } from "langchain/document_loaders/fs/csv";const loader = new CSVLoader("src/document_loaders/example_data/example.csv");const docs = await loader.load();/*[  Document {    "metadata": {      "line": 1,      "source": "src/document_loaders/example_data/example.csv",    },    "pageContent": "id: 1text: This is a sentence.",  },  Document {    "metadata": {      "line": 2,      "source": "src/document_loaders/example_data/example.csv",    },    "pageContent": "id: 2text: This is another sentence.",  },]*/

Usage, extracting a single column[](#usage-extracting-a-single-column "Direct link to Usage, extracting a single column")
--------------------------------------------------------------------------------------------------------------------------

Example CSV file:

    id,text1,This is a sentence.2,This is another sentence.

Example code:

    import { CSVLoader } from "langchain/document_loaders/fs/csv";const loader = new CSVLoader(  "src/document_loaders/example_data/example.csv",  "text");const docs = await loader.load();/*[  Document {    "metadata": {      "line": 1,      "source": "src/document_loaders/example_data/example.csv",    },    "pageContent": "This is a sentence.",  },  Document {    "metadata": {      "line": 2,      "source": "src/document_loaders/example_data/example.csv",    },    "pageContent": "This is another sentence.",  },]*/