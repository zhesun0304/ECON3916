# Architecting the Prediction Engine

## Objective
Built a multivariate OLS-based hedonic pricing model to forecast residential property values and evaluate predictive performance in dollar terms using Root Mean Squared Error (RMSE).

## Methodology
- Ingested and inspected the Zillow ZHVI 2026 Micro Dataset to understand the scale, dispersion, and market structure of the target variable, **Home_Value**.
- Specified a multivariate Ordinary Least Squares model using the **statsmodels Patsy formula API**, enabling clear and interpretable model architecture through formula-based regression design.
- Modeled housing values as a function of key structural and locational predictors, including **Square_Footage**, **Property_Age**, and **Distance_to_Transit**.
- Estimated the model parameters and reviewed diagnostic outputs such as coefficient signs, statistical significance, and overall model fit.
- Generated fitted values from the estimated model to shift the analysis from explanatory econometrics toward predictive valuation.
- Calculated **Root Mean Squared Error (RMSE)** to quantify average prediction error in **actual US Dollars**, translating model performance into an interpretable measure of financial risk.
- Evaluated the model through the lens of business decision-making, emphasizing that predictive usefulness depends not only on statistical fit, but also on the real-world magnitude of pricing error.

## Key Findings
This project successfully reframed a classical OLS regression exercise as a practical prediction engine for real estate valuation. Rather than stopping at coefficient interpretation, the analysis focused on predictive loss minimization and operational relevance. The most important result was the calculation of **RMSE in dollar terms**, which provided a direct estimate of the model’s average pricing error and therefore its potential exposure to algorithmic mispricing risk. This made the model more actionable from a tech-economics perspective, linking statistical output to real financial consequences in a modern housing market.
