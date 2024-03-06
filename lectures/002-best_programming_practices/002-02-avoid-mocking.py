# %% [markdown]
# # Which is better to unit testing?
# ```
# def function(file_name):
#     stuff = open(file_name)
#     file_contents = do_stuff(stuff)
# ```
# or
# ```
# def function(file_contents):
#     do_stuff(file_contents)
#
# Better to teset the function that modifies mock data in memory than
# to mock out a service.
