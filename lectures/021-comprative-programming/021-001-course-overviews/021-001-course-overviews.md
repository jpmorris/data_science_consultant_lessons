# Comparative programming - course overviews

The purpose of this section is to complete a broad, quick survey of several programming courses to
understand broad concepts in different languages. This section will be structured by concept rather
than by language with each language described under each concept.

## Highest-level topics in programming

- Language Specific
  - Syntax
  - Data types/Data Structures
  - Control structures
  - Functions
  - Classes
  - Libraries
  - Frameworks
  - Tools
  - Best practices
  - Testing
  - Debugging
  - Performance
  - Concurrency
- Non-Language Specific
  - Program Design and Architecture
    - Design patterns
  - Data Structures
  - Algorithms
  - Performance

## Origins

<!-- prettier-ignore-start -->
| Language | Year Released | Creator          |
|----------|---------------|------------------|
| Python   | 1991          | Guido van Rossum |
| Go       | 2009          | Google           |
<!--
| C           | 1972          | Dennis Ritchie                                                     |
| C++         | 1985          | Bjarne Stroustrup                                                  |
| C#          | 2000          | Microsoft                                                          |
| Objective-C | 1984          | Brad Cox                                                           |
| JavaScript  | 1995          | Brendan Eich                                                       |
| TypeScript  | 2012          | Microsoft                                                          |
| Java        | 1995          | Sun Microsystems                                                   |
| Kotlin      | 2011          | JetBrains                                                          |
| Swift       | 2014          | Apple                                                              |
| SQL         | 1974          | IBM                                                                |
| Rust        | 2010          | Mozilla                                                            |
| Scala       | 2003          | Martin Odersky                                                     |
| R           | 1993          | Ross Ihaka, Robert Gentleman                                       |
| Julia       | 2012          | Jeff Bezanson, Stefan Karpinski, Viral B. Shah, Alan Edelman       |
| Haskell     | 1990          | Simon Peyton Jones, Philip Wadler                                  |
| Ruby        | 1995          | Yukihiro Matsumoto                                                 |
| Perl        | 1987          | Larry Wall                                                         |
| PHP         | 1995          | Rasmus Lerdorf                                                     |
| Lua         | 1993          | Roberto Ierusalimschy, Waldemar Celes, Luiz Henrique de Figueiredo |
| Prolog      | 1972          | Alain Colmerauer, Robert Kowalski                                  |
| Lisp        | 1958          | John McCarthy                                                      |
| Erlang      | 1986          | Joe Armstrong, Robert Virding, Mike Williams                       |
| Elixir      | 2011          | José Valim                                                         |
| Clojure     | 2007          | Rich Hickey                                                        |
| Groovy      | 2003          | James Strachan                                                     |
| Fortran     | 1957          | John Backus                                                        |
| Cobol       | 1959          | Grace Hopper                                                       |
| Pascal      | 1970          | Niklaus Wirth                                                      |
| OCaml       | 1996          | Xavier Leroy, Jérôme Vouillon, Damien Doligez, and others         |
-->
<!-- prettier-ignore-end -->

## Properties

<!-- prettier-ignore-start -->
| Language | Type System | Paradigm(s)    | Compilation | Memory Management  | Concurrency | 0 or 1-basted indexing | Statement Seperators | Block Delimters | Package Manager | String Quotes     |
|----------|-------------|----------------|-------------|--------------------|-------------|------------------------|----------------------|-----------------|-----------------|-------------------|
| Python   | Dynamic     | Multi-paradigm | Interpreted | Garbage Collection | Yes         | 0                      | Newline              | Indentation     | pip,poetry,uv   | Single, Double    |
| Go       | Static      | Multi-paradigm | Compiled    | Garbage Collection | Yes         | 0                      | Semicolon            | Curly Braces    | go              | Double, Backticks |
<!--
| C           | Static      | Procedural, Structured | Compiled    | Manual                       | No          | 0                      |
| C++         | Static      | Multi-paradigm         | Compiled    | Manual                       | Yes         | 0                      |
| C#          | Static      | Multi-paradigm         | Compiled    | Garbage Collection           | Yes         | 0                      |
| Objective-C | Static      | Multi-paradigm         | Compiled    | Manual                       | Yes         | 0                      |
| JavaScript  | Dynamic     | Multi-paradigm         | Interpreted | Garbage Collection           | Yes         | 0                      |
| TypeScript  | Static      | Multi-paradigm         | Compiled    | Garbage Collection           | Yes         | 0                      |
| Java        | Static      | Multi-paradigm         | Compiled    | Garbage Collection           | Yes         | 0                      |
| Kotlin      | Static      | Multi-paradigm         | Compiled    | Garbage Collection           | Yes         | 0                      |
| Swift       | Static      | Multi-paradigm         | Compiled    | Automatic Reference Counting | Yes         | 0                      |
| SQL         | N/A         | Declarative            | Interpreted | N/A                          | N/A         | N/A                    |
| Rust        | Static      | Multi-paradigm         | Compiled    | Manual                       | Yes         | 0                      |
| Scala       | Static      | Multi-paradigm         | Compiled    | Garbage Collection           | Yes         | 0                      |
| R           | Dynamic     | Multi-paradigm         | Interpreted | Garbage Collection           | Yes         | 1                      |
| Julia       | Dynamic     | Multi-paradigm         | Interpreted | Garbage Collection           | Yes         | 1                      |
| Haskell     | Static      | Functional             | Compiled    | Garbage Collection           | Yes         | 1                      |
| Ruby        | Dynamic     | Multi-paradigm         | Interpreted | Garbage Collection           | Yes         | 0                      |
| Perl        | Dynamic     | Multi-paradigm         | Interpreted | Garbage Collection           | Yes         | 0                      |
| PHP         | Dynamic     | Multi-paradigm         | Interpreted | Garbage Collection           | Yes         | 0                      |
| Lua         | Dynamic     | Multi-paradigm         | Interpreted | Garbage Collection           | Yes         | 1                      |
| Prolog      | N/A         | Logic                  | Interpreted | N/A                          | N/A         | N/A                    |
| Lisp        | Dynamic     | Multi-paradigm         | Interpreted | Garbage Collection           | Yes         | 0                      |
| Scheme      | Dynamic     | Multi-paradigm         | Interpreted | Garbage Collection           | Yes         | 0                      |
| Smalltalk   | Dynamic     | Object-oriented        | Interpreted | Garbage Collection           | Yes         | 1                      |
| Erlang      | Dynamic     | Functional             | Interpreted | Garbage Collection           | Yes         | 1                      |
| Elixir      | Dynamic     | Functional             | Interpreted | Garbage Collection           | Yes         | 0                      |
| Clojure     | Dynamic     | Functional             | Interpreted | Garbage Collection           | Yes         | 0                      |
| Groovy      | Dynamic     | Multi-paradigm         | Interpreted | Garbage Collection           | Yes         | 0                      |
| Fortran     | Static      | Procedural             | Compiled    | Manual                       | No          | 1                      |
| Groovy      | Static      | Procedural             | Compiled    | Manual                       | No          | 1                      |
| Cobol       | Static      | Procedural             | Compiled    | Manual                       | No          | 1                      |
| Ada         | Static      | Multi-paradigm         | Compiled    | Manual                       | Yes         | 0                      |
| Pascal      | Static      | Procedural             | Compiled    | Manual                       | No          | 1                      |
-->
<!-- prettier-ignore-end -->

## Installation Particularities

Generally programming languages can be installed from their respective websites. Alternatively, it
is often possible to install a language using the operating system's package manager. `apt`, `yum`,
`yay` are common for linux distributions, `brew` for MacOS, and `choco` for Windows.

### Python

#### Virtual Environments

Python isolates development environments (configuration and libraries installed) from the system
`python` using **virtual environments**. To create a virtual environment, run the following command
in your terminal:

```bash
python -m venv myenv
```

You can also create environments using `virtualenv`:

```bash
pip install virtualenv
virtualenv myenv
```

Also look into `poetry` and `uv` for more robust development management (packaging, dependencies,
isolation, etc.)

### Go

## Code/File Structure/Layout

<!-- prettier-ignore-start-->
| Language | Module                                                   | Package                         | Variable Case Type |
|----------|----------------------------------------------------------|---------------------------------| --------------|
| Python   | Single Python file                                       | Directory with multiple modules | snake_case    |
| Go       | Collection of Go source files that are compiled together | Collection of go modules        | camelCase     |


<!-- prettier-ignore-end -->

### Python

In python each file is a module. A module can contain functions, classes, and variables. A group of
modules is called a package. A package is a directory that contains a special file called
`__init__.py`. This file can be empty or contain initialization code for the package. There is no
necessary entrypoint. A `main()` function can be used in a script to run the code or a different
name can be used. When python executes a file it runs the code from top to bottom at first, though
sometimes this is only to define functions and classes and when the code executes it may jump around
into different clases or function definitions.

### Go

Go packages are defined on a per-directory basis. Each directory can contain multiple `.go` files.
The package name is defined at the top of each file. The package name must match the name of the
directory containing the file. The `main` package is an exception to this rule. The `main` package
is a special package that defines an executable program. The `main` package must contain a `main`
function that is the entry point of the program.

## Syntax

### Python

### Go

Go is a statically typed language, so types need to be declared. Variables are declared with `var`,
there is a `:=` operator when a type can be inferred.

```go
var investmentAmount float64 = 1000
expectedReturnRate := 5.5
// or
var investmentAmount, years float64 = 1000, 10
```

#### Constants vs Variables

Constants are declared with the `const` keyword. Constants are immutable and must be assigned a
value at the time of declaration. Variables are declared with the `var` keyword. Variables can be
assigned a value at the time of declaration or later in the program.

#### Functions

Like many statically typed languages the types must be specified for function parameters and return
values. In go you can specify a common type in the arguments, and you specify the return types after
the function signature.

```go
func calculateFinancials(revenue float64, expenses float64, taxRate float64) (ebt float64, profit float64, ratio float64) {
    ebt := revenue - expenses
    profit := ebt * (1 - taxRate/100)
    ratio := ebt / profit
    return ebt, profit, ratio
}

func calculateFinancials(revenue, expenses, taxRate float64) (float64, float64, float64) {
    ebt := revenue - expenses
    profit := ebt * (1 - taxRate/100)
    ratio := ebt / profit
    return ebt, profit, ratio
}
```

## Control Structures

### Python

- Uses `elif` for else if statements.j
- Supports: `for`, `while`
- Supports: `continue`, `break`, and `return` statements

```python

# Infinite Loop
while True:
    print("This will run forever")

match choice:
    case 1:
        print("You chose option 1")
        # You can use `break` to exit the loop
    case 2:
        print("You chose option 2")
        # This will execute for case 2
    case _:
        # This is the default case if none of the above cases match
        print("Invalid option")
```

### Go

- Go uses `else if`.
- No `while` loop, only `for`
- Supports: `continue`, `break`, and `return` statements
- You can assign an evaluation to a variable in Go.
-

```go
// Assigning an expression to a variable
wantsCheckBalance := choice == 1

// C-style `if` statement
for i := 0; i < 10; i++ {
    fmt.Println("Iteration", i)
}

// infinite loop
for {
    // This will run indefinitely until you break out of it
    fmt.Println("This will run forever")
}

for condition {
    // This is a conditional loop that will run as long as the condition is true
    // You can also use this to check for a condition before executing the loop body
    fmt.Println("This will run as long as the condition is true")
}

switch choice {
case 1:
    fmt.Println("You chose option 1")
    // You can use `fallthrough` to continue to the next case
case 2:
    fmt.Println("You chose option 2")
    // This will execute for case 2
default:
    // This is the default case if none of the above cases match
    fmt.Println("Invalid option")

}
```
