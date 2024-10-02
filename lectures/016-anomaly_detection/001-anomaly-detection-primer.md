# Resources

## Courses

- Machine Learning - Anomaly Detection via PyCaret -
  https://www.coursera.org/projects/anomaly-detection
- Intel - Anomaly Detection -
  https://www.intel.com/content/www/us/en/developer/topic-technology/artificial-intelligence/training/course-anomaly-detection.html
- Datacamp - Anomaly Detection in Python -
  https://www.datacamp.com/courses/anomaly-detection-in-python
- Udemy - Anomaly Detection: Machine Learning, Deep Learning, AutoML -
  https://www.udemy.com/course/anomaly-detection/?couponCode=OF83024F

## Textbooks

- Beginning Anomaly Detection Using Python-Based Deep Learning - Apress
- Anomaly Detection Princples and Algorithms - Springer

# What is Normal? What is an Anomaly?

## Survey of Possible Anomalies - The wide world of anomalies:

![Anomaly Example 1](images/anomaly_ex1.png)
![Anomaly Example 2 - Sales](images/anomaly_ex2_sales.png)
![Anomaly Example 3 - SVT](images/anomaly_ex3.png)

![Anomaly Example 4](images/anomaly_ex4_svt.png) [^1]
![Anomaly Example 5 - Higgs](images/anomaly_ex5_higgs.png) [^2]
![Anomaly Example 6](images/anomaly_ex6.png)

Also:

- In cybersecurity (malware, hacking, fraudulent emails), anomalous network traffic.
- In finance (fraud detection, credit card fraud), anomalous transactions.
- Healthcare (disease detection), anomalous patient data.

## Definitions and considerations

### Anomalies as an observer-dependent concept

- **Anomaly** - A deviation from what is standard, normal, or expected.
- An anomaly is some data that is different than what is defined as normal.
- **outlier** - A data point that is significantly different from other data points. Some say that
  outliers are anomalies, however, a more robust definitions reserves anomalies based on expectation
  and outlier based on distance from other data points.
  - An outlier need not be an anomaly
- **inlier** - A data point that is not an outlier, a 'normal' data point.
- In the grandest sense, nothing is an anomaly. The universe does what the universe does. However,
  in a given context, with a given expectation, hypotehesis, model, or understanding of the scope of
  data, an anomaly can be defined.
- Note a possible more human-centered quality of anomaly detection: it's depending on what (a human)
  expects.
  - This differs from, say, building a statistical model which aims to describe or predict based on
    regularity of the data, which may include anomalies, and may require modeling of those
    anomalies, but there is less observer-dependent nature of the task:
    - Statistical description or prediction asks if it has properly modeled the data and relevant
      anomalies; anomaly detection asks what should even classifiy as an anomaly in the first place.

### How the human-centered concept of anomaly is important to practioners

- Very important caveats surround this definition:
  - **stationarity** - the underlying generating process of the data is not changing significantly
    over time.
  - And underlying model of the data is assumed in order to define what is normal and what is not.
    - It can be argued that most of scientific progress is the study of anomalies.
    - Because of the human-centeredness of anomaly detection, a expert can provide important context
      and define 'anomaly' different that a novice.
  - Is there enough data to define what is normal?
  - Since normality is defined by ill-defined parameters (such a deviation from the mean), the
    definition can be subjective.
    - A domain expert familiar with the generating process will provide important context to help
      define normal or anomalies.

# Ways to describe Anomaly Detection

- note: note not Novelty detection
  - **novelty detection** - detecting class of data exists in the new data

## Labeled data or not

1. Supervised Anomaly Detection
2. Semi-Supervised Anomaly Detection
3. Unsupervised Anomaly Detection

## Approach based:

1. Distance-based: points are farther from other are anomalous.
1. Density-based: points that are in low density regions are considered anomalous.
1. Rank-based: The most anomalous points are those whose neighbors have others as nearest neighbors.

## Dimensionality of the data

### Unidimensional

- Not all distributions are gaussian.  
  ![Probability Distributions](images/probability_distributions.jpg)
  - Although standard deviation is defined on all distributions it is less useful in non-normal
    distributions. However, it may still be used to define anomalies, except where the distribution
    is asymmetrical.
  - Luckily many distributions end up being near normal or almost symmetrical.
    - But many will not be symmetrical, let alone normal. (E.g. income, wealth, almost anything to
      do with money), or multimodal.
    - If possible use the properties of a closer-matched distribution
    - This is NOT because of the central limit theorem. - Aside: - **Central Limit Theorem** - The
      distribution of the sum of a large number of independent, identically distributed random
      variables approaches a normal distribution, regardless of the shape of the original
      distribution. - Said for a specific case: the sampling distribution from any distribution
      shape will be normal ![Central Limit Theorem](images/central_limit_theorem.png)
- Shape matters because a naive (and often correct way) to find anomalies it to cut out data that
  exists outside of a certain number of standard deviations from the mean.

#### Naive unidemensional anomaly detection

- The fundamental issue: can we create a set of rules that increases precision () and recall?
  - Review precisison and recall:
    - Precision: Of all data 'retrieved' (postiive), what percent are relevant (true)?
    - Recall: of all data that are relevant (true), what percent are relevant (true)?

![Review: Precision-Recall](images/review-precision-recall.png)

- In the case of (quasi-)symmetrical distributions, you may be able to use the properties of a
  normal distribution (mean and standard deviation) to make cuts.

![Symetrical histogram](images/symmetrical_histogram.png)

- In the case of asymmetrical distributions, a simple method is to visualize the data and decide
  (maybe with a domain expert) a cut point to classify as an anomaly.

![Asymetrical histogram](images/asymmetrical_histogram.png)

In this case maybe we pick a value greater than 8000 or 10000 as an anomaly.

- In the case of multimodal distributions, there may be no other option than ad hoc slicing.

![Multimodal histogram](images/multimodal_histogram.png)

2. Multidimensional

- Euclidean distance is the most common way, but may not be appropriate if numbers have different
  scales and scaling factor is not obvious across dimensions.
- An outlier may exist in a orthogonal dimension that cannot be separated in other dimensions.
- Also applying PCA may reveal a separation that is not obvious in the original dimensions because
  of slight differences that compound across dimensions.

1. Time dependence

[^1]:
    "A 40 year old lady comes to the emergency department from her husband’s funeral with a
    sensation of ‘fluttering’ in her chest. She is feeling very anxious. An ECG is performed. What
    is the diagnosis?"

[^2]: Also see: https://cds.cern.ch/images/ATLAS-PHOTO-2012-001-2
