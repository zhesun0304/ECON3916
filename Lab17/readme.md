# Yield Curve Recession Forecasting with Logistic Regression

## Overview
This project builds a logistic regression model to estimate the probability of an NBER recession within 12 months using the Treasury yield spread. The analysis replicates the core logic behind the New York Fed recession-probability framework and then extends the model by adding the lagged unemployment rate as a second predictor.

## Methods
- Collected monthly macroeconomic data from FRED
- Constructed a binary recession indicator based on NBER recession periods
- Fit a one-predictor logistic regression using the lagged yield spread
- Converted coefficients into odds ratios for interpretation
- Generated a recession-probability time series and compared it to historical recessions
- Extended the model with `UNRATE_lag12`
- Evaluated model performance with time-series cross-validation

## Key Findings
The one-predictor model showed that a more inverted yield curve is associated with higher recession risk. In the two-predictor model, the yield spread remained the stronger signal, while lagged unemployment was not statistically significant once the spread was included. This suggests that the yield curve still contains the main forward-looking information in this specification.

## Tools
Python, pandas, numpy, matplotlib, statsmodels, scikit-learn, fredapi

## Takeaway
This notebook shows how logistic regression can turn a macro-financial signal into an interpretable probability forecast, while also illustrating the limits of probabilistic prediction in real time.
