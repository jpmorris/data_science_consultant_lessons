# 2025 Themes:

- LLM From Scratch
- NLP 4-course specialization
- Cloud level solution and architecture 
  - Guest Lectures: Chris A, Vickey
- Classical ML Deep Dive
- AI Industry/Tools

# Today's Agenda:

- METR stduy
- NLP - Machine Translation and Document Search


# Near-term/Ongoing Theme Talks:

- Signal Attenuation and quasi-time series anomaly detection
  - When Chris and Chuck are ready
- LLM From Scratch
  - Add as needed: CGAP Attention Model
- NLP Course
  - Add as needed: TFIDF, NMF (CGAP unsupervised topics)
- MCP: Model Context Protocol
- Vibecoding tools review (as part of project building)

# Continuous learning Chat (these should always go int repo too):

- which metrics are robust to class imbalance? Why is f1 score robust to class imbalance?
- generator comprehension
- Go through the skills guide

# Challenge Problems

- Chris' Problem - Bootstrapping LLM
- Chucks problem

# Project Related Talks

- Project learning requirements:
  - Go
  - JavaScript/Typescript
  - Programming
    - Data Structures
    - Algorithms
      - Review of Most Common
      - Sample of some LeetCode Design Patterns for Python for Scripting/Data Science
  - Platform Choice and Tech Stacks, and Tools
  - System Design courses
    - Microservices
    - Scalable Applications
    - Backend Development and Design
- Comparative Programming (Review of Languages required)

# Possible AWS Cert information:

- Solutions Architect - Associate
- Solutions Architect - Professional
- Data Engineer
- Machine Learning Engineer
- Machine Learning Specialty - expires Jan 31 2026
- Developer
- Cloud Practitioner - Optional
- AI Practitioner - Optional

# Next Agendas Ideas

- Linux from scratch
- Simulation: and review of Car Destination Challenge Problem
- Deep Learning course for more low-level
- Advanced Classical ML - theory, automl, model improvement, phenomenology
- After LLM from scratch:
  - review of Deepseek and other open source code
- Taylor as guest speaker for programming questions (need a GOOD list of programming questions,
  after projects and programming review
- Chris A as guest speaker for cloud design
  - Need to review LZA and Data Platform design
- Review each part of pipeline along the way:
  - NMF - unsupervised clustering
  - Attention model - line labeler
- Review of Canonical Papers (after project)

# Eventual:

- Go through flan tasks
- Git
  - trunked based development vs gitflow (and how it relates to (our) data science repo)
- pythonic
- Seconary IDE Primer - wait until Chuck has VSCode again

# Comparative programming

The goal here is to get a good overview of a bunch of relevant programming languages, take notes,
and decide if there is important comparative points.

Since we are surveying many langauges, we need short dense courses.

C C++ C# Objective-C JavaScript TypeScript Java Kotlin Swift SQL Rust Scala R Julia Haskell Ruby
Perl PHP Lua Prolog Lisp Scheme Smalltalk Erlang Elixir Clojure Groovy Fortran Groovy Cobol Ada
Pascal

<!-- prettier-ignore-start -->
| Language   | Course                                                      | Hours | Link                                                                         |
|------------|-------------------------------------------------------------|-------|------------------------------------------------------------------------------|
| Go         | Go - The Complete Guide                                     | 15    | https://www.udemy.com/course/go-the-complete-guide                           |
| Javascript | The Complete Gavascript Course 2025: From Zero to Expert!   | 71    | https://www.udemy.com/course/the-complete-javascript-course/                 |
| Typescript | | | |
| C          | C Programming for Beginners                                 | 25    | https://www.udemy.com/course/c-programming-for-beginners-/                   |
| C++        | Beginning C++ Programming - From Beginner to Beyond         | 46    | https://www.udemy.com/course/beginning-c-plus-plus-programming               |
| Haskell    | The Complete Haskell Course: From Zero to Expert            | 24    | https://www.udemy.com/course/the-complete-haskell-course-from-zero-to-expert |
| Scala      | Complete Scala 3 Development Masterclass                    | 20    | https://www.udemy.com/course/completescala3/                                 |
| Java       | 60 Days of Java: The Complete Java masterclass              | 58    | https://www.udemy.com/course/javamasterclass/                                |
| Rust       | Learn to Code with Rust                                     | 58    | https://www.udemy.com/course/learn-to-code-with-rust/                        |
| Kotlin     | The Complete Android 14 & Kotlin Development Masterclass    | 66    | https://www.udemy.com/course/android-kotlin-developer                        |
| Prolog     | The Complete Prolog Programming Course: From Zero to Expert | 15    | https://www.udemy.com/course/learn-prolog-programming-from-zero-to-hero/     |
| C#         | Complete C# Masterclass                                     | 46    | https://www.udemy.com/course/complete-csharp-masterclass/                    |
| R          | | | |
| Julia      | || |

<!-- prettier-ignore-end -->

- 444 total hours
- 148 If you 3x it.
- 120 If you skip intro content and what you're already familiar with.
- If you dedicate 2.5 hours a week to this, you can get through it in about 50 weeks. This is a
  year-long course if you take it slow.

## List of programming best-practices to cover -- Brainstorming for eventual content

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

- review of computing mathematics/discrete math (check the shaums book)
- more best practices:
  - Never nesters
  - Do not wrap everything in try/catch
  - No bare except
  -
- CI/CD
- AutoML
- Computer Vision (after frigate experments)
- review of sci-kit API
- ML Theory
- git primer
- python SYSPATH/PYTHONPATH/module imports
- complex problem solving strategies
- showcase personal projects
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

- Review APIs fully
- SQL Primer Will review soon
- Git Primer
- Bash/GNU Primer need project relevance
- other distributions, need project relevance also confidence limits
- review of all stat tests also CONOVA etc, need good examples database review cleaning +
  transformation + selection review of pandas/numpy/scikit API data normalization, imputation, etc
  part of database review unstructured data data security awareness algorithm comparision automl
  feature selection review review of metrics math for data science algorithm comparision review of
  unsupervised learning review of NLP review of Deep Learning review of AWS services data pipelining
  Mlops model monitoring high-performance computing hadoop et al big data review (esp platforms
  agile review?
