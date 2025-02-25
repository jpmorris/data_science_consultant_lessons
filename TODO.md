# Continuous learning Chat (these should always go int repo too):

- generator comprehension
- Go through the skills guide

# Next Agendas:

- NLP continuous
- Review of all hackathon projects and the inherent LLM architectures and methods
  - Now only two more questions
- Simulation and review of Challenge Problem
- Chris' paper
- LLM from scratch
- Play around with DeepSeek

- Model review: Go through the Text analytics training pipeline
- Taylor as guest speaker for programming questions
- Chris A as guest speaker for cloud design
- Record of State in Pipeline Design

- Review of Learnings from recent code reviews:
  - using kwargs
  - review of line labeler refactoring
  - review of augmentor refactoring

# near term:

- go through flan tasks
- trunked based development vs gitflow (and how it relates to (our) data science repo)
- generating data:

  - own model
  - python packages
  - CTGAN
  - LLMs
  - compare outputs?

- pythonic

## List of programming best-practices to cover

- logging without polluting app code
- do not execute at import-time - keep your module-level globals clean of executable code
  - avoid execution code at global-level
  - sqlalchemy persistent engine vs singleton vs factory vs. creating a new engine every time
- variable naming: code SHOULD READ
- error handling
  - Python vs other languages on using exceptions for flow control
  - EAFP vs LBYL:
    https://softwareengineering.stackexchange.com/questions/298795/should-exceptions-be-raised-higher-up-or-lower-down-or-both
- if you abstract PLEASE EXPOSE ALL EXISTING FUNCTIONALITY
  - do not hide functionality
  - e.g. dynamic dags inability to pass in arguments
- OOP vs Functional Programming vs programming with functions
  - Show examples in the different paradigms
  - Should a data scientist ever do MyDataframe(pd.DataFrame) or anything like that? I there ever a
    time for a data scientist to use OOP?
- Do you pass in the most raw form of data to a function or do you pass in the most processed form
  of data to a function? E.g. you need to transform a np.array(list[dict]) do you past the list and
  transform in the function or do you transform before you pass into the function. Example: see
  spacy example labeled_spacy_files.py in dagster code
- how to rewrite function to support: 2 separate functions, function flag, two independent functions
  or modify data storage (see: labeled_spacy_files comparision with unlabeled)

# RNN, LSTM, Transformers compared (should be part of deep learning lesson?)

- contextualize with deep learning basics
- show the code
- where is the attention?
- can we find the original transformer code?
  - `github.com/tensorflow/tensor2tesnor`

# List to cover

- Good programming practices
- Pythonic tricks
- SQL primer
- GenAI
- NLP

- review of computing mathematics/discrete math (check the shaums book)
- more best practices:
  - Never nesters
  - Do not wrap everything in try/catch
  - No bare except
  -
- CI/CD
- AutoML
- Computer Vision
- IDE Primer
- review of sci-kit API
- order of algorithmic complexity (show sql example timings)
- ML Theory
- Data Structures
- Design Patterns
- git primer
- cli/gnu tools primer
- python SYSPATH/PYTHONPATH/module imports
- complex problem solving strategies
- showcase personal projects
- high-performance computing
  - algorithm optimization (use graph query as example)
- review of confusion matrix - how to memorize forever
- information theory and the informational limit of datasets

# Later

- functional programming
- dynamic programming

# Things to be aware of:

- all computers have keyrings
  - using an example to get the password from the keyring and login to aws:
    - https://stackoverflow.com/questions/14756352/how-is-python-keyring-implemented-on-windows

# from melissas spreadhseet

Review APIs fully SQL Primer Will review soon Git Primer Bash/GNU Primer need project relevance
other distributions, need project relevance also confidence limits review of all stat tests also
CONOVA etc, need good examples database review cleaning + transformation + selection review of
pandas/numpy/scikit API data normalization, imputation, etc part of database review unstructured
data data security awareness algorithm comparision automl feature selection review review of metrics
math for data science algorithm comparision review of unsupervised learning review of NLP review of
Deep Learning review of AWS services data pipelining Mlops model monitoring high-performance
computing hadoop et al big data review (esp platforms agile review?
