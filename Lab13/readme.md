# The Architecture of Dimensionality: Hedonic Pricing & the FWL Theorem

## Objective
Executed a multivariate hedonic pricing model to estimate residential sale values while formally demonstrating, through the Frisch-Waugh-Lovell theorem, how regression algorithms isolate a variable’s ceteris paribus effect by partialling out confounding variation.

## Methodology
- Loaded a 2026 California real estate dataset containing **Sale_Price**, **Property_Age**, and **Distance_to_Tech_Hub**.
- Estimated a **naive bivariate OLS model** regressing sale price on property age alone to assess the direction and magnitude of the uncontrolled relationship.
- Expanded the specification into a **multivariate hedonic pricing model** by adding distance to tech hubs as a control variable, allowing the regression to separate structural housing characteristics from locational advantage.
- Compared the naive and controlled age coefficients to diagnose the presence and direction of **omitted variable bias (OVB)**.
- Manually executed the **Frisch-Waugh-Lovell (FWL) theorem** in three steps:
  - Regressed **Sale_Price** on **Distance_to_Tech_Hub** and extracted the price residuals.
  - Regressed **Property_Age** on **Distance_to_Tech_Hub** and extracted the age residuals.
  - Regressed the price residuals on the age residuals, removing the intercept for exact algebraic equivalence.
- Verified that the coefficient from the residual-on-residual regression matched the **Property_Age** coefficient from the full multivariate model to multiple decimal places.
- Interpreted the workflow as a computational proof of how modern statistical systems remove shared covariance to recover an uncorrelated signal of interest.

## Key Findings
This project showed that a naive pricing algorithm can generate seriously misleading inferences when an important locational confounder is omitted. In this market, **Property_Age** and **Distance_to_Tech_Hub** were correlated, meaning that a simple regression incorrectly assigned part of the value of geographic proximity to the age of the home itself. Once distance to tech hubs was included, the coefficient on property age shifted materially, revealing the underlying omitted variable bias embedded in the naive specification.

The manual FWL procedure provided the formal correction mechanism. By residualizing both **Sale_Price** and **Property_Age** with respect to **Distance_to_Tech_Hub**, the analysis stripped away their shared variance and isolated the pure partial effect of age. The resulting residual regression reproduced the exact multivariate coefficient, offering a direct mathematical proof of algorithmic **ceteris paribus**. From a tech-economics perspective, this demonstrates why high-dimensional modeling is not just a statistical refinement, but a necessary safeguard against systematic mispricing in confounded real-world markets.
