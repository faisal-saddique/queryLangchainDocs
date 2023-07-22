Split code and markup
=====================

CodeTextSplitter allows you to split your code and markup with support for multiple languages.

LangChain supports a variety of different markup and programming language-specific text splitters to split your text based on language-specific syntax. This results in more semantically self-contained chunks that are more useful to a vector store or other retriever. Popular languages like JavaScript, Python, Solidity, and Rust are supported as well as Latex, HTML, and Markdown.

Usage[​](#usage "Direct link to Usage")
---------------------------------------

Initialize a standard `RecursiveCharacterTextSplitter` with the `fromLanguage` factory method. Below are some examples for various languages.

JavaScript[​](#javascript "Direct link to JavaScript")
------------------------------------------------------

    import {  SupportedTextSplitterLanguages,  RecursiveCharacterTextSplitter,} from "langchain/text_splitter";console.log(SupportedTextSplitterLanguages); // Array of supported languages/*  [    'cpp',      'go',    'java',     'js',    'php',      'proto',    'python',   'rst',    'ruby',     'rust',    'scala',    'swift',    'markdown', 'latex',    'html'  ]*/const jsCode = `function helloWorld() {  console.log("Hello, World!");}// Call the functionhelloWorld();`;const splitter = RecursiveCharacterTextSplitter.fromLanguage("js", {  chunkSize: 32,  chunkOverlap: 0,});const jsOutput = await splitter.createDocuments([jsCode]);console.log(jsOutput);/*  [    Document {      pageContent: 'function helloWorld() {',      metadata: { loc: [Object] }    },    Document {      pageContent: 'console.log("Hello, World!");',      metadata: { loc: [Object] }    },    Document {      pageContent: '}\n// Call the function',      metadata: { loc: [Object] }    },    Document {      pageContent: 'helloWorld();',      metadata: { loc: [Object] }    }  ]*/

#### API Reference:

*   [SupportedTextSplitterLanguages](/docs/api/text_splitter/variables/SupportedTextSplitterLanguages) from `langchain/text_splitter`
*   [RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter) from `langchain/text_splitter`

Python[​](#python "Direct link to Python")
------------------------------------------

    import { RecursiveCharacterTextSplitter } from "langchain/text_splitter";const pythonCode = `def hello_world():  print("Hello, World!")# Call the functionhello_world()`;const splitter = RecursiveCharacterTextSplitter.fromLanguage("python", {  chunkSize: 32,  chunkOverlap: 0,});const pythonOutput = await splitter.createDocuments([pythonCode]);console.log(pythonOutput);/*  [    Document {      pageContent: 'def hello_world():',      metadata: { loc: [Object] }    },    Document {      pageContent: 'print("Hello, World!")',      metadata: { loc: [Object] }    },    Document {      pageContent: '# Call the function',      metadata: { loc: [Object] }    },    Document {      pageContent: 'hello_world()',      metadata: { loc: [Object] }    }  ]*/

#### API Reference:

*   [RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter) from `langchain/text_splitter`

HTML[​](#html "Direct link to HTML")
------------------------------------

    import { RecursiveCharacterTextSplitter } from "langchain/text_splitter";const text = `<!DOCTYPE html><html>  <head>    <title>🦜️🔗 LangChain</title>    <style>      body {        font-family: Arial, sans-serif;      }      h1 {        color: darkblue;      }    </style>  </head>  <body>    <div>      <h1>🦜️🔗 LangChain</h1>      <p>⚡ Building applications with LLMs through composability ⚡</p>    </div>    <div>      As an open source project in a rapidly developing field, we are extremely open to contributions.    </div>  </body></html>`;const splitter = RecursiveCharacterTextSplitter.fromLanguage("html", {  chunkSize: 175,  chunkOverlap: 20,});const output = await splitter.createDocuments([text]);console.log(output);/*  [    Document {      pageContent: '<!DOCTYPE html>\n<html>',      metadata: { loc: [Object] }    },    Document {      pageContent: '<head>\n    <title>🦜️🔗 LangChain</title>',      metadata: { loc: [Object] }    },    Document {      pageContent: '<style>\n' +        '      body {\n' +        '        font-family: Arial, sans-serif;\n' +        '      }\n' +        '      h1 {\n' +        '        color: darkblue;\n' +        '      }\n' +        '    </style>\n' +        '  </head>',      metadata: { loc: [Object] }    },    Document {      pageContent: '<body>\n' +        '    <div>\n' +        '      <h1>🦜️🔗 LangChain</h1>\n' +        '      <p>⚡ Building applications with LLMs through composability ⚡</p>\n' +        '    </div>',      metadata: { loc: [Object] }    },    Document {      pageContent: '<div>\n' +        '      As an open source project in a rapidly developing field, we are extremely open to contributions.\n' +        '    </div>\n' +        '  </body>\n' +        '</html>',      metadata: { loc: [Object] }    }  ]*/

#### API Reference:

*   [RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter) from `langchain/text_splitter`

Latex[​](#latex "Direct link to Latex")
---------------------------------------

    import { RecursiveCharacterTextSplitter } from "langchain/text_splitter";const text = `\\begin{document}\\title{🦜️🔗 LangChain}⚡ Building applications with LLMs through composability ⚡\\section{Quick Install}\\begin{verbatim}Hopefully this code block isn't splityarn add langchain\\end{verbatim}As an open source project in a rapidly developing field, we are extremely open to contributions.\\end{document}`;const splitter = RecursiveCharacterTextSplitter.fromLanguage("latex", {  chunkSize: 100,  chunkOverlap: 0,});const output = await splitter.createDocuments([text]);console.log(output);/*  [    Document {      pageContent: '\\begin{document}\n' +        '\\title{🦜️🔗 LangChain}\n' +        '⚡ Building applications with LLMs through composability ⚡',      metadata: { loc: [Object] }    },    Document {      pageContent: '\\section{Quick Install}',      metadata: { loc: [Object] }    },    Document {      pageContent: '\\begin{verbatim}\n' +        "Hopefully this code block isn't split\n" +        'yarn add langchain\n' +        '\\end{verbatim}',      metadata: { loc: [Object] }    },    Document {      pageContent: 'As an open source project in a rapidly developing field, we are extremely open to contributions.',      metadata: { loc: [Object] }    },    Document {      pageContent: '\\end{document}',      metadata: { loc: [Object] }    }  ]*/

#### API Reference:

*   [RecursiveCharacterTextSplitter](/docs/api/text_splitter/classes/RecursiveCharacterTextSplitter) from `langchain/text_splitter`