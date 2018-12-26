# Statistical Inference

The process of inferring something about the population based on what is measured in the sample is called **statistical inference**.

Forms of inference:

1. __Point inference__: estimate an unknown parameter using a single number that is calculated from the sample data. 
2. __Interval Inference__: estimate an unknown parameter using an interval of valuesthat is likely to contain the true value of that parameter.
3. __Hypothesis Testing__: check whether or not the data from the sample provide evidence against some claim about the population.

- when the variable of interest is __categorical__, the population parameter that we will infer is the __population proportion (p)__ associated with the variable.
- when the variable of interest is __quantitative__, the population parameter that we will infer about is the __population mean ($\mu$)__ associated with the variable.

Sample mean $\bar{x}$ and smaple proportion $\hat{p}$ are unbiased estimate of $\mu$ and $p$ respectively as long as the samples are taken randomly and study design is not flawed.

## Estimating population proportion

Standard error of the estimator $\hat{p}$ is $\sqrt{\frac{p (1 - p)}{n}}$.

Confidence interval of $\hat{p}$ is $p \pm z^*\cdot\sqrt{\frac{p(1-p)}{n}}$.


For the margin of error $m$, the required sample size is $\frac{1}{m^2}$, with conservative value of $\hat{p}$ taken as $\frac{1}{2}$. 

These are safe to use if $n\cdot \hat{p} \ge 10$ and $n \cdot (1-\hat{p}) \ge 10$

To obtain a desired margin of error (m) in a 95% confidence interval for unknown population proportion p, a conservative sample size n is $\frac{1}{m^2}$

The margin of error of a poll is determined (conservatively) by $\frac{1}{\sqrt{n}}$

The methods developed is this unit are safe to use as long as $n \cdot p \ge 10$ and $n \cdot (1-\hat{p})\ge 10$