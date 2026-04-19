# Predictive Architecture for Hospital Procedure Pricing

## Objective
This project builds and audits an econometric prediction pipeline for hospital procedure costs using clinical telemetry, patient vital signs, and high-cardinality diagnosis data. The goal was not only to fit an Ordinary Least Squares model, but also to test whether the model is statistically defensible for real-world pricing decisions in a healthcare setting.

## Project Overview
The assignment was structured as a full modeling workflow:

- diagnose spurious correlations using causal reasoning
- audit multicollinearity with Variance Inflation Factors
- investigate structured missingness in telemetry data
- handle a high-cardinality diagnosis variable without falling into the dummy variable trap
- fit an OLS pricing model using Patsy formulas
- quantify prediction risk in absolute US dollars using RMSE
- evaluate model reliability through residual diagnostics
- formally test for heteroscedasticity with White’s Lagrange Multiplier test
- use the P.R.I.M.E. prompting framework to direct generative AI for advanced econometric testing

## Data
Two datasets were used in the analysis:

- **OmniCare_Clinical_Vitals.csv**
  - patient physiological variables such as height, weight, BMI, systolic blood pressure, and diastolic blood pressure
- **OmniCare_Telemetry_Data.csv**
  - remote monitoring and pricing variables including diagnosis code, clinic capacity, time of day, insurance plan indicator, admission rate, continuous heart rate, and procedure cost

These files were merged by `Patient_ID` to create the final analytical dataset.

## Methodology

### 1. Causal topology and confounding
A statistically significant positive relationship was observed between `High_Deductible_Insurance_Plan` and `Inpatient_Admission_Rate`. Rather than treating this as causal, the analysis used a Directed Acyclic Graph to show how an omitted confounder such as baseline wealth or systemic poverty can create a spurious fork structure. This demonstrated why a naïve regression coefficient can be biased by omitted-variable contamination.

### 2. Multicollinearity forensics
Variance Inflation Factors were calculated for the continuous physiological features. The audit showed severe redundancy among `Weight_kg`, `Height_cm`, and `BMI`. Because BMI is mechanically derived from weight and height, it was removed to improve structural stability. Recomputed VIF values confirmed a more stable feature set after the adjustment.

### 3. Missingness architecture
A missingness matrix was generated for the telemetry data using `missingno`. The analysis treated the missingness in `Continuous_Heart_Rate` as conceptually non-random under a realistic policy scenario in which low-income patients avoid transmitting wearable data because of data-plan costs. This highlighted why simple mean imputation would distort variance, weaken covariance structure, and damage inferential validity.

### 4. Escaping the dummy variable trap
The variable `Primary_Diagnosis_Code` contains hundreds of distinct medical strings. A full one-hot encoding strategy would create a singular design matrix if used alongside an intercept because the sum of all exhaustive diagnosis dummies equals one. This is a direct matrix-rank failure that breaks classical OLS inversion.

### 5. Target encoding
To preserve information while avoiding the curse of dimensionality, the diagnosis variable was encoded with a `TargetEncoder`, mapping each diagnosis code to the historical mean of `Procedure_Cost_USD`. This transformed a large sparse categorical space into a usable continuous predictor.

### 6. OLS prediction engine
The final OLS model regressed `Procedure_Cost_USD` on:

- target-encoded diagnosis
- clinic capacity percentage
- time-of-day index
- sanitized vital signs:
  - `Weight_kg`
  - `Height_cm`
  - `Systolic_BP`
  - `Diastolic_BP`

This model was estimated using `statsmodels.formula.api` with a Patsy-style formula.

### 7. Financial loss quantification
Model error was evaluated with Root Mean Squared Error in US dollars rather than relying only on R-squared. This made the predictive risk interpretable in operational terms. The exercise emphasized that even a moderate statistical error can become economically dangerous when deployed in hospital pricing.

### 8. Residual diagnostics and heteroscedasticity testing
Residuals were plotted against fitted values to visually assess whether prediction error widened at higher pricing levels. White’s Lagrange Multiplier test was then applied as a formal heteroscedasticity diagnostic. The test strongly rejected the null of homoscedasticity, indicating that the OLS model’s error variance is not constant.

### 9. AI context engineering
The assignment also required the use of the P.R.I.M.E. prompting framework to direct an LLM to generate code for White’s heteroscedasticity test. This demonstrated how generative AI can be used as a controlled productivity tool in an applied econometrics workflow when prompt design is explicit and technically grounded.

## Key Findings

- A correlation between insurance plan type and inpatient admissions can be entirely spurious when confounding is ignored.
- Multicollinearity was severe before sanitizing the physiological feature set.
- BMI was the most redundant vital-sign variable and was removed.
- Missing heart-rate telemetry should not be treated as random under a socioeconomic transmission-cost mechanism.
- One-hot encoding a high-cardinality diagnosis field would create a singular OLS design matrix.
- Target encoding provided a tractable low-dimensional representation of diagnosis information.
- RMSE translated model error into real-dollar hospital pricing risk.
- Residual diagnostics and White’s test both indicated heteroscedasticity, meaning the model is less reliable at higher predicted procedure-cost levels.

## Why This Project Matters
This project shows that building a predictive model is only one part of econometric decision-making. In a healthcare pricing context, a model must also survive causal scrutiny, matrix diagnostics, missing-data analysis, and error-risk evaluation. A model that looks statistically useful at first glance may still be unsafe to deploy if its coefficients are biased, its features are structurally unstable, or its residual variance explodes in the highest-cost cases.

## Tools Used
- Python
- pandas
- numpy
- matplotlib
- seaborn
- statsmodels
- missingno
- category_encoders
- networkx
- Google Colab

## Files
- `The_Predictive_Architecture.ipynb`
- `OmniCare_Clinical_Vitals.csv`
- `OmniCare_Telemetry_Data.csv`

## Author Note
This notebook was designed as an applied econometrics and predictive analytics exercise, combining causal reasoning, statistical diagnostics, machine-learning-style feature engineering, and AI-assisted workflow design in a single hospital pricing case study.
