# structured data query languages
There are several types of query lanugages that can be used to parse, slice, query, and reformat XML, HTML, JSON, etc.
- For example:
    - XPath - to query XML
    - XQuery - to query XML
    - JSONPath - for JSON
      - related: `jq` from command line
    - SPARQL - for RDF
- Usually an interface to between this query language and most programming languages like python
- This can be an alternative to manual parsing in a python script though the `json` library using keys and values
- It can often be used indpendent of python or a programming language
- The queries can be more compact
- When to use over `json` library? Best to try both and see which is more readable and maintainable