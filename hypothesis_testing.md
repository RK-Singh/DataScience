# Hypothesis testing

**Statistical hypothesis testing** is defined as:<br>
**Assessing evidence provided by the data in favor of or against some claim about the population.**

**Hypothesis testing step 1: Stating the claims:**

The **null hypothesis** (denoted by "<b>H<sub>0<sub> </b>") suggests nothing special is going on; no change in the status quo.

The **alternate hypothesis** (denoted by "<b>H<sub>a<sub> </b>") disagrees with null hypothesis. It usually represents what we want to check or what we suspect is really going on.

**Hypothesis testing step 2: Choosing a sample and collecting data:**

Collect data, summarize it with sample proportion, sample mean and the sample standard deviation. Use these sample statistic to summarize a test statistic.

**Hypothesis testing step 3: Assessing the evidence:**

calculate probability of observing the data when H<sub>0</sub> is true. If this probability is very small, reject H<sub>0</sub>.

**Hypothesis testing step 4: Making concludion:**

The cut-off to reject H<sub>0</sub> ($\alpha$) is called **significance level of the test**. Commonly, $\alpha = 0.05$ or 5%.


 -  if the p-value < $\alpha$ (usually 0.05), then the data we got is considered to be "rare (or surprising) enough" when H<sub>0</sub> is true, and we say that the data provide significant evidence against H<sub>0</sub>, so we reject H<sub>0</sub> and accept H<sub>a</sub> i.e. statistically significant.
 -  if the p-value > $\alpha$ (usually 0.05), then our data are not considered to be "surprising enough" when Ho is true, and we say that our data do not provide enough evidence to reject H<sub>0</sub> (or, equivalently, that the data do not provide enough evidence to accept H<sub>a</sub>) i.e. statistically not significant.

## Hypothesis testing for the population proportion (p):
This test is nown as the **z-test for the population proportion (p)**. It is done when we are working with a categorical variable. Every test has a test statistic, which is a measure of how far the sample proportion is from the null value p<sub>0</sub>.

$$z=\frac{\hat{p}-p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}}$$

The _p-value_ is the probability of observing test statistics extreme as observed (or even more extreme) assuming that the null hypothesis is true.

- $H_a : p < p_0 \implies p - value= P(Z\le z)$ **left tail test**
- $H_a : p > p_0 \implies p - value= P(Z \ge z)$ **right tail test**
- $H_a : p =\not p_0 \implies p - value= 2P(Z\ge|z|)$ **two tail test**

The _critical value_ is the value which cuts off an area referred to as the _critical region_ (or area of rejection).

Every hypothesis test is based on the assumption that $H_0$ is true.

## Types of error

- If the null hypothesis is true and we do not reject it, it is a **correct decision**
- If the null hypothesis is wrong and we reject it, is is a **correct decision**
- If the null hypothesis is true and we reject it, it is **type I** error.
- If the null hypothesis is wrong and we fail to reject it, it is **type II** error.

## Multivariate analysis

- matched sample
- two means: independent sample
- more than two means: independent sample

Two sample t-test:

1. Stating the hypothesis:
  - The null hypothesis has the form:
    - $H_0:\mu_1-\mu_2=0$

  - The alternate hypothesis takes one of the 3 form:
    - $H_0:\mu_1-\mu_2>0$
    - $H_0:\mu_1-\mu_2<0$
    - $H_0:\mu_1-\mu_2=\not0$


2. Check conditions:
    1. The two samples are indeed independent.
    2. One of the two scenarios:
       1.  Both populations are normal.
       2.  Populations are not normal but sample size > 30.

3. Assuming it is safe to use, the two-sample t-test statistic is:
    $t=\frac{(\bar{y_1}-\bar{y_2} - 0)}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$