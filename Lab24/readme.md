# Causal ML — Double Machine Learning for 401(k) Policy Evaluation

## Objective

This lab applies Double Machine Learning to estimate the causal effect of 401(k) eligibility on household net financial assets while addressing confounding, regularization bias, and treatment effect heterogeneity across income groups.

## Methodology

- Demonstrated the risk of regularization bias using a simulated data-generating process where the true treatment effect was known to be 5.0.

- Compared naive LASSO-based estimation against the true causal effect to show how prediction-focused machine learning can shrink treatment coefficients toward zero when applied directly to causal questions.

- Loaded 401(k) pension plan data and defined `net_tfa` as the outcome variable, `e401` as the treatment variable, and household financial and demographic characteristics as control variables.

- Set up a DoubleML Partially Linear Regression model to separate the prediction task from the causal estimation task.

- Used Random Forest nuisance learners to flexibly model both the outcome process and the treatment assignment process.

- Applied 5-fold cross-fitting to reduce overfitting and improve the credibility of the causal estimate.

- Estimated the Average Treatment Effect of 401(k) eligibility on household net financial assets.

- Conducted Conditional Average Treatment Effect analysis by income quartile to evaluate whether 401(k) eligibility has different effects across the income distribution.

- Visualized CATE estimates with 95% confidence intervals to compare the magnitude and uncertainty of treatment effects across income subgroups.

## Key Findings

The simulation showed that naive machine learning is not automatically valid for causal inference. Although LASSO is useful for prediction and variable selection, it can shrink the treatment coefficient toward zero when used directly in a causal estimation problem. This motivates the use of Double Machine Learning, which uses machine learning for nuisance prediction while preserving a valid treatment effect estimate.

In the 401(k) application, the DoubleML PLR model estimated that 401(k) eligibility increased net total financial assets by approximately **$[YOUR_ATE_HERE]** on average. This estimate should be interpreted as the effect of eligibility after adjusting for observable household differences such as income, age, education, family structure, and other financial characteristics.

The CATE analysis showed that treatment effects varied across income quartiles. The estimated effects were approximately **$[Q1_ATE]** for the lowest-income quartile, **$[Q2_ATE]** for the second quartile, **$[Q3_ATE]** for the third quartile, and **$[Q4_ATE]** for the highest-income quartile. If the estimates rise with income, this suggests that higher-income households may be better able to convert 401(k) eligibility into actual asset accumulation because they face fewer liquidity constraints and have more disposable income available for retirement saving.

Overall, this lab demonstrates how causal machine learning can support policy evaluation in household finance. The results highlight both the promise and the limitation of retirement savings policy: expanding eligibility may raise financial assets, but the size of the effect can differ substantially across income groups. From a policy perspective, this suggests that 401(k) access may need to be paired with additional support, such as matching contributions or automatic enrollment, to generate stronger savings gains for lower-income households.
