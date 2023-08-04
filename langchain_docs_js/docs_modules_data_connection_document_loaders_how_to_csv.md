CSV
===

> A [comma-separated values (CSV)](https://en.wikipedia.org/wiki/Comma-separated_values) file is a delimited text file that uses a comma to separate values. Each line of the file is a data record. Each record consists of one or more fields, separated by commas.

Load CSV data with a single row per document.

Setup[](#setup "Direct link to Setup")
---------------------------------------

    npm install d3-dsv@2

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