# Review

Last time we implemented makemore -- a basic character-level language model -- which makes examples
similar to the training data.

The problem with the previous implementation is that it only uses a single letter of context.
However, if as we try and incorporate more context, the number of possibilities grows exponentially.
To solve this, we will use a multi-layer perceptron (MLP) to help us learn more complex patterns in
the data.

See Karpathy's video for more details: https://karpathy.ai/zero-to-hero.html And his repo here:
https://github.com/karpathy/makemore

# Building a MLP

See the the paper we use for MLPs here: https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf


