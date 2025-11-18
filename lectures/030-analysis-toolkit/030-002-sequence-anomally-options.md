# Setup

- Want to look for anomalies in connected entities that interact with each other (all are making
  charges to us, the payer)
- These anomalies would be charging patterns that are different in:
  - Amount
  - Frequency
  - Time
  - Location
- We want to use as much data as possible. There are several encodings of this information that will
  help us exploit as much of the informational content as possible.
  - Related entities - suggest graph-based analysis
  - Sequences of charges - suggest sequence-based analysis (e.g. LSTM, transformers)
  - NO Labeled data - but would suggest supervised learning

## Options

- TIP: **USE GENAI FOR IDEATION**

### Jensen-Shannon Divergence (JSD)

- Algorithm:
  - For each entity, create a histogram of charge amounts (or other features like time, frequency).
  - Compute the JSD between the histograms of different entities to measure the similarity of their
    charging patterns.
  - Entities with high JSD values compared to the average can be flagged as anomalies.
    - Pros:
      - Effective for detecting subtle differences in charging patterns.
      - Can be applied to various features (amount, time, frequency) for a comprehensive analysis.
      - Computationally efficient for large datasets.
      - Robust to noise in the data.
    - Cons:
      - May not capture complex temporal patterns in sequences.
      - Requires careful selection of histogram bins.
      - Sensitive to the choice of features used for histogram creation.
- Method:
  - Using discrete distributions (histograms) to represent the data.
  - JSD is a symmetric and smoothed version of Kullback-Leibler divergence

### Change Point Detection (CPD)
- Algorithm:
  - For each entity, create a time series of charge amounts (or other features like frequency).
  - Apply CPD algorithms (e.g., PELT, Binary Segmentation) to identify points in the time series
    where the statistical properties change significantly.
  - Entities with significant change points can be flagged as anomalies.
    - Pros:
      - Effective for detecting abrupt changes in charging patterns over time.
      - Can handle non-stationary data and varying patterns.
      - Provides interpretable results by identifying specific change points.
    - Cons:
      - May miss gradual changes in patterns.
      - Requires careful tuning of algorithm parameters (e.g., penalty values).
      - Computationally intensive for large datasets.
- Example (Change Point Detection in Climate Science):
  - During the "Global Warming Hiatus" period (1998-2013), the rate of global temperature increase slowed down
    significantly compared to previous decades. Change point detection algorithms can identify this
    period as a significant change point in the time series of global temperatures, indicating a
    shift in the underlying climate dynamics.


 