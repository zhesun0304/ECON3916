# Assignment 5: The Sovereign Risk Engine

## Regularization, Classification, and Model Evaluation for Macroeconomic Early Warning Systems

This project builds a macroeconomic early warning system for identifying countries at elevated risk of a growth crisis. The setting is framed as an IMF-style forecasting task, where the goal is not only to predict GDP per capita growth, but also to classify whether a country may experience sustained negative growth.

The notebook uses live World Bank Development Indicator data, regularized regression, logistic regression, and classification evaluation tools to compare different modeling strategies under realistic operational constraints.

---

## Project Overview

The original forecasting problem is based on a high-dimensional macroeconomic dataset with many World Bank indicators and a relatively limited number of countries. This creates a strong risk of overfitting when using a standard OLS regression model.

The project addresses this issue by:

- Diagnosing OLS overfitting using train/test performance.
- Applying Ridge and Lasso regularization.
- Visualizing the Lasso coefficient path.
- Building a binary crisis classifier using logistic regression.
- Evaluating the classifier using accuracy, recall, precision, ROC curves, precision-recall curves, and confusion matrices.
- Choosing classification thresholds based on real IMF-style operational constraints.
- Extending the analysis with AI-assisted bootstrap stability and cost-sensitive threshold optimization.

---

## Data Source

The dataset is downloaded directly from the World Bank API using `wbgapi`.

The analysis uses World Development Indicators for approximately 150 countries across the 2013–2019 period. The indicators are collapsed into country-level averages.

The continuous outcome is:

```text
gdp_growth_pc
