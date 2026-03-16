# Recovering Experimental Truths via Propensity Score Matching

## Overview
This project examines one of the central challenges in causal inference: how to recover a credible treatment effect when working with observational rather than experimental data. Using the observational subset of the Lalonde dataset, I applied Propensity Score Matching (PSM) to correct for selection bias and reconstruct a comparison closer to the randomized benchmark.

## Objective
The objective of this lab was to repair the failure of naive observational comparison by using Propensity Score Matching to build a more credible counterfactual and recover the underlying causal effect of job training on earnings.

## Methodology
This analysis was implemented in Python using `pandas`, `numpy`, and `scikit-learn`, with a focus on modeling treatment selection and reconstructing balance between treated and control groups.

### Technical approach
- **Modeled selection bias**
  - Identified that the observational control group differed systematically from the treated group, creating a biased naive comparison.
  - Treated the assignment process itself as a modeling problem rather than assuming observed groups were directly comparable.

- **Estimated propensity scores**
  - Built a logistic regression model to estimate each individual’s probability of receiving treatment based on observed pre-treatment characteristics.
  - Used the propensity score as a balancing metric to summarize multidimensional confounding.

- **Applied nearest-neighbor matching**
  - Matched treated individuals to observational controls with similar propensity scores using a nearest-neighbor algorithm.
  - Constructed a matched sample designed to reduce imbalance and better approximate the experimental counterfactual.

- **Re-estimated the treatment effect**
  - Compared post-matching outcomes between treated and matched control groups.
  - Evaluated whether the recovered estimate aligned more closely with the known experimental result.

## Key Findings
The naive observational comparison produced a heavily biased estimate, incorrectly suggesting a large negative treatment effect of approximately **-$15,204**. After applying Propensity Score Matching, the estimated treatment effect shifted substantially and recovered a positive effect of roughly **+$1,800**, much closer to the experimental benchmark.

These results demonstrate how strongly selection bias can distort causal conclusions in observational data. More importantly, they show that careful design and matching can recover a far more credible estimate of the true treatment effect.

## Why This Project Matters
In applied economics and data science, observational data is far more common than randomized experiments. That makes the ability to diagnose selection bias and repair invalid comparisons a critical skill. This project demonstrates not just technical implementation, but an understanding that credible causal inference depends on designing better comparisons, not simply computing more statistics.
