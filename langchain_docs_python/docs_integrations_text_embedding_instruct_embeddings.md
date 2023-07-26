InstructEmbeddings
==================

Let's load the HuggingFace instruct Embeddings class.

    from langchain.embeddings import HuggingFaceInstructEmbeddings

    embeddings = HuggingFaceInstructEmbeddings(    query_instruction="Represent the query for retrieval: ")

        load INSTRUCTOR_Transformer    max_seq_length  512

    text = "This is a test document."

    query_result = embeddings.embed_query(text)