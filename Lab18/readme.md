# Fraud Detection Model Evaluation under Capacity Constraints

## Overview
This project evaluates a fraud detection classifier in a highly imbalanced credit card transaction dataset. The goal is not just to measure accuracy, but to assess whether the model is useful for real fraud operations where the investigation team has limited daily capacity.

## Objective
The main objective of this lab was to show why standard accuracy is misleading in rare-event classification and to replace it with more meaningful fraud-detection metrics such as Precision, Recall, F1, ROC, and Precision-Recall analysis. The assignment also introduced a real business constraint by limiting the fraud team to 500 investigations per day.

## Methods
- Loaded the credit card transaction dataset
- Prepared features by dropping `Time`, scaling `Amount`, and separating `X` and `y`
- Split the data into training and test sets using stratified sampling
- Fit a classification model to predict fraudulent transactions
- Evaluated performance using:
  - confusion matrix
  - precision
  - recall
  - F1 score
  - ROC curve
  - Precision-Recall curve
- Tested different classification thresholds to study the precision-recall tradeoff
- Selected an operating threshold under a capacity constraint of 500 daily investigations

## Key Findings
This lab demonstrated the **accuracy paradox**: a model can achieve extremely high accuracy in an imbalanced dataset while still failing to identify fraud effectively. Threshold choice turned out to be a business decision rather than a purely statistical one. Under the investigation-capacity constraint, the selected threshold balanced fraud detection performance with operational feasibility.

## Business Interpretation
In fraud detection, the “best” model is not the one with the highest raw accuracy. It is the one that delivers the most useful fraud alerts within the bank’s review capacity. This project shows how model evaluation connects directly to staffing limits, risk tolerance, and the economics of investigation.

## Tools Used
- Python
- pandas
- numpy
- matplotlib
- scikit-learn

## Files
- `creditcard.csv`
- `lab_18_model_evaluation.ipynb`

## Takeaway
Model evaluation is where machine learning meets decision-making. In an imbalanced fraud setting, metrics like Recall and Precision — combined with threshold tuning under real-world constraints — matter much more than headline accuracy.
