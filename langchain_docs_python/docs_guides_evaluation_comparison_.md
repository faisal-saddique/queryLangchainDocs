Comparison Evaluators
=====================

[

📄️ Custom Pairwise Evaluator
-----------------------------

You can make your own pairwise string evaluators by inheriting from PairwiseStringEvaluator class and overwriting the evaluatestringpairs method (and the aevaluatestringpairs method if you want to use the evaluator asynchronously).

](/docs/guides/evaluation/comparison/custom)

[

📄️ Pairwise Embedding Distance
-------------------------------

One way to measure the similarity (or dissimilarity) between two predictions on a shared or similar input is to embed the predictions and compute a vector distance between the two embeddings.\[1\]

](/docs/guides/evaluation/comparison/pairwise_embedding_distance)

[

📄️ Pairwise String Comparison
------------------------------

Often you will want to compare predictions of an LLM, Chain, or Agent for a given input. The StringComparison evaluators facilitate this so you can answer questions like:

](/docs/guides/evaluation/comparison/pairwise_string)