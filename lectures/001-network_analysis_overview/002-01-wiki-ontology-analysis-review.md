# Wiki Ontology Analysis Review

Review: we would like to get all relevant terms that are related to machine learning to see an
interesting overview of what arcane topics/techniques we may want to know about ( e.g SMOTE,
Winzorize, AdaBoost.M1, Personal PageRank, FastRP etc)

- Problem: we have so many unrelated nodes (names etc)
- My first solution: Just do NER over these and filter out names, dates etc
- My second solution: get glossary of terms (strip them from glossary of machine learning books) and
  establish neighborhood based on connectedness between these terms
- ChatGPT's ideas:
  - Had about 11 of them, and I learned a lot
    - I had to use my experience to pick the best one
  - Landed on three:
    - Semantic Similarity
    - Personalized PageRank
    - Community Detection with Leiden/Louvain

## Personalize PageRank

### Reminder: PageRank
- Algorithm:
  - Start with a uniform probability distribution over all nodes.
  - Perform random walks on the graph, with a probability of returning to the starting node at each
    step.
  - After many iter
ations, nodes that are frequently visited during these random walks will have
    higher PageRank scores.
  - Rank nodes based on their PageRank scores to identify the most important nodes in the graph.



### Personalized PageRank
- Algorithm:
  - Start with a set of seed nodes (e.g., known machine learning terms).
  - Initialize a probability distribution where the seed nodes have higher probabilities.
  - Perform random walks on the graph, with a probability of returning to the seed nodes at each step.
  - After many iterations, nodes that are frequently visited during these random walks will have
    higher PageRank scores.
  - Rank nodes based on their PageRank scores to identify those most relevant to the seed terms.

## FastRP
- Algorithm:
  - Initialize random vectors for each node in the graph.
  - Perform a series of matrix multiplications and non-linear transformations to propagate
    information through the graph.
  - After several iterations, the resulting vectors capture the structural properties of the graph.
  - Use these vectors as embeddings for downstream tasks like node classification or clustering.

## Louvain/Leiden Community Detection
- Algorithm:
  - Start with each node in its own community.
  - For each node, evaluate the gain in modularity by moving it to the community of each neighbor.
  - Move the node to the community that yields the highest modularity gain (if positive).
  - Repeat until no further modularity improvements can be made.
  - Aggregate nodes in the same community into a single node and repeat the process on the new graph.
- Important concept: Modularity
  - A measure of the strength of division of a network into communities.
  - High modularity indicates dense connections within communities and sparse connections between them.