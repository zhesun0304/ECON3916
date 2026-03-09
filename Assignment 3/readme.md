# Econ 3916 — Assignment 3: Causal Inference, Non-Parametric Inference, and Matching

This assignment applies non-parametric inference and causal inference tools to four business-style problems involving skewed outcomes, experimental falsification, and selection bias. The workflow combines manual statistical engines, matching design, and diagnostic visualization to evaluate claims made by firms and internal teams.

---

## Project Overview

The assignment is organized into four phases:

1. **Bootstrapping non-parametric uncertainty** for zero-inflated and right-skewed tip data  
2. **Permutation testing** for an A/B delivery-time experiment with extreme outliers  
3. **Propensity Score Matching (PSM)** to reduce selection bias in a loyalty program setting  
4. **AI-assisted expansion** through a Love Plot that evaluates covariate balance before and after matching  

The overall goal is to show why standard parametric tools can fail under skewness, outliers, and self-selection, and how more robust econometric methods provide better empirical evidence.

---

## Phase 1 — Bootstrapping Non-Parametric Uncertainty

### Problem
A labor union challenges SwiftCart’s claim about “Median Driver Compensation.” Tip data is difficult to analyze because it is:

- **Zero-inflated**: many users tip exactly \$0
- **Heavily right-skewed**: a few users leave very large tips

In this setting, normal-theory approximations and CLT-based confidence intervals are not reliable for the median.

### Data Generating Process
A synthetic audit sample of 250 driver tips was constructed using:

- 100 zero tips
- 150 positive tips drawn from an exponential distribution with scale = 5.0

### Method
A **manual bootstrap engine** was written using `numpy` only.

- Resampled the observed sample **with replacement**
- Repeated the process **10,000 times**
- Computed the **median** for each bootstrap resample
- Used `np.percentile` to construct a **95% percentile confidence interval**

### Result
- **Sample median** ≈ `0.7553`
- **95% Bootstrap CI** ≈ `[0.2653, 1.3636]`

### Interpretation
The confidence interval is **asymmetric**, with a longer upper tail than lower tail. This reflects the actual topology of the data:

- mass at zero
- right-skewed positive values
- non-normal sampling distribution of the median

This demonstrates why bootstrap percentile intervals are more appropriate than symmetric parametric intervals in this setting.

---

## Phase 2 — Falsification in Logistics A/B Testing

### Problem
An engineering team claims a new “Batch Routing” algorithm reduces delivery times. However, while treatment usually performs well, it also produces rare but extreme upper-tail outliers caused by software crash loops. This violates the homoscedasticity assumptions of a standard t-test.

### Data Generating Process
Synthetic A/B test data was generated for 1,000 deliveries:

- **Control**: 500 observations from `Normal(mean=35, sd=5)`
- **Treatment**: 500 observations from `LogNormal(mean=3.4, sigma=0.4)`

### Observed Difference in Means
The simple observed difference was defined as:

\[
\bar{X}_{control} - \bar{X}_{treatment}
\]

Result:

- **Observed difference in means** ≈ `2.2650`

A positive value indicates the treatment group had a lower average delivery time.

### Method
A **manual permutation test** was implemented using `numpy` only.

- Concatenated all 1,000 outcomes into one array
- Repeated **5,000 random permutations**
- Split each permutation into two pseudo-groups of 500
- Computed the simulated difference in means for each iteration
- Calculated the empirical p-value as the share of simulated differences at least as extreme as the observed difference

### Result
- **Empirical two-sided p-value** = `0.0004`

This means only:

\[
\frac{2}{5000} = 0.0004
\]

of the permutations produced a difference as extreme as the observed one.

### Interpretation
The p-value is extremely small, providing strong evidence against the null of no treatment effect. The permutation test is preferable here because it does **not** rely on:

- normality
- equal variances
- clean tail behavior

This makes it a more credible falsification test in the presence of crash-loop outliers.

---

## Phase 3 — Causal Control and Selection Bias

### Problem
The marketing team claims users who subscribe to **SwiftPass** spend much more per month and wants to increase acquisition spending. But this comparison is likely contaminated by **selection bias**: high-volume users may naturally self-select into the program.

### Dataset
The provided dataset `swiftcart_loyalty.csv` includes:

- pre-treatment spending
- account age
- support tickets
- subscriber status
- post-treatment spending

---

### Step 3.1 — Naive Simple Difference in Means

The initial estimate compared average post-treatment spending between:

- **Subscribers** (`D=1`)
- **Non-Subscribers** (`D=0`)

#### Result
- Mean post-spend for `D=0`: **56.4729**
- Mean post-spend for `D=1`: **74.0436**

So the naive Simple Difference in Outcomes (SDO) was:

\[
E[Y|D=1] - E[Y|D=0] = 17.5707
\]

### Interpretation
At face value, subscribers appear to spend about **17.57** more after treatment. But this estimate is not causal, because subscribers and non-subscribers are not randomly assigned.

---

### Step 3.2 — Propensity Score Matching (PSM)

### Method
To reduce observable selection bias:

1. Estimated each user’s **propensity score** using `LogisticRegression`
2. Used only **pre-treatment covariates**:
   - `pre_spend`
   - `account_age`
   - `support_tickets`
3. Performed **1:1 nearest-neighbor matching** using `NearestNeighbors`
4. Matched each subscriber to the single non-subscriber with the closest estimated propensity score
5. Computed the **Average Treatment Effect on the Treated (ATT)** using the matched sample

### Result
- **Naive SDO** = `17.5707`
- **PSM ATT** = `9.9139`

### Interpretation
After constructing a matched control group, the estimated effect falls substantially:

\[
17.5707 - 9.9139 = 7.6568
\]

This suggests that a large portion of the raw spending gap was not caused by SwiftPass itself, but by the fact that power users were more likely to join the program in the first place.

So the more credible causal interpretation is:

- the naive comparison **overstated** the effect
- the matched ATT is smaller and more defensible
- selection bias was materially influencing the original claim

---

## Phase 4 — AI Expansion: Love Plot Diagnostics

### Objective
After matching, a **Love Plot** was created to visualize covariate balance before and after matching.

### Method
The plot compares **absolute standardized mean differences (|SMD|)** for each pre-treatment covariate in:

- `df_unmatched`
- `df_matched`

The covariates included were:

- `pre_spend`
- `account_age`
- `support_tickets`

The standardized mean difference is:

\[
SMD = \frac{\bar{X}_T - \bar{X}_C}{\sqrt{(s_T^2 + s_C^2)/2}}
\]

Love plots conventionally display **absolute** SMD values.

### Interpretation Criteria
The main visual evidence of improved balance is:

- post-match points move **leftward** toward zero
- most covariates fall below `|SMD| < 0.10`
- at minimum, covariates should be well below `|SMD| < 0.25`

### Theoretical Conclusion
A strong Love Plot provides evidence that matching improved balance on **observed** covariates. However, it does **not conclusively prove** that all selection bias has been eliminated, because:

- matching only addresses **observable** confounders
- unobserved confounding may still remain
- good balance is necessary for causal credibility, but not sufficient for perfect identification

So the appropriate claim is:

> Matching appears to have substantially mitigated observable selection bias, thereby improving the credibility of the ATT estimate.

---

## Key Takeaways

- **Bootstrap** is powerful when the sampling distribution is non-normal, asymmetric, and zero-inflated.
- **Permutation tests** provide robust inference when outliers and heteroskedasticity make standard t-tests unreliable.
- **Naive group comparisons** can dramatically overstate treatment effects when selection bias is present.
- **PSM** helps construct a more credible counterfactual by matching treated units to similar untreated units.
- **Love Plots** are useful diagnostics for checking whether matching improved balance across observed covariates.

---

## Tools Used

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `sklearn.linear_model.LogisticRegression`
- `sklearn.neighbors.NearestNeighbors`

---

## Final Conclusion

This assignment shows how careful econometric design changes the interpretation of empirical claims. Under skewness, outliers, and self-selection, naive or standard parametric methods can be misleading. By using bootstrap inference, permutation testing, propensity score matching, and balance diagnostics, we obtain more credible estimates and a stronger framework for causal analysis.

The central lesson is that **data alone do not identify causal truth**. The credibility of a conclusion depends on whether the statistical design respects the structure of the data and the mechanism generating treatment assignment.
