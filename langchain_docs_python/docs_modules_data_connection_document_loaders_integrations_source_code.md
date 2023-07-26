Source Code
===========

This notebook covers how to load source code files using a special approach with language parsing: each top-level function and class in the code is loaded into separate documents. Any remaining code top-level code outside the already loaded functions and classes will be loaded into a seperate document.

This approach can potentially improve the accuracy of QA models over source code. Currently, the supported languages for code parsing are Python and JavaScript. The language used for parsing can be configured, along with the minimum number of lines required to activate the splitting based on syntax.

    pip install esprima

    import warningswarnings.filterwarnings("ignore")from pprint import pprintfrom langchain.text_splitter import Languagefrom langchain.document_loaders.generic import GenericLoaderfrom langchain.document_loaders.parsers import LanguageParser

    loader = GenericLoader.from_filesystem(    "./example_data/source_code",    glob="*",    suffixes=[".py", ".js"],    parser=LanguageParser(),)docs = loader.load()

    len(docs)

        6

    for document in docs:    pprint(document.metadata)

        {'content_type': 'functions_classes',     'language': <Language.PYTHON: 'python'>,     'source': 'example_data/source_code/example.py'}    {'content_type': 'functions_classes',     'language': <Language.PYTHON: 'python'>,     'source': 'example_data/source_code/example.py'}    {'content_type': 'simplified_code',     'language': <Language.PYTHON: 'python'>,     'source': 'example_data/source_code/example.py'}    {'content_type': 'functions_classes',     'language': <Language.JS: 'js'>,     'source': 'example_data/source_code/example.js'}    {'content_type': 'functions_classes',     'language': <Language.JS: 'js'>,     'source': 'example_data/source_code/example.js'}    {'content_type': 'simplified_code',     'language': <Language.JS: 'js'>,     'source': 'example_data/source_code/example.js'}

    print("\n\n--8<--\n\n".join([document.page_content for document in docs]))

        class MyClass:        def __init__(self, name):            self.name = name            def greet(self):            print(f"Hello, {self.name}!")        --8<--        def main():        name = input("Enter your name: ")        obj = MyClass(name)        obj.greet()        --8<--        # Code for: class MyClass:            # Code for: def main():            if __name__ == "__main__":        main()        --8<--        class MyClass {      constructor(name) {        this.name = name;      }          greet() {        console.log(`Hello, ${this.name}!`);      }    }        --8<--        function main() {      const name = prompt("Enter your name:");      const obj = new MyClass(name);      obj.greet();    }        --8<--        // Code for: class MyClass {        // Code for: function main() {        main();

The parser can be disabled for small files.

The parameter `parser_threshold` indicates the minimum number of lines that the source code file must have to be segmented using the parser.

    loader = GenericLoader.from_filesystem(    "./example_data/source_code",    glob="*",    suffixes=[".py"],    parser=LanguageParser(language=Language.PYTHON, parser_threshold=1000),)docs = loader.load()

    len(docs)

        1

    print(docs[0].page_content)

        class MyClass:        def __init__(self, name):            self.name = name            def greet(self):            print(f"Hello, {self.name}!")            def main():        name = input("Enter your name: ")        obj = MyClass(name)        obj.greet()            if __name__ == "__main__":        main()    

Splitting[](#splitting "Direct link to Splitting")
---------------------------------------------------

Additional splitting could be needed for those functions, classes, or scripts that are too big.

    loader = GenericLoader.from_filesystem(    "./example_data/source_code",    glob="*",    suffixes=[".js"],    parser=LanguageParser(language=Language.JS),)docs = loader.load()

    from langchain.text_splitter import (    RecursiveCharacterTextSplitter,    Language,)

    js_splitter = RecursiveCharacterTextSplitter.from_language(    language=Language.JS, chunk_size=60, chunk_overlap=0)

    result = js_splitter.split_documents(docs)

    len(result)

        7

    print("\n\n--8<--\n\n".join([document.page_content for document in result]))

        class MyClass {      constructor(name) {        this.name = name;        --8<--        }        --8<--        greet() {        console.log(`Hello, ${this.name}!`);      }    }        --8<--        function main() {      const name = prompt("Enter your name:");        --8<--        const obj = new MyClass(name);      obj.greet();    }        --8<--        // Code for: class MyClass {        // Code for: function main() {        --8<--        main();