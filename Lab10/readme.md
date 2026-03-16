# Causality, Spurious Regression & Structural Forensics

## Overview
This project examines how spurious correlation and multicollinearity can distort inference in macroeconomic time-series data. Using live data from the Federal Reserve Economic Data (FRED) API, I analyzed a focused set of macro indicators to show how raw level variables often appear strongly correlated simply because they share common time trends rather than meaningful structural relationships.

## Objective
The objective of this lab was to demonstrate why correlation in trending macroeconomic data can be misleading, and how proper diagnostics and transformations are necessary to recover more credible economic relationships.

## Methodology
Using Python, `pandas`, `seaborn`, and `statsmodels`, I built a workflow to diagnose and repair the “everything is correlated” problem in macroeconomic data. First, I visualized the raw correlation structure across CPI, unemployment, the federal funds rate, industrial production, and M2, highlighting how trend-driven variables can create misleadingly strong associations. I then applied **Variance Inflation Factor (VIF)** diagnostics to quantify multicollinearity and identify redundancy among predictors.

To address the underlying non-stationarity, I transformed key trending variables into **Year-over-Year (YoY) growth rates**, which reduced spurious co-movement and produced a more structurally meaningful correlation matrix. Finally, I used **Directed Acyclic Graphs (DAGs)** to formalize causal assumptions and distinguish direct causal channels from shared responses to broader macroeconomic forces. Together, these steps framed the analysis not as a search for high correlations, but as an exercise in structural economic reasoning.

## Why This Project Matters
In applied economics and data science, raw correlations in observational macro data can easily produce false narratives. This project demonstrates the importance of combining statistical diagnostics, transformations, and causal logic before drawing conclusions from time-series relationships.
