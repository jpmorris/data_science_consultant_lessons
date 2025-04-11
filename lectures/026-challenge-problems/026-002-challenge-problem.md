# Challenge Problem #2 - Scores from Binary flags and Count column

## Given:

A list of audit flags and list of findings (and thereby number of findings) one per each audit

## Deliverable:

Some method to determine a relative rank of severity (1 to 5) to present to users so they know which
risky audits to concentrate on

## Current Solution

- Using all columns: flags and findings count
- Standardize the data
- Use PCA to reduce the dimensionality of the data
- Take the top component
- Use several Gaussians over the first component of this data as a histogram. The data for different
  peaks in the distributions, cut at certain standard deviations to define the levels 1 to 5
  statistically

## Challenge:

Can you think of any other way to do this? There are probably other ways but there may not be
anything easy, and this may be the best way. Feel free to think about this from the user-level, the
client-level, feel free to think outside the box and all over. No bad ideas. Sometimes the solution
involves something with the business or thinking in a different way.

## Notes/insights:

One reason the original team used PCA may have been that they wouldn't have to survey users. There
may be a way to label data by surveying users but I think it might be ad-hoc, subjective and kind of
messy. Maybe you can think of a better way if you want to go that way.

## Proposed Options:

- Users can label data:

1.  We could get users to label **cases/rows** in terms of risk, get a few hundred to 1000 and then
    train any multilevel ORDERED classification
    - Binary classification is the most common, multiclass classification is somewhat common, but in
      this case we have an ORDERED MULTLEVEL classificaiton which lends to unique implementations:
      - Ordinal Logistic Regresson - `statsmodels.miscmodels.orginal_model.OrderedModel`
      - PyMC - a python bayesian multilevel modeling which also allows the use of Markov Chain Mote
        Carlo methods
      - Statsmodels and 'mord' libraries also do ordered multilevel classification
    - The problem with this method besides needing expert labelers is that the subjective nature of
      this labeling may have wide variance
2.  We could get users to label the **flags/columns** in terms of risk. In this case we are
    weighting the flags and then doing a linear combination of the flags to get a risk score
    - This method also requires domain experts, and may have wide variance but probably less than
      labeling cases/rows.

- Non (or minimum) domain expert labeling

3.  Simple sum - We could just add up all the 'Y' flags to get a score and then set cuts based on
    the distribution (possibility tuned with a domain expert)

    - The count column can be scaled by a weight factor
    - There may be a concern that too many cases will bunch at a given score (hence the reason to
      try and spread them out with PCA), however this may signal that there really should be a large
      number with a given score. Weighting as in solution #2 above may spread out the data more.
    - If there are known properties of the flags (such as) the rarity of the flag is more important
      you can scale the flag by its reciprocal.

4.  Current PCA solution

    - Problem only explains 14% of the variance in the flags
    - Benefit is you don't need any labelers.
