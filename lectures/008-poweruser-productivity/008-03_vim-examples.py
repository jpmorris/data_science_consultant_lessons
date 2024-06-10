import pandas as pd
import constants
import numpy as np

# 1. Jump by relative line number

# 1. Copy lines jump to part of line and do selective inesrts
df = pd.DataFrame({"column": [1, 2, 3, 4, 5]})
df["column"] = df["column"].apply(lambda x: x + 1)
df["column"] = df["column"].apply(lambda x: x + 1)

# 1. All-caps a selection

var = constants.make_this_uppercase

# 1. Jump to any position in the visible area

# 1. Delete inside parentheses


def func1(
    a,
    b,
    c,
    d,
    e,
):
    return a + b


# 1. Add `import numpy as np` to the top of the file and come back to add 1 to 10 in the array.

x = np.array([])

# 1. Jump to a definition


def add(a, b):
    return a + b


# lots of lines
# lots of lines
# lots of lines

# lots of lines
add(1, 2)


# 1. Multiple cursors, append '_new' to all variables
a = 1
b = 1
c = 1
d = 1
e = 1
f = 1
g = 1
h = 1
i = 1

# 1. Replace all occurrences in a file:
oldvar = 1
print(oldvar)
print(oldvar)
print(oldvar)
# lots of lines
print(oldvar)
