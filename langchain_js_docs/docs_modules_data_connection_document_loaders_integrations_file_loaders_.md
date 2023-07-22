File Loaders
============

Compatibility

Only available on Node.js.

These loaders are used to load files given a filesystem path or a Blob object.

[

📄️ Folders with multiple files
-------------------------------

This example goes over how to load data from folders with multiple files. The second argument is a map of file extensions to loader factories. Each file will be passed to the matching loader, and the resulting documents will be concatenated together.

](/docs/modules/data_connection/document_loaders/integrations/file_loaders/directory)

[

📄️ CSV files
-------------

This example goes over how to load data from CSV files. The second argument is the column name to extract from the CSV file. One document will be created for each row in the CSV file. When column is not specified, each row is converted into a key/value pair with each key/value pair outputted to a new line in the document's pageContent. When column is specified, one document is created for each row, and the value of the specified column is used as the document's pageContent.

](/docs/modules/data_connection/document_loaders/integrations/file_loaders/csv)

[

📄️ Docx files
--------------

This example goes over how to load data from docx files.

](/docs/modules/data_connection/document_loaders/integrations/file_loaders/docx)

[

📄️ EPUB files
--------------

This example goes over how to load data from EPUB files. By default, one document will be created for each chapter in the EPUB file, you can change this behavior by setting the splitChapters option to false.

](/docs/modules/data_connection/document_loaders/integrations/file_loaders/epub)

[

📄️ JSON files
--------------

The JSON loader use JSON pointer to target keys in your JSON files you want to target.

](/docs/modules/data_connection/document_loaders/integrations/file_loaders/json)

[

📄️ JSONLines files
-------------------

This example goes over how to load data from JSONLines or JSONL files. The second argument is a JSONPointer to the property to extract from each JSON object in the file. One document will be created for each JSON object in the file.

](/docs/modules/data_connection/document_loaders/integrations/file_loaders/jsonlines)

[

📄️ Notion markdown export
--------------------------

This example goes over how to load data from your Notion pages exported from the notion dashboard.

](/docs/modules/data_connection/document_loaders/integrations/file_loaders/notion_markdown)

[

📄️ PDF files
-------------

This example goes over how to load data from PDF files. By default, one document will be created for each page in the PDF file, you can change this behavior by setting the splitPages option to false.

](/docs/modules/data_connection/document_loaders/integrations/file_loaders/pdf)

[

📄️ Subtitles
-------------

This example goes over how to load data from subtitle files. One document will be created for each subtitles file.

](/docs/modules/data_connection/document_loaders/integrations/file_loaders/subtitles)

[

📄️ Text files
--------------

This example goes over how to load data from text files.

](/docs/modules/data_connection/document_loaders/integrations/file_loaders/text)

[

📄️ Unstructured
----------------

This example covers how to use Unstructured to load files of many types. Unstructured currently supports loading of text files, powerpoints, html, pdfs, images, and more.

](/docs/modules/data_connection/document_loaders/integrations/file_loaders/unstructured)