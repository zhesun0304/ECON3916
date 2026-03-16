# Hypothesis Testing & Causal Evidence Architecture

## Overview
This project applies hypothesis testing to the Lalonde (1986) experimental dataset in order to evaluate whether a job training program produced a real causal effect on participants’ 1978 earnings. Rather than treating statistical significance as a mechanical output, this lab frames inference as an exercise in falsification: testing whether the observed treatment effect is strong enough to contradict the Null Hypothesis under rigorous decision rules.

The central goal was to move beyond simple estimation and toward **causal evidence architecture**. In practice, that meant distinguishing a true economic signal from stochastic noise and validating results under both parametric and non-parametric frameworks.

## Objective
The objective of this lab was to operationalize the scientific method in an applied data science context. Using the Lalonde benchmark dataset, I evaluated competing explanations of earnings differences by asking whether the observed treatment effect could plausibly arise from chance alone.

This lab represents a shift from **estimation** to **falsification**:
- Estimation asks, “What is the size of the effect?”
- Falsification asks, “Is the observed effect credible enough to reject a no-effect world?”

By structuring the analysis around formal hypothesis tests, I treated statistical inference as a disciplined process of adjudicating between causal narratives.

## Technical Approach
This analysis was implemented in Python using `pandas`, `numpy`, `scipy.stats`, `matplotlib`, and `seaborn`.

### Methods used
- **Welch’s T-Test**
  - Estimated the Average Treatment Effect (ATE) by comparing mean 1978 earnings between treated and control groups.
  - Interpreted the T-statistic as a **Signal-to-Noise ratio**, where the signal is the difference in means and the noise is the uncertainty around that estimate.
  - Used Welch’s specification to avoid assuming equal variances across groups.

- **Permutation Test (10,000 resamples)**
  - Constructed an empirical null distribution by randomly shuffling treatment labels.
  - Verified whether the observed difference in means remained statistically unusual without relying on strict normality assumptions.
  - Strengthened inference given the heavy-tailed nature of earnings data.

- **Distributional Visualization**
  - Compared kernel density estimates of treated and control earnings to visually inspect the counterfactual shift in outcomes.
  - Used visualization to connect statistical results back to the underlying economic distribution.

### Statistical discipline
- Applied explicit hypothesis testing decision rules at a conventional significance threshold.
- Controlled for **Type I error risk** by grounding conclusions in formal p-values rather than post-hoc storytelling.
- Cross-validated results across both parametric and non-parametric methods to reduce dependence on a single modeling assumption.

## Key Findings
The analysis identified a positive treatment effect of approximately **$1,795** in real earnings for participants who received job training. Both the Welch’s T-Test and the Permutation Test indicated that this effect was statistically significant, allowing me to reject the Null Hypothesis.

In other words, the observed earnings lift was unlikely to be explained by random assignment noise alone. This provided evidence, by **statistical contradiction**, that the training program generated a real causal effect in the experimental sample.

## Business Insight
In the modern algorithmic economy, the ability to calculate a statistic is no longer rare. The scarce skill is designing evidence that can withstand scrutiny. Firms such as Netflix, Uber, and other data-intensive organizations do not simply ask whether a metric is “significant”; they ask whether the design is valid, whether the comparison is credible, and whether the conclusion is robust to bias and noise.

Rigorous hypothesis testing functions as a **safety valve** for decision-making:
- It guards against **data grubbing** and overinterpreting random variation.
- It reduces the risk of acting on **spurious correlations**.
- It creates a structured framework for falsifying weak claims before they influence business strategy, product design, or policy decisions.

This matters because poor inference scales quickly in high-stakes environments. A false positive in experimentation can lead to wasted capital, misguided product changes, or flawed policy recommendations. By contrast, disciplined falsification helps organizations distinguish genuine causal signals from attractive but unreliable stories.

## Why This Project Matters
This lab demonstrates more than technical fluency with Python. It signals an understanding of how to build credible evidence in settings where causal claims matter. The project shows how classical statistical tools, when framed correctly, become part of a broader system for evaluating truth under uncertainty.

That is the foundation of strong data science: not just computing answers, but knowing which answers deserve to be believed.
