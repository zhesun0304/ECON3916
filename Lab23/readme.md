# FedSpeak Analysis — NLP on FOMC Minutes

## Objective

This lab applies natural language processing and unsupervised machine learning to analyze how Federal Reserve communication changes across macroeconomic regimes.

## Methodology

- Loaded and preprocessed FOMC meeting minutes by cleaning text, tokenizing, lemmatizing, and removing stop words.
- Built a TF-IDF document-term matrix using unigrams and bigrams to represent central-bank language numerically.
- Computed simplified Loughran-McDonald sentiment measures, including net sentiment and uncertainty.
- Visualized sentiment and uncertainty trends across more than two decades of FOMC communication.
- Reduced the TF-IDF matrix with TruncatedSVD and clustered FOMC documents using K-Means.
- Projected documents into two dimensions to visualize language-based clusters.
- Compared sentiment patterns before and after March 2020 to evaluate changes in Fed communication after the COVID-19 shock.

## Key Findings

The TF-IDF model captured recurring language patterns in FOMC minutes, while the Loughran-McDonald sentiment scores translated policy communication into measurable indicators of tone and uncertainty. K-Means clustering separated the documents into distinct language regimes, suggesting that monetary-policy communication changes across different macroeconomic environments. The pre/post-COVID comparison showed how Federal Reserve language shifted after the pandemic shock, with the potential for more negative or uncertain wording during periods of economic disruption, inflation pressure, and policy tightening.

## Economic Interpretation

This lab demonstrates how NLP can be used as an economic measurement tool. Instead of treating FOMC minutes as qualitative background information, the project converts policy language into structured data that can be compared across time. From a tech-economics perspective, this approach shows how text data can help identify shifts in expectations, uncertainty, and institutional communication during major economic events.
