# Beta/Binomial Distribution
A previous data scientist needed to do an anomaly detection for when a series of audits performed by CPAs produced zero findings in their audits.  This suggests an issue with the auditing.  This must, of course, be compared to what the average number of zero audits are generally produced.

Since this naturally a statistical solution: we are comparing a case to averages based on how often we are expecting 'success' (zero findings) should occur this suggests natural distributions based on Bernoulli trials.

** Bernoulli Trials **
A Bernoulli trial is a random experiment where there are only two possible outcomes: success or failure. Each trial is independent of the others, and the probability of success remains constant across trials.

A **Binomial distribution** is a discrete probability distribution that describes the number of successes in a fixed number of independent Bernoulli trials, each with the same probability of success. The binomial distribution is characterized by two parameters: the number of trials (n) and the probability of success in each trial (p) of the formula:

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$

You'll recall that Bayes' Theorem allows us to update our beliefs about the probability of an event based on new evidence. In the context of the Beta/Binomial distribution, we can use Bayes' Theorem to update our prior beliefs about the probability of success (p) based on observed data.
