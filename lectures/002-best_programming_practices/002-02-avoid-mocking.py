# %% [markdown]
# # Given the following code snippets:


# %%
def work_with_file(file_name):
    with open(file_name) as fp:
        file_contents = fp.read()
        do_stuff(risky_stuff)


# %% [markdown]
# or

# %%
with open(file_name) as fp:
    file_contents = fp.read()


def function(file_contents):
    do_stuff(file_contents)


# %% [markdown]
# # Questions:
# 1. Which seems better?
# <details>
#  <summary>Answer</summary>
#  <p> The second one is better because it separates the file reading from the file processing. This makes the code more modular and easier to test. </p>
# </details>
#
# 2. Which function should you test?
#
# <details>
#  <summary>Answer</summary>
#  You would have to needlessly mock the file in `work_with_file()` when you could just test the contents.
#  This may seem obvious here, but always question unit test-level mocks (databases, etc.) and whehter you need them.
# </details>
