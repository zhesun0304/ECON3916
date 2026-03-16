# Data Wrangling & Engineering Pipeline

## Overview
This project focuses on transforming a chaotic, enterprise-style dataset into a structurally valid input for econometric modeling. Using `messy_hr_economics.csv`, I applied a sequence of diagnostic and feature-engineering steps designed to identify missingness patterns, repair incomplete variables, and encode categorical information in a way that preserves interpretability while avoiding failures in linear modeling.

## Objective
The objective of this lab was to engineer structurally sound features and resolve non-random missingness so that a messy real-world dataset could be converted into a reliable matrix for econometric estimation.

## Methodology
This workflow was implemented in Python using `pandas`, `statsmodels`, `missingno`, and `category_encoders`.

### Technical approach
- **Diagnosed missingness visually**
  - Used missing-data forensics to inspect the structure of null values rather than relying only on text-based summaries.
  - Identified aligned missingness patterns across variables, indicating that some missing values followed a structured mechanism consistent with **Missing at Random (MAR)**.

- **Applied conditional imputation**
  - Imputed missing values in key compensation variables using grouped summary statistics rather than blunt global replacements.
  - Used department-level median imputation to preserve within-group structure and reduce distortion of the salary distribution.

- **Demonstrated the Dummy Variable Trap**
  - Generated full dummy encodings for categorical variables to expose the risk of perfect multicollinearity in regression design matrices.
  - Showed how including all category indicators alongside an intercept leads to linear dependence and unstable estimation.

- **Escaped perfect multicollinearity**
  - Rebuilt the design matrix using a dropped reference category (`k-1` encoding), restoring a valid regression specification.
  - Preserved interpretability by establishing an explicit baseline group for comparison.

- **Compressed high-cardinality categorical data**
  - Applied **Target Encoding** to the high-cardinality `office_zip` variable.
  - Converted hundreds of geographic categories into a single continuous signal tied to the outcome variable, avoiding the dimensional explosion of naive one-hot encoding.

## Key Findings
The lab successfully mapped structured missingness patterns in the dataset and showed that the missing data mechanism was not purely random. Conditional imputation allowed missing salary information to be repaired in a way that respected organizational structure rather than flattening meaningful variation.

The analysis also demonstrated how careless categorical encoding can break the linear algebra of regression through perfect multicollinearity. By dropping a reference class, I avoided the **Dummy Variable Trap** and restored a valid design matrix. Finally, Target Encoding provided an efficient solution to high-cardinality geographic data, compressing location information into a modeling-ready feature without sacrificing signal.

## Why This Project Matters
In applied econometrics and data science, poor data preparation can invalidate an entire modeling pipeline before estimation even begins. This project demonstrates that rigorous modeling starts with structural engineering: understanding how data is missing, how variables should be encoded, and how to preserve identification while preparing features for analysis.

Rather than treating data cleaning as a routine preprocessing step, this lab frames it as a core part of empirical design. That perspective is essential in real-world settings where messy enterprise data, not clean benchmark datasets, is the norm.
