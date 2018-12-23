# Data and Variables

* __Data__ are pieces of information about individuals organised into variables.
* An __individual__ mean a particular person or object.
* A __variable__ mean a partiular characteristic of an individual.
* A __dataset__ is a set of data identified with particular circumstances.
* Variables can be classified into two categories:
  * Categorical variables: takes category or label values and place an individual in one of several groups.
  * Quantitative variables: take numerical values and represent some kind of measurement.

__Note:__ if average of the variable makes sense, its quantitative otherwise qualitative.
  
* Scales of measurement of variables:
  * Nominal: discrete categories to describe qualitative difference e.g. types of pets. (Names only)
  * Ordinal: indicates ranked ordered difference (without precise degree of difference) e.g. order of finish in a race. (has an order, can be sorted)
  * Interval: gives meaningful difference e.g. distance between pairs consecutive numbers. (start and end given)
  * Ratio: has a meaningful 0 point (Numeric data)
* Distribution of a variable means:
  * what values the variable takes
  * hhow often the variable takes those values

# Exploratory data analysis

Numerical summaries can be visualized as pie chart or bar chart.

Interpreting histogram

* Shape symmetry/skewness, peakedness (modality)
* Center midpoint, half lesser half larger values
* Spread variability or approx range
* Outliers

Mean Median Mode,

Range = Max - Min <br>
Inter Quartile Range = Middle 50% of the data.

The 1.5(IQR) criterion for outliers: An observation is considered a suspected outlier if
* below Q1 - 1.5(IQR)
* above Q3 + 1.5(IQR)

## Boxplot

Five number summary:
* Range gives min and max, covers the whole data
* Q1, M adn Q3 together gives IQR, middle 50% of the data

The standard deviation should be measure of spread along with the mean as measure of center.

 The Standard Deviation Rule:

  *  Approximately 68% of the observations fall within 1 standard deviation of the mean.
  *  Approximately 95% of the observations fall within 2 standard deviations of the mean.
  *  Approximately 99.7% (or virtually all) of the observations fall within 3 standard deviations of the mean.

Two quantitative variables: use scatterplot. The explanatory variable on the horizontal axis and the response variable on the vertical axis. Direction, form and strength + deviation from the pattern.
* Direction: positive, negative or neither.
* Form: linear, curvilinear or clusters.
* Strength: variance.
* Deviation from pattern: outliers.

# Correlation Coefficient

The correlation coefficient $r$ is a numerical measure that measures the strength and direction of a linear relationship between two quantitative variables.

* $r \ \in \ [-1, 1]$
* the closer r is to 0, the weaker is the relationship
* the farther r is from r, the stronger is the relationship.
* sign gives the direction of the relationship.
* r is unitless and does not affected when units of measurement are changed.
* measures only the strength of linear relationship, ignores all others.



A lurking variable is a variable that was not included in your analysis, but that could substantially change your interpretation of the data if it were included.
* Because of the possibility of lurking variables, we adhere to the principle that association does not imply causation.
* Including a lurking variable in our exploration may:
  * help us to gain a deeper understanding of the relationship between variables, or
  * lead us to rethink the direction of an association.
<br>Whenever including a lurking variable causes us to rethink the direction of an association, this is an instance of Simpson's paradox.

The 4 step process that encompasses statistics: data production, exploratory data analysis, probability and inference.

Choosing individuals to collect data is known as sampling, the process of collection of data is study design

Sampling:
1. Volunteered sampling
2. Convenience sampling
3. sampling frame
4. systematic sampling

Probability sampling plan
1. Simple Random sampling
2. Cluster sampling: create groups and select some groups randomly
3. Stratified sampling: create strata and select random members of each stratum

The z-score is used to find probabilities of values other than integral deviationn from the mean.

z-score = (value - mean)/standard deviation 
$$z = \frac{x - \mu}{\sigma} $$

## Steps in Solving Two Types of Normal Problems

1. Given a normal value x, solve for probability:
   - Standardize: calculate &nbsp;&nbsp; $\displaystyle z = \frac{x- \mu}{\sigma}$
   - Locate z in the margins of the normal table. Find the corresponding probability of a normal random variable taking value below z inside the table.
2. Given a probability, solve for normal value x:
   -  Locate the probability inside the normal table. Find the corresponding z value in the margins.
   - "Unstandardize": calculate &nbsp;&nbsp;$x = \mu + z * \sigma$