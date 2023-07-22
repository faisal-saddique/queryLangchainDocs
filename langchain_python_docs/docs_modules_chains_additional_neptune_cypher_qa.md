Neptune Open Cypher QA Chain
============================

This QA chain queries Neptune graph database using openCypher and returns human readable response

    from langchain.graphs.neptune_graph import NeptuneGraphhost = "<neptune-host>"port = 80use_https = Falsegraph = NeptuneGraph(host=host, port=port, use_https=use_https)

    from langchain.chat_models import ChatOpenAIfrom langchain.chains.graph_qa.neptune_cypher import NeptuneOpenCypherQAChainllm = ChatOpenAI(temperature=0, model="gpt-4")chain = NeptuneOpenCypherQAChain.from_llm(llm=llm, graph=graph)chain.run("how many outgoing routes does the Austin airport have?")