# THIS IS A FORK OF THE CODE USED IN THE COURSE WHICH CAN BE FOUND AT 
https://github.com/amanchadha/coursera-natural-language-processing-specialization/tree/master


# Natural Language Processing Specialization on Coursera (offered by deeplearning.ai)

Programming assignments from all courses in the Coursera [Natural Language Processing Specialization](https://www.coursera.org/specializations/natural-language-processing) offered by `deeplearning.ai`.

## Credits

This repo contains my work for this specialization. The code base, quiz questions and diagrams are taken from the [Natural Language Processing Specialization](https://www.coursera.org/specializations/natural-language-processing), unless specified otherwise.

## Courses

The [Natural Language Processing Specialization](https://www.coursera.org/specializations/natural-language-processing) on Coursera contains four courses:

- Course 1: [Natural Language Processing with Classification and Vector Spaces](https://www.coursera.org/learn/classification-vector-spaces-in-nlp)
- Course 2: [Natural Language Processing with Probabilistic Models](https://www.coursera.org/learn/probabilistic-models-in-nlp)
- Course 3: [Natural Language Processing with Sequence Models](https://www.coursera.org/learn/sequence-models-in-nlp)
- Course 4: [Natural Language Processing with Attention Models](https://www.coursera.org/learn/attention-models-in-nlp)

## Specialization Info

- Natural Language Processing (NLP) uses algorithms to understand and manipulate human language. This technology is one of the most broadly applied areas of machine learning. As AI continues to expand, so will the demand for professionals skilled at building models that analyze speech and language, uncover contextual patterns, and produce insights from text and audio.

- By the end of this specialization, you will be ready to design NLP applications that perform question-answering and sentiment analysis, create tools to translate languages and summarize text, and even build chatbots. These and other NLP applications are going to be at the forefront of the coming transformation to an AI-powered future.

- This Specialization is designed and taught by two experts in NLP, machine learning, and deep learning. Younes Bensouda Mourri is an Instructor of AI at Stanford University who also helped build the Deep Learning Specialization. Łukasz Kaiser is a Staff Research Scientist at Google Brain and the co-author of Tensorflow, the Tensor2Tensor and Trax libraries, and the Transformer paper.

## Topics Covered

*This Specialization will equip you with the state-of-the-art deep learning techniques needed to build cutting-edge NLP systems:*

- Use logistic regression, naïve Bayes, and word vectors to implement sentiment analysis, complete analogies, and translate words, and use locality sensitive hashing for approximate nearest neighbors.

- Use dynamic programming, hidden Markov models, and word embeddings to autocorrect misspelled words, autocomplete partial sentences, and identify part-of-speech tags for words.

- Use dense and recurrent neural networks, LSTMs, GRUs, and Siamese networks in TensorFlow and Trax to perform advanced sentiment analysis, text generation, named entity recognition, and to identify duplicate questions.

- Use encoder-decoder, causal, and self-attention to perform advanced machine translation of complete sentences, text summarization, question-answering and to build chatbots. Models covered include T5, BERT, transformer, reformer, and more!
Enjoy!

## Programming Assignments

### Course 1: Natural Language Processing with Classification and Vector Spaces

  - **Week 1**
    - Assignment: 
      - [Sentiment Analysis with Logistic Regression](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/1%20-%20Natural%20Language%20Processing%20with%20Classification%20and%20Vector%20Spaces/Week%201/C1W1_A1_Logistic%20Regression.ipynb)
    - Labs: 
      - [Natural language Preprocessing](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/1%20-%20Natural%20Language%20Processing%20with%20Classification%20and%20Vector%20Spaces/Week%201/C1W1_L1_Natural%20language%20preprocessing.ipynb)
      - [Visualizing word frequencies](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/1%20-%20Natural%20Language%20Processing%20with%20Classification%20and%20Vector%20Spaces/Week%201/C1W1_L2_Visualizing%20word%20frequencies.ipynb)
      - [Visualizing tweets and Logistic Regression models](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/1%20-%20Natural%20Language%20Processing%20with%20Classification%20and%20Vector%20Spaces/Week%201/C1W1_L3_Visualizing%20tweets%20and%20Logistic%20Regression%20models.ipynb)
  - **Week 2**
    - Assignment:
      - [Naive Bayes](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/1%20-%20Natural%20Language%20Processing%20with%20Classification%20and%20Vector%20Spaces/Week%202/C1W2_A1_Naive%20Bayes.ipynb)
    - Labs:
      - [Visualizing likelihoods and confidence ellipses](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/1%20-%20Natural%20Language%20Processing%20with%20Classification%20and%20Vector%20Spaces/Week%202/C1W2_L1_Visualizing%20likelihoods%20and%20confidence%20ellipses.ipynb)
  - **Week 3**
    - Assignment:
      - [Word Embeddings: Hello Vectors](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/1%20-%20Natural%20Language%20Processing%20with%20Classification%20and%20Vector%20Spaces/Week%203/C1W3_A1_Word%20Embeddings.ipynb)
    - Labs:
      - [Linear algebra in Python with Numpy](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/1%20-%20Natural%20Language%20Processing%20with%20Classification%20and%20Vector%20Spaces/Week%203/C1W3_L1_Linear%20algebra%20in%20Python%20with%20Numpy.ipynb)
      - [Manipulating word embeddings](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/1%20-%20Natural%20Language%20Processing%20with%20Classification%20and%20Vector%20Spaces/Week%203/C1W3_L2_Manipulating%20word%20embeddings.ipynb)
      - [Another explanation about PCA](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/1%20-%20Natural%20Language%20Processing%20with%20Classification%20and%20Vector%20Spaces/Week%203/C1W3_L3_Another%20explanation%20about%20PCA.ipynb)                
  - **Week 4**
    - Assignment:
      - [Word Translation](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/1%20-%20Natural%20Language%20Processing%20with%20Classification%20and%20Vector%20Spaces/Week%204/C1W4_A1_Word%20Translation.ipynb)
    - Labs: 
      - [Rotation matrices in R2](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/1%20-%20Natural%20Language%20Processing%20with%20Classification%20and%20Vector%20Spaces/Week%204/C1W4_L1_Rotation%20matrices%20in%20R2.ipynb)
      - [Hash tables](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/1%20-%20Natural%20Language%20Processing%20with%20Classification%20and%20Vector%20Spaces/Week%204/C1W4_L2_Hash%20tables.ipynb)

### Course 2: Natural Language Processing with Probabilistic Models

  - **Week 1**
    - Assignment:
      - [Autocorrect](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/2%20-%20Natural%20Language%20Processing%20with%20Probabilistic%20Models/Week%201/C2W1_A1_Autocorrect.ipynb)
    - Labs: 
      - [Building the vocabulary](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/2%20-%20Natural%20Language%20Processing%20with%20Probabilistic%20Models/Week%201/C2W1_L1_Building%20the%20vocabulary.ipynb)
      - [Candidates from edits](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/2%20-%20Natural%20Language%20Processing%20with%20Probabilistic%20Models/Week%201/C2W1_L2_Candidates%20from%20edits.ipynb)
  - **Week 2**
    - Assignment:
      - [Part of Speech Tagging](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/2%20-%20Natural%20Language%20Processing%20with%20Probabilistic%20Models/Week%202/C2W2_A1_Part%20of%20Speech%20Tagging.ipynb)
    - Labs: 
      - [Working with text data](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/2%20-%20Natural%20Language%20Processing%20with%20Probabilistic%20Models/Week%202/C2W2_L1_Working%20with%20text%20data.ipynb)
      - [Working with tags and NumPy](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/2%20-%20Natural%20Language%20Processing%20with%20Probabilistic%20Models/Week%202/C2W2_L2_Working%20with%20tags%20and%20Numpy.ipynb)
  - **Week 3**
    - Assignment:
      - [Autocomplete](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/2%20-%20Natural%20Language%20Processing%20with%20Probabilistic%20Models/Week%203/C2W3_A1_Autocomplete.ipynb)
    - Labs: 
      - [Corpus preprocessing for N-grams](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/2%20-%20Natural%20Language%20Processing%20with%20Probabilistic%20Models/Week%203/C2W3_L1_Corpus%20preprocessing%20for%20N-grams.ipynb)
      - [Building the language model](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/2%20-%20Natural%20Language%20Processing%20with%20Probabilistic%20Models/Week%203/C2W3_L2_Building%20the%20language%20model.ipynb)
      - [Language model generalization](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/2%20-%20Natural%20Language%20Processing%20with%20Probabilistic%20Models/Week%203/C2W3_L3_Language%20model%20generalization.ipynb)                
  - **Week 4**
    - Assignment:
      - [Word Embeddings](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/2%20-%20Natural%20Language%20Processing%20with%20Probabilistic%20Models/Week%204/C2W4_A1_Word%20Embeddings.ipynb)
    - Labs: 
      - [Data Preparation](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/2%20-%20Natural%20Language%20Processing%20with%20Probabilistic%20Models/Week%204/C2W4_L1_Data%20Preparation.ipynb)
      - [Intro to CBOW model](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/2%20-%20Natural%20Language%20Processing%20with%20Probabilistic%20Models/Week%204/C2W4_L2_Intro%20to%20CBOW%20model.ipynb)             
      - [Training the CBOW model](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/2%20-%20Natural%20Language%20Processing%20with%20Probabilistic%20Models/Week%204/C2W4_L3_Training%20the%20CBOW%20model.ipynb)
      - [Word Embeddings](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/2%20-%20Natural%20Language%20Processing%20with%20Probabilistic%20Models/Week%204/C2W4_L4_Word%20Embeddings.ipynb)
      - [Word Embeddings Step by Step](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/2%20-%20Natural%20Language%20Processing%20with%20Probabilistic%20Models/Week%204/C2W4_L5_Word%20Embeddings%20Step%20by%20Step.ipynb)

### Course 3: Natural Language Processing with Sequence Models

  - **Week 1**
    - Assignment:
      - [Sentiment with Deep Neural Networks](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/3%20-%20Natural%20Language%20Processing%20with%20Sequence%20Models/Week%201/C3W1_A1_Sentiment%20with%20Deep%20Neural%20Networks.ipynb)
    - Labs:
      - [Introduction to Trax](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/3%20-%20Natural%20Language%20Processing%20with%20Sequence%20Models/Week%201/C3W1_L1_Introduction%20to%20Trax.ipynb)
      - [Classes and Subclasses](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/3%20-%20Natural%20Language%20Processing%20with%20Sequence%20Models/Week%201/C3W1_L2_Classes%20and%20Subclasses.ipynb)
      - [Data Generators](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/3%20-%20Natural%20Language%20Processing%20with%20Sequence%20Models/Week%201/C3W1_L3_Data%20Generators.ipynb)
  - **Week 2**
    - Assignment:
      - [Deep N-grams](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/3%20-%20Natural%20Language%20Processing%20with%20Sequence%20Models/Week%202/C3W2_A1_Deep%20N-grams.ipynb)
    - Labs: 
      - [Hidden State Activation](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/3%20-%20Natural%20Language%20Processing%20with%20Sequence%20Models/Week%202/C3W2_L1_Hidden_State_Activation.ipynb)
      - [Working with JAX NumPy and Calculating Perplexity](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/3%20-%20Natural%20Language%20Processing%20with%20Sequence%20Models/Week%202/C3W2_L2_Working%20with%20JAX%20NumPy%20and%20Calculating%20Perplexity.ipynb)
      - [Vanilla RNNs, GRUs and the scan function](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/3%20-%20Natural%20Language%20Processing%20with%20Sequence%20Models/Week%202/C3W2_L3_Vanilla%20RNNs%2C%20GRUs%20and%20the%20scan%20function.ipynb)
      - [Creating a GRU model using Trax](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/3%20-%20Natural%20Language%20Processing%20with%20Sequence%20Models/Week%202/C3W2_L4_Creating%20a%20GRU%20model%20using%20Trax.ipynb)
  - **Week 3**
    - Assignment:
      - [Named Entity Recognition (NER)](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/3%20-%20Natural%20Language%20Processing%20with%20Sequence%20Models/Week%203/C3W3_A1_Named%20Entity%20Recognition.ipynb)
    - Labs: 
      - [Vanishing Gradients](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/3%20-%20Natural%20Language%20Processing%20with%20Sequence%20Models/Week%203/C3W3_L1_Vanishing%20Gradients.ipynb)
  - **Week 4**
    - Assignment:
      - [Question duplicates](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/3%20-%20Natural%20Language%20Processing%20with%20Sequence%20Models/Week%204/C3W4_A1_Question%20duplicates.ipynb)
    - Labs:
      - [Creating a Siamese Model using Trax](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/3%20-%20Natural%20Language%20Processing%20with%20Sequence%20Models/Week%204/C3W4_L1_Creating%20a%20Siamese%20Model%20using%20Trax.ipynb)
      - [Modified Triplet Loss](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/3%20-%20Natural%20Language%20Processing%20with%20Sequence%20Models/Week%204/C3W4_L2_Modified%20Triplet%20Loss.ipynb)             
      - [Evaluate a Siamese Model](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/3%20-%20Natural%20Language%20Processing%20with%20Sequence%20Models/Week%204/C3W4_L3_Evaluate%20a%20Siamese%20Model.ipynb)             

### Course 4: Natural Language Processing with Attention Models

  - **Week 1**
    - Assignment:
      - [NMT with Attention](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/4%20-%20Natural%20Language%20Processing%20with%20Attention%20Models/Week%201/C4W1_A1_NMT_with_Attention.ipynb)
    - Labs:
      - [Stack Semantics](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/4%20-%20Natural%20Language%20Processing%20with%20Attention%20Models/Week%201/C4W1_L1_Ungraded_Lab_Stack_Semantics.ipynb)
      - [BLEU Score](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/4%20-%20Natural%20Language%20Processing%20with%20Attention%20Models/Week%201/C4W1_L2_Ungraded_Lab_Bleu_Score)
  - **Week 2**
    - Assignment:
      - [Transformer Summarizer](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/4%20-%20Natural%20Language%20Processing%20with%20Attention%20Models/Week%202/C4W2_A1_Transformer_Summarizer.ipynb)
    - Labs: 
      - [Attention](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/4%20-%20Natural%20Language%20Processing%20with%20Attention%20Models/Week%202/C4W2_L1_Attention.ipynb)
      - [The Transformer Decoder](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/4%20-%20Natural%20Language%20Processing%20with%20Attention%20Models/Week%202/C4W2_L2_Transformer_Decoder.ipynb)
  - **Week 3**
    - Assignment:
      - [Question Answering](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/4%20-%20Natural%20Language%20Processing%20with%20Attention%20Models/Week%203/C4W3_A1_Question_Answering.ipynb)
    - Labs: 
      - [SentencePiece and BPE](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/4%20-%20Natural%20Language%20Processing%20with%20Attention%20Models/Week%203/C4W3_L1_SentencePiece_and_BPE.ipynb)
      - [BERT Loss](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/4%20-%20Natural%20Language%20Processing%20with%20Attention%20Models/Week%203/C4W3_L2_BERT_Loss.ipynb)
      - [T5](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/4%20-%20Natural%20Language%20Processing%20with%20Attention%20Models/Week%203/C4W3_L3_T5.ipynb)      
  - **Week 4**
    - Assignment:
      - [Chatbot](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/4%20-%20Natural%20Language%20Processing%20with%20Attention%20Models/Week%204/C4W4_A1_Chatbot.ipynb)
    - Labs:
      - [Reformer LSH](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/4%20-%20Natural%20Language%20Processing%20with%20Attention%20Models/Week%204/C4W4_L1_Ungraded_Lab_Reformer_LSH.ipynb)
      - [Revnet](https://nbviewer.jupyter.org/github/amanchadha/coursera-natural-language-processing-specialization/blob/master/4%20-%20Natural%20Language%20Processing%20with%20Attention%20Models/Week%204/C4W4_L2_Ungraded_Lab_Revnet.ipynb)
      
## Disclaimer

I recognize the hard time people spend on building intuition, understanding new concepts and debugging assignments. The solutions uploaded here are **only for reference**. They are meant to unblock you if you get stuck somewhere. Please do not copy any part of the code as-is (the programming assignments are fairly easy if you read the instructions carefully). Similarly, try out the quizzes yourself before you refer to the quiz solutions.
