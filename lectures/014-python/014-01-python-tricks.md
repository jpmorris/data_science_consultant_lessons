# Python Tricks

## Using case-match with space on re match options
- Python 3.10 introduced structural pattern matching https://docs.python.org/3/whatsnew/3.10.html#pep-634-structural-pattern-matching
  which allows to compare a subject to different patterns. 
- This feature does not support regular expressions directly in the case patterns
- However, you can use a regular expression in the match statement with named groups to achive a similar effect
- Moreover, by using the `(?x)` flag in the regular expression, you can add whitespace to the regular expression options

```python
a_re1 = re.compile(
    r"""(?x)
    (?P<full>[0-9]{2}\.[0-9]{3})|
    (?P<partial>[0-9]{2})\.|
    (?P<other>.?)
    """
)


def clean_as(a_el):
    if not a_el:
        return "00.000"
    mo = re.match(a_re1, a_el)
    if not mo:
        return "00.000"
    match mo.lastgroup:
        case "full":
            return mo.group(mo.lastindex)
        case "partial":
            return mo.group(mo.lastindex) + ".000"
        case _:
            return "00.000"

    as1 = as.apply(lambda x: [clean_as(y) for y in x])

```
## To ad-hoc test the speed of a block of code
If you're wondering which version of a piece code you are refactoring or writing is faster
you can use `timeit` in the code and run and print to console or check with the debugger:
```python
import timeit 
def test1():
    # some code
    pass

def test2():
    # different code
    pass

test1time = timeit.timeit(lambda: test1(), number=10)
test2time = timeit.timeit(lambda: test2(), number=10)
```