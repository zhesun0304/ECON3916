# Tree-Based Models — Random Forests

## Objective
This lab evaluates how tree-based machine learning models improve predictive performance relative to linear baselines by modeling non-linear relationships, interaction effects, and complex feature importance patterns in California housing data.

## Methodology
- Compared **Single Decision Tree**, **Ridge Regression**, and **Random Forest** on the California Housing dataset (**20,640 observations, 8 predictors**).
- Measured out-of-sample model quality using **RMSE** and **R²** on a held-out test set.
- Tuned Random Forest hyperparameters with **GridSearchCV**, searching over:
  - `n_estimators`
  - `max_depth`
  - `max_features`
- Evaluated the tuned forest against the untuned benchmark to assess generalization gains.
- Extracted and compared two feature importance measures:
  - **MDI (Mean Decrease in Impurity)** from the training process
  - **Permutation importance** on the test set
- Built a **Random Forest classifier** and compared its **AUC** against logistic regression.
- Created an interactive dashboard with **Plotly** and **ipywidgets** to explore Random Forest behavior dynamically.

## Key Findings
- The **Single Tree** achieved perfect in-sample fit but much weaker test performance, indicating high variance and overfitting.
- **Ridge Regression** produced more stable but lower predictive performance, suggesting that linear structure alone misses important non-linear housing patterns.
- **Random Forest** delivered the strongest overall results, achieving **Test R² = 0.8051**, compared with **Ridge Test R² = 0.5759**.
- After tuning, the Random Forest improved further to **Test R² = 0.8090** and **Test RMSE = 0.5003**.
- Feature importance analysis showed strong agreement that **median income (`MedInc`)** is the dominant predictor, while also highlighting differences between impurity-based and permutation-based rankings.
- In the classification extension, **Random Forest** outperformed **Logistic Regression** on discrimination accuracy, with **AUC = 0.9609** versus **0.9060**.

## Interpretation
This lab shows why tree-based ensembles are often superior when the data-generating process is non-linear. Random Forest reduced the variance problem of a single tree while preserving flexibility that linear models cannot capture, placing it closer to the “sweet spot” on the bias-variance tradeoff.

## How to Run
1. Open the notebook in Jupyter or Google Colab.
2. Run all cells in order.
3. Review the model comparison tables, tuned Random Forest output, feature importance charts, and interactive dashboard.
4. Save generated figures into the `figures/` folder if needed for GitHub submission.

## Files
- `lab_ch19_guided.ipynb`
- `README.md`
- `figures/` (for saved plots and screenshots)

## Tools Used
Python, pandas, numpy, scikit-learn, matplotlib, plotly, ipywidgets

## Takeaway
Random Forest provided the best balance of predictive accuracy and generalization in this lab, demonstrating how ensemble methods can outperform both linear models and single trees in applied economic and housing-price prediction tasks.
