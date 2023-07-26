Grobid
======

This page covers how to use the Grobid to parse articles for LangChain. It is separated into two parts: installation and running the server

Installation and Setup[](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

#Ensure You have Java installed !apt-get install -y openjdk-11-jdk -q !update-alternatives --set java /usr/lib/jvm/java-11-openjdk-amd64/bin/java

#Clone and install the Grobid Repo import os !git clone [https://github.com/kermitt2/grobid.git](https://github.com/kermitt2/grobid.git) os.environ\["JAVA\_HOME"\] = "/usr/lib/jvm/java-11-openjdk-amd64" os.chdir('grobid') !./gradlew clean install

#Run the server, get\_ipython().system\_raw('nohup ./gradlew run > grobid.log 2>&1 &')

You can now use the GrobidParser to produce documents

    from langchain.document_loaders.parsers import GrobidParserfrom langchain.document_loaders.generic import GenericLoader#Produce chunks from article paragraphsloader = GenericLoader.from_filesystem(    "/Users/31treehaus/Desktop/Papers/",    glob="*",    suffixes=[".pdf"],    parser= GrobidParser(segment_sentences=False))docs = loader.load()#Produce chunks from article sentencesloader = GenericLoader.from_filesystem(    "/Users/31treehaus/Desktop/Papers/",    glob="*",    suffixes=[".pdf"],    parser= GrobidParser(segment_sentences=True))docs = loader.load()

Chunk metadata will include bboxes although these are a bit funky to parse, see [https://grobid.readthedocs.io/en/latest/Coordinates-in-PDF/](https://grobid.readthedocs.io/en/latest/Coordinates-in-PDF/)