# Sampling distribution

1. A __sample statistic__ is a numerical summary measure calculated for sample data (always a __random__ variable). 
2. The same numerical summary measure calculated for the population data are called __population parameter__ (a constant).
3. Since the sample statistic is a random variable, it has a probability distribution, which is commonly known as sampling distribution.
4. The difference between value of the sample statistic and the value of the corresponding population parameter is known as sampling error. $$sampling \ error = \bar{x} - \mu$$
5. The errors that occur in collection, recording and tabulation is known as nonsampling error.
6. The mean of sampling distribution of $\bar{x}$ is equal to pupulation mean i.e. $\mu_{\bar{x}} = \mu$
7. The standard deviation of sampling distribution of $\bar{x}$ is known as standard error i.e. $\sigma_{\bar{x}} = s.e.$
8. The sample mean $\bar{x}$ is the estimate of population mean $\mu$. When $\bar{x} = \mu$, $\bar{x}$ is known as unbiased estimate. Otherwise a biased estimate.
9. Standard error, $\displaystyle\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$ ; if $\displaystyle\frac{n}{N} \leq 0.05$ otherwise with finite population corrector $\displaystyle\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}} \sqrt{\frac{N-n}{N - 1}} $
13. __Central limit theorem__, sampling distribution of a normal or non-normal population tends to be a normal distribution with $\mu_{\bar{x}} = \mu$ and $\displaystyle\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$ for $n \geq 30$.
14. The $z$ value for a sample value of $\bar{x}$ is $\displaystyle z = \frac{\bar{x} - \mu}{\sigma_{\bar{x}}}$
15. sample proportion, $\hat{p}$. Standard deviation $\sigma_{\hat{p}} = p = \sqrt{\frac{pq}{n}}$ 

# Estimation of mean and proportion, Inferential statistics

* The assignments of value(s) to sample population parameter based on the value of the corresponding sample statistic is called estimation.
* The value assigned to a population parameter based on the sample statistic is called an estimate.
* The sample statistic used to estimate a population parameter is called an estimator.
* Estimation types
  * The value of a sample statistic that is used to estimate a population parameter is called a point estimate.
  * In interval estimation, an interval is constructed round the point estimate and it is stated that this interval is likely to contain the corresponding population estimate.
* **Confidence level and confidence interval:** Each interval is constructed with regard to a confidence level and is called confidence interval. $$ Point\ estimate \pm Margin\  of\ error $$ The confidence level associated with the confidence interval states how much confidence we have that this interval contains the true population parameter. The confidence level is denoted by $(1 - \alpha)100\%$

* Margin of error is the quantity added or subtracted to the $\bar{x}$ to calculate the confidence interval. $E = z\sigma_{\bar{x}}$

## How to estimate population mean
__Case I__: If the following three conditions are satisfied

1. population standard deviation $\sigma$ is known
2. sample size is small i.e. $n < 30$ 
3. the population from which the sample is selected is normally distributed

Use normal distribution to make confidence interval of $\mu$.

__Case II__: If the following two conditions are satisfied

1. population standard deviation is known
2. sample size is large i.e. $n \ge 30$

Use normal distribution to make confidence interval

__Case III__: If the following three conditions are fulfilled

1. population standard deviation is known
2. sample size is small i.e. $n < 30$
3. population from which the sample is selected is not normally distributed.

Use non parametric method to make the confidence of $\mu$

# Estimation of population mean when $\sigma$ is not known

**Case I**: If the following conditions are fulfilled:
1. population standard deviation is not known
2. sample size is small i.e. $n < 30$
3. the population from which the sample is selected is normally distributed
then use $t$ distribution to make the confidence interval for $\mu$.

**Case II**: If the following two conditions are satisfied:
1. The population standard deviation $\sigma$ in not known
2. the sample size is large i.e. $n \ge 30$
use $t$ distribution to make the confidence interval.

**Case III**: If the following three conditions are satisfied:
1. The population standard deviation is not known
2. the sample size is small
3. the population from the sample is selected is not normally distibuted

use non parametric method to estimate $\mu$

# $t$- distribution

A special type of bell shaped distribution with mean 0 and standard deviation $\displaystyle\sqrt{df(df - 2)}$. It has only one parameter called degree of freedom $df$. For large smple size, the t distribution approaches the standard normal distribution.

