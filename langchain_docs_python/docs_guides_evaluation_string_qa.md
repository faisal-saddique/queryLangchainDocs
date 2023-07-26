QA Correctness
==============

When thinking about a QA system, one of the most important questions to ask is whether the final generated result is correct. The `"qa"` evaluator compares a question-answering model's response to a reference answer to provide this level of information. If you are able to annotate a test dataset, this evaluator will be useful.

For more details, check out the reference docs for the [QAEvalChain](https://api.python.langchain.com/en/latest/evaluation/langchain.evaluation.qa.eval_chain.QAEvalChain.html#langchain.evaluation.qa.eval_chain.QAEvalChain)'s class definition.

    from langchain.chat_models import ChatOpenAIfrom langchain.evaluation import load_evaluatorllm = ChatOpenAI(model="gpt-4", temperature=0)# Note: the eval_llm is optional. A gpt-4 model will be provided by default if not specifiedevaluator = load_evaluator("qa", eval_llm=llm)

    evaluator.evaluate_strings(    input="What's last quarter's sales numbers?",    prediction="Last quarter we sold 600,000 total units of product.",    reference="Last quarter we sold 100,000 units of product A, 210,000 units of product B, and 300,000 units of product C.",)

        {'reasoning': None, 'value': 'CORRECT', 'score': 1}

SQL Correctness[](#sql-correctness "Direct link to SQL Correctness")
---------------------------------------------------------------------

You can use an LLM to check the equivalence of a SQL query against a reference SQL query using the sql prompt.

    from langchain.evaluation.qa.eval_prompt import SQL_PROMPTeval_chain = load_evaluator("qa", eval_llm=llm, prompt=SQL_PROMPT)

    eval_chain.evaluate_strings(    input="What's last quarter's sales numbers?",    prediction="""SELECT SUM(sale_amount) AS last_quarter_salesFROM salesWHERE sale_date >= DATEADD(quarter, -1, GETDATE()) AND sale_date < GETDATE();""",    reference="""SELECT SUM(sub.sale_amount) AS last_quarter_salesFROM (    SELECT sale_amount    FROM sales    WHERE sale_date >= DATEADD(quarter, -1, GETDATE()) AND sale_date < GETDATE()) AS sub;""",)

        {'reasoning': 'The expert answer and the submission are very similar in their structure and logic. Both queries are trying to calculate the sum of sales amounts for the last quarter. They both use the SUM function to add up the sale_amount from the sales table. They also both use the same WHERE clause to filter the sales data to only include sales from the last quarter. The WHERE clause uses the DATEADD function to subtract 1 quarter from the current date (GETDATE()) and only includes sales where the sale_date is greater than or equal to this date and less than the current date.\n\nThe main difference between the two queries is that the expert answer uses a subquery to first select the sale_amount from the sales table with the appropriate date filter, and then sums these amounts in the outer query. The submission, on the other hand, does not use a subquery and instead sums the sale_amount directly in the main query with the same date filter.\n\nHowever, this difference does not affect the result of the query. Both queries will return the same result, which is the sum of the sales amounts for the last quarter.\n\nCORRECT',     'value': 'CORRECT',     'score': 1}

Using Context[](#using-context "Direct link to Using Context")
---------------------------------------------------------------

Sometimes, reference labels aren't all available, but you have additional knowledge as context from a retrieval system. Often there may be additional information that isn't available to the model you want to evaluate. For this type of scenario, you can use the [ContextQAEvalChain](https://api.python.langchain.com/en/latest/evaluation/langchain.evaluation.qa.eval_chain.ContextQAEvalChain.html#langchain.evaluation.qa.eval_chain.ContextQAEvalChain).

    eval_chain = load_evaluator("context_qa", eval_llm=llm)eval_chain.evaluate_strings(    input="Who won the NFC championship game in 2023?",    prediction="Eagles",    reference="NFC Championship Game 2023: Philadelphia Eagles 31, San Francisco 49ers 7",)

        {'reasoning': None, 'value': 'CORRECT', 'score': 1}

CoT With Context[](#cot-with-context "Direct link to CoT With Context")
------------------------------------------------------------------------

The same prompt strategies such as chain of thought can be used to make the evaluation results more reliable. The [CotQAEvalChain's](https://api.python.langchain.com/en/latest/evaluation/langchain.evaluation.qa.eval_chain.CotQAEvalChain.html#langchain.evaluation.qa.eval_chain.CotQAEvalChain) default prompt instructs the model to do this.

    eval_chain = load_evaluator("cot_qa", eval_llm=llm)eval_chain.evaluate_strings(    input="Who won the NFC championship game in 2023?",    prediction="Eagles",    reference="NFC Championship Game 2023: Philadelphia Eagles 31, San Francisco 49ers 7",)

        {'reasoning': 'The student\'s answer is "Eagles". The context states that the Philadelphia Eagles won the NFC championship game in 2023. Therefore, the student\'s answer matches the information provided in the context.',     'value': 'GRADE: CORRECT',     'score': 1}