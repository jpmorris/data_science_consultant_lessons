# %% [markdown]
# This is a multiline
#
# Markdown cell

# %% [markdown]
# # Another Markdown cell
# ## With lots of formatting
# ###  Like this
# 1. list one
# 1. list two
# 1. list three


# %%
# This is a code cell
class A:
    def one():
        return 1

    def two():
        return 2


# %%
# a graph
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)

# %% [markdown]
# [//]: <> FLASHCARD
# A text flashcard (supported by Anki; need script to grab content and strip out first row of pound signs):

# %% [markdown]
# [//]: # FLASHCARD
# This is question;this is the answer
# another question;"another answer with a semicolon; in it"

# %% [markdown]
# [//]: # FLASHCARD
# This is a question with an image <img src="images/testquestion.png">;This is an answer with an image <img src="images/testanswer.png">

# %% [markdown]
# A powerpoint slide (need script to grab content and strip out first row of pound signs):

# %% [markdown]
# [//]: # SLIDE (This is a markdown comment desginating a slide)
# ![picture of spaghetti](images/spaghetti.jpg)
#
# ## Going to sleep
#
# - Get in bed
# - Count sheep
