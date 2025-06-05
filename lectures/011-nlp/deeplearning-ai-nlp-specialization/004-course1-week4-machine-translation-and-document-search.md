# Machine Translation and Documentation Search

- [Machine Translation and Documentation Search](#machine-translation-and-documentation-search)
  - [Review from Week 3](#review-from-week-3)
  - [Important tools](#important-tools)
    - [Transforming word vectors](#transforming-word-vectors)
      - [Steps required to learn $R$](#steps-required-to-learn-r)
    - [Hash Function](#hash-function)
      - [Locality Sensitive Hashing](#locality-sensitive-hashing)
  - [Notebook Example](#notebook-example)
    - [Word Embeddings for English and French Words](#word-embeddings-for-english-and-french-words)
      - [`get_matrices`](#get_matrices)
    - [Translations](#translations)
      - [Translation as Linear Transformation of Embeddings](#translation-as-linear-transformation-of-embeddings)
        - [`compute_loss`](#compute_loss)
        - [`compute_gradient`](#compute_gradient)
          - [Early Stopping](#early-stopping)
        - [`align_embeddings()`](#align_embeddings)
      - [Testing the Translation](#testing-the-translation)
        - [k-Nearest Neighbors](#k-nearest-neighbors)
        - [Cosine Similarity](#cosine-similarity)
        - [Distance](#distance)
        - [`nearest_neighbor()`](#nearest_neighbor)
        - [`test_vocabulary()`](#test_vocabulary)
    - [LSH and Document Search](#lsh-and-document-search)
      - [Getting the Document Embeddings](#getting-the-document-embeddings)
        - [`get_document_embedding()`](#get_document_embedding)
        - [`get_document_vecs()`](#get_document_vecs)
      - [Looking up the Tweets](#looking-up-the-tweets)
      - [Finding the most Similar Tweets with LSH](#finding-the-most-similar-tweets-with-lsh)
      - [Getting the Hash Number for a Vector - `hash_value_of_vector()`](#getting-the-hash-number-for-a-vector---hash_value_of_vector)
      - [Creating a hash Table - `make_hash_table()`](#creating-a-hash-table---make_hash_table)
      - [Creating all Hash Tables - `approximate_knn()`](#creating-all-hash-tables---approximate_knn)

## Review from Week 3

<u>**'eigen' from German word for 'own'**</u>

- $Av = \lambda v$
- Eigenvector = vector that doesn't change under linear transformation
- Eigenvalue = scale of the transformation

<u>**Singular Value Decomposition (SVD)**</u>

- Given Matrix $A$ that you will decompose $\color{red} A = U \Sigma V^T $
- Algorithm
  1. Find the eigenvalues of $A^T A$
     - Can be solved via the characteristic equation: $\det(A^T A - \lambda I) = 0$
  1. Find the eigenvectors of $A^T A$, and normalize
     - Get reduced echelon form of $[A - \lambda I | 0]$ by Gaussian elimination or other methods
  1. Form Decomposition $A = U \Sigma V^T$
     - U is the matrix of normalized eigenvectors of $A^T A$, $v_1, v_2, \ldots, v_n$
     - $\Sigma$ is the square root of eigenvalues of $A^T A$ along the diagonal -- these are called
       the <span style="color:yellow">**singular values**</span>
     - $V^T$ is the matrix of eigenvectors of A transformed eigenvectors:
       $A v_1, A v_2, \ldots, A v_n$
- PCA from SVD:
  - The <span style="color:red">**principal components**</span> are the **right singular vectors**
    in the columns of $V^T$ - The <span style="color:yellow">**square of singular values is variance
    explained**</span> Example
    $$
    U \Sigma V^T =
    \begin{bmatrix}
    -0.3333 & 0.6667 & 0.6667 \\
    -0.6667 & 0.3333 & -0.6667 \\
    -0.6667 & -0.6667 & 0.3333
    \end{bmatrix}
    \color{yellow}
    \begin{bmatrix}
    6\sqrt{10} & 0 & 0 \\
    0 & 3\sqrt{10} & 0 \\
    0 & 0 & 0
    \end{bmatrix}
    \color{red}
    \begin{bmatrix}
    -0.3333 & -0.6667 & -0.6667 \\
    0.6667 & 0.3333 & -0.6667 \\
    0.6667 & -0.6667 & 0.3333
    \end{bmatrix}
    $$

<u>**PCA from Covariance Matrix**</u>

- Input: Data matrix X (m × n) with m samples and n features
- Output: Reduced <span style="color:red">**principle components**</span> data matrix, X' (m × k),
  where k ≤ n, and <span style="color:yellow">**engenvalues of the covariance matrix describing
  variance explained**</span>
- Algorithm:

  1. Center the data: $$X_{\text{centered}} = X - \text{mean}(X)$$
  1. Compute the Covariance Matrix: $$ Cov(X) = \frac{1}{m-1} X^T X $$
  1. Compute the eigenvectors and eigenvalues of the covariance matrix: $$ Cv = \lambda v $$
  1. Select the top k principal components: - Sort the eigenvalues in descending order - Select the
     first $k$ columns of $V^T$: $V_k = V^T[0..k]$
  1. Transform the data: - Project the data onto the new basis:

     ${\color{red} \textbf X'} = X_{\text{centered}} × {\color{yellow} \textbf V_k^T}$

<u>**PCA Notebook Summary**</u>

- Vector Math and Cosine Similarity
  - The previous talk on 'Vector Space Models' used word embeddings and cosine similarity to find a
    country of a capital city based on the vector relations between cities and countries.
    $$v_{\text{country2}} = v_{\text{country1}} -  v_{\text{capital1}} + v_{\text{capital2}}$$
  - For example: $$v_{\text{country2}} = v_{\text{Athens}} -  v_{\text{Greece}} + v_{\text{Cario}}$$
  - The cosine similarity is calculated between this calculated vector and all other vectors to find
    the unknown country vector. In the example above, the vector with the smallest cosine similarity
    should be the vector for Egypt.
- PCA dimensionality reduction to visualize embeddings
  - Using algorithm above, reduce the demsionality of 300 down to 2
  - Plot these 2 dimensions to visualize the embeddings. Even these 2 dimensions (which explain the
    most variance) can group similar words.

---

## Important tools

### Transforming word vectors

Word vectors can be transformed from one space to another. For example, if we have word vectors in
English and we want to transform them to French, we can use a transformation matrix $R$ to do this.

#### Steps required to learn $R$

![Transforming Word Vectors](images/transforming_word_vectors.png)

<!-- prettier-ignore-start -->

1. Initilize $R$
1. For loop
   - Calculate **Frobenius norm** for Loss
     - $ \text{Loss} = \|XR - Y \|_F$
     - $ g = \frac{d}{dR}\text{Loss}$
     - $ R = R - \alpha \star g$

<!-- prettier-ignore-end -->

Example how Frobenious norm is calculated:

$$
A = \begin{bmatrix}
2 & 2 \\
2 & 2
\end{bmatrix}
$$

<!-- prettier-ignore-start -->

$$ \|A\|_F = \sqrt{2^2 + 2^2 + 2^2 + 2^2} = \sqrt{16} = 4 $$

$$
\|A\|_F = \sqrt{\sum_{i=1}^m
\sum*{j=1}^n |a*{ij}|^2} = \sqrt{a*{11}^2 + a*{12}^2 + a*{21}^2 + a*{22}^2}
$$

<!-- prettier-ignore-end -->

### Hash Function

A hash function is any function that can be used to map data of arbitrary size to fixed-size values.
The values returned by a hash function are called hash values.

We see hash functions used in many applications, including:

- password encryption/storage
- data integrity verification
- digital signatures

MD5, SHA-1, and SHA-256 are all examples of hash functions.

```bash
$ echo -n "hello world" | md5sum
5eb63bbbe01eeed093cb22bb8f5acdc3
```

```bash
$ echo -n "hello world" | sha1sum
2aae6c35c94fcfb415dbe95f408b9ce91ee846ed
```

```bash
$ echo -n "hello world" | sha256sum
a591a6d40bf420404a011733cfb7b190d62c65bf0bcda190f2c91f8b3c4e9e91
```

In linux the password is hashed using `yescrypt` Key Derivation Function (KDF) and stored in the
`/etc/shadow` file. The `yescrypt` KDF is a memory-hard function that is designed to be slow and
difficult to compute, making it more resistant to brute-force attacks. You can reproduce the hash
found in the `/etc/shadow` file by running the following command:

```bash
# /etc/shadow format starts $6$SALT$HASH:LAST_CHANGE:MIN:MAX:WARN:INACTIVE:EXPIRED:LOGIN_COUNT:AGE
# see man https://www.cyberciti.biz/faq/understanding-etcshadow-file/
$ openssl passwd -6 -salt <salt found in /etc/pass for user> <user's password>
```

For security purposes, hash functions can be made to be hard to compute so slow down brute-force
attacks from high-performance computers. However, outside the security domain, hash lookups are
$O(1)$, can be accessed in constant time.

Python dictionaries are an example of a hash table.

```python
# Hash table
hash_table = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}
```

Regardless of the size of the hash table, the time complexity for searching for a key is $O(1)$.
This is because the key itself defines the location in memory and no sorting or searching is
required.

#### Locality Sensitive Hashing

Sometimes we want to hash values but for values to have relationships so that hash values will group
similar values together. This is called locality sensitive hashing (LSH). This would be dangerous in
the security domain where we don't want any information of the password to be determined by the
algorithm, but for lookups, LSH is a useful technique.

![Locality Sensitive Hashing](images/locality_sensitive_hashing_intro.png "Locality Sensitive Hashing")

![Multiple Planes](images/multiple-planes.png "Multiple Planes")

## Notebook Example

### Word Embeddings for English and French Words

#### `get_matrices`

- Given word embeddings and English to French dictionary create an embedding matrix `get_matrices`
  where English and French embedding matrices (of shape (num_words, embedding_size)) where each row
  in the English matrix corresponds to the the same row in the French matrix.
  - It appears that embeddings come from word2vec (Gensim)

### Translations

Summary: If we have a transformation across word embeddings, $R$, from English to French, we can
transform compute any word embedding, $e$, to get a new embedding $eR = f$. We can then lookup the
closest vector to this transformation and that should be the translation.

Steps:

1. Assemble embedding matrices from embedding vectors and known dictionary (`get_matrices`)
1. Find transformation $R$ by iterative updating - `align_embeddings()`:
   1. Calculate the loss (the Frobenius norm) of the Transformation matrix - `compute_loss()`
   1. Calculate the gradient of the loss - `compute_gradient()`
   1. Update, $R$ and repeat

#### Translation as Linear Transformation of Embeddings

We first need to find R by minimizing R for our training data which compares our transformed English
embedding with the corresponding French embedding.

##### `compute_loss`

- Finding the transformation matrix involves finding an R that minimizes the norm of the difference
  between the transformed English embedding and the French embedding.

$$\arg \min _{\mathbf{R}}\| \mathbf{X R} - \mathbf{Y}\|_{F}\tag{1} $$

Here we use the Frobenius norm:

$$\|\mathbf{A}\|_{F} \equiv \sqrt{\sum_{i=1}^{m} \sum_{j=1}^{n}\left|a_{i j}\right|^{2}}\tag{2}$$

In practice, the square of the Frobenius norm is used to make it easier to compute the gradient, and
we divide by the number of words, $m$ to get the average loss over the examples because loss can
increase with dictionary size.

$$\frac{1}{m} \| \mathbf{X R} - \mathbf{Y} \|_{F}^{2}$$

##### `compute_gradient`

To minimize the elements of R, we calculate the gradient of the loss and perform Gradient Descent.
The derivative is:

$$\frac{d}{dR}𝐿(𝑋,𝑌,𝑅)=\frac{d}{dR}\Big(\frac{1}{m}\| X R -Y\|_{F}^{2}\Big) = \frac{2}{m}X^{T} (X R - Y)$$

We optimize $R$ by iteratively updating values in the direction of the gradient

$$ R*{new} = R*{old} - \alpha g $$

Where $\alpha$ is the learning rate, and g is the gradient of the loss.

<div style="background-color: rgb(87, 61, 61);">

<font color="red">**To Remember Forever**</font>

###### Early Stopping

Early stopping is a technique used to prevent overfitting in machine learning models. It involves
monitoring the model's performance on a validation set during training and stopping the training
process when the performance starts to degrade.

- Why not always do 'early stopping'? The dataset may have noise in validation set leading to
  premature stopping or it may stop too soon. Use early stopping as a solution to overfitting, not
  as a default.
- An alternative is to train with a fixed number of iterations.

</div>

##### `align_embeddings()`

The sorted embedding matrices (French and English) are used to update the transformation matrix,
$R$, by `compute_loss`, `compute_gradient` and updating the transformation matrix.

#### Testing the Translation

##### k-Nearest Neighbors

This is not the common k-NN algorithm used in classification, but is a vector search for the closest
vector using cosine similarity.

The transformation of the English word to French, $eR = f$, often wont give the **exact**
corresponding French vector, however the vector should be close to the real translation. By finding
the nearest vector we can find the proper translation.

##### Cosine Similarity

$$\cos(u,v)=\frac{u\cdot v}{\left\|u\right\|\left\|v\right\|}$$

- $\cos(u,v)$ = $1$ when $u$ and $v$ lie on the same line and have the same direction.
- $\cos(u,v)$ is $-1$ when they have exactly opposite directions.
- $\cos(u,v)$ is $0$ when the vectors are orthogonal (perpendicular) to each other.

##### Distance

- We can obtain distance metric from cosine similarity, but the cosine similarity can't be used
  directly as the distance metric.
- When the cosine similarity increases (towards $1$), the "distance" between the two vectors
  decreases (towards $0$).
- We can define the cosine distance between $u$ and $v$ as

$$d_{\text{cos}}(u,v)=1-\cos(u,v)$$

##### `nearest_neighbor()`

- Again, this is not the common k-NN algorithm used in classification, but is a vector search for
  the closest vector using cosine similarity.
- We calculate the cosine similarity for a set of candidate vectors and select the closest.

##### `test_vocabulary()`

- This function predicts a French translation for all English words using `nearest_neighbor()` and
  calculates the accuracy.

### LSH and Document Search

#### Getting the Document Embeddings

- We can create a document embedding by summing up the embeddings of all words in the document.
- **Bag-of-Words**: This is a common technique where we treat the document as a set of words and
  ignore the order of the words. The document embedding is simply the sum of the embeddings of all
  words in the document.
- By summing up the embeddings in this way we are creating a Bag-of-Words representation of the
  document.

##### `get_document_embedding()`

- We get the document embedding by summing up the embeddings of all words in the document.

##### `get_document_vecs()`

- This function gets the document embeddings for a set of documents.

#### Looking up the Tweets

- Given a new tweet we can compare it to all other tweets using the cosine similarity to find the
  most similar tweets.

#### Finding the most Similar Tweets with LSH

- Searching a large set of documents for the most similar document scales as $O(n)$, which is not
  efficient. By using locality sensitive hashing (LSH) the location of a document (vector) is
  defined by its content, and similar documents will be hashed to the same location.
- In this case, we can split up a document space with random planes. The dot product of the normal
  to the plan with a given vector says which side the plane vector lies.

#### Getting the Hash Number for a Vector - `hash_value_of_vector()`

- We compute which side the vector (tweet embedding in this case), vectorially, by taking the doct
  product of this vector with the matrix of all planes.

- Not unlike counting in other bases, we can define a unique number which specifies the location of
  the vector in the document space.
- In our case we raise two to the power of the index of the plane and sum these values to get a
  unique number for the vector.

$$hash = \sum_{i=0}^{N-1} \left( 2^{i} \times h_{i} \right)$$

- here $i$ is the vector index and $2^{i}$ is the power of two for the index. This sum will always
  produce a unique number for a given vector.

#### Creating a hash Table - `make_hash_table()`

- In order to do speedy lookups, we need to create a hash table to store the vectors.
- We create $2 \times \text{num\_planes}$ hash tables, one for each side of the plane.
- Each hash table is a dictionary where the key is the hash value and the value is a list of vectors
  (tweets) that have that hash value.
- The hash value is computed using `hash_value_of_vector()` and the vectors are stored in the hash
  table/dictionary.

#### Creating all Hash Tables - `approximate_knn()`

- This is the full function. It creates multiple hash tables (universes) that can speed up
  comparisions at the cost of tables/universe-creation.
