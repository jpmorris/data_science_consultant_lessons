## II. Supervised Learning

Supervised learning is learning from labeled examples. It has two main branches: **Classification**
and **Regression**.

---

### A. Classification (Discrete Targets)

#### 1. k-Nearest Neighbors (kNN)

- **Idea**: Classify a point based on the majority label among its closest neighbors.
- **Distance Metrics**: Euclidean, Manhattan, cosine similarity.
- **Strengths**: Simple, intuitive, no training phase.
- **Weaknesses**: Computationally expensive on large datasets, sensitive to irrelevant features.
- **Applications**: Dating site recommendation, handwriting recognition.

#### 2. Decision Trees (ID3, C4.5, CART)

- **Core Mechanism**: Recursive splitting of features based on information gain (entropy reduction).
- **Advantages**: Easy to interpret, can handle categorical + numerical data.
- **Challenges**: Overfitting (mitigated with pruning).
- **Applications**: Predicting contact lens prescriptions.
- **Variants**:
  - C4.5 → classification trees.
  - CART → works for both regression and classification.

#### 3. Naïve Bayes

- **Theory**: Bayesian decision rule with assumption of feature independence.
- **Formula**: \( P(Class|Features) ∝ P(Features|Class) \* P(Class) \).
- **Strengths**: Simple, efficient, good for text data.
- **Weaknesses**: Strong independence assumption often unrealistic.
- **Applications**: Spam filtering, sentiment analysis, document classification.

#### 4. Logistic Regression

- **Concept**: Uses a sigmoid function to model probability of a class.
- **Optimization**: Parameters found via gradient ascent or stochastic gradient ascent.
- **Interpretability**: Coefficients indicate feature importance.
- **Applications**: Medical data (e.g., horse colic mortality prediction).

#### 5. Support Vector Machines (SVMs)

- **Principle**: Maximize the margin between decision boundary and closest data points (support
  vectors).
- **Extensions**:
  - Kernels (RBF, polynomial, linear) → allow non-linear classification.
  - SMO algorithm → efficient optimization.
- **Strengths**: Effective in high dimensions, strong theoretical foundation.
- **Applications**: Handwriting recognition, bioinformatics classification.

#### 6. Ensemble Methods – AdaBoost

- **Concept**: Combine many weak learners (e.g., decision stumps) into a strong classifier.
- **Mechanism**: Reweight misclassified examples in successive rounds.
- **Advantages**: High accuracy, works well with simple base classifiers.
- **Limitations**: Sensitive to noisy data, outliers.
- **Applications**: Face detection, difficult imbalanced classification problems.

---

### B. Regression (Continuous Targets)

#### 1. Linear Regression

- **Goal**: Fit a line (or hyperplane) that minimizes squared error.
- **Evaluation**: Correlation coefficient between predicted and actual values.
- **Limitation**: Fails with multicollinearity or non-linear interactions.

#### 2. Locally Weighted Linear Regression (LWLR)

- **Idea**: Fit local models around each query point using weighted data.
- **Benefit**: Captures local nonlinearities.
- **Drawback**: Computationally expensive.

#### 3. Shrinkage Methods

- **Ridge Regression**: Adds penalty term (\(\lambda \sum \beta^2\)) to shrink coefficients.
- **Lasso Regression**: Penalty forces some coefficients to zero (feature selection).
- **Forward Stagewise Regression**: Greedy approximation to Lasso.
- **Bias–Variance Tradeoff**: Shrinkage introduces bias but reduces variance.

#### 4. Tree-Based Regression (CART)

- **Process**: Split dataset recursively into regions, fit simple models in each.
- **Features**:
  - Prepruning and Postpruning to reduce overfitting.
  - Model Trees: regression equations in leaves.
- **Applications**: Housing prices, stock forecasting, nonlinear phenomena.

---

## III. Unsupervised Learning

### 1. Clustering

- **k-Means Clustering**
  - Iterative assignment to nearest centroid, recompute centroids.
  - Bisecting k-means: recursively split clusters.
  - Applications: geographic clustering, image segmentation.
- **Other Algorithms**:
  - Hierarchical clustering, DBSCAN, OPTICS.

### 2. Association Rule Mining

- **Apriori Algorithm**
  - Uses Apriori principle: all subsets of a frequent itemset must be frequent.
  - Finds frequent itemsets → generates rules.
  - Application: Market basket analysis (“diapers → beer”).
- **FP-Growth Algorithm**
  - More efficient: compress dataset into FP-trees.
  - Applications: Mining Twitter word co-occurrence, web clickstreams.

### 3. Density Estimation

- **Expectation Maximization (EM)**, Gaussian Mixture Models.
- **Parzen Windows** for non-parametric density estimation.
- Applications: anomaly detection, clustering, probability modeling.

---

## IV. Dimensionality Reduction and Feature Learning

### 1. Principal Component Analysis (PCA)

- **Concept**: Rotate coordinate axes to align with directions of maximum variance.
- **Benefits**:
  - Reduces noise, simplifies data.
  - Makes visualization feasible.
- **Applications**: Semiconductor manufacturing analysis, data compression.

### 2. Singular Value Decomposition (SVD)

- **Mathematical Tool**: Factorizes data into orthogonal matrices.
- **Applications**:
  - Latent Semantic Indexing (text mining).
  - Collaborative filtering (recommendation engines).
  - Image compression.
- **Strengths**: Extracts latent factors, handles sparse data well.

### 3. Other Classical Methods

- **Factor Analysis**: Models data as a combination of latent variables + noise.
- **Independent Component Analysis (ICA)**: Extracts statistically independent signals (e.g.,
  separating audio sources).

---

## V. Feature Engineering and Feature Selection

### 1. Feature Engineering (Creating New Features)

- **Why Important**:
  - Algorithms are only as good as the features provided.
  - Example: raw text must be converted into word vectors before classification.
- **Techniques**:
  - **Data Transformation**: normalization, log transforms.
  - **Encoding Categorical Variables**: one-hot, frequency encoding.
  - **Text Features**: bag-of-words, TF-IDF, n-grams.
  - **Image Features (Classical)**: pixel intensities, HOG, SIFT.
  - **Polynomial & Interaction Features**: capture nonlinearities.
  - **Domain-Specific**: finance (volatility), biology (gene motifs).
- **Automated Feature Engineering**: feature crosses, feature hashing, representation learning.

### 2. Feature Selection (Choosing the Best Features)

- **Why Important**:
  - Reduces overfitting, speeds training, simplifies interpretation.
- **Categories of Methods**:
  1. **Filter Methods** (statistical tests: correlation, chi-squared, mutual info).
  2. **Wrapper Methods** (Forward Selection, Backward Elimination, RFE).
  3. **Embedded Methods** (built into models: Lasso, decision trees, random forests).
- **Examples**:
  - Naïve Bayes spam filtering drops rare words.
  - Lasso forces coefficients to zero (embedded feature selection).
  - Decision trees rank features by importance.

### 3. Relationship with Dimensionality Reduction

- **Feature Engineering** = add _better_ features.
- **Feature Selection** = remove _worse_ features.
- **Dimensionality Reduction** = compress into _fewer_ features.
- Together they form the **preprocessing pipeline** that determines model success.

---

## VI. Practical Tools and Scaling

### 1. Big Data & Distributed Learning

- **MapReduce** (Hadoop, AWS EMR).
- **mrjob** in Python for parallel jobs.
- **Pegasos Algorithm**: scalable SVM training.

### 2. Model Evaluation & Metrics

- **Classification**: accuracy, precision, recall, F1-score, ROC curves.
- **Regression**: correlation coefficient, MSE, RMSE.
- **Cross-validation**: robust evaluation.

### 3. Real-World Data Challenges

- Missing values: imputation, removal.
- Class imbalance: oversampling, undersampling, cost-sensitive learning.
- Feature engineering and normalization.

---

# ✅ Final Summary

Classical Machine Learning includes:

- **Supervised Learning**: classification (kNN, trees, Naïve Bayes, logistic regression, SVM,
  ensembles) and regression (linear, shrinkage, CART).
- **Unsupervised Learning**: clustering (k-means), association rules (Apriori, FP-growth), density
  estimation.
- **Dimensionality Reduction**: PCA, SVD, ICA, factor analysis.
- **Feature Engineering & Selection**: critical preprocessing steps that improve accuracy and
  efficiency.
- **Practical Tools**: MapReduce, Pegasos, cross-validation, preprocessing pipelines.

The **data pipeline** can be summarized:  
**Raw Data → Feature Engineering → Feature Selection/Dimensionality Reduction → Model Training →
Evaluation → Deployment.**
