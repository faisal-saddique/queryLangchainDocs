Grobid
======

GROBID is a machine learning library for extracting, parsing, and re-structuring raw documents.

It is particularly good for sturctured PDFs, like academic papers.

This loader uses GROBIB to parse PDFs into `Documents` that retain metadata associated with the section of text.

* * *

For users on `Mac` -

(Note: additional instructions can be found [here](https://python.langchain.com/docs/ecosystem/integrations/grobid.mdx).)

Install Java (Apple Silicon):

    $ arch -arm64 brew install openjdk@11$ brew --prefix openjdk@11/opt/homebrew/opt/openjdk@ 11

In `~/.zshrc`:

    export JAVA_HOME=/opt/homebrew/opt/openjdk@11export PATH=$JAVA_HOME/bin:$PATH

Then, in Terminal:

    $ source ~/.zshrc

Confirm install:

    $ which java/opt/homebrew/opt/openjdk@11/bin/java$ java -version openjdk version "11.0.19" 2023-04-18OpenJDK Runtime Environment Homebrew (build 11.0.19+0)OpenJDK 64-Bit Server VM Homebrew (build 11.0.19+0, mixed mode)

Then, get [Grobid](https://grobid.readthedocs.io/en/latest/Install-Grobid/#getting-grobid):

    $ curl -LO https://github.com/kermitt2/grobid/archive/0.7.3.zip$ unzip 0.7.3.zip

Build

    $ ./gradlew clean install

Then, run the server:

    get_ipython().system_raw('nohup ./gradlew run > grobid.log 2>&1 &')

Now, we can use the data loader.

    from langchain.document_loaders.parsers import GrobidParserfrom langchain.document_loaders.generic import GenericLoader

    loader = GenericLoader.from_filesystem(    "../Papers/",    glob="*",    suffixes=[".pdf"],    parser=GrobidParser(segment_sentences=False),)docs = loader.load()

    docs[3].page_content

        'Unlike Chinchilla, PaLM, or GPT-3, we only use publicly available data, making our work compatible with open-sourcing, while most existing models rely on data which is either not publicly available or undocumented (e.g."Books -2TB" or "Social media conversations").There exist some exceptions, notably OPT (Zhang et al., 2022), GPT-NeoX (Black et al., 2022), BLOOM (Scao et al., 2022) and GLM (Zeng et al., 2022), but none that are competitive with PaLM-62B or Chinchilla.'

    docs[3].metadata

        {'text': 'Unlike Chinchilla, PaLM, or GPT-3, we only use publicly available data, making our work compatible with open-sourcing, while most existing models rely on data which is either not publicly available or undocumented (e.g."Books -2TB" or "Social media conversations").There exist some exceptions, notably OPT (Zhang et al., 2022), GPT-NeoX (Black et al., 2022), BLOOM (Scao et al., 2022) and GLM (Zeng et al., 2022), but none that are competitive with PaLM-62B or Chinchilla.',     'para': '2',     'bboxes': "[[{'page': '1', 'x': '317.05', 'y': '509.17', 'h': '207.73', 'w': '9.46'}, {'page': '1', 'x': '306.14', 'y': '522.72', 'h': '220.08', 'w': '9.46'}, {'page': '1', 'x': '306.14', 'y': '536.27', 'h': '218.27', 'w': '9.46'}, {'page': '1', 'x': '306.14', 'y': '549.82', 'h': '218.65', 'w': '9.46'}, {'page': '1', 'x': '306.14', 'y': '563.37', 'h': '136.98', 'w': '9.46'}], [{'page': '1', 'x': '446.49', 'y': '563.37', 'h': '78.11', 'w': '9.46'}, {'page': '1', 'x': '304.69', 'y': '576.92', 'h': '138.32', 'w': '9.46'}], [{'page': '1', 'x': '447.75', 'y': '576.92', 'h': '76.66', 'w': '9.46'}, {'page': '1', 'x': '306.14', 'y': '590.47', 'h': '219.63', 'w': '9.46'}, {'page': '1', 'x': '306.14', 'y': '604.02', 'h': '218.27', 'w': '9.46'}, {'page': '1', 'x': '306.14', 'y': '617.56', 'h': '218.27', 'w': '9.46'}, {'page': '1', 'x': '306.14', 'y': '631.11', 'h': '220.18', 'w': '9.46'}]]",     'pages': "('1', '1')",     'section_title': 'Introduction',     'section_number': '1',     'paper_title': 'LLaMA: Open and Efficient Foundation Language Models',     'file_path': '/Users/31treehaus/Desktop/Papers/2302.13971.pdf'}