# Testing in Python

There are two popular libraries for testing in Python:

- `unittest` (built-in) - old
- `pytest` (third-party) Pytest is the more popular and we will concentrate on it below. Also has
  many plugins

## Testing Best practices:

- Don't write tests for the sake of coverage
  - **Line Coverage**: Percentage of lines of code that are executed by the tests
  - Sometimes this ends up happening when metrics need to be met
- DEFINITELY write tests when you are refactoring
  - This creates an input-output contract that you can use to ensure that your refactoring didn't
    break anything
  - The risk of not doing this is making many changes and not knowing which broke the code. This is
    a nightmare.
- Unless you're doing TDD (Testing Driven Development), you probably shouldnt, wait until you've
  established your API and have a relatively stable code (or at least functions) before writing
  tests
  - Otherwise you'll end up breaking your tests as your code is in flux
    - This will happen at some level regardless, but you can minimize it
- Your suite of tests should be fast
  - Unit tests ideally run less than a second
  - Component and Integration tests can run longer
- Run your tests often.
  - Tests that don't run, don't inform and eventually break
  - Ideally your IDE is running all your tests at every file save
  - Minimally your tests should be run before you push to a shared repository or be part of a CI/CD
    pipeline
- Shorten the unit test feedback loop. Shorten the time between making code changes and a failed
  unit test
  - You can continuously run pytest whenever a file is saved from a terminal
  - Better if your IDE runs your tests at every file save
    - VSCode is only starting to support this
    - PyCharm has had this for a while
  - This way you can see if you broke something as soon as you save
- Code Smell: if you have to mock out file, api, database access (etc) in order to test a function
  (unless you are testing the access itself) that function is doing too much
- Create single-responsibility functions (or as close as possible)
  - the more side-effects and multiple-responsibilities a function has, the harder it is to test and
    the more fragile the tests are
  - this allows for easy mocking of dependencies

## Application Code vs Data Science Testing Considerations

- Tests should be as simple, fast, and relevant to edge and corner cases
  - **edge case** - is a problem or situation that occurs only at an extreme (maximum or minimum)
    operating parameter.
  - **corner case** - (pathological case) is a problem or situation that occurs only outside of
    normal operating parameters—specifically one that manifests itself when multiple environmental
    variables or conditions are simultaneously at extreme levels, even though each parameter is
    within the specified range for that parameter.
  - You can and should test the normal case, but edge and corner cases or where complexity and bugs
    may arise should be the focus
    - In practices many tests are created for even the normal cases. This is fine if the tests are
      not fragile, are fast, and don't need to be rewriten often
- Data Science testing in production often means running a case or multiple cases through tests that
  include:
  - Loading a model
  - Inference against a statistical model
  - Data preprocessing
- For unit tests all additional (especially slow) steps that can be removed from the test should be.
  - At some point the test is practically irreduceable (must run through a statistical model)
  - However, often loading the model (depending on the size) and making inferences is expensive and
    this overhead makes it difficult to run all unit tests in a matter of seconds
- Some solutions:
  - Run the unit tests less frequently (not after every save)
  - Move all expensive tests to a model-quality suite independent of application testing
    - This may not be possible when you are refactorng related to model code
- Pandas has specific functions for unit testing
  - `assert_frame_equal()` will compare two dataframes, and has a tolerance for non-deterministic
    dataframes

# Pytest

- Tests are functions that start with `test_` or end with `_test`
  - `_test` has the advantage of easier to tab through and easier to visually parse when next to
    many other files
- Can build both class and function-based tests
  - You can write class-based tests for functional code
    - Watch out for inheritance hell if you do this
- When setting up use the command line before using any IDE integration. VSCode is often silent with
  errors. Check VSCode output (select 'Python' in the output dropdown) for errors.

## Output

Pytest hides outputs which can make it hard to debug tests. Use the `-s` flag to show outputs.

### Example

```python
# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5
```

```bash
pytest t_test.py -s
```

## Organization of tests

You can organize tests 'in-tree' or 'out-of-tree'. In-tree is where the tests are in the same
folder, out-of-tree is where the tests are in a separate 'tests' folder. The out-of-tree method
seems to be more popular and easier to stay organized

## Parameterized Tests

## Fixtures

### Parametrized Fixtures

### Scope

## Backwards Compatable with unittest

## Doctests

You can put tests in your docstrings. Don't do this. Much easier and powerful to have an actual
testing suite that has more features, lintable etc.

## Pytest-cov

A pytest plugin that shows coverage. Even the docs say that this plugin may be unnecessary when you
can just run coverage independently:

```bash
coverage run -m pytest tests
coverage report
```
