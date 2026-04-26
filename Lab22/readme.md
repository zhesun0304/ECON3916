# Clustering World Economies with K-Means & PCA

## Objective

This lab used unsupervised machine learning to identify economically meaningful country groups from multidimensional development indicators, then compared those algorithmic clusters against the World Bank’s official income classifications.

## Methodology

- Downloaded 10 World Bank development indicators for approximately 160 countries using `wbgapi`, including GDP per capita, life expectancy, infant mortality, primary enrollment, GINI index, CO₂ emissions per capita, internet access, trade openness, unemployment, and urbanization.

- Cleaned the country-level dataset by retaining economies with sufficient indicator coverage and imputing remaining missing values using median-based imputation.

- Standardized all development indicators with `StandardScaler` so that variables measured on different scales contributed equally to the clustering process.

- Fit a K-Means clustering model with `K=4` to approximate the four major World Bank income categories: low, lower-middle, upper-middle, and high income.

- Used PCA to reduce the standardized 10-dimensional feature space into two principal components for visualization and interpretation.

- Evaluated alternative cluster counts from `K=2` through `K=10` using both the elbow method and silhouette analysis.

- Cross-tabulated the algorithmic K-Means clusters against World Bank income classifications to assess how closely the unsupervised model aligned with official income-based categories.

- Extended the same clustering pipeline to the California Housing dataset from `scikit-learn`, applying standardization, K-Means clustering, PCA visualization, and centroid interpretation to census tract-level housing and demographic features.

## Key Findings

The K-Means model produced clusters that broadly reflected global development differences, especially along dimensions such as GDP per capita, life expectancy, infant mortality, internet access, and urbanization. Countries with higher income and stronger social indicators tended to group together, while lower-income economies with weaker health and infrastructure indicators formed separate clusters.

The cross-tabulation showed that the algorithmic clusters partially aligned with World Bank income classifications, but not perfectly. This is an important result: the World Bank’s income groups are primarily based on income thresholds, while K-Means considered a broader set of development indicators. As a result, some countries were grouped differently when health, education, emissions, trade exposure, unemployment, and urbanization were included.

The elbow and silhouette analysis suggested that the optimal number of clusters was **[FILL IN YOUR BEST K]**. If the silhouette score favored a smaller K, this indicates that broader development categories were more clearly separated. If K=4 performed reasonably well, it supports the interpretation that the data roughly mirrors the World Bank’s four income classifications while still revealing multidimensional differences within those groups.

The California Housing extension showed that the same unsupervised learning pipeline can be adapted from international development analysis to local housing-market segmentation. Census tracts clustered into groups that could be interpreted using income, housing value, household size, occupancy, and geographic location. These clusters can be labeled with economically meaningful categories such as higher-income expensive tracts, lower-income dense tracts, middle-income suburban tracts, or sparse/rural housing markets.

Overall, this lab demonstrated how K-Means and PCA can transform high-dimensional socioeconomic data into interpretable clusters. From a policy and analytics perspective, the exercise highlights both the value and the limitation of unsupervised learning: it can reveal hidden structure in development data, but the resulting clusters require careful economic interpretation rather than mechanical acceptance.
