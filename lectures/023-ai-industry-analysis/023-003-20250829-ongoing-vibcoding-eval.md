# Ongoing Vibecoding Evaluation

<!-- prettier-ignore-start -->
| Task                                         | Model                    | Prompt                                                                                                                          | Developer | Performance | Notes                                                                                                                                                                                                      | Link |
|----------------------------------------------|--------------------------|---------------------------------------------------------------------------------------------------------------------------------|-----------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|
| Adding CLI arguments to GCP Syntheize TTS    | ChatGPT-o4               |                                                                                                                                 | Me        | Great       | Adding simple arguments works very well (must be millions of examples in the training set)                                                                                                                 |      |
| Top sentence Length Finder                   | ChatGPT-o4               | I need code that takes in text as an argument and then parses between periods and displays the top 10 sentences.                | Me        | Very Good   | The regex didn't parse large spaces well, but was good enough for my use.                                                                                                                                  |      |
| Spacy NLP Code:                              | ChatGPT-o4               | Can you modify the code to create a texcat training loopfor training data which is the merge of train-cases and train_noncases. | Me        | Ok          | All models didn't understand Dagster integration, and some logic removing texcat component                                                                                                                 |      |
| Full tower-defense game                      | Unknown (Cursor)         | Many                                                                                                                            | Primeagen | Ok          | You needed seasoned developers to pull of a mediocre game                                                                                                                                                  |      |
| Generate pdf table->csv code with pdfplumber | ChatGPT-o3 mini (VSCode) | Can you add a cell that takes in a pdf extracts a table and exports it to csv using the python library pdfplumber?              | Me        | Poor        | The AI knew about the `pdf.extract_table()` function so it seems to know the API so it must have the API in its training data, but it doesn't know the data structure so it can't shape the data correctly |      |
| Generate pdf table->csv code with tabula-pv  | ChatGPT-o4               | Can you add a cell that takes in a pdf, extracts a table, and exports it to csv using the python library tabula-pv              | Me        | Poor        |                                                                                                                                                                                                            |      |
| Generate go code to insert wikipedia xml to parquet for neo4j inmport | GPT-4.1 | varied | Me | Very Good | Issues:  did not fill out files when it said it did | |

<!-- prettier-ignore-end -->

## Evaluating use cases

- Generate go code to insert wikipedia xml to parquet for neo4j import
  - Issues:
    - did not create code when it said it did
    - Used older library of parquet-go
      - With this older model didn't know it was closing the file before flushing buffer (had to
        reorder `defer writer.Close()` and `parquet.writeStop()`)
        - and it kept wanting to put back the broken order
        - Also newer version removed adding target node to list, which had to be fixed
