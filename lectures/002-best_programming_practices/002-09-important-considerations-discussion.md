# Important Considerations Discussion

Listed here are some of the hard decisions, best practicies, antipatterns, and code smells that
should be considered when a data scientist writes production code.

Data science code is often written a scripts and functions not classes and methods, but many
considerations found in OOP also apply to data science programming, and some will be discused below.

## Review of OOP Principles and how it applies to non-OOP code

## Review of Functional Programming and how it applies to non-OOP code

## Review of SOLID

## Quick review of agreed upon best practices so we can get to the bigger questions:

- No bare exceptions
- Dont mock in tests unless you must
- No magic numbers
- No magic strings
- No nested loops
- No nested conditionals
- No nested comprehensions
- No nested functions
- No nested classes
- No global variables

## How often, if ever, should data scientists use OOP?

<give example of creating a pandas class>

## When should you NOT write unit tests?

## Exceptions vs Errors

## Abstraction vs Repetition - DRY isn't sacrosanct.

## Never Nester - How many levels of nesting is too many?
