Split by character
==================

This is the simplest method. This splits based on characters (by default "\\n\\n") and measure chunk length by number of characters.

1.  How the text is split: by single character
2.  How the chunk size is measured: by number of characters

CharacterTextSplitter
=====================

Besides the `RecursiveCharacterTextSplitter`, there is also the more standard `CharacterTextSplitter`. This splits only on one type of character (defaults to `"\n\n"`). You can use it in the exact same way.

    import { Document } from "langchain/document";import { CharacterTextSplitter } from "langchain/text_splitter";const text = "foo bar baz 123";const splitter = new CharacterTextSplitter({  separator: " ",  chunkSize: 7,  chunkOverlap: 3,});const output = await splitter.createDocuments([text]);