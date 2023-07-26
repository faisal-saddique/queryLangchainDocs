Elasticsearch database
======================

Interact with Elasticsearch analytics database via Langchain. This chain builds search queries via the Elasticsearch DSL API (filters and aggregations).

The Elasticsearch client must have permissions for index listing, mapping description and search queries.

See [here](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html) for instructions on how to run Elasticsearch locally.

Make sure to install the Elasticsearch Python client before:

    pip install elasticsearch

    from elasticsearch import Elasticsearchfrom langchain.chains.elasticsearch_database import ElasticsearchDatabaseChainfrom langchain.chat_models import ChatOpenAI

    # Initialize Elasticsearch python client.# See https://elasticsearch-py.readthedocs.io/en/v8.8.2/api.html#elasticsearch.ElasticsearchELASTIC_SEARCH_SERVER = "https://elastic:pass@localhost:9200"db = Elasticsearch(ELASTIC_SEARCH_SERVER)

Uncomment the next cell to initially populate your db.

    # customers = [#     {"firstname": "Jennifer", "lastname": "Walters"},#     {"firstname": "Monica","lastname":"Rambeau"},#     {"firstname": "Carol","lastname":"Danvers"},#     {"firstname": "Wanda","lastname":"Maximoff"},#     {"firstname": "Jennifer","lastname":"Takeda"},# ]# for i, customer in enumerate(customers):#     db.create(index="customers", document=customer, id=i)

    llm = ChatOpenAI(model_name="gpt-4", temperature=0)chain = ElasticsearchDatabaseChain.from_llm(llm=llm, database=db, verbose=True)

    question = "What are the first names of all the customers?"chain.run(question)

                > Entering new ElasticsearchDatabaseChain chain...    What are the first names of all the customers?    ESQuery:{'size': 10, 'query': {'match_all': {}}, '_source': ['firstname']}    ESResult: {'took': 5, 'timed_out': False, '_shards': {'total': 1, 'successful': 1, 'skipped': 0, 'failed': 0}, 'hits': {'total': {'value': 6, 'relation': 'eq'}, 'max_score': 1.0, 'hits': [{'_index': 'customers', '_id': '0', '_score': 1.0, '_source': {'firstname': 'Jennifer'}}, {'_index': 'customers', '_id': '1', '_score': 1.0, '_source': {'firstname': 'Monica'}}, {'_index': 'customers', '_id': '2', '_score': 1.0, '_source': {'firstname': 'Carol'}}, {'_index': 'customers', '_id': '3', '_score': 1.0, '_source': {'firstname': 'Wanda'}}, {'_index': 'customers', '_id': '4', '_score': 1.0, '_source': {'firstname': 'Jennifer'}}, {'_index': 'customers', '_id': 'firstname', '_score': 1.0, '_source': {'firstname': 'Jennifer'}}]}}    Answer:The first names of all the customers are Jennifer, Monica, Carol, Wanda, and Jennifer.    > Finished chain.    'The first names of all the customers are Jennifer, Monica, Carol, Wanda, and Jennifer.'

Custom prompt[](#custom-prompt "Direct link to Custom prompt")
---------------------------------------------------------------

For best results you'll likely need to customize the prompt.

    from langchain.chains.elasticsearch_database.prompts import DEFAULT_DSL_TEMPLATEfrom langchain.prompts.prompt import PromptTemplatePROMPT_TEMPLATE = """Given an input question, create a syntactically correct Elasticsearch query to run. Unless the user specifies in their question a specific number of examples they wish to obtain, always limit your query to at most {top_k} results. You can order the results by a relevant column to return the most interesting examples in the database.Unless told to do not query for all the columns from a specific index, only ask for a the few relevant columns given the question.Pay attention to use only the column names that you can see in the mapping description. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which index. Return the query as valid json.Use the following format:Question: Question hereESQuery: Elasticsearch Query formatted as json"""PROMPT = PromptTemplate.from_template(    PROMPT_TEMPLATE,)chain = ElasticsearchDatabaseChain.from_llm(llm=llm, database=db, query_prompt=PROMPT)

Adding example rows from each index[](#adding-example-rows-from-each-index "Direct link to Adding example rows from each index")
---------------------------------------------------------------------------------------------------------------------------------

Sometimes, the format of the data is not obvious and it is optimal to include a sample of rows from the indices in the prompt to allow the LLM to understand the data before providing a final query. Here we will use this feature to let the LLM know that artists are saved with their full names by providing ten rows from the index.

    chain = ElasticsearchDatabaseChain.from_llm(    llm=ChatOpenAI(temperature=0),    database=db,    sample_documents_in_index_info=2,  # 2 rows from each index will be included in the prompt as sample data)