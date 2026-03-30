# The Polynomial Trap: Bias-Variance Tradeoff

## Objective
Demonstrate the bias-variance tradeoff in predictive modeling by comparing polynomial regressions of increasing complexity, using both synthetic sine-wave data and real housing data, and applying cross-validation to select models that generalize well to unseen observations.

## Dataset
This notebook uses two datasets:

- **Synthetic sine-wave data**
  - Training set: 50 observations
  - Test set: 200 observations
  - Data generating process: \( y = \sin(2\pi x) + \epsilon \)
  - Purpose: visualize underfitting, overfitting, and the complexity curve in a controlled setting where the true function is known

- **Ames Housing dataset**
  - 1,460 observations
  - 80 features
  - Purpose: apply bias-variance concepts to a realistic prediction problem and compare a high-dimensional “kitchen-sink” model against a simpler reduced-feature specification

## Tools
- **Python**
- **NumPy**
- **scikit-learn**
  - `PolynomialFeatures`
  - `LinearRegression`
  - `cross_val_score`
- **matplotlib**

## Methodology
- Generated noisy synthetic data from a known sine-wave function to study model complexity in a controlled environment
- Fit polynomial regression models from low to high degree and visualized how the fitted curves changed as complexity increased
- Calculated **training RMSE** and **test RMSE** across polynomial degrees to build a **complexity curve**
- Identified the model “sweet spot” where test error was minimized, balancing underfitting and overfitting
- Implemented **5-fold cross-validation** to estimate out-of-sample performance without using the test set for model selection
- Compared manual and scikit-learn cross-validation logic to verify results
- Applied the same validation framework to the **Ames Housing** dataset
- Evaluated a **kitchen-sink model** using all numeric predictors against a **simple model** using the five features most correlated with `SalePrice`
- Compared models using both **training \(R^2\)** and **cross-validated RMSE** to distinguish fit from generalization

## Key Findings
- For the synthetic sine-wave problem, **polynomial degrees 3–5** provided the best predictive performance
- Low-degree models had high bias and failed to capture the nonlinear signal, while very high-degree models overfit the noise
- The **complexity curve** clearly showed that training error alone is misleading: it kept falling as degree increased, even when test error worsened
- **5-fold cross-validation** successfully selected the same degree range as the true test-optimal model, showing how CV can recover the best complexity level in practice
- On the Ames Housing data, the **5-feature model outperformed the kitchen-sink model in cross-validated RMSE**, despite having a lower training \(R^2\)
- This result reinforced the main lesson of the notebook: the best deployment model is the one that generalizes best, not the one that fits the training data most aggressively

## Why This Project Matters
This notebook shows how statistical learning theory translates into real model-selection decisions. Rather than treating overfitting as an abstract concept, the analysis makes it visible through fitted curves, error decomposition, and cross-validation. The project reflects a practical forecasting mindset: evaluate models based on **out-of-sample performance**, quantify the **generalization gap**, and choose the specification that is most reliable for new data.

## Takeaway
The central lesson of this project is that **model complexity must be disciplined by validation**. In both synthetic and real-world settings, simpler models can outperform more flexible alternatives when judged by unseen-data accuracy. This is the core of the bias-variance tradeoff and a foundational principle for predictive modeling in data science and economics analytics.
